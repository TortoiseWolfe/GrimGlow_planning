<!--
GrimGlow Phase 1 Constitution — adapted from ScriptHammer v1.0.1
(ratified 2025-09-20, last amended 2025-09-25). Source:
~/repos/ScriptHammer/.specify/memory/constitution.md.

This constitution governs Phase 1 of GrimGlow per the two-phase dev plan
(`docs/GrimGlow_Two_Phase_Development_Plan.md` §2): the browser-first
prologue (Phase 1a) and its iOS port (Phase 1b). It does NOT govern
Phase 2 (Unity full game) — see `constitution-unity.md` for that.

Principles I–VI inherit from ScriptHammer with stack-specific
adaptations called out inline. Principles VII–VIII are added for
game-specific concerns and orchestration discipline that ScriptHammer
treats as runtime guidance but GrimGlow elevates to constitutional.
-->

# GrimGlow Phase 1 Constitution

## Core Principles

### I. Component Structure Compliance

Every component MUST follow the 5-file pattern: `index.tsx`,
`Component.tsx`, `Component.test.tsx`, `Component.stories.tsx`, and
`Component.accessibility.test.tsx`. This structure is enforced via CI/CD
pipeline validation. Use the component generator (`pnpm run
generate:component` for Phase 1a, RN plopfile equivalent for Phase 1b)
to ensure compliance. No exceptions — manual component creation will
cause build failures.

**Phase 1b adaptation:** the 5-file pattern still holds; the file
extensions become `.tsx` for RN components, the Storybook story uses
`@storybook/react-native`, and the accessibility test uses
`react-native-testing-library` + `axe-react-native`.

### II. Test-First Development

Tests MUST be written before implementation following RED-GREEN-REFACTOR
cycle. Minimum 25% unit-test coverage baseline (target 58%+). Critical
paths — save/load, dialogue branching, scene state machines — require
comprehensive test suites. Husky pre-push hooks block commits without
tests.

**Phase 1a:** Vitest (unit) + Playwright (browser E2E) + Pa11y (a11y).
**Phase 1b:** Vitest (unit) + Detox or Maestro (RN E2E) +
axe-react-native (a11y).

3D canvas content is exempt from automated a11y scans (canvas not
auditable by Pa11y/axe-core) but requires documented manual a11y review
per Principle V's 3D carve-out.

### III. SpecKit/PRP Methodology (NON-NEGOTIABLE)

Features taking >1 day MUST follow the SpecKit flow:

```
PRP → /speckit.specify → /speckit.clarify → /speckit.plan
    → /speckit.checklist → /speckit.tasks → /speckit.analyze
    → /speckit.implement
```

PRPs live at `docs/prp-docs/<feature>-prp.md`. SpecKit artifacts live
at `specs/<NNN-name>/`. Ad-hoc feature development is forbidden.
"This one is small" is not an exemption — write the PRP.

### IV. Docker-First Development

Docker Compose is the primary development environment. Never `pnpm
install` on the host. Never `sudo` — permission errors mean Docker, not
chmod. Git commits run inside the container so hooks fire correctly.
Multi-stage Dockerfiles with explicit `dev`/`test`/`prod` targets.
`docker compose up` is the only way to start any track.

**Phase 1b adaptation:** EAS Build runs in the cloud rather than local
Docker for the iOS native build itself, but local dev (Metro bundler,
Vitest, Storybook for RN) still runs in Docker.

### V. Progressive Enhancement + Accessibility as a Build Gate

Core functionality works everywhere first; enhancements layer on top.
WCAG 2.1 Level AA minimum (AAA the stretch goal). 90+ Lighthouse
performance, 95+ Lighthouse accessibility. 44px minimum touch targets.
Mobile-first responsive on 1a; mobile-native on 1b. Keyboard navigation,
screen reader compatibility, visible focus indicators. Accessibility is
not a polish phase — it's a build gate.

**3D content carve-out (game-specific):**

- `<canvas>` regions are excluded from automated Pa11y/axe scans —
  document the exclusion explicitly in `config/pa11yci.json` (1a) or
  the RN equivalent (1b)
- Manual a11y review required for every 3D scene before merge
- `prefers-reduced-motion: reduce` MUST disable auto-rotation, idle
  animations, parallax, and ambient camera drift; user-initiated
  motion (orbit, click-to-move) still works
