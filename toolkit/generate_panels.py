#!/usr/bin/env python3
"""Batch-generate comic panel art via ComfyUI API.

Parses GrimGlow production scripts, extracts per-panel art prompts,
maps characters to IP-Adapter reference images, and submits workflows
to ComfyUI for generation.

Usage:
    python3 toolkit/generate_panels.py --issue 1                    # Full issue
    python3 toolkit/generate_panels.py --issue 1 --page 1           # Single page
    python3 toolkit/generate_panels.py --issue 1 --page 3 --panel 2 # Resume from panel
    python3 toolkit/generate_panels.py --issue 1 --dry-run           # Preview without generating

Requires: ComfyUI running at localhost:8188 (via docker-compose.yml)
"""

import argparse
import glob
import json
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths — works from repo root
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = REPO_ROOT / "comic" / "scripts"

# Add wireframes dir to path so we can import parse_script
sys.path.insert(0, str(REPO_ROOT / "comic" / "wireframes"))
from generate_wireframes import parse_script  # noqa: E402

# ComfyUI API
COMFYUI_URL = "http://127.0.0.1:8188"

def _set_comfyui_url(url: str):
    global COMFYUI_URL
    COMFYUI_URL = url

def _set_checkpoint(name: str):
    global CHECKPOINT
    CHECKPOINT = name

# ---------------------------------------------------------------------------
# Character → IP-Adapter reference image mapping
# Files must exist in comfyui-data/ComfyUI/input/ (uploaded via API or copied)
# ---------------------------------------------------------------------------

CHARACTER_REFS = {
    "SABLE":    "sable_ref.png",
    "WREN":     "wren_ref.png",
    "JINK":     "jink_ref.png",
    "THRESH":   "thresh_ref.png",
    "LUMA":     "luma_ref.png",
    "THEODORE": "theodore_ref.png",
}

# Source turnaround sheets (for initial setup — copy to ComfyUI input dir)
CHARACTER_TURNAROUNDS = {
    "SABLE":    "Sable/GrimGlow_Turnaround_Sable_2026-03-09.png",
    "WREN":     "Wren/GrimGlow_Turnaround_Wren_2026-03-09.png",
    "JINK":     "Jink/GrimGlow_Turnaround_Jink_2026-03-09.png",
    "THRESH":   "Thresh/GrimGlow_Turnaround_Thresh_2026-03-09.png",
    "LUMA":     "Luma/GrimGlow_Turnaround_Luma_2026-03-09.png",
    "THEODORE": "Theodore/GrimGlow_Turnaround_Theodore_2026-03-08.png",
}

# ---------------------------------------------------------------------------
# Model configuration — Flux-dev (GGUF quantized for 8GB VRAM)
# ---------------------------------------------------------------------------

FLUX_UNET = "flux1-dev-Q4_0.gguf"
FLUX_CLIP_L = "clip_l.safetensors"
FLUX_T5XXL = "t5xxl_fp8_e4m3fn.safetensors"
FLUX_VAE = "ae.safetensors"

# Character LoRA — single multi-character model trained on all 6 characters.
# Loaded conditionally at runtime (skipped if file not found in ComfyUI).
LORA_MODEL = "grimglow_characters.safetensors"
LORA_STRENGTH = 0.75
LORA_AVAILABLE = False  # set at startup by check_lora()

# Trigger words per character — prepended to prompts for text conditioning.
# These activate the LoRA's per-character learning when the LoRA is loaded.
CHARACTER_TRIGGERS = {
    "SABLE":    "grimglow_sable",
    "WREN":     "grimglow_wren",
    "JINK":     "grimglow_jink",
    "THRESH":   "grimglow_thresh",
    "LUMA":     "grimglow_luma",
    "THEODORE": "grimglow_theodore",
}

# Negative prompt — reduces hallucinated extra figures and duplicates.
# Flux-dev doesn't lean on negatives as hard as SDXL, but it still helps.
NEGATIVE_PROMPT = (
    "extra people, crowd, bystanders, duplicate figures, "
    "multiple copies of same character"
)

# ---------------------------------------------------------------------------
# Shot type → panel dimensions
# ---------------------------------------------------------------------------

LANDSCAPE_SHOTS = {"EST", "XWIDE", "WIDE"}

# Establishing / extreme wide shots rarely show characters in close enough
# detail for IP-Adapter to help — it just pulls the reference figure into frame.
SKIP_IPADAPTER_SHOTS = {"EST", "XWIDE"}

