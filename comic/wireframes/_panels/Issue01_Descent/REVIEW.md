# Issue 1 Wireframe Review — Visual QA Status

**Method:** every panel SVG rendered in headless Chromium (mcp/playwright) at its native viewBox. Composed pages rendered at 800×1200 via `<image xlink:href>` panel refs resolved by `index.html` `inlinePanelImages()`. Screenshots in `screenshots/`.

**Last update:** 2026-04-27 (loop session extended through commit a48c18d — Pages 5-7 added).

---

## TL;DR — current state

**Pages 1–3 of Issue 1 are now meeting the quality bar** for hair, dialogue, anatomy, environment, and composition. Earlier "submarine / toque / teapot / stick-figure / no console" failure modes from v1 have been fixed across all 17 panel files (P01P01–P01P06, P02P01–P02P05, P03P01–P03P06).

**Pages 5, 6, 7 of Issue 1 are now also at quality bar.** Pages 5-6 (Section 2 — THE FALL: Victorian reveal + Theodore introduction). Page 7 (Section 3 opening — THE WRECKAGE: squad emerges from crashed ship in gutter). 14 new panels created, all deployed.

**Pages 4, 8-22 of Issue 1 remain auto-generated stick-figure storyboards** — 10pt dialogue, abstract figures. These are placeholders awaiting the same per-panel quality treatment.

**Issues 2–12 have script prompts only**, no wireframes yet.

---

## Page 1 — DONE

### P01P01 — Establishing wide, recon vessel in temporal corridor (742×364)
- ✅ Hexagonal lattice corridor walls with prismatic shimmer
- ✅ Predatory-fish ship silhouette
- ✅ Caption + Sable speech-from-ship balloon spec-compliant
- 🟢 Ship slightly small in frame (acceptable for establishing wide)

### P01P02 — Sable MCU at command station (241×364) — REFERENCE PANEL
- ✅ Silver-white scalp coverage with hairline edge stroke + 27 buzz stipples (no toque)
- ✅ Holographic command-telemetry display behind Sable with scrolling glyphs
- ✅ Calm authority pose, dialogue spec-compliant
- This is the gold-standard panel; other panels' hair was propagated against this template.

### P01P03 — Wren at engineering console (241×364) — REDRAWN
- ✅ High messy bun (multi-loop overlapping mass + bun-tie ring + escaping wisps)
- ✅ Holographic display rendered IN FRONT OF Wren — central hex lattice + floating data ring + 2 side cubes + "97%" coherence readout + ember sparkles
- ✅ Hands reaching forward into the holographic field (not terminating in abdomen)
- ✅ Dialogue spec-compliant
- 🟢 Torso silhouette could be slightly leaner (mascot-proportions critique partially addressed)

### P01P04 — Jink restless at scout station (241×364) — REDRAWN
- ✅ Multi-clump curls with dark separation + glints (no beehive blob)
- ✅ Viewport behind with prismatic streaks
- ✅ Jump seat + dangling leg + drumming hand
- ✅ 3 dialogue balloons spec-compliant

### P01P05 — Thresh at weapon rack through bridge archway (494×364) — REDRAWN
- ✅ Tall swept-back pomp + shaved sides with stipple + lock streaks + highlights
- ✅ Archway frames composition (left/right wedges)
- ✅ Corridor depth — distant doorway with light leak + secondary light strip + perspective lines
- ✅ Weapon rack with 3 visible rifle silhouettes
- 🟡 3/4 back pose still flat front-view (deferred — would need full figure rewrite; structurally sound)

### P01P06 — Luma close-up with holographic lenses (241×364) — REDRAWN
- ✅ Thick rope braid (38px wide, 8 plait segments + highlights + double-band tie + tassel wisps)
- ✅ Holographic lenses with scrolling geometric data
- ✅ Smooth pulled-back top + center part
- ✅ 3 dialogue balloons spec-compliant

---

## Page 2 — DONE

