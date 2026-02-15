# Enterprise OS Platform — Page Inventory
## 8 Tabs. Permission-Gated. One Living Organism.

**Date:** 2026-02-14 (Corrected)
**Based on:** PRD_Enterprise_OS_V7_MASTER.md, PRD_5_Coherence_Enterprise_Platform.md, Google Notebook EnterpriseOS Summary (8 reports + 3 infographics)
**Sources:** See SESSION_SOURCES.md

---

## Design Philosophy

**8 tabs on the home screen. One per module. Everything lives inside them.**

The same 8 tabs are visible to everyone — but the depth and breadth of what's shown within each adapts to the user's permission level (L1-L7). A freelancer clicking "Command Deck" sees their scoped workspace. The CEO clicking it sees whole-org velocity.

**System Root (00) is invisible.** It's the spine — governance, naming conventions, master context. It runs under the hood but is never a tab.

**S>C>E Governance is visible everywhere.** Yellow (Staging), Green (Canonical), Blue (Execution) badges appear on all content throughout the platform.

---

## THE HUB (Home Screen)

| Element | Purpose |
|---------|---------|
| **8 Module Tiles** | Navigation to each module. Each tile shows a health indicator and key metric |
| **Morning Brief** | Auto-generated "6AM newspaper" — yesterday's wins, today's top 3 priorities. Role-appropriate |
| **Org Pulse** (L5+) | Live activity feed — who's working on what, where the bottlenecks are |
| **State Snapshot** (L7) | CEO view — what is true right now. Strategic alignment health score (1-10) |

The Hub is the landing page. It adapts based on permission level:
- **L1 Freelancer:** Their assigned tasks + relevant templates
- **L2 Professional:** Their sessions, outputs, today's priorities
- **L3 Team Lead:** Team activity + their own work
- **L4 Dept Head:** Pillar health + team rollups
- **L5 Executive:** Build milestones + resource gaps + morning brief
- **L6 C-Suite:** KPI pulse + MRR + decision traceability
- **L7 CEO:** Everything. Org Pulse. State Snapshot. AI Challenge alerts

---

## TAB 1: NAVIGATION CENTRE (The Brain)
*Sets direction. Tracks alignment. Validates strategy against reality.*

### Screens Within This Tab

| # | Screen | Route | Purpose | Min Level |
|---|--------|-------|---------|-----------|
| 1 | Goal Intake Wizard | `/nav/goals/new` | Stream-of-consciousness portal. User dumps intent, AI asks refinement questions, auto-generates Alignment-to-Assets plan using the 5A Foundation | L2 |
| 2 | Goal Health Dashboard | `/nav/dashboard` | Visual heatmap of active objectives. Health Scores (1-10) calculated from alignment drift, activity completion, decision velocity | L3 |
| 3 | Morning Brief | `/nav/brief` | Daily "newspaper" — yesterday's wins, today's top 3 priorities. Pre-calibrated by the system. Available from Hub too | L1 |
| 4 | Decision & Iteration Log | `/nav/decisions` | "Version History" for strategy. Every pivot logged with rationale. Shows the "messy path" not just the final decision | L3 |
| 5 | AI Challenge Console | `/nav/challenges` | Proactive sidebar: "This task has been idle 5 days. Delete or commit a date?" System challenges assumptions, suggests optimisations | L5 |
| 6 | State Snapshot | `/nav/state` | What is true right now. AI refreshes daily. Generates morning briefs and flags misalignment between Activities and Alignment | L6 |

**5A Foundation visible throughout:** Alignment (Vision) → Awareness (Reality) → Accountabilities (Ownership) → Activities (Rhythm) → Assets (Compounding)

**5 Dynamic Layers:** State, Decisions, Learning, Iterations, AI Dialogue — each goal tracks all 10 components

---

## TAB 2: COMMAND DECK (The Hands)
*Where work happens. Sessions logged. Total Recall.*

### Screens Within This Tab

| # | Screen | Route | Purpose | Min Level |
|---|--------|-------|---------|-----------|
| 7 | Active Cockpit | `/cmd/session` | The 3-Habit Execution Loop: Start Session (Intent) → Work Inside (Collaboration) → End Session (Auto-Synthesis). Three-pane layout: running log (left), AI chat (middle), outputs pane (right). Every input source and thread URL captured | L1 |
| 8 | Session History | `/cmd/sessions` | Previous sessions with auto-generated summaries. Searchable. Full provenance chain | L1 |
| 9 | Auto-Digest Generation | `/cmd/digests` | Split-screen: messy session log transforms into polished manager-ready summary. Zero-effort reporting | L3 |
| 10 | Agent Registry | `/cmd/agents` | Library of 80+ role profiles to activate per session. Each agent has specialised lens (SEO Lead, Data Engineer, Copy Chief, etc.) | L2 |
| 11 | Approval & Governance Queue | `/cmd/approvals` | "Swipe to Approve" interface for promoting Staging to Canonical. The quality gate | L4 |

