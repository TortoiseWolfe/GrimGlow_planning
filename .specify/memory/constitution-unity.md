<!--
GrimGlow Phase 2 (Unity) Constitution — adapted from ScriptHammer v1.0.1
and GrimGlow Phase 1 v1.0.0 (this repo's constitution.md).

This constitution governs Phase 2 of GrimGlow per the two-phase dev
plan (`docs/GrimGlow_Two_Phase_Development_Plan.md` §3): the full Unity
PC game distributed via Steam/itch.io. It is paper-only until Phase 1
ships and validates the IP — Phase 2 code work begins after that gate.

Unity is qualitatively different from ScriptHammer's web stack. Most
ScriptHammer principles still apply at the *discipline* level
(constitution-governed, test-first, SpecKit-only, Docker for build
pipeline, conventional commits). The *mechanics* differ entirely:
prefabs and MonoBehaviours instead of React components, Unity Test
Framework instead of Vitest/Playwright, HLSL/Shader Graph instead of
GLSL, save files instead of Supabase.

Principles I–VI mirror Phase 1's. Principle VII covers Unity-specific
discipline (Ollama contract, save-import from Phase 1, asset bridge
from Unity's perspective). Principle VIII is unchanged.

This constitution is a draft. Substantive amendments are expected once
Phase 1 ships and Unity work begins; treat this as the v1.0.0 starting
point, not the final word.
-->

# GrimGlow Phase 2 (Unity) Constitution

## Core Principles

### I. Component Structure Compliance — Unity 5-File Analogue

Every game-domain Unity component MUST follow the 5-file analogue:

1. `Component.cs` — the MonoBehaviour or ScriptableObject implementation
2. `ComponentEditor.cs` — custom editor / inspector
3. `Component.PlayMode.cs` — Unity Test Framework PlayMode test
4. `Component.EditMode.cs` — Unity Test Framework EditMode test
5. `Component.prefab` (or `.asset` for ScriptableObject) — the canonical
   instance / data definition

A Unity Editor menu item (`Tools > GrimGlow > New Component...`)
scaffolds all 5 files; manual creation is forbidden for game-domain
components. Engine-internal scripts (utility classes, math helpers,
extension methods) are exempt and live in `Assets/Scripts/Util/`.

CI fails if a `MonoBehaviour` lands without its `PlayMode` + `EditMode`
test files.

### II. Test-First Development

Tests MUST be written before implementation following RED-GREEN-REFACTOR.
Unity Test Framework with PlayMode + EditMode coverage. Critical paths —
save/load (including Phase 1 save import), squad AI behavior trees,
NPC perception state machines, scale-shift transitions, dialogue
state — require comprehensive test suites.

Coverage thresholds:

- 25% baseline EditMode coverage
- PlayMode tests for all gameplay-critical systems
- Headless integration tests for save round-tripping (Phase 1 → Phase 2)

CI runs Unity Test Framework headless in Docker; pre-merge gate.

### III. SpecKit/PRP Methodology (NON-NEGOTIABLE)

Every game system (squad AI, Titan AI, dialogue, scale-shift mechanic,
mission scripting, save migration) MUST follow the SpecKit flow:

```
PRP → /speckit.specify → /speckit.clarify → /speckit.plan
    → /speckit.checklist → /speckit.tasks → /speckit.analyze
    → /speckit.implement
```

PRPs at `docs/prp-docs/<system>-prp.md`. SpecKit artifacts at
`specs/<NNN-name>/`. Ad-hoc system development is forbidden, including
"refactor" and "polish" passes — those need a PRP too.

### IV. Docker-First Where Feasible (v1.0.1: scoped to CI only)

Local development runs in the Unity Editor directly — there is no
viable Docker-first option for the Editor itself. **Locked in v1.0.1:
Docker scope is "CI builds + tests only."** Running the Editor inside
a container with X11 forwarding was considered and rejected as
fragile across host OS variations and unreliable for GPU access.
However, on the CI side:

- **CI builds** run headless Unity in Docker (`unityci/editor` images)
- **Asset import / preprocessing** runs in Docker
- **Test runs** in CI run Unity Test Framework headless in Docker
- **Build pipeline** (Linux/Windows/macOS targets) runs in Docker

Local dev still respects the spirit of Docker-first: no `sudo` for
Unity issues, no system-level package installs to make Unity work,
all dependencies declared in the project (Unity Package Manager
manifests).

### V. Accessibility as a Build Gate — Game Edition

Unity UI Accessibility is a build gate, not a polish phase:

- **Controller remapping** — every input action user-rebindable
- **Subtitle / closed-caption support** — required for all narrative
  audio, defaults on, clearly togglable, font-size adjustable
- **Colorblind palettes** — protan, deutan, tritan modes; never rely
  on color alone for game-state encoding
- **Motion sensitivity** — slider for camera shake, motion blur,
  parallax intensity; "reduce motion" preset disables them all
- **Difficulty-independent accessibility** — combat assist options
  (auto-aim, slow-time, infinite ammo) available without locking
  story progress
- **Readable text** — minimum text size 14pt at 1080p, dyslexic-
  friendly font option, contrast modes
- **Audio cues** — every important visual signal has an audio cue
  alternative; every important audio signal has a visual alternative

A11y review required for every PR that touches UI, input, audio, or
camera systems.

### VI. Privacy & Compliance First

Steam analytics consent gate before any telemetry. GDPR save-data
export ("export my saves") accessible from Settings. "Delete my data"
deletes local saves and any cloud-sync state. No Ollama prompt logging
beyond a debug-only opt-in. Crash reports via Sentry .NET only after
explicit user consent (default off).

Secrets (Steam keys, build pipeline tokens, Sentry DSN) live in CI
env vars and EAS-equivalent secret stores. Never in committed scenes,
prefabs, or source. `.env` gitignored.

### VII. Unity-Specific Discipline

**Ollama contract:**

- Ollama is a **localhost dependency** running as a background process
  on the player's machine. Unity communicates via HTTP to localhost.
- Graceful degradation when Ollama is not installed: NPC dialogue
  falls back to scripted branching (the same Ink scripts Phase 1
  used). Player sees a non-intrusive notification explaining the
  fallback and how to install Ollama for the dynamic-dialogue
  experience.
- Two model tiers per dev plan §3.1: 7B for Theodore and key NPCs,
  3B for ambient barks. Hardware detection picks the tier; player
  can override.
- Cloud API fallback (per dev plan §3.2.1) is **opt-in** with explicit
  consent; never on by default. No PII in prompts.
- All Ollama prompts are version-controlled and treated as content
  (review-gated) — they're game-design artifacts, not transient code.

**Save import from Phase 1:**

- Phase 2 reads any Phase 1 save-export code on first launch, with
  explicit user opt-in ("Import your prologue save").
- Save format is reverse-compatible — Phase 1's save-export
  specification is the authoritative input contract; Phase 2 must
  not require schema changes that break existing Phase 1 saves.
- Players who skipped Phase 1 see a brief cinematic recap (built
  from Phase 1 assets per dev plan §3.2) and start with sensible
  defaults.

**Asset bridge:**

- Master GLB assets, Meshy.ai prompt records, and shared shader R&D
  live in the dedicated Git-LFS asset-bridge repo (same repo Phase 1
  consumes from). Unity imports via a custom `AssetPostprocessor` that
  reassigns Three.js / R3F materials to URP equivalents on import.
- Higher-poly versions of Phase 1 models generated in Meshy.ai when
  needed, committed to the bridge, replacing Phase 1's lower-poly
  versions for Phase 2 use.
- Phase 1's GLSL shaders are the *spec* for Phase 2's HLSL/Shader
  Graph implementations — same logic, different language. Both
  versions live in the bridge.

**AI architecture separation (per dev plan §3):**

- **Gameplay AI** (NavMesh, behavior trees, state machines, perception)
  is platform-native Unity code. No Ollama involvement.
- **Conversational AI** (Ollama dynamic dialogue) is a separate
  subsystem, gated by Principle VII's Ollama contract.
- The two share a common game-state layer; never reference each other
  directly.

**Performance budgets:**

- 60 fps target on Steam Deck (the de facto handheld baseline)
- 30 fps acceptable on lowest spec if "reduce motion" engaged and
  Ollama tier dropped to 3B
- Frame budget: 16ms total, ≤4ms for AI subsystems combined
- Asset streaming for any environment >500MB

**Visual language fidelity:**

- "Holographic glow" (emissive + fresnel), "gaslight volumetrics", and
  "degradation overlay" shaders carry forward from Phase 1's GLSL R&D
- Dual-lighting system (warm gaslight vs. cool holographic) is a
  hard requirement — every scene contrast-tests both light vocabularies
- Painterly post-processing pipeline (film grain, vignetting, warm
  color grade) — Phase 1 establishes the look; Phase 2 enhances it,
  never abandons it

### VIII. Multi-Terminal Assembly-Line Orchestration

Same as Phase 1. Game-dev roles (LevelDesigner, NarrativeDesigner,
TechnicalArtist, AudioDesigner) are first-class. Add Phase 2-specific
roles by amendment if Unity work surfaces gaps:

- **AIDesigner** (likely needed for behavior trees + Ollama prompt
  authoring)
- **CombatDesigner** (Phase 2 introduces real-time stealth/combat
  that Phase 1 didn't have)
- **MissionScripter** (heist mission design)

Terminal git rule unchanged: commit only, never push — Operator owns
the push.

## Technical Standards

### Engine + Tooling

- **Unity** with URP (Universal Render Pipeline). Locked in v1.0.1
  (2026-05-02). Rationale: faster to ship, broader hardware support
  (Steam Deck-friendly per Principle V perf budgets), simpler shader
  graph, and matches the painterly + dual-lighting visual target
  without HDRP's overhead. Future amendment to HDRP requires a
  TechnicalArtist prototype showing concrete blockers.
- **C# 11+** with nullable reference types enabled, treat-warnings-
  as-errors
- **Unity Test Framework** for PlayMode + EditMode tests
- **Unity Cloud Build** OR **headless Unity in Docker** for CI builds
- **Mixamo** for humanoid rigs (per dev plan §2.2)
- **Ollama** running locally; abstraction layer per Principle VII

### Asset Pipeline

- All 3D assets sourced from the Git-LFS asset-bridge repo
- AssetPostprocessor reassigns materials to URP on import
- No assets duplicated into this repo — bridge is single source of
  truth
- Texture budget per asset documented in import settings; CI fails
  on imports that exceed budget without explicit override

### Code Quality

- Roslyn analyzers + EditorConfig for C# style
- Pre-commit hooks (via dotnet-format) for consistent formatting
- Conventional commits with `Co-Authored-By: Claude` footer when
  AI-assisted
- No `TODO` / `FIXME` in committed code without an associated GitHub
  issue (matches ScriptHammer's "no technical debt" principle)

## Development Workflow

### SpecKit Execution Flow

Identical to Phase 1.

### Contribution Process

- Feature branch (`<NNN>-<slug>`)
- Local Unity Editor development; CI builds in Docker
- All tests pass before push
- PR references `specs/<NNN-*>/` artifacts
- A11y review for any UI/input/audio/camera change
- Operator merges; terminals never push

## Quality Gates

### Build Requirements

- All game-domain components follow 5-file analogue
- C# compiles with no warnings (`-warnaserror`)
- Unity build succeeds for Linux, Windows, and (when planned) macOS
- Asset import passes (no missing materials, no broken prefab
  references)
- Asset bridge dependency resolved (no missing GLBs)

### Test Requirements

- EditMode coverage above 25% baseline
- PlayMode tests for all gameplay-critical systems
- Save import test passes (Phase 1 save → Phase 2 game)
- Ollama fallback test passes (game runs with Ollama unreachable)

### Performance Standards

- 60 fps on Steam Deck baseline
- Memory budget per platform documented; CI tracks regressions
- Initial load under 30 seconds on baseline
- Save / load operations under 500ms

### Accessibility Standards

- All Principle V requirements verified manually pre-release
- Subtitle support tested across all narrative scenes
- Controller remapping tested with at least 3 controller types
- Colorblind modes verified by tech-artist review

## Governance

Same amendment / compliance / version-management / enforcement model
as Phase 1. Substantive amendments expected when Unity work begins
and reality contacts the paper.

---

**Version**: 1.0.1 (paper)
**Ratified**: 2026-05-02 (v1.0.0); amended 2026-05-02 (v1.0.1)
**Status**: paper-only — no Unity code work has started yet. Will be
amended further once Phase 1 ships and Phase 2 implementation begins.
**Source constitutions**: ScriptHammer v1.0.1 (ratified 2025-09-20),
GrimGlow Phase 1 v1.0.0 (this repo, ratified 2026-05-02).
**Scope**: GrimGlow Phase 2 (Unity full PC game on Steam/itch.io).
Phase 1 (browser + iOS prologue) is governed by `constitution.md`.

### Amendment log

- **v1.0.1 (2026-05-02)** — Lock URP as the render pipeline (was
  "TBD by tech-art prototype"). Lock Docker scope to "CI builds + tests
  only" (Principle IV) — local Unity Editor runs on host, dependencies
  declared via Unity Package Manager, no global host installs.
