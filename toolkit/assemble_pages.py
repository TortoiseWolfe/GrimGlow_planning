#!/usr/bin/env python3
"""Assemble GrimGlow comic pages from generated panel PNGs.

Composites panel art into full pages with speech balloons and caption
boxes, using the same layout grid and dialogue data as the wireframes.

Usage:
    python3 toolkit/assemble_pages.py --issue 1                    # All pages
    python3 toolkit/assemble_pages.py --issue 1 --page 1           # Single page
    python3 toolkit/assemble_pages.py --issue 1 --page 1 --end-page 5
    python3 toolkit/assemble_pages.py --issue 1 --dry-run          # Preview layout
    python3 toolkit/assemble_pages.py --issue 1 --pdf              # Also make PDF
"""

import argparse
import glob
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = REPO_ROOT / "comic" / "scripts"
DEFAULT_PANEL_DIR = REPO_ROOT / "comfyui-data" / "ComfyUI" / "output"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "comic" / "assembled"

sys.path.insert(0, str(REPO_ROOT / "comic" / "wireframes"))
from generate_wireframes import (  # noqa: E402
    parse_script,
    panels_to_grid,
    CHAR_COLORS,
    _wrap_text,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DEFAULT_CANVAS = (2480, 3508)  # A4 at 300dpi
MARGIN = 70
GUTTER = 29
TITLE_RESERVE = 88
BG_COLOR = (255, 255, 255)
PANEL_BORDER_WIDTH = 4
PANEL_BORDER_COLOR = (42, 42, 42)

CAPTION_FILL = (245, 236, 216, 235)
CAPTION_OUTLINE = (200, 184, 152, 255)
CAPTION_TEXT = (90, 74, 48, 255)
SPEECH_FILL = (255, 255, 255, 235)
DIALOGUE_TEXT = (51, 51, 51, 255)
BALLOON_RADIUS = 15
BALLOON_OUTLINE_W = 3
TAIL_SIZE = 20

FONT_PATHS = {
    "bold": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "regular": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "caption": "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def find_script(issue_num: int) -> Path:
    pattern = str(SCRIPT_DIR / f"Issue{issue_num:02d}_*_Script.md")
    matches = glob.glob(pattern)
    if not matches:
        print(f"ERROR: No script found for Issue {issue_num}")
        sys.exit(1)
    return Path(matches[0])


def _hex_to_rgba(hex_color: str, alpha: int = 255) -> tuple:
    h = hex_color.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), alpha)


def _tinted_fill(hex_color: str, alpha: int = 235) -> tuple:
    """Create a light tinted fill from a character color (white + 15% color)."""
    r, g, b, _ = _hex_to_rgba(hex_color)
    mix = 0.15
    return (round(255 * (1 - mix) + r * mix),
            round(255 * (1 - mix) + g * mix),
            round(255 * (1 - mix) + b * mix),
            alpha)


def _strip_markup(text: str) -> str:
    """Strip markdown bold/italic markers from dialogue text."""
    import re
    text = re.sub(r'\*{1,2}', '', text)
    return text.strip()


def load_fonts(font_dir: str | None = None, base_size: int = 28) -> dict:
    paths = dict(FONT_PATHS)
    if font_dir:
        d = Path(font_dir)
        for key, name in [("bold", "bold.ttf"), ("regular", "regular.ttf"), ("caption", "caption.ttf")]:
            p = d / name
            if p.exists():
                paths[key] = str(p)

    return {
        "bold": ImageFont.truetype(paths["bold"], base_size),
        "regular": ImageFont.truetype(paths["regular"], round(base_size * 0.85)),
        "caption": ImageFont.truetype(paths["caption"], round(base_size * 0.8)),
        "page_num": ImageFont.truetype(paths["bold"], round(base_size * 1.4)),
        "placeholder": ImageFont.truetype(paths["bold"], round(base_size * 0.7)),
        "base_size": base_size,
    }


# ---------------------------------------------------------------------------
# Panel loading and fitting
# ---------------------------------------------------------------------------

def load_panel(panel_dir: Path, page_num: int, panel_num: int) -> Image.Image | None:
    pattern = str(panel_dir / f"page{page_num:02d}_panel{panel_num:02d}_*.png")
    matches = glob.glob(pattern)
    if not matches:
        return None
    return Image.open(matches[0]).convert("RGB")


