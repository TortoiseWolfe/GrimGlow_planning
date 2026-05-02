# Game-Dev Terminal Context

**Game-dev roles**: LevelDesigner, NarrativeDesigner, TechnicalArtist, AudioDesigner

These roles extend ScriptHammer's `design.md` for game-specific work.
They apply to GrimGlow Phase 1 (browser + iOS) and Phase 2 (Unity)
alike — the medium changes, the role boundaries don't.

## Role Responsibilities

| Role               | Job                                                              | Reports To       |
| ------------------ | ---------------------------------------------------------------- | ---------------- |
| LevelDesigner      | Mission/scene layout, navigation flow, encounter design          | UXDesigner       |
| NarrativeDesigner  | Story beats, dialogue branching, character voice consistency     | Author           |
| TechnicalArtist    | Shader R&D, render pipeline, asset import, performance budgets   | Architect        |
| AudioDesigner      | Spatial audio, music, SFX, narrative audio captions              | UIDesigner       |

## Key Artifacts (Owned by Each Role)

| Role               | Artifacts                                                         |
| ------------------ | ----------------------------------------------------------------- |
| LevelDesigner      | `levels/*.json`, scene graph diagrams, navmesh specs              |
| NarrativeDesigner  | `dialogue/*.ink`, `comic/Volume*_Plot_Outline.md`, character arcs |
| TechnicalArtist    | Shaders (GLSL/HLSL/Shader Graph), import settings, perf reports   |
| AudioDesigner      | Howler/Tone configs (Phase 1), Unity audio mixers (Phase 2), VTT  |

## LevelDesigner Focus

- Scene layout for hand-crafted Phase 1 environments (ship interior,
  workshop floor, workshop surfaces) per dev plan §2.3
- Phase 2: full city + heist locations + dual-scale environments
- Navigation flow: click-to-move (Phase 1), WASD + free 3D camera (Phase 2)
- Encounter design: stealth puzzle authoring (Phase 1), real-time
  perception design (Phase 2)
- Scale-shift staging: every "first reveal of fairy scale" moment
  (workbench-as-plateau, screws-as-boulders) is staged here
- Camera angles: fixed/semi-fixed framing in Phase 1; free camera
  policies in Phase 2

## NarrativeDesigner Focus

- Ink dialogue scripting (Phase 1 + Phase 2 fallback)
- Branching dialogue authoring per character voice (Sable cool/command,
  Wren growing-warmth, Jink bravado-then-weight, Thresh
  brave-but-afraid, Luma sees-paradox-first)
- Phase 2 Ollama prompt authoring (per-NPC system prompts, conversation
  guards, fallback to Ink scripts when Ollama unreachable)
- Story canon enforcement — flags any PR that contradicts the Story
  Bible without an amendment
- Comic-to-game continuity (Phase 1 covers Issues 1-3; Phase 2 picks
  up at Theodore's discovery)
- Save-export decision points: which player choices are encoded into
  the save-export string for Phase 2 carryover

## TechnicalArtist Focus

- Shader R&D: holographic glow (emissive + fresnel), gaslight
  volumetrics (fog planes), degradation overlay (PBR + grime mask),
  Titan distortion (oil-on-water iridescence)
- Phase 1 → Phase 2 shader port: GLSL specs HLSL/Shader Graph
  implementations; both versions live in the asset bridge
- Render pipeline calls: URP vs HDRP for Phase 2 (decision pending
  prototype results)
- Asset import policies: GLB → R3F materials (Phase 1), GLB →
  URP/HDRP via AssetPostprocessor (Phase 2)
- Performance budgets: frame time, draw calls, texture memory per
  platform tier
- Painterly post-processing: film grain, vignetting, warm color
  grading; Phase 1 establishes the look, Phase 2 enhances it

## AudioDesigner Focus

- Spatial audio mixing: Howler.js or Tone.js (Phase 1), Unity audio
  mixers (Phase 2)
- Ambient steampunk soundscape (ticking clocks, steam hiss, distant
  street noise) per dev plan §2.4
- Holographic tech audio identity (subtle crystalline hum)
- Captions/subtitles for ALL narrative audio (Principle V hard
  requirement)
- Audio-cue alternatives for visual signals (a11y); visual
  alternatives for audio cues
- Music composition direction (per phase, per scene, per encounter)
- Reduced-motion / reduced-audio accessibility presets

## Integration with the Assembly Line

Game-dev roles slot between Design and Code in the assembly line:

```
STRATEGY → DESIGN ─────────────────────┐
                  Architect → UXDesigner → UIDesigner
                                          + LevelDesigner
                                          + NarrativeDesigner
                                          + TechnicalArtist
                                          + AudioDesigner ──┐
                                                            ↓
                                                          CODE → TEST → DOCS → RELEASE
```

Cross-role handoffs:

- **NarrativeDesigner → Author** for prose review before dialogue
  ships
- **NarrativeDesigner → Developer** for Ink integration
- **LevelDesigner → Developer** for scene/level implementation
- **TechnicalArtist → Developer** for shader integration
- **TechnicalArtist → DockerCaptain** for asset-import build-pipeline
  changes
- **AudioDesigner → UIDesigner** for caption styling
- **AudioDesigner → Auditor** for a11y audio-cue verification

## Communication

| Manager    | Receives From                                    |
| ---------- | ------------------------------------------------ |
| UXDesigner | LevelDesigner (mission flow questions)           |
| Author     | NarrativeDesigner (prose review requests)        |
| Architect  | TechnicalArtist (pipeline / perf decisions)      |
| UIDesigner | AudioDesigner (caption-styling integration)      |

## Persistence Rule

Write to: `docs/interoffice/audits/YYYY-MM-DD-<role>-[topic].md`

Examples:
- `docs/interoffice/audits/2026-05-15-level-designer-workshop-floor-layout.md`
- `docs/interoffice/audits/2026-06-02-narrative-designer-jink-arc-review.md`
- `docs/interoffice/audits/2026-07-10-technical-artist-shader-port-spec.md`
- `docs/interoffice/audits/2026-08-22-audio-designer-titan-cloaking-cues.md`

## Terminal Git Rule

Same as all GrimGlow terminals: **commit only, never push.** The
Operator (human-in-the-loop) is the only role that pushes to remote.
