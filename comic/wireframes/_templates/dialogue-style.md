# Dialogue Balloon Style Spec — GrimGlow Comic Panels

Canonical style for every speech balloon, caption, and SFX in the comic. Apply uniformly across all panels.

## Why this exists

Previous panels had:
- Translucent fills (`opacity="0.92"`) so panel art bled through and made text muddy
- 1px borders that disappeared against busy backgrounds
- 10.5pt body text — too small to read at panel display size
- Balloons placed over the speaker's face
- Three balloons stacked vertically eating an entire CU panel

This spec fixes all of those.

## Speech balloons (character dialogue)

```svg
<!-- Drop-shadow filter (define once in <defs>): -->
<filter id="balloonShadow" x="-10%" y="-10%" width="120%" height="120%">
  <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#000" flood-opacity="0.45"/>
</filter>

<!-- Balloon body: -->
<rect x="X" y="Y" width="W" height="H" rx="8"
      fill="#ffffff" stroke="#<SUIT_COLOR>" stroke-width="2"
      filter="url(#balloonShadow)"/>

<!-- Speaker name: -->
<text x="X+10" y="Y+22"
      font-family="Helvetica Neue, Arial, sans-serif"
      font-size="14" font-weight="800"
      fill="#<SUIT_COLOR>"
      letter-spacing="0.3">SPEAKER</text>

<!-- Body text: -->
<text x="X+10" y="Y+40"
      font-family="Helvetica Neue, Arial, sans-serif"
      font-size="13" font-weight="500"
      fill="#1a1a1a">Dialogue line here.</text>

<!-- Tail (pointing toward speaker, NOT covering them): -->
<path d="M tail-base-x,Y+H L tail-base-x+10,Y+H L tail-tip-x,Y+H+12 Z"
      fill="#ffffff" stroke="#<SUIT_COLOR>" stroke-width="2"
      stroke-linejoin="round"/>
<!-- White overlay to hide the border segment that crosses into the balloon body: -->
<line x1="tail-base-x" y1="Y+H" x2="tail-base-x+10" y2="Y+H"
      stroke="#ffffff" stroke-width="3"/>
```

### Speaker color reference

| Character | Border / name fill |
|-----------|--------------------|
| Sable     | `#5a606a` (silver/grey) |
| Wren      | `#c87a35` (copper) |
| Jink      | `#2ed078` (emerald) |
| Thresh    | `#dc2030` (crimson) |
| Luma      | `#5a3ad8` (sapphire-violet) |
| Theodore  | `#6a4220` (warm brown) |
| SFX       | `#1a1a1a` (black) |
| Caption   | `#5a4a30` (parchment ink) |

### Sizing rules

- Min balloon width: **enough to fit longest line at 13pt without wrapping unless intentional**.
- Min balloon height: 30px for one-line, +18px per additional wrapped line, +20px for the speaker label row.
- Padding: 10px left/right, 14px top, 10px bottom.

## Off-panel speech (`(O.P.)`)

Same as a regular balloon but:
- `stroke-dasharray="4,3"` on the balloon outline.
- Speaker label suffix: `SPEAKER (O.P.)`.
- No tail.

## Caption / narration boxes

```svg
<rect x="X" y="Y" width="W" height="H" rx="2"
      fill="#f5ecd8" stroke="#c8b898" stroke-width="1.5"
      filter="url(#balloonShadow)"/>
<text x="X+10" y="Y+22"
      font-family="Helvetica Neue, Arial, sans-serif"
      font-size="13" font-weight="700" font-style="italic"
      fill="#5a4a30"
      letter-spacing="0.3">CAPTION</text>
<text x="X+10" y="Y+40"
      font-family="Helvetica Neue, Arial, sans-serif"
      font-size="13" font-style="italic"
      fill="#5a4a30">Narration text.</text>
```

## SFX (sound effects: KRAAANG, CHUNK, etc.)

```svg
<!-- Stroke first (creates the outline), fill on top for the inner color -->
<text x="X" y="Y" font-family="Impact, sans-serif"
      font-size="64" font-weight="900"
      stroke="#1a0408" stroke-width="4" stroke-linejoin="round"
      paint-order="stroke fill"
      fill="#ffe080"
      transform="rotate(-8 X Y)">KRAAANG</text>
```

- Always at least 32pt — bigger for impact moments (KRAAANG = 64pt).
- Bright fill (yellow / red / white) over thick dark stroke.
- Slight rotation (5–15°) for energy. Never axis-aligned.

## Placement rules (inviolable)

1. **NEVER overlap a speaker's face.** Place balloons in the panel's empty quadrant. If three balloons are needed in a tight CU, redesign the panel composition — don't pile them on top of the character.
2. **Tail points TO the speaker but does not cross them.** If the speaker's mouth is at top-right of a panel and the balloon is at top-left, the tail emerges from the balloon's right edge and angles toward the speaker — but stops at the panel midline.
3. **Reading order: top-left → bottom-right.** Place balloons so the eye picks them up in dialogue order.
4. **Maximum 2 balloons per panel for ECU/CU shots.** For exchanges with 3+ lines (e.g. Luma's "data is extraordinary..." → Sable cuts off → Luma "...right.") split across two panels OR use the negative space at panel corners with smaller balloons.
5. **Balloons stay inside the panel border.** No bleed-out.
6. **No balloon larger than 40% of the panel area.** If text is too long, edit the dialogue or split the panel.

## Testing checklist (per panel)

Before marking a panel done:

- [ ] All balloons opaque white, no background bleeding through?
- [ ] All borders ≥2px in the speaker's department color?
- [ ] All body text ≥13pt, all speaker labels ≥14pt and bold?
- [ ] Drop shadow under each balloon?
- [ ] No balloon covers any speaker's face?
- [ ] Tails point at the right person and don't lie over them?
- [ ] At normal display size (panel rendered at native viewBox), text is comfortably readable?
