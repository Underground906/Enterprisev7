# Enterprise OS Platform — Screen Inventory
## All Screens Across 8 Modules

**Date:** 2026-02-14
**Source:** PRD_Enterprise_OS_V7_MASTER.md
**Note:** Each module is a standalone app. 8 modules x 5 core screens = 40 primary screens + shared screens.

---

## MODULE 1: NAVIGATION CENTRE (The Brain)
*App: NavOS | Purpose: Strategy → Roadmap → Daily Focus*

| # | Screen | Route | Layout | Kit Source |
|---|--------|-------|--------|-----------|
| 1 | Goal Intake Wizard | `/nav/goals/new` | Dashboard Form (multi-step) | Brainwave + Briefberry |
| 2 | Goal Health Dashboard | `/nav/dashboard` | **UNIQUE** — heatmap + cards | Brainwave + Zipformat |
| 3 | Morning Brief (6AM Digest) | `/nav/brief` | Dashboard Home | Brainwave |
| 4 | Decision & Iteration Log | `/nav/decisions` | Dashboard List | Brainwave + Trakr |
| 5 | AI Challenge Console | `/nav/challenges` | Chat + Dashboard | Source AI + Brainwave |
| 6 | Role Perspective Panel | `/nav/perspectives` | Dashboard Detail | Brainwave |

---

## MODULE 2: COMMAND DECK (The Hands)
*App: Execution.ai | Purpose: Work Sessions → Outputs → Digests*

| # | Screen | Route | Layout | Kit Source |
|---|--------|-------|--------|-----------|
| 7 | Active Cockpit | `/cmd/session` | **UNIQUE** — 3-pane (log + chat + outputs) | Brainwave + Source AI |
| 8 | Session History | `/cmd/sessions` | Dashboard List | Brainwave + Trakr |
| 9 | Auto-Digest View | `/cmd/digests` | Dashboard Detail | Brainwave |
| 10 | Agent Registry | `/cmd/agents` | Dashboard List | Brainwave |
| 11 | Agent Workspace | `/cmd/agents/:id` | Dashboard Detail | Brainwave + Source AI |
| 12 | Approval Queue | `/cmd/approvals` | Dashboard List | Brainwave |
| 13 | Org Pulse | `/cmd/pulse` | **UNIQUE** — live activity feed | Brainwave + Social Dashboards |
| 14 | Velocity Metrics | `/cmd/metrics` | Analytics | Brainwave + Zipformat |

---

## MODULE 3: CORE ENGINE (The Nervous System)
*App: Connective.ai | Purpose: Routing → Indexing → Governance*

| # | Screen | Route | Layout | Kit Source |
|---|--------|-------|--------|-----------|
| 15 | Routing Rules Editor | `/engine/routing` | Dashboard Form | Brainwave |
| 16 | Universal Index | `/engine/index` | Dashboard List | Brainwave + Trakr |
| 17 | RAG Quality Dashboard | `/engine/rag` | Analytics | Brainwave + Zipformat |
| 18 | Schema Library | `/engine/schemas` | Dashboard List | Brainwave |
| 19 | Error & Failure Log | `/engine/errors` | Dashboard List | Brainwave |
| 20 | Provenance Auditor | `/engine/provenance` | Dashboard Detail | Brainwave + Trakr |

---

## MODULE 4: KNOWLEDGE LIBRARY (The Stomach)
*App: DigestOS | Purpose: Ingest → Extract → Classify → Store*

| # | Screen | Route | Layout | Kit Source |
|---|--------|-------|--------|-----------|
| 21 | Ingestion Inbox | `/library/inbox` | Dashboard List | Brainwave |
| 22 | Artifact Extraction View | `/library/extract/:id` | **UNIQUE** — split-screen editor | Brainwave |
| 23 | Promotion Console | `/library/promote` | Dashboard List (with actions) | Brainwave |
| 24 | Semantic Search | `/library/search` | **UNIQUE** — search + facets + results | Brainwave + Triply |
| 25 | Pipeline Health Monitor | `/library/health` | Analytics | Brainwave + Zipformat |
| 26 | Session Archive | `/library/sessions` | Dashboard List | Brainwave + Trakr |

---

## MODULE 5: TEMPLATE HUB (The DNA)
*App: ScaleOS | Purpose: Blueprints → Scaffolds → Generation*

| # | Screen | Route | Layout | Kit Source |
|---|--------|-------|--------|-----------|
| 27 | Template Catalogue | `/templates/browse` | Dashboard List (card grid) | Brainwave |
| 28 | Template Detail | `/templates/:id` | Dashboard Detail | Brainwave |
| 29 | Dynamic Document Generator | `/templates/generate` | Dashboard Form (wizard) | Brainwave + Briefberry |
| 30 | Scaffold Replicator | `/templates/scaffold` | Dashboard Form | Brainwave |
| 31 | Prompt Chain Editor | `/templates/prompts` | **UNIQUE** — visual flow builder | Brainwave |
| 32 | Brand DNA Vault | `/templates/brand` | Dashboard Detail | Brainwave + Caresync |

---

## MODULE 6: DOMAIN PILLARS (The Organs)
*App: PillarOS | Purpose: 23 Specialist Knowledge Domains*

| # | Screen | Route | Layout | Kit Source |
|---|--------|-------|--------|-----------|
| 33 | Pillar Grid | `/pillars` | Dashboard Home (card grid) | Brainwave |
| 34 | Pillar Detail / Canon Viewer | `/pillars/:id` | Dashboard Detail | Brainwave |
| 35 | Artifact Browser | `/pillars/:id/artifacts` | Dashboard List | Brainwave + Trakr |
| 36 | Thread Archive | `/pillars/:id/threads` | Dashboard List | Brainwave |
| 37 | Pillar Routing Rules | `/pillars/:id/routing` | Dashboard Form | Brainwave |
| 38 | Cross-Pillar Search | `/pillars/search` | Dashboard List (search) | Brainwave + Triply |

