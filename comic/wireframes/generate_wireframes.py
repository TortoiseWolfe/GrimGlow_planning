#!/usr/bin/env python3
"""Generate SVG wireframes from GrimGlow comic script Layout lines.

Parses all 12 Volume 1 script files and produces:
- Per-page wireframes (400x600px) with labeled panel rectangles
- Per-issue overview sheets (1200x900px) showing 22 thumbnail pages

Usage:
    python3 generate_wireframes.py

Re-run whenever Layout lines change — output is deterministic and idempotent.
"""

import math
import os
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent.parent / "scripts"
OUTPUT_DIR = Path(__file__).resolve().parent

# Individual page SVG dimensions
PAGE_W, PAGE_H = 800, 1200
MARGIN = 24
GUTTER = 10
DRAW_W = PAGE_W - 2 * MARGIN
DRAW_H = PAGE_H - 2 * MARGIN - 30  # reserve 30px for page title at top

# Overview SVG dimensions
OV_W, OV_H = 1600, 1400
OV_COLS, OV_ROWS = 4, 6
OV_PAD = 20
OV_TITLE_H = 40

# Colors
PANEL_FILL = "#f5f0e8"
PANEL_STROKE = "#2a2a2a"
BG_FILL = "#ffffff"
LABEL_COLOR = "#2a2a2a"
SHOT_COLOR = "#888888"
INSET_FILL = "#e8e0d0"

# Issue file mapping
ISSUES = [
    ("Issue01_Descent_Script.md", "Issue01_Descent", "Issue 1 — Descent"),
    ("Issue02_Small_World_Script.md", "Issue02_Small_World", "Issue 2 — Small World"),
    ("Issue03_The_Tinkers_Boy_Script.md", "Issue03_The_Tinkers_Boy", "Issue 3 — The Tinker's Boy"),
    ("Issue04_Useful_Giant_Script.md", "Issue04_Useful_Giant", "Issue 4 — Useful Giant"),
    ("Issue05_The_Clockmakers_Heart_Script.md", "Issue05_The_Clockmakers_Heart", "Issue 5 — The Clockmaker's Heart"),
    ("Issue06_Traces_Script.md", "Issue06_Traces", "Issue 6 — Traces"),
    ("Issue07_The_Lens_Script.md", "Issue07_The_Lens", "Issue 7 — The Lens"),
    ("Issue08_What_Luma_Found_Script.md", "Issue08_What_Luma_Found", "Issue 8 — What Luma Found"),
    ("Issue09_Sables_File_Script.md", "Issue09_Sables_File", "Issue 9 — Sable's File"),
    ("Issue10_The_Titan_Script.md", "Issue10_The_Titan", "Issue 10 — The Titan"),
    ("Issue11_Convergence_Script.md", "Issue11_Convergence", "Issue 11 — Convergence"),
    ("Issue12_The_Stories_They_Tell_Script.md", "Issue12_The_Stories_They_Tell", "Issue 12 — The Stories They Tell"),
]


# ---------------------------------------------------------------------------
# Shot abbreviation
# ---------------------------------------------------------------------------

def abbreviate_shot(shot_text: str) -> str:
    """Convert a Shot: value to a short abbreviation."""
    s = shot_text.lower()
    if "splash" in s or "full page" in s or "full-page" in s:
        return "SPLASH"
    if "pov" in s:
        return "POV"
    if "reaction" in s:
        return "RXN"
    if "establishing" in s:
        return "EST"
    if "extreme wide" in s or "ultra-wide" in s:
        return "XWIDE"
    if "extreme close" in s or "extreme tight" in s:
        return "ECU"
    if "medium close" in s:
        return "MCU"
    if "medium wide" in s:
        return "MW"
    if "dynamic" in s:
        return "DYN"
    if "close-up" in s or "close up" in s:
        return "CU"
    if "medium" in s:
        return "MED"
    if "wide" in s:
        return "WIDE"
    return ""


# ---------------------------------------------------------------------------
# Script parser
# ---------------------------------------------------------------------------

def parse_script(filepath: Path) -> list[dict]:
    """Parse a script file and return a list of page dicts.

    Each page dict has:
        page_num: int
        panel_count: int
        layout: str
        panels: list of {num, width_hint, shot, shot_abbr, dialogue, action, art_prompt}
    """
    text = filepath.read_text(encoding="utf-8")
    lines = text.split("\n")

    pages = []
    current_page = None
    current_panel = None
    in_dialogue = False
    in_art_prompt = False
    art_prompt_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Capture art prompt lines (between ```text and ```)
        if in_art_prompt:
            stripped_fence = line.strip()
            if stripped_fence == "```":
                # Closing fence — store the captured art prompt
                if current_panel is not None:
                    current_panel["art_prompt"] = "\n".join(art_prompt_lines).strip()
                in_art_prompt = False
                art_prompt_lines = []
                current_panel = None
            else:
                art_prompt_lines.append(line.rstrip())
            i += 1
            continue

        # Detect page header
        page_match = re.match(r"^### PAGE (\d+)", line)
        if page_match:
            if current_page is not None:
                pages.append(current_page)

            page_num = int(page_match.group(1))

            count_match = re.search(r"\((\d+)\s*panels?", line)
            if count_match:
                panel_count = int(count_match.group(1))
            elif "single panel" in line.lower() or "full-page splash" in line.upper() or "FULL-PAGE PANEL" in line:
                panel_count = 1
            else:
                panel_count = 0

            current_page = {
                "page_num": page_num,
                "panel_count": panel_count,
                "layout": "",
                "panels": [],
            }
            current_panel = None
            in_dialogue = False
            i += 1
            continue

        # Detect Layout line
        if current_page and line.strip().startswith("**Layout:**"):
            layout_text = line.strip().replace("**Layout:**", "").strip()
            current_page["layout"] = layout_text
            in_dialogue = False
            i += 1
            continue

        # Detect panel header
        panel_match = re.match(r"^####\s+Panel\s+(\d+)\s*[—–-]\s*(.*)", line)
        if panel_match and current_page is not None:
            panel_num = int(panel_match.group(1))
            width_hint = panel_match.group(2).strip()
            current_panel = {
                "num": panel_num,
                "width_hint": width_hint,
                "shot": "",
                "shot_abbr": "",
                "dialogue": [],   # list of {speaker, text, type}
                "action": "",
                "art_prompt": "",
            }
            current_page["panels"].append(current_panel)
            in_dialogue = False
            i += 1
            continue

        # Detect field lines within a panel
        if current_panel:
            stripped = line.strip()

            if stripped.startswith("**Shot:**"):
                current_panel["shot"] = stripped.replace("**Shot:**", "").strip()
                current_panel["shot_abbr"] = abbreviate_shot(current_panel["shot"])
                in_dialogue = False
                i += 1
                continue

            if stripped.startswith("**Action:**"):
                current_panel["action"] = stripped.replace("**Action:**", "").strip()
                in_dialogue = False
                i += 1
                continue

            if stripped.startswith("**Dialogue:**"):
                in_dialogue = True
                i += 1
                continue

            # End dialogue on next bold field or horizontal rule
            if stripped.startswith("**") and stripped.endswith("**"):
                in_dialogue = False
            if stripped.startswith("```text") or stripped.startswith("```\n") or stripped == "```":
                in_dialogue = False
                if stripped.startswith("```text"):
                    # Opening art prompt fence — start capturing
                    in_art_prompt = True
                    art_prompt_lines = []
                    i += 1
                    continue
                else:
                    current_panel = None
            if stripped == "---":
                in_dialogue = False
                current_panel = None

            # Parse dialogue lines
            if in_dialogue and stripped.startswith("- "):
                dl = stripped[2:]
                # CAPTION: *"text"*
                cap_match = re.match(r'CAPTION:\s*(.*)', dl)
                if cap_match:
                    cap_text = cap_match.group(1).strip().strip('*"').strip('"*').strip('*').strip('"')
                    current_panel["dialogue"].append({
                        "speaker": "CAPTION",
                        "text": cap_text,
                        "type": "caption",
                    })
                else:
                    # SPEAKER (qualifier): "text"  or  SPEAKER: "text"
                    spk_match = re.match(r'([A-Z][A-Z ]+?)(?:\s*\([^)]*\))?\s*:\s*"?(.*?)"?\s*$', dl)
                    if spk_match:
                        speaker = spk_match.group(1).strip()
                        text = spk_match.group(2).strip().strip('"')
                        current_panel["dialogue"].append({
                            "speaker": speaker,
                            "text": text,
                            "type": "speech",
                        })

        i += 1

    if current_page is not None:
        pages.append(current_page)

    for page in pages:
        if page["panel_count"] == 0:
            page["panel_count"] = len(page["panels"])

    return pages


