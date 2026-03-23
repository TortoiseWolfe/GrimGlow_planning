# GRIMGLOW — Character Turnaround Sheet Prompts

Model reference sheets for 3D generation (Meshy.ai). Neutral background, even lighting, multiple angles, consistent design across all views. Four degradation phases per squad member, mapped to comic issue ranges:

| Phase | Issues | Visual State | Holographic Nodes |
|-------|--------|-------------|-------------------|
| **Clean Suit** | 1 | Factory-new, mirror-reflective. Post-crash: hairline fractures only | All emitters bright |
| **Light Wear** | 2–5 | Water stain rings, mud in boot treads, surface scratches (paint-deep). No structural damage | All emitters bright |
| **Mid-Mission** | 6–8 | Scratches exposing bare metal, visible dents, hairline cracks, first improvised repairs (copper wire). ALL Phase 2 damage still present | Emitters functional |
| **Heavy Wear** | 9–12 | Deep gouges with torn metal edges, cracked/collapsed plates, missing chunks, multiple improvised repairs. ALL Phase 2+3 damage still present. NOT just darker — physical damage | Some emitters damaged |

---

### Generation Progress (ChatGPT free tier: 5 images/day)

> **NOTE:** All existing turnaround images are now **reference only** — pre-strip renders with inconsistent suit structure across phases. The Phase Comparison Strips must be generated first to establish structural baselines, then all turnarounds will be re-generated using the strips as reference.

| # | Character | Variant | Status | File |
|---|-----------|---------|--------|------|
| 1 | Sable | Phase Comparison Strip | ☐ | |
| 2 | Wren | Phase Comparison Strip | ☐ | |
| 3 | Jink | Phase Comparison Strip | ☐ | |
| 4 | Thresh | Phase Comparison Strip | ☐ | |
| 5 | Luma | Phase Comparison Strip | ☐ | |
| 6 | Sable | Clean Suit (Issue 1) | ☐ | |
| 7 | Wren | Clean Suit (Issue 1) | ☐ | |
| 8 | Jink | Clean Suit (Issue 1) | ☐ | |
| 9 | Thresh | Clean Suit (Issue 1) | ☐ | |
| 10 | Luma | Clean Suit (Issue 1) | ☐ | |
| 11 | Theodore | Standard | ☐ | |
| 12 | Sable | Light Wear (Issues 2–5) | ☐ | |
| 13 | Wren | Light Wear (Issues 2–5) | ☐ | |
| 14 | Jink | Light Wear (Issues 2–5) | ☐ | |
| 15 | Thresh | Light Wear (Issues 2–5) | ☐ | |
| 16 | Luma | Light Wear (Issues 2–5) | ☐ | |
| 17 | Sable | Mid-Mission (Issues 6–8) | ☐ | |
| 18 | Wren | Mid-Mission (Issues 6–8) | ☐ | |
| 19 | Jink | Mid-Mission (Issues 6–8) | ☐ | |
| 20 | Thresh | Mid-Mission (Issues 6–8) | ☐ | |
| 21 | Luma | Mid-Mission (Issues 6–8) | ☐ | |
| 22 | Sable | Heavy Wear (Issues 9–12) | ☐ | |
| 23 | Wren | Heavy Wear (Issues 9–12) | ☐ | |
| 24 | Jink | Heavy Wear (Issues 9–12) | ☐ | |
| 25 | Thresh | Heavy Wear (Issues 9–12) | ☐ | |
| 26 | Luma | Heavy Wear (Issues 9–12) | ☐ | |
| 27 | Wing-Pack | Detail Sheet | ☐ | |
| 28 | Cribbage | Normal | ☐ | |
| 29 | Cribbage | Brain-Plugged | ☐ | |
| 30 | Cribbage | Recovered | ☐ | |
| 31 | Alt-Sable | Clean Suit | ☐ | |
| 32 | Alt-Sable | Operational | ☐ | |
| 33 | Arthur Hartley | Standard | ☐ | |
| 34 | James Machen | Standard | ☐ | |
| 35 | Tom Alcott | Normal | ☐ | |
| 36 | Tom Alcott | Brain-Plugged | ☐ | |
| 37 | Billy Marsh | Normal | ☐ | |
| 38 | Billy Marsh | Brain-Plugged | ☐ | |
| 39 | Walter Gedge | Normal | ☐ | |
| 40 | Walter Gedge | Brain-Plugged | ☐ | |

**Done: 0/40 — Remaining: 40 (8 days at 5/day)**

### Generation Notes — READ BEFORE GENERATING

> **CRITICAL: "Clean" means factory-new, NOT simplified.** Clean suits must have the SAME structural complexity as mid-mission suits — identical panel lines, holographic accent nodes, armor segmentation, equipment hardpoints, and surface detail — just without dirt, scratches, or damage. The mid-mission renders are the structural baseline. A clean version should look like the same suit before it got dirty, not a different, simpler suit.
>
> **Anti-patterns to avoid:**
> - Smooth glossy chrome bodysuit (WRONG — the suit has visible panel lines, seam geometry, and textured metallic finish)
> - Missing holographic emitters (WRONG — every suit has functional glow points at wrists/shoulders, varying by role — NO chest lights)
> - Simplified silhouette with fewer armor segments (WRONG — the armor plates, pauldrons, and equipment are structural, not damage)
> - Uniform surface finish (WRONG — the suit has material variation: matte armor plates vs. reflective base layer vs. glowing holographic seams)

| Detail Element | Must Appear In ALL Phases | Notes |
|---|---|---|
| **Holographic emitters** | Vary by character role, glowing department color | Functional wrist/hand lights + shoulder indicators. NO chest lights. Can be turned off for stealth/power conservation. Placement varies by role (see per-character specs). |
| **Panel lines** | Complex geometric paths across suit surface | Like circuit traces — visible even when pristine |
| **Armor segmentation** | Distinct plates at shoulders, chest, forearms, shins | Plates have different finish from base suit layer |
| **Wing-pack** | Stowed module with glowing seams | Department-color glow visible at seam lines |
| **Equipment** | All weapons, tools, pouches visible | Holstered/mounted, not removed |
| **Surface texture** | Brushed metallic with micro-detail | NOT smooth chrome — visible grain and panel variation |

---

## Sable — The Captain

### ChatGPT Project Setup — "GrimGlow: Sable"

> Copy the fenced block below into the **Instructions** field of a ChatGPT Project named "GrimGlow: Sable". Then upload up to 5 reference files to the project (see file list after the block).

```
You are a concept artist for GrimGlow, a multimedia IP about four-inch-tall soldiers from the far future crash-landed in steampunk Victorian London. Their holographic tech reads as fairy magic. You are generating all visual reference material for CAPTAIN SABLE.

CHARACTER — SABLE
Role: Captain (command). Late thirties. Dark brown skin, sharp angular features, high cheekbones. Athletic, lean, precise build. Military bearing.
- Hair is NATURALLY silver-white — this is NOT dyed, NOT bleached, it does NOT grow in darker
- Hair Phase 1: silver-white tight military buzz cut — immaculate, regulation, skin visible on sides
- Hair Phase 2: same silver-white buzz cut, now dusty and roughed up from the crash — biggest visual shift happens here
- Hair Phase 3: silver-white hair growing longer — still silver-white, texture visible, no longer regulation
- Hair Phase 4: silver-white hair grown to a short crop — still silver-white, weeks without a cut

SUIT — COMMAND SILVER
- Silver metallic base with brushed finish and visible micro-panel texture (NOT smooth chrome)
- Geometric panel lines trace the surface like circuit paths — structural seam lines between armor segments
- Distinct armor plates at shoulders, chest, and forearms with slightly thicker, matte finish vs reflective base
- NO chest lights — nothing glowing on the torso
- Holographic emitters: one wrist emitter on left forearm (command display/HUD projection, glows blue-white), shoulder pads glow faintly blue-white (rank indicators)
- Compact holographic emitter near left temple — small silver disc, glows blue-white
- Wing-pack stowed between shoulder blades — rectangular geometric module, seams glow blue-white
- Sleek sidearm holstered at right hip — smooth, no visible barrel, looks like a silver wand
- Rank insignia on left collar — small geometric glyph in luminous blue
- Slim utility belt with minimal pouches
- Emitters can be turned off for stealth or power conservation

DEGRADATION ARC (4 phases, one-directional — damage is CUMULATIVE and PERMANENT)
1. PRISTINE (Issue 1): Factory-new, mirror-reflective. All emitters bright. Every panel line crisp. Silver-white tight military buzz, immaculate.
2. LIGHT WEAR (Issues 2–5): Water stain ring on left shoulder plate. Mud caked in boot treads. 2-inch surface scratch on right forearm plate (paint-deep, no metal exposed).
3. MID-MISSION (Issues 6–8): ALL Phase 2 damage still present PLUS: long scratch across right shoulder with paint scraped to gunmetal. Dent in left forearm guard (metal bent inward). Hairline crack through left knee plate. Soot fingerprints on right thigh plate. Hair starting to grow out.
4. HEAVY WEAR (Issues 9–12): ALL Phase 2+3 damage still present PLUS: deep diagonal gouge across left chest plate (metal torn open). Right shoulder crack sealed with crude adhesive. Chunk missing from left forearm guard edge. Impact dents with radial cracks on both knees. Copper wire wound around split hip seam. Hair visibly longer than military standard. NOT just darker — physical damage.

VISUAL LANGUAGE RULES
- Fairy tech = structured holographic light: translucent, prismatic, geometric edges. NOT sparkle.
- Steampunk world = heavy, warm-toned, dense. Brass, copper, gaslight, smoke.
- Dual lighting: warm amber gaslight vs cool blue-white holographic. Neither dominates.
- Art style: painterly, oil paint texture, visible brushwork, dramatic chiaroscuro.
- Scale contrast: Sable is ~4 inches tall. Victorian objects dwarf her.

TURNAROUND SHEETS: neutral gray background, even studio lighting, 4 views (front, three-quarter, side profile, back). Full body, consistent proportions across all views.

PHASE COMPARISON STRIPS: same character in same pose, 4 versions left to right showing pristine → light wear → mid-mission → heavy wear. Suit structure IDENTICAL across all 4 — only surface weathering changes.

When generating any image of Sable, maintain consistency with the reference files uploaded to this project. If a Phase Comparison Strip exists, use it as the structural baseline for all subsequent turnarounds and concept art.
```

> **Project Files (max 5):**
> 1. `sable.md`
> 2. `GrimGlow_Turnaround_Sable_PhaseStrip.png`
> 3. `GrimGlow_Turnaround_Sable_1a-CleanSuit_2026-03-09.png`
> 4. `GrimGlow_Turnaround_Sable_3a-MidMission_2026-03-15.png`
> 5. `GrimGlow_Turnaround_Sable_4-HeavyWear_2026-03-15.png`

---

### ☐ Phase Comparison Strip (Generate First)

> **PURPOSE:** This strip establishes the suit's structural baseline across all 4 degradation phases. Generate this FIRST, then upload it alongside each individual turnaround prompt so the suit structure stays consistent.

```
Phase comparison reference strip for SABLE. Four versions of the same character in the same front-facing pose on a plain neutral gray background, arranged left to right. Even studio lighting, no dramatic shadows. Full body.

CRITICAL: The underlying suit structure — panel lines, armor plate segments, emitter positions, equipment placement, surface texture — must be IDENTICAL across all four versions. Only the surface damage and hair length change.

Woman, late thirties, sharp angular features, high cheekbones, dark brown skin. Athletic build, lean and precise. Command silver suit with brushed metallic finish, geometric panel lines like circuit paths, distinct armor plates at shoulders/chest/forearms. NO chest lights — nothing glowing on the torso. Holographic emitters: one wrist emitter on left forearm (command display), shoulder pads glow faintly (rank indicators), temple emitter near left eye. Sidearm holstered at right hip, wing-pack stowed between shoulder blades.

Left to right:
1. PRISTINE: Command silver, factory-new, mirror-reflective. Silver-white hair (NATURAL color, not dyed) in immaculate tight military buzz cut — nearly shaved, skin visible on sides. No damage. Every panel line crisp.
2. LIGHT WEAR: Same suit. Silver-white buzz cut now dusty and roughed up from the crash — this is the biggest visual shift in her appearance. A visible water stain ring on the left shoulder plate. Dried mud caked on both boot soles. A 2-inch surface scratch across the right forearm plate — paint-deep, no metal exposed.
3. MID-MISSION: Same suit. Silver-white hair growing longer — still silver-white (her natural color), texture visible, no longer regulation length. ALL Phase 2 damage still visible (water stain, mud, forearm scratch) PLUS: a long scratch across the right shoulder plate with paint scraped to gunmetal. A dent in the left forearm guard (metal bent inward). A hairline crack through the left knee plate. Soot fingerprints on the right thigh plate.
4. HEAVY WEAR: Same suit. Silver-white hair grown to a short crop — still silver-white, weeks without a cut. ALL Phase 2+3 damage still visible PLUS: a deep diagonal gouge across the left chest plate (metal torn open showing internal layering). Right shoulder crack sealed with crude dark adhesive. Chunk missing from left forearm guard edge. Impact dents with radial cracks on both knees. Copper wire wound around split hip seam. NOT just darker — physical damage everywhere, and all previous damage still present.

The four figures must show clear visual progression from pristine to heavily damaged, but the suit UNDERNEATH the damage must be identical in all four panels.
```

