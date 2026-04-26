# Page 1 + Page 2 Panel Review — Visual QA

**Method:** every panel SVG rendered in headless Chromium (mcp/playwright) at its native viewBox. Composed pages rendered at 800×1200 via `<object>` wrapper so external `<image xlink:href>` panel refs resolve. All screenshots in `screenshots/`.

**TL;DR:** Several panels are unrecognizable as the scenes the script describes. The character templates I built up front read as cartoon mascots when re-posed inline rather than as the painterly mid-mission figures the project is aiming for. Specific panel-by-panel issues below — I rank each with severity 🔴 critical (full redraw), 🟡 significant (partial fix), 🟢 minor.

---

## Page 1

### P01P01 — Establishing wide, recon vessel in temporal corridor (742×364)
Screenshot: `screenshots/p01p01.png`

- 🟡 Ship reads as a **submarine**, not the angular military "predatory fish" the script specifies. Hull curves are too smooth/cute; needs sharper angles, more aggressive silhouette.
- 🟡 Ship is too small relative to the corridor — slightly low-angle should still give it presence.
- 🟢 The two cyan dots near bow read like submarine portholes side-by-side rather than nav lights at the ship's extremities.
- ✅ Hexagonal lattice corridor walls converging to vanishing point is solid.
- ✅ Prismatic shimmer streaks across walls work.
- ✅ Caption + Sable speech-from-ship balloon legible and well-placed.
- ✅ Cool prismatic palette holds; no warm-light leakage.

### P01P02 — Sable MCU at command station (241×364)
Screenshot: `screenshots/p01p02.png`

- 🔴 **Sable's hair looks like a chef's toque / white turban**, not a "very short military-cropped silver-white buzz cut" — the rendering is a smooth dome reading as thick volume on top of head.
- 🟡 Holographic display behind her is generic — the glyphs/text rectangles read as a mockup placeholder, not living telemetry.
- 🟡 Chest accent nodes are barely visible.
- ✅ Skin tone, calm expression, blue tint, dialogue placement work.

### P01P03 — Wren at engineering console (241×364)
Screenshot: `screenshots/p01p03.png`