def make_placeholder(width: int, height: int, fonts: dict) -> Image.Image:
    img = Image.new("RGB", (width, height), (180, 180, 180))
    draw = ImageDraw.Draw(img)
    text = "MISSING PANEL"
    bbox = draw.textbbox((0, 0), text, font=fonts["placeholder"])
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((width - tw) // 2, (height - th) // 2), text,
              font=fonts["placeholder"], fill=(100, 100, 100))
    return img


def fit_to_cell(img: Image.Image, target_w: int, target_h: int) -> Image.Image:
    """Center-crop and resize to exactly fill target (cover mode)."""
    src_w, src_h = img.size
    target_aspect = target_w / target_h
    src_aspect = src_w / src_h

    if src_aspect > target_aspect:
        # Source wider — scale by height, crop width
        scale = target_h / src_h
        new_w = round(src_w * scale)
        resized = img.resize((new_w, target_h), Image.LANCZOS)
        left = (new_w - target_w) // 2
        return resized.crop((left, 0, left + target_w, target_h))
    else:
        # Source taller — scale by width, crop height
        scale = target_w / src_w
        new_h = round(src_h * scale)
        resized = img.resize((target_w, new_h), Image.LANCZOS)
        top = (new_h - target_h) // 2
        return resized.crop((0, top, target_w, top + target_h))


# ---------------------------------------------------------------------------
# Speech balloon rendering
# ---------------------------------------------------------------------------

def draw_speech_bubble(
    draw: ImageDraw.ImageDraw,
    fonts: dict,
    cell_x: int, cell_y: int, cell_w: int,
    y_pos: int,
    speaker: str,
    text: str,
    color_hex: str,
    align_right: bool = False,
) -> int:
    """Draw a speech bubble. Returns total height consumed."""
    padding = 18
    color = _hex_to_rgba(color_hex)
    line_h = fonts["base_size"] + 4

    # Measure and wrap
    avg_cw = fonts["regular"].getlength("x")
    max_chars = max(10, int((cell_w - padding * 4) / avg_cw))
    lines = _wrap_text(text, max_chars)

    # Measure actual widths
    speaker_w = draw.textbbox((0, 0), speaker, font=fonts["bold"])[2]
    max_line_w = max(draw.textbbox((0, 0), ln, font=fonts["regular"])[2] for ln in lines)

    bubble_w = min(cell_w - padding * 2, int(max(speaker_w, max_line_w) + padding * 2))
    bubble_h = (len(lines) + 1) * line_h + padding * 2

    # Position
    if align_right and bubble_w < cell_w - padding * 3:
        bx = cell_x + cell_w - padding - bubble_w
    else:
        bx = cell_x + padding
    by = y_pos

    # Tinted fill from character color
    fill = _tinted_fill(color_hex)

    # Bubble
    draw.rounded_rectangle(
        [bx, by, bx + bubble_w, by + bubble_h],
        radius=BALLOON_RADIUS,
        fill=fill,
        outline=color,
        width=BALLOON_OUTLINE_W,
    )

    # Tail — points toward the speaker (left for left-aligned, right for right-aligned)
    tail_y = by + bubble_h
    if align_right:
        tail_x = bx + int(bubble_w * 0.7)
        tail_pts = [(tail_x, tail_y), (tail_x + TAIL_SIZE, tail_y),
                    (tail_x + TAIL_SIZE + 8, tail_y + TAIL_SIZE)]
    else:
        tail_x = bx + int(bubble_w * 0.3)
        tail_pts = [(tail_x, tail_y), (tail_x + TAIL_SIZE, tail_y),
                    (tail_x - 8, tail_y + TAIL_SIZE)]
    draw.polygon(tail_pts, fill=fill, outline=color)
    # Cover seam
    draw.line(
        [(tail_x - 1, tail_y), (tail_x + TAIL_SIZE + 1, tail_y)],
        fill=fill, width=BALLOON_OUTLINE_W + 2,
    )

    # Speaker name
    ty = by + padding
    draw.text((bx + padding, ty), speaker, font=fonts["bold"], fill=color)

    # Dialogue text
    ty += line_h
    for ln in lines:
        draw.text((bx + padding, ty), ln, font=fonts["regular"], fill=DIALOGUE_TEXT)
        ty += line_h

    return bubble_h + TAIL_SIZE