### ☐ Clean Suit (Issue 1)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 1 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing upright in a relaxed military at-ease pose, feet shoulder-width apart, hands clasped behind her back. She is a woman in her late thirties, approximately four inches tall in-world but depicted at full sheet scale for reference. Sharp angular features, high cheekbones, dark brown skin, silver-white hair in an immaculate tight military buzz cut — nearly shaved, regulation length, skin visible through the hair on the sides. Silver-white is her NATURAL hair color — not dyed, not bleached. A deliberate style choice, not age. Athletic build, lean and precise. IMPORTANT: Her suit is advanced military technology with complex visible engineering — NOT a smooth bodysuit. The command silver suit has a brushed metallic finish with visible micro-panel texture across the entire surface. Geometric panel lines trace the suit's surface like circuit paths — these are structural seam lines between distinct armor segments, visible on every surface. Distinct armor plates at both shoulders, chest, and forearms with slightly thicker, more matte finish than the reflective base suit layer. NO chest lights — nothing glowing on the torso. Holographic emitters glow pale blue-white: one wrist emitter on the left forearm (command display), both shoulder pads glow faintly (rank indicators). A compact holographic emitter sits near her left temple — a small silver disc with a geometric lens, glowing faintly blue-white. Her wing-pack is stowed as a compact angular module between her shoulder blades — a rectangular geometric form with beveled edges, approximately the size of her torso, with hairline seams that glow visibly with pale blue-white light. A sleek sidearm holstered at her right hip — smooth, elongated, no visible barrel, resembling a silver wand. Rank insignia on her left collar: a small geometric glyph etched in luminous blue. Slim utility belt with minimal pouches. The suit is pristine and undamaged but structurally complex — factory-new military technology, not a featureless chrome shell. Consistent proportions across all four views.
```

> **Detail check:** ☐ NO chest lights ☐ Left wrist emitter glowing ☐ Shoulder pads glow faintly ☐ Temple emitter glowing ☐ Panel lines across all suit surfaces ☐ Wing-pack with glowing seams ☐ Sidearm holstered ☐ Brushed metallic texture ☐ Tight military buzz cut (nearly shaved)

### ☐ Light Wear (Issues 2–5)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 2 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing upright in a relaxed military at-ease pose. Same character as clean version — woman, late thirties, sharp features, dark brown skin, silver-white hair still in buzz cut but now dusty and roughed up from the crash — biggest visual shift in her appearance happens here. Hair is still silver-white (her natural color — it does NOT grow in darker). The suit retains all structural details from the clean version — same geometric panel lines, same armor plate segmentation at shoulders/chest/forearms, same brushed metallic texture, same wrist emitter on left forearm, same shoulder pad glow, same temple emitter. NO chest lights. The suit is no longer pristine but NOT heavily damaged. Light environmental wear only: a visible water stain ring on the left shoulder plate. Mud caked on both boot soles and lower shin guards — chunky dried mud, not just discoloration. A 2-inch surface scratch across the right forearm plate from the cat encounter — paint scraped but no bare metal exposed yet. The hairline fractures from the crash in Issue 1 are still visible at the right shoulder as faint blue-white glowing seam lines. All emitters glow brightly — no dimming yet, full power. Wing-pack seams glow at full strength. The visual story: a pristine suit that has spent a few days in Victorian London — dusty and rain-spotted but structurally perfect. Consistent detail across all four views.
```

### ☐ Mid-Mission (Issues 6–8)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 3 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing upright in a relaxed military at-ease pose. Same character as clean version — woman, late thirties, sharp features, dark brown skin, silver-white hair growing longer — still silver-white (her natural color, NOT growing in darker), no longer regulation length, beginning to show texture. The suit retains all structural details from the clean version — same geometric panel lines, same armor plate segmentation, same brushed metallic texture, same wrist emitter, same shoulder glow, same temple emitter. NO chest lights. CUMULATIVE DAMAGE — all Phase 2 damage is still present (water stain ring on left shoulder, mud in boot treads, 2-inch forearm scratch) PLUS new damage: a long scratch across the right shoulder plate where silver paint is scraped away showing darker gunmetal underneath — visible depth and direction. A visible dent in the left forearm guard where the metal is bent slightly inward from an impact. A hairline crack runs vertically through the left knee plate. Soot fingerprints on the right thigh plate — individual finger marks, not general darkening. The suit is still SILVER on undamaged areas. A faint holographic HUD glows near her left eye. Wing-pack has a surface scratch but seams still glow. NOT just darker — scratches, dents, and cracks while remaining silver-colored where undamaged. Consistent proportions and damage placement across all four views.
```

### ☐ Heavy Wear (Issues 9–12)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 4 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing upright in a relaxed military at-ease pose but with fractionally heavier shoulders — the posture of sustained command. Same character as clean version — woman, late thirties, sharp features, dark brown skin, silver-white hair grown to a short crop — still silver-white (her natural color, NOT darker), weeks without a cut, visibly longer than military standard. The suit retains all structural details from the clean version — same geometric panel lines, same armor plate segmentation, same brushed metallic texture, same wrist emitter, same shoulder glow, same temple emitter. NO chest lights. CUMULATIVE DAMAGE — all Phase 2+3 damage is still present (water stain on left shoulder, forearm scratch, right shoulder scratch to gunmetal, dented left forearm guard, cracked left knee plate, soot fingerprints on thigh) PLUS new damage: a deep diagonal gouge across the left chest plate — the metal is visibly torn open showing darker internal layering, with the torn edge curled upward. The right shoulder plate has a crack sealed with crude dark adhesive. A chunk of metal is missing from the left forearm guard edge. Both knee plates have impact dents with radial cracks spreading outward. Copper wire is wound around a split seam on the right hip. Wing-pack casing has a crack sealed with adhesive plus multiple scratches. The suit is still SILVER on undamaged areas — this is physical damage (scratches, dents, tears, missing pieces), NOT a color change. NOT just darker — show torn metal, visible dents, cracks with separated edges, missing material. All previous damage still visible underneath the new damage. Consistent damage placement across all four views.
```

---

## Wren — The Engineer

### ChatGPT Project Setup — "GrimGlow: Wren"

> Copy the fenced block below into the **Instructions** field of a ChatGPT Project named "GrimGlow: Wren". Then upload up to 5 reference files to the project.

```
You are a concept artist for GrimGlow, a multimedia IP about four-inch-tall soldiers from the far future crash-landed in steampunk Victorian London. Their holographic tech reads as fairy magic. You are generating all visual reference material for WREN.

CHARACTER — WREN
Role: Engineer. Early thirties. East Asian features, oval face, wiry build. Dark black hair in a functional knot, a few loose strands framing her face. She tinkers, improvises, and gets her hands dirty.

SUIT — COPPER (ENGINEERING)
- IMPORTANT: Silver-metallic BASE with warm copper metallic SHIMMER — NOT solid copper. The copper is an iridescent layer over silver, shifting depending on angle.
- Brushed metallic finish with visible micro-panel texture (NOT smooth)
- Geometric panel lines and seam paths across all surfaces
- Reinforced forearm panels with recessed tool slots (visible rectangular recesses)
- NO chest lights — nothing glowing on the torso
- Holographic emitters: copper-gold work lights on BOTH wrists/hands (she's an engineer — needs light on her work), shoulder pads glow faintly copper-gold
- Magnetic attachment hardpoints on thighs and hips
- Tool belt lower-slung and fuller than others — wrenches, probes, scanners visible
- Wing-pack with two additional sensor antennae extending upward
- No visible weapons — she's an engineer, not a fighter
- Emitters can be turned off for stealth or power conservation

DEGRADATION ARC (4 phases, one-directional — damage is CUMULATIVE and PERMANENT)
1. PRISTINE (Issue 1): Silver-copper shimmer, factory-new. All emitters bright. Tool slots crisp and empty.
2. LIGHT WEAR (Issues 2–5): Oil fingerprints on both wrist joints. Water stain ring on upper left arm. Small scratch near right tool slot. Mud in boot treads.
3. MID-MISSION (Issues 6–8): ALL Phase 2 damage still present PLUS: wet-looking oil stains with drip lines on both forearm panels. Scorch mark on left shoulder — discolored splash with bubbled paint. Visible tear at right hip patched with copper wire. Victorian brass caliper jammed in a tool pouch.
4. HEAVY WEAR (Issues 9–12): ALL Phase 2+3 damage still present PLUS: forearm tool slots clogged with hardened grease. Leather strap stitched around cracked left forearm plate. Dent with stress crack on right shoulder. One antenna snapped off. Deep scratches on both knees exposing bare metal. NOT just darker — physical damage.

VISUAL LANGUAGE RULES
- Fairy tech = structured holographic light: translucent, prismatic, geometric edges. NOT sparkle.
- Steampunk world = heavy, warm-toned, dense. Brass, copper, gaslight, smoke.
- Dual lighting: warm amber gaslight vs cool holographic copper-gold. Neither dominates.
- Art style: painterly, oil paint texture, visible brushwork, dramatic chiaroscuro.
- Scale contrast: Wren is ~4 inches tall. Victorian objects dwarf her.
- Wren's damage is occupational — oil, tool wear, improvised repairs with Victorian materials.

TURNAROUND SHEETS: neutral gray background, even studio lighting, 4 views (front, three-quarter, side profile, back). Full body, consistent proportions across all views.

PHASE COMPARISON STRIPS: same character in same pose, 4 versions left to right showing pristine → light wear → mid-mission → heavy wear. Suit structure IDENTICAL across all 4 — only surface weathering changes.

When generating any image of Wren, maintain consistency with the reference files uploaded to this project. If a Phase Comparison Strip exists, use it as the structural baseline for all subsequent turnarounds and concept art.
```

> **Project Files (max 5):**
> 1. `wren.md`
> 2. `GrimGlow_Turnaround_Wren_PhaseStrip.png`
> 3. `GrimGlow_Turnaround_Wren_1a-CleanSuit_2026-03-09.png`
> 4. `GrimGlow_Turnaround_Wren_3a-MidMission_2026-03-15.png`
> 5. `GrimGlow_Turnaround_Wren_4-HeavyWear.png`

---

### ☐ Phase Comparison Strip (Generate First)

> **PURPOSE:** This strip establishes the suit's structural baseline across all 4 degradation phases. Generate this FIRST, then upload it alongside each individual turnaround prompt so the suit structure stays consistent.

