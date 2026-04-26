# Character SVG Templates

Master templates for the six main characters of GrimGlow. Each template is a self-contained 400×600px SVG that encodes a character's full visual recipe — proportions, suit color stops, accent geometry, hair, skin, and (where applicable) wing-pack and wear-state overlays.

These are **not** used directly as panel artwork. They are the visual vocabulary that per-panel SVGs reference and re-pose for each scene.

## The Six Templates

| File | Character | Department | Suit | Key visual markers |
|------|-----------|------------|------|--------------------|
| `sable.svg` | Sable | Command | Silver | Dark brown skin, silver-white close-cropped hair, blue-white hex accents, sidearm right hip |
| `wren.svg` | Wren | Engineering | Silver + copper trim | East Asian, low black knot, copper-gold round accents, utility belt with tools, oil-stained hands |
| `jink.svg` | Jink | Reconnaissance | Emerald (full color) | Light brown skin, golden-blonde curly hair, dragonfly wing-pack, emerald hex accents |
| `thresh.svg` | Thresh | Security | Crimson/ruby (full color) | Pale skin, copper-red swept-back hair, heavier armor (chunky pauldrons), red hex accents, rifle on back |
| `luma.svg` | Luma | Science/Medical | Sapphire-violet (full color) | South Asian warm brown skin, single thick braid over right shoulder, holographic lens visor, blue-violet accents |
| `theodore.svg` | Theodore | (Human) | None — Victorian working clothes | Sandy-brown tousled hair, freckles, off-white linen shirt, brown waistcoat, brass gear pendant, oil-stained hands |

## Visual Ground Truth

Each template is calibrated against the corresponding turnaround sheet in `concept-art/<Name>/`. The clean-suit turnarounds (`*_CleanSuit_*.png`) define the pristine baseline. Mid-mission and heavy-wear turnarounds inform the wear-state overlay groups inside each template.

## Template Structure (Common Pattern)

Every template follows the same internal structure. Read `sable.svg` as the canonical reference.

### `<defs>`

Named gradients and filters keyed by character prefix:

- `<character>SuitMetal` — vertical linear gradient defining the suit's primary metal color stops (5 stops, top-bright → bottom-dark).
- `<character>SuitHighlight` — horizontal linear gradient overlaid on plates for left-edge catch-light.
- `<character>SuitSeam` — vertical dark-to-darker for plate seams and undersuit.
- `<character>SkinTone` — vertical gradient for exposed skin (face, neck, hands, forearms).
- `<character>Hair` — radial or linear depending on style (volume vs. flat).
- `<character>HologramCore` — radial gradient for the bright center of holographic accent nodes (department-color-keyed).
- `<character>HologramGlow` — radial gradient for the bloom around accent nodes.
- `<character>Shadow` — feDropShadow filter for grounding the figure.
- `<character>HoloBloom` — feGaussianBlur filter for the soft bloom on accents.
- `<character>HexNode` (or `<character>CopperNode` for Wren) — reusable `<symbol>` for an accent node (hexagonal for fairy-tech, circular for Wren's engineer fitting).

### Layered figure groups

The figure is composed in z-order from back to front:

```
<g id="<character>-figure" filter="url(#<character>Shadow)">
  <g id="<character>-legs">...</g>      <!-- z=0 -->
  <g id="<character>-torso">...</g>     <!-- z=1 -->
  <g id="<character>-arms">...</g>      <!-- z=2 -->
  <g id="<character>-head">...</g>      <!-- z=3 -->
</g>
```

Jink has an additional `jink-wingpack-rear` group placed BEFORE the figure group so the wings render behind the body.

Thresh has a `thresh-back-rifle` group with a rifle stock peeking up behind the right shoulder.

### Wear-state overlays

Each template (except Theodore) includes four toggleable overlay groups appended after the figure:

```
<g id="<character>-wear-clean" display="inline"/>      <!-- baseline, no overlay -->
<g id="<character>-wear-fresh-impact" display="none">  <!-- Issue 1 post-crash -->
<g id="<character>-wear-mid-mission" display="none">   <!-- mid-volume soot/scratches -->
<g id="<character>-wear-heavy" display="none">         <!-- late-volume heavy damage -->
```

A panel SVG that needs Sable in mid-mission state copies the relevant figure groups and toggles the matching overlay's `display` to `inline`.

The specific damage shown in `fresh-impact` matches the Asset Manifest in each issue's script (e.g., Sable's cracked panel at right shoulder, Thresh's dented left pauldron, Luma's cracked lens).