def draw_caption_box(
    draw: ImageDraw.ImageDraw,
    fonts: dict,
    x: int, y: int, max_w: int,
    text: str,
) -> int:
    """Draw a caption box. Returns total height consumed."""
    padding = 18
    line_h = round(fonts["base_size"] * 0.85) + 4

    avg_cw = fonts["caption"].getlength("x")
    max_chars = max(10, int((max_w - padding * 4) / avg_cw))
    lines = _wrap_text(text, max_chars)

    max_line_w = max(draw.textbbox((0, 0), ln, font=fonts["caption"])[2] for ln in lines)
    cap_w = min(int(max_w * 0.8), int(max_line_w + padding * 2))
    cap_h = len(lines) * line_h + padding * 2

    draw.rectangle(
        [x, y, x + cap_w, y + cap_h],
        fill=CAPTION_FILL,
        outline=CAPTION_OUTLINE,
        width=2,
    )

    ty = y + padding
    for ln in lines:
        draw.text((x + padding, ty), ln, font=fonts["caption"], fill=CAPTION_TEXT)
        ty += line_h

    return cap_h + 6


# ---------------------------------------------------------------------------
# Page assembly
# ---------------------------------------------------------------------------

def assemble_page(
    page_data: dict,
    panel_dir: Path,
    canvas_size: tuple[int, int],
    fonts: dict,
) -> Image.Image:
    """Assemble one complete comic page."""
    canvas = Image.new("RGB", canvas_size, BG_COLOR)
    panels = page_data["panels"]

    # Draw area
    draw_x = MARGIN
    draw_y = MARGIN + TITLE_RESERVE
    draw_w = canvas_size[0] - 2 * MARGIN
    draw_h = canvas_size[1] - 2 * MARGIN - TITLE_RESERVE

    # Grid layout
    grid = panels_to_grid(panels)
    cells = [cell for row in grid for cell in row]

    # Draw page number
    canvas_draw = ImageDraw.Draw(canvas)
    page_label = f"PAGE {page_data['page_num']}"
    canvas_draw.text((MARGIN, MARGIN + 10), page_label,
                     font=fonts["page_num"], fill=(100, 100, 100))

    # Paste panels
    cell_rects = []  # Store pixel rects for dialogue overlay
    for idx, cell in enumerate(cells):
        is_inset = cell.get("inset", False)

        cx = draw_x + cell["x"] * draw_w
        cy = draw_y + cell["y"] * draw_h
        cw = cell["w"] * draw_w
        ch = cell["h"] * draw_h

        # Gutter inset
        if not is_inset and len(cells) > 1:
            cx += GUTTER / 2
            cy += GUTTER / 2
            cw -= GUTTER
            ch -= GUTTER

        target_w = max(1, round(cw))
        target_h = max(1, round(ch))
        paste_x = round(cx)
        paste_y = round(cy)

        if target_w < 2 or target_h < 2:
            cell_rects.append(None)
            continue

        # Load panel
        if idx < len(panels):
            img = load_panel(panel_dir, page_data["page_num"], panels[idx]["num"])
            if img is None:
                img = make_placeholder(target_w, target_h, fonts)
            else:
                img = fit_to_cell(img, target_w, target_h)
        else:
            img = make_placeholder(target_w, target_h, fonts)

        canvas.paste(img, (paste_x, paste_y))

        # Panel border
        canvas_draw.rectangle(
            [paste_x, paste_y, paste_x + target_w, paste_y + target_h],
            outline=PANEL_BORDER_COLOR, width=PANEL_BORDER_WIDTH,
        )

        cell_rects.append((paste_x, paste_y, target_w, target_h))

    # Dialogue overlay (RGBA for semi-transparency)
    overlay = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)

    for idx, rect in enumerate(cell_rects):
        if rect is None or idx >= len(panels):
            continue
        panel = panels[idx]
        dialogue = panel.get("dialogue", [])
        if not dialogue:
            continue

        px, py, pw, ph = rect
        padding = 18
        y_cursor = py + padding + 4
        align_right = False

        for d in dialogue:
            if y_cursor > py + ph * 0.92:
                break

            speaker = d["speaker"]
            text = _strip_markup(d["text"])
            dtype = d["type"]

            if dtype == "caption":
                consumed = draw_caption_box(
                    overlay_draw, fonts,
                    px + padding, y_cursor, pw,
                    text,
                )
                y_cursor += consumed
            else:
                color_hex = CHAR_COLORS.get(speaker.upper(), "#999999")
                consumed = draw_speech_bubble(
                    overlay_draw, fonts,
                    px, py, pw,
                    y_cursor,
                    speaker, text, color_hex,
                    align_right,
                )
                y_cursor += consumed + 12
                align_right = not align_right

    # Composite
    canvas_rgba = canvas.convert("RGBA")
    result = Image.alpha_composite(canvas_rgba, overlay)
    return result.convert("RGB")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Assemble GrimGlow comic pages")
    parser.add_argument("--issue", type=int, required=True, help="Issue number (1-12)")
    parser.add_argument("--page", type=int, default=1, help="Start from page N")
    parser.add_argument("--end-page", type=int, default=0, help="Stop after page N (0=all)")
    parser.add_argument("--dry-run", action="store_true", help="Preview layout only")
    parser.add_argument("--pdf", action="store_true", help="Also compile PDF")
    parser.add_argument("--panel-dir", type=str, help="Override panel PNG directory")
    parser.add_argument("--output-dir", type=str, help="Override output directory")
    parser.add_argument("--font-dir", type=str, help="Custom font directory")
    parser.add_argument("--width", type=int, default=DEFAULT_CANVAS[0])
    parser.add_argument("--height", type=int, default=DEFAULT_CANVAS[1])
    args = parser.parse_args()

    script_path = find_script(args.issue)
    print(f"Script: {script_path.name}")

    pages = parse_script(script_path)
    print(f"Parsed: {len(pages)} pages")

    panel_dir = Path(args.panel_dir) if args.panel_dir else DEFAULT_PANEL_DIR / f"issue{args.issue:02d}"
    output_dir = Path(args.output_dir) if args.output_dir else DEFAULT_OUTPUT_DIR / f"Issue{args.issue:02d}"
    canvas_size = (args.width, args.height)

    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)
        fonts = load_fonts(args.font_dir)

    rendered = 0
    pdf_pages = []

    for page in pages:
        pnum = page["page_num"]
        if pnum < args.page:
            continue
        if args.end_page > 0 and pnum > args.end_page:
            continue

        grid = panels_to_grid(page["panels"])
        cells = [c for row in grid for c in row]
        panel_count = len(page["panels"])
        dialogue_count = sum(len(p.get("dialogue", [])) for p in page["panels"])

        print(f"  Page {pnum:2d}: {panel_count} panels, {len(cells)} cells, "
              f"{dialogue_count} dialogue items")

        if args.dry_run:
            for idx, panel in enumerate(page["panels"]):
                shot = panel.get("shot_abbr", "?")
                dlg = len(panel.get("dialogue", []))
                print(f"    Panel {panel['num']}: {shot:5s} dialogue={dlg}")
            rendered += 1
            continue

        img = assemble_page(page, panel_dir, canvas_size, fonts)
        out_path = output_dir / f"page{pnum:02d}.png"
        img.save(out_path, "PNG")
        print(f"    → {out_path.name}")
        rendered += 1

        if args.pdf:
            pdf_pages.append(out_path)

    print(f"\n{'Preview' if args.dry_run else 'Assembled'}: {rendered} pages")

    if args.pdf and pdf_pages and not args.dry_run:
        pdf_path = output_dir / f"Issue{args.issue:02d}.pdf"
        images = [Image.open(p) for p in pdf_pages]
        images[0].save(pdf_path, save_all=True, append_images=images[1:], resolution=300)
        for im in images:
            im.close()
        print(f"PDF: {pdf_path}")

    if not args.dry_run:
        print(f"Output: {output_dir}")


if __name__ == "__main__":
    main()