### P02P01 — Bridge wide OTS Sable, full squad (494×364) — REDRAWN
- ✅ Sable OTS reduced to bottom-right corner (was snowman dominating right half)
- ✅ Wren left at engineering console (visible)
- ✅ Jink center on jump seat (visible)
- ✅ Thresh through corridor archway in back wall (visible, ruby suit + pomp)
- ✅ Luma right at science station (now visible in sapphire suit + braid)
- ✅ Holographic displays — copper engineering left, violet science right, blue command center
- ✅ Dialogue spec-compliant 4-line wrap
- 🟡 Squad proportions still slightly mascot-like at small scale (acceptable for a wide establishing)

### P02P02 — ECU Jink hand drumming on knee (238×364) — REDRAWN
- ✅ Anatomical hand: 4 visible knuckles (cream highlights, cast shadows), 4 fingers + thumb clearly separated, varied heights showing drumming rhythm, fingernails, tendon ridges
- ✅ Flat knee plate (not hemispherical) with armor segmentation seams + center hex node
- ✅ Wrist holographic emitter casting emerald geometric grid onto hand
- ✅ Tap-impact ripples where fingers touch knee
- ✅ Out-of-focus prismatic background blur

### P02P03 — Sable + Thresh face each other through bridge arch (742×364)
- ✅ Sable profile buzz with scalp coverage + 17 stipples + hairline edge
- ✅ Thresh profile pomp rising above silhouette with 4 lock streaks + highlights
- ✅ Department color separation (silver/ruby) reads
- ✅ Dialogue spec-compliant
- 🟡 Bodies still limbless from waist down (deferred for full figure redraw)
- 🟡 Holographic display behind Sable still simple (deferred)

### P02P04 — Wren flags ripple in field (366×364)
- ✅ Wren multi-loop messy bun (no flat helmet)
- ✅ "92.0%" callout on display
- ✅ 3 dialogue balloons spec-compliant
- 🟢 Bun partially behind dialogue balloon (unavoidable given balloon position)

### P02P05 — Luma fascination cut short (366×364)
- ✅ Thick prominent rope braid (38px, 8 plait segments, double tie, tassel)
- ✅ Holographic lenses with scrolling data
- ✅ "—" cut-off dialogue spec-compliant

---

## Page 3 — DONE

All 6 panels are high-quality individual SVG files referenced by a thin compositor pattern (matching page01.svg).

### P03P01 — Full width IMPACT, KRAAANG, 25° dutch (742×364)
- ✅ All 5 squad thrown by impact at varied angles
- ✅ Red emergency strobing dominant, blue-white fragments
- ✅ Holographic shrapnel exploding in 3 colors
- ✅ Hull breach with sparking conduits + smoke
- ✅ Buckled ceiling + heaved floor
- ✅ KRAAANG SFX 72pt + WREN "CONTACT—!" balloon spec-compliant
- 🟢 Hair fragments per character not detailed-template (figures heavily transformed; chaos panel makes detailed hair secondary)

### P03P02 — Sable CU controlled fury, 15° canted (241×364)
- ✅ Red-strobe-right / dying-blue-left split lighting on face
- ✅ Sable buzz cut visible
- ✅ Hand on console + hand reaching for comm
- ✅ Dialogue spec-compliant

### P03P03 — Wren at destroyed console, 10° dutch (241×364)
- ✅ Wren multi-loop messy bun + escaping temple wisps + bun-tie ring
- ✅ Console fragmenting with copper-gold shrapnel
- ✅ Grim focus expression
- ✅ Dialogue spec-compliant

### P03P04 — POV through cracking viewport (241×364)
- ✅ Cracking viewport spiderweb pattern
- ✅ Dark Titan shape glimpsed in violent prismatic distortion
- ✅ Oil-on-water iridescence at Titan edges
- ✅ THRESH (O.P.) dashed-border off-panel balloon spec-compliant

### P03P05 — Squad on knees, Sable standing wide (366×364)
- ✅ Sable upright with silver buzz stipple
- ✅ Wren on knees at console, multi-loop bun + temple wisps
- ✅ Luma crawling toward medical kit with thick trailing braid (4 plait segments + tie)
- ✅ Jink tangled in harness with multi-clump curls + glints
- ✅ Red emergency dominant, dying blue fragments
- ✅ 2 dialogue balloons SABLE→WREN spec-compliant

