# 05_TEMPLATE_HUB — README

**Body Metaphor:** The DNA
**Status:** Active — core templates present, expanding
**Standalone App Name:** ScaleOS / Blueprint.ai

---

## Purpose

The enterprise's genetic repository. If a process is mastered once, it is never reinvented from scratch. The Template Hub provides push-button starts for any task — ensuring standardized excellence at scale. It houses the reusable blueprints that tell the Kinetic Limbs (Build Factory) how to assemble materials into living products.

**Core Principle:** "If it will be reused, repeated, or scaled — it belongs in the DNA."

---

## What Belongs Here

- Agent definitions and system prompts
- PRD templates and scaffolds
- SOP templates for repeatable processes
- Master prompt patterns for AI sessions
- Code templates and boilerplate
- Workflow definitions (multi-step chains)
- Document templates (reports, briefs, reviews)
- Planning templates (goal sessions, sprints)
- Context templates (pillar docs, project docs)

## What Does NOT Belong Here

- Filled-in documents or actual PRDs (go to `07_BUILD_FACTORY/[project]/02_Product/`)
- Domain-specific knowledge (go to `06_DOMAIN_PILLARS`)
- Raw content or threads (go to `04_KNOWLEDGE_LIBRARY`)
- Executed scripts (go to `03_CORE_ENGINE`)

---

## Folder Structure

```
05_TEMPLATE_HUB/
├── AGENT_TEMPLATES/       → AI agent definitions and system prompts
│   ├── builder_agent.md         → Agent for build/assembly tasks
│   ├── orchestrator_agent.md    → Agent for multi-step coordination
│   └── validator_agent.md       → Agent for quality checking
├── CODE_TEMPLATES/        → Boilerplate code for common patterns
├── CONTEXT_TEMPLATES/     → Templates for pillar/project context docs
├── DOCUMENT_TEMPLATES/    → General document templates
├── PLANNING_TEMPLATES/    → Goal planning and sprint templates
│   └── GOAL_PLANNING_SESSION.md → Structured goal-setting workflow
├── PRD_TEMPLATES/         → Product requirement document templates
├── PROMPT_TEMPLATES/      → Master prompt patterns for AI sessions
│   └── THREAD_ROUTING.md       → Prompt for routing content to pillars
├── SOP_TEMPLATES/         → Standard operating procedure templates
├── WORKFLOW_TEMPLATES/    → Multi-step workflow definitions
├── PILLAR_DOC_TEMPLATES.md → Master template for pillar documentation
└── 90_ARCHIVE/            → Superseded template versions
```

---

## Key Templates

### Agent Templates
1. **Builder Agent** — Executes specific build tasks within a project scaffold
2. **Orchestrator Agent** — Coordinates multi-agent workflows, manages handoffs
3. **Validator Agent** — Reviews outputs against canon standards and quality gates

### Pillar Documentation Templates
`PILLAR_DOC_TEMPLATES.md` contains 4 standard templates:
- **README.md** — Pillar overview, purpose, folder structure
- **INDEX.md** — File inventory with status tracking
- **ROUTING_RULES.md** — Inbound/outbound routing logic
- **CANON_STATUS.md** — Production readiness audit

### Planning Templates
- **GOAL_PLANNING_SESSION.md** — Structured 5A framework goal intake

### Prompt Templates
- **THREAD_ROUTING.md** — System prompt for classifying content to pillars

---

## The Scaffold Principle

The Hub provides two standard scaffolds used across the system:

### 9-Folder Project Scaffold (Build Factory)
```
01_Strategy → 02_Product → 03_Design → 04_Architecture
→ 05_Development → 06_Testing → 07_Deployment → 08_Marketing → 90_Archive
```

### 16-Folder Pillar Scaffold (Domain Pillars)
```
00_CANON/ → 01_threads/ → 02_artifacts/ → 03+ domain-specific
→ 90_ARCHIVE/
```

Both ensure **Zero Abstraction** — learn one structure, navigate them all.

---

## The 29 Artifact Types

Every piece of extracted knowledge maps to one of 29 types. Each type has (or should have) a corresponding template in this Hub:

| # | Type | Template Status |
|---|------|----------------|
| 1 | Frameworks | Needed |
| 2 | SOPs | Available (SOP_TEMPLATES/) |
| 3 | Decision Logs | Needed |
| 4 | Code Snippets | Available (CODE_TEMPLATES/) |
| 5 | UI Specs | Needed |
| 6 | Database Schemas | Needed |
| 7 | Market Intel | Needed |
| 8 | Hooks & Messaging | Needed |
| 9 | Unique Mechanisms | Needed |
| 10 | Process Maps | Needed |
| 11-29 | Various | Needed |

**Gap:** Most artifact type templates still need creation.

---

## Integration

| Connects To | How |
|-------------|-----|
| 03_CORE_ENGINE | Provides prompt templates for routing scripts |
| 04_KNOWLEDGE_LIBRARY | 29 artifact types guide extraction |
| 06_DOMAIN_PILLARS | Pillar doc templates standardize all 23 pillars |
| 07_BUILD_FACTORY | Project scaffold + PRD templates for every build |
| 02_COMMAND_DECK | Agent templates power the Agent Registry |

---

## Quick Start

1. **Starting a new project?** Copy the 9-folder scaffold from Build Factory
2. **Creating pillar docs?** Use templates in `PILLAR_DOC_TEMPLATES.md`
3. **Setting up an AI agent?** Check `AGENT_TEMPLATES/` for base definitions
4. **Planning a goal?** Use `PLANNING_TEMPLATES/GOAL_PLANNING_SESSION.md`
5. **Routing content?** Reference `PROMPT_TEMPLATES/THREAD_ROUTING.md`

---

**Last Updated:** 2026-02-13
