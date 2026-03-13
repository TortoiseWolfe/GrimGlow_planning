#!/usr/bin/env python3
"""Prepare LoRA training dataset from GrimGlow turnaround sheets + concept art.

Splits each 4-view turnaround (1536x1024) into individual views,
includes concept art where available, and generates caption files
for kohya_ss training.

Usage:
    python3 toolkit/prepare_training_data.py              # Prepare all characters
    python3 toolkit/prepare_training_data.py --char sable  # Single character
    python3 toolkit/prepare_training_data.py --dry-run     # Preview without writing
"""

import argparse
import re
from pathlib import Path
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parent.parent
CONCEPT_ART_DIR = REPO_ROOT / "concept-art"
OUTPUT_DIR = REPO_ROOT / "training-data"

# Character data — trigger words, identity, outfit, turnaround dates
CHARACTERS = {
    "sable": {
        "trigger": "grimglow_sable",
        "identity": "woman, late 30s, dark brown skin, silver-white cropped hair",
        "outfit": "silver metallic suit, blue-white holographic nodes",
        "turnaround": "Sable/GrimGlow_Turnaround_Sable_2026-03-09.png",
        "concept": "Sable/GrimGlow_Concept_Sable.png",
    },
    "wren": {
        "trigger": "grimglow_wren",
        "identity": "woman, early 30s, East Asian, dark hair messy knot, wiry build",
        "outfit": "copper metallic suit, copper-gold holographic nodes",
        "turnaround": "Wren/GrimGlow_Turnaround_Wren_2026-03-09.png",
        "concept": "Wren/GrimGlow_Concept_Wren.png",
    },
    "jink": {
        "trigger": "grimglow_jink",
        "identity": "young androgynous person, golden blonde curly hair, lean build",
        "outfit": "emerald metallic suit, emerald holographic nodes",
        "turnaround": "Jink/GrimGlow_Turnaround_Jink_2026-03-09.png",
        "concept": "Jink/GrimGlow_Concept_Jink.png",
    },
    "thresh": {
        "trigger": "grimglow_thresh",
        "identity": "woman, broad muscular build, pale skin, copper-red buzz cut",
        "outfit": "ruby-crimson metallic suit, heavy armor plating, crimson nodes",
        "turnaround": "Thresh/GrimGlow_Turnaround_Thresh_2026-03-09.png",
        "concept": "Thresh/GrimGlow_Concept_Thresh.png",
    },
    "luma": {
        "trigger": "grimglow_luma",
        "identity": "woman, late 20s, South Asian, warm brown skin, braided dark hair",
        "outfit": "sapphire-violet metallic suit, holographic lenses",
        "turnaround": "Luma/GrimGlow_Turnaround_Luma_2026-03-09.png",
        "concept": "Luma/GrimGlow_Concept_Luma.png",
    },
    "theodore": {
        "trigger": "grimglow_theodore",
        "identity": "boy, 12-13, slight, sandy-brown hair, hazel eyes",
        "outfit": "collarless shirt, leather waistcoat, patched trousers",
        "turnaround": "Theodore/GrimGlow_Turnaround_Theodore_2026-03-08.png",
        "concept": None,  # no concept art
    },
}

VIEW_TAGS = ["front view", "three quarter view", "side view", "back view"]

# No forced resize — save at native resolution to preserve proportions.
# sd-scripts bucketing handles mixed resolutions (384x1024, 1024x1536).


def build_caption(trigger: str, identity: str, outfit: str, view_tag: str) -> str:
    """Build a training caption for one image."""
    return f"{trigger}, {identity}, {outfit}, oil painting, science fiction, {view_tag}"


def prepare_character(name: str, data: dict, dry_run: bool = False) -> int:
    """Prepare training data for one character. Returns image count."""
    char_dir = OUTPUT_DIR / f"grimglow_{name}"
    count = 0

    # Split turnaround into 4 views
    turnaround_path = CONCEPT_ART_DIR / data["turnaround"]
    if not turnaround_path.exists():
        print(f"  WARNING: Turnaround not found: {turnaround_path}")
        return 0

    img = Image.open(turnaround_path)
    view_width = img.size[0] // 4  # 384px each

    for i, view_tag in enumerate(VIEW_TAGS):
        left = i * view_width
        crop = img.crop((left, 0, left + view_width, img.size[1]))
        # Save at native resolution (384x1024) — no stretch

        view_names = ["front", "34", "side", "back"]
        img_name = f"{name}_{view_names[i]}.png"
        txt_name = f"{name}_{view_names[i]}.txt"
        caption = build_caption(data["trigger"], data["identity"], data["outfit"], view_tag)

        if dry_run:
            print(f"  {img_name:25s} ({crop.size[0]}x{crop.size[1]}) → {caption[:80]}...")
        else:
            char_dir.mkdir(parents=True, exist_ok=True)
            crop.save(char_dir / img_name, "PNG")
            (char_dir / txt_name).write_text(caption)
            print(f"  {img_name}")

        count += 1

    # Include concept art if available
    if data["concept"]:
        concept_path = CONCEPT_ART_DIR / data["concept"]
        if concept_path.exists():
            concept_img = Image.open(concept_path)
            img_name = f"{name}_concept.png"
            txt_name = f"{name}_concept.txt"
            caption = build_caption(
                data["trigger"], data["identity"], data["outfit"],
                "character illustration"
            )

            if dry_run:
                print(f"  {img_name:25s} ({concept_img.size[0]}x{concept_img.size[1]}) → {caption[:80]}...")
            else:
                char_dir.mkdir(parents=True, exist_ok=True)
                concept_img.save(char_dir / img_name, "PNG")
                (char_dir / txt_name).write_text(caption)
                print(f"  {img_name}")

            count += 1

    return count


def main():
    parser = argparse.ArgumentParser(description="Prepare GrimGlow LoRA training data")
    parser.add_argument("--char", type=str, help="Single character name (e.g., sable)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    total = 0
    chars = {args.char: CHARACTERS[args.char]} if args.char else CHARACTERS

    for name, data in chars.items():
        print(f"\n{name.upper()} ({data['trigger']}):")
        count = prepare_character(name, data, args.dry_run)
        total += count

    print(f"\nTotal: {total} images {'(dry run)' if args.dry_run else 'created'}")
    if not args.dry_run:
        print(f"Output: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
