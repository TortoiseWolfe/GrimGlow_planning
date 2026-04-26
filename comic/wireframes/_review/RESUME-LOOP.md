# Resume `/loop` prompt for the GrimGlow comic wireframe quality pass

Paste the block below verbatim as the **first message** of a new Claude Code
session in this repo. `/loop` will detect there's no time interval and
self-pace — picking up exactly where the previous session left off.

Last commit on `main` when this prompt was written: **`2bccf14`**
Live preview: **https://tortoisewolfe.github.io/GrimGlow_planning/**

---

```
/loop Resume the GrimGlow comic wireframe quality pass. State as of last commit (2bccf14): Pages 1-2 of Issue 1 have all dialogue boxes meeting the dialogue-style.md spec (opaque white, 13pt body / 14pt speaker, 2px speaker-color border, drop shadow, no face overlap). Character templates in comic/wireframes/_templates/ have new hair geometry (Sable buzz, Wren high bun, Jink curls, Thresh swept pomp, Luma thick braid, Theodore tousled spikes), but only P01P02 has had its inline panel hair propagated — P01P03 through P02P05 still ship the old smooth-dome hair. Page 3 panels 1-5 exist but pre-date the dialogue style spec and the hair rewrite. Live preview deploys to https://tortoisewolfe.github.io/GrimGlow_planning/ via .github/workflows/pages.yml on every push to main. Local viewer at http://localhost:3001/. Verification pipeline: mcp/playwright via .mcp.json renders panels at native viewBox to /screenshots/ for self-critique. Use _review/view.html?s=<path> to render any SVG with external <image> refs resolved.

Pending tasks (priority order). Self-pace, one panel per iteration:

1. Inline-propagate the new hair geometry to the 10 P1+P2 panels that still use old hair (#42 in the task list at task continuation). For each panel: locate the inline hair <path>/<g>, replace with the corresponding template's new geometry translated to the panel's head center coordinates. Screenshot via http://localhost:3001/_review/view.html?s=_panels/Issue01_Descent/<file>, verify hair reads correctly per character (Sable buzz NOT a dome, Wren high knot NOT a flat helmet, Jink curl clumps NOT a beehive, Thresh tall swept pomp, Luma thick rope braid, Theodore spikes), then commit.

2. Apply the same dialogue-style.md sweep to Page 3 panels 1-5 (#33 was Page 1+2 only): opaque white, 13/14pt, 2px border in speaker department color, drop shadow, no face overlap, max 2 balloons per CU/MCU. Screenshot each.

3. Apply hair propagation to Page 3 panels 1-5.

4. Redraw Page 3 Panel 6 (ECU Wren's hand on emergency toggle, the deferred panel from earlier) using the new hair templates and dialogue style.

5. Recompose comic/wireframes/Issue01_Descent/page03.svg with all 6 Page 3 panels in their layout grid (full-width 742×364 at (29,59); three 241×364 at y=433 spaced (29, 280, 530); two 366×364 at y=807 spaced (29, 405)). Use xlink:href="_panels/Issue01_Descent/page03_panelNN.svg" — drop the leading ../, the viewer's inlinePanelImages function in index.html resolves relative to doc base.

6. Worst-art-staging redraws (the failure modes from REVIEW.md): P02P02 (Jink's hand currently reads as a teapot — needs anatomical hand with knuckles/fingers/knee plate), P02P01 (squad members read as stick figures — proportions and recognizability), P01P03 (no console visible, add the copper-gold holographic display), P01P05 (archway with corridor depth, Thresh in 3/4 back view).

For every panel touched: screenshot via mcp__playwright__browser_navigate to the _review URL + browser_take_screenshot to /screenshots/, read it back, compare to the script spec at comic/scripts/Issue01_Descent_Script.md and the quality bar at comic/wireframes/_templates/quality-bar.md. Don't claim a panel done without the verification screenshot.

Commit batches of 1-3 related fixes with descriptive messages so the GitHub Pages deploy gives the user incremental visible progress. Push to main; the .github/workflows/pages.yml workflow auto-deploys.

Stop and ask the user if: a screenshot reveals a regression you can't fix in 2 retries, scope feels larger than expected, or you hit context budget. Otherwise self-pace dynamically — fast panels (small balloons, simple hair swap) every ~5-10 min, complex redraws (P02P01, P02P02) every ~20-30 min. End when all 6 priorities above are done OR the user signals stop.
```

---

## Companion docs the loop reads

- `comic/wireframes/_templates/dialogue-style.md` — balloon spec checklist.
- `comic/wireframes/_templates/quality-bar.md` — per-panel done-criteria.
- `comic/wireframes/_panels/Issue01_Descent/REVIEW.md` — visual QA findings
  with severity ratings; loop priority 6 redraws come from here.
- `comic/scripts/Issue01_Descent_Script.md` — per-panel Shot/Camera/Action/
  Expression/Lighting/painterly-prompt source of truth.
- `comic/wireframes/_templates/{sable,wren,jink,thresh,luma,theodore}.svg` —
  new hair geometry to propagate; head center is at `cx=200, cy=180` in the
  templates and varies per panel.

## Environment expectations the loop assumes

- Local viewer container `wireframes-viewer-1` healthy on `localhost:3001`
  (Docker Desktop running).
- Playwright MCP server connected (`claude mcp list` shows `playwright ✓`).
  If not, the `.mcp.json` config is correct — restart Claude Code so the
  MCP server is spawned fresh.
- Git remote `origin` set to GitHub repo with the `pages.yml` workflow.

## Update this file after each loop run

When the loop completes (or pauses), bump:
- The "last commit" SHA at the top.
- The pending tasks block — strike done, add anything new the loop discovered.
