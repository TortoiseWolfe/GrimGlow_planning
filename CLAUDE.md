# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

GrimGlow is a multimedia IP spanning a comic series, a browser-based prologue (Three.js), and a full PC game (Unity). This repository is the **planning/design bible** — no code lives here. It contains the narrative, character, and visual design documents that drive all downstream production.

**Premise:** A squad of four-inch-tall soldiers from the far future crash-lands in a steampunk Victorian world. Their holographic tech reads as fairy magic. Their enormous enemies (the Titans) read as monsters. They accidentally become the origin of fairy tales.

## Repository Structure

```
docs/                  — Authoritative design documents (.md)
  Story_Bible          — Core IP: concept, characters, visual language, three-layer plot (Survival, Enemy, Paradox). Read this first.
  Product_Design_Requirements — Unity game tech design: AI architecture, scale system, stealth/combat, rendering.
  Two_Phase_Development_Plan  — Phase 1 Three.js browser prologue → Phase 2 Unity PC game. Shared Meshy.ai asset pipeline.
  style-guide          — Prose style guide for consistent narrative voice across all documents.

characters/            — Character reference prompts (.md)
  Character_Prompts    — Mid-mission painterly art prompts (Sable, Wren, Jink, Thresh, Luma, Theodore).
  Character_Turnarounds — Meshy.ai 3D model reference sheets. Clean suit + mid-mission variants, wing-pack detail sheet.
  wiki/                — Canonical character reference pages (one per character).
  brainstorms/         — Working brainstorm documents for character development and relationships.

comic/                 — Volume 1 comic production files (.md)
  Volume1_Plot_Outline   — 12-issue plot outline, three-act structure, per-issue breakdowns, character arcs, fairy tale echoes.
  Volume1_Script_Prompts — Full 22-page script generation prompts for all 12 issues. Feed alongside reference docs for complete scripts.
  Volume1_Issue_Prompts  — Painterly cover/key moment art prompts per issue.

concept-art/           — Character concept art and turnarounds (.png/.jpg)
  Sable/               — Concept art + turnarounds for Sable
  Wren/                — Concept art + turnarounds for Wren
  Jink/                — Concept art + turnarounds for Jink
  Thresh/              — Concept art + turnarounds for Thresh
  Luma/                — Concept art + turnarounds for Luma
  Theodore/            — Turnarounds for Theodore
  reference/           — Historical reference photos

world-building/        — World design, 3D asset prompts, and reference maps
  meshy-environment-prompts — 142 Meshy.ai 3D component prompts across 21 sections (buildings, NPCs, terrain, etc).
  maps/                — Historical maps: Booth poverty maps, Goad fire insurance plans, LIDAR heightmaps.
  reference-photos/    — Victorian London reference photographs.
  brainstorms/         — Working brainstorm documents for world-building and lore.
```

## Key Characters

| Character | Role | Suit Color | Visual Key | Arc |
|-----------|------|------------|------------|-----|
| **Sable** | Captain | Silver (command) | Dark brown skin, silver-white cropped hair, authority | Command without a chain of command |
| **Wren** | Engineer | Copper metallic | East Asian, messy black hair knot, oil-stained suit | Growing admiration for "primitive" human ingenuity |
| **Jink** | Scout | Emerald metallic | Young, androgynous, bright golden blonde curly hair, fastest flyer | Learning actions in the past have weight |
| **Thresh** | Soldier | Ruby/crimson metallic | Broad, copper-red buzz cut, heavy armor | Brave in the future, terrified in the past — fights afraid |
| **Luma** | Medic/Scientist | Sapphire/violet metallic | South Asian, braided hair, holographic lenses | Sees the paradox first; most tempted to stay |
| **Theodore** | Human ally | — | Victorian boy, 12-13, tinker's apprentice | Wants fairies to be magical; learns they're something better |

## Visual Language Rules

- **Fairy tech:** Structured holographic light — translucent, prismatic, geometric edges. Not sparkle, but "light trapped in geometry." Reads as runes/magic to Victorian eyes. Suits are department-coded in jewel-tone metallics (silver, copper, emerald, ruby, sapphire) with matching holographic accent glow.
- **Steampunk world:** Heavy, warm-toned, dense. Brass, copper, gaslight, smoke. Everything is two environments: human-scale and fairy-scale.
- **Titans:** Dark mirror of fairy tech. Oil-on-water iridescence, shadow that moves wrong. Cloaking is not invisibility but *wrongness*.
- **Degradation arc:** Suits start pristine silver and accumulate soot/damage across the story. Holographic elements still glow through grime. This is the core visual metaphor.
- **Dual lighting:** Every scene contrasts warm amber gaslight against cool blue-white holographic light. Neither dominates.

## Technical Stack (for downstream production)

| Component | Phase 1 (Browser) | Phase 2 (Full Game) |
|-----------|-------------------|---------------------|
| Engine | Three.js + WebGL 2 | Unity (URP/HDRP) |
| 3D Assets | Meshy.ai GLB (lower-poly, baked lighting) | Meshy.ai GLB (higher-poly, Unity materials) |
| Dialogue | Ink (inkle scripting) → JavaScript | Ollama local LLM (7B for key NPCs, 3B for ambient) |
| Audio | Howler.js / Tone.js | Unity audio |
| Hosting | Static (Vercel/Netlify/itch.io), <50MB | Steam / itch.io |

## Working with This Repository

- All documents are now markdown. The `docs/` files are the authoritative design documents; other .md files are creative production documents (prompts, outlines).
- When generating new content, maintain consistency with the established visual language and character voices.
- Art prompts follow a consistent formula: painterly style, oil paint texture, visible brushwork, scale contrast, warm/cool light duality.
- Character turnaround prompts are structured for Meshy.ai 3D model generation (neutral background, four views, even lighting).
- Script generation prompts are self-contained per issue but should be fed alongside the Story Bible, Character Prompts, Character Turnarounds, and Plot Outline for best results. Each prompt specifies 22-page budgets with exact page ranges per story beat.
- The comic and game share narrative continuity — the prologue browser game covers Issues 1-3 (crash through Theodore's discovery).