# ---------------------------------------------------------------------------
# Panel width hints → grid cells
# ---------------------------------------------------------------------------

def parse_width_hint(hint: str) -> tuple[float, float, bool]:
    """Parse a panel width hint into (width_fraction, height_weight, is_inset).

    Width fraction: 0..1 of page width (1.0 = full width).
    Height weight: relative row height (1.0 = normal, 0.4 = narrow strip, 2.0 = splash).
    """
    h = hint.lower()

    # --- Inset panels (overlaid on splash) ---
    if "inset" in h:
        return 0.0, 0.0, True  # handled separately

    # --- Width ---
    width = 1.0
    if "quarter width" in h or "one-quarter" in h:
        width = 0.25
    elif "one-fifth" in h:
        width = 0.2
    elif "one-third" in h or ("narrow" in h and "one-third" in h):
        width = 0.33
    elif "two-thirds" in h:
        width = 0.67
    elif "two-fifths" in h:
        width = 0.4
    elif "three-quarter" in h:
        width = 0.75
    elif "half" in h and "full" not in h:
        width = 0.5
    elif "quarter page" in h:
        width = 0.5  # quarter-page = half width, half height grid cell
    elif "narrow" in h and "full" not in h and "strip" not in h:
        width = 0.33
    elif "wide" in h and "full" not in h and "widescreen" not in h:
        width = 0.67
    elif "equal" in h:
        width = 0.5
    elif "left half" in h or "right half" in h:
        width = 0.5
    # full width, full-width, full page, splash, etc. stay at 1.0

    # --- Height weight ---
    hw = 1.0
    if "full-page" in h or "full page" in h:
        hw = 3.0
    elif "splash" in h and ("top two-thirds" in h or "bottom two-thirds" in h
                            or "two-thirds" in h):
        hw = 2.0
    elif "splash" in h and ("top half" in h or "bottom half" in h or "half-page" in h):
        hw = 1.5
    elif "splash" in h:
        hw = 3.0
    elif "two-thirds of page" in h or "bottom two-thirds" in h:
        hw = 2.0
    elif "tall" in h or "top half" in h or "bottom half" in h or "half page" in h:
        hw = 1.5
    elif "top quarter" in h or "quarter height" in h:
        hw = 0.4
    elif "narrow strip" in h or "thin strip" in h or "narrow horizontal" in h:
        hw = 0.4
    elif "widescreen" in h or "letterbox" in h:
        hw = 0.6
    elif "narrow" in h and "strip" in h:
        hw = 0.4
    elif "shorter" in h:
        hw = 0.7
    elif "narrow" in h and ("beat" in h or "footer" in h):
        hw = 0.5

    return width, hw, False


def _parse_inset_position(hint: str) -> tuple[float, float]:
    """Parse an inset panel's position hint into (x, y) fractions."""
    h = hint.lower()
    # Vertical
    if "upper" in h or "top" in h:
        y = 0.05
    elif "middle" in h or "center" in h:
        y = 0.4
    else:  # lower, bottom, or default
        y = 0.75

    # Horizontal
    if "left" in h:
        x = 0.05
    elif "right" in h:
        x = 0.75
    elif "center" in h or "centre" in h:
        x = 0.4
    else:
        x = 0.75  # default to right

    return x, y


def panels_to_grid(panels: list[dict]) -> list[list[dict]]:
    """Derive a grid layout from per-panel width hints.

    Groups panels into rows by accumulating fractional widths until they
    reach ~1.0. Inset panels are separated and overlaid on the splash.

    Returns list of rows, each row is a list of cell dicts:
        {x, y, w, h} as fractions of the drawable area (0..1)
        Inset cells also have {"inset": True}
    """
    if not panels:
        return [[{"x": 0, "y": 0, "w": 1.0, "h": 1.0}]]

    # Separate inset panels from regular panels
    regular = []
    insets = []
    for p in panels:
        w, hw, is_inset = parse_width_hint(p["width_hint"])
        if is_inset:
            insets.append(p)
        else:
            regular.append({"panel": p, "width": w, "hw": hw})

    if not regular:
        # All inset — shouldn't happen, but handle gracefully
        regular = [{"panel": panels[0], "width": 1.0, "hw": 1.0}]
        insets = panels[1:]

    # Group regular panels into rows by accumulating widths
    rows_data = []  # list of lists of {panel, width, hw}
    current_row = []
    row_width = 0.0

    for item in regular:
        w = item["width"]

        if w >= 0.95:
            # Full-width panel: flush current row, then own row
            if current_row:
                rows_data.append(current_row)
                current_row = []
                row_width = 0.0
            rows_data.append([item])
        elif row_width + w > 1.05:
            # Would overflow: start new row
            if current_row:
                rows_data.append(current_row)
            current_row = [item]
            row_width = w
        else:
            current_row.append(item)
            row_width += w
            if row_width >= 0.95:
                rows_data.append(current_row)
                current_row = []
                row_width = 0.0

    if current_row:
        rows_data.append(current_row)

    # Compute row heights from max height weight in each row
    row_hws = [max(it["hw"] for it in row) for row in rows_data]
    total_hw = sum(row_hws)
    if total_hw == 0:
        total_hw = 1

    # Build positioned grid cells
    grid = []
    y_cursor = 0.0

    for row, rh in zip(rows_data, row_hws):
        row_h = rh / total_hw
        cells = []
        total_w = sum(it["width"] for it in row)
        if total_w == 0:
            total_w = 1.0
        x_cursor = 0.0

        for it in row:
            cell_w = it["width"] / total_w  # normalize to fill row
            cells.append({
                "x": x_cursor,
                "y": y_cursor,
                "w": cell_w,
                "h": row_h,
            })
            x_cursor += cell_w

        grid.append(cells)
        y_cursor += row_h

    # Add inset panels as overlay cells
    if insets:
        inset_size = 0.2
        inset_cells = []
        for p in insets:
            ix, iy = _parse_inset_position(p["width_hint"])
            inset_cells.append({
                "x": ix, "y": iy,
                "w": inset_size, "h": inset_size,
                "inset": True,
            })
        # Append insets to the first row (they overlay everything)
        grid[0].extend(inset_cells)

    return grid


