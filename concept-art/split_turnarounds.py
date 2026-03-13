#!/usr/bin/env python3
"""Split character turnaround sheets into individual view images.

Detects the gaps between figures by analyzing column-wise variance against
the neutral background, then crops at the midpoint of each gap. This handles
turnarounds where figures are not evenly spaced (e.g. broader armor, braids,
hand-on-hip poses).

Usage:
  python3 split_turnarounds.py                    # Process all 6 characters (clean suits)
  python3 split_turnarounds.py --variant mid-mission  # Process mid-mission turnarounds
  python3 split_turnarounds.py --variant light-wear   # Process light-wear turnarounds
  python3 split_turnarounds.py --variant heavy-wear   # Process heavy-wear turnarounds
  python3 split_turnarounds.py Sable Wren         # Process specific characters
  python3 split_turnarounds.py --source 2026-03-08 # Use a different turnaround date
  python3 split_turnarounds.py --debug             # Show detected gap positions
"""

import sys
from pathlib import Path
from PIL import Image
import numpy as np

VIEWS = ["front", "three-quarter", "profile", "back"]
CHARACTERS = ["Sable", "Wren", "Jink", "Thresh", "Luma", "Theodore"]

SCRIPT_DIR = Path(__file__).parent


def find_turnaround(character: str, source_date: str | None = None,
                    variant: str | None = None) -> Path | None:
    """Find the turnaround image for a character, preferring the given date.

    variant: None for clean suit, "mid-mission" for MidMission, etc.
    """
    char_dir = SCRIPT_DIR / character
    if not char_dir.is_dir():
        return None

    # Build the variant tag for filenames (e.g. "_MidMission")
    variant_tag = f"_{''.join(w.capitalize() for w in variant.split('-'))}" if variant else ""

    if source_date:
        dated = char_dir / f"GrimGlow_Turnaround_{character}{variant_tag}_{source_date}.png"
        if dated.exists():
            return dated

    # Search for any file matching the variant pattern
    import glob
    pattern = str(char_dir / f"GrimGlow_Turnaround_{character}{variant_tag}_*.png")
    matches = sorted(glob.glob(pattern), reverse=True)  # newest date first

    if variant:
        # For variants, any match is good
        if matches:
            return Path(matches[0])
    else:
        # For clean suits, exclude files with variant tags (e.g. _MidMission_)
        clean_matches = [m for m in matches
                         if f"_Turnaround_{character}_20" in m]
        if clean_matches:
            return Path(clean_matches[0])
        # Fall back to undated
        candidate = char_dir / f"GrimGlow_Turnaround_{character}.png"
        if candidate.exists():
            return candidate

    return None


def find_gaps(img: Image.Image, debug: bool = False) -> list[int]:
    """Find the 3 vertical gaps between 4 figures by analyzing column variance.

    Strategy:
    1. Sample the middle 60% of the image height (skip floor/ceiling gradient)
    2. Compute per-column standard deviation across RGB channels
    3. Low-variance columns = background (neutral gray)
    4. Find contiguous runs of low-variance columns
    5. Pick the 3 widest runs in the inner 80% of the image width
    6. Return the midpoint of each gap
    """
    arr = np.array(img.convert("RGB"), dtype=np.float32)
    h, w, _ = arr.shape

    # Sample middle 60% of height to avoid floor shadows and top gradients
    y_start = int(h * 0.20)
    y_end = int(h * 0.80)
    sample = arr[y_start:y_end, :, :]

    # Per-column standard deviation across height and RGB channels
    col_std = sample.std(axis=(0, 2))  # shape: (w,)

    # Threshold: columns with low std are background
    # Use a relative threshold based on the distribution
    threshold = np.percentile(col_std, 30)

    is_bg = col_std < threshold

    # Only look for gaps in the inner 80% of width (avoid edges)
    margin = int(w * 0.10)

    # Find contiguous runs of background columns
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
            if gap_width > 5:  # ignore tiny gaps (noise)
                gaps.append((gap_start, gap_end, gap_width))
            in_gap = False

    if in_gap:
        gaps.append((gap_start, w - margin, w - margin - gap_start))

    # Select the best 3 gaps by scoring all valid combinations.
    # A good set of 3 gaps divides the image into 4 roughly equal sections
    # using the widest available gaps.
    from itertools import combinations

    min_spacing = int(w * 0.12)
    best_combo = None
    best_score = float("inf")

    for combo in combinations(gaps, 3):
        mids = sorted((g[0] + g[1]) // 2 for g in combo)

        # Reject if any two gaps too close
        if any(mids[i+1] - mids[i] < min_spacing for i in range(2)):
            continue

        # Score: variance of 4 section widths (lower = more even)
        sections = [mids[0], mids[1] - mids[0], mids[2] - mids[1], w - mids[2]]
        avg = w / 4
        evenness = sum((s - avg) ** 2 for s in sections)

        # Bonus for wider gaps (subtract total gap width scaled down)
        total_width = sum(g[2] for g in combo)
        score = evenness - total_width * 10

        if score < best_score:
            best_score = score
            best_combo = combo

    if best_combo:
        top_gaps = list(best_combo)
    else:
        # Fallback: widest 3
        top_gaps = gaps[:3]

    # Sort by position left to right
    top_gaps.sort(key=lambda g: g[0])

    if debug:
        print(f"    Threshold: {threshold:.1f}")
        print(f"    All gaps found: {len(gaps)}")
        for i, (start, end, width) in enumerate(top_gaps):
            mid = (start + end) // 2
            print(f"    Gap {i+1}: x={start}-{end} (width={width}, mid={mid})")

    # Return midpoints
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

    # Build crop boundaries: [0, cut1, cut2, cut3, width]
    boundaries = [0] + cuts + [w]

    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = []

    # Prefix for variant views: e.g. "Sable_mid-mission_front.png"
    prefix = f"{character}_{variant}_" if variant else f"{character}_"

    for i, view in enumerate(VIEWS):
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

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--source" and i + 1 < len(args):
            source_date = args[i + 1]
            i += 2
        elif args[i] == "--variant" and i + 1 < len(args):
            variant = args[i + 1]
            i += 2
        elif args[i] == "--debug":
            debug = True
            i += 1
        else:
            characters.append(args[i])
            i += 1

    if not characters:
        characters = CHARACTERS

    for character in characters:
        turnaround = find_turnaround(character, source_date, variant=variant)
        if turnaround is None:
            print(f"  SKIP  {character} — no turnaround found")
            continue

        output_dir = SCRIPT_DIR / character / "views"
        outputs = split_turnaround(turnaround, character, output_dir,
                                   debug=debug, variant=variant)

        print(f"  SPLIT {character} ({turnaround.name})")
        for out in outputs:
            print(f"        → {out.relative_to(SCRIPT_DIR)}")


if __name__ == "__main__":
    main()