def get_panel_dimensions(shot_abbr: str, width_hint: str = "") -> tuple[int, int]:
    """Return (width, height) for a panel based on layout width hint and shot type.

    Matches panel generation size to the actual comic layout slot.
    All dimensions are Flux-friendly multiples of 64.
    """
    hint = width_hint.lower()

    # --- Full-page splash ---
    if "full-page splash" in hint or "splash" in hint and "half" not in hint:
        return 1024, 1536  # tall full-page

    # --- Narrow strips (full width but very short) ---
    if "narrow strip" in hint:
        return 1536, 512  # wide cinematic strip

    # --- Widescreen / letterbox ---
    if "widescreen" in hint or "letterbox" in hint:
        return 1536, 640  # ultra-wide

    # --- Full width (standard height) ---
    if "full width" in hint:
        if "top half" in hint or "half-page" in hint:
            return 1536, 768  # full width, tall
        if "top quarter" in hint:
            return 1536, 512  # full width, short
        return 1536, 832  # full width, standard

    # --- Two-thirds / Wide ---
    if "two-thirds" in hint or "wide," in hint:
        if shot_abbr in LANDSCAPE_SHOTS:
            return 1024, 768
        return 1024, 1216  # tall two-thirds

    # --- Half width ---
    if "half width" in hint or "half," in hint:
        if shot_abbr in LANDSCAPE_SHOTS:
            return 832, 640
        return 768, 1024  # standard half

    # --- One-third / Narrow ---
    if "one-third" in hint or "narrow" in hint:
        if shot_abbr in LANDSCAPE_SHOTS:
            return 640, 512
        return 512, 1024  # tall narrow

    # --- Quarter width ---
    if "quarter" in hint:
        return 384, 1024  # very narrow vertical strip

    # --- Fallback: use shot type ---
    if shot_abbr in LANDSCAPE_SHOTS:
        return 1216, 832  # landscape
    return 832, 1216  # portrait (default)


# ---------------------------------------------------------------------------
# Prompt preparation — inject consistency guardrails
# ---------------------------------------------------------------------------

# --- Scale detection keywords ---
# Direct fairy-scale mentions
SCALE_KEYWORDS = [
    "fairy scale", "fairy-scale", "four inch", "four-inch",
    "gutter", "rain gutter", "rooftop", "chimney", "slate",
    "tiles", "tile", "ledge", "lead flashing",
]

# Victorian environment terms — when a squad character is in this environment,
# they must be fairy-scale (4 inches tall). Theodore and human witnesses are not.
VICTORIAN_ENV_KEYWORDS = [
    "cobblestone", "gaslight", "gas lamp", "church spire",
    "victorian street", "london street", "chimney pot",
    "terraced house", "alley", "workshop", "wreckage",
]
FAIRY_SCALE_CHARACTERS = {"SABLE", "WREN", "JINK", "THRESH", "LUMA"}

# --- Canonical ship descriptions ---
# Injected into ship-visible panels so Flux generates a consistent design.

# Exterior: the ship as seen from outside
SHIP_DESCRIPTION = (
    "The vessel is a compact angular dark-hulled military recon ship "
    "shaped like a predatory fish, blue-white light bleeding from hull seams "
    "and viewports, conduit lines tracing the underbelly, narrow and functional."
)
SHIP_KEYWORDS = ["vessel", "spacecraft", "recon ship"]

# Interior: the bridge/cockpit as seen from inside
BRIDGE_DESCRIPTION = (
    "The bridge interior resembles a submarine cockpit: compact, functional, "
    "every surface purposeful. Narrow rectangular viewports (NOT round, NOT circular) "
    "show the exterior. Holographic displays float at workstations in geometric "
    "blue-white light. Overhead panels provide clinical white lighting. "
    "The space is small and cramped, crew members close together."
)
# These are multi-word phrases to avoid false positives on wreckage descriptions
# like "shattered console half-buried in debris" which mention "console" but
# aren't bridge-interior scenes.
BRIDGE_KEYWORDS = [
    "bridge archway", "command station", "command console",
    "engineering console", "workstation", "cockpit",
    "jump seat",
]