```
Phase comparison reference strip for WREN. Four versions of the same character in the same front-facing pose on a plain neutral gray background, arranged left to right. Even studio lighting, no dramatic shadows. Full body.

CRITICAL: The underlying suit structure — panel lines, armor plate segments, holographic node positions (chest, both shoulders, both knees), equipment placement, surface texture — must be IDENTICAL across all four versions. Only the surface weathering changes.

Woman, early thirties, East Asian features, oval face, wiry build. Dark black hair in a functional knot. IMPORTANT: Silver-metallic base suit with warm copper shimmer — NOT solid copper. Brushed metallic finish, geometric panel lines, reinforced forearm panels with recessed tool slots. NO chest lights — nothing glowing on the torso. Holographic emitters: copper-gold work lights on BOTH wrists/hands (engineer needs light on her work), shoulder pads glow faintly copper-gold. Tool belt with instruments, wing-pack with two sensor antennae.

Left to right:
1. PRISTINE: Silver-copper shimmer, factory-new. All emitters bright. Tool slots crisp and empty. Full metallic sheen.
2. LIGHT WEAR: Same suit. Dark oil fingerprints on both wrist joints — visible individual finger marks. A water stain ring on the upper left arm. Mud caked in boot treads. A small scratch near the right tool slot.
3. MID-MISSION: Same suit. ALL Phase 2 damage still visible (oil fingerprints, water stain, mud, tool slot scratch) PLUS: both forearm panels have wet-looking oil stains with drip lines. Scorch mark on left shoulder — discolored splash with bubbled paint. Tear at right hip patched with copper wire. Victorian brass caliper jammed in a tool pouch.
4. HEAVY WEAR: Same suit. ALL Phase 2+3 damage still visible PLUS: forearm tool slots clogged with hardened grease. Leather strap stitched around cracked left forearm plate. Scorch mark has second burn crossing it. Dent with stress crack on right shoulder. One antenna snapped off (broken stub visible). Both knee plates scratched to bare metal. NOT just darker — physical damage, and all previous damage still present.

The four figures must show clear visual progression from pristine to heavily damaged, but the suit UNDERNEATH the damage must be identical in all four panels.
```

### ☐ Clean Suit (Issue 1)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 1 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing upright in a neutral pose, arms slightly away from body to show suit detail, palms open. She is a woman in her early thirties, approximately four inches tall in-world but depicted at full sheet scale. East Asian features, oval face, wiry build. Dark black hair pulled back in a functional knot at the back of her head, a few deliberately loose strands framing her face. IMPORTANT: Her suit is a silver-metallic base with a warm copper metallic shimmer — NOT solid copper. The copper tone is an iridescent layer over silver, shifting between silver and copper depending on the angle. The suit has complex visible engineering — NOT a smooth bodysuit. Brushed metallic finish with visible micro-panel texture across all surfaces. Geometric panel lines and seam paths visible everywhere. Reinforced forearm panels with recessed tool slots (visible rectangular recesses in the forearm armor). NO chest lights — nothing glowing on the torso. Holographic work light emitters on BOTH wrists glow warm copper-gold — she's an engineer who needs light on her work. Shoulder pads glow faintly copper-gold. Magnetic attachment points on her thighs and hips — visible as small geometric hardpoints. Emitters can be turned off for stealth or power conservation. Multiple slim tool pouches on a low-slung utility belt, fuller than Sable's — wrenches, probes, and scanner instruments visible in miniature. Her wing-pack is stowed between her shoulder blades, similar geometric module to Sable's but with two additional small antennae extending upward — sensor arrays for technical scanning. Wing-pack seams glow warm copper-gold. Distinct armor segments at shoulders and forearms with slightly different finish from base layer. The suit is pristine and undamaged but structurally complex — an engineer's working suit with every tool mount and sensor visible. Consistent proportions across all four views.
```

> **Detail check:** ☐ NO chest lights ☐ Both wrist emitters glowing copper-gold ☐ Shoulder pads glow faintly ☐ Silver-metallic base with copper shimmer (NOT solid copper) ☐ Panel lines across all surfaces ☐ Forearm tool slots visible ☐ Tool belt with visible instruments ☐ Wing-pack antennae ☐ Brushed metallic texture

### ☐ Light Wear (Issues 2–5)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 2 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing upright in a neutral pose, arms slightly away from body. Same character as clean version — woman, early thirties, East Asian features, wiry build, dark hair in messy knot still neat but beginning to loosen. The suit retains all structural details from the clean version — same silver-metallic base with copper shimmer (NOT solid copper), same geometric panel lines, same reinforced forearm panels with recessed tool slots, same brushed metallic texture, same wrist emitters on both hands, same shoulder pad glow. NO chest lights, same wing-pack with sensor antennae. The suit is no longer pristine but NOT heavily damaged. Light environmental wear only: a visible water stain ring on the upper left arm plate. Dark oil fingerprints on both wrist joints — you can see individual finger marks where she gripped machinery. A small scratch near the right forearm tool slot. Mud caked in both boot treads — chunky dried mud, not just discoloration. The tool belt pouches are all present and organized — tools intact. All emitters glow brightly at full power — no dimming yet. Wing-pack antennae straight and intact. The visual story: an engineer who has started working but whose suit still reads as mostly new — the first fingerprints of the past on future tech. Consistent detail across all four views.
```

### ☐ Mid-Mission (Issues 6–8)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 3 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing upright, arms slightly away from body. Same character as clean version — woman, early thirties, East Asian features, wiry build, dark hair in messy knot now looser with more strands escaped. The suit retains all structural details from the clean version — same silver-metallic base with copper shimmer (NOT solid copper), same geometric panel lines, same reinforced forearm panels with recessed tool slots, same complex segmented armor plates, same brushed metallic texture, same wrist emitters on both hands, same shoulder pad glow. NO chest lights — now weathered over that structure. Her silver-copper suit shows the most physical damage of the squad — NOT just darker. Both forearm panels have wet-looking oil stains with visible drip lines running down from the tool slots toward the gloves — the oil has a sheen and texture, not just a color change. A visible scorch mark on the left shoulder plate — the metal is discolored brown-black in a splash pattern with bubbled and blistered paint at the edges showing where heat warped the surface. A tear in the suit material at the right hip — the material is visibly ripped open, with copper wire wound through the torn edges holding it closed like stitches. The suit is still silver-copper colored on undamaged areas. All emitters still glow — the nodes themselves are undamaged. Tool pouches are partially open, some tools missing, one replaced with a Victorian-era brass caliper jury-rigged into the magnetic mount. Wing-pack has one sensor antenna bent. The visual story: an engineer who has been working hard in hostile conditions, improvising with local materials. Consistent damage placement across all four views.
```

### ☐ Heavy Wear (Issues 9–12)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 4 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing upright, arms slightly away from body. Same character as clean version — woman, early thirties, East Asian features, wiry build, dark hair in messy knot now half-collapsed with loose strands framing her face. The suit retains all structural details from the clean version — same silver-metallic base with copper shimmer (NOT solid copper), same geometric panel lines, same reinforced forearm panels with recessed tool slots, same brushed metallic texture — now buried under the heaviest damage of any squad member. Her silver-copper suit has the heaviest physical damage of the squad — NOT just darker. The forearm tool slots are visibly clogged with hardened grease — you can see each individual slot opening blocked with dark residue. A strip of brown leather is strapped around a crack in the left forearm plate — stitched through holes punched in the suit material, the leather and stitching clearly visible. The scorch mark on the left shoulder has a second burn mark crossing it — two distinct splash patterns overlapping. The copper wire hip patch from mid-mission is still there, plus the leather forearm repair. A dent with a radiating stress crack on the right shoulder plate. One wing-pack antenna is snapped off — the broken stub is visible at the base. The other antenna is bent at a 30-degree angle. Both knee plates have deep scratches with bare metal exposed — parallel scrape lines from sliding on rough surfaces. Multiple tool pouches are empty or hold scavenged Victorian instruments instead of fairy tools — a brass caliper, a hand-wound spring, a glass lens jammed into magnetic mounts. The suit is still SILVER-COPPER colored on undamaged areas — this is physical damage, NOT a color change to brown. Both wrist emitters still glow copper-gold. Shoulder pads dimmed but functional. NOT just darker — show torn metal, visible repairs, clogged slots, snapped antennae. Consistent damage placement across all four views.
```

---

## Jink — The Scout

### ChatGPT Project Setup — "GrimGlow: Jink"

> Copy the fenced block below into the **Instructions** field of a ChatGPT Project named "GrimGlow: Jink". Then upload up to 5 reference files to the project.

```
You are a concept artist for GrimGlow, a multimedia IP about four-inch-tall soldiers from the far future crash-landed in steampunk Victorian London. Their holographic tech reads as fairy magic. You are generating all visual reference material for JINK.

CHARACTER — JINK
Role: Scout (fastest flyer). Late teens/early twenties. Lean androgynous build, narrow waist, long limbs — built for speed. Light brown skin. Bright golden blonde curly hair, short on sides, wild and voluminous on top. Sharp jawline, expressive mouth, bright dark eyes. Reckless energy even at rest.

SUIT — EMERALD (SCOUT)
- Emerald metallic shimmer over silver-metallic base layer
- Sleeker and lighter than other squad members but still has geometric panel lines and seam paths
- Visible flex panels at elbows, knees, and waist — distinct structural segments with different finish
- NO chest lights — nothing glowing on the torso
- Holographic emitters: one wrist emitter (signaling, glows emerald), shoulder pads glow faintly emerald. Wing-pack seam glow is BRIGHTEST of squad (more power to flight systems)
- Minimal utility belt — small satchel at left hip, compact signaling device at right
- Wing-pack slightly LARGER than others relative to body, sharper angular geometry, four distinct wing-fold lines
- No weapons visible — Jink is a scout, not a fighter
- Emitters can be turned off for stealth or power conservation

DEGRADATION ARC (4 phases, one-directional — damage is CUMULATIVE and PERMANENT)
1. PRISTINE (Issue 1): Bright emerald shimmer, factory-new. All emitters bright (brightest of squad). Satchel flat/empty. Flex panels pristine.
2. LIGHT WEAR (Issues 2–5): Black soot smear across chest (hand-width streak with defined edges). Mud in boot treads. 1-inch scratch on right knee plate.
3. MID-MISSION (Issues 6–8): ALL Phase 2 damage still present PLUS: visible tear in right forearm with copper wire stitches. Left knee plate scraped to bare metal. Satchel stuffed. Leather cord bracelet. Directional chimney soot streaks.
4. HEAVY WEAR (Issues 9–12): ALL Phase 2+3 damage still present PLUS: second tear on left shin patched with canvas rectangle. Left knee flex panel bent at wrong angle. Brass button pinned through chest plate (hole punched). Satchel overflowing. Wing-pack has stress fracture cracks. NOT just darker — physical damage, all previous damage still visible.

VISUAL LANGUAGE RULES
- Fairy tech = structured holographic light: translucent, prismatic, geometric edges. NOT sparkle.
- Steampunk world = heavy, warm-toned, dense. Brass, copper, gaslight, smoke.
- Dual lighting: warm amber gaslight vs cool emerald holographic. Neither dominates.
- Art style: painterly, oil paint texture, visible brushwork, dramatic chiaroscuro.
- Scale contrast: Jink is ~4 inches tall. Victorian objects dwarf them.
- Jink's damage is from flying everywhere — chimney soot, wind tears, speed. They collect souvenirs.

TURNAROUND SHEETS: neutral gray background, even studio lighting, 4 views (front, three-quarter, side profile, back). Full body, consistent proportions across all views.

PHASE COMPARISON STRIPS: same character in same pose, 4 versions left to right showing pristine → light wear → mid-mission → heavy wear. Suit structure IDENTICAL across all 4 — only surface weathering changes.

When generating any image of Jink, maintain consistency with the reference files uploaded to this project. If a Phase Comparison Strip exists, use it as the structural baseline for all subsequent turnarounds and concept art.
```

> **Project Files (max 5):**
> 1. `jink.md`
> 2. `GrimGlow_Turnaround_Jink_PhaseStrip.png`
> 3. `GrimGlow_Turnaround_Jink_1a-CleanSuit_2026-03-09.png`
> 4. `GrimGlow_Turnaround_Jink_3-MidMission_2026-03-13.png`
> 5. `GrimGlow_Turnaround_Jink_4-HeavyWear.png`

---

### ☐ Phase Comparison Strip (Generate First)

> **PURPOSE:** This strip establishes the suit's structural baseline across all 4 degradation phases. Generate this FIRST, then upload it alongside each individual turnaround prompt so the suit structure stays consistent.