- All 3D scenes MUST provide a 2D HUD/overlay path for critical UI
  (dialogue, inventory, HUD chrome) using standard accessible
  components, so canvas content is never the only way to perceive
  game state
- Captions/subtitles required for any audio with narrative content
- Color is not the only encoding for game-state signals (use shape,
  motion, or text alongside color)

### VI. Privacy & Compliance First

GDPR-compliant by default. Consent modal before any tracking. Analytics
only activate after explicit user consent. Save state in localStorage
(1a) or AsyncStorage/SecureStore (1b) is treated as user data — clear
disclosure in the privacy policy, "delete my save" UI affordance.
Tip-jar payments via Stripe Payment Links (1a) or StoreKit IAP (1b)
honor user privacy: no PII beyond what the payment processor strictly
requires.

Secrets never in committed code. `.env` gitignored. Committed config
files use `${VAR:-placeholder}` pattern.

### VII. Game-Specific Discipline

GrimGlow adds disciplines ScriptHammer doesn't need. These are
constitutional, not advisory.

**Save-export code (per dev plan §3.2):** Phase 1 MUST emit a short
deterministic string encoding key player decisions for Phase 2
carryover. Save format is reverse-compatible — Phase 2 reads any
1a/1b save without modification. Versioned with explicit migration
paths.

**Asset bridge:** Master GLB assets, Meshy.ai prompt records, and
shared shader R&D live in a dedicated Git-LFS repo external to this
one. Phase 1 consumes from the bridge; never duplicates assets into
this repo. Adding an asset means committing it to the bridge first,
referencing it here second.

**Authored content versioning:** Ink dialogue scripts (`*.ink`),
character data (`characters/wiki/*.md`), world-building documents
(`world-building/**`), and comic scripts (`comic/**`) are *content*,
not code, but receive code-equivalent review: PR-based, narrative
designer + author sign-off required. Story canon changes require
amendment to the dev plan.

**Logic / rendering separation:** Game logic (scene state machines,
dialogue tree advancement, save format, character behavior) MUST live
in platform-agnostic TypeScript modules importable by both 1a (browser
R3F) and 1b (RN R3F-native). The rendering layer is the only file set
that diverges between 1a and 1b. Every PR that touches game logic
states explicitly which platforms it runs on (both, by default).

**Performance budgets:**

- Total asset budget for 1a initial load: under 50 MB (per dev plan §2.4)
- Streaming acceptable for secondary environments
- Frame target: 60 fps on mid-tier hardware (2020 MacBook Air,
  iPhone 12); 30 fps acceptable on low-end if reduced-motion engaged

### VIII. Multi-Terminal Assembly-Line Orchestration

GrimGlow inherits ScriptHammer's role assembly line, extended with
game-dev roles:

```
STRATEGY: CTO → ProductOwner → BusinessAnalyst
DESIGN:   Architect → UXDesigner → UIDesigner
        + LevelDesigner → NarrativeDesigner → TechnicalArtist → AudioDesigner
CODE:     Developer → Toolsmith → Security
TEST:     TestEngineer → QALead → Auditor
DOCS:     Author → TechWriter
RELEASE:  DevOps → DockerCaptain → ReleaseManager → Coordinator
```