### P03P06 — ECU Wren's hand on emergency toggle (366×364) — NEW
- ✅ Anatomical hand with 4 knuckles + 4 fingers + thumb wrapped around grip ball
- ✅ Brass mounting plate with rivets, EMERG. DRIVE stencil, hazard stripes
- ✅ Steel toggle lever pulled DOWN
- ✅ Copper suit sleeve with plate seams + copper trim
- ✅ Wrist holographic emitter glowing copper-gold
- ✅ White-hot drive flare bleeding from all 4 frame corners
- ✅ Red emergency wash + WREN balloon + CHUNK SFX 42pt

---

## Composed pages — DONE

### page01.svg, page02.svg, page03.svg
- ✅ All 3 pages compose via `<image xlink:href="_panels/Issue01_Descent/page0X_panelN.svg"/>` pattern
- ✅ Layout grids match script-spec dimensions
- ✅ Inline panel hrefs resolve correctly via `inlinePanelImages()` against `index.html` doc base path
- ✅ Live-deployed via `.github/workflows/pages.yml` to GitHub Pages on every push to main

---

## Templates — DONE

### `_templates/{sable,wren,jink,thresh,luma,theodore}.svg`
- ✅ All 6 character templates have multi-path hair geometry per `quality-bar.md` spec
- ✅ Sable buzz / Wren bun / Jink curls / Thresh pomp / Luma braid / Theodore tousled
- ✅ Wear-state overlays defined (clean / fresh-impact / mid-mission / heavy)

### `_templates/dialogue-style.md`
- ✅ Canonical: opaque white fill, 14pt 800-weight Helvetica Neue speaker label, 13pt 500-weight body, 2px speaker-color border, balloonShadow drop shadow filter, tail polygon stroke-width 2
- ✅ Speaker color reference table per character
- ✅ Inviolable placement rules (no face overlap, max 2 balloons per ECU/CU)
- ✅ Applied across all 17 P1-P3 panel SVGs

---

## Pages 5-7 — DONE (added in extended session)

### Page 5 — Victorian reveal (4 panels)
- P5P1 cityscape "The city sleeps" (warm-only world before squad arrives)
- P5P2 lamplighter Jack Hobday on rounds
- P5P3 Victorian woman witness, dual light meets human face for first time
- P5P4 ECU hand crossing herself, cool prismatic overwhelms warm amber

### Page 6 — Theodore introduction (5 panels)
- P6P1 Clerkenwell side street with Theodore silhouette in lit window (HARTLEY · TINKER trade sign)
- P6P2 Theodore close-up at window, dual lighting on wonder face, hand pressed to glass with brass gear ring
- P6P3 post-star roofscape (the city forgets)
- P6P4 Hobday aftermath, stopped working, looking up — thought balloon
- P6P5 ECU Theodore's hand on glass with oil-stained fingertips

### Page 7 — Squad in wreckage (5 panels)
- P7P1 worm's-eye gutter establishing with Sable face-down
- P7P2 ECU Sable's hand twitching (cracked gauntlet leaking blue-white)
- P7P3 Sable rising from debris, bracing arm
- P7P4 Sable face CU scanning, command activating
- P7P5 bird's-eye revealing all 5 squad members in gutter against vast slate roof

---

## Pending — Pages 4, 8–22

All pages 4–22 are currently auto-generated stick-figure storyboards (single monolithic SVG per page, ~5–13KB each). They show panel layout grids + tiny inline figure markers + 10pt dialogue. The work is structurally complete (panels exist with correct counts and dimensions) but artistically placeholder.

To bring them to Page 1–3 quality:

**Per page:**
1. Recompose page0N.svg as a thin xlink:href compositor (matching `page01.svg`'s pattern)
2. For each panel slot, create `_panels/Issue01_Descent/page0N_panelM.svg` with full painterly art
3. Apply dialogue-style.md to all balloons
4. Use character templates as the recipe for figures
5. Render via mcp/playwright at native viewBox + verify against `comic/scripts/Issue01_Descent_Script.md`
6. Commit per-panel batches of 1–3 fixes

**Estimated scope:** ~85 panels × ~25KB SVG each ≈ 2.1MB of careful hand-coded art. Per-panel pace from this loop session was ~5–10 min for hair propagation, ~20–30 min for full panel redraws. So 25–50 hours total for Issue 1 completion.

**Suggested triage order** (story-critical / high-emotion-beat panels first):
- **Page 5** — first Victorian reveal (the past for the first time)
- **Page 6** — Theodore introduction (the boy who finds them)
- **Page 12** — first Theodore-meets-fairies beat
- **Page 18-22** — episode climax + cliffhanger
- **Page 4** — the descent itself (transition from Page 3 emergency)
- **Pages 7-11, 13-17** — middle continuity

---

## Pending — Issues 2–12

Script prompts exist in `comic/scripts/Issue02_Small_World_Script.md` through `Issue12_The_Stories_They_Tell_Script.md`. No wireframes yet.

Recommend doing Issue 1 fully first (validate pipeline + style + character consistency) before scaling.

---

## Tooling status

- ✅ `mcp/playwright` via Docker MCP toolkit for rendering
- ✅ `_review/view.html?s=path/to.svg` viewer for individual panels (external `<image>` refs resolve correctly)
- ✅ `index.html` with `inlinePanelImages()` for composed pages (resolves relative hrefs against doc base path)
- ✅ Local viewer at http://localhost:3001 via docker-compose `wireframe-viewer` profile
- ✅ GitHub Pages deploys on push to main via `.github/workflows/pages.yml`
- ✅ Live preview: https://tortoisewolfe.github.io/GrimGlow_planning/

---

## Loop session commit log (most recent)

```
4539726 fix(P01P05): add corridor depth — distant doorway, perspective lines
f08e14c fix(P01P03): render holographic display in front of Wren
6f2053f fix(P02P01): shrink Sable OTS from snowman to corner element
770f660 fix(P02P02): redraw hand-on-knee — anatomical hand, flat knee plate
998ff01 fix(P03P03+P03P05): propagate template hair to Page 3 figures
f1515e8 fix(page03): recompose as thin xlink:href compositor matching page01
292bec2 feat(P03P06): create ECU emergency toggle panel from script spec
a062bdf fix(P03P01-P03P05): apply dialogue-style.md spec across all 5 panels
8e7fe83 fix(P02P05): replace thin braid with thick prominent Luma rope
6a880d4 fix(P02P04): replace flat-helmet bun with Wren multi-loop messy bun
a3aa6e8 fix(P02P03): apply Thresh pomp + Sable buzz to profile silhouettes
c719b4f fix(P01P06): replace thin braid with thick prominent Luma rope
ed7b870 fix(P01P05): replace generic bowl cut with Thresh tall swept pomp
d6843b7 fix(P01P03): replace flat helmet hair with Wren high messy bun
a4a0694 fix(P01P04): replace beehive blob hair with multi-clump Jink curls
2bccf14 fix(panels): reposition + widen dialogue per spec across 11 P1+P2 panels
```

---

## What I want from the user before continuing

Pages 1–3 are now at quality bar. The natural next decisions:

1. **Continue Issue 1 (Pages 4–22)?** If yes, in what triage order? My recommendation: Page 5 first (Victorian reveal — the highest emotional pivot), then Page 6 (Theodore intro). Pages 7-22 in script order after that.

2. **Switch to a different goal?** E.g. start Issue 2 wireframes, or revisit any P1-P3 panel that still feels short of bar (P02P03 limbless bodies, P01P05 3/4 back pose, etc.).

3. **Iterate on tooling?** E.g. build a SVG-component library so character figures can be `<use>`d instead of hand-redrawn per panel — would dramatically speed the remaining 85+ panels.

4. **Add automated regression checks?** Pa11y/visual-snapshot tests in CI so future hair/dialogue edits don't drift from the spec.