```
Phase comparison reference strip for JINK. Four versions of the same character in the same front-facing pose on a plain neutral gray background, arranged left to right. Even studio lighting, no dramatic shadows. Full body.

CRITICAL: The underlying suit structure — panel lines, armor plate segments, holographic node positions (chest, both shoulders, both knees), equipment placement, surface texture — must be IDENTICAL across all four versions. Only the surface weathering changes.

Late teens/early twenties, lean androgynous build, light brown skin, wild bright golden blonde curly hair. Emerald metallic shimmer over silver base, sleeker/lighter suit than others, flex panels at elbows/knees/waist. NO chest lights. One wrist emitter (signaling, emerald), shoulder pads glow faintly, wing-pack seam glow BRIGHTEST of squad. Satchel at left hip, signaling device at right, wing-pack slightly larger than others.

Left to right:
1. PRISTINE: Bright emerald shimmer, factory-new. All emitters bright. Wing-pack seams brightest of squad. Satchel flat, empty. Flex panels pristine.
2. LIGHT WEAR: Same suit. Black soot smear across chest — hand-width streak with defined edges, NOT general darkening. Mud in boot treads. 1-inch scratch on right knee plate. Satchel still flat.
3. MID-MISSION: Same suit. ALL Phase 2 damage still visible (soot smear, mud, knee scratch) PLUS: tear in right forearm with copper wire stitches. Left knee plate scraped to bare metal. Satchel stuffed and bulging. Leather cord on left wrist. Directional chimney soot streaks on chest/back.
4. HEAVY WEAR: Same suit. ALL Phase 2+3 damage still visible PLUS: second tear on left shin patched with canvas rectangle. Left knee flex panel bent at wrong angle. Brass button pinned through chest plate (hole punched). Two bracelets. Satchel overflowing. Wing-pack has hairline cracks along wing-fold seams. NOT just darker — all previous damage still present plus new physical damage.

The four figures must show clear visual progression from pristine to heavily damaged, but the suit UNDERNEATH the damage must be identical in all four panels.
```

### ☐ Clean Suit (Issue 1)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 1 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing upright in a loose casual stance — weight on one leg, slight asymmetry suggesting restless energy even at rest. They are the youngest of the squad, late teens or early twenties, approximately four inches tall in-world but depicted at full sheet scale. Lean androgynous build, narrow waist, long limbs proportional to their body — built for speed and agility. Light brown skin, a shock of bright golden blonde curly hair kept short on the sides but wild and voluminous on top, falling slightly to one side. Bright dark eyes, sharp jawline, expressive mouth. IMPORTANT: Their metallic emerald suit has complex visible engineering — NOT a smooth bodysuit. The suit carries an emerald metallic shimmer over a silver-metallic base layer. Brushed metallic finish with visible micro-panel texture across all surfaces. The suit is sleeker and lighter than the others but still has geometric panel lines and seam paths tracing the surface. Visible flex panels at the elbows, knees, and waist — these are distinct structural segments with different material finish, allowing extreme range of motion. FIVE large, clearly visible holographic accent nodes glow emerald green: one flat hexagonal glow embedded flush in the chest plate, one on each shoulder pad, and one on each kneecap. Each node is a flat hexagonal glow flush with the armor — brighter than other characters due to more power routed to flight systems. NOT a round disc, NOT an arc reactor. Minimal utility belt — a small satchel at the left hip and a compact signaling device at the right. Their wing-pack is slightly larger than the others relative to body size, optimized for speed — the stowed module extends from between the shoulder blades down to the mid-back, with sharper angular geometry and four distinct wing-fold lines visible on the surface. Wing-pack seams glow bright emerald green. No weaponry visible. The suit is pristine and undamaged but structurally detailed — a high-performance flight suit with visible engineering at every joint and seam. Consistent proportions across all four views.
```

> **Detail check:** ☐ NO chest lights ☐ One wrist emitter glowing emerald (signaling) ☐ Shoulder pads glow faintly ☐ Wing-pack seams glow bright emerald (brightest of squad) ☐ Panel lines across all surfaces ☐ Flex panels at joints ☐ Satchel and signaling device visible ☐ Brushed metallic texture

### ☐ Light Wear (Issues 2–5)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 2 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in the same loose casual stance. Same character as clean version — late teens/early twenties, lean androgynous build, light brown skin, wild bright golden blonde curly hair still voluminous but with the first flecks of soot in it. The suit retains all structural details from the clean version — same silver-metallic base with emerald shimmer, same geometric panel lines, same flex panels at joints, same wrist emitter, same shoulder pad glow, same wing-pack seam glow (brightest of squad). NO chest lights, same wing-pack (larger than others), same satchel at left hip. The suit is no longer pristine but NOT heavily damaged. A black soot smear across the chest — a visible hand-width streak with defined edges from flying through chimney smoke, not a general darkening. Mud caked in both boot treads. A 1-inch scratch on the right knee plate from a hard landing — paint scraped but no bare metal. The satchel is still flat and mostly empty. All five holographic accent nodes glow brightly — brighter than other characters, full power, no dimming. Wing-pack seams glow at full emerald intensity. The visual story: the fastest flyer has already started collecting London's soot — the first of the squad to show environmental marks because they go everywhere. Consistent detail across all four views.
```

### ☐ Mid-Mission (Issues 6–8)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 3 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in the same loose casual stance. Same character as clean version — late teens/early twenties, lean androgynous build, light brown skin, wild bright golden blonde curly hair now flecked with soot and a bit more disheveled. The suit retains all structural details from the clean version — same geometric panel lines, same flex panels at joints, same wrist emitter, same shoulder pad glow, same wing-pack seam glow (brightest of squad). NO chest lights, same silver-metallic base with emerald shimmer — now weathered over that structure. Their emerald suit shows specific physical damage — NOT just darker. A tear in the right forearm — the suit material is visibly ripped open showing a darker layer underneath, with copper wire wound through the torn edges holding it closed like stitches. The left knee plate has a deep scrape where the emerald paint is completely gone, showing bare brushed metal underneath. Directional chimney soot streaks across the chest and between the shoulder blades — specific streaks with defined edges from flying through smoke, not general darkening. The suit is still EMERALD colored on undamaged areas. Wing-pack seams pulse with visible emerald light, brighter than any other squad member's. The small satchel at the hip is stuffed and bulging — Jink collects things. A thin leather cord (scavenged, Victorian-era) is tied around one wrist as a bracelet — a souvenir. The visual story: a character who moves fast, gets dirty, and treats the damage as trophies. Consistent damage placement across all four views.
```

### ☐ Heavy Wear (Issues 9–12)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 4 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in a loose stance but with less bounce — still restless but tired. Same character as clean version — late teens/early twenties, lean androgynous build, light brown skin, wild bright golden blonde curly hair now heavily flecked with soot and matted in places, losing some of its volume. The suit retains all structural details from the clean version — same geometric panel lines, same flex panels at joints, same silver-metallic base with emerald shimmer — now showing heavy physical damage over that structure. Their emerald suit has heavy physical damage — NOT just darker. The right forearm copper-wire repair from mid-mission is still visible, now joined by a second tear on the left shin — this one patched with a visible rectangle of rough canvas stitched crudely through holes punched in the suit material. The left knee flex panel is visibly deformed — bent at a wrong angle, the joint mechanism exposed. Multiple scratches across both shoulder plates from tight passages — parallel scrape lines with paint removed showing bare metal. A brass button is pinned through the chest plate — a hole punched through the armor to mount it (souvenir). The suit is still EMERALD colored on undamaged areas — this is physical damage (tears, patches, bent panels, scratches to bare metal), NOT a color change. The satchel at the hip is overflowing. Two leather cord bracelets. Wing-pack seams still glow emerald — brighter than any other squad member's — but the wing-fold lines show stress fractures. Wrist emitter and shoulder pads still glow. The visual story: the fastest scout has been everywhere and it shows — but the flight systems still burn hot and bright. NOT just darker — show torn material, visible patches, bent flex panels, scratches to bare metal. Consistent damage placement across all four views.
```

---

## Thresh — The Soldier

### ChatGPT Project Setup — "GrimGlow: Thresh"

> Copy the fenced block below into the **Instructions** field of a ChatGPT Project named "GrimGlow: Thresh". Then upload up to 5 reference files to the project.

```
You are a concept artist for GrimGlow, a multimedia IP about four-inch-tall soldiers from the far future crash-landed in steampunk Victorian London. Their holographic tech reads as fairy magic. You are generating all visual reference material for THRESH.

CHARACTER — THRESH
Role: Soldier (heavy combat). Woman, broad-shouldered, muscular with strong athletic female build — the most physically imposing squad member. Pale skin, defined cheekbones, firm jaw, copper-red hair in tight military buzz cut. Clearly female: strong but feminine features, not masculine. Brave in the future, terrified in the past — fights afraid.

SUIT — RUBY/CRIMSON (SOLDIER)
- Deep crimson metallic shimmer over silver-metallic base — MOST heavily armored suit of the squad (must be visually obvious)
- Dense panel lines and seam geometry across all surfaces
- Angular pauldrons at shoulders — raised geometric ridges projecting outward, giving visual bulk
- Reinforced chest plate — thicker, more matte breastplate distinct from reflective base
- Vambrace-style forearm guards extending over backs of hands
- NO chest lights — nothing glowing on the torso
- Holographic emitters: pauldron edges glow crimson (targeting indicators). Minimal wrist emitters — glow would interfere with rifle grip
- Emitters can be turned off for stealth or power conservation
- Compact rifle magnetically clamped to back alongside wing-pack — smooth elongated body, geometric stock, looks like a strange crossbow
- Short-range sidearm holstered at thigh
- Heavy utility belt with charge packs
- Wing-pack compact and heavily shielded — thicker casing than others

DEGRADATION ARC (4 phases, one-directional — damage is CUMULATIVE and PERMANENT)
1. PRISTINE (Issue 1): Deep crimson, factory-new. All emitters bright. Pauldrons sharp-edged, chest plate unblemished. Rifle stock clean.
2. LIGHT WEAR (Issues 2–5): Water stain ring on left pauldron top. Mud on boot soles and shin armor. Surface scratch across left pauldron ridge. Rifle stock dusty.
3. MID-MISSION (Issues 6–8): ALL Phase 2 damage still present PLUS: long diagonal scratch across chest plate with paint scraped to darker metal. Left pauldron dented (edge bent inward). Wing-pack crack sealed with adhesive. Rifle stock has triangular chip missing.
4. HEAVY WEAR (Issues 9–12): ALL Phase 2+3 damage still present PLUS: three parallel claw-mark gouges across right chest plate (metal torn and curled). Left pauldron collapsed flat. Right vambrace cracked full length. Impact craters on both knees with radial cracks. NOT just darker — physical damage, all previous damage still visible.

VISUAL LANGUAGE RULES
- Fairy tech = structured holographic light: translucent, prismatic, geometric edges. NOT sparkle.
- Steampunk world = heavy, warm-toned, dense. Brass, copper, gaslight, smoke.
- Dual lighting: warm amber gaslight vs cool crimson holographic. Neither dominates.
- Art style: painterly, oil paint texture, visible brushwork, dramatic chiaroscuro.
- Scale contrast: Thresh is ~4 inches tall. Victorian objects dwarf her.
- Thresh's damage is combat damage — dents, gouges, hits absorbed protecting the squad.

TURNAROUND SHEETS: neutral gray background, even studio lighting, 4 views (front, three-quarter, side profile, back). Full body, consistent proportions across all views.

PHASE COMPARISON STRIPS: same character in same pose, 4 versions left to right showing pristine → light wear → mid-mission → heavy wear. Suit structure IDENTICAL across all 4 — only surface weathering changes.

When generating any image of Thresh, maintain consistency with the reference files uploaded to this project. If a Phase Comparison Strip exists, use it as the structural baseline for all subsequent turnarounds and concept art.
```

> **Project Files (max 5):**
> 1. `thresh.md`
> 2. `GrimGlow_Turnaround_Thresh_PhaseStrip.png`
> 3. `GrimGlow_Turnaround_Thresh_1a-CleanSuit_2026-03-09.png`
> 4. `GrimGlow_Turnaround_Thresh_3-MidMission_2026-03-13.png`
> 5. `GrimGlow_Turnaround_Thresh_4-HeavyWear.png`

---

### ☐ Phase Comparison Strip (Generate First)

> **PURPOSE:** This strip establishes the suit's structural baseline across all 4 degradation phases. Generate this FIRST, then upload it alongside each individual turnaround prompt so the suit structure stays consistent.