## How a Panel SVG Uses These Templates

The hybrid approach: master template defines the visual recipe; each panel re-draws the character inline at the panel's specific pose, scale, expression, and wear-state.

Per-panel workflow:

1. **Read the panel's spec** in `comic/scripts/Issue<N>_<Title>_Script.md`. The Shot, Camera, Action, Expression, Lighting, and painterly art-prompt fields define what the panel must show.
2. **Identify which characters appear** and at what scale. Squad members are fairy-scale (~4 inches in-world). Theodore is human-scale. When both appear together, the squad members are dramatically smaller in frame.
3. **Compose the background scene first** — environment, atmosphere, light sources. Use linear gradients for sky/walls, radial gradients for individual light sources (gaslight = warm amber, holographic = cool blue-white). Layer with comments.
4. **Draw the figures** by re-creating the relevant `<g>` groups from the templates inline, transformed for the panel's pose:
   - `transform="translate(x,y) scale(s) rotate(r)"` to position and orient.
   - Adjust limb path coordinates if the pose requires (arms raised, body twisted, kneeling, falling, in flight).
   - Substitute the active wear-state overlay for the scene's degradation point.
   - For close-ups, drop the legs group; just torso + head.
5. **Add the holographic / fairy-tech elements** specified in the script — floating displays, glyphs, drive cores, weapons-system overlays. Use the same accent gradients defined per-character.
6. **Apply dual lighting** per Visual Language Rules in `CLAUDE.md` — every scene contrasts warm gaslight against cool holographic light, with accent radial gradients for each light source.
7. **Speech bubbles + dialogue** — keep the existing wireframe convention: speaker color border = suit color, panel-number badge top-right, shot-type abbreviation bottom-right.

## Quality Bar

The benchmark is `/home/TurtleWolfe/repos/SpokeToWork/public/spoketowork-logo-static.svg` — ~9.5KB, 67 paths, 4 named layers with HTML comments, named gradients in `<defs>`, feDropShadow filters, geometric precision (24 tread grooves at 15° increments).

**Templates target:** ~10–15KB each. All six current templates land in 13.8–15.2KB. Density per template: ~130–155 elements, 17+ defs entries (gradients/filters/symbols).

**Panel character figures target:** ~6KB+ when adapted into a panel — the panel SVG itself can grow well beyond that with background/lighting/effects.

## Loop Unit

**One panel per loop iteration.** Each iteration:

1. Reads one panel's spec from the issue script.
2. Produces one handcrafted panel composition that overwrites the corresponding region in the page SVG (for Issue 1 Page 1, that's `Issue01_Descent/page01.svg`).
3. Updates the page SVG so the dockerized viewer at `localhost:3001` reflects current progress.

Issue 1 Page 1 is the proof-of-concept (6 panels, 6 iterations). After it validates, the same templates serve every subsequent panel that features these characters — only future issues' wear-state overlays evolve.

## Future Templates

Volume 1 will eventually need additional templates beyond these six:

- Mr. Cribbage (clockmaker master, Issues 3–5)
- Lamplighter, telegraph clerk, and other Victorian witnesses (Issues 5+)
- Titans (dark-mirror fairy tech: oil-on-water iridescence, shadow that moves wrong)

These are added on demand when their first significant panel iteration arrives.
