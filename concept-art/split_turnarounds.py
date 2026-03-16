#!/usr/bin/env python3
"""Split character turnaround sheets into individual view images.

Detects the gaps between figures by analyzing column-wise variance against
the neutral background, then crops at the midpoint of each gap. This handles
turnarounds where figures are not evenly spaced (e.g. broader armor, braids,
hand-on-hip poses).

Usage:
  python3 split_turnarounds.py                        # Process all 6 characters (clean suits)
  python3 split_turnarounds.py --variant mid-mission  # Process mid-mission turnarounds
  python3 split_turnarounds.py --variant phase-strip  # Process phase comparison strips
  python3 split_turnarounds.py --all                  # Process ALL variants for all characters
  python3 split_turnarounds.py Sable Wren             # Process specific characters
  python3 split_turnarounds.py --source 2026-03-08    # Use a different turnaround date
  python3 split_turnarounds.py --debug                # Show detected gap positions
"""

import sys
import glob
from pathlib import Path
from PIL import Image
import numpy as np

VIEWS = ["front", "three-quarter", "profile", "back"]
CHARACTERS = ["Sable", "Wren", "Jink", "Thresh", "Luma", "Theodore"]

# Phase numbering for consistent sort order (clean → light → mid → heavy)
# Tuple: (file_tag_base, view_prefix)
PHASE_MAP = {
    "clean-suit":  ("1-CleanSuit",  "1-clean-suit"),
    "light-wear":  ("2-LightWear",  "2-light-wear"),
    "mid-mission": ("3-MidMission", "3-mid-mission"),
    "heavy-wear":  ("4-HeavyWear",  "4-heavy-wear"),
    "phase-strip": ("PhaseStrip",   "phase-strip"),
}

# Phase strip splits into phases (not angles)
PHASE_STRIP_VIEWS = ["1-clean-suit", "2-light-wear", "3-mid-mission", "4-heavy-wear"]

ALL_VARIANTS = ["clean-suit", "light-wear", "mid-mission", "heavy-wear"]

SCRIPT_DIR = Path(__file__).parent


def find_turnaround(character: str, source_date: str | None = None,
                    variant: str | None = None) -> Path | None:
    """Find the turnaround image for a character, preferring the given date.

    Handles a/b/c suffixes — prefers 'a' (newest/best), then no suffix, then 'b', 'c'.
    variant: "clean-suit", "light-wear", "mid-mission", "heavy-wear",
             "phase-strip", or None (= clean-suit).
    """
    char_dir = SCRIPT_DIR / character
    if not char_dir.is_dir():
        return None

    # Map variant to phase-numbered filename tag base
    effective_variant = variant or "clean-suit"
    if effective_variant in PHASE_MAP:
        tag_base = PHASE_MAP[effective_variant][0]
    else:
        tag_base = ''.join(w.capitalize() for w in effective_variant.split('-'))

    if source_date:
        # Try exact match with date (with and without letter suffix)
        for suffix in ["a", "", "b", "c"]:
            tag = f"_{tag_base}" if not suffix else f"_{suffix}-{tag_base}" if tag_base[0].isdigit() else f"_{tag_base}"
            # For phase-numbered tags like "1-CleanSuit", letter goes before: "1a-CleanSuit"
            if tag_base[0].isdigit():
                num_part = tag_base.split("-", 1)
                lettered_tag = f"_{num_part[0]}{suffix}-{num_part[1]}" if suffix else f"_{tag_base}"
            else:
                lettered_tag = f"_{tag_base}{suffix}" if suffix else f"_{tag_base}"
            dated = char_dir / f"GrimGlow_Turnaround_{character}{lettered_tag}_{source_date}.png"
            if dated.exists():
                return dated

    # Search for any file matching the phase tag pattern (with optional letter suffix)
    # For "1-CleanSuit", match "1-CleanSuit", "1a-CleanSuit", "1b-CleanSuit", etc.
    if tag_base[0].isdigit():
        num_prefix = tag_base[0]
        tag_rest = tag_base[1:]  # e.g. "-CleanSuit"
        pattern = str(char_dir / f"GrimGlow_Turnaround_{character}_{num_prefix}*{tag_rest}_*.png")
    else:
        pattern = str(char_dir / f"GrimGlow_Turnaround_{character}_{tag_base}*.png")

    matches = sorted(glob.glob(pattern))

    if not matches:
        # Theodore fallback — undated file with optional a/b suffix
        if character == "Theodore" and effective_variant == "clean-suit":
            for suffix in ["_a", "_b", ""]:
                candidate = char_dir / f"GrimGlow_Turnaround_{character}{suffix}.png"
                if candidate.exists():
                    return candidate
        return None

    # Prefer 'a' suffix, then no suffix, then 'b', then 'c'
    def sort_key(path_str):
        name = Path(path_str).name
        if tag_base[0].isdigit():
            # Extract the letter between number and dash: "1a-CleanSuit" → 'a'
            after_num = name.split(f"_{num_prefix}")[1] if f"_{num_prefix}" in name else ""
            letter = after_num[0] if after_num and after_num[0].isalpha() and after_num[0] != '-' else ''
        else:
            letter = ''
        # Sort: 'a' first, then '' (no letter), then 'b', 'c'
        priority = {'a': 0, '': 1, 'b': 2, 'c': 3}.get(letter, 4)
        return priority

    matches.sort(key=sort_key)
    return Path(matches[0])