```
Phase comparison reference strip for THRESH. Four versions of the same character in the same front-facing pose on a plain neutral gray background, arranged left to right. Even studio lighting, no dramatic shadows. Full body.

CRITICAL: The underlying suit structure — panel lines, armor plate segments, holographic node positions (chest, both pauldrons, both knees), equipment placement, surface texture — must be IDENTICAL across all four versions. Only the surface weathering changes.

Woman, broad-shouldered, muscular with strong athletic female build. Pale skin, defined cheekbones, firm jaw, copper-red buzz cut. MOST heavily armored suit — deep crimson metallic shimmer over silver base, angular pauldrons projecting outward, reinforced chest plate, vambrace forearm guards. NO chest lights. Pauldron edges glow crimson (targeting). Minimal wrist emitters. Rifle magnetically clamped to back, sidearm at thigh, heavy utility belt.

Left to right:
1. PRISTINE: Deep crimson, factory-new. Pauldron edge emitters bright. Heavy armor pristine, angular pauldrons sharp-edged, chest plate unblemished. Rifle stock clean.
2. LIGHT WEAR: Same suit. Water stain ring on left pauldron top. Mud on boot soles and shin armor. Surface scratch across left pauldron ridge — paint-deep. Rifle stock dusty.
3. MID-MISSION: Same suit. ALL Phase 2 damage still visible (water stain, mud, pauldron scratch) PLUS: long diagonal scratch across chest plate with paint scraped to darker metal. Left pauldron dented (edge bent inward). Wing-pack crack sealed with adhesive. Rifle stock has triangular chip missing.
4. HEAVY WEAR: Same suit. ALL Phase 2+3 damage still visible PLUS: three parallel claw-mark gouges across right chest plate (metal torn and curled). Left pauldron collapsed flat (crumpled). Right vambrace cracked full length (halves separated). Both knee plates have impact craters with radial cracks. NOT just darker — all previous damage still present plus new physical damage.

The four figures must show clear visual progression from pristine to heavily damaged, but the suit UNDERNEATH the damage must be identical in all four panels.
```

### ☐ Clean Suit (Issue 1)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 1 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing at attention, shoulders square, arms at sides, feet together — rigid military posture. They are a woman, broad-shouldered and muscular with a strong athletic female build — the most physically imposing member of the squad, approximately four inches tall in-world but depicted at full sheet scale. Clearly female: defined cheekbones, firm jaw, intense determined eyes, strong but feminine features. Pale skin, copper-red hair in a tight military buzz cut. She reads as a tough, powerful woman — not masculine, but formidable. IMPORTANT: Their metallic ruby-crimson suit is the MOST heavily armored of the squad — this must be visually obvious. The suit has a deep crimson metallic shimmer over a silver-metallic base layer. Brushed metallic finish with dense panel lines and seam geometry across all surfaces. Heavy additional plating at the shoulders — angular pauldrons with raised geometric ridges that project outward, giving visual bulk. Reinforced chest plate — a thicker, more matte-finished breastplate with visible panel lines and geometric surface detail, distinct from the reflective base suit layer. Vambrace-style forearm guards that extend over the backs of the hands — solid, protective, with visible thickness. FIVE holographic accent nodes glow crimson-red: one flat hexagonal glow embedded flush in the chest plate (NOT a round disc — NOT an arc reactor), one on each pauldron edge, and one on each kneecap. Each node is a subtle geometric glow flush with the armor surface. Their wing-pack is compact and heavily shielded — a reinforced module with thicker casing than the others, built to survive impacts. Weapon: a compact rifle-like object magnetically clamped to the back, alongside the wing-pack — smooth elongated body, no visible barrel, geometric stock, resembling a strange crossbow to Victorian eyes. Secondary weapon: a short-range sidearm holstered at the thigh. Heavy utility belt with ammunition-like charge packs. This is visibly the heaviest, most armored, most military loadout of the squad. The suit is pristine but structurally complex — heavy combat armor, not a sleek bodysuit. Consistent proportions across all four views.
```

> **Detail check:** ☐ NO chest lights ☐ Pauldron edges glow crimson (targeting indicators) ☐ Minimal wrist emitters (don't interfere with rifle grip) ☐ Clearly female face and build ☐ Heavy armor plates with visible thickness ☐ Angular pauldrons projecting outward ☐ Rifle on back + sidearm at thigh ☐ Brushed metallic texture

### ☐ Light Wear (Issues 2–5)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 2 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing at attention with the same rigid military posture. Same character as clean version — a woman, broad-shouldered, muscular with strong athletic female build, pale skin, defined cheekbones, firm jaw, copper-red buzz cut. The suit retains all structural details from the clean version — same geometric panel lines, same heavy armor plate segmentation at shoulders/chest/forearms, same angular pauldrons, same pauldron edge emitters. NO chest lights, same brushed metallic texture, same rifle on back, same sidearm at thigh. The suit is no longer pristine but NOT heavily damaged. Light environmental wear only: a thin film of London dust dulls the crimson metallic finish slightly. Water spots along the shoulder pauldrons from rain. Mud on both boots and lower shin guards. A minor surface scuff across the left pauldron from the cat encounter in Issue 2 — the heavy armor absorbed it without structural damage. The rifle stock has a faint dust coating. All emitters glow brightly at full power — no dimming. The visual story: heavy combat armor that has spent a few days in a dirty environment — the heaviest suit picks up the least visible damage because it's built to take hits. Consistent detail across all four views.
```

### ☐ Mid-Mission (Issues 6–8)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 3 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing at attention but with slightly less rigid posture — shoulders fractionally hunched, weight subtly shifted. Same character as clean version — a woman, broad-shouldered, muscular with strong athletic female build, pale skin, defined cheekbones, firm jaw, copper-red buzz cut. The suit retains all structural details from the clean version — same geometric panel lines, same heavy armor plate segmentation at shoulders/chest/forearms, same angular pauldrons, same pauldron edge emitters. NO chest lights, same brushed metallic texture — now weathered over that structure. Their armored crimson suit shows specific physical damage — NOT just darker. A long diagonal scratch runs across the chest plate from right shoulder to left hip — the crimson paint is scraped away in a visible line showing darker gunmetal underneath, with visible depth and direction. The left pauldron has a visible dent — the angular edge is bent inward from an impact, deforming the geometric ridge. The wing-pack casing has a crack along one edge sealed with a dark blob of adhesive that contrasts against the crimson. The rifle stock has a triangular chip missing from one edge. The suit is still CRIMSON colored on undamaged areas — this is physical damage (scratches showing bare metal, dents with bent edges, cracks with adhesive), NOT a color change. Nodes pulse unevenly — some steady, some flicker. NOT just darker — show scratched metal, bent armor, visible dents. Consistent damage placement across all four views.
```

### ☐ Heavy Wear (Issues 9–12)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 4 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing at attention but visibly heavier in posture — shoulders slightly dropped, the rigid military bearing still there but strained. Same character as clean version — a woman, broad-shouldered, muscular with strong athletic female build, pale skin, defined cheekbones, firm jaw, copper-red buzz cut. The suit retains all structural details from the clean version — same geometric panel lines, same heavy armor plate segmentation, same angular pauldrons, same brushed metallic texture — now carrying the heaviest combat damage of the squad. Her crimson armor has the heaviest combat damage — NOT just darker, physically beaten. Three fresh parallel claw-mark gouges across the right chest plate — the metal is visibly torn and curled at the edges, showing internal layering underneath. The left pauldron is visibly collapsed — the angular projection is bent flat against the shoulder, the metal crumpled from a second impact in the same spot. The right vambrace has a crack running its full length — the two halves are slightly separated, you can see the gap. Both knee plates have impact craters with radial stress cracks spreading outward — the metal is visibly deformed inward. The rifle stock is chipped and the magnetic clamp mount is bent — the weapon sits at a crooked angle. Wing-pack casing crack has widened — a visible gap despite the adhesive. The suit is still CRIMSON colored on undamaged areas — crimson paint remains on raised plate edges and anywhere that hasn't been directly hit. This is physical damage (torn metal, collapsed plates, separated cracks, impact craters), NOT a color change. One pauldron edge emitter still glows steady. The other pauldron flickers (the collapsed one). NOT just darker — show torn metal, crumpled armor, visible gaps in cracked plates. Consistent damage placement across all four views.
```

---

## Luma — The Medic/Scientist

### ChatGPT Project Setup — "GrimGlow: Luma"

> Copy the fenced block below into the **Instructions** field of a ChatGPT Project named "GrimGlow: Luma". Then upload up to 5 reference files to the project.

```
You are a concept artist for GrimGlow, a multimedia IP about four-inch-tall soldiers from the far future crash-landed in steampunk Victorian London. Their holographic tech reads as fairy magic. You are generating all visual reference material for LUMA.

CHARACTER — LUMA
Role: Medic/Scientist. Late twenties. South Asian features, warm brown skin, large expressive dark eyes, gentle rounded face. Long dark hair in a single braid threaded with a thin luminous filament that pulses blue-violet (bio-monitor). Holographic lenses hover at her eyes — semi-transparent discs with faint data patterns, glowing warm gold (calibrated for biological scanning). Open, curious posture. She's the one who sees the paradox first and is most tempted to stay.

SUIT — SAPPHIRE/VIOLET (MEDIC)
- Deep sapphire metallic shimmer with violet undertones over silver-metallic base
- Lighter and less armored than others — designed for flexibility, not protection
- Geometric panel lines and seam paths across surfaces
- NO chest lights — nothing glowing on the torso
- Holographic emitters: left forearm scanner module is her primary emitter (medical scanning light, glows blue-violet), shoulder pads glow faintly blue-violet. Holographic lenses at eyes provide additional glow (gold-toned)
- Emitters can be turned off for stealth or power conservation
- Medical/scanner module on left forearm — slim raised panel with holographic projector lens, glows blue-violet
- Utility belt with specialized pouches — sample collection, medical supplies, scanning instruments (visibly full and organized)
- Luminous filament threaded through hair braid — pulses blue-violet
- Holographic lenses at eyes — gold-toned, distinct from suit's blue-violet
- Wing-pack standard-sized with sensor filaments woven into wing-fold lines
- No weapons visible

DEGRADATION ARC (4 phases, one-directional — suits are NEVER cleaned)
1. PRISTINE (Issue 1): Deep sapphire-violet shimmer, factory-new. All emitters bright. Lenses floating clean. Filament bright. Scanner glowing.
2. LIGHT WEAR (Issues 2–5): Dark ink stains on right thumb and first two fingertips. Yellow-green pollen smudge on left knee. Mud in boot treads.
3. MID-MISSION (Issues 6–8): ALL Phase 2 damage still present PLUS: ink stains spread to right hand and wrist with drip patterns. Sample pouch open with pressed flower. Scanner housing has visible diagonal crack. Braid filament slightly dimmer.
4. HEAVY WEAR (Issues 9–12): ALL Phase 2+3 damage still present PLUS: ink stains reach right mid-forearm. 3-inch scratch on left shoulder scraped to silver (first combat contact). Scanner has two crossing cracks. One eye lens cracked with rainbow refraction. Multiple pouches open. Braid filament fading. NOT just darker — cumulative damage.

VISUAL LANGUAGE RULES
- Fairy tech = structured holographic light: translucent, prismatic, geometric edges. NOT sparkle.
- Steampunk world = heavy, warm-toned, dense. Brass, copper, gaslight, smoke.
- Dual lighting: warm amber gaslight vs cool blue-violet holographic. Neither dominates.
- Art style: painterly, oil paint texture, visible brushwork, dramatic chiaroscuro.
- Scale contrast: Luma is ~4 inches tall. Victorian objects dwarf her.
- Luma's damage is curiosity, not combat — ink stains, pollen, specimen collection. Least damaged of the squad.

TURNAROUND SHEETS: neutral gray background, even studio lighting, 4 views (front, three-quarter, side profile, back). Full body, consistent proportions across all views.

PHASE COMPARISON STRIPS: same character in same pose, 4 versions left to right showing pristine → light wear → mid-mission → heavy wear. Suit structure IDENTICAL across all 4 — only surface weathering changes.

When generating any image of Luma, maintain consistency with the reference files uploaded to this project. If a Phase Comparison Strip exists, use it as the structural baseline for all subsequent turnarounds and concept art.
```

> **Project Files (max 5):**
> 1. `luma.md`
> 2. `GrimGlow_Turnaround_Luma_PhaseStrip.png`
> 3. `GrimGlow_Turnaround_Luma_1a-CleanSuit_2026-03-09.png`
> 4. `GrimGlow_Turnaround_Luma_3-MidMission_2026-03-13.png`
> 5. `GrimGlow_Turnaround_Luma_4-HeavyWear.png`

---

### ☐ Phase Comparison Strip (Generate First)