**Session Log Entry Schema:** Every entry captures: timestamp, entry_type (work/decision/output/note/milestone), message, input_source (type, platform, thread_name, thread_url), outputs (type, path, pillar_id), goal_id

**Org Pulse (L5+):** Real-time view of every active session across the entire company

---

## TAB 3: CORE ENGINE (The Nervous System)
*Routes signals. Indexes everything. Ensures zero-latency knowledge transfer.*

### Screens Within This Tab

| # | Screen | Route | Purpose | Min Level |
|---|--------|-------|---------|-----------|
| 12 | Universal Index | `/engine/index` | Filterable list of every file, thread, artifact in the system. Epoch Counts. Full provenance metadata | L2 |
| 13 | Routing Rules Editor | `/engine/routing` | Logic-builder for keyword thresholds per pillar. Semantic scoring + LLM fallback configuration | L4 |
| 14 | RAG Quality Dashboard | `/engine/rag` | Chunking efficiency, token counts, embedding accuracy. HNSW index performance. Vector retrieval quality | L4 |
| 15 | Schema & Data Model Library | `/engine/schemas` | PostgreSQL/JSON schemas. New projects pull their skeleton from here | L3 |
| 16 | Error Library & Failure Log | `/engine/errors` | Diagnostic "heart monitor" for script and API failures. Routing accuracy metrics | L3 |

**Routing Pipeline:** Capture → Process → Route (score against 23 pillar keyword maps) → Store → Index

**Path Predictability:** PATH = ROOT/COMPONENT/PILLAR_ID/ZONE_PREFIX_FOLDER_NAME — agents calculate, never search

---

## TAB 4: KNOWLEDGE LIBRARY (The Stomach)
*Ingests raw data. Digests into 29 artifact types. Makes everything RAG-searchable.*

### Screens Within This Tab

| # | Screen | Route | Purpose | Min Level |
|---|--------|-------|---------|-----------|
| 17 | Ingestion Inbox | `/library/inbox` | Global inbox: Pending, Processing, Routed, Unrouted. URL Sniffer for web content. Multi-source: PDF, Word, AI chat exports, YouTube transcripts, Slack, GitHub, RSS | L2 |
| 18 | Artifact Extraction View | `/library/extract/:id` | Split-screen: raw source (left) vs. 29 extracted artifact types (right). The EKX-1 methodology in action | L3 |
| 19 | Promotion Console | `/library/promote` | Quality Gate: review Staging content, one-click promote to Canonical. The S→C transition. Human-mandatory review | L4 |
| 20 | Semantic Search | `/library/search` | Universal search across all pillars. Lattice Filters by Project, Domain, Date. Hybrid: vector + keyword + metadata | L1 |
| 21 | Pipeline Health Monitor | `/library/health` | Real-time status bars for active scrapers, fetchers, and ingestion jobs. Throughput metrics | L4 |

**5-Stage Metabolic Pipeline:** Capture → Extract (EKX-1: 29 artifact types) → Classify (score against pillars) → Store (PostgreSQL + pgvector) → Index (master indices updated, stakeholders notified)

**The 29 Artifact Types:** Frameworks, SOPs, Decisions, Code Snippets, Market Intel, Hooks, UI Specs, Database Schemas, Prompts, Templates, Wizards, Design Tokens, Agent Compositions, Headline Formulas, Copy Formulas, Copy Checklists, UI Layouts, Workflows, Checklists, KPI Cards, Trust Badges, Style References, Keyword Matrices, Search Intent Maps, Avatar Profiles, Market Validations, Hub+Spoke Models, Canonical References, Persona Overlays

---

## TAB 5: TEMPLATE HUB (The DNA)
*Genetic repository. If a process is mastered once, it's never reinvented.*

### Screens Within This Tab