def _simple_grid(panel_count: int) -> list[list[dict]]:
    """Fallback: arrange N panels in a reasonable grid when no width hints."""
    if panel_count <= 0:
        return [[{"x": 0, "y": 0, "w": 1.0, "h": 1.0}]]
    if panel_count == 1:
        return [[{"x": 0, "y": 0, "w": 1.0, "h": 1.0}]]

    # Build synthetic row descriptors
    row_descs = []
    if panel_count == 2:
        row_descs = [{"hw": 1.0, "widths": [1.0]}, {"hw": 1.0, "widths": [1.0]}]
    elif panel_count == 3:
        row_descs = [{"hw": 1.0, "widths": [1.0]}, {"hw": 1.0, "widths": [0.5, 0.5]}]
    elif panel_count == 4:
        row_descs = [{"hw": 1.0, "widths": [0.5, 0.5]}, {"hw": 1.0, "widths": [0.5, 0.5]}]
    elif panel_count == 5:
        row_descs = [
            {"hw": 1.0, "widths": [1.0]},
            {"hw": 1.0, "widths": [0.5, 0.5]},
            {"hw": 1.0, "widths": [0.5, 0.5]},
        ]
    else:  # 6+: fill 2-col rows
        row_descs = [{"hw": 1.0, "widths": [0.5, 0.5]}
                     for _ in range((panel_count + 1) // 2)]

    total_hw = sum(r["hw"] for r in row_descs)
    grid = []
    y_cursor = 0.0
    for rd in row_descs:
        row_h = rd["hw"] / total_hw
        cells = []
        x_cursor = 0.0
        tw = sum(rd["widths"])
        for wf in rd["widths"]:
            cw = wf / tw
            cells.append({"x": x_cursor, "y": y_cursor, "w": cw, "h": row_h})
            x_cursor += cw
        grid.append(cells)
        y_cursor += row_h
    return grid


# ---------------------------------------------------------------------------
# Character colors (suit accents for speech bubble borders)
# ---------------------------------------------------------------------------

CHAR_COLORS = {
    "SABLE":    "#b0b0b0",  # silver
    "WREN":     "#c87533",  # copper
    "JINK":     "#2e8b57",  # emerald
    "THRESH":   "#b22222",  # crimson
    "LUMA":     "#6a5acd",  # violet
    "THEODORE": "#c49a6c",  # warm amber
    "CAPTION":  "#e8dcc8",  # parchment
}

def _char_color(speaker: str) -> str:
    return CHAR_COLORS.get(speaker.upper(), "#999999")


# ---------------------------------------------------------------------------
# Text wrapping helper
# ---------------------------------------------------------------------------

def _wrap_text(text: str, max_chars: int) -> list[str]:
    """Wrap text to fit within max_chars per line."""
    words = text.split()
    lines = []
    current = ""
    for w in words:
        if current and len(current) + 1 + len(w) > max_chars:
            lines.append(current)
            current = w
        else:
            current = current + " " + w if current else w
    if current:
        lines.append(current)
    return lines if lines else [""]


# ---------------------------------------------------------------------------
# Figure drawing (simple silhouettes based on shot type)
# ---------------------------------------------------------------------------

def _draw_figure(parts: list, cx: float, cy: float, cw: float, ch: float,
                 shot_abbr: str, panel: dict):
    """Draw detailed character silhouettes based on shot type."""
    fg = "#c0b8a8"   # warm grey figure fill
    fg2 = "#a89888"  # darker accent

    # Collect unique speaking characters for multi-figure support
    speakers = []
    if panel.get("dialogue"):
        seen = set()
        for d in panel["dialogue"]:
            if d["type"] == "speech" and d["speaker"] not in seen:
                speakers.append(d["speaker"])
                seen.add(d["speaker"])

    char_col = _char_color(speakers[0]) if speakers else fg

    mid_x = cx + cw / 2
    mid_y = cy + ch / 2

    if shot_abbr in ("EST", "XWIDE", "WIDE"):
        # Wide shot: figures at bottom with ground, shoulders, arms, shadow
        ground_y = cy + ch * 0.78
        parts.append(
            f'<line x1="{cx + 6:.1f}" y1="{ground_y:.1f}" '
            f'x2="{cx + cw - 6:.1f}" y2="{ground_y:.1f}" '
            f'stroke="{fg2}" stroke-width="1.0" opacity="0.5"/>'
        )
        fig_h = min(ch * 0.18, 45)
        n_figs = min(len(speakers), 3) if speakers else (1 if cw < 160 else 2 if cw < 320 else 3)
        spacing = cw / (n_figs + 1)
        for i in range(n_figs):
            fc = _char_color(speakers[i]) if i < len(speakers) else char_col
            fx = cx + spacing * (i + 1)
            fy = ground_y
            head_r = fig_h * 0.18
            neck_y = fy - fig_h + head_r * 2
            # ground shadow
            parts.append(
                f'<ellipse cx="{fx:.1f}" cy="{fy + 2:.1f}" '
                f'rx="{fig_h * 0.25:.1f}" ry="{fig_h * 0.06:.1f}" '
                f'fill="{fg2}" opacity="0.2"/>'
            )
            # legs (slightly angled)
            parts.append(
                f'<line x1="{fx - fig_h * 0.06:.1f}" y1="{fy - fig_h * 0.35:.1f}" '
                f'x2="{fx - fig_h * 0.15:.1f}" y2="{fy:.1f}" '
                f'stroke="{fc}" stroke-width="2" opacity="0.5"/>'
            )
            parts.append(
                f'<line x1="{fx + fig_h * 0.06:.1f}" y1="{fy - fig_h * 0.35:.1f}" '
                f'x2="{fx + fig_h * 0.15:.1f}" y2="{fy:.1f}" '
                f'stroke="{fc}" stroke-width="2" opacity="0.5"/>'
            )
            # body
            parts.append(
                f'<line x1="{fx:.1f}" y1="{neck_y:.1f}" '
                f'x2="{fx:.1f}" y2="{fy - fig_h * 0.35:.1f}" '
                f'stroke="{fc}" stroke-width="2.5" opacity="0.6"/>'
            )
            # shoulders
            sh_w = fig_h * 0.3
            parts.append(
                f'<line x1="{fx - sh_w:.1f}" y1="{neck_y + 2:.1f}" '
                f'x2="{fx + sh_w:.1f}" y2="{neck_y + 2:.1f}" '
                f'stroke="{fc}" stroke-width="2" opacity="0.5"/>'
            )
            # arms (angled down from shoulders)
            parts.append(
                f'<line x1="{fx - sh_w:.1f}" y1="{neck_y + 2:.1f}" '
                f'x2="{fx - sh_w - fig_h * 0.1:.1f}" y2="{neck_y + fig_h * 0.3:.1f}" '
                f'stroke="{fc}" stroke-width="1.5" opacity="0.4"/>'
            )
            parts.append(
                f'<line x1="{fx + sh_w:.1f}" y1="{neck_y + 2:.1f}" '
                f'x2="{fx + sh_w + fig_h * 0.1:.1f}" y2="{neck_y + fig_h * 0.3:.1f}" '
                f'stroke="{fc}" stroke-width="1.5" opacity="0.4"/>'
            )
            # head
            parts.append(
                f'<circle cx="{fx:.1f}" cy="{fy - fig_h:.1f}" r="{head_r:.1f}" '
                f'fill="{fc}" opacity="0.6"/>'
            )

    elif shot_abbr in ("MED", "MW"):
        # Medium shot: detailed torso with neck, shoulders, arms, belt line
        fig_h = ch * 0.45
        fig_w = min(cw * 0.35, fig_h * 0.65)
        base_y = cy + ch * 0.72
        head_r = fig_w * 0.38
        neck_w = head_r * 0.4
        shoulder_y = base_y - fig_h + head_r * 2.8
        head_y = base_y - fig_h
        # torso (tapered shape)
        parts.append(
            f'<path d="M{mid_x - fig_w * 0.55:.1f},{base_y:.1f} '
            f'L{mid_x - fig_w * 0.5:.1f},{shoulder_y + 4:.1f} '
            f'Q{mid_x - fig_w * 0.45:.1f},{shoulder_y:.1f} {mid_x - neck_w:.1f},{shoulder_y:.1f} '
            f'L{mid_x + neck_w:.1f},{shoulder_y:.1f} '
            f'Q{mid_x + fig_w * 0.45:.1f},{shoulder_y:.1f} {mid_x + fig_w * 0.5:.1f},{shoulder_y + 4:.1f} '
            f'L{mid_x + fig_w * 0.55:.1f},{base_y:.1f} Z" '
            f'fill="{char_col}" opacity="0.35"/>'
        )
        # belt line
        belt_y = base_y - fig_h * 0.15
        parts.append(
            f'<line x1="{mid_x - fig_w * 0.5:.1f}" y1="{belt_y:.1f}" '
            f'x2="{mid_x + fig_w * 0.5:.1f}" y2="{belt_y:.1f}" '
            f'stroke="{char_col}" stroke-width="1" opacity="0.3"/>'
        )
        # arms (bent at elbows)
        arm_top_y = shoulder_y + 4
        elbow_y = arm_top_y + fig_h * 0.25
        # left arm
        parts.append(
            f'<line x1="{mid_x - fig_w * 0.5:.1f}" y1="{arm_top_y:.1f}" '
            f'x2="{mid_x - fig_w * 0.7:.1f}" y2="{elbow_y:.1f}" '
            f'stroke="{char_col}" stroke-width="2" opacity="0.3"/>'
        )
        parts.append(
            f'<line x1="{mid_x - fig_w * 0.7:.1f}" y1="{elbow_y:.1f}" '
            f'x2="{mid_x - fig_w * 0.55:.1f}" y2="{elbow_y + fig_h * 0.15:.1f}" '
            f'stroke="{char_col}" stroke-width="2" opacity="0.3"/>'
        )
        # right arm
        parts.append(
            f'<line x1="{mid_x + fig_w * 0.5:.1f}" y1="{arm_top_y:.1f}" '
            f'x2="{mid_x + fig_w * 0.7:.1f}" y2="{elbow_y:.1f}" '
            f'stroke="{char_col}" stroke-width="2" opacity="0.3"/>'
        )
        parts.append(
            f'<line x1="{mid_x + fig_w * 0.7:.1f}" y1="{elbow_y:.1f}" '
            f'x2="{mid_x + fig_w * 0.55:.1f}" y2="{elbow_y + fig_h * 0.15:.1f}" '
            f'stroke="{char_col}" stroke-width="2" opacity="0.3"/>'
        )
        # neck
        parts.append(
            f'<line x1="{mid_x:.1f}" y1="{head_y + head_r:.1f}" '
            f'x2="{mid_x:.1f}" y2="{shoulder_y:.1f}" '
            f'stroke="{char_col}" stroke-width="3" opacity="0.35"/>'
        )
        # head
        parts.append(
            f'<circle cx="{mid_x:.1f}" cy="{head_y:.1f}" '
            f'r="{head_r:.1f}" fill="{char_col}" opacity="0.4"/>'
        )

    elif shot_abbr in ("MCU",):
        # Medium close-up: head + shoulders with jaw, hair, collar, ears
        fig_h = ch * 0.5
        head_r = min(cw * 0.18, fig_h * 0.35)
        head_y = cy + ch * 0.4
        shoulder_w = head_r * 3.2
        # shoulders + collar (curved)
        parts.append(
            f'<path d="M{mid_x - shoulder_w/2:.1f},{head_y + head_r * 2.0:.1f} '
            f'Q{mid_x - shoulder_w/2:.1f},{head_y + head_r * 1.2:.1f} '
            f'{mid_x - head_r * 0.4:.1f},{head_y + head_r * 1.1:.1f} '
            f'L{mid_x + head_r * 0.4:.1f},{head_y + head_r * 1.1:.1f} '
            f'Q{mid_x + shoulder_w/2:.1f},{head_y + head_r * 1.2:.1f} '
            f'{mid_x + shoulder_w/2:.1f},{head_y + head_r * 2.0:.1f} '
            f'L{mid_x + shoulder_w/2:.1f},{cy + ch * 0.88:.1f} '
            f'L{mid_x - shoulder_w/2:.1f},{cy + ch * 0.88:.1f} Z" '
            f'fill="{char_col}" opacity="0.25"/>'
        )
        # collar V-neckline
        parts.append(
            f'<path d="M{mid_x - head_r * 0.35:.1f},{head_y + head_r * 1.1:.1f} '
            f'L{mid_x:.1f},{head_y + head_r * 1.6:.1f} '
            f'L{mid_x + head_r * 0.35:.1f},{head_y + head_r * 1.1:.1f}" '
            f'fill="none" stroke="{char_col}" stroke-width="1" opacity="0.3"/>'
        )
        # head
        parts.append(
            f'<circle cx="{mid_x:.1f}" cy="{head_y:.1f}" '
            f'r="{head_r:.1f}" fill="{char_col}" opacity="0.35"/>'
        )
        # jaw line (slightly narrower)
        jaw_r = head_r * 0.85
        parts.append(
            f'<path d="M{mid_x - head_r:.1f},{head_y + head_r * 0.2:.1f} '
            f'Q{mid_x - jaw_r:.1f},{head_y + head_r * 1.1:.1f} '
            f'{mid_x:.1f},{head_y + head_r * 1.15:.1f} '
            f'Q{mid_x + jaw_r:.1f},{head_y + head_r * 1.1:.1f} '
            f'{mid_x + head_r:.1f},{head_y + head_r * 0.2:.1f}" '
            f'fill="none" stroke="{char_col}" stroke-width="1.2" opacity="0.3"/>'
        )
        # hair arc
        parts.append(
            f'<path d="M{mid_x - head_r * 1.05:.1f},{head_y - head_r * 0.1:.1f} '
            f'Q{mid_x:.1f},{head_y - head_r * 1.3:.1f} '
            f'{mid_x + head_r * 1.05:.1f},{head_y - head_r * 0.1:.1f}" '
            f'fill="none" stroke="{char_col}" stroke-width="2" opacity="0.4"/>'
        )
        # ears
        ear_y = head_y + head_r * 0.05
        parts.append(
            f'<ellipse cx="{mid_x - head_r - 2:.1f}" cy="{ear_y:.1f}" '
            f'rx="2.5" ry="4" fill="{char_col}" opacity="0.25"/>'
        )
        parts.append(
            f'<ellipse cx="{mid_x + head_r + 2:.1f}" cy="{ear_y:.1f}" '
            f'rx="2.5" ry="4" fill="{char_col}" opacity="0.25"/>'
        )

    elif shot_abbr in ("CU", "ECU"):
        # Close-up: detailed face with nose, mouth, eyebrows, hair, eyes
        face_h = ch * 0.45
        face_w = min(cw * 0.4, face_h * 0.7)
        face_y = cy + ch * 0.42
        parts.append(
            f'<ellipse cx="{mid_x:.1f}" cy="{face_y:.1f}" '
            f'rx="{face_w:.1f}" ry="{face_h:.1f}" '
            f'fill="{char_col}" opacity="0.18"/>'
        )
        # Hair (arc over top of head)
        parts.append(
            f'<path d="M{mid_x - face_w * 1.05:.1f},{face_y - face_h * 0.35:.1f} '
            f'Q{mid_x:.1f},{face_y - face_h * 1.15:.1f} '
            f'{mid_x + face_w * 1.05:.1f},{face_y - face_h * 0.35:.1f}" '
            f'fill="none" stroke="{char_col}" stroke-width="3" opacity="0.35"/>'
        )
        # Eyebrows
        brow_y = face_y - face_h * 0.22
        brow_w = face_w * 0.3
        parts.append(
            f'<line x1="{mid_x - face_w * 0.35:.1f}" y1="{brow_y:.1f}" '
            f'x2="{mid_x - face_w * 0.35 + brow_w:.1f}" y2="{brow_y - 2:.1f}" '
            f'stroke="{fg2}" stroke-width="1.5" opacity="0.45"/>'
        )
        parts.append(
            f'<line x1="{mid_x + face_w * 0.35 - brow_w:.1f}" y1="{brow_y - 2:.1f}" '
            f'x2="{mid_x + face_w * 0.35:.1f}" y2="{brow_y:.1f}" '
            f'stroke="{fg2}" stroke-width="1.5" opacity="0.45"/>'
        )
        # Eyes (small ellipses)
        eye_y = face_y - face_h * 0.12
        eye_rx = face_w * 0.12
        eye_ry = face_h * 0.05
        parts.append(
            f'<ellipse cx="{mid_x - face_w * 0.28:.1f}" cy="{eye_y:.1f}" '
            f'rx="{eye_rx:.1f}" ry="{eye_ry:.1f}" '
            f'fill="{fg2}" opacity="0.45"/>'
        )
        parts.append(
            f'<ellipse cx="{mid_x + face_w * 0.28:.1f}" cy="{eye_y:.1f}" '
            f'rx="{eye_rx:.1f}" ry="{eye_ry:.1f}" '
            f'fill="{fg2}" opacity="0.45"/>'
        )
        # Nose (short vertical line)
        nose_top = face_y + face_h * 0.02
        nose_bot = face_y + face_h * 0.18
        parts.append(
            f'<line x1="{mid_x:.1f}" y1="{nose_top:.1f}" '
            f'x2="{mid_x:.1f}" y2="{nose_bot:.1f}" '
            f'stroke="{fg2}" stroke-width="1.2" opacity="0.35"/>'
        )
        # Nose tip (small curve)
        parts.append(
            f'<path d="M{mid_x - face_w * 0.06:.1f},{nose_bot:.1f} '
            f'Q{mid_x:.1f},{nose_bot + 3:.1f} '
            f'{mid_x + face_w * 0.06:.1f},{nose_bot:.1f}" '
            f'fill="none" stroke="{fg2}" stroke-width="1" opacity="0.3"/>'
        )
        # Mouth
        mouth_y = face_y + face_h * 0.32
        mouth_w = face_w * 0.25
        parts.append(
            f'<line x1="{mid_x - mouth_w:.1f}" y1="{mouth_y:.1f}" '
            f'x2="{mid_x + mouth_w:.1f}" y2="{mouth_y:.1f}" '
            f'stroke="{fg2}" stroke-width="1.2" opacity="0.35"/>'
        )

    elif shot_abbr == "POV":
        # POV: perspective lines with horizon and depth
        van_x = mid_x
        van_y = cy + ch * 0.35
        # horizon line
        parts.append(
            f'<line x1="{cx + 8:.1f}" y1="{van_y:.1f}" '
            f'x2="{cx + cw - 8:.1f}" y2="{van_y:.1f}" '
            f'stroke="{fg2}" stroke-width="0.6" opacity="0.2"/>'
        )
        for angle_offset in [-0.4, -0.2, -0.07, 0.07, 0.2, 0.4]:
            ex = mid_x + cw * angle_offset
            ey = cy + ch * 0.9
            parts.append(
                f'<line x1="{van_x:.1f}" y1="{van_y:.1f}" '
                f'x2="{ex:.1f}" y2="{ey:.1f}" '
                f'stroke="{fg2}" stroke-width="0.8" opacity="0.25"/>'
            )
        # vanishing point dot
        parts.append(
            f'<circle cx="{van_x:.1f}" cy="{van_y:.1f}" r="3" '
            f'fill="{fg2}" opacity="0.3"/>'
        )

    elif shot_abbr in ("SPLASH", "DYN"):
        # Splash/dynamic: large figure with bent legs, wing-pack, action lines
        fig_h = ch * 0.55
        head_r = min(cw * 0.08, 20)
        base_y = cy + ch * 0.78
        lean = cw * 0.06
        hip_y = base_y - fig_h * 0.35
        # legs (bent at knees)
        knee_y = base_y - fig_h * 0.15
        parts.append(
            f'<line x1="{mid_x - lean * 0.5:.1f}" y1="{hip_y:.1f}" '
            f'x2="{mid_x - lean * 2:.1f}" y2="{knee_y:.1f}" '
            f'stroke="{char_col}" stroke-width="3" opacity="0.35"/>'
        )
        parts.append(
            f'<line x1="{mid_x - lean * 2:.1f}" y1="{knee_y:.1f}" '
            f'x2="{mid_x - lean * 1:.1f}" y2="{base_y:.1f}" '
            f'stroke="{char_col}" stroke-width="3" opacity="0.35"/>'
        )
        parts.append(
            f'<line x1="{mid_x + lean * 0.5:.1f}" y1="{hip_y:.1f}" '
            f'x2="{mid_x + lean * 2.5:.1f}" y2="{knee_y - fig_h * 0.05:.1f}" '
            f'stroke="{char_col}" stroke-width="3" opacity="0.35"/>'
        )
        parts.append(
            f'<line x1="{mid_x + lean * 2.5:.1f}" y1="{knee_y - fig_h * 0.05:.1f}" '
            f'x2="{mid_x + lean * 3:.1f}" y2="{base_y - fig_h * 0.08:.1f}" '
            f'stroke="{char_col}" stroke-width="3" opacity="0.35"/>'
        )
        # body (torso)
        torso_top = base_y - fig_h + head_r * 2.2
        parts.append(
            f'<line x1="{mid_x + lean:.1f}" y1="{torso_top:.1f}" '
            f'x2="{mid_x - lean * 0.3:.1f}" y2="{hip_y:.1f}" '
            f'stroke="{char_col}" stroke-width="3.5" opacity="0.4"/>'
        )
        # head
        parts.append(
            f'<circle cx="{mid_x + lean:.1f}" cy="{base_y - fig_h:.1f}" '
            f'r="{head_r:.1f}" fill="{char_col}" opacity="0.4"/>'
        )
        # arms (dynamic pose)
        arm_y = torso_top + fig_h * 0.15
        parts.append(
            f'<line x1="{mid_x + lean * 0.5:.1f}" y1="{arm_y:.1f}" '
            f'x2="{mid_x + cw * 0.18:.1f}" y2="{arm_y - ch * 0.08:.1f}" '
            f'stroke="{char_col}" stroke-width="2.5" opacity="0.35"/>'
        )
        parts.append(
            f'<line x1="{mid_x + lean * 0.5:.1f}" y1="{arm_y:.1f}" '
            f'x2="{mid_x - cw * 0.14:.1f}" y2="{arm_y + ch * 0.06:.1f}" '
            f'stroke="{char_col}" stroke-width="2.5" opacity="0.35"/>'
        )
        # wing-pack suggestion (arced lines behind torso)
        wing_cx = mid_x + lean * 0.5
        wing_cy = arm_y - fig_h * 0.05
        parts.append(
            f'<path d="M{wing_cx:.1f},{wing_cy:.1f} '
            f'Q{wing_cx - cw * 0.12:.1f},{wing_cy - ch * 0.1:.1f} '
            f'{wing_cx - cw * 0.08:.1f},{wing_cy - ch * 0.18:.1f}" '
            f'fill="none" stroke="{char_col}" stroke-width="1.5" opacity="0.25"/>'
        )
        parts.append(
            f'<path d="M{wing_cx:.1f},{wing_cy:.1f} '
            f'Q{wing_cx + cw * 0.12:.1f},{wing_cy - ch * 0.1:.1f} '
            f'{wing_cx + cw * 0.08:.1f},{wing_cy - ch * 0.18:.1f}" '
            f'fill="none" stroke="{char_col}" stroke-width="1.5" opacity="0.25"/>'
        )
        # action/speed lines
        for dy in [-0.18, -0.08, 0.02, 0.12]:
            lx1 = cx + cw * 0.78
            lx2 = cx + cw * 0.95
            ly = mid_y + ch * dy
            parts.append(
                f'<line x1="{lx1:.1f}" y1="{ly:.1f}" '
                f'x2="{lx2:.1f}" y2="{ly:.1f}" '
                f'stroke="{fg2}" stroke-width="1.2" opacity="0.3"/>'
            )
        # impact/energy radiating lines
        for angle in [-0.3, -0.15, 0.15, 0.3]:
            rx1 = cx + cw * 0.05
            ry = mid_y + ch * angle
            rx2 = cx + cw * 0.18
            parts.append(
                f'<line x1="{rx1:.1f}" y1="{ry:.1f}" '
                f'x2="{rx2:.1f}" y2="{ry:.1f}" '
                f'stroke="{fg2}" stroke-width="1" opacity="0.2"/>'
            )

    elif shot_abbr == "RXN":
        # Reaction: detailed face with expression marks
        face_r = min(cw * 0.24, ch * 0.24, 45)
        # face
        parts.append(
            f'<circle cx="{mid_x:.1f}" cy="{mid_y:.1f}" '
            f'r="{face_r:.1f}" fill="{char_col}" opacity="0.22"/>'
        )
        # eyebrows (angled for expression)
        parts.append(
            f'<line x1="{mid_x - face_r * 0.55:.1f}" y1="{mid_y - face_r * 0.25:.1f}" '
            f'x2="{mid_x - face_r * 0.15:.1f}" y2="{mid_y - face_r * 0.42:.1f}" '
            f'stroke="{fg2}" stroke-width="1.5" opacity="0.5"/>'
        )
        parts.append(
            f'<line x1="{mid_x + face_r * 0.15:.1f}" y1="{mid_y - face_r * 0.42:.1f}" '
            f'x2="{mid_x + face_r * 0.55:.1f}" y2="{mid_y - face_r * 0.25:.1f}" '
            f'stroke="{fg2}" stroke-width="1.5" opacity="0.5"/>'
        )
        # eyes
        parts.append(
            f'<ellipse cx="{mid_x - face_r * 0.3:.1f}" cy="{mid_y - face_r * 0.1:.1f}" '
            f'rx="{face_r * 0.1:.1f}" ry="{face_r * 0.06:.1f}" '
            f'fill="{fg2}" opacity="0.5"/>'
        )
        parts.append(
            f'<ellipse cx="{mid_x + face_r * 0.3:.1f}" cy="{mid_y - face_r * 0.1:.1f}" '
            f'rx="{face_r * 0.1:.1f}" ry="{face_r * 0.06:.1f}" '
            f'fill="{fg2}" opacity="0.5"/>'
        )
        # nose
        parts.append(
            f'<line x1="{mid_x:.1f}" y1="{mid_y + face_r * 0.02:.1f}" '
            f'x2="{mid_x:.1f}" y2="{mid_y + face_r * 0.2:.1f}" '
            f'stroke="{fg2}" stroke-width="1" opacity="0.35"/>'
        )
        # mouth (open for reaction)
        parts.append(
            f'<ellipse cx="{mid_x:.1f}" cy="{mid_y + face_r * 0.38:.1f}" '
            f'rx="{face_r * 0.15:.1f}" ry="{face_r * 0.08:.1f}" '
            f'fill="{fg2}" opacity="0.25"/>'
        )
        # surprise/stress lines radiating outward
        for angle_deg in [30, 60, 120, 150, 210, 240, 300, 330]:
            rad = math.radians(angle_deg)
            r1 = face_r * 1.15
            r2 = face_r * 1.35
            x1 = mid_x + r1 * math.cos(rad)
            y1 = mid_y + r1 * math.sin(rad)
            x2 = mid_x + r2 * math.cos(rad)
            y2 = mid_y + r2 * math.sin(rad)
            parts.append(
                f'<line x1="{x1:.1f}" y1="{y1:.1f}" '
                f'x2="{x2:.1f}" y2="{y2:.1f}" '
                f'stroke="{fg2}" stroke-width="1" opacity="0.3"/>'
            )


# ---------------------------------------------------------------------------
# Speech bubble and caption rendering
# ---------------------------------------------------------------------------

def _draw_dialogue(parts: list, cx: float, cy: float, cw: float, ch: float,
                   panel: dict):
    """Draw speech bubbles and caption boxes for a panel's dialogue."""
    dialogue = panel.get("dialogue", [])
    if not dialogue:
        return

    # Budget vertical space for dialogue — use top and bottom zones
    pad = 6
    font_size = 9.0 if cw < 120 else 10.0 if cw < 250 else 11.0
    line_h = font_size + 3
    chars_per_line = max(10, int((cw - pad * 4) / (font_size * 0.52)))

    # Place dialogue items from top
    y_cursor = cy + pad + 2
    align_right = False  # alternate sides for conversation flow

    for d in dialogue:
        if y_cursor > cy + ch * 0.92:
            break  # stop near bottom edge

        speaker = d["speaker"]
        text = d["text"]
        dtype = d["type"]

        # No truncation — show full dialogue for proofreading
        lines = _wrap_text(text, chars_per_line)

        bubble_h = (len(lines) + 1) * line_h + pad * 2  # +1 for speaker name
        bubble_w = min(cw - pad * 2, max(len(max(lines, key=len)) * font_size * 0.55, 50) + pad * 2)

        if dtype == "caption":
            # Caption box: rectangular, amber tint — wide for readability
            cap_w = min(cw * 0.8, bubble_w)
            bx = cx + pad
            by = y_cursor
            parts.append(
                f'<rect x="{bx:.1f}" y="{by:.1f}" width="{cap_w:.1f}" '
                f'height="{bubble_h:.1f}" rx="2" '
                f'fill="#f5ecd8" stroke="#c8b898" stroke-width="0.8" opacity="0.92"/>'
            )
            # Caption text (italic)
            ty = by + pad + font_size
            parts.append(
                f'<text x="{bx + pad:.1f}" y="{ty:.1f}" '
                f'font-size="{font_size}" fill="#5a4a30" font-style="italic" '
                f'font-weight="500">'
                f'{_escape_xml("CAPTION")}</text>'
            )
            for ln in lines:
                ty += line_h
                parts.append(
                    f'<text x="{bx + pad:.1f}" y="{ty:.1f}" '
                    f'font-size="{font_size}" fill="#5a4a30" font-style="italic">'
                    f'{_escape_xml(ln)}</text>'
                )
            y_cursor = by + bubble_h + 4

        else:
            # Speech bubble: rounded rect with tail
            # Alternate left/right for conversation flow
            if align_right and bubble_w < cw - pad * 3:
                bx = cx + cw - pad - bubble_w
            else:
                bx = cx + pad
            by = y_cursor
            border_col = _char_color(speaker)
            parts.append(
                f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bubble_w:.1f}" '
                f'height="{bubble_h:.1f}" rx="6" '
                f'fill="white" stroke="{border_col}" stroke-width="1.0" opacity="0.92"/>'
            )
            # Tail (triangle pointing down)
            tail_x = bx + bubble_w * 0.3
            tail_y = by + bubble_h
            parts.append(
                f'<polygon points="{tail_x:.1f},{tail_y:.1f} '
                f'{tail_x + 8:.1f},{tail_y:.1f} '
                f'{tail_x - 3:.1f},{tail_y + 8:.1f}" '
                f'fill="white" stroke="{border_col}" stroke-width="0.8"/>'
            )
            # Cover tail-bubble seam
            parts.append(
                f'<line x1="{tail_x - 0.5:.1f}" y1="{tail_y:.1f}" '
                f'x2="{tail_x + 8.5:.1f}" y2="{tail_y:.1f}" '
                f'stroke="white" stroke-width="1.5"/>'
            )
            # Speaker name
            ty = by + pad + font_size
            parts.append(
                f'<text x="{bx + pad:.1f}" y="{ty:.1f}" '
                f'font-size="{font_size}" fill="{border_col}" '
                f'font-weight="700">'
                f'{_escape_xml(speaker)}</text>'
            )
            # Dialogue text
            for ln in lines:
                ty += line_h
                parts.append(
                    f'<text x="{bx + pad:.1f}" y="{ty:.1f}" '
                    f'font-size="{font_size}" fill="#333333">'
                    f'{_escape_xml(ln)}</text>'
                )
            y_cursor = by + bubble_h + 10
            align_right = not align_right  # alternate for next bubble


# ---------------------------------------------------------------------------
# SVG rendering
# ---------------------------------------------------------------------------

def render_page_svg(page: dict) -> str:
    """Render a single page wireframe as an SVG string with figures and dialogue."""
    # Derive grid from per-panel width hints
    if page["panels"]:
        grid = panels_to_grid(page["panels"])
    else:
        grid = _simple_grid(page["panel_count"])

    cells = []
    for row in grid:
        cells.extend(row)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {PAGE_W} {PAGE_H}" '
        f'width="{PAGE_W}" height="{PAGE_H}" style="background:{BG_FILL}">',
        '<style>',
        '  text { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; }',
        '</style>',
    ]

    # Page title
    title_text = f'PAGE {page["page_num"]}  ({page["panel_count"]} panels)'
    parts.append(
        f'<text x="{PAGE_W/2}" y="22" text-anchor="middle" '
        f'font-size="16" fill="{SHOT_COLOR}" font-weight="500">{title_text}</text>'
    )

    draw_y0 = MARGIN + 30
    panels = page["panels"]

    for idx, cell in enumerate(cells):
        is_inset = cell.get("inset", False)

        cx = MARGIN + cell["x"] * DRAW_W
        cy = draw_y0 + cell["y"] * DRAW_H
        cw = cell["w"] * DRAW_W
        ch = cell["h"] * DRAW_H

        if not is_inset and len(cells) > 1:
            cx += GUTTER / 2
            cy += GUTTER / 2
            cw -= GUTTER
            ch -= GUTTER

        if cw < 2 or ch < 2:
            continue

        fill = INSET_FILL if is_inset else PANEL_FILL
        stroke_w = 1.0 if is_inset else 1.5

        # Panel background
        parts.append(
            f'<rect x="{cx:.1f}" y="{cy:.1f}" width="{cw:.1f}" height="{ch:.1f}" '
            f'rx="2" fill="{fill}" stroke="{PANEL_STROKE}" stroke-width="{stroke_w}"/>'
        )

        if idx < len(panels):
            p = panels[idx]

            # Draw character figure
            if cw > 30 and ch > 30:
                _draw_figure(parts, cx, cy, cw, ch, p.get("shot_abbr", ""), p)

            # Draw dialogue bubbles and captions
            if cw > 50 and ch > 40:
                _draw_dialogue(parts, cx, cy, cw, ch, p)

            # Panel number (top-right corner)
            num_x = cx + cw - 12
            num_y = cy + 16
            fs = 12 if min(cw, ch) > 60 else 9
            parts.append(
                f'<text x="{num_x:.1f}" y="{num_y:.1f}" text-anchor="end" '
                f'font-size="{fs}" font-weight="bold" fill="{SHOT_COLOR}" '
                f'opacity="0.6">{p["num"]}</text>'
            )

            # Shot type label (bottom-right)
            if p.get("shot_abbr") and ch > 50:
                parts.append(
                    f'<text x="{cx + cw - 6:.1f}" y="{cy + ch - 6:.1f}" '
                    f'text-anchor="end" font-size="9" fill="{SHOT_COLOR}" '
                    f'opacity="0.5">{p["shot_abbr"]}</text>'
                )

    parts.append("</svg>")
    return "\n".join(parts)