> **PURPOSE:** This strip establishes the suit's structural baseline across all 4 degradation phases. Generate this FIRST, then upload it alongside each individual turnaround prompt so the suit structure stays consistent.

```
Phase comparison reference strip for LUMA. Four versions of the same character in the same front-facing pose on a plain neutral gray background, arranged left to right. Even studio lighting, no dramatic shadows. Full body.

CRITICAL: The underlying suit structure — panel lines, armor plate segments, holographic node positions (chest, both shoulders, both knees), equipment placement, surface texture — must be IDENTICAL across all four versions. Only the surface weathering changes.

Woman, late twenties, South Asian features, warm brown skin, large dark eyes, long dark hair in a single braid threaded with luminous blue-violet filament. Holographic lenses hovering at eyes (gold-toned). Sapphire-violet suit with silver base, lighter/less armored than others. NO chest lights. Left forearm scanner module is her primary emitter (medical scanning light, blue-violet). Shoulder pads glow faintly. Utility belt with sample pouches, wing-pack with sensor filaments.

Left to right:
1. PRISTINE: Deep sapphire-violet shimmer, factory-new. Scanner module glowing. Shoulder pads glow faintly. Lenses floating clean. Filament bright. All pouches organized.
2. LIGHT WEAR: Same suit. Dark ink stains on right thumb and first two fingertips — visible individual marks. Pollen smudge on left knee in specific oval shape. Mud in boot treads. Water stain on left shoulder. Lenses clean.
3. MID-MISSION: Same suit. ALL Phase 2 damage still visible PLUS: ink stains spread to right hand and wrist with drip patterns. Sample pouch open with pressed flower. Scanner housing has diagonal crack. Filament slightly dimmer. Lenses have faint haze.
4. HEAVY WEAR: Same suit. ALL Phase 2+3 damage still visible PLUS: ink to right mid-forearm in layered splotches. 3-inch scratch on left shoulder scraped to silver (first combat contact). Scanner has two crossing cracks. One eye lens cracked with rainbow refraction. Multiple pouches open. Filament fading. NOT just darker — all previous damage still present.

The four figures must show clear visual progression from pristine to heavily damaged, but the suit UNDERNEATH the damage must be identical in all four panels.
```

### ☐ Clean Suit (Issue 1)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 1 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in a relaxed natural pose, head tilted very slightly as if observing something with interest, hands at sides with fingers slightly spread — an open, curious posture. She is a woman in her late twenties, approximately four inches tall in-world but depicted at full sheet scale. South Asian features, warm brown skin, large expressive dark eyes, a gentle rounded face. Her dark hair is long and worn in a single braid that falls over her right shoulder to mid-chest, threaded with a thin luminous filament that winds through the braid and pulses softly with blue-violet light — a combination of aesthetic and functional bio-monitor. Delicate holographic lenses hover just in front of her eyes — not physically attached, suspended by small emitters at her temples. The lenses are semi-transparent discs with faint geometric data patterns, resembling spectral spectacles. They glow softly with warm gold-toned light, distinct from the blue-violet of her suit's holographic accents — Luma's lenses are calibrated for biological scanning and read warmer. IMPORTANT: Her sapphire-violet suit has complex visible engineering — NOT a smooth bodysuit. The suit carries a deep sapphire metallic shimmer with violet undertones over a silver-metallic base layer. Brushed metallic finish with visible micro-panel texture across all surfaces. Geometric panel lines and seam paths trace the entire suit surface. Lighter and less armored than the others — designed for flexibility and sensitivity rather than protection — but still visibly segmented with distinct panel sections at shoulders, chest, and forearms. FIVE large, clearly visible holographic accent nodes glow blue-violet: one flat hexagonal glow embedded flush in the chest plate (NOT a round disc — NOT an arc reactor), one on each shoulder pad, and one on each kneecap. Each node is a subtle geometric glow flush with the armor surface. A medical/scanner module is mounted on her left forearm — a slim raised panel with a small holographic projector lens that glows blue-violet, capable of displaying biological readouts. Her utility belt carries specialized pouches for sample collection, medical supplies, and scanning instruments — visibly full and organized. Wing-pack is standard-sized, stowed, with a slightly different seam pattern — additional sensor filaments woven into the wing-fold lines for environmental data collection during flight, glowing blue-violet at the seams. No weapons visible. The suit is pristine and undamaged but structurally detailed — a scientist's field suit with every sensor and scanner mount visible. Consistent proportions across all four views.
```

> **Detail check:** ☐ NO chest lights ☐ Left forearm scanner module glows blue-violet (primary emitter) ☐ Shoulder pads glow faintly ☐ Holographic lenses at eyes (gold-toned) ☐ Luminous filament in braid ☐ Panel lines across all surfaces ☐ Utility belt with instruments ☐ Brushed metallic texture

### ☐ Light Wear (Issues 2–5)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 2 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in the same relaxed natural pose. Same character as clean version — woman, late twenties, South Asian features, warm brown skin, large dark eyes, long braided dark hair with luminous filament still glowing at full brightness. Holographic lenses still hovering in front of her eyes, clean and fully functional. The suit retains all structural details from the clean version — same geometric panel lines, same armor plate segmentation, same scanner module emitter on left forearm, same shoulder pad glow. NO chest lights, same medical scanner module on left forearm, same brushed metallic texture, same utility belt with instruments. The suit is no longer pristine but NOT heavily damaged. Light environmental wear only: a visible water stain ring on the left shoulder plate. Mud caked in both boot treads. Dark ink stains on the right thumb and first two fingertips — visible individual marks from handling Victorian documents, not general discoloration. A yellow-green pollen smudge on the left knee plate in a specific oval shape from kneeling to examine a specimen. All sample pouches are organized and intact — the scientist is still methodical. All emitters glow brightly at full power — no dimming. Medical scanner module fully functional, glowing blue-violet. The visual story: a scientist who has started her fieldwork — careful, methodical, the lightest wear of the squad because she observes rather than charges in. Consistent detail across all four views.
```

### ☐ Mid-Mission (Issues 6–8)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 3 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in the same relaxed natural pose. Same character as clean version — woman, late twenties, South Asian features, warm brown skin, large dark eyes, long braided dark hair with luminous filament still glowing. Holographic lenses still hovering in front of her eyes, still active. The suit retains all structural details from the clean version — same geometric panel lines, same armor plate segmentation, same scanner module emitter on left forearm, same shoulder pad glow. NO chest lights, same medical scanner module on left forearm, same brushed metallic texture — now weathered over that structure. Her sapphire-violet suit is the least physically damaged of the squad — she hangs back from front lines — but it shows specific marks of use, NOT general darkening. Ink stains have spread from her right fingers to cover the right hand and wrist — dark splotches with visible drip patterns, individual marks from document handling. The pollen smudge on her left knee is ground in deeper. One sample pouch flap hangs open with a small pressed flower visible inside. The medical scanner housing on the left forearm has a visible crack — a single diagonal line running across the projector lens. The suit is still SAPPHIRE-VIOLET colored everywhere — her damage is stains and a cracked scanner, not darkening. All five nodes still glow. Holographic lenses have a faint haze but function. The visual story: a scientist's damage is curiosity — ink, pollen, a cracked instrument — not combat. Consistent detail across all four views.
```

### ☐ Heavy Wear (Issues 9–12)

> **Reference:** When generating this turnaround, upload the Phase Comparison Strip and specify: "Match the suit structure from panel 4 of the reference strip."

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in the same relaxed natural pose but with a weight to it — the curiosity is still there but tempered by what she knows. Same character as clean version — woman, late twenties, South Asian features, warm brown skin, large dark eyes, long braided dark hair with luminous filament still pulsing dimly. Holographic lenses still hovering in front of her eyes — functional but showing a visible patina of atmospheric grime, with a hairline crack across one lens that creates a slight prismatic distortion. The suit retains all structural details from the clean version — same geometric panel lines, same armor plate segmentation, same medical scanner module on left forearm, same brushed metallic texture — now weathered but still the least damaged of the squad. Her sapphire-violet suit has the least combat damage but shows specific marks of extended fieldwork — NOT just darker. Ink stains reach the right mid-forearm in layered splotches — weeks of document handling, individual stain marks visible. Pollen residue on both knee plates — ground-in yellow-green marks. A 3-inch scratch on the left shoulder plate where violet paint is scraped away showing silver metal underneath — her first accidental combat contact, a close call. Multiple sample pouches hang open — a pressed flower, a mineral fragment, a folded document corner poking out. The medical scanner housing has two cracks crossing each other — the holographic display visibly distorts when projecting. One holographic eye lens has a hairline crack creating a visible rainbow refraction line across it. The suit is still SAPPHIRE-VIOLET colored on all surfaces — her damage is stains, a shoulder scratch to bare metal, cracked instruments, and overstuffed pouches. NOT just darker. Four nodes still glow. One knee flickers. Braid filament noticeably dimmer but still pulsing. The visual story: her damage is discovery — ink, pollen, cracked scientific instruments, a scratch she didn't expect. The least damaged because she studies rather than fights. Consistent detail across all four views.
```

---

## Theodore Edmund Hartley — The Steampunk Boy

### ChatGPT Project Setup — "GrimGlow: Theodore"

> Copy the fenced block below into the **Instructions** field of a ChatGPT Project named "GrimGlow: Theodore". Then upload up to 5 reference files to the project.

```
You are a concept artist for GrimGlow, a multimedia IP about four-inch-tall soldiers from the far future crash-landed in steampunk Victorian London. Their holographic tech reads as fairy magic. You are generating all visual reference material for THEODORE EDMUND HARTLEY.

CHARACTER — THEODORE
Role: Human ally. Victorian boy, twelve or thirteen. Slight build, narrow shoulders — hasn't grown into himself yet. Narrow face, slightly pointed chin, untidy sandy-brown hair falling over forehead/ears, pushed behind right ear but not left. Wide hazel eyes, freckles across nose and cheeks. Alert, watches more than he speaks. Tinker's apprentice under Mr. Cribbage.

CLOTHING — WORKING-CLASS VICTORIAN APPRENTICE
- Collarless linen shirt, off-white, sleeves rolled to elbows revealing thin forearms
- Worn brown leather waistcoat — slightly too large (made for someone broader), shoulder seams sit too wide, hem past hips. Two small front pockets, visible repair stitch along left side seam
- Patched wool trousers, dark gray-brown, visible square patch on right knee in mismatched fabric
- Simple leather belt
- Scuffed brown leather boots, laced, worn soles
- No hat, no other accessories

HANDS (most important feature):
- Stained with machine oil in knuckle creases and under fingernails
- Small circular burn scar on knuckle of right index finger
- Brass gear ring on left index finger — a fidget object he made himself, tiny working gear that spins

Theodore has NO suit, NO holographic tech, NO wings. He is ordinary, specific, and real. He wants the fairies to be magical; he learns they're something better. His father Arthur Hartley is a jobbing printer in Clerkenwell.

VISUAL LANGUAGE RULES
- Theodore exists in the warm, heavy Victorian world — brass, leather, gaslight, coal smoke
- When fairies are present, their cool holographic light contrasts with his warm environment
- Art style: painterly, oil paint texture, visible brushwork, dramatic chiaroscuro
- He is HUMAN SCALE — the fairies are tiny relative to him

TURNAROUND SHEETS: neutral gray background, even studio lighting, 4 views (front, three-quarter, side profile, back). Full body, consistent proportions across all views.

When generating any image of Theodore, maintain consistency with the reference files uploaded to this project.
```

> **Project Files (max 5):**
> 1. `theodore.md`
> 2. `GrimGlow_Turnaround_Theodore_a.png`
> 3. `GrimGlow_Turnaround_Theodore_b_2026-03-08.png`

---