Terminal git rule: **commit only, never push** — only the Operator
(human-in-the-loop) pushes. `.claude/roles/*.md`, `.claude/commands/*.md`,
and orchestration commands (`/dispatch`, `/queue`, `/rfc`, `/council`)
carry forward. Wireframe work uses the SpecKit `/speckit.wireframe.*`
skills (the dedicated 6-role wireframe pipeline was retired and
absorbed into Developer/UIDesigner per ScriptHammer's CLAUDE.md).

The orchestration model is part of the constitution, not a per-feature
addition. New roles get added by amendment, not by ad-hoc role
invention.

## Technical Standards

### Phase 1a Framework Requirements

- Next.js 15.5+ with App Router and static export
- React 19+ with TypeScript strict mode
- Tailwind CSS 4 with DaisyUI for theming (32 themes — same as
  ScriptHammer; the 3D scene reads CSS custom properties for
  warm-gaslight vs. cool-holographic dual lighting per dev plan §2.5)
- `@react-three/fiber` + `@react-three/drei` for R3F
- Ink (inkle) compiled to JS for branching dialogue
- Howler.js or Tone.js for spatial audio
- pnpm 10.16.1, Node.js 20+ LTS

### Phase 1b Framework Requirements

- Expo SDK 53+ with React Native 0.79+
- React 19+ with TypeScript strict mode
- `react-native-unistyles` (or equivalent token-based system) for
  the RN-port of the 32-theme system
- `@react-three/fiber/native` + `expo-gl` for R3F-native
- Same Ink scripts compiled with the same compiler, JS target swapped
- Native audio: `expo-av` or equivalent
- StoreKit 2 for tip-jar IAP

### Testing Standards

- Vitest unit tests (1a + 1b)
- Playwright browser E2E (1a)
- Detox or Maestro RN E2E (1b)
- Pa11y for browser a11y (1a)
- axe-react-native for RN a11y (1b)
- Storybook for component documentation (both phases)
- MSW for API mocking in tests where applicable

### Code Quality

- ESLint with Next.js / Expo config
- Prettier for consistent formatting
- TypeScript strict mode enabled
- Husky pre-commit hooks for validation
- Component structure validation in CI/CD
- Conventional commits with `Co-Authored-By: Claude` footer when
  AI-assisted

## Development Workflow

### SpecKit Execution Flow

Same as ScriptHammer:

1. Create PRP document with requirements
2. Run `/speckit.specify` — produces `spec.md`
3. Run `/speckit.clarify` — interactive clarification
4. Run `/speckit.plan` — produces `plan.md`
5. Run `/speckit.checklist` — quality gates
6. Run `/speckit.tasks` — produces `tasks.md`
7. Run `/speckit.analyze` — cross-artifact consistency
8. Run `/speckit.implement` — execute the plan

### Contribution Process

- Feature branch following naming convention (`<NNN>-<slug>`)
- Implement using Docker environment
- All tests pass before push
- PR with comprehensive description; reference the SpecKit `specs/<NNN-*>/`
- Pass all CI/CD checks for merge
- Operator merges; terminals never push

## Quality Gates

### Build Requirements

- All components follow 5-file structure
- TypeScript compilation without errors
- Build completes without warnings
- Phase 1a static export generates successfully (Vercel/Netlify/itch.io)
- Phase 1b EAS Build succeeds for iOS and (eventually) Android
- Total bundle / asset budget per Principle VII

### Test Requirements

- Unit test coverage above 25% minimum
- All accessibility tests passing (excluding canvas regions, which
  require manual review per Principle V)
- E2E tests run successfully locally
- No failing tests in test suite
- Storybook stories render without errors

### Performance Standards

- Lighthouse Performance: 90+ (1a)
- Lighthouse Accessibility: 95+ (1a)
- First Contentful Paint under 2 seconds (1a)
- Time to Interactive under 3.5 seconds (1a)
- Cumulative Layout Shift under 0.1 (1a)
- Frame rate per Principle VII (1a + 1b)

### Accessibility Standards

- WCAG 2.1 Level AA compliance (AAA stretch goal)
- Keyboard navigation fully functional (1a)
- Game controller and touch input fully functional (1b)
- Screen reader compatibility verified
- Color contrast ratios meet standards
- Focus indicators clearly visible
- Reduced-motion respected (Principle V)
- Captions for narrative audio (Principle V)

## Governance

### Amendment Procedure

Amendments require: documentation of rationale, impact analysis on
existing code/content, migration plan if breaking changes, and operator
approval via PR. Major version bumps for principle changes, minor for
additions, patch for clarifications.

### Compliance Verification

All PRs verify constitutional compliance. CI/CD enforces technical
standards mechanically where possible (5-file structure, test
coverage, type checks, lint, build, Lighthouse). Manual compliance
review for principles that resist mechanization (the 3D a11y
carve-out, narrative content review, story canon).

### Version Management

Constitution follows semantic versioning. All versions archived in this
file's git history. Amendments tracked with ratification dates.

### Enforcement

The constitution supersedes all other practices. Violations must be
justified with documented rationale in the PR description. Temporary
exceptions require an operator-approved sprint constitution. Runtime
AI-assistance guidance lives in `CLAUDE.md`; the constitution is the
authoritative source when the two conflict.

---

**Version**: 1.0.0
**Ratified**: 2026-05-02
**Source constitution**: ScriptHammer v1.0.1 (ratified 2025-09-20)
**Scope**: GrimGlow Phase 1 (browser prologue + iOS port). Phase 2
(Unity full game) is governed by `constitution-unity.md`.