| # | Screen | Route | Purpose | Min Level |
|---|--------|-------|---------|-----------|
| 22 | Template Catalogue | `/templates/browse` | Searchable grid: Agents, Prompts, SOPs, Project Scaffolds, Copy Frameworks. 7 artifact types: Frameworks, Schemas, Prompts, Templates, Wizards, Canonical References, Execution Artifacts | L1 |
| 23 | Dynamic Document Generator | `/templates/generate` | Wizard: select blueprint, fill parameters, AI assembles high-fidelity doc using Brand DNA and Role Perspectives | L2 |
| 24 | Scaffold Replicator | `/templates/scaffold` | One-click deployment: 9-folder project scaffold (Build Factory) or 16-folder domain scaffold (Pillars) | L4 |
| 25 | Prompt Chain Editor | `/templates/prompts` | Visual flow builder chaining AI models into production sequences. Multi-step prompt orchestration | L3 |
| 26 | Brand DNA Vault | `/templates/brand` | Irreducible backbone: vision, voice rules, unique mechanisms. The guardrails all agents must follow | L2 |

---

## TAB 6: DOMAIN PILLARS (The Organs)
*23+ specialist knowledge domains. Symmetric 16-folder scaffold. Zero Abstraction.*

### Screens Within This Tab

| # | Screen | Route | Purpose | Min Level |
|---|--------|-------|---------|-----------|
| 27 | Pillar Grid | `/pillars` | Bird's-eye view of all 23+ pillars. Item counts, health status (freshness score), last update, Canonical vs Staging ratio | L2 |
| 28 | Pillar Detail / Canon Viewer | `/pillars/:id` | Authoritative reference document. The SSOT that AI agents read from exclusively. 16-folder scaffold view | L1 |
| 29 | Artifact Browser | `/pillars/:id/artifacts` | Filterable archive of high-value extracted assets within a specific pillar | L2 |
| 30 | Thread Archive | `/pillars/:id/threads` | Raw AI conversation histories with full provenance chain | L3 |
| 31 | Routing Rules (per Pillar) | `/pillars/:id/routing` | Pillar-specific keyword scoring thresholds and semantic routing configuration | L4 |

**4 Functional Groups:**
- **Knowledge Organs:** Ingestion, Keywords, Navigation, RAG, Agents, Research
- **Creation Organs:** Avatars, Brand, Copy, Content, Graphics, Video, UI, ContentGen
- **Platform Organs:** Property, Fitness, Voice, Dog
- **System Organs:** Roles, Practices, Build Story, SEO, Enterprise_OS

**16-Folder Scaffold (every pillar identical):**
- Zone A (Ingestion): 01_Staging, 02_Raw_Inputs, 13_Research_Dumps
- Zone B (Digestion): 04_Keywords, 05_RAG_Bundles, 06_Taxonomy, 02_Routing
- Zone C (Canon): 03_Single_Source_of_Truth
- Zone D (Execution): 07_Frameworks, 08_SOPs, 09_Prompts, 10_UI_Blocks, 11_Templates, 12_Artifacts
- Zone E (Governance): 14_Audit_Logs, 15_Health, 16_Archive

---

## TAB 7: BUILD FACTORY (The Kinetic Limbs)
*High-speed production line. Intelligence assembled into launched products.*

### Screens Within This Tab

| # | Screen | Route | Purpose | Min Level |
|---|--------|-------|---------|-----------|
| 32 | Project Registry | `/factory/projects` | Active builds with Maturity Grades: Speculative → Operational → Production-Ready. Each project uses the 9-folder scaffold | L2 |
| 33 | 17-Step Mission Control | `/factory/:id/pipeline` | Linear production line tracking all 17 build stages. Track 1 (Intelligence) → Track 2 (Foundation) → Track 3 (Brand & Creative) → Track 4 (Build & Launch) | L3 |
| 34 | Assembly Dashboard | `/factory/:id/assemble` | Drag-and-drop: snap Copy Frameworks, UI Components, and Database Schemas from Pillars into the active project scaffold | L3 |
| 35 | PRD Editor | `/factory/:id/prd` | Multi-role AI reviewers flag risks before coding begins. The "Role-Informed" spec where 80+ expert profiles contribute perspectives | L3 |
| 36 | Build Story | `/factory/:id/story` | Chronological timeline capturing breakthroughs, anti-patterns, and the evolution of each build. Institutional memory of HOW things got built | L2 |

**17-Step Pipeline:**
1. Market Analysis → 2. LSI Keyword Taxonomy → 3. Keyword Permutation → 4. Market Players → 5. Competitor & Avatar Deep Dive → 6. Database Architecture → 7. Platform Architecture → 8. Content Strategy → 9. Metrics Framework → 10. Brand Foundation → 11. PRD Creation → 12. Copy Architecture → 13. UI/UX Design → 14. Development → 15. Content Production → 16. GTM Execution → 17. Optimisation Loop

**Golden Sequence:** PRD (Function) → Copy Architecture (Logic) → UI/UX Design (Interface)

