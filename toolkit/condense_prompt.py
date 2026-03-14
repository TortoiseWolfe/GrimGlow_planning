#!/usr/bin/env python3
"""Condense GrimGlow art prompts to fit SDXL's ~77-token CLIP window.

Rebuilds each prompt using structured character data + extracted scene keywords,
targeting ~62 tokens (leaving 15 headroom for the "oil painting, science fiction,"
prefix added by generate_panels.py).

Usage:
    python3 toolkit/condense_prompt.py --issue 1 --page 1   # Preview single page
    python3 toolkit/condense_prompt.py --issue 1             # Preview full issue
"""

import argparse
import glob
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "comic" / "wireframes"))
from generate_wireframes import parse_script  # noqa: E402

SCRIPT_DIR = REPO_ROOT / "comic" / "scripts"

# ---------------------------------------------------------------------------
# Character identity tags — traits IP-Adapter does NOT reliably transfer
# (skin tone, hair, ethnicity, build). Suit color reinforces IP-Adapter.
# ---------------------------------------------------------------------------

CHARACTER_TAGS = {
    "SABLE": {
        "identity": "woman, late 30s, dark brown skin, very short military-cropped silver-white hair",
        "suit": "silver metallic suit, blue-white holographic nodes",
    },
    "WREN": {
        "identity": "woman, early 30s, East Asian, dark hair in high messy bun, wiry build",
        "suit": "copper metallic suit, copper-gold holographic nodes",
    },
    "JINK": {
        "identity": "young adult late teens, androgynous, golden blonde curly hair, lean build",
        "suit": "emerald metallic suit, emerald holographic nodes",
    },
    "THRESH": {
        "identity": "muscular woman, powerful athletic build, pale skin, copper-red buzz cut",
        "suit": "ruby-crimson metallic suit, heavy armor plating, crimson nodes",
    },
    "LUMA": {
        "identity": "woman, late 20s, South Asian, warm brown skin, long dark hair in thick braid",
        "suit": "sapphire-violet metallic suit, holographic lenses",
    },
    "THEODORE": {
        "identity": "lanky pre-teen boy 12-13, sandy-brown hair, hazel eyes",
        "suit": "collarless shirt, leather waistcoat, patched trousers",
    },
}

# ---------------------------------------------------------------------------
# Shot type → CLIP-effective camera description
# ---------------------------------------------------------------------------

SHOT_CAMERA_MAP = {
    "EST":    "establishing wide shot",
    "XWIDE":  "extreme wide shot",
    "WIDE":   "wide shot",
    "MW":     "medium wide shot",
    "MED":    "medium shot",
    "MCU":    "medium close-up",
    "CU":     "close-up portrait",
    "ECU":    "extreme close-up",
    "POV":    "point of view shot",
    "DYN":    "dynamic action shot",
    "RXN":    "reaction close-up",
    "SPLASH": "full page illustration",
}

# ---------------------------------------------------------------------------
# SDXL synonym replacements — narrative → visual
# ---------------------------------------------------------------------------

SDXL_SYNONYMS = [
    # Order matters — longer phrases first to avoid partial matches
    ("recon vessel", "spacecraft"),
    ("military vessel", "spacecraft"),
    ("vessel in full profile", "spacecraft in full profile"),
    ("vessel", "spacecraft"),
    ("temporal corridor", "glowing energy tunnel in space"),
    ("holographic display", "glowing translucent screen"),
    ("holographic", "glowing"),
    ("fairy-scale", "miniature scale"),
    ("fairy scale", "miniature scale"),
    ("wing-pack", "translucent dragonfly wings"),
    ("department-colored", ""),
    ("department colored", ""),
]

# Phrases to strip entirely — narrative language CLIP ignores
STRIP_PHRASES = [
    "Painterly illustrated style, rich detail.",
    "Painterly illustrated style, rich detail. ",
    "Oil paint texture, visible brushwork,",
    "Oil paint texture, visible brushwork.",
    "oil paint texture, visible brushwork",
    "visible brushwork,",
    "visible brushwork.",
]

# Narrative phrases that waste tokens
NARRATIVE_DROPS = [
    r"muscle memory",
    r"quiet command authority",
    r"practiced efficiency",
    r"the face of someone who has done this many times",
    r"completely at home in \w+ role",
    r"the mood is [\w\s,—–-]+\.",
    r"The mood is [\w\s,—–-]+\.",
    r"This is who \w+ was —[^.]+\.",
]

# Camera lens specs to strip
LENS_PATTERN = re.compile(r"\b\d{2,3}mm\s*(wide|telephoto|lens)?\b\.?\s*", re.IGNORECASE)

