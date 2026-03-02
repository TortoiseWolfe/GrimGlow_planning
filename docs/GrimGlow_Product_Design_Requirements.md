# GRIMGLOW — Product Design Requirements

*Working Document — v0.1*

| | |
|---|---|
| **Platform** | PC (Windows) |
| **Engine** | Unity (URP/HDRP) |
| **3D Assets** | Meshy.ai (GLB/FBX) |
| **Local AI** | Ollama |
| **Genre** | Stealth / Heist / Action-Adventure |

---

## 1. Product Overview

GrimGlow is a stealth/heist action-adventure game set in a steampunk Victorian world, viewed from the perspective of a squad of four-inch-tall alien soldiers from the far future. Stranded in the past after a crash during a temporal cold war, the squad must scavenge steampunk-era components to repair their ship while evading detection by the giant humans around them and countering enemy operatives (the Titans) who crashed alongside them.

The game combines squad-based tactical gameplay with heist-style mission planning, stealth traversal through scale-shifted environments, and a narrative layer driven by both scripted story beats and dynamic AI-powered NPC conversations.

## 2. Technical Stack

### 2.1 Game Engine: Unity

Unity is selected as the primary engine for the following reasons:

- Mature 3D asset pipeline with native GLB/FBX import from Meshy.ai
- URP (Universal Render Pipeline) or HDRP (High Definition Render Pipeline) for the dual-lighting system central to GrimGlow's visual identity: warm gaslight vs. cool holographic fairy tech
- Built-in NavMesh system supporting multi-scale pathfinding (fairy-scale and human-scale navigation on the same map)
- Extensive Asset Store ecosystem for behavior trees, shader tools, and AI integration
- Free tier covers development up to $200K annual revenue

### 2.2 3D Asset Pipeline

Character models, props, and environmental assets will be generated via Meshy.ai and exported as GLB or FBX. The pipeline is:

1. Generate base model in Meshy.ai from text or image prompts
2. Export as GLB/FBX with materials
3. Import into Unity; adjust materials to URP/HDRP-compatible shaders
4. Rig and animate in Unity (Mixamo for humanoid rigs where applicable)
5. Apply GrimGlow-specific shader effects (holographic glow, degradation overlays, prismatic light trails)

### 2.3 Local AI: Ollama

Conversational NPC AI will be powered by Ollama running as a local background process on the player's machine. Unity communicates with Ollama via HTTP requests to localhost.

## 3. AI System Architecture

GrimGlow requires two distinct AI systems: gameplay AI (pathfinding, combat, stealth behavior) and conversational AI (dynamic NPC dialogue). These are architecturally separate but share a common game-state layer.

### 3.1 Gameplay AI

#### 3.1.1 Squad AI (Fairy Characters)

The player's squad members (Sable, Wren, Jink, Thresh, Luma) operate as AI companions when not directly controlled. Each character requires:

- **NavMesh pathfinding** — Fairy-scale NavMesh baked on surfaces humans consider incidental: shelves, pipes, rafters, windowsills, workbenches. Must support flight (3D NavMesh volumes) for wing-pack traversal.
- **Behavior trees** — Role-specific decision trees. Sable prioritizes cover and overwatch. Wren moves toward objective components. Jink scouts ahead and takes risks. Thresh holds defensive positions. Luma hangs back and provides support.
- **Squad coordination** — Shared awareness system so squad members react to each other's positions, alerts, and status. Example: if Thresh is spotted, Jink creates a distraction.

#### 3.1.2 Human NPC AI (Steampunk Civilians)

Humans operate on predictable routines that the player must learn and exploit. This is the stealth game's core loop.

- **State machine architecture** — States include: Routine, Alert, Searching, Alarmed, Returning to Routine. Transitions driven by line-of-sight, sound, and environmental triggers (e.g., a moved object, a missing component).
- **Perception system** — Vision cones scaled to the fairies' tiny size. Humans don't naturally look at fairy-scale surfaces, so detection depends on movement, light emission (holographic tech glowing in darkness), and noise. A fairy standing still on a dark shelf is nearly invisible; a fairy flying with wing-pack deployed across a lit room is extremely visible.
- **Schedule system** — NPCs follow time-based routines (shopkeeper opens at dawn, locks up at dusk, takes lunch at noon). Missions are designed around exploiting these windows.

#### 3.1.3 Titan AI (Enemy Combatants)

