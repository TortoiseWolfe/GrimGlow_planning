# Finished Comic Art Quality Bar

This is the bar every panel must clear before it's marked done. Anything below this is unfinished.

## Anatomy

- [ ] **Proportions:** adult fairy-scale figures are 7–8 heads tall in full-body shots. Theodore is 6 heads (12-13 yo). NOT mascot proportions (3–4 heads = stuffed-animal look).
- [ ] **Distinct silhouettes per character:** if you traced the figure's outline only, could a reader still tell Sable from Wren from Luma? The answer should be yes — different builds, hair shapes, suit profiles.
- [ ] **Joints connect.** Shoulder → upper arm → elbow → forearm → wrist → hand — every junction visible, no smooth blob from torso to fingertip.
- [ ] **Hands have fingers.** Even thumbnail-sized hands at distance need at least a thumb + finger separation. ECU/CU hands need all 5 digits + knuckles + nail highlights.
- [ ] **Faces have structure** (brow ridge, nose bridge, cheekbones, jaw, chin). Not a flat oval with dots for eyes.

## Hair

Hair is the worst recurring quality issue in v1 panels. Specific per-character standards in `_templates/<character>.svg` after the hair-rewrite. Per panel:

- [ ] Hair has **multiple lock paths or distinct strand outlines**, not a single smooth gradient shape.
- [ ] Hair silhouette matches the character's canonical style:
  - Sable: tight buzz cut close to skull. **NOT a dome / toque.**
  - Wren: high messy bun on top with escaping strands at temples. **NOT a flat helmet.**
  - Jink: distinct curl clumps with visible separation between locks. **NOT a single beehive blob.**
  - Thresh: tall swept-back pomp + shaved sides. **NOT a forelock or bowl cut.**
  - Luma: smooth pulled-back top + thick prominent rope braid (always visible, not a thin line).
  - Theodore: tousled spikes/short locks, sandy-brown.
- [ ] Hair has highlight strands or rim light on the lit side.

## Suit / costume

- [ ] **Plate seams visible.** Real comic armor has segmentation lines, gaps at joints, layered plates. Not a smooth color gradient torso.
- [ ] **Holographic accent nodes** glow from defined plate locations (shoulders, chest center, hip, knees) — same locations character to character so the squad reads as a unit.
- [ ] **Department color identifies at a glance** even if the character is small in frame.
- [ ] **Wear-state matches the script's Asset Manifest** for the panel (clean / fresh-impact / mid-mission / heavy).

## Lighting

- [ ] **Dual lighting active:** every scene has a warm key (gaslight / copper hologram / red emergency) AND a cool key (blue-white hologram / corridor light / starlight) per the project Visual Language Rules. Even pure-bridge scenes have department-color hotspots competing.
- [ ] **Light SOURCES are visible** (a window, a hologram, a node, a strobe) — not just a wash of color.
- [ ] **Cast light hits surfaces.** A blue hologram doesn't just exist; it casts blue light on the character's near side. Faces are split by light-source direction.
- [ ] **Bloom on bright sources** (feGaussianBlur). Not a hard-edged neon disc.

## Holographic displays / fairy tech

- [ ] Reads as **"structured light trapped in geometry"** — translucent prismatic shapes, geometric edges, layered depth.
- [ ] **Not a flat rectangle with text inside.** Multiple Z-depth elements: floating glyphs at different distances, a frame, internal lattice, scrolling data, accent ticks, corner brackets.
- [ ] **Glyphs are abstract geometric shapes,** not English words. Hexagons, triangles, glyphs, waveforms, numeric bars. The viewer should NOT be able to read what the data says — it should read as alien instrumentation.
- [ ] Casts colored light onto the character manipulating it (their hands and face are tinted by the display's color).

## Environment

- [ ] **Backgrounds are scenes, not symbolic stand-ins.** A bridge has a ceiling with structural beams + light strips, walls with viewports, a floor with plates. Not a black void with one stripe.
- [ ] **Perspective consistent within the panel.** If the camera is low-angle, the ceiling pushes up, floor expands, figures are taller. If high-angle, the opposite.
- [ ] **Foreground / midground / background separation.** Three depth planes minimum. Foreground often has frame-establishing elements (an OTS shoulder, a console edge, a hand at frame edge); background gives the panel scale.

## Composition

- [ ] **Subject placement matches the script's shot description.** "Wide" means the subject doesn't fill the frame. "ECU" means it does. "Profile" means the subject is in side view. Don't default to centered front-view for everything.
- [ ] **Eye flow** — the panel directs the reader's eye to the speaker first (via lighting, contrast, framing), then to the dialogue, then to the next panel.
- [ ] **Dutch angle if specified** is rotated cleanly and includes the entire scene (background + figure both tilted), not just the figure.

## Dialogue

See `dialogue-style.md`. All checklist items there must pass.

## Per-panel definition of done

A panel is "finished comic art quality" when:

1. Every checkbox above is checked.
2. Re-rendered via mcp/playwright at native viewBox dimensions.
3. Compared screenshot-vs-script — every Shot, Camera, Action, Expression, Lighting, and key painterly-prompt element from `comic/scripts/Issue01_Descent_Script.md` is visibly present in the rendered output.
4. Reviewed against the failure modes from REVIEW.md to confirm none recur (no submarines instead of recon vessels, no toques instead of buzz cuts, no teapots instead of hands, no missing consoles, no stick-figure squad members).

## Realistic scope warning

Hand-coded comic-art SVG is **slow per panel**. Expect:

- Character templates: ~15–25KB each, 200+ elements (current ~14KB, 130–150 elements — needs ~50% more density).
- Action panels with multiple figures: ~40–80KB, 400+ elements.
- ECU panels (one figure): ~25–40KB, 250+ elements.
- 22 pages × ~5 panels avg per page × Issue 1 alone = ~100 finished-art panels. At one-per-iteration pace this is dozens of hours of work.

Page 1 + Page 2 (the validation set) = 11 panels. Get those right first; only then scale.