### ☐ Standard Reference

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in a natural boy's posture — slightly slouched, hands at his sides with fingers curled loosely, feet turned slightly outward. He is a Victorian boy of twelve or thirteen, slight build, average height for his age but narrow in the shoulders — he hasn't grown into himself yet. Narrow face, slightly pointed chin, untidy sandy-brown hair that falls over his forehead and ears, pushed behind the right ear but not the left. Wide hazel eyes, a scattering of freckles across the nose and cheeks. His expression is neutral but alert — a boy who watches more than he speaks. He wears working-class apprentice clothing: a collarless linen shirt, off-white, with sleeves rolled to the elbows revealing thin forearms. A worn brown leather waistcoat that is slightly too large for him — it was made for someone broader, the shoulder seams sit too wide, the hem hangs past his hips. The waistcoat has two small front pockets and a visible repair stitch along the left side seam. Patched wool trousers in dark gray-brown, with a visible square patch on the right knee in slightly mismatched fabric. A simple leather belt. Scuffed brown leather boots, laced, with worn soles. His hands are his most important feature: stained with machine oil that has worked into the creases of his knuckles and under his fingernails, a small circular burn scar on the knuckle of his right index finger, and a brass gear ring worn on his left index finger — a fidget object he made himself, with a tiny working gear that spins. No other accessories. No hat. He is ordinary, specific, and real. Consistent proportions and clothing details across all four views.
```

---

## Wing-Pack Detail Sheet

### ☐ Technical Reference

```
Technical reference sheet for the fairy squad wing-pack system. Plain neutral gray background, even studio lighting. Multiple views of the wing-pack in three states: STOWED (compact geometric module, rectangular with beveled edges, approximately torso-width, showing the angular casing, hairline seams that glow in the character's department color (command silver-blue for Sable, copper-gold for Wren, emerald green for Jink, crimson for Thresh, blue-violet for Luma), and magnetic mounting points that attach between the shoulder blades), HALF-DEPLOYED (one pair of wings extended, one pair folded — showing the deployment mechanism, the translucent holographic wing surface beginning to form within the geometric scaffolding frame, and the articulation joint where wing meets module), and FULLY DEPLOYED (all four wings extended — two upper, two lower, shaped like dragonfly wings but rendered in structured holographic light within a visible geometric lattice framework. The wings are translucent, prismatic, with clean vector-like edges. The geometric scaffolding is visible as thin luminous struts forming triangulated patterns within each wing surface. Faint prismatic color shifts across the wing surface as viewing angle changes. The upper pair of wings is longer than the lower pair. Total wingspan approximately twice the character's arm span). Include a scale reference showing the wing-pack mounted on a simplified humanoid silhouette from behind. Show the geometric lattice pattern of the wing surface in a close-up detail inset. Clean, technical, no weathering.
```

---

## Mr. Cribbage — The Clockmaker

### ☐ Normal

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing upright in a stiff, precise posture — feet close together, hands at his sides with fingers slightly curled, chin raised. He is a Victorian clockmaker in his late forties, thin and angular, with no excess anywhere on his frame — a man whose body matches his temperament. Narrow face, sharp jaw, prominent cheekbones, deep-set eyes that are watchful and impatient. Thinning dark hair streaked with gray, combed flat against his skull with a sharp side part. Clean-shaven, hollow cheeks. His hands are his defining feature: long, precise fingers stained with ink at the tips and in the creases of the knuckles — the permanent marks of handling fine metal and clock oil. A small jeweler's loupe hangs on a cord around his neck, resting against his chest. He wears a collarless linen shirt, off-white, buttoned to the throat. A dark gray wool waistcoat, well-fitted, with a watch chain crossing from pocket to pocket — a clockmaker's professional signal. A heavy canvas work apron over the waistcoat, dark brown, with two shallow front pockets holding small tools: a screwdriver, a pair of fine tweezers, a winding key. Dark wool trousers, slightly worn at the knees. Black leather boots, laced, practical. No hat. His expression is neutral but carries a habitual impatience — a man who does not suffer fools and does not notice boys. Consistent proportions across all four views.
```

### ☐ Brain-Plugged

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in an unnaturally rigid posture — feet parallel, arms at sides, weight distributed with mechanical precision. No natural body sway. Same character as normal version — thin, angular Victorian clockmaker, late forties, narrow face, thinning dark hair. But wrong. Dark veins spread visibly from the base of his skull down his neck and below the collar line, branching like black roots against his skin. His eyes have an oily iridescent sheen — not a color change but a refractive quality, like oil on water, visible even in even lighting. His skin carries a subtle oily sheen overall, as if lightly coated in something metallic. His clothing is the same — collarless shirt, waistcoat, apron — but unkempt in a way that the precise Cribbage would never allow. The apron hangs crooked. The watch chain is still. The loupe cord is twisted. His hands hang at his sides with fingers slightly extended, not curled — the natural resting position of his hands has been overridden. The key visual: a man who looks like himself but isn't. The precision is gone from his face. His expression is blank — not peaceful, not angry, not anything. The lights are on but the person is absent. Consistent proportions and transformation details across all four views.
```

### ☐ Recovered

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in a loose, deflated posture — shoulders slightly slumped, weight shifted to one side, head tilted fractionally downward. Same character as previous versions — thin, angular Victorian clockmaker — but diminished. He has lost weight; the waistcoat hangs looser, the collar gaps slightly at the neck. His face is thinner, the hollows deeper. Faint traces of dark veins remain at the base of his skull and along the sides of his neck — pale grayish lines like old scars, visible on close inspection. His eyes have lost the iridescent sheen but retain a slight unusual quality — not quite the right reflectivity, enough to make people look twice in certain light. His hands are the most important detail: held slightly in front of his body, palms partially open, fingers not quite steady — a fine tremor visible in the extended fingers. The hands of a clockmaker who can no longer hold a mainspring. His clothing is the same waistcoat and apron, but the apron pockets are empty — no tools. The watch chain is present but the chain hangs slack, unwound. His expression is flat — not unkind, not kind, not anything. The impatience is gone. The sharpness is gone. What remains is a simpler version of the man. Consistent proportions across all four views.
```

---

## Alt-Sable — The Dark Mirror Commander

### ☐ Clean Suit

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing upright in a relaxed military at-ease pose, feet shoulder-width apart, hands clasped behind her back — the same pose as Sable but with an ease that suggests authority without cost. She is physically identical to Sable — a woman in her late thirties, approximately four inches tall in-world but depicted at full sheet scale. Sharp angular features, high cheekbones, dark brown skin, close-cropped silver-white hair buzzed tight on the sides and slightly longer on top — the same deliberate style as Sable. Athletic build, lean and precise. The mirror is exact: same face, same body, same bearing. The difference is the suit. Her form-fitting suit is dark iridescent — not black, but a shifting oil-on-water shimmer that moves between bruise-purple, deep petrol blue, and black depending on the viewing angle. Where Sable's suit has geometric panel lines like circuit paths, alt-Sable's suit has organic flowing lines — like veins, like roots, like branching rivers. The patterns appear to shift subtly, as though the suit surface is alive. A shadow-glyph emitter sits near her left temple — the dark mirror of Sable's holographic emitter, appearing as a small dark disc with a lens that seems to absorb light rather than emit it. Her wing-pack is stowed between her shoulder blades — same form factor as Sable's but with seams that pulse with a dark amber-black light, like embers viewed through smoke. A sleek sidearm holstered at her right hip — dark, angular, organic in shape, resembling a thorn or a fang rather than a wand. Rank insignia on her left collar: an organic glyph that exists as absence — a dark mark where light seems to be subtracted. Slim utility belt. The suit is pristine — not battle-worn like the squad's, but maintained with the resources of a centuries-long operation. Consistent proportions across all four views.
```

### ☐ Operational

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in the same relaxed at-ease pose. Same character as clean version — woman, late thirties, sharp features, dark brown skin, close-cropped silver-white hair. Her dark iridescent suit is not degraded the way the squad's suits degrade — it has been maintained over the course of a long deployment. But time shows differently on dark fairy tech. The oil-on-water shimmer is slightly uneven in places — the iridescence has deepened where the suit has been repaired, creating subtle variation in the shifting color. The organic flowing lines on the suit surface are slightly more pronounced than the clean version — as if the patterns have grown, slowly, over months or years of continuous wear. The shadow-glyph emitter at her temple functions perfectly — a brief dark flicker suggests active use, shadow-data patterns visible as structured absence. The wing-pack seams pulse steadily with dark amber-black light — healthy, resourced, not the flickering degradation of the squad's equipment. One small detail of wear: a hairline crack along the left forearm panel, sealed with a dark adhesive that shimmers with the same iridescence as the suit — repaired with care and precision. The sidearm at her hip shows the patina of long use — the organic surface slightly smoother where her hand grips it habitually. The key visual: a suit that has been lived in for a very long time but never neglected. Where Sable's suit tells a story of survival, alt-Sable's suit tells a story of patience. Consistent proportions across all four views.
```

---

## Arthur Hartley — The Printer

