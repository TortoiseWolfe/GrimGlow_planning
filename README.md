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

characters/
  GrimGlow_Character_Prompts.md        — Painterly art prompts (Sable, Wren, Jink, Thresh, Luma, Theodore)
  GrimGlow_Character_Turnarounds.md    — Meshy.ai 3D model reference sheets

comic/
  GrimGlow_Volume1_Plot_Outline.md     — 12-issue plot outline, three-act structure
  GrimGlow_Volume1_Script_Prompts.md   — Full 22-page script generation prompts per issue
  GrimGlow_Volume1_Issue_Prompts.md    — Cover/key moment art prompts per issue

concept-art/
  GrimGlow_Concept_Sable.png
  GrimGlow_Concept_Wren.png
  GrimGlow_Concept_Jink.png
  GrimGlow_Concept_Thresh.png
  GrimGlow_Concept_Luma.png

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

## Phase 1: World Building

Use `cw-brainstorming` to explore and capture world rules before committing them to wiki pages. Brainstorming notes stay skeletal — AI suggestions are tagged, nothing is locked in.

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

**Output:** Save brainstorming notes to `world-building/` directory as working markdown files.

---

## Phase 2: Character Development

Start with brainstorming to deepen backstories and voice, then formalize into wiki-style profiles.

### Brainstorm Character Depth

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

### Formalize as Wiki Pages

Once brainstorming is solid, create canonical character profiles:

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

---

## Phase 3: Style Guide Creation

Create a GrimGlow prose style that Claude can follow consistently. This skill analyzes existing writing and produces AI-directed style instructions.

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

Output as a style guide markdown file at style-guide.md.
```

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
- style-guide.md for prose style

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
and consistency with the GrimGlow style guide at style-guide.md.
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
Style: style-guide.md
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

- [ ] **World wiki pages** — Locations (London at fairy scale, the wreckage, Theodore's workshop), tech systems (fairy tech rules, steampunk tech rules), faction lore (Titans, prior operatives)
- [ ] **Character profiles** — Deep backstory + voice guide for Sable, Wren, Jink, Thresh, Luma, Theodore
- [ ] **GrimGlow style guide** — Prose style skill derived from Story Bible visual language
- [ ] **Comic Issue 1 script** — Full 22-page script; test the entire pipeline end-to-end
- [ ] **Phase 1 dialogue trees** — Ink scripts for the browser prologue (squad conversations, Theodore discovery)
- [ ] **Comic Issues 2-12 scripts** — Remaining 11 issues, one at a time through the write/critique/revise cycle
- [ ] **NPC system prompts** — Ollama personality prompts for Phase 2 (Theodore 7B, ambient NPCs 3B)
- [ ] **Lore articles** — In-world documents (Theodore's journal entries, squad mission logs, Titan field reports)

---

## Links

- [creative-writing-skills plugin](https://github.com/haowjy/creative-writing-skills) — cw-brainstorming, cw-prose-writing, cw-story-critique, cw-official-docs, cw-style-skill-creator
- See `CLAUDE.md` for full project context, character tables, visual language rules, and tech stack details
