# GrimGlow — Planning & Design Bible

A squad of four-inch-tall soldiers from the far future crash-lands in a steampunk Victorian world. Their holographic tech reads as fairy magic. Their enormous enemies read as monsters. They accidentally become the origin of fairy tales.

This repository is the **design bible** — narrative, character, and visual design documents that drive all downstream production (comic series, Three.js browser prologue, Unity PC game). No code lives here.

**What exists:** Story Bible, Product Design Requirements, Two-Phase Development Plan, 12-issue comic outline with script prompts, character references, concept art.

**What this guide helps you create:** World wiki pages, deep character profiles, a prose style guide, comic scripts, dialogue trees, and revision-tested prose — all using [creative-writing-skills](https://github.com/haowjy/creative-writing-skills) inside Claude Code.

---

## Repository Map

```
docs/
  GrimGlow_Story_Bible.md              — Core IP: concept, characters, visual language, three-layer plot
  GrimGlow_Product_Design_Requirements.md — Unity game tech design: AI, scale, stealth/combat, rendering
  GrimGlow_Two_Phase_Development_Plan.md  — Phase 1 Three.js browser → Phase 2 Unity PC game
  style-guide.md                       — Prose style guide for consistent narrative voice

characters/
  GrimGlow_Character_Prompts.md        — Painterly art prompts (Sable, Wren, Jink, Thresh, Luma, Theodore)
  GrimGlow_Character_Turnarounds.md    — Meshy.ai 3D model reference sheets
  wiki/                                — Canonical character reference pages (one per character)
  brainstorms/                         — Working brainstorm documents (14 files)

comic/
  GrimGlow_Volume1_Plot_Outline.md     — 12-issue plot outline, three-act structure
  GrimGlow_Volume1_Script_Prompts.md   — Full 22-page script generation prompts per issue
  GrimGlow_Volume1_Issue_Prompts.md    — Cover/key moment art prompts per issue

concept-art/
  Sable/, Wren/, Jink/, Thresh/, Luma/, Theodore/ — Per-character concept art + turnarounds
  reference/                           — Historical reference photos

world-building/
  meshy-environment-prompts.md         — 142 Meshy.ai 3D component prompts (21 sections)
  maps/                                — Booth, Goad, Stanford, LIDAR heightmap data
  reference-photos/                    — Victorian London reference photographs
  brainstorms/                         — Working brainstorm documents (11 files)

CLAUDE.md                              — Project instructions for Claude Code
```

See `CLAUDE.md` for full project context, character tables, visual language rules, and tech stack.

---

## Prerequisites

Install the creative-writing-skills plugin for Claude Code:

```bash
claude plugin marketplace add haowjy/creative-writing-skills
claude plugin install creative-writing-skills@creative-writing-skills
```

The grey-haven creative-writing plugin (for revision pipelines and audits) installs separately if not already present.

---

## Workflow Overview

The creative writing pipeline moves left to right. Each stage has a dedicated skill and slash command.

```
Brainstorm ──→ Document ──→ Style Guide ──→ Write ──→ Critique ──→ Revise ──→ Audit
   /bs           /wiki      style-skill      /write    /critique   /prose-     /writing-
                             -creator                              revision    audit
```

| Stage | Skill | Command | Output |
|-------|-------|---------|--------|
| Brainstorm | `cw-brainstorming` | `/bs` | Working notes (.md) |
| Document | `cw-official-docs` | `/wiki` | Wiki pages (.md) |
| Style Guide | `cw-style-skill-creator` | (invoked directly) | Style skill (.md or .skill) |
| Write | `cw-prose-writing` | `/write [style]` | Scenes, scripts, dialogue |
| Critique | `cw-story-critique` | `/critique` | Feedback report |
| Revise | `creative-writing` | `/prose-revision` | Revised manuscript |
| Audit | `creative-writing` | `/writing-audit` | SVQ scores + issues |

---

## ~~Phase 1: World Building~~ ✓

Use `cw-brainstorming` to explore and capture world rules before committing them to wiki pages. Brainstorming notes stay skeletal — AI suggestions are tagged, nothing is locked in.

**Output:** Brainstorming notes saved to `world-building/` directory.

<details>
<summary>Archived — prompts used in prior sessions</summary>

```
/bs
```

### Victorian London at Fairy Scale

```
Let's brainstorm the fairy-scale geography of Victorian London for GrimGlow.
The squad is four inches tall. I need to work out:
- How they navigate between locations (rooftops, gutters, pipe networks, rat paths)
- What human infrastructure looks like at their scale (a cobblestone is a boulder, a gas lamp is a lighthouse)
- Safe zones vs. danger zones (cats, birds, rat territories, human foot traffic)
- How weather affects them at this scale (rain is a flood, wind is a gale)
Reference docs/GrimGlow_Story_Bible.md for the visual language rules.
```

### Steampunk Technology Rules

```
Let's brainstorm the steampunk technology rules for the Victorian world.
I need consistent logic for:
- What level of tech exists (steam power, clockwork, early electrical, pneumatic tubes)
- How Wren interacts with it (what she finds ingenious vs. primitive)
- What components the squad needs to scavenge and where they'd find them
- How human tech contrasts with fairy tech visually (brass/copper vs. holographic geometry)
Reference the component list from comic/GrimGlow_Volume1_Plot_Outline.md.
```

### Titan Biology and Culture

```
Let's brainstorm Titan biology and culture for GrimGlow.
The Story Bible says they use oil-on-water iridescent cloaking and brain-plug humans as foot soldiers.
I need to explore:
- Their physiology (how big are they relative to humans? how do they move?)
- Their cloaking mechanics (not invisibility but "wrongness" — what does that mean in practice?)
- Their motivation at the convergence point (steering the industrial revolution — why? toward what?)
- Their relationship to the squad's fairy tech (dark mirror — what's the connection?)
- How they communicate and organize
```

### Temporal Mechanics

```
Let's brainstorm the temporal mechanics — the paradox layer of the plot.
The squad IS the convergence point. Their presence creates the fairy tales that inspired the future
that sent them back. I need to work out:
- The causal loop: what exactly feeds back? (stories? tech artifacts? genetic material?)
- What Luma discovers and when (she sees the paradox first)
- The rules: can they change things? or is the loop closed?
- What "STAY" means in the context of the cache from prior operatives
- How this resolves in Issue 12 without feeling like a cop-out
Reference the three-layer plot in docs/GrimGlow_Story_Bible.md.
```

</details>

---

## ~~Phase 2: Character Development~~ ✓

Brainstormed backstories and voice, then formalized into wiki-style profiles for all six main characters.

**Output:** Brainstorm notes in `characters/brainstorms/brainstorm-*.md`; wiki pages in `characters/wiki/` (sable, wren, jink, thresh, luma, theodore).

<details>
<summary>Archived — brainstorm prompts used in prior sessions</summary>

```
/bs
```

```
Let's brainstorm Sable's backstory and internal life for GrimGlow.
She's the captain — dark brown skin, silver-white cropped hair, carries authority like weight.
I need to explore:
- Her military career before this mission (what shaped her command style?)
- The hidden mission file — what does she know that the squad doesn't?
- How she relates to each squad member individually
- Her arc: "command without a chain of command" — what does she lose? what does she find?
- Her voice: how does she talk? short sentences? formal? when does the mask slip?
Reference characters/GrimGlow_Character_Prompts.md and comic/GrimGlow_Volume1_Plot_Outline.md.
```

Repeat for each character, adjusting the focus:

```
Let's brainstorm Wren's relationship with Victorian technology.
She's the engineer — East Asian, messy hair knot, oil-stained.
Her arc is "growing admiration for primitive human ingenuity."
- What specific inventions fascinate her? (clockwork? steam pressure? lenscraft?)
- When does admiration become dangerous? (tempted to help, violating mission protocol?)
- How does her engineering mind process the paradox when it's revealed?
- Her voice: technical vocabulary? dry humor? talks to machines?
```

```
Let's brainstorm Jink's recklessness and what it costs.
They're the scout — youngest, androgynous, wild curly hair, fastest flyer.
Their arc is "learning actions in the past have weight."
- Why the recklessness? (youth? invincibility? never faced real consequences before?)
- Breaking protocol with Theodore — impulse? loneliness? curiosity? all three?
- What does "actions have weight" mean for someone who's never had permanence?
- Their relationship with the squad (the kid everyone protects and everyone is frustrated by)
- Their voice: fast, casual, quips when it's not appropriate — but when do they go quiet?
```

```
Let's brainstorm Theodore's inner world and what "something better" means.
He's the human ally — 12-13, tinker's apprentice, sandy-brown hair, clever hands.
His arc is "wants fairies to be magical; learns they're something better."
- His life before the fairies (alone? overlooked? what does Cribbage's workshop mean to him?)
- What does he think fairies ARE when he first meets Jink? What story is he telling himself?
- The disillusionment: when does he realize they're soldiers, not magical beings?
- What "something better" means — what replaces the fairy tale in his mind?
- His voice: Victorian earnest, formal, tinker's vocabulary — but how does he talk to Jink vs. Sable?
```

```
Let's brainstorm the Jink-Theodore relationship as a cross-reference.
Jink is the reckless scout who makes unauthorized first contact.
Theodore is the tinker's apprentice who wants fairies to be magical.
- How does their bond evolve across 12 issues?
- What does each offer the other that no one else can?
- Their voice contrast: Jink is fast/casual, Theodore is earnest/Victorian
- The moment Theodore learns they're soldiers, not fairies — how does Jink handle that?
```

```
Let's brainstorm Thresh's fear arc.
He's the soldier — broad, copper-red buzz cut, heavy armor.
"Brave in the future, terrified in the past — fights afraid."
- What specifically terrifies him? (the scale? the primitiveness? something personal?)
- How does fear manifest physically? (shaking hands? over-checking corners? snapping at Jink?)
- The transformation: not fearless, but "trained action despite fear"
- His relationship with Sable (does he resent her calm? depend on it?)
- His voice: blunt, military shorthand, but the fear leaks through in word choice
```

```
Let's brainstorm Luma's temptation to stay.
She's the medic/scientist — South Asian, holographic lenses, braided hair.
She sees the paradox first and is most tempted to remain in the past.
- What draws her? (the botany? the slower pace? the chance to study history firsthand?)
- When does she realize the causal loop? What evidence accumulates?
- The ethical weight: if they're the origin of fairy tales, leaving might erase the future
- Her voice: precise, observational, asks questions that sound casual but aren't
```

</details>

<details>
<summary>Archived — wiki page prompts used in prior sessions</summary>

```
/wiki
```

```
Create a canonical character profile for Captain Sable.
Sources: characters/GrimGlow_Character_Prompts.md, docs/GrimGlow_Story_Bible.md,
comic/GrimGlow_Volume1_Plot_Outline.md, and the brainstorming notes in world-building/.
Include: full name/rank, physical description, personality, backstory, relationships,
arc summary, voice notes, and key moments across the 12-issue run.
Save to characters/wiki/sable.md.
```

```
/wiki
```

```
Create a canonical character profile for Wren, the squad's engineer.
Sources: characters/GrimGlow_Character_Prompts.md, docs/GrimGlow_Story_Bible.md,
comic/GrimGlow_Volume1_Plot_Outline.md, and the brainstorming notes in world-building/.
Include: full name/rank, physical description, personality, backstory, relationships,
arc summary ("growing admiration for primitive human ingenuity"), voice notes
(technical vocabulary, dry humor, talks to machines), and key moments:
the clockwork cathedral in Issue 5, the lighthouse lens swap in Issue 7,
the feedback pulse against the Titan in Issue 10, and the disarm walkthrough
she gives Theodore in Issue 12.
Save to characters/wiki/wren.md.
```

```
/wiki
```

```
Create a canonical character profile for Jink, the squad's scout.
Sources: characters/GrimGlow_Character_Prompts.md, docs/GrimGlow_Story_Bible.md,
comic/GrimGlow_Volume1_Plot_Outline.md, and the brainstorming notes in world-building/.
Include: full name/rank, physical description (androgynous, wild curly hair, uses they/them),
personality, backstory, relationships (especially the bond with Theodore),
arc summary ("learning actions in the past have weight"), voice notes
(fast, casual, irreverent — but serious when it counts), and key moments:
unauthorized first contact in Issue 3, exhilaration vs. squad tension in Issues 2 and 5,
the Titan sighting from the lighthouse in Issue 7, fury at Sable's lie in Issue 9,
and the rooftop conversation with Theodore in Issue 11.
Save to characters/wiki/jink.md.
```

```
/wiki
```

```
Create a canonical character profile for Thresh, the squad's soldier.
Sources: characters/GrimGlow_Character_Prompts.md, docs/GrimGlow_Story_Bible.md,
comic/GrimGlow_Volume1_Plot_Outline.md, and the brainstorming notes in world-building/.
Include: full name/rank, physical description (broad, copper-red buzz cut, heavy armor),
personality, backstory, relationships (especially with Sable),
arc summary ("brave in the future, terrified in the past — fights afraid"),
voice notes (blunt, military shorthand, fear leaks through in silence and word choice),
and key moments: confident competence in the Issue 1 future opening,
fear surfacing during the cat encounter in Issue 2, exposed overwatch in Issue 5,
the boot near-miss in Issue 7, the encounter with the gentle child in Issue 8,
and the breakthrough combat against the Titan in Issue 10 — afraid and fighting anyway.
Save to characters/wiki/thresh.md.
```

```
/wiki
```

```
Create a canonical character profile for Luma, the squad's medic and scientist.
Sources: characters/GrimGlow_Character_Prompts.md, docs/GrimGlow_Story_Bible.md,
comic/GrimGlow_Volume1_Plot_Outline.md, and the brainstorming notes in world-building/.
Include: full name/rank, physical description (South Asian, braided hair with luminous filament,
holographic lenses), personality, backstory, relationships (especially the investigation
partnership with Theodore), arc summary ("sees the paradox first; most tempted to stay"),
voice notes (precise, observational, asks questions that sound casual but aren't),
and key moments: the fairy glyph discovery in Issue 4, Titan traces and waistcoat-pocket
investigation in Issue 6, the church cache and "STAY" in Issue 8,
connecting the dots for the squad in Issues 9 and 11, and delivering the full
paradox revelation in Issue 12 — the convergence point is the stories humanity tells.
Save to characters/wiki/luma.md.
```

```
/wiki
```

```
Create a canonical character profile for Theodore Edmund Hartley, the human ally.
Sources: characters/GrimGlow_Character_Prompts.md, docs/GrimGlow_Story_Bible.md,
comic/GrimGlow_Volume1_Plot_Outline.md, and the brainstorming notes in world-building/.
Include: full name, age (12-13), physical description (sandy-brown hair, hazel eyes,
oil-stained clever hands, brass gear ring, worn waistcoat), personality, backstory
(apprentice to Mr. Cribbage, alone, resourceful, overlooked), relationships
(especially the bond with Jink, the investigation partnership with Luma,
and the complicated trust with Sable), arc summary ("wants fairies to be magical;
learns they're something better"), voice notes (period-appropriate Victorian English,
earnest, formal, tinker's vocabulary), and key moments: glimpsing the falling star
in Issue 1, finding the shard and meeting Jink in Issue 3, the charging cradle
demonstration in Issue 4, the terrible-liar diversion in Issue 5, guiding Luma
through old streets in Issues 6 and 8, the rooftop conversation with Jink in Issue 11,
and disarming the final Titan device with clockwork hands in Issue 12 —
then writing the first fairy tale alone by candlelight.
Save to characters/wiki/theodore.md.
```

</details>

---

## ~~Phase 3: Style Guide Creation~~ ✓

Created a GrimGlow prose style guide using `cw-style-skill-creator`. The guide covers prose texture, dual lighting, scale contrast, degradation arc, fairy tech, Titan description, and all six character voices.

**Output:** `docs/style-guide.md` at repo root.

<details>
<summary>Archived — prompt used in prior session</summary>

```
Use the cw-style-skill-creator skill to create a GrimGlow prose style guide.

Analyze these source documents for tone, voice, imagery patterns, and visual language:
- docs/GrimGlow_Story_Bible.md (especially the Visual Language Rules section)
- characters/GrimGlow_Character_Prompts.md
- comic/GrimGlow_Volume1_Plot_Outline.md
- comic/GrimGlow_Volume1_Issue_Prompts.md

The style should capture:
- Painterly, textured prose — oil paint feeling, visible brushwork in word choice
- Dual lighting in every scene description (warm amber gaslight vs. cool blue-white holographic)
- Scale contrast as a constant presence (human objects described from fairy perspective)
- Degradation arc language (pristine → soot-streaked → light bleeding through grime)
- Titan descriptions using wrongness/discomfort, not standard monster language
- Character voice distinctions (Sable: clipped authority, Wren: technical precision,
  Jink: fast/reckless, Thresh: military bluntness masking fear, Luma: precise observation,
  Theodore: Victorian earnestness)

Output as a style guide markdown file at docs/style-guide.md.
```

</details>

---

## Phase 4: Prose Writing

With world-building documented and a style guide in place, write actual content.

```
/write grimglow
```

### Comic Script — Issue 1

```
Write the full 22-page comic script for GrimGlow Issue 1: "Descent."
Follow the script generation prompt in comic/GrimGlow_Volume1_Script_Prompts.md (Issue 1 section).
Reference:
- docs/GrimGlow_Story_Bible.md for visual language and character voices
- comic/GrimGlow_Volume1_Plot_Outline.md for plot beats
- characters/GrimGlow_Character_Prompts.md for visual descriptions
- docs/style-guide.md for prose style

Page budget:
- Pages 1-4: Future spaceship, routine mission, ambush, temporal corridor collapse
- Pages 5-6: The fall from human perspective, witnesses, falling star
- Pages 7-14: Crash wreckage, scale revelation, squad dynamics, component needs
- Pages 15-20: First night, survival, fear vs. wonder, character moments
- Pages 21-22: Sable alone with hidden file, final vista of the enormous city

Format as a comic script with panel descriptions, dialogue, and caption text.
Save to comic/scripts/issue-01-descent.md.
```

### Phase 1 Dialogue — Theodore's Discovery

```
Write the dialogue tree for Theodore's first encounter with Jink in Ink format.
This covers Issue 3 of the comic / the climactic scene of the Phase 1 browser prologue.

Context: Theodore is working alone in his master's workshop at night. He notices
impossible light coming from under a brass gear housing. He investigates and finds Jink,
who freezes mid-flight.

Branching points:
- Theodore's reaction: wonder vs. fear vs. practical curiosity
- Whether Jink tries to flee or stays
- How much Jink reveals (nothing / half-truths / the truth)
- Whether Theodore offers to help or demands answers

Each branch should feel true to both characters:
- Theodore: Victorian speech patterns, tinker's vocabulary, earnest
- Jink: fast-talking, deflective humor, slang from the future that confuses Theodore

Reference the Ink scripting format. Save to dialogue/theodore-discovery.ink.
```

### Comic Script — Subsequent Issues

```
Write the full 22-page comic script for GrimGlow Issue 2: "Small World."
Follow the script generation prompt in comic/GrimGlow_Volume1_Script_Prompts.md (Issue 2 section).
Use the same reference documents as Issue 1.
Focus on: scale as survival horror, the component list emerging, squad friction.
Save to comic/scripts/issue-02-small-world.md.
```

Continue this pattern for Issues 3-12, adjusting the prompt to reference each issue's specific section in the Script Prompts and Plot Outline.

---

## Phase 5: Story Critique

After writing a draft, get structured feedback.

```
/critique
```

```
Critique the Issue 1 script at comic/scripts/issue-01-descent.md.

Evaluate against:
- Character voice consistency (does each squad member sound distinct?)
- Scale language (is the fairy-scale perspective maintained throughout?)
- Visual language compliance (dual lighting, holographic geometry, degradation arc)
- Pacing across 22 pages (does the crash land at the right beat? is the first night earned?)
- Emotional arc (does it move from routine → catastrophe → awe?)
- Setup for Issue 2 (are the right threads planted?)

Reference docs/GrimGlow_Story_Bible.md for the canonical rules.
Flag any contradictions with the Plot Outline.
```

---

## Phase 6: Revision & Polish

For longer prose or scripts that need systematic improvement, use the 6-phase prose revision pipeline.

```
/prose-revision
```

```
Run the prose revision pipeline on comic/scripts/issue-01-descent.md.
This is a comic script for a painterly, textured IP.
Priority areas: dialogue voice distinction, visual description density,
and consistency with the GrimGlow style guide at docs/style-guide.md.
```

The pipeline runs six phases automatically:
1. Surface cleanup (grammar, clarity)
2. Prose craft (sentence rhythm, word choice)
3. SVQ polish (style, voice, quality scoring)
4. Sentence architecture (structural revision)
5. Enrichment (sensory detail, subtext)
6. Final audit (consistency check)

---

## Phase 7: Manuscript Audit

For a comprehensive quality assessment with scoring:

```
/writing-audit
```

```
Audit the GrimGlow Issue 1 script at comic/scripts/issue-01-descent.md.
Check for:
- Believability (do the steampunk world rules hold? does the tech feel consistent?)
- Internal consistency (character knowledge, timeline, object permanence)
- World rule compliance (visual language, scale physics, fairy tech behavior)
- Prose quality (SVQ scoring)

Reference docs/GrimGlow_Story_Bible.md as the canonical source of truth.
```

Acceptance thresholds: SVQ >= 7.0 and Believability >= 80 to pass.

---

## Production Pipelines (Quick Reference)

For larger-scale content production, the grey-haven creative-writing plugin offers heavier pipelines:

| Pipeline | Command | Use Case |
|----------|---------|----------|
| Novel Development | `/writing-team` | Full pre-production: research, foundation, structure, dialogue, integration |
| Content Production | `/content-team` | Non-fiction: lore articles, marketing copy, dev blog posts |
| Multi-Reviewer | `/writing-review` | Synthesize feedback from parallel review agents |
| Manuscript Audit | `/writing-audit` | SVQ + believability scoring with accept/revise/rework thresholds |
| Prose Revision | `/prose-revision` | 6-phase systematic manuscript revision |

### Novel Development Pipeline

```
/writing-team
```

```
Develop the GrimGlow novelization of Volume 1 (Issues 1-12).
Source material: comic/GrimGlow_Volume1_Plot_Outline.md
Character references: characters/GrimGlow_Character_Prompts.md
World rules: docs/GrimGlow_Story_Bible.md
Style: docs/style-guide.md
```

---

## Quick Reference Card

| Task | Command | Example Prompt |
|------|---------|----------------|
| Explore world rules | `/bs` | `"Let's brainstorm how gas lamps work at fairy scale"` |
| Deepen a character | `/bs` | `"Let's brainstorm Thresh's backstory before the crash"` |
| Create wiki page | `/wiki` | `"Create a canonical profile for Luma"` |
| Build style guide | (direct) | `"Use cw-style-skill-creator to analyze the Story Bible"` |
| Write a scene | `/write` | `"Write the Issue 3 workshop discovery scene"` |
| Get feedback | `/critique` | `"Critique this script for voice consistency"` |
| Revise prose | `/prose-revision` | `"Run revision pipeline on issue-01-descent.md"` |
| Audit manuscript | `/writing-audit` | `"Audit Issue 1 for believability and world consistency"` |
| Full novel dev | `/writing-team` | `"Develop the Volume 1 novelization"` |
| Marketing content | `/content-team` | `"Write a dev blog post about the GrimGlow art pipeline"` |

---

## Content Roadmap

Prioritized checklist of content to develop:

- [x] **Character profiles (main six)** — Wiki pages for Sable, Wren, Jink, Thresh, Luma, Theodore (`characters/wiki/`)
- [x] **GrimGlow style guide** — Prose style skill derived from Story Bible visual language (`docs/style-guide.md`)
- [ ] **Secondary character profiles** — See tier list below
- [ ] **World wiki pages** — Locations (London at fairy scale, the wreckage, Theodore's workshop), tech systems (fairy tech rules, steampunk tech rules), faction lore (Titans, prior operatives)
- [ ] **Comic Issue 1 script** — Full 22-page script; test the entire pipeline end-to-end
- [ ] **Phase 1 dialogue trees** — Ink scripts for the browser prologue (squad conversations, Theodore discovery)
- [ ] **Comic Issues 2-12 scripts** — Remaining 11 issues, one at a time through the write/critique/revise cycle
- [ ] **NPC system prompts** — Ollama personality prompts for Phase 2 (Theodore 7B, ambient NPCs 3B)
- [ ] **Lore articles** — In-world documents (Theodore's journal entries, squad mission logs, Titan field reports)

### Secondary Characters — Not Yet Covered

Characters identified across brainstorm files, Plot Outline, and Script Prompts that do not yet have wiki pages or dedicated profiles.

**Tier 1 — Named characters with on-page arcs (need wiki pages)**

| Character | Role | States | Key Sources |
|-----------|------|--------|-------------|
| **Mr. Cribbage** | Theodore's clockmaker master; dismissive, competent, unkind | Normal → brain-plugged → recovered-but-diminished | `brainstorm-ogre-origin.md`, `brainstorm-theodore-inner-world.md`, `wiki/theodore.md` |
| **Alt-Sable (Dark Sable)** | Leader of dark fairy commanders; alternate-timeline Sable | Hidden in Vol 1; reveal planned for future volume | `brainstorm-titan-biology-culture.md`, `brainstorm-dark-fairy-operations.md`, `wiki/sable.md` (hidden layer) |
| **Theodore's Father** | Runs a printing press; present in London but absent from Theodore's daily life | Normal only | `brainstorm-theodore-inner-world.md`, `wiki/theodore.md` |
| **The Folklorist** | University academic who collects sightings; publishes pamphlet *"The Stories They Tell"* | Normal only | Plot Outline Issues 10-11, Script Prompts |

**Tier 2 — Unnamed but narratively significant (need profiles or lore entries)**

| Character | Role | Key Appearance |
|-----------|------|----------------|
| **Dark fairy commanders (2-3)** | Subordinate commanders directing brain-plugged humans | `brainstorm-dark-fairy-operations.md` |
| **Brain-plugged humans (~5)** | Titan foot soldiers — telegraph operator, factory hand, dock laborer, others | `brainstorm-ogre-origin.md` |
| **The Child** | Young child who reaches toward Thresh without fear | Issue 8 — Thresh's arc turning point |
| **The Clockmaker (Clerkenwell)** | High-end shop owner; discovers "brownie" handprint in oil | Issue 5 — first fairy tale echo generated |
| **The Journalist** | Newspaper reporter who records sightings and the "telegraph demon" | Issues 7, 10 — bridges oral folklore to print |
| **The Lighthouse Keeper** | Witnesses "dancing lights" in the gallery | Issue 7 |
| **The Lamplighter** | First civilian witness; sees will-o'-the-wisps in gutter | Issue 2 |
| **Prior Operatives** | Previous fairy teams at convergence point; left cache and "STAY" | Issues 4, 6, 8 (evidence); backstory across volumes |

**Tier 3 — Background/referenced (brief mentions sufficient)**

| Character | Role |
|-----------|------|
| Theodore's Mother | Deceased before story; era-appropriate causes |
| Theodore's Grandmother | Deceased; source of fairy tales; storytelling voice Theodore inherits (Issue 9) |
| The Clockmaker's Wife | Hears brownie story |
| Harbor Authority men | Dismiss lighthouse keeper's report |
| The Child's Parent | Calls child away from Thresh |
| Theodore's friends/peers | Repeat his fairy stories; folklore propagation chain |

### Secondary Character Development Prompts

#### Tier 1 — Brainstorm + Wiki

**Mr. Cribbage**

```
/bs
```

```
Let's brainstorm Mr. Cribbage for GrimGlow — Theodore's clockmaker master.
He needs three states across Volume 1:

1. NORMAL: "Competent but unkind in a mundane way — dismissive, impatient, uninterested
   in Theodore's cleverness." What makes him specifically unkind? Not villainous — mundanely
   crushing. He takes credit for Theodore's fixes. He's skilled but cold. What's his workshop
   like? His daily rhythm? His reputation in the neighborhood?

2. BRAIN-PLUGGED: The dark fairy commanders implant him because his shop sits near telegraph
   infrastructure the Titans are corrupting. What does brain-plugging look like from the outside?
   Dark veins from the implant site, iridescent eyes, oily skin sheen, movement that lacks
   natural micro-adjustments. How does Theodore discover what happened to Cribbage?
   The power dynamic inverts completely — the master who dismissed Theodore now needs his help.

3. RECOVERED: "Comes back wrong — confused, diminished, missing time, personality flattened."
   The origin of changeling stories. What specifically is lost? Fine motor skills (a clockmaker
   who can't hold a tool)? Memory gaps? Emotional flatness? Does he remember Theodore differently?

Reference characters/brainstorms/brainstorm-theodore-inner-world.md, world-building/brainstorms/brainstorm-ogre-origin.md,
and characters/wiki/theodore.md for existing material on Cribbage.
```

```
/wiki
```

```
Create a canonical character profile for Mr. Cribbage, Theodore's clockmaker master.
Sources: world-building/brainstorms/brainstorm-ogre-origin.md, characters/brainstorms/brainstorm-theodore-inner-world.md,
characters/wiki/theodore.md, comic/GrimGlow_Volume1_Plot_Outline.md, and the Cribbage brainstorm.
Include: physical description, personality, workshop details, relationship with Theodore,
three states (normal, brain-plugged, recovered-but-diminished), the changeling echo,
and his role in the convergence point (his shop's proximity to telegraph infrastructure).
Save to characters/wiki/cribbage.md.
```

**Alt-Sable (Dark Sable)**

```
/bs
```

```
Let's brainstorm Alt-Sable — the dark fairy commander who leads the Titan operation in London.
She is an alternate-timeline version of Sable who "made the opposite choices at every fork —
dominance over cooperation, control over trust, power over connection."

I need to explore:
- The dark mirror principle at every level: light/geometric vs. shadow/organic tech,
  cooperation vs. dominance, trusted squad vs. brain-plugged conscripts
- Her command style — how does it parallel Sable's? Same tactical precision, same patience,
  same hard calls — but her "squad" is brain-plugged humans, not trusted companions
- What choices diverged? At what fork did Alt-Sable choose power over connection?
- Her appearance — does she look like Sable? Is the resemblance immediately visible or
  subtle enough to miss? What does her suit look like (dark mirror of command silver)?
- Her presence in Volume 1 — she's hidden, but her tactical patterns mirror Sable's.
  Does Sable sense something familiar about the enemy commander's decisions?
- The Volume 2+ reveal — when Sable discovers the mirror, every Volume 1 decision recontextualizes

Reference world-building/brainstorms/brainstorm-titan-biology-culture.md,
world-building/brainstorms/brainstorm-dark-fairy-operations.md,
and characters/wiki/sable.md (hidden layer section) for existing material.
```

```
/wiki
```

```
Create a canonical character profile for Alt-Sable (Dark Sable), the dark fairy commander.
Sources: world-building/brainstorms/brainstorm-titan-biology-culture.md,
world-building/brainstorms/brainstorm-dark-fairy-operations.md, characters/wiki/sable.md (hidden layer),
and the Alt-Sable brainstorm.
Include: identity, physical description (dark mirror of Sable), command style,
the divergence point, her London operation, parallels with Sable's Volume 1 decisions,
relationship to the brain-plugged human network, and the planned reveal.
Mark Volume 2+ content clearly. Use <hidden> tags for spoiler material.
Save to characters/wiki/alt-sable.md.
```

**Theodore's Father**

```
/bs
```

```
Let's brainstorm Theodore's father for GrimGlow.
He runs a printing press in London. Present in the city but absent from daily life.
"Not absent by choice — absent by circumstance."

I need to explore:
- His printing operation — what does he print? Broadsheets? Pamphlets? Commercial jobs?
  Where is the press located relative to Cribbage's workshop and the squad's territory?
- The absence — mother died (childbirth or disease), father couldn't manage a child and a press.
  Theodore apprenticed to Cribbage for practical reasons. How often do they see each other?
  Is there warmth when they do, or has distance calcified?
- His name — Theodore Edmund Hartley carries parental aspiration. What kind of man names
  his son that? Someone with ambitions his station hasn't delivered on yet.
- The convergence mechanism — Theodore's fairy tale + his father's press = printed myth
  that can survive centuries. Does Theodore bring the story to his father? Does the father
  print it? This is the propagation engine for the entire convergence point.
- Theodore's grandmother (his father's mother?) — source of the fairy tales Theodore inherited.
  What was the father's relationship with her stories? Did he dismiss them or treasure them?

Reference characters/brainstorms/brainstorm-theodore-inner-world.md and characters/wiki/theodore.md
for existing material.
```

```
/wiki
```

```
Create a canonical character profile for Theodore's father (name TBD from brainstorm).
Sources: characters/brainstorms/brainstorm-theodore-inner-world.md, characters/wiki/theodore.md,
and the father brainstorm.
Include: name, occupation (printing press operator), physical description,
personality, relationship with Theodore, the absence and its causes,
the printing press as convergence mechanism, connection to the grandmother's fairy tales.
Save to characters/wiki/theodore-father.md.
```

**The Folklorist**

```
/bs
```

```
Let's brainstorm the Folklorist for GrimGlow — the university academic who codifies
the fairy tales into permanent published form.

He appears in Issues 10-11 and his pamphlet "The Stories They Tell" shares the volume's title.
I need to explore:
- Who is he? Victorian folklorist at a London university — what discipline?
  (Folklore studies were genuinely emerging in the 1880s — the Folk-Lore Society was founded 1878.)
- His methodology — does he collect accounts scientifically? Interview witnesses?
  Compile newspaper clippings? What draws him to these specific sightings?
- The pamphlet — what does it contain? How is it organized? Fairy sightings (brownies,
  dancing lights, will-o'-the-wisps) alongside monster sightings (the telegraph demon,
  shadows that move wrong, the Tall Ones). Two mythologies in one publication.
- His significance — he transforms scattered oral and journalistic folklore into
  permanent, academically legitimized text. "The mythology is setting like concrete."
  He is the mechanism by which ephemeral stories become durable culture.
- Does he ever encounter the squad directly? Or does he only work from secondhand accounts?
- His relationship to the convergence point — if Theodore's fairy tale is the origin story,
  the Folklorist's pamphlet is the academic legitimization that makes it survive.

Reference comic/GrimGlow_Volume1_Plot_Outline.md (Issues 10-11)
and comic/GrimGlow_Volume1_Script_Prompts.md for existing mentions.
```

```
/wiki
```

```
Create a canonical character profile for the Folklorist.
Sources: comic/GrimGlow_Volume1_Plot_Outline.md, comic/GrimGlow_Volume1_Script_Prompts.md,
and the Folklorist brainstorm.
Include: name (from brainstorm), university affiliation, physical description,
methodology, the pamphlet "The Stories They Tell" (contents, publication, impact),
his role in the folklore codification chain, and his significance to the convergence point.
Save to characters/wiki/folklorist.md.
```

#### Tier 2 — Brainstorm + Lore Entries

**Dark Fairy Commanders**

```
/bs
```

```
Let's brainstorm the dark fairy commander faction for GrimGlow.
Alt-Sable leads, but there are 2-3 subordinate commanders in the London operation.
These are fairy-sized beings from the diverged Titan civilization who direct
brain-plugged human foot soldiers.

I need to explore:
- How many commanders total? What are their specializations?
  (One for each Titan operation zone? Telegraph, industrial, waterfront?)
- Their relationship to Alt-Sable — do they serve willingly? Are they also alternate-timeline
  versions of someone? Or are they a different class of operative?
- Their tech — inverted fairy tech. What does their communication protocol look like?
  Encrypted, short-range, shadow-frequency? How do they control the brain-plugged humans?
- Their visibility in Volume 1 — mostly hidden behind their human muscle.
  When do they become visible? Do any of them encounter the squad directly?
- Their cloaking — the same "wrongness" as the Titans, or something subtler at fairy scale?

Reference world-building/brainstorms/brainstorm-dark-fairy-operations.md
and world-building/brainstorms/brainstorm-titan-biology-culture.md for existing material.
Output to world-building/ as a brainstorm file.
```

**Brain-Plugged Humans / Ogre Origin**

```
/bs
```

```
Let's brainstorm the brain-plugged humans as individual characters for GrimGlow.
There are approximately 5 in the London operation. Each was a person before the device
went in at the base of the skull.

I need to explore:
- Who are they specifically? A telegraph operator, a factory hand, a dock laborer —
  what were their lives before? Names? Families? The horror is that they were people.
- The brain-plugging process — what does it look like? The device goes in at the base of
  the skull. The victim's will is overridden. Dark veins spread from the implant site.
  Eyes develop an iridescent sheen. Skin takes on an oily quality. Movement loses
  the micro-adjustments of natural motion.
- Control states — direct command (real-time puppeteering), standing orders (patrol loops),
  or uncontrolled fugue (when signal is lost). What happens in each state?
- The changeling echo — "people stolen by dark forces and brought back... changed."
  When released or when devices fail, they come back wrong. What specifically is lost?
- The ogre origin — Luma notices the physiological changes map to ogre physiology
  in the squad's medical databases. The Titans aren't using an existing slave race.
  They're creating one from humanity across centuries. This is seed material for Volume 2.
- Cribbage as the specific case study — the named brain-plugged human Theodore knows.

Reference world-building/brainstorms/brainstorm-ogre-origin.md for extensive existing material.
Output to world-building/ as a brainstorm file.
```

**Victorian Witness Chain**

```
/bs
```

```
Let's brainstorm the Victorian witness chain for GrimGlow — the humans who see the squad
and the Titans and generate the folklore that becomes the convergence point.

The chain runs: squad actions → human witnesses → oral retelling → journalism → academic
codification → printing → permanent mythology. I need to develop each link:

1. THE LAMPLIGHTER (Issue 2) — First witness. Sees will-o'-the-wisps in a rain gutter.
   Crosses himself. Tells someone at the pub. What kind of man? Superstitious? Practical?
   Does he believe what he saw or rationalize it?

2. THE CLOCKMAKER (Issue 5) — Clerkenwell shop owner, not Cribbage. Finds a tiny handprint
   in oil on his workbench. Tells his wife a brownie visited. Leaves out a saucer of milk.
   What kind of man leaves milk for a brownie? Educated? Traditional? Charmed?

3. THE LIGHTHOUSE KEEPER (Issue 7) — Reports dancing lights in the gallery to harbor authority.
   Harbor men dismiss it as drink. What kind of man makes an official report about fairy lights?
   Conscientious? Stubborn? Does he know how it sounds?

4. THE JOURNALIST (Issues 7, 10) — Notes down the keeper's report. Later writes about the
   "telegraph demon." Bridges oral folklore to print media. What paper? What beat?
   Sensationalist or earnest? Does he believe any of it?

5. THE CHILD (Issue 8) — Younger than Theodore. Wanders into Thresh's alley. Sees Thresh
   and isn't afraid. Reaches out a hand. Parent calls them away. Does the child tell anyone?
   Does this become a story? "I saw a tiny red knight in the alley."

6. THEODORE'S FRIENDS (ongoing) — Peers who hear Theodore's accounts and repeat them.
   Childhood folklore transmission — the most unreliable and the most durable.

How do these individual sightings compound into a cultural phenomenon that the Folklorist
can collect? What's the tipping point where scattered stories become shared mythology?

Reference comic/GrimGlow_Volume1_Plot_Outline.md for all witness appearances.
Output to world-building/ as a brainstorm file.
```

**Prior Operatives**

```
/bs
```

```
Let's brainstorm the prior operatives for GrimGlow — the previous fairy teams sent
to the convergence point before the current squad.

The evidence chain: old fairy glyphs across London (Issue 4), a sealed church basement
cache containing a corroded wing-pack, a dead data core, and the carved word "STAY" (Issue 8).
Sable's mission file references "prior insertions — none of whom reported back" (Issue 9).

I need to explore:
- How many teams? One? Several across centuries? A single long-lived operative?
- When were they sent? Decades before the squad? Centuries? The church foundation legends
  suggest the "good folk" were present when the church was built — how old is that?
- What was their mission? The same as the squad's (intervention at the convergence point)?
  Or reconnaissance that evolved into something else?
- Why didn't they report back? Did they choose to stay? Were they ordered to? Did they die?
  The word "STAY" has four readings: confirmation, horror, self-portrait, evidence.
- What happened to them physically? The corroded wing-pack and dead data core suggest
  they lived and died here. Are there descendants? Bones? Other caches?
- The fairy glyphs at human height — someone was communicating with humans. Who? Why?
  Was this an earlier version of the Theodore relationship?
- How does this connect to the local folklore about "the good folk" blessing the church site?
  The prior operatives ARE the old fairy tales, just as the current squad is the new ones.

Reference comic/GrimGlow_Volume1_Plot_Outline.md (Issues 4, 6, 8, 9),
world-building/brainstorms/brainstorm-temporal-mechanics.md,
and characters/brainstorms/brainstorm-luma-temptation.md for existing material.
Output to world-building/ as a brainstorm file.
```

#### Tier 3

Tier 3 characters (Theodore's mother, grandmother, clockmaker's wife, harbor men, child's parent, Theodore's peers) are developed organically within the Tier 1 and Tier 2 brainstorms above — no dedicated prompts needed.

---

## Links

- [creative-writing-skills plugin](https://github.com/haowjy/creative-writing-skills) — cw-brainstorming, cw-prose-writing, cw-story-critique, cw-official-docs, cw-style-skill-creator
- See `CLAUDE.md` for full project context, character tables, visual language rules, and tech stack details
