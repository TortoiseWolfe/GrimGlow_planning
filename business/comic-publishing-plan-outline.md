# Comic Publishing — Business Plan Outline

**Status:** Outline v1, 2026-11-25. Owner: Jonathan Pohlner (ScriptHammer).
**Scope:** Publishing and business plan for the serialized comic (working title
"GrimGlow" — rename pending, see Open Items). Story canon lives in this repo;
this outline covers the publishing business only.

## The property

- A serialized sci-fi comic: a four-inch fairy squad from the far future,
  stranded in steampunk London. Twelve issues scripted.
- Part of one shared universe with the ScriptHammer game and the robot band —
  each promotes the others.
- Production method: AI-generated character models (Meshy), sets built and
  rendered in Blender, pages assembled and lettered by hand. The process is
  documented (.blend files, drafts, blueprints) — it is both the workflow and
  the rights position: human selection, arrangement, and composition carry
  the copyright (cf. US Copyright Office, *Zarya of the Dawn*).

## Home base and URL structure — DECIDED 2026-11-25

Both paths, not either/or:

- `scripthammer.com/comics/` — the library: this series plus future
  storylines and other comics.
- `scripthammer.com/comics/<series-slug>/` — this series' home under the
  library.
- `scripthammer.com/<series-slug>` — a direct link that redirects to the
  series page, for sharing and print.

The home site is canonical: every mirror points back to it. It is the only
shelf no platform can delist.

## Syndication map (research: 2026-11-25 platform policy review)

**Launch mirrors (AI-made art accepted, non-exclusive):**

| Channel | Terms that matter |
|---|---|
| Own site | Canonical home; RSS feed; mailing-list capture |
| WEBTOON Canvas | No AI clause in Canvas terms; licence expressly non-exclusive; vertical scroll only; ad revenue $0 until 1,000 subs + 40,000 monthly page views — a reach play |
| Substack | No AI ban; paid subscriptions from day 1 (10% + Stripe); exportable list |
| itch.io | AI allowed with the AI Disclosure tag (strictly enforced for comics since Nov 2026); pay-what-you-want PDFs double as tipping |

**Conditional (clear before uploading):**

- **GlobalComix** — best page-format platform; pays from the first reader.
  Policy bans visuals "made fully via Gen AI prompts" but allows AI as one
  tool among many. Our pages are human-composed Blender renders — the route
  in is a pre-clearance email to their content team with the process
  breakdown (script → Meshy models → Blender posing/lighting/render →
  manual assembly/lettering). Keep their reply on file.
- **VoyceMe** — AI-native and non-exclusive, but its terms address AI made
  with its own tools; confirm an externally produced series by email first.

**Collected volumes:**

- **Amazon KDP** — print + fixed-layout ebook once an arc is complete.
  AI-generated content disclosure required at upload. **Never enroll in
  KDP Select** (90-day Kindle exclusivity, includes your own site).

**Do not build on (AI bans / dead):** Tapas (AI banned; service ends
2027-03-31), ComicFury (genAI banned even in part), The Duck (removal
reserved for mostly-genAI comics), Inkverse (genAI as primary means banned),
DriveThruComics (AI-assisted comics banned), Dashtoon (studio shut
2026-08-15).

**Exclusivity traps — decline by default:** WEBTOON Originals (exclusive
worldwide digital rights), KDP Select, NamiComi Creator Rewards
(monetization must be exclusive). Posting is non-exclusive everywhere;
exclusivity hides in the paid tiers.

## Format playbook

- One high-resolution master per page → two cuts:
  - **Page cut** — home site, GlobalComix, KDP volumes.
  - **Vertical cut** — WEBTOON Canvas, VoyceMe.
- Lettering standard (set 2026-11-25): speech balloons colour-coded per
  character (warm, faded suit colour, ~50% transparent fill, solid text);
  narration white/translucent; per-character fonts a later refinement.

## Discovery

1. **Short video first** — TikTok → Instagram Reels / YouTube Shorts: panel
   slideshows with narration plus process clips (model-to-render timelapses,
   set fly-throughs). The only documented from-zero viral engine. Measure
   conversion to readers, not views.
2. **Directories (submit once, passive)** — TopWebComics (voting; ads from
   $1/day), Belfry, Piperka, Comic Rocket. All fed by the home site's RSS.
3. **Reddit** — r/comics bans AI outright; episodes do not go there. Process
   posts in maker communities (r/Blender etc.) only, always honestly framed.
4. Bluesky + creator cross-promotion.

## Monetization stack (year one: expect ~$0 from platform ads)

Audience (Canvas + short video) → owned list (site + Substack) → fan money
(Patreon/Ko-fi early access and process posts; itch.io pay-what-you-want) →
collected editions (KDP print on demand). GlobalComix is the exception that
pays from reader #1, if cleared.

## Production pipeline (the moat)

Scripts (12 issues) → character models (Meshy, rigged) → Blender sets built
from drawn blueprints (ship interior; crash-site gutter; London locations by
issue order) → shot-library panel renders (one Blender file per page, one
scene per panel, cameras per the script's shot directions) → lettering →
two format cuts → publish home first, mirrors same day.

## Open items / gates

1. **Series rename** — "GrimGlow" is saturated (author platform, merch,
   games). Blocks: series slug, the direct-link path, handles, domain and
   trademark checks on the final pick. Direction pick is Jonathan's.
2. **Meshy commercial licence** — verify the commercial-use rights for
   generated models on the current plan tier BEFORE launch; GlobalComix and
   KDP both require full rights to AI outputs. (Same check owed for the LCA
   stage-set resale.)
3. **GlobalComix pre-clearance email** — draft from the pipeline section
   above; send before any upload.
4. **VoyceMe confirmation email** — externally produced series.
5. **Cadence** — pages per week, set once page production time is measured
   (page 1 shot library is the timing baseline).
6. **Home-site build** — the /comics/ library and series pages on
   scripthammer.com, RSS, list capture.

## Repo map

- **Planning + business:** this repo (GrimGlow_planning) — canon, scripts,
  business outlines.
- **Production:** grimglow-unity (game), game-art-assets (binary art, LFS).