def prepare_prompt(
    art_prompt: str,
    speakers: list[str],
    shot_abbr: str,
) -> str:
    """Inject figure-count, scale, and ship-design guardrails into art prompts.

    Called before build_workflow() to reduce ghost characters, scale drift,
    and ship design inconsistency.
    """
    parts = [art_prompt]
    prompt_lower = art_prompt.lower()

    # --- Figure count enforcement (skip wide/establishing shots) ---
    if shot_abbr not in SKIP_IPADAPTER_SHOTS:
        n = len(speakers)
        if n == 1:
            parts.append("single figure only, no other people in frame")
        elif n >= 2:
            parts.append(
                f"exactly {n} figures visible, no bystanders, "
                "no background people"
            )

    # --- Scale reinforcement for fairy-scale scenes ---
    needs_scale = False

    # Check 1: direct fairy-scale environment keywords
    if any(kw in prompt_lower for kw in SCALE_KEYWORDS):
        needs_scale = True

    # Check 2: squad character in Victorian environment
    if not needs_scale and speakers:
        has_fairy_char = any(s in FAIRY_SCALE_CHARACTERS for s in speakers)
        has_victorian_env = any(kw in prompt_lower for kw in VICTORIAN_ENV_KEYWORDS)
        if has_fairy_char and has_victorian_env:
            needs_scale = True

    if needs_scale and "four-inch-tall" not in prompt_lower:
        parts.append(
            "four-inch-tall miniature figure, fairy scale, "
            "tiny against the enormous Victorian environment"
        )

    # --- Ship design consistency ---
    if any(kw in prompt_lower for kw in SHIP_KEYWORDS):
        parts.append(SHIP_DESCRIPTION)

    # --- Bridge interior consistency ---
    if any(kw in prompt_lower for kw in BRIDGE_KEYWORDS):
        parts.append(BRIDGE_DESCRIPTION)

    return " ".join(parts)


# ---------------------------------------------------------------------------
# Workflow builder
# ---------------------------------------------------------------------------

def build_workflow(
    art_prompt: str,
    width: int,
    height: int,
    filename_prefix: str,
    character_ref: str | None = None,
    character_trigger: str | None = None,
    seed: int = 0,
) -> dict:
    """Build a ComfyUI API workflow for a single panel using Flux-dev.

    Returns the full prompt dict ready for /prompt endpoint.
    Flux uses T5-XXL for long text understanding — no 77-token limit.
    When a character LoRA is available and a trigger word is active,
    a LoraLoader node is inserted to activate per-character conditioning.
    """
    positive_text = f"{character_trigger}, {art_prompt}" if character_trigger else art_prompt

    workflow = {}

    # Node 1: UnetLoaderGGUF (Flux-dev quantized)
    workflow["1"] = {
        "class_type": "UnetLoaderGGUF",
        "inputs": {"unet_name": FLUX_UNET},
    }

    # Node 10: LoraLoader (conditional — only when LoRA available + character active)
    use_lora = LORA_AVAILABLE and character_trigger is not None
    if use_lora:
        workflow["10"] = {
            "class_type": "LoraLoader",
            "inputs": {
                "lora_name": LORA_MODEL,
                "strength_model": LORA_STRENGTH,
                "strength_clip": LORA_STRENGTH,
                "model": ["1", 0],
                "clip": ["2", 0],
            },
        }

    # The model source for KSampler: LoRA output if loaded, else raw UNet
    model_source = ["10", 0] if use_lora else ["1", 0]
    # The CLIP source for text encoding: LoRA output if loaded, else raw CLIP
    clip_source = ["10", 1] if use_lora else ["2", 0]

    # Node 2: DualCLIPLoader (CLIP-L + T5-XXL for Flux)
    workflow["2"] = {
        "class_type": "DualCLIPLoader",
        "inputs": {
            "clip_name1": FLUX_CLIP_L,
            "clip_name2": FLUX_T5XXL,
            "type": "flux",
        },
    }

    # Node 3: CLIPTextEncode (positive)
    workflow["3"] = {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "text": positive_text,
            "clip": clip_source,
        },
    }

    # Node 4: CLIPTextEncode (negative)
    workflow["4"] = {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "text": NEGATIVE_PROMPT,
            "clip": clip_source,
        },
    }

    # Node 5: EmptySD3LatentImage (Flux uses SD3 latent format)
    workflow["5"] = {
        "class_type": "EmptySD3LatentImage",
        "inputs": {
            "width": width,
            "height": height,
            "batch_size": 1,
        },
    }

    # Node 6: KSampler (Flux-dev — 20 steps, CFG 2.0 for GGUF Q4_0)
    workflow["6"] = {
        "class_type": "KSampler",
        "inputs": {
            "seed": seed,
            "steps": 20,
            "cfg": 2.0,
            "sampler_name": "euler",
            "scheduler": "simple",
            "denoise": 1.0,
            "model": model_source,
            "positive": ["3", 0],
            "negative": ["4", 0],
            "latent_image": ["5", 0],
        },
    }

    # Node 7: VAELoader (Flux VAE loaded separately)
    workflow["7"] = {
        "class_type": "VAELoader",
        "inputs": {"vae_name": FLUX_VAE},
    }

    # Node 8: VAEDecode
    workflow["8"] = {
        "class_type": "VAEDecode",
        "inputs": {
            "samples": ["6", 0],
            "vae": ["7", 0],
        },
    }

    # Node 9: SaveImage
    workflow["9"] = {
        "class_type": "SaveImage",
        "inputs": {
            "filename_prefix": filename_prefix,
            "images": ["8", 0],
        },
    }

    return {"prompt": workflow}