The Titans are large, intelligent, and dangerous. Their AI must feel qualitatively different from human NPCs — they are actively hunting the fairies, not passively going about their lives.

- **Predatory behavior trees** — Titans use sensor sweeps, set traps, and adapt to player tactics. If the player uses a route twice, Titans begin patrolling it.
- **Cloaking system** — Titans use their own stealth tech (dark iridescent shimmer) which the player can learn to detect via environmental cues: animals reacting, shadows behaving wrong, a faint oil-on-water distortion.
- **Escalation** — Titan AI becomes more aggressive as the story progresses. Early game: surveillance. Mid game: active interference. Late game: direct confrontation.

### 3.2 Conversational AI

#### 3.2.1 Architecture Overview

Conversational AI runs through an abstraction layer (the Dialogue Interface) that decouples the game from any specific AI provider. This allows swapping between Ollama (local), a cloud API fallback, or scripted dialogue without changing game code.

| Layer | Component | Function | Location |
|-------|-----------|----------|----------|
| Game State | Context Manager | Tracks story progress, relationships, revealed information | Unity (C#) |
| Prompt Builder | System Prompt Engine | Assembles character persona + context + conversation history into prompt | Unity (C#) |
| Dialogue Interface | HTTP Client | Sends prompt, receives response, handles streaming | Unity (C#) |
| AI Provider | Ollama (primary) | Runs local LLM, returns completions | Local process |

#### 3.2.2 Ollama Integration

Ollama runs as a background service on the player's machine, launched automatically when the game starts and shut down on exit. Unity communicates via HTTP POST to localhost:11434.

- **Primary model:** 7B parameter model (e.g., Mistral 7B, Llama 3.1 8B) for Theodore and key NPCs. Chosen for balance of quality and performance.
- **Lightweight model:** 3B parameter model (e.g., Phi-3 Mini) for ambient NPC barks — shopkeepers, street vendors, background characters who need one or two contextual lines.
- **Model bundling:** Game installer includes Ollama and pre-downloaded model weights. No internet connection required for AI dialogue after installation.

#### 3.2.3 Character System Prompts

Each AI-driven NPC has a persistent system prompt that defines their personality, knowledge boundaries, speech patterns, and relationship to the player. Theodore's system prompt is the most complex:

- **Persona:** Victorian working-class boy, 12–13, tinker's apprentice. Speaks in period-appropriate English without being incomprehensible. Curious, clever, slightly awed.
- **Knowledge boundaries:** Only knows what the fairies have revealed to him in-game. Cannot reference future technology, events, or concepts unprompted. Can speculate about fairy tech using Victorian-era frames (calls holograms "spirit lights," refers to wing-packs as "luminous wings").
- **Emotional state:** Tracked by the Context Manager. Theodore's tone shifts based on story progress — early wonder gives way to concern, protectiveness, and eventually fear as the Titans become more active.
- **Memory injection:** Each prompt includes a compressed summary of all prior conversations and key story events, injected as context. Ollama has no persistent memory; the game manages all state.

#### 3.2.4 Conversation State Management

Because local LLMs have no memory between calls, the game must maintain a conversation state system in Unity:

- **Session history:** Rolling buffer of the current conversation (last 10–15 exchanges) included in each prompt.
- **Persistent memory:** Key facts, decisions, and revelations stored in a structured data file per save game. Compressed into a summary block injected into the system prompt.
- **Relationship tracker:** Numerical values tracking Theodore's trust, fear, curiosity, and loyalty toward each squad member. These modulate the system prompt's tone instructions.
- **Guardrails:** Response validation layer that catches anachronisms, out-of-character statements, and hallucinated plot points before displaying to the player. Flagged responses fall back to a pool of pre-written contextual lines.

### 3.3 Hardware Requirements for AI

| Spec | Minimum (3B model) | Recommended (7B+ model) |
|------|--------------------|-----------------------|
| GPU VRAM | 4 GB | 8 GB+ |
| System RAM | 16 GB | 32 GB |
| Storage (models) | ~2 GB | ~5–10 GB |
| CPU | Modern quad-core | 8-core / Apple Silicon |

The game must detect available hardware at startup and automatically select the appropriate model tier. If hardware is insufficient for any local model, the system falls back to scripted dialogue with no degradation of core gameplay.

## 4. Core Gameplay Systems

### 4.1 Scale System

Every environment exists at two scales simultaneously. The game world is built at human scale; fairy-scale navigation, interaction, and perception are layered on top. A Victorian clockmaker's shop is one room to a human and an entire explorable landscape to the fairies. The scale system is GrimGlow's defining mechanical and visual feature.

### 4.2 Mission Structure

Each mission follows the heist template: Wren identifies a needed component, the squad scouts the location, the player plans an approach (entry point, timing, distractions, contingencies), and executes. Complications arise dynamically — NPC schedule changes, Titan interference, Theodore needing to provide cover. Missions map to the three plot layers: survival (get the part), enemy (counter Titan activity discovered during the heist), and paradox (manage the narrative footprint of the squad's actions).

### 4.3 Stealth and Detection

The fairy squad's primary advantage is invisibility through scale. Detection is driven by the perception system described in Section 3.1.2. The player manages visibility by controlling light emission (holographic tech can be dimmed at the cost of functionality), movement speed (flying is fast but visible; climbing is slow but hidden), and environmental awareness (staying in shadow, using cover objects, timing movements to NPC routines).

### 4.4 Combat

Combat is asymmetric. Fairies cannot overpower humans or Titans through force. Fairy weapons can stun, disorient, or disable — never kill humans. Against Titans, combat is more direct but still emphasizes mobility, teamwork, and environmental advantage over raw damage. Thresh is the squad's damage dealer; Jink provides flanking and distraction; Sable coordinates; Wren deploys tech-based traps; Luma provides healing and buffs.

## 5. Visual and Rendering Requirements

### 5.1 Dual Lighting System

The game's visual identity rests on the contrast between two light vocabularies: warm, amber, analog steampunk light (gaslight, candlelight, furnace glow) and cool, blue-white, geometric holographic fairy tech light. Every scene should feature both, with neither dominating. URP or HDRP must support:

- Volumetric fog and atmospheric scattering for gaslight environments
- Emissive holographic materials with prismatic/iridescent properties for fairy tech
- Real-time shadow interaction between both light types at fairy scale
- Degradation shader system: fairy suits accumulate grime over time while holographic elements continue to glow through the surface layer

### 5.2 Scale Rendering

Environments must be detailed at both human and fairy scale. A workbench surface that reads as a flat table at human scale must have visible wood grain, tool marks, and scattered components that function as terrain at fairy scale. This requires high-resolution environmental textures and careful LOD management to maintain performance.

### 5.3 Titan Visual Effects

Titan cloaking is rendered as a dark iridescent distortion — oil-on-water shimmer with slight spatial warping. When Titans are nearby but unseen, the environment subtly reacts: shadows elongate, gaslight flickers, small animals flee. These ambient cues are the player's primary detection mechanism.

## 6. Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Player hardware insufficient for local LLM + game simultaneously | AI dialogue unavailable or causes frame drops | Auto-detect hardware; fall back to scripted dialogue gracefully. Design all critical story beats as scripted, not AI-generated. |
| Local LLM breaks character or produces anachronisms | Immersion broken, player sees "behind the curtain" | Response validation layer catches common failures. Pre-written fallback lines for each conversation context. System prompts heavily constrained with few-shot examples. |
| Meshy.ai model quality inconsistent across characters | Visual inconsistency in art direction | Establish style guide prompts per character. Manual cleanup pass on all imported models. Shader-based visual unification (consistent holographic glow, suit material). |
| Dual-scale environments too expensive to render | Performance issues on mid-range PCs | Aggressive LOD system. Fairy-scale detail only loaded when camera is at fairy scale. Human-scale simplification when zoomed in. |
| Ollama version or model compatibility changes | AI system breaks on update | Pin Ollama version and model weights in installer. Bundle everything; do not rely on external downloads post-install. |

## 7. Open Questions

1. Should the player directly control one fairy and issue commands to the squad, or switch freely between all five?
2. How deep should the Theodore conversation system go? Full open-ended dialogue, or AI-enhanced branching (AI selects and modulates from a large pool of authored responses)?
3. Is the comic book a separate product or integrated into the game (e.g., motion comic cutscenes between missions)?
4. What is the target mission count for a first release? 8–12 heist missions maps to roughly 15–25 hours of gameplay.
5. Should Titan encounters be scripted set-pieces or dynamic (Titans appear procedurally based on player actions)?
6. Multiplayer: is co-op squad play (each player controls one fairy) a future consideration, or is this strictly single-player?