def render_overview_svg(pages: list[dict], issue_title: str) -> str:
    """Render a thumbnail overview of all pages in an issue."""
    # Calculate thumbnail dimensions
    usable_w = OV_W - 2 * OV_PAD
    usable_h = OV_H - OV_TITLE_H - 2 * OV_PAD
    thumb_w = (usable_w - (OV_COLS - 1) * OV_PAD) / OV_COLS
    thumb_h = (usable_h - (OV_ROWS - 1) * OV_PAD) / OV_ROWS
    # Maintain ~2:3 aspect ratio
    if thumb_h / thumb_w > 1.5:
        thumb_h = thumb_w * 1.5
    elif thumb_w / thumb_h > 0.667:
        thumb_w = thumb_h * 0.667

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {OV_W} {OV_H}" '
        f'width="{OV_W}" height="{OV_H}" style="background:{BG_FILL}">',
        f'<style>',
        f'  text {{ font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; }}',
        f'</style>',
    ]

    # Title
    parts.append(
        f'<text x="{OV_W/2}" y="{OV_PAD + 28}" text-anchor="middle" '
        f'font-size="26" font-weight="bold" fill="{LABEL_COLOR}">'
        f'GRIMGLOW — {_escape_xml(issue_title)}</text>'
    )

    # Center the grid
    grid_w = OV_COLS * thumb_w + (OV_COLS - 1) * OV_PAD
    grid_h = OV_ROWS * thumb_h + (OV_ROWS - 1) * (OV_PAD + 14)  # extra for label
    start_x = (OV_W - grid_w) / 2
    start_y = OV_TITLE_H + OV_PAD

    for i, page in enumerate(pages):
        col = i % OV_COLS
        row = i // OV_COLS
        tx = start_x + col * (thumb_w + OV_PAD)
        ty = start_y + row * (thumb_h + OV_PAD + 14)

        # Thumbnail border
        parts.append(
            f'<rect x="{tx:.1f}" y="{ty:.1f}" width="{thumb_w:.1f}" '
            f'height="{thumb_h:.1f}" rx="1" fill="{BG_FILL}" '
            f'stroke="{PANEL_STROKE}" stroke-width="0.5"/>'
        )

        # Draw mini panels
        if page["panels"]:
            grid = panels_to_grid(page["panels"])
        else:
            grid = _simple_grid(page["panel_count"])
        cells = []
        for r in grid:
            cells.extend(r)

        mini_margin = 3
        mini_draw_w = thumb_w - 2 * mini_margin
        mini_draw_h = thumb_h - 2 * mini_margin
        mini_gutter = 2

        for cell in cells:
            is_inset = cell.get("inset", False)
            cx = tx + mini_margin + cell["x"] * mini_draw_w
            cy = ty + mini_margin + cell["y"] * mini_draw_h
            cw = cell["w"] * mini_draw_w
            ch = cell["h"] * mini_draw_h

            if not is_inset and len(cells) > 1:
                cx += mini_gutter / 2
                cy += mini_gutter / 2
                cw -= mini_gutter
                ch -= mini_gutter

            if cw < 1 or ch < 1:
                continue

            fill = INSET_FILL if is_inset else PANEL_FILL
            parts.append(
                f'<rect x="{cx:.1f}" y="{cy:.1f}" width="{cw:.1f}" '
                f'height="{ch:.1f}" rx="1" fill="{fill}" '
                f'stroke="{PANEL_STROKE}" stroke-width="0.5"/>'
            )

        # Page number label below thumbnail
        parts.append(
            f'<text x="{tx + thumb_w / 2:.1f}" y="{ty + thumb_h + 11:.1f}" '
            f'text-anchor="middle" font-size="9" fill="{SHOT_COLOR}">P{page["page_num"]}</text>'
        )

    parts.append("</svg>")
    return "\n".join(parts)


def _escape_xml(text: str) -> str:
    """Escape XML special characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    total_pages = 0
    total_svgs = 0

    for script_file, dir_name, title in ISSUES:
        script_path = SCRIPT_DIR / script_file
        if not script_path.exists():
            print(f"  SKIP: {script_file} not found")
            continue

        out_dir = OUTPUT_DIR / dir_name
        out_dir.mkdir(parents=True, exist_ok=True)

        pages = parse_script(script_path)
        print(f"  {title}: {len(pages)} pages parsed")

        # Generate individual page SVGs
        for page in pages:
            svg = render_page_svg(page)
            out_path = out_dir / f"page{page['page_num']:02d}.svg"
            out_path.write_text(svg, encoding="utf-8")
            total_svgs += 1

        # Generate overview SVG
        overview_svg = render_overview_svg(pages, title)
        overview_path = out_dir / "overview.svg"
        overview_path.write_text(overview_svg, encoding="utf-8")
        total_svgs += 1

        total_pages += len(pages)

    print(f"\nDone: {total_pages} pages → {total_svgs} SVGs")


if __name__ == "__main__":
    main()
