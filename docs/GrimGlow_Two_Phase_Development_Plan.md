# GRIMGLOW — Two-Phase Development Plan

*Browser Prologue → Full Game — Working Document — v0.1*

| | |
|---|---|
| **Phase 1** | Three.js browser experience |
| **Phase 2** | Unity PC game |
| **Bridge** | Shared assets, narrative, audience |

---

## 1. Strategic Overview

GrimGlow development follows a two-phase model. Phase 1 builds a browser-playable narrative experience in Three.js that establishes the IP, attracts an audience, and validates core creative decisions. Phase 2 is the full PC game in Unity, informed by everything learned in Phase 1. The two phases share characters, world-building, visual assets, story continuity, and audience.

This is not a prototype-then-rebuild strategy. Phase 1 is a standalone, shippable product — a prologue chapter that tells a complete story within the larger GrimGlow narrative. Players who discover GrimGlow through the browser experience carry their investment in the characters and world directly into Phase 2. The prologue does not replace the full game; it makes the full game matter more when it arrives.

## 2. Phase 1 — Browser Prologue (Three.js)

### 2.1 Product Definition

A browser-based narrative experience playable at a URL with no download or installation. Genre sits between point-and-click adventure and visual novel with real-time 3D environments. Estimated playtime: 45–90 minutes. Free to play, with optional support/tip mechanism.

### 2.2 Narrative Scope

The prologue covers the crash and the first 48 hours. The squad wakes in the wreckage of their ship, hidden beneath the floorboards of a tinker's workshop. They assess damage, establish what they've lost, and begin their first scavenging mission. Theodore discovers them at the end of the prologue — his face appearing through a gap in the floorboards, lit from below by their holographic tech. That image is the final frame. The prologue's job is to make the player desperate to know what happens next.