# ---------------------------------------------------------------------------
# Environment and lighting keyword extraction
# ---------------------------------------------------------------------------

ENVIRONMENT_KEYWORDS = [
    "rooftop", "gutter", "rain gutter", "bridge", "corridor", "street",
    "workshop", "chimney", "slate", "cobblestone", "fog", "gaslight",
    "wreckage", "debris", "archway", "viewport", "console", "cockpit",
    "jump seat", "doorway", "tiles", "moss", "iron", "cast-iron",
    "church spire", "cobblestones", "shop fronts", "alley",
    "Victorian", "London",
]

LIGHTING_KEYWORDS = [
    "amber", "blue-white", "prismatic", "gaslight", "warm light",
    "cool light", "crimson", "copper-gold", "blue-violet", "red emergency",
    "dual lighting", "chiaroscuro", "no warm light", "cool prismatic",
    "emergency lighting", "strobe", "geometric light",
]

# ---------------------------------------------------------------------------
# Token estimation
# ---------------------------------------------------------------------------

def estimate_tokens(text: str) -> int:
    """Rough CLIP BPE token estimate. ~1.3 tokens per word."""
    words = text.split()
    return int(len(words) * 1.3)


def _trim_to_tokens(text: str, target: int) -> str:
    """Trim text from the end to fit within target token count."""
    words = text.split()
    while estimate_tokens(" ".join(words)) > target and len(words) > 5:
        words.pop()
    return " ".join(words)


# ---------------------------------------------------------------------------
# Core prompt condensation
# ---------------------------------------------------------------------------

def condense_prompt(
    art_prompt: str,
    characters: list[str],
    shot_abbr: str,
    ipadapter_active: bool = False,
    target_tokens: int = 62,
) -> str:
    """Condense an art prompt to fit SDXL's CLIP token window.

    When ipadapter_active=True, emits only skin/hair identity tags (not suit)
    to avoid IP-Adapter + text both describing the character → duplicate figures.

    Returns the condensed prompt WITHOUT the "oil painting, science fiction,"
    prefix (that's added by build_workflow in generate_panels.py).
    """
    # --- 1. Clean the raw prompt ---
    cleaned = art_prompt

    # Strip style prefixes/suffixes (LoRA handles these)
    for phrase in STRIP_PHRASES:
        cleaned = cleaned.replace(phrase, "")

    # Apply SDXL synonyms
    for old, new in SDXL_SYNONYMS:
        cleaned = cleaned.replace(old, new)

    # Drop camera lens specs
    cleaned = LENS_PATTERN.sub("", cleaned)

    # Drop narrative phrases
    for pattern in NARRATIVE_DROPS:
        cleaned = re.sub(pattern, "", cleaned, flags=re.IGNORECASE)

    # Clean up whitespace
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    cleaned = re.sub(r"\s*[,—–-]\s*[,—–-]\s*", ", ", cleaned)

    # --- 2. Build structured prompt parts ---
    parts = []

    # Shot type
    shot_text = SHOT_CAMERA_MAP.get(shot_abbr, "")
    if shot_text:
        parts.append(shot_text)

    # Character identity block
    # Filter to characters actually VISIBLE in the panel — off-panel speakers
    # appear in dialogue but aren't described in the art prompt.
    is_establishing = shot_abbr in {"EST", "XWIDE"}
    prompt_lower = cleaned.lower()
    visible_chars = [c for c in characters if c.lower() in prompt_lower]
    # Fallback: if no characters found in text but we have speakers, use first
    if not visible_chars and characters and not is_establishing:
        visible_chars = characters[:1]
    char_tags = []

    if visible_chars and not is_establishing:
        for char_name in visible_chars[:2]:  # max 2 characters
            tags = CHARACTER_TAGS.get(char_name)
            if tags:
                identity = tags["identity"]
                # When IP-Adapter is active, skip suit description to avoid
                # text + IP-Adapter both describing the same figure → duplicates.
                # IP-Adapter handles suit design; text handles skin/hair only.
                if ipadapter_active:
                    char_tags.append(identity)
                else:
                    suit = tags.get("suit", "")
                    char_tags.append(f"{identity}, {suit}" if suit else identity)

        # Duplicate prevention
        if len(visible_chars) == 1:
            parts.append("single figure")
        elif len(visible_chars) >= 2:
            parts.append("two figures")

        for tag in char_tags:
            parts.append(tag)

    # --- 3. Extract scene subject ---
    # Split into sentences, find the action/composition sentence
    sentences = re.split(r'(?<=[.!])\s+', cleaned)

    # Filter out sentences that are purely character descriptions or lighting
    scene_sentences = []
    for s in sentences:
        s_lower = s.lower()
        # Skip if it's mostly character physical description
        if any(kw in s_lower for kw in ["skin", "hair", "build", "features", "eyes"]):
            if any(kw in s_lower for kw in ["she is", "he is", "they are", "a woman", "a man"]):
                continue
        # Skip pure lighting sentences
        if s_lower.startswith("the ") and any(kw in s_lower for kw in ["lighting", "light from", "illuminat"]):
            continue
        if s_lower.startswith("no warm") or s_lower.startswith("cool ") and "light" in s_lower:
            continue
        scene_sentences.append(s)

    # Take the most descriptive scene sentences (up to ~15 words total for char panels)
    scene_budget = 20 if is_establishing else 15
    scene_words = []
    for s in scene_sentences:
        words = s.split()
        if len(scene_words) + len(words) <= scene_budget:
            scene_words.extend(words)
        elif not scene_words:
            # At least get the first sentence truncated
            scene_words = words[:scene_budget]
            break
        else:
            break

    if scene_words:
        scene_text = " ".join(scene_words).rstrip(".,;")
        parts.append(scene_text)

    # --- 4. Extract environment keywords ---
    prompt_lower = cleaned.lower()
    found_env = []
    for kw in ENVIRONMENT_KEYWORDS:
        if kw.lower() in prompt_lower:
            found_env.append(kw)
    # Deduplicate and limit
    found_env = list(dict.fromkeys(found_env))[:4]
    if found_env:
        parts.append(", ".join(found_env))

    # --- 5. Extract lighting keywords ---
    found_light = []
    for kw in LIGHTING_KEYWORDS:
        kw_lower = kw.lower()
        if kw_lower in prompt_lower:
            # Skip if preceded by negation ("no warm light" → don't add "warm light")
            idx = prompt_lower.find(kw_lower)
            before = prompt_lower[max(0, idx - 4):idx].strip()
            if before.endswith("no") or before.endswith("not") or before.endswith("without"):
                continue
            found_light.append(kw)
    found_light = list(dict.fromkeys(found_light))[:3]
    if found_light:
        parts.append(", ".join(found_light))

    # --- 6. Assemble and trim ---
    result = ", ".join(parts)

    # Clean up
    result = re.sub(r",\s*,", ",", result)
    result = re.sub(r"\s+", " ", result).strip().rstrip(",").strip()

    # Trim if over budget (drop from the end — lighting/env go first)
    if estimate_tokens(result) > target_tokens:
        result = _trim_to_tokens(result, target_tokens)

    return result