- 🔴 **No console / no holographic display visible.** Script calls for Wren hunched over a console with copper-gold hologram of geometric shapes and waveforms. Just a generic torso here.
- 🔴 Body proportions wrong — torso way too wide, shoulders look swollen/balloon-shaped.
- 🟡 Hair is a flat black mound on top, doesn't read as the messy knot/bun.
- 🟡 Arms terminate in the abdomen line, not visible reaching forward.
- 🟡 Mustache-like dark line under nose reads as a mustache (it's supposed to be jaw shadow).
- ✅ Copper accent nodes pop nicely.

### P01P04 — Jink restless at scout station (241×364)
Screenshot: `screenshots/p01p04.png`

- 🔴 Body is dutch-tilted but Jink's pose is awkward — limbs read as melted/blobby, posture doesn't say "lounged on jump seat one leg up".
- 🔴 The viewport with corridor streaks is tiny and pushed off to the right; supposed to be **behind** Jink showing the corridor rushing past.
- 🟡 "Curly blonde hair" rendered as a single yellow beehive blob, not curls.
- 🟡 No visible jump seat structure — Jink is supposed to be sitting on a wall-mounted seat, not at a console.
- ✅ Emerald color identification reads.
- ✅ Smirking face partially visible.
- ✅ Three speech balloons all readable.

### P01P05 — Thresh at weapon rack through bridge archway (494×364)
Screenshot: `screenshots/p01p05.png`

- 🔴 Wide-left panel but Thresh is centered, not framed through an archway looking down a corridor as the script calls for. The "archway" looks like a generic doorway frame, no perspective depth.
- 🔴 Thresh's face: cartoonishly small head with bouncing carrot-orange forelock — doesn't read as the "broad, copper-red buzz cut, square jaw, formidable" soldier.
- 🔴 Pose is flat front view — script says "back partially to camera, running her hands along weapon" — should be 3/4 back angle.
- 🟡 Rifle she's holding is barely visible behind her.
- 🟡 Weapons rack on right is just abstract red bars; doesn't read as a weapons rack.
- 🟡 Body proportions: torso normal but shoulders/arms are oddly tubular.
- ✅ Crimson glow on rack does signal "security zone".
- ✅ Dialogue balloon clean.

### P01P06 — Luma close-up with holographic lenses (241×364)
Screenshot: `screenshots/p01p06.png`

- 🔴 The "holographic lenses hovering in front of eyes" read as **regular glasses/eyewear**, not floating geometric lens displays.
- 🔴 The braid is barely visible — a thin black string running over right shoulder; should be a thick prominent rope of hair.
- 🟡 Hand near chin (the "thinking gesture") is barely perceivable — just a brown blob between her face and torso.
- 🟡 Three speech balloons stacked vertically eat frame real estate (3 balloons in a CU panel is rough).
- ✅ Skin tone, suit color reads correctly.
- ✅ Mouth slightly open expressing the cut-off line works.

---

## Page 2

### P02P01 — Bridge wide OTS Sable, full squad (494×364)
Screenshot: `screenshots/p02p01.png`

- 🔴 **Sable's "back of head + shoulder" foreground is a giant white-haired blob that dominates the frame** — looks like a snowman, not an OTS framing element.
- 🔴 Wren on the left is a stick figure with a tiny head; barely reads as Wren.
- 🔴 Jink in the middle looks like a child sitting on a green chair (proportions off, head too small).
- 🔴 Thresh in red is half-hidden behind the floating display.
- 🔴 Where's Luma? Supposed to be at science right; not visible.
- 🔴 Corridor archway with Thresh through it is missing — Thresh should be through an arch in the back wall.
- 🟡 The "holographic displays" are flat blue rectangles that don't read as holograms.
- ✅ Caption legible.
- ✅ Color-coding by suit reads at a glance.

### P02P02 — ECU Jink's hand drumming on knee (238×364)
Screenshot: `screenshots/p02p02.png`

- 🔴 **Looks like a teapot or a UFO**, not a hand drumming on a knee. The geometry doesn't read as anatomy at all.
- 🔴 The forearm coming in from upper-left is a green diagonal slab.
- 🔴 The "hand" is a beige amorphous shape with antennae.
- 🔴 The knee is a smooth green dome at the bottom; no anatomical landmark.
- 🔴 Fingers are not perceivable despite being modeled in the SVG.
- ✅ Out-of-focus prismatic background blur is OK.
- ✅ Wrist emitter glow visible.
- ✅ Dialogue placement legible.

### P02P03 — Sable + Thresh face each other through bridge arch (742×364)
Screenshot: `screenshots/p02p03.png`

- 🔴 Bodies are limbless from the waist down — they end at the hips with rectangular pelvises floating.
- 🔴 Both characters facing nearly head-on rather than profile — script: "profile framing".
- 🔴 The "Thresh-was-confident" beat doesn't land — Thresh looks small, slumped, with a generic orange bowl cut, not the "tall swept-back pomp".
- 🟡 Sable's hair still reads as a white knit cap / chef hat.
- 🟡 The archway between them is just a vertical strip of color separation — no architectural depth, no meeting of blue/crimson light at the threshold.
- 🟡 Holographic display behind Sable (left) is empty.
- 🟡 Weapon rack behind Thresh (right) barely visible.
- ✅ Department color separation across panel halves works.
- ✅ Dialogue clear.

### P02P04 — Wren flags ripple in field (366×364)
Screenshot: `screenshots/p02p04.png`

- 🔴 The "RIPPLE" annotation label is **literally the text "RIPPLE"** on the holographic display — looks like a Lorem-ipsum placeholder.
- 🟡 Wren's face is mostly hidden by the speech balloon; the brow-furrow / observational expression that defines this beat is gone.
- 🟡 Three speech balloons stacked top-left crowd the panel.
- 🟢 Hair just reads as a black helmet again.
- ✅ Console / display has actual data shown (better than P01P03).
- ✅ Hand on display visible.
- ✅ "92.0%" callout is decent.

### P02P05 — Luma fascination cut short (366×364)
Screenshot: `screenshots/p02p05.png`

- 🔴 Hair rendered as **black wisps coming out of the side of her head like horns or pigtails**, not pulled back smooth with a thick braid.
- 🟡 The thick braid trunk is invisible — the script's prominent rope-of-hair element doesn't exist.
- 🟡 The dramatic geometric light patterns from the lenses (script: "structured geometric patterns reflected onto cheeks") read as unintentional ink-blots/shadows.
- 🟢 Mouth open expression is barely there.
- ✅ Lenses bigger and read better here than P01P06 — actually look like lens displays with data inside.
- ✅ Suit color, sapphire chest accents read.
- ✅ "—" cut-off dialogue placement works for the held-breath beat.

---

## Composed pages

### page01.svg (composed)
Screenshot: `screenshots/page01_composed.png`
- ✅ All 6 panels render in their layout grid with correct borders, page title, and panel-number badges.
- The composition reads — but the overall page quality is bottlenecked by the per-panel issues above (especially P01P02, P01P03, P01P05, P01P06).

### page02.svg (composed)
Screenshot: `screenshots/page02_composed.png`
- ✅ All 5 panels render in their layout grid.
- Same caveat: page-level composition works, panel quality bottlenecks the result.

---

## Patterns across all panels (root causes)

1. **Hair is the worst recurring problem.** Sable's "buzz cut" is rendered as a smooth dome (toque). Wren's "messy bun" is a flat black helmet. Jink's "wild curls" are a beehive blob. Luma's "thick braid pulled back" is wisps + invisible braid. Thresh's "swept-back pomp" is a generic forelock. → Hair geometry needs a complete re-think — the smooth gradient ovals I'm using read as headwear, not hair. Likely needs jagged silhouettes, individual lock paths, or stippled overlay.

2. **Bodies feel like mascots, not action figures.** The torso/arm rounded rectangles consistently read as plush characters. Real comic figures need angular plate seams, weight, asymmetric pose. The character templates' "front-facing canonical pose" is being re-used too literally; per-panel poses should rotate, foreshorten, twist.

3. **Holographic displays are weak.** They read as flat rectangles with stacked rectangles inside (placeholder mockups), not "structured light trapped in geometry" per the visual language rules. Need true 3D-feeling layered geometry, depth, light bleed, scrolling-text artifacts.

4. **Environment is missing or perfunctory.** Bridge interior is mostly black with a strip of ceiling. Arches are color stripes. Weapon racks are abstract bars. Story-critical environment elements need actual scene rendering, not symbolic stand-ins.

5. **Off-canon proportions** keep slipping in (Wren's swollen torso, Jink's child-like head-to-body ratio, Thresh's small head). The character templates' proportions don't survive being re-drawn inline at different scales.

---

## What I want from you before I start fixing

1. **Triage:** Which panels first? My recommendation in priority order:
   - P02P02 (Jink's hand) — currently unrecognizable, easy isolated fix.
   - P02P01 (bridge wide) — anchor establishing shot for Page 2; needs Sable's OTS restraint + visible Luma + Thresh through arch.
   - P01P03 (Wren at console) — story-critical; missing console + display + arms.
   - P01P05 (Thresh weapon rack) — sets up Thresh's confidence beat; needs the archway framing + 3/4 back pose.
   - Then sweep all panels for: better hair (ALL characters), better holographic displays, better limbs/poses.

2. **Approach question:** for the hair problem in particular — do you want me to:
   - (a) Patch hair on each existing panel one at a time, or
   - (b) Rewrite the 6 character templates' hair geometry first, then re-do panels (more upfront work, every panel benefits)?

3. **Quality target:** Are these supposed to read as **finished comic art** or as **storyboard-quality wireframes that show what the panel WILL be**? The current state is closer to finished-but-amateur. If the goal is storyboards, the bar shifts to "is the action/staging legible" rather than "does the figure look anatomically correct."

I'll wait for direction on these before touching any panels.
