# Asset Bridge — Decision Record

**Status**: paper-only (no repo created yet)
**Decision date**: 2026-05-02
**Required by**: GrimGlow Phase 1 constitution Principle VII (asset
bridge), Phase 2 (Unity) constitution Principle VII (asset bridge),
dev plan §4 (The Asset Bridge)

## What This Document Decides

This document records the decisions about the shared GrimGlow asset
bridge repo. Creating the repo itself is a separate authorized step
(`gh repo create` or equivalent) — this document is the spec it will
follow.

## Repo Name

**`grimglow-assets`**

Rationale: shorter than `grimglow-asset-bridge`, makes the intent
obvious, matches the dev plan's terminology ("shared asset
repository"), and stays organization-agnostic if the repo eventually
moves under a TSD-org or GrimGlow-IP-org namespace.

Owner namespace: `TortoiseWolfe/grimglow-assets` initially; can move
under a dedicated org later without breaking consumers (LFS pointers
are content-addressed, not URL-bound).

## Visibility

**Private** initially. Master art assets are pre-release IP and
shouldn't be public until at least Phase 1 ships. Make public after
Phase 1 launch if/when an open-source contribution path makes sense
(unlikely — this is proprietary IP).

## Storage

**Git-LFS** for all binary content. Configure in `.gitattributes`:

```gitattributes
*.glb       filter=lfs diff=lfs merge=lfs -text
*.fbx       filter=lfs diff=lfs merge=lfs -text
*.gltf      filter=lfs diff=lfs merge=lfs -text
*.bin       filter=lfs diff=lfs merge=lfs -text
*.png       filter=lfs diff=lfs merge=lfs -text
*.jpg       filter=lfs diff=lfs merge=lfs -text
*.jpeg      filter=lfs diff=lfs merge=lfs -text
*.psd       filter=lfs diff=lfs merge=lfs -text
*.tga       filter=lfs diff=lfs merge=lfs -text
*.exr       filter=lfs diff=lfs merge=lfs -text
*.hdr       filter=lfs diff=lfs merge=lfs -text
*.wav       filter=lfs diff=lfs merge=lfs -text
*.flac      filter=lfs diff=lfs merge=lfs -text
*.ogg       filter=lfs diff=lfs merge=lfs -text
*.mp3       filter=lfs diff=lfs merge=lfs -text
```

Source files (markdown prompts, GLSL/HLSL shader source, JSON manifests)
stay regular Git so they're diffable.

## Repo Layout

```
grimglow-assets/
├── README.md                 # how to consume from Phase 1 / Phase 2
├── .gitattributes            # LFS rules per above
├── .github/
│   └── workflows/            # validate LFS pointers, asset-budget checks
│
├── characters/               # one subdir per squad member + Theodore
│   ├── sable/
│   │   ├── master.glb        # Meshy-generated master
│   │   ├── prompt.md         # Meshy prompt + iteration history
│   │   ├── turnaround.png    # 4-view reference sheet
│   │   ├── concept-art/      # painterly references
│   │   └── variants/         # damage/grime states (clean, mid, late)
│   ├── wren/                 # same structure
│   ├── jink/
│   ├── thresh/
│   ├── luma/
│   └── theodore/
│
├── environments/
│   ├── ship-interior/
│   │   ├── master.glb
│   │   ├── prompt.md
│   │   └── components/       # individual props as separate GLBs
│   ├── workshop-floor/
│   ├── workshop-surfaces/
│   └── (Phase 2: full city, heist locations)
│
├── shaders/
│   ├── holographic-glow/
│   │   ├── glsl/             # Phase 1 implementation (Three.js)
│   │   ├── hlsl/             # Phase 2 implementation (Unity)
│   │   ├── spec.md           # math + intent (the language-agnostic logic)
│   │   └── reference.png     # visual target
│   ├── gaslight-volumetrics/
│   ├── degradation-overlay/
│   └── titan-distortion/
│
├── audio/
│   ├── ambient/              # steampunk soundscape, holographic hum
│   ├── characters/           # voice samples (when recorded)
│   ├── music/                # composed tracks
│   └── sfx/
│
├── prompts/
│   ├── meshy-environment-prompts.md  # mirror of GrimGlow_planning's
│   ├── meshy-character-prompts.md
│   └── prompt-iteration-log.md       # what worked, what didn't
│
└── manifests/
    ├── phase1-required.json  # which assets Phase 1 needs
    ├── phase2-required.json  # which assets Phase 2 needs
    └── asset-budgets.json    # per-asset size budget per platform
```