Story beats covered: the crash, waking in the wreckage, Sable taking command, Wren's assessment of what's broken, the first venture out of the ship into the workshop (the player's first experience of the scale shift), a scavenging mission to acquire a basic component, the first distant evidence of Titan presence (a shadow that moves wrong, an animal that flees from nothing), and Theodore's discovery. The Titans are felt but not seen. The paradox layer is hinted at once — Luma finds a mark on a beam that looks like it was made by fairy tech, but old. Decades old.

### 2.3 Gameplay Scope

Phase 1 is deliberately constrained to what Three.js handles well, and avoids systems that would require the full Unity toolchain.

| System | Phase 1 (Browser) | Phase 2 (Unity) |
|--------|-------------------|-----------------|
| Navigation | Click-to-move / WASD in constrained environments. Fixed or semi-fixed camera angles. | Full 3D free camera. Flight. Open environments. |
| Stealth | Puzzle-based. Learn NPC pattern, time your movement. Turn-based or phase-based. | Real-time stealth with perception cones, sound, light detection. |
| Combat | None. Tension is environmental (a cat, a closing door, a dropped tool). | Asymmetric real-time combat vs. Titans. |
| Squad AI | Squad members are narrative presences. They speak, react, advise. Player controls one fairy; others follow scripted behavior. | Full behavior trees. Companion AI. Role-based tactics. |
| NPC AI | Scripted patrol routes, simple state machine (idle/alert). Puzzle inputs. | Full state machines with schedules, perception, memory. |
| Dialogue | Branching authored dialogue with character portraits. No LLM. | Ollama-powered dynamic conversation for Theodore and key NPCs. |
| Environments | 2–3 hand-crafted locations (ship interior, workshop floor, workshop surfaces). High detail, small scope. | Full city. Multiple heist locations. Dual-scale open environments. |

### 2.4 Technical Stack

- **Rendering:** Three.js with WebGL 2. Custom shaders for holographic glow (emissive + fresnel), gaslight volumetrics (simple fog planes), and the degradation overlay (layered PBR materials with grime mask).
- **Scene management:** Each location is a self-contained Three.js scene. Transitions between locations use fade-to-black or in-world movement (flying through a crack in the floorboards).
- **3D assets:** Meshy.ai exports (GLB). Same models feed both phases. Phase 1 uses lower-poly versions with baked lighting where possible to maintain browser performance.
- **Audio:** Howler.js or Tone.js for spatial audio. Ambient steampunk soundscape (ticking clocks, steam hiss, distant street noise). Holographic tech emits a subtle crystalline hum.
- **Dialogue system:** Ink (inkle's narrative scripting language) compiled to JavaScript. Branching dialogue with state tracking. Character portraits displayed alongside text.
- **UI framework:** HTML/CSS overlay on the Three.js canvas for dialogue boxes, inventory, and HUD elements. Keeps UI crisp at all resolutions.
- **Hosting:** Static site. Deployable to Vercel, Netlify, or itch.io. Total asset budget target: under 50 MB for fast initial load, with streaming for secondary environments.

### 2.5 Visual Targets

Phase 1 prioritizes mood over fidelity. The constrained environments allow for high detail within small spaces. The visual targets are:

- **Scale awe:** The first time the player leaves the crashed ship and sees the workshop from fairy scale — a workbench as a plateau, a scattered handful of screws as boulders, gaslight filtering through cracks like shafts of sunlight — must land as a genuine moment of wonder. This single scene is the visual proof-of-concept for the entire IP.
- **Light contrast:** Every frame should feature the warm/cool duality. The crashed ship's interior glows with damaged holographic systems (flickering blue-white geometric light) while the workshop around it is all amber gaslight and dark wood. The two light vocabularies meeting is the visual thesis.
- **Painterly quality:** Post-processing should push the rendered image toward the painterly style established in the character prompts. Subtle film grain, soft vignetting, warm color grading. The game should feel like a painting you can walk through.

### 2.6 Success Metrics

Phase 1 succeeds if it accomplishes three things:

- **Audience:** Builds a mailing list / community (Discord, social media) of players who want Phase 2. Target: 10,000+ players within 3 months of launch, with a measurable conversion to community membership.
- **Validation:** Tests whether the scale-shift mechanic, the fairy/steampunk aesthetic fusion, and the character dynamics resonate emotionally with players. Measured through completion rates, time spent in dialogue, and qualitative feedback.
- **Pipeline proof:** Confirms that Meshy.ai → Three.js/Unity asset pipeline works. Confirms that the visual language (holographic glow, degradation, dual lighting) translates from concept art prompts to real-time 3D. Every asset created for Phase 1 feeds Phase 2.

## 3. Phase 2 — Full Game (Unity)

### 3.1 Product Definition

A PC game (Windows) distributed via Steam and/or itch.io. Stealth/heist action-adventure with squad-based tactics, real-time 3D environments at dual scale, Ollama-powered NPC dialogue, and a full narrative arc covering all three plot layers (Survival, Enemy, Paradox). Estimated playtime: 15–25 hours. Premium pricing.

### 3.2 Narrative Continuity

Phase 2 picks up exactly where the prologue ends: Theodore has just discovered the fairies. Players who completed Phase 1 enter Phase 2 with existing emotional investment in the characters and an understanding of the world's rules. Players who skipped Phase 1 get a brief cinematic recap (built from Phase 1 assets) that covers the crash and discovery.

The prologue's events are canon. Choices the player made in Phase 1 (dialogue selections, how they handled the scavenging mission, whether they were careful or reckless) can optionally carry forward via a save-export code — a short string that encodes key decisions, entered at the start of Phase 2. This rewards Phase 1 players without punishing newcomers.

### 3.3 Technical Stack

As specified in the GrimGlow Product Design Requirements document (v0.1). Key systems:

- **Engine:** Unity with URP or HDRP.
- **Gameplay AI:** NavMesh pathfinding (multi-scale), behavior trees (squad + Titan AI), state machines (human NPC routines).
- **Conversational AI:** Ollama running locally. 7B model for Theodore and key NPCs. 3B model for ambient NPC barks. Abstraction layer allowing cloud API fallback. Scripted fallback for insufficient hardware.
- **3D assets:** Meshy.ai pipeline. Phase 1 models upgraded with higher-poly versions, Unity-native materials, and enhanced shaders. Phase 1 environments rebuilt at full fidelity as the opening area of Phase 2.

### 3.4 What Phase 1 De-Risks

By the time Phase 2 begins full production, Phase 1 will have answered the following questions:

| Question | How Phase 1 Answers It |
|----------|----------------------|
| Does the scale-shift mechanic feel good? | Phase 1 players experience it directly. Completion rates and feedback reveal whether wonder or confusion dominates. |
| Do the characters resonate? | Dialogue engagement metrics. Which characters do players spend time with? Which dialogue branches are explored? |
| Does the Meshy.ai pipeline hold up? | Full production test across 6 character models and 2–3 environments. Quality gaps identified before committing to 15+ hours of content. |
| Does the visual language translate to 3D? | Holographic glow, degradation shaders, dual lighting, and painterly post-processing all implemented and tested in browser. Shader logic ports to Unity. |
| Is there an audience? | Community size, engagement, and willingness to pay (measured via tip jar, wishlist signups, survey responses). |
| What's the right dialogue depth? | Phase 1 uses authored branching dialogue. Player response patterns reveal whether open-ended AI conversation (Phase 2) will add value or whether curated branching is sufficient. |

## 4. The Asset Bridge

The two-phase model only works if Phase 1 production feeds Phase 2 directly. This section defines what transfers and how.

### 4.1 3D Models

All character and environment models are created in Meshy.ai and exported as GLB. The master asset is the GLB file, which imports cleanly into both Three.js and Unity.

- **Phase 1:** GLB loaded directly into Three.js. Materials converted to Three.js MeshStandardMaterial or custom ShaderMaterial for holographic effects.
- **Phase 2:** Same GLB imported into Unity. Materials reassigned to URP/HDRP Lit or custom shader graphs. Higher-poly versions generated in Meshy where needed. Rigging and animation added in Unity (Mixamo for humanoids).
- **Shared asset repository:** A single Git-LFS repository holds all master GLB files, texture maps, and Meshy prompt records. Both phases pull from the same source.

### 4.2 Shaders and Visual Effects

The core visual effects — holographic glow, degradation overlay, gaslight volumetrics, Titan distortion — are implemented twice: once in GLSL for Three.js, once in Unity Shader Graph or HLSL. The logic is the same; the implementation language differs. Phase 1 shader development serves as R&D for Phase 2.

- **Holographic glow:** Fresnel-based emissive with animated noise displacement. Phase 1 implementation in Three.js ShaderMaterial. Phase 2 port to Unity Shader Graph with identical parameter names for consistent look.
- **Degradation system:** Layered material with clean base, grime mask (procedurally increasing over game time), and emissive holographic layer bleeding through. Same approach in both engines using mask textures.
- **Gaslight:** Phase 1 uses fog planes and emissive point lights (performant for browser). Phase 2 upgrades to true volumetric lighting in HDRP.

### 4.3 Narrative Content

Dialogue scripts written in Ink for Phase 1 transfer to Phase 2 as the foundation for the authored dialogue pool. Phase 2's AI conversation system uses these scripts as few-shot examples in system prompts, ensuring that Ollama-generated dialogue stays tonally consistent with the voice established in Phase 1.

- **Character voice guides:** Every line of Phase 1 dialogue doubles as a style reference for Phase 2's AI prompts. Sable's clipped authority, Wren's technical bluntness, Jink's irreverence, Thresh's tension, Luma's wonder — all established in authored form before AI extends them.
- **Theodore's voice:** Theodore does not appear in Phase 1 dialogue (he discovers the fairies in the final frame). But his workshop environment, his belongings, and the squad's observations about him establish his character before he speaks. Phase 2's AI system prompt for Theodore draws on these indirect characterizations.
- **World-building consistency:** Lore, terminology, and in-world rules established in Phase 1 (how wing-packs work, what fairy tech looks like to humans, the squad's military structure) are codified into a reference document that feeds both authored and AI-generated content in Phase 2.

### 4.4 Audience

The most valuable asset that transfers between phases is not code or models — it is the community. Phase 1's audience becomes Phase 2's launch audience. The bridge mechanisms are:

- **Mailing list:** Collected at the end of Phase 1 ("Want to know what Theodore says next?"). Directly converts to Steam wishlist notifications and launch-day awareness.
- **Discord / community:** Built around Phase 1 discussion, fan art, speculation about what happens next. Active community at Phase 2 launch is the single strongest predictor of indie game success.
- **Save-export code:** A short alphanumeric string generated at the end of Phase 1 that encodes the player's key decisions. Entered at Phase 2 start to customize the opening state. Creates a tangible thread between the two products.
- **Content creation pipeline:** The comic (if developed alongside) shares characters, visual language, and narrative with both game phases. Each product drives audience to the others.

## 5. Estimated Timeline

These estimates assume a solo developer or very small team. Adjust proportionally for additional contributors.

| Phase | Milestone | Scope | Duration |
|-------|-----------|-------|----------|
| 1 | Pre-production | Story bible finalized. Character models generated. Shader R&D. Three.js scene prototype. | 4–6 weeks |
| 1 | Production | All environments built. Dialogue written in Ink. Stealth puzzle designed. Audio integrated. Post-processing tuned. | 8–12 weeks |
| 1 | Polish & Launch | Playtesting. Bug fixes. Performance optimization (target: 60fps on mid-range hardware, mobile-viable). Deploy to web. | 2–4 weeks |
| Bridge | Community & Learning | Gather player feedback. Build community. Analyze metrics. Begin Unity prototyping. Port shaders. | 4–8 weeks |
| 2 | Pre-production | Unity project setup. Asset pipeline confirmed. NavMesh prototyping. Ollama integration prototype. Level design for first 3 missions. | 6–8 weeks |
| 2 | Production | Full mission content (8–12 missions). Squad AI. Titan AI. Human NPC systems. Theodore conversation system. All environments. | 6–12 months |
| 2 | Polish & Launch | Playtesting. Balancing. Performance optimization. Steam page. Marketing push to Phase 1 audience. | 2–3 months |

Phase 1 total: roughly 3–5 months to a playable browser prologue. Phase 2 total: roughly 10–18 months after Phase 1 ships. The bridge period overlaps with early Phase 2 pre-production.

## 6. Two-Phase-Specific Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Phase 1 sets expectations Phase 2 can't meet | Players expect browser-quality intimacy at Unity scale; disappointment if Phase 2 feels generic | Phase 2's opening area is the Phase 1 workshop rebuilt at full fidelity. Familiar space, elevated quality. Proves the upgrade immediately. |
| Engine switch loses visual consistency | Three.js and Unity render differently; GrimGlow's look changes between phases | Shader logic documented with parameter specs during Phase 1. Side-by-side comparison testing during bridge period. Post-processing tuned to match. |
| Phase 1 audience doesn't convert to Phase 2 buyers | Free browser players aren't willing to pay for PC game | Save-export code creates personal investment. Mailing list + Discord maintain engagement. Phase 2 pricing validated via surveys during bridge period. |
| Phase 2 scope creep from Phase 1 feedback | Players request features that inflate Phase 2 beyond achievable scope | Phase 2 scope locked before community feedback period. Feedback informs execution quality and prioritization, not scope expansion. |
| Momentum loss during bridge period | Too long between Phase 1 and Phase 2; audience moves on | Bridge period includes regular dev updates, behind-the-scenes content, comic releases, and community engagement. Phase 2 early access or demo within 6 months of Phase 1 launch. |
| Meshy.ai models too low quality for Unity's higher fidelity demands | Assets that look fine in Three.js look rough in Unity with better lighting | Identified during Phase 1. Manual cleanup budget allocated in Phase 2 pre-production. Shader-based visual unification (consistent holographic glow, suit materials) compensates for model imperfections. |

## 7. Open Questions

1. Should Phase 1 include a playable Theodore scene (e.g., a short sequence from his perspective before the crash) or should his first appearance be strictly the final reveal?
2. Is the comic developed in parallel with Phase 1, between phases, or alongside Phase 2? Parallel development maximizes cross-promotion but splits production effort.
3. Should Phase 1 be monetized (paid itch.io, Patreon-gated) or free with community-building as the primary goal? Free maximizes reach; paid validates willingness to pay.
4. What's the minimum viable Titan presence in the prologue? The current plan is indirect evidence only (shadows, environmental cues). Should there be a direct Titan encounter to demonstrate the threat?
5. Should the save-export code be a simple decision encoding, or should it include playstyle data (cautious vs. reckless, exploration time, dialogue choices) that modulates Phase 2's AI system prompts?
6. Is mobile browser a Phase 1 target? Three.js runs on mobile but touch controls and performance constraints require additional design and optimization work.