def find_gaps(img: Image.Image, debug: bool = False) -> list[int]:
    """Find the 3 vertical gaps between 4 figures by analyzing column variance."""
    arr = np.array(img.convert("RGB"), dtype=np.float32)
    h, w, _ = arr.shape

    y_start = int(h * 0.20)
    y_end = int(h * 0.80)
    sample = arr[y_start:y_end, :, :]

    col_std = sample.std(axis=(0, 2))
    threshold = np.percentile(col_std, 30)
    is_bg = col_std < threshold

    margin = int(w * 0.10)

    gaps = []
    in_gap = False
    gap_start = 0

    for x in range(margin, w - margin):
        if is_bg[x] and not in_gap:
            gap_start = x
            in_gap = True
        elif not is_bg[x] and in_gap:
            gap_end = x
            gap_width = gap_end - gap_start
            if gap_width > 5:
                gaps.append((gap_start, gap_end, gap_width))
            in_gap = False

    if in_gap:
        gaps.append((gap_start, w - margin, w - margin - gap_start))

    from itertools import combinations

    min_spacing = int(w * 0.12)
    best_combo = None
    best_score = float("inf")

    for combo in combinations(gaps, 3):
        mids = sorted((g[0] + g[1]) // 2 for g in combo)
        if any(mids[i+1] - mids[i] < min_spacing for i in range(2)):
            continue
        sections = [mids[0], mids[1] - mids[0], mids[2] - mids[1], w - mids[2]]
        avg = w / 4
        evenness = sum((s - avg) ** 2 for s in sections)
        total_width = sum(g[2] for g in combo)
        score = evenness - total_width * 10
        if score < best_score:
            best_score = score
            best_combo = combo

    if best_combo:
        top_gaps = list(best_combo)
    else:
        top_gaps = gaps[:3]

    top_gaps.sort(key=lambda g: g[0])

    if debug:
        print(f"    Threshold: {threshold:.1f}")
        print(f"    All gaps found: {len(gaps)}")
        for i, (start, end, width) in enumerate(top_gaps):
            mid = (start + end) // 2
            print(f"    Gap {i+1}: x={start}-{end} (width={width}, mid={mid})")

    return [(g[0] + g[1]) // 2 for g in top_gaps]


def split_turnaround(image_path: Path, character: str, output_dir: Path,
                     debug: bool = False, variant: str | None = None) -> list[Path]:
    """Split a turnaround sheet into 4 individual view images."""
    img = Image.open(image_path)
    w, h = img.size

    cuts = find_gaps(img, debug=debug)

    if len(cuts) != 3:
        print(f"  WARNING: Found {len(cuts)} gaps instead of 3 for {character}, "
              f"falling back to equal quarters")
        cuts = [w // 4, w // 2, 3 * w // 4]

    boundaries = [0] + cuts + [w]
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = []

    effective_variant = variant or "clean-suit"

    # Phase strips use phase names as "views" instead of angles
    if effective_variant == "phase-strip":
        view_names = PHASE_STRIP_VIEWS
        prefix = f"{character}_phase-strip_"
    elif character == "Theodore":
        view_names = VIEWS
        prefix = f"{character}_"
    else:
        if effective_variant in PHASE_MAP:
            view_tag = PHASE_MAP[effective_variant][1]
        else:
            view_tag = effective_variant
        view_names = VIEWS
        prefix = f"{character}_{view_tag}_"

    for i, view in enumerate(view_names):
        left = boundaries[i]
        right = boundaries[i + 1]
        cropped = img.crop((left, 0, right, h))

        out_path = output_dir / f"{prefix}{view}.png"
        cropped.save(out_path, "PNG")
        outputs.append(out_path)

    return outputs


def main():
    source_date = None
    variant = None
    characters = []
    debug = False
    run_all = False

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--source" and i + 1 < len(args):
            source_date = args[i + 1]
            i += 2
        elif args[i] == "--variant" and i + 1 < len(args):
            variant = args[i + 1]
            i += 2
        elif args[i] == "--all":
            run_all = True
            i += 1
        elif args[i] == "--debug":
            debug = True
            i += 1
        else:
            characters.append(args[i])
            i += 1

    if not characters:
        characters = CHARACTERS

    if run_all:
        variants_to_run = ALL_VARIANTS
    else:
        variants_to_run = [variant or "clean-suit"]

    for v in variants_to_run:
        for character in characters:
            turnaround = find_turnaround(character, source_date, variant=v)
            if turnaround is None:
                if run_all:
                    continue
                print(f"  SKIP  {character} ({v}) — no turnaround found")
                continue

            output_dir = SCRIPT_DIR / character / "views"
            outputs = split_turnaround(turnaround, character, output_dir,
                                       debug=debug, variant=v)

            print(f"  SPLIT {character} ({turnaround.name})")
            for out in outputs:
                print(f"        → {out.relative_to(SCRIPT_DIR)}")


if __name__ == "__main__":
    main()