---

## MODULE 7: BUILD FACTORY (The Kinetic Limbs)
*App: Velocity.ai | Purpose: Concept → Build → Launch*

| # | Screen | Route | Layout | Kit Source |
|---|--------|-------|--------|-----------|
| 39 | Project Registry | `/factory/projects` | Dashboard List | Brainwave + Trakr |
| 40 | Project Detail | `/factory/projects/:id` | Dashboard Detail | Brainwave + Trakr |
| 41 | 17-Step Mission Control | `/factory/projects/:id/pipeline` | **UNIQUE** — step tracker | Brainwave + Trakr + Strivo |
| 42 | Assembly Dashboard | `/factory/projects/:id/assemble` | **UNIQUE** — drag-and-drop | Brainwave + Tendly |
| 43 | PRD Editor | `/factory/projects/:id/prd` | Dashboard Form (rich text) | Brainwave |
| 44 | Build Story Timeline | `/factory/projects/:id/story` | Dashboard Detail (timeline) | Brainwave + Trakr |

---

## MODULE 8: OPERATIONS (The Immune System)
*App: Immunity.ai | Purpose: Post-Launch Governance*

| # | Screen | Route | Layout | Kit Source |
|---|--------|-------|--------|-----------|
| 45 | System Health Dashboard | `/ops/health` | **UNIQUE** — org heatmap | Brainwave + Zipformat |
| 46 | Strategic Goal Cascade | `/ops/goals` | **UNIQUE** — visual tree | Brainwave |
| 47 | Canonisation Queue | `/ops/canon` | Dashboard List | Brainwave |
| 48 | Daily Digest Viewer | `/ops/digest` | Dashboard Detail | Brainwave |
| 49 | Whole-Org Pulse | `/ops/pulse` | Dashboard List (live feed) | Brainwave + Social Dashboards |
| 50 | KPI Dashboard | `/ops/kpi` | Analytics | Brainwave + Zipformat |

---

## SHARED SCREENS (Cross-Module)

| # | Screen | Route | Layout | Kit Source |
|---|--------|-------|--------|-----------|
| 51 | Login | `/login` | Auth | Briefberry |
| 52 | Register / Onboarding | `/register` | Auth (multi-step) | Briefberry + Strivo |
| 53 | User Profile | `/profile` | Dashboard Form | Brainwave |
| 54 | Settings | `/settings` | Dashboard Form | Brainwave |
| 55 | Global Search | `/search` | Dashboard List | Brainwave + Triply |
| 56 | Notification Centre | `/notifications` | Dashboard List | Brainwave |

---

## SUMMARY

| Module | Screens | Unique Designs | Templated |
|--------|---------|---------------|-----------|
| Navigation Centre | 6 | 1 (Goal Health Dashboard) | 5 |
| Command Deck | 8 | 2 (Active Cockpit, Org Pulse) | 6 |
| Core Engine | 6 | 0 | 6 |
| Knowledge Library | 6 | 2 (Artifact Extraction, Semantic Search) | 4 |
| Template Hub | 6 | 1 (Prompt Chain Editor) | 5 |
| Domain Pillars | 6 | 0 | 6 |
| Build Factory | 6 | 2 (Mission Control, Assembly Dashboard) | 4 |
| Operations | 6 | 2 (System Health, Goal Cascade) | 4 |
| Shared | 6 | 0 | 6 |
| **TOTAL** | **56** | **10** | **46** |

---

## BOILERPLATE COVERAGE

Enterprise OS uses primarily **dashboard layouts** since it's an internal tool:

| Layout | Screens Using It | Count |
|--------|-----------------|-------|
| Dashboard List (table/grid + filters) | Session History, Agent Registry, Approval Queue, Universal Index, Inbox, Catalogue, Pillar Grid, Project Registry, Canon Queue, etc. | 22 |
| Dashboard Detail (header + tabs + panels) | Digest View, Agent Workspace, Pillar Detail, Project Detail, Build Story, etc. | 12 |
| Dashboard Form (inputs + actions) | Goal Intake, Routing Rules, Scaffold, PRD Editor, Settings, etc. | 10 |
| Analytics (charts + stat cards) | Velocity Metrics, RAG Quality, Pipeline Health, KPI Dashboard, etc. | 5 |
| Chat Interface | AI Challenge Console, Active Cockpit (chat pane) | 2 |
| Auth | Login, Register | 2 |
| Unique | 10 screens needing custom design | 10 |

**One kit (Brainwave 2.0) covers 90%+ of Enterprise OS screens.** It's the dashboard workhorse.

---

## BUILD PRIORITY

Enterprise OS is in **maintenance mode** for the 90-day plan. But when building:

### Phase 1: Core Experience (Modules 1-2)
- Navigation Centre: Goal Dashboard + Morning Brief + AI Challenge
- Command Deck: Active Cockpit + Session History + Digest

### Phase 2: Knowledge Layer (Modules 3-4)
- Core Engine: Routing Rules + Universal Index
- Knowledge Library: Ingestion Inbox + Semantic Search + Artifact Extraction

### Phase 3: Production Layer (Modules 5-7)
- Template Hub: Catalogue + Generator
- Domain Pillars: Pillar Grid + Canon Viewer + Artifact Browser
- Build Factory: Project Registry + Mission Control

### Phase 4: Governance (Module 8)
- Operations: System Health + KPI Dashboard + Goal Cascade

---

*56 screens. 10 unique designs. 46 templated. Brainwave 2.0 is the base for everything.*