# ---------------------------------------------------------------------------
# ComfyUI API client
# ---------------------------------------------------------------------------

def submit_prompt(workflow: dict) -> str:
    """Submit a workflow to ComfyUI and return the prompt_id."""
    data = json.dumps(workflow).encode("utf-8")
    req = urllib.request.Request(
        f"{COMFYUI_URL}/prompt",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
    return result["prompt_id"]


def wait_for_completion(prompt_id: str, poll_interval: float = 2.0, timeout: float = 600.0):
    """Poll ComfyUI until the prompt is complete or times out."""
    start = time.time()
    while time.time() - start < timeout:
        try:
            req = urllib.request.Request(f"{COMFYUI_URL}/history/{prompt_id}")
            with urllib.request.urlopen(req, timeout=10) as resp:
                history = json.loads(resp.read())
            if prompt_id in history:
                outputs = history[prompt_id].get("outputs", {})
                status = history[prompt_id].get("status", {})
                # Check if SaveImage node (node 9) produced output
                if "9" in outputs and outputs["9"].get("images"):
                    return outputs["9"]["images"]
                # Cached execution — completed but outputs dict is empty
                if status.get("status_str") == "success" and not outputs:
                    return [{"filename": "cached", "subfolder": "", "type": "output"}]
                # Check for errors
                if status.get("status_str") == "error":
                    msgs = status.get("messages", [])
                    print(f"  ERROR: {msgs}")
                    return None
        except urllib.error.URLError:
            pass
        time.sleep(poll_interval)

    print(f"  TIMEOUT waiting for prompt {prompt_id}")
    return None


def check_comfyui() -> bool:
    """Check if ComfyUI is reachable."""
    try:
        req = urllib.request.Request(f"{COMFYUI_URL}/system_stats")
        with urllib.request.urlopen(req, timeout=5) as resp:
            resp.read()
        return True
    except (urllib.error.URLError, OSError):
        return False


def check_lora() -> bool:
    """Check if the character LoRA model is available in ComfyUI.

    Queries the ComfyUI object_info endpoint for LoraLoader and checks
    if our model appears in the available lora list. Falls back gracefully.
    """
    global LORA_AVAILABLE
    try:
        req = urllib.request.Request(f"{COMFYUI_URL}/object_info/LoraLoader")
        with urllib.request.urlopen(req, timeout=5) as resp:
            info = json.loads(resp.read())
        lora_list = (
            info.get("LoraLoader", {})
            .get("input", {})
            .get("required", {})
            .get("lora_name", [[]])[0]
        )
        if LORA_MODEL in lora_list:
            LORA_AVAILABLE = True
            print(f"LoRA: {LORA_MODEL} found")
            return True
        else:
            print(f"LoRA: {LORA_MODEL} not found — generating without LoRA")
            return False
    except (urllib.error.URLError, OSError, KeyError, IndexError):
        print(f"LoRA: could not query ComfyUI — generating without LoRA")
        return False


# ---------------------------------------------------------------------------
# Script finder
# ---------------------------------------------------------------------------

def find_script(issue_num: int) -> Path:
    """Find the script file for a given issue number."""
    pattern = str(SCRIPT_DIR / f"Issue{issue_num:02d}_*_Script.md")
    matches = glob.glob(pattern)
    if not matches:
        print(f"ERROR: No script found for Issue {issue_num}")
        print(f"  Searched: {pattern}")
        sys.exit(1)
    return Path(matches[0])


# ---------------------------------------------------------------------------
# Main batch generation
# ---------------------------------------------------------------------------

def generate_panels(
    issue_num: int,
    start_page: int = 1,
    end_page: int = 0,
    start_panel: int = 1,
    dry_run: bool = False,
):
    """Generate all panels for an issue (or subset)."""
    script_path = find_script(issue_num)
    print(f"Script: {script_path.name}")

    pages = parse_script(script_path)
    print(f"Parsed: {len(pages)} pages")

    # Count total panels
    total = sum(len(p["panels"]) for p in pages)
    skipped = 0
    generated = 0
    errors = 0

    for page in pages:
        pnum = page["page_num"]
        if pnum < start_page:
            skipped += len(page["panels"])
            continue
        if end_page > 0 and pnum > end_page:
            skipped += len(page["panels"])
            continue

        for panel in page["panels"]:
            panel_num = panel["num"]

            # Resume support
            if pnum == start_page and panel_num < start_panel:
                skipped += 1
                continue

            art_prompt = panel.get("art_prompt", "")
            if not art_prompt:
                print(f"  Page {pnum} Panel {panel_num}: SKIP (no art prompt)")
                skipped += 1
                continue

            # Determine character reference from dialogue speakers
            speakers = [
                d["speaker"] for d in panel["dialogue"]
                if d["type"] == "speech" and d["speaker"] in CHARACTER_REFS
            ]
            char_ref = CHARACTER_REFS.get(speakers[0]) if speakers else None

            # Skip IP-Adapter and character LoRA on establishing/extreme wide
            # shots — characters aren't visible enough, and the LoRA bleeds
            # character features into non-character scenes (e.g. water ships).
            if panel["shot_abbr"] in SKIP_IPADAPTER_SHOTS:
                char_ref = None
                speakers = []  # also prevents trigger word + LoRA loading

            # Panel dimensions — use layout width hint for proper sizing
            width_hint = panel.get("width_hint", "")
            width, height = get_panel_dimensions(panel["shot_abbr"], width_hint)

            # Deterministic seed
            seed = issue_num * 10000 + pnum * 100 + panel_num

            # Output path
            filename_prefix = f"issue{issue_num:02d}/page{pnum:02d}_panel{panel_num:02d}"

            char_name = speakers[0] if speakers else "none"
            orientation = "landscape" if panel["shot_abbr"] in LANDSCAPE_SHOTS else "portrait"

            print(
                f"  Page {pnum:2d} Panel {panel_num}: "
                f"{panel['shot_abbr']:5s} {width:4d}x{height:<4d} "
                f"char={char_name:8s} seed={seed}"
            )

            if dry_run:
                generated += 1
                continue

            # Character trigger word for LoRA activation
            char_trigger = CHARACTER_TRIGGERS.get(speakers[0]) if speakers else None

            # Inject figure-count and scale guardrails
            art_prompt = prepare_prompt(art_prompt, speakers, panel["shot_abbr"])

            # Build and submit workflow
            workflow = build_workflow(
                art_prompt=art_prompt,
                width=width,
                height=height,
                filename_prefix=filename_prefix,
                character_ref=char_ref,
                character_trigger=char_trigger,
                seed=seed,
            )

            try:
                prompt_id = submit_prompt(workflow)
                print(f"    → Submitted: {prompt_id[:8]}...", end="", flush=True)

                images = wait_for_completion(prompt_id)
                if images:
                    print(f" DONE ({images[0]['filename']})")
                    generated += 1
                else:
                    print(" FAILED")
                    errors += 1
            except Exception as e:
                print(f"    → ERROR: {e}")
                errors += 1

    print(f"\nSummary: {generated} generated, {skipped} skipped, {errors} errors (of {total} total)")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Batch-generate GrimGlow comic panels")
    parser.add_argument("--issue", type=int, required=True, help="Issue number (1-12)")
    parser.add_argument("--page", type=int, default=1, help="Start from page N")
    parser.add_argument("--end-page", type=int, default=0, help="Stop after page N (0 = all)")
    parser.add_argument("--panel", type=int, default=1, help="Start from panel N (on start page)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without generating")
    parser.add_argument("--url", default=COMFYUI_URL, help="ComfyUI API URL")
    args = parser.parse_args()

    _set_comfyui_url(args.url)

    if not args.dry_run:
        if not check_comfyui():
            print(f"ERROR: ComfyUI not reachable at {COMFYUI_URL}")
            print("  Start it with: bash toolkit/gpu-swap.sh comfyui")
            sys.exit(1)
        print(f"ComfyUI: {COMFYUI_URL} ✓")
        check_lora()

    generate_panels(
        issue_num=args.issue,
        start_page=args.page,
        end_page=args.end_page,
        start_panel=args.panel,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