**9-Folder Project Scaffold:** 01_Strategy, 02_Product, 03_Design, 04_Architecture, 05_Development, 06_Testing, 07_Deployment, 08_Marketing, 90_Archive

---

## TAB 8: OPERATIONS (The Immune System)
*Post-launch governance. Closes the loop between intent and results.*

### Screens Within This Tab

| # | Screen | Route | Purpose | Min Level |
|---|--------|-------|---------|-----------|
| 37 | System Health Dashboard | `/ops/health` | Org heatmap: ingestion stats, routing accuracy, pillar freshness scores. The "vital signs" of the enterprise | L4 |
| 38 | Strategic Goal Cascade | `/ops/goals` | Visual tree: individual tasks auto-update department-level goals which auto-update CEO-level strategic objectives. Know → Build → Ship → Learn coherence loop | L5 |
| 39 | Canonisation Queue | `/ops/canon` | Quality Gate for promoting Staging to Canonical across the whole system. Aggregate view of all pending promotions | L4 |
| 40 | Daily Digest Viewer | `/ops/digest` | AI-synthesised morning briefing, tailored by role level. Team Lead gets tactical. CEO gets strategic pivot validation | L3 |
| 41 | Whole-Org Pulse | `/ops/pulse` | Live activity feed: every active session, every routing decision, every output. The CEO's "what is happening RIGHT NOW" view | L6 |

**10 Operational Areas:** Financials, Legal, Marketing, HR, Public Relations, Metrics, Social, Lead Gen, Project Coordination, Goal Achievement

**The Coherence Loop:** Task completion auto-updates CEO strategic objectives

---

## SHARED / GLOBAL SCREENS

| # | Screen | Route | Purpose |
|---|--------|-------|---------|
| 42 | Login | `/login` | Authentication |
| 43 | Register / Onboarding | `/register` | New user setup + role assignment (L1-L7) |
| 44 | User Management | `/admin/users` | Assign roles, set permission levels, manage access (L6+ only) |
| 45 | Settings | `/settings` | Personal preferences, notifications, integrations |
| 46 | Global Search | `/search` | Cross-module semantic search. Same engine as Knowledge Library search but accessible from anywhere |

---

## PERMISSION & GATES — 7-LEVEL HIERARCHY

This is the core of the Enterprise product. The same interface, progressively disclosed.

| Level | Role | Hub View | Data Access |
|-------|------|----------|-------------|
| L1 | Freelancer | Assigned tasks + relevant templates | Scoped workspace only. Read-only Brand Rules and SOPs |
| L2 | Individual Pro | Today's priorities + their sessions/outputs | Own work + search access. Total Recall for their tasks |
| L3 | Team Lead | Team activity + approvals | Team session logs, velocity metrics, output approval queue |
| L4 | Dept Head | Pillar health + team rollups | Domain Pillar health, freshness scores, cross-session efficiency, promotion queue |
| L5 | Executive | Build milestones + Morning Brief + Org Pulse | Build Factory progress, Navigation alignment, resource gaps, strategic KPIs |
| L6 | C-Suite | Strategic KPI Pulse + decision traceability | MRR, revenue pipelines, financial health. Full audit trail |
| L7 | CEO/Owner | **Everything.** Org Pulse. State Snapshot. AI Challenges | Total visibility. Auto-generated CEO Digest. Strategic pivot validation. The complete organism |

**Progressive Disclosure Rule:** Higher levels see everything lower levels see, plus their own layer. L7 can drill down to L1-level detail on any team member.

---

## S>C>E GOVERNANCE (Visible Throughout)

| Badge | State | Who Controls | UI Treatment |
|-------|-------|-------------|-------------|
| 🟡 Yellow | **Staging** — Raw, unverified input | System auto-assigns on intake | Yellow badge on all unverified content |
| 🟢 Green | **Canonical** — Verified source of truth | Humans promote (mandatory review) | Green badge. Agents read ONLY from this |
| 🔵 Blue | **Execution** — Generated output | Agents execute from Canonical | Blue badge. Considered disposable |

**The Golden Rule:** STAGING = suggestions. CANONICAL = truth. EXECUTION = output. Agents read from CANONICAL. Humans promote from STAGING to CANONICAL. If the canonical layer is solid, you can regenerate everything else.

**Promotion Queue** accessible from: Knowledge Library (Tab 4), Operations (Tab 8), and within each Pillar (Tab 6).

---

## SCREEN-TO-KIT MAPPING