# ---------------------------------------------------------------------------
# CLI test mode
# ---------------------------------------------------------------------------

def find_script(issue_num: int) -> Path:
    pattern = str(SCRIPT_DIR / f"Issue{issue_num:02d}_*_Script.md")
    matches = glob.glob(pattern)
    if not matches:
        print(f"ERROR: No script for Issue {issue_num}")
        sys.exit(1)
    return Path(matches[0])


def test_issue(issue_num: int, page_filter: int = 0):
    """Print before/after prompt comparison for an issue."""
    script = find_script(issue_num)
    pages = parse_script(script)

    total = 0
    over_budget = 0

    for page in pages:
        pnum = page["page_num"]
        if page_filter and pnum != page_filter:
            continue

        for panel in page["panels"]:
            art_prompt = panel.get("art_prompt", "")
            if not art_prompt:
                continue

            # Extract characters from dialogue
            speakers = [
                d["speaker"] for d in panel["dialogue"]
                if d["type"] == "speech" and d["speaker"] in CHARACTER_TAGS
            ]
            characters = list(dict.fromkeys(speakers))  # dedupe, preserve order

            shot = panel["shot_abbr"]

            condensed = condense_prompt(art_prompt, characters, shot)
            orig_tokens = estimate_tokens(art_prompt)
            new_tokens = estimate_tokens(condensed)

            total += 1
            flag = ""
            if new_tokens > 62:
                over_budget += 1
                flag = " *** OVER BUDGET ***"

            chars_str = "+".join(characters) if characters else "none"
            print(f"\n--- Page {pnum} Panel {panel['num']} ({shot}, {chars_str}){flag}")
            print(f"  BEFORE ({orig_tokens:3d} tokens): {art_prompt[:120]}...")
            print(f"  AFTER  ({new_tokens:3d} tokens): {condensed}")

    print(f"\n{'='*60}")
    print(f"Total: {total} panels, {over_budget} over 62-token budget")


def main():
    parser = argparse.ArgumentParser(description="Test prompt condensation")
    parser.add_argument("--issue", type=int, required=True)
    parser.add_argument("--page", type=int, default=0, help="Filter to single page")
    args = parser.parse_args()

    test_issue(args.issue, args.page)


if __name__ == "__main__":
    main()