## Consumption Pattern

### Phase 1a (browser, Next.js)

- Consumed via **git submodule** at `grimglow-prologue/assets/` (or
  similar path)
- Phase 1a build pipeline copies relevant GLBs from the submodule
  into `public/models/` for Three.js loading at runtime
- LFS pointers resolved during `pnpm install` or build
- CI verifies all `manifests/phase1-required.json` assets are
  available

### Phase 1b (RN iOS, Expo)

- Same submodule pattern
- Build pipeline bundles GLBs into the app via Metro asset resolver
- Same `manifests/phase1-required.json`

### Phase 2 (Unity)

- Submodule mounted at `Assets/AssetBridge/` (or via Unity Package
  Manager local path)
- Custom `AssetPostprocessor` script reassigns Three.js / R3F
  materials to URP/HDRP equivalents on import
- Higher-poly versions live in `characters/<name>/variants/hires/`
  for Phase 2 use; Phase 1 uses `master.glb` (lower-poly)
- Manifest: `phase2-required.json`

### GrimGlow_planning (this repo)

- The planning repo references the bridge but does NOT consume from
  it directly
- Concept art and prompt records that originated here get **migrated
  into the bridge** when ready, not duplicated
- After migration, this repo's `concept-art/` and `world-building/`
  references point to bridge paths

## Migration Path from GrimGlow_planning

The current `GrimGlow_planning/` repo already contains:

- `concept-art/<character>/` — concept art and turnarounds
- `characters/Character_Turnarounds.md` — Meshy turnaround prompts
- `world-building/meshy-environment-prompts.md` — 142 environment
  prompts

**Migration plan** (executed when the bridge repo is created):

1. Move `concept-art/` content into `grimglow-assets/characters/<name>/concept-art/`
2. Move turnaround images into `grimglow-assets/characters/<name>/turnaround.png`
3. Move Meshy prompts into `grimglow-assets/prompts/`
4. Replace `concept-art/` here with a thin pointer doc
5. Update `CLAUDE.md` to reflect the new locations

Migration is itself a SpecKit feature; gets a PRP.

## What This Does NOT Decide

- Whether to mirror the bridge to S3 / Cloudflare R2 for CDN access
  (probably yes for Phase 1 web hosting, decide when Phase 1 hosting
  is finalized)
- Whether to use Git-LFS with GitHub or migrate to a self-hosted LFS
  server later (start with GitHub, evaluate when bandwidth costs
  become real)
- Music composer / voice-actor IP rights (handled per-asset, outside
  this repo's scope)
- Whether the repo should be split into `grimglow-assets-3d`,
  `grimglow-assets-audio`, `grimglow-assets-shaders` (probably
  no — single-repo simplifies submodule management)

## Verification (when repo is created)

- `git clone --recurse-submodules` from a Phase 1 dev environment
  resolves all LFS pointers
- A test consumer (a tiny Next.js page that loads `sable/master.glb`)
  renders without error
- The Phase 2 AssetPostprocessor (when written) imports the same GLB
  and converts materials correctly
- `manifests/phase1-required.json` validates against `find characters
  environments | grep .glb`

## Authorization Checkpoint

Creating the repo requires:

```bash
gh repo create TortoiseWolfe/grimglow-assets --private \
  --description "Shared 3D / audio / shader assets for GrimGlow Phase 1 + Phase 2"
```

This requires explicit operator authorization. The execution plan
(`gleaming-kitten-execution.md`) deliberately stops at "decision
recorded" — repo creation is a separate authorized step.