| Screen | Primary Kit | Secondary Kit | What To Pull |
|--------|------------|---------------|-------------|
| Hub / Home | Brainwave 2.0 | Square Dashboard | Module tiles, stat cards, activity feed |
| Goal Intake Wizard | Brainwave 2.0 | Briefberry | Multi-step form, progress bar |
| Goal Health Dashboard | Brainwave 2.0 | Zipformat | Heatmap, health score cards |
| Active Cockpit | Brainwave 2.0 | Source Fusion AI | 3-pane layout, chat interface, log stream |
| Agent Registry | Brainwave 2.0 | — | Card grid, search, filters |
| Universal Index | Brainwave 2.0 | Trakr | Data table, filters, bulk actions |
| Routing Rules Editor | Brainwave 2.0 | — | Form builder, logic controls |
| Ingestion Inbox | Brainwave 2.0 | — | Status pipeline, file upload |
| Artifact Extraction | Brainwave 2.0 | — | Split-screen editor |
| Semantic Search | Brainwave 2.0 | Triply AI | Search + facets + results |
| Pillar Grid | Brainwave 2.0 | — | Card grid with health indicators |
| 17-Step Mission Control | Brainwave 2.0 | Trakr + Strivo | Step tracker, pipeline view |
| Assembly Dashboard | Brainwave 2.0 | Tendly | Drag-and-drop interface |
| System Health | Brainwave 2.0 | Zipformat | Org heatmap, metrics |
| Goal Cascade | Brainwave 2.0 | — | Visual tree, progress bars |
| Auth | Briefberry | Strivo | Auth forms |
| All other screens | Brainwave 2.0 | — | Dashboard list/detail/form templates |

**Brainwave 2.0 covers 90%+ of all Enterprise OS screens.** It's the dashboard workhorse.

---

## BOILERPLATE LAYOUTS

| Layout | Screens Using It | Count |
|--------|-----------------|-------|
| Dashboard List (table/grid + filters) | Session History, Agent Registry, Universal Index, Ingestion Inbox, Template Catalogue, Pillar Grid, Project Registry, Canon Queue, Thread Archive, Error Log | ~15 |
| Dashboard Detail (header + tabs + panels) | Pillar Detail, Digest View, Build Story, PRD Editor, Brand DNA Vault | ~8 |
| Dashboard Form (inputs + actions) | Goal Intake, Routing Rules, Scaffold Replicator, Settings | ~6 |
| Analytics (charts + stat cards) | Goal Health, RAG Quality, Pipeline Health, System Health, Goal Cascade | ~5 |
| Unique 3-Pane (cockpit) | Active Cockpit | 1 |
| Unique Split-Screen | Artifact Extraction, Auto-Digest Generation | 2 |
| Chat Interface | AI Challenge Console | 1 |
| Auth | Login, Register | 2 |
| Search | Semantic Search, Global Search | 2 |
| Live Feed | Org Pulse, Whole-Org Pulse | 2 |

---

## SUMMARY

| Section | Screens |
|---------|---------|
| Hub (Home) | 1 (adapts by level) |
| Tab 1: Navigation Centre | 6 |
| Tab 2: Command Deck | 5 |
| Tab 3: Core Engine | 5 |
| Tab 4: Knowledge Library | 5 |
| Tab 5: Template Hub | 5 |
| Tab 6: Domain Pillars | 5 |
| Tab 7: Build Factory | 5 |
| Tab 8: Operations | 5 |
| Shared/Global | 5 |
| **TOTAL** | **47** |

But many of these are the SAME layout template with different data. In practice:
- ~15 are "Dashboard List" (same template, different columns)
- ~8 are "Dashboard Detail" (same template, different content)
- ~5 are "Analytics" (same template, different charts)
- **~8 are unique designs** (Cockpit, Extraction, Heatmap, Goal Cascade, Mission Control, Assembly, Org Pulse, AI Challenge)

---

## BUILD PRIORITY

Enterprise OS is in **dogfood mode** — build for internal use first, then commercialise.

### Phase 1: Daily Operations (Hub + Tabs 1-2)
- Hub: 8 module tiles + Morning Brief
- Navigation: Goal Intake + Goal Health Dashboard
- Command Deck: Active Cockpit + Session History

### Phase 2: Knowledge Layer (Tabs 3-4)
- Core Engine: Universal Index + Routing Rules
- Knowledge Library: Ingestion Inbox + Semantic Search + Promotion Console

### Phase 3: Production (Tabs 5-7)
- Template Hub: Catalogue + Generator
- Pillars: Pillar Grid + Canon Viewer
- Build Factory: Project Registry + Mission Control

### Phase 4: Governance & Scale (Tab 8 + Permissions)
- Operations: System Health + Goal Cascade + Org Pulse
- User Management: L1-L7 permission system
- S>C>E governance badges throughout