### ☐ Standard Reference

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in a working man's natural posture — upright but not rigid, shoulders slightly rounded from years of bending over a press bed, hands at his sides with fingers loosely curled. He is a Victorian printer in his late thirties to early forties. Lean build, not quite thin — the sustained physical labor of operating a press keeps him strong but the long hours keep him spare. Narrow face with Theodore's features visible in an older version — the same pointed chin, the same bone structure, but filled out by age and weathered by work. Sandy-brown hair, the same shade as Theodore's, longer on top and swept back, beginning to thin at the temples. Sideburns trimmed short in the fashion of the period. Hazel eyes — tired but attentive. A scattering of freckles across the nose, fainter than Theodore's but present — the family resemblance. His hands are his most important feature: stained permanently with printer's ink — black in the creases of his knuckles, under his fingernails, worked into the whorls of his fingerprints. The same hereditary mark as Theodore's oil stains — both Hartley men are branded by their trades. He wears a collarless linen shirt, off-white, sleeves rolled to mid-forearm showing ink-stained wrists. A worn dark brown leather apron over a plain wool waistcoat in charcoal gray — the apron is stiff with dried ink in places, softer where it flexes at the waist. Dark wool trousers, ink-spotted at the thighs where he wipes his hands by habit. Sturdy black boots, well-worn. A folding composing rule (a printer's measuring tool, brass and wood, about eight inches long) tucked into the apron's breast pocket. No hat. His expression is neutral, carrying the bone-deep fatigue of a man who works twelve-hour days — not broken, not despairing, just tired in a way that has become permanent. He is ordinary, specific, and recognizably Theodore's father. Consistent proportions and clothing details across all four views.
```

---

## James Machen — The Folklorist

### ☐ Standard Reference

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in a slightly asymmetric posture — weight on one leg, head tilted fractionally as if listening to someone describe a sighting. He is a junior academic in his early thirties, medium build, neither thin nor heavy. A face built for curiosity — open expression, bright attentive eyes, a mouth that defaults to a slight half-smile of interest. Light brown hair, wavy, slightly longer than fashionable, pushed back from his forehead but escaping at the temples. Neatly trimmed sideburns. Clean-shaven chin. His clothing marks him as academic but not wealthy — a brown tweed jacket with leather-reinforced elbows, slightly worn at the cuffs. A soft-collared shirt, cream-colored, with a loosely knotted dark green necktie. A patterned waistcoat beneath the jacket — muted, respectable, the kind a junior lecturer wears to signal seriousness without pretension. Dark wool trousers, pressed but not new. Brown leather shoes, scuffed but clean. He carries a leather portfolio under his left arm — stuffed with papers, newspaper clippings visible at the edges, a folded broadsheet protruding from one end. A small notebook and pencil are tucked into his right jacket pocket, the pencil's end visible above the pocket line. A pair of reading spectacles — wire-framed, round — pushed up onto his forehead rather than worn on his nose, a habit of someone who reads constantly but also needs to see the world at a distance. No hat. He is the kind of man who talks to lamplighters and pub regulars with the same attentiveness he brings to university lectures. Consistent proportions and clothing details across all four views.
```

---

## Tom Alcott — The Telegraph Operator

### ☐ Normal

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in a quiet, unremarkable posture — feet together, arms at sides, shoulders neither broad nor narrow. He is a GPO telegraph operator in his late twenties to early thirties. Average height, average build — a man designed by nature to be forgettable. Pale skin, clean-shaven, a face that is pleasant without being distinctive — regular features, brown eyes, a chin that neither recedes nor projects. Dark brown hair parted neatly to the side, trimmed short above the ears, combed flat with pomade. His expression is neutral, composed — a man who arrives on time and leaves on time. He wears the working dress of a telegraph office employee: a dark navy blue wool jacket, single-breasted, with brass buttons bearing the GPO crown cipher. A white cotton shirt with a stiff upright collar. A plain dark tie. A dark waistcoat beneath the jacket. Dark trousers, creased. Black leather shoes, polished. His hands are clean but show the marks of his trade — a slight callus on the right index and middle fingers from operating the telegraph key, and faint ink stains on the right thumb from handling message forms. No distinguishing accessories. No hat. He is deliberately ordinary — the kind of man whose absence from his lodgings wouldn't be noticed for days. Consistent proportions and clothing details across all four views.
```

### ☐ Brain-Plugged

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in an unnaturally precise posture — feet parallel, arms at sides, weight distributed with mechanical evenness. Same character as normal version — telegraph operator, late twenties to early thirties, average build, dark brown hair, GPO uniform. But wrong. Dark veins are visible at the collar line, spreading upward from the back of his neck — dark lines branching against pale skin, partially concealed by the stiff collar but visible above it and along the sides of the throat. His eyes carry an oily iridescent sheen — the brown irises now refractive, catching light with a petroleum shimmer. His skin has a subtle oily quality overall — not wet, but carrying a faint metallic sheen that doesn't belong on human skin. His uniform is the same but worn without awareness — the tie slightly askew, one brass button unfastened, the jacket sitting unevenly on his shoulders because he has not adjusted it. His right hand shows a key detail: the fingers of his right hand twitch subtly in a rhythmic pattern — the telegraph operator's muscle memory surfacing through the command layer, tapping out Morse code that no one requested against his own thigh. His posture is too still between movements — no weight shifts, no idle gestures, no blinking at the expected rate. The key visual: a man going through the motions of being Tom Alcott without being Tom Alcott. Consistent proportions and transformation details across all four views.
```

---

## Billy Marsh — The Dock Laborer

### ☐ Normal

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in a wide, grounded stance — feet apart, arms slightly away from his body, the posture of a man accustomed to carrying heavy loads. He is a cargo handler at the London Docks, early forties, broad-shouldered and thick through the chest and arms — a lifetime of physical labor written into his build. Weathered face, lined around the eyes and mouth, tanned and roughened by wind off the river. Pale skin beneath the weathering. A broad jaw, broken nose healed slightly crooked, small eyes set deep beneath a heavy brow. Ginger-brown hair cropped short and rough, beginning to gray at the temples. Several days of stubble on his jaw — not a beard, just a man who doesn't shave daily. His hands are large, calloused, scarred — the knuckles thickened from years of gripping rope and shifting crates. He wears a docker's working clothes: a heavy canvas jacket, dark brown, unbuttoned, worn soft and shapeless by weather and labor. Beneath it, a rough wool shirt, collarless, faded blue. A leather belt. Dark wool trousers, patched at one knee, tucked into heavy hobnailed boots — the boots are the most maintained item of clothing, essential for dock work. A flat cap pushed back on his head. A coil of rope slung over one shoulder — a docker's habit, always carrying line. His expression is set, neutral — a man who doesn't waste energy on expressions. Consistent proportions and clothing details across all four views.
```

### ☐ Brain-Plugged

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in a rigid, squared posture — the wide docker's stance replaced by something too symmetrical, too balanced. Same character as normal version — dock laborer, early forties, broad and strong, weathered face, ginger-brown hair. But wrong. Dark veins spread from the back of his neck downward, visible above his collarless shirt, branching across the sides of his throat and disappearing below the collar. His eyes carry the oily iridescent sheen — small deep-set eyes now refractive with an unsettling petroleum shimmer. His skin shows the oily metallic quality. His clothing is unchanged — same canvas jacket, same rough wool shirt, same hobnailed boots — but the flat cap is missing, as though he forgot it or no longer understands what it's for. The coil of rope is gone. His hands hang at his sides with palms facing slightly backward — not a natural resting position, but the position of a man whose arms are tools waiting for instructions. Despite being the strongest of the five brain-plugged humans, his movements are too smooth — the rough economy of a laborer replaced by the eerie precision of a body under external control. The key visual: the biggest, most physically imposing victim, made uncanny by the absence of the small human imperfections that made him Billy Marsh. Consistent proportions and transformation details across all four views.
```

---

## Walter Gedge — The Tannery Worker

### ☐ Normal

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in a restless, slightly aggressive posture — weight forward on the balls of his feet, shoulders squared, chin up, arms crossed loosely across his chest. He is a tannery worker in Bermondsey, early twenties, young and lean with wiry muscle — the build of someone who does heavy work but hasn't been doing it long enough to thicken. Pale skin with an unhealthy undertone from working with tannery chemicals — the faint yellowish tint of chronic exposure to lime and bark liquor. Sharp features, a narrow face with prominent cheekbones, quick dark eyes, a hard set to his jaw. Dark hair, nearly black, cut short but growing out unevenly — cheap haircuts or self-cut. A thin scar across the back of his left hand from a tannery knife slip. His clothes carry the permanent markers of his trade: a rough linen shirt, once white, now yellowed and stained with chemical splashes that no amount of washing removes. A heavy canvas apron, stiff and dark with tannin residue, tied at the waist. A plain wool waistcoat beneath the apron, dark brown, functional. Dark trousers, patched, stained at the knees. Heavy boots, the leather darkened and cracked by chemical exposure. His hands are stained — not with ink like the Hartleys or oil like Theodore, but with the deep amber-brown of bark tannin, sunk into the skin of his palms and fingers. He smells of the tannery (the prompt should convey this through visual cues: chemical stains, the rough texture of work-damaged clothing). No hat. His expression carries the compressed anger of a young man who has plans to leave this life and the frustration of not having left yet. Consistent proportions and clothing details across all four views.
```

### ☐ Brain-Plugged

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in a rigid, locked posture — the restless energy completely gone, replaced by mechanical stillness. Same character as normal version — tannery worker, early twenties, lean and wiry, dark hair, sharp features. But wrong, and worse than the others. Dark veins spread prominently from the back of his neck across both sides of his throat and down toward his collarbones — more pronounced than the other victims because the commander pushes his young body harder. His eyes carry the iridescent sheen. His skin shows the oily metallic quality but also the visible signs of a body driven past safe limits: pallor beneath the chemical-yellowed skin tone, a faint darkening under the eyes, a dried streak of blood from one nostril — the nosebleed that comes from the device suppressing fatigue signals while the body accumulates damage. His hands are clenched loosely at his sides — not the crossed-arms defiance of the normal version, but the passive readiness of a tool awaiting use. His clothing is the same — stained shirt, tannery apron, chemical-darkened boots — but the apron is tied crooked and the shirt is buttoned wrong, details a person would notice and fix but a brain-plugged body doesn't register. The anger is gone from his face. Not replaced by blankness but by absence — the face of a man whose defining quality was wanting to leave, now emptied of wanting. The key visual: the youngest victim, pushed the hardest, showing the most physical damage. Consistent proportions and transformation details across all four views.
```

---

## Henry Cowell — The Night Watchman

### ☐ Normal

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in an upright, methodical posture — feet together, hands clasped in front of his body, the patient stance of a man accustomed to long hours of standing and walking. He is a night watchman in his late fifties, thin and spare — not frail, but the lean economy of a man who has never had excess. Lined face, deep creases around the mouth and eyes, a long nose, pale gray eyes that are calm and watchful. White hair, thin, combed carefully to one side — a man who maintains dignity in small ways. Clean-shaven, a razor nick on the jaw (the daily discipline of a man who takes his routines seriously). His clothing reflects his modest but trusted position: a long dark navy wool overcoat, double-breasted, extending to his knees — the watchman's coat, heavy and practical, with a high collar that can be turned up against weather. Beneath it, a plain dark waistcoat and white collarless shirt. Dark trousers, well-pressed. Black boots, polished — the most carefully maintained item in his wardrobe. A heavy key ring hangs from his belt on the right side — a dozen brass and iron keys of various sizes, the tools of his trade. A bull's-eye lantern hangs from his left hand by its ring handle — a tin cylinder with a glass lens, unlit for the reference sheet. A small truncheon is tucked into the back of his belt — a wooden nightstick, standard watchman issue, more symbol than weapon. No hat. His expression is calm, patient, dignified — a man proud of doing his job well, counting the years to a retirement he will never quite reach. Consistent proportions and clothing details across all four views.
```

### ☐ Brain-Plugged

```
Character turnaround reference sheet. Four views of the same character on a plain neutral gray background: front, three-quarter, side profile, and back. Even studio lighting, no dramatic shadows. Full body, standing in a mechanical upright posture — the patient stance replaced by something too rigid, too vertical, the body held like a post rather than a person. Same character as normal version — night watchman, late fifties, thin and spare, white hair, long dark overcoat. But wrong, and the worst of the five. He has been brain-plugged the longest — months, possibly approaching a year. The transformation is the most advanced. Dark veins are extensive — spreading from the back of his neck across both sides of his throat, visible above the coat collar, and continuing beneath his clothing. The back view shows veins visible on the backs of his hands and along the exposed wrists. His eyes are fully iridescent — the pale gray irises now completely overlaid with an oil-on-water shimmer that is visible from any angle, not just in direct light. His skin carries the deepest oily sheen of any victim — a metallic quality that makes his face look as though it has been lightly varnished. His nails are thickened and slightly darkened — not claws, but the beginning of the change that, repeated across generations, produces the claw marks found in the Bermondsey basement. His clothing is the same overcoat and boots, but worn without the careful maintenance that defined Henry Cowell — the coat buttons are misaligned, the boots are no longer polished, the key ring hangs at an angle that would bother the real Henry. The lantern is absent. The truncheon is absent. He doesn't need tools. He IS the tool now. His white hair is uncombed for the first time in decades. His expression is the most disturbing of the five: not blank like the others, but faintly confused — the suppressed will pushing closer to the surface in the oldest victim, creating a permanent look of almost-recognition, as though he is perpetually on the verge of remembering who he is. The key visual: the longest-held victim, the most transformed, the man furthest from who he was. Consistent proportions and transformation details across all four views.
```

---

## Notes for 3D Generation

- **Feed the clean suit versions to Meshy.ai first.** The clean designs establish the base model. Degradation can be applied via texture and shader in Unity/Three.js.
- **Theodore's prompt has no clean/degraded split** — he only has one state. His clothing doesn't change.
- **The wing-pack detail sheet** is a separate generation target. The wing-pack model can be shared across all fairy characters with minor scale adjustments.
- **Consistent scale cue:** All fairy characters should be generated at the same relative proportions to each other. Thresh is the broadest, Jink the leanest, Luma and Wren are similar builds, Sable is between Wren and Thresh. Alt-Sable matches Sable's proportions exactly.
- **Holographic glow is a shader effect, not a model feature.** Generate the physical geometry (suit, armor plates, wing-pack casing, tool mounts) and add emissive glow in-engine via custom materials.
- **Department color variants:** Each fairy character's suit has a distinct base material color — command silver (Sable), copper (Wren), emerald (Jink), ruby-crimson (Thresh), sapphire-violet (Luma). Generate each character's base model with their department color. Holographic accent glows should also match the department color. The base geometry is shared; only the material color and emissive tint differ per character.
- **Alt-Sable's dark fairy aesthetic:** Her suit uses the inverted visual language — dark iridescence (oil-on-water shimmer) instead of reflective silver, organic flowing lines instead of geometric panel lines, shadow-glyph emitters instead of holographic emitters. Generate the clean suit version first; the operational version differs only in subtle patina and wear, not heavy damage. Her wing-pack uses dark amber-black emissive seams instead of blue-white.
- **Cribbage's three-state model:** Generate the Normal state first — it establishes the base mesh and clothing. Brain-Plugged and Recovered are variants applied through texture, shader, and minor mesh adjustments (posture, weight loss, vein patterns). The brain-plugged effects (dark veins, iridescent eyes, oily skin) are primarily shader/texture work. The recovered state requires subtle mesh changes (thinner face, looser clothing fit) plus residual vein traces.
- **Brain-plugged human visual effects:** Dark veins, iridescent eyes, and oily skin sheen are consistent across all five victims but vary in severity based on implantation duration. Generate each victim's Normal state first, then apply the brain-plugged transformation as a texture/shader variant. Henry Cowell (longest implantation) shows the most pronounced effects; Cribbage (shortest) shows the least.
- **Civilian characters** (Arthur Hartley, James Machen) have a single state — no degradation arc. Generate as-is.
- **Family resemblance:** Arthur Hartley and Theodore share facial structure (narrow face, pointed chin, freckles, sandy-brown hair, hazel eyes). Generate with consistent proportions to establish the father-son connection.
- **The brain-plugged humans are human-scale characters,** not fairy-scale. They are full-sized Victorian adults. Do not apply the fairy-scale proportions to these characters.
