# ENTERPRISE OS V7 — SYSTEM CAPABILITIES

> **What this system does when everything is working.**
> Use this as a benchmark. If a feature described here isn't working, that's a gap to close.
> Last updated: 2026-02-20

---

## 1. KNOWLEDGE INGESTION AND EXTRACTION

### What It Does
Takes any input — AI chat threads, documents, PDFs, research notes, books, API scrapes, YouTube transcripts, competitor content — and processes it into structured, routed, searchable knowledge. Then runs extraction passes to pull out usable intelligence.

### Two Stages: Routing Then Extraction

**Stage 1 — Routing:** Get the content into the right place.

```
RAW INPUT (any format)
    |
    v
04_KNOWLEDGE_LIBRARY/EXTRACTION_PIPELINE/RAW_INTAKE/
    |
    v
intake_processor.py scores content against pillar keywords
    |
    +--> Score >= 2 keyword hits --> Routes to correct pillar's 01_INPUT/ or 01_threads/
    |
    +--> Score < 2 hits ----------> Goes to 04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/
    |
    v
Routing decision logged to 03_CORE_ENGINE/ROUTING_ENGINE/routing_logs/
```

**Stage 2 — Extraction:** Pull structured intelligence out of the content.

Four extraction processes handle different content types:

| Process | Input Type | What It Extracts | Output |
|---------|-----------|-----------------|--------|
| **27-Domain Pass** | Any content | Classifies across all 27 extraction domains (see below) | Domain tags + extracted items per domain |
| **EKX-1 Thread Extraction** | AI chat threads | 20-section structured summary (decisions, SOPs, scripts, entities, assets, etc.) | Searchable thread summary |
| **Copy/Sales Extraction** | Any project/product/IP content | Benefits, features, problems solved, USPs, unique mechanisms, hooks, sales arguments, objections, proof points, CTAs | Copy intelligence for marketing |
| **Book Extraction** | Book content, long-form IP | Proofs, arguments, facts, rhetorical devices, hooks, objections & myths to disprove, beliefs to challenge, solutions | Book intelligence for content & clarity |

### The Staging-to-Canonical Flow

Every piece of knowledge follows this path:

| Stage | What It Means | Where It Lives | Can Automate? |
|-------|--------------|----------------|---------------|
| **Staging** | Raw, unverified, noisy | `01_INPUT/`, `01_threads/`, `RAW_INTAKE/` | Yes |
| **Canonical** | Reviewed, distilled, stable | `00_CANON/` folders | Only after human sign-off |
| **Execution** | Generated output, disposable | Project deliverables, generated pages | Yes |

**Iron rule:** Execution never flows back to Canonical automatically. A human must approve.

### The 27 Extraction Domains

Every piece of content gets classified across these domains. This is the master taxonomy — it tells you what kind of intelligence a piece of content contains.

1. Product & Platform Definition
2. Benefits & Outcomes
3. Hooks, Messaging & Positioning
4. Unique Mechanisms & Differentiation
5. Processes, SOPs & Workflows
6. Performance, Learning & Feedback
7. Navigation, Goals & Decision Systems
8. Project & Delivery Management
9. Roles, Responsibilities & Virtual Workforce
10. Automation Opportunities
11. Enforcement & Quality Control
12. Knowledge Architecture & RAG
13. Templates & Reusable Scaffolds
14. Data Models & Databases
15. Libraries (UI / Copy / Media / Assets)
16. UI / UX & Interface Implications
17. Engineering & Infrastructure
18. Operations & Post-Launch
19. Commercialisation & Monetisation
20. Governance & Evolution
21. Meta-Systems
22. Scripts, Code & Pipelines
23. Books, Writing & Long-Form IP
24. Courses, Webinars & Educational Products
25. Training & Onboarding Systems
26. External Intelligence Ingestion
27. Intelligence Routing & Dissemination

### EKX-1 Thread Extraction (20 Sections)

When an AI chat thread is ingested, EKX-1 extracts these 20 sections into a structured summary:

1. Narrative & Context — What was this thread about?
2. Objectives (Explicit) — What were we trying to achieve?
3. Success Criteria — How would we know it worked?
4. Decisions & Rules — What was decided?
5. SOPs / Workflows — What processes were defined?
6. Scripts / Commands — What code or commands were produced?
7. Inputs & Outputs — What went in, what came out?
8. Missteps / Errors / Risks — What went wrong?
9. Blockers — What stopped progress?
10. Status — Where did it end up?
11. Progress Markers — What milestones were hit?
12. Refinements — What improved during the thread?
13. Dependencies — What does this depend on?
14. Entity Maps — Key concepts, names, relationships
15. Glossary — Terms defined in this thread
16. Future — What's planned next?
17. Pending — What's unfinished?
18. Open Questions — What's unresolved?
19. Meta-Observations — Patterns, insights about the process itself
20. Reusable Assets — Frameworks, templates, prompts worth keeping

### Copy/Sales Extraction

When content relates to any project, product, platform, or IP you're building, this extraction pulls out commercial intelligence:

| Category | What Gets Extracted |
|----------|-------------------|
| **Benefits** | User benefits, business benefits, operational benefits |
| **Features** | Capabilities, modules, functions |
| **Problems** | Problems the target audience has |
| **Problems Solved** | How this product/service solves each problem |
| **USPs** | What makes this unique vs competitors |
| **Unique Mechanisms** | The proprietary "how it works" — named systems, frameworks, methods |
| **Hooks** | Attention-grabbing angles for headlines, ads, content |
| **Sales Arguments** | Logical and emotional reasons to buy/engage |
| **Objections** | What the audience might push back on |
| **Proof Points** | Evidence: case studies, data, testimonials, demonstrations |
| **CTAs** | Calls to action — what you want them to do next |

This feeds directly into PIL_03_COPY for copywriting across all channels.

**Existing frameworks** (documented in PIL_03 DOCS.md, physical files need creating):
- Copy Block Functions (attention, trust, conversion blocks with psychological triggers)
- Master Copywriter Formulas (Schwartz, Caples, Kennedy, Halbert, Ogilvy)
- Universal Copy Formula (Headline → Subhead → Lead → Body → Offer → CTA → Close)
- 163 asset templates across website, funnel, email, social, ads, video

### Book Extraction

When content relates to your book or long-form intellectual property:

| Category | What Gets Extracted |
|----------|-------------------|
| **Proofs** | Evidence, data, case studies, demonstrations |
| **Arguments** | Core logical arguments and reasoning chains |
| **Facts** | Verifiable facts and statistics |
| **Hooks** | Opening angles, chapter hooks, narrative hooks |
| **Rhetorical Devices** | Metaphors, analogies, stories, frameworks that make ideas stick |
| **Objections & Myths** | Common beliefs/myths the audience holds that you can disprove |
| **Beliefs to Challenge** | Assumptions the reader has that need reframing |
| **Solutions** | What you offer in place of the myths/wrong beliefs |

### Input Types and Staging Locations

Every piece of content enters through a typed subfolder in `RAW_INTAKE/`:

```
04_KNOWLEDGE_LIBRARY/EXTRACTION_PIPELINE/RAW_INTAKE/
├── threads/      ← AI chat exports (Claude, ChatGPT, DeepSeek, Gemini)
├── books/        ← Book chapters, manuscripts, long-form IP
├── api_scrapes/  ← Structured data from APIs (JSON, CSV)
├── youtube/      ← Video transcripts
├── research/     ← Research notes, competitor analysis, market data
├── prds/         ← PRDs, screen specs, design briefs
└── general/      ← Anything that doesn't fit above
```

| Content Type | Staging Folder | Default Extraction | Typical Destination |
|---|---|---|---|
| AI chat threads | `threads/` | `thread` (EKX-1) | Pillar `01_threads/` |
| Books, chapters | `books/` | `book` | Relevant pillar or project |
| API scrapes | `api_scrapes/` | `domains` | Pillar or project |
| YouTube transcripts | `youtube/` | `domains` or `copy` | Pillar based on content |
| Research notes | `research/` | `domains` + `copy` | `PIL_21_MARKET_RESEARCH` or relevant |
| PRDs, design specs | `prds/` | `domains` + `copy` | Project `02_Product/` |
| Everything else | `general/` | `domains` | Routing scores decide |

Each input type gets routed first (via `intake_processor.py`), then the appropriate extraction runs on it. The `session_wrapup.py` script checks for unprocessed files in RAW_INTAKE at the end of every session.

### Current State
- Routing pipeline: **Implemented** (`intake_processor.py`)
- Routing keywords: **Defined** (in `DOMAIN_REGISTRY.json`)
- Routing logs: **Active** (timestamped markdown logs)
- 27 extraction domains: **Defined + Script built** (`v7_extract.py domains`)
- EKX-1 thread extraction: **Defined + Script built** (`v7_extract.py thread`)
- Copy/sales extraction: **Framework documented + Script built** (`v7_extract.py copy`)
- Book extraction: **Categories defined + Script built** (`v7_extract.py book`)
- Batch extraction: **Implemented** with checkpointing, resume, dry-run (`v7_extract.py batch`)
- API support: DeepSeek (default, cost-effective) and Claude (higher quality, higher cost)
- Extraction logs: **Active** (`03_CORE_ENGINE/ROUTING_ENGINE/extraction_logs/`)
- Copy framework physical files: **Not yet created** (9 canon docs, slot schemas, templates)

### Extraction Output Storage (Dual Copy)

Every extraction produces outputs in two places:

**Copy 1 — Alongside source file** (browse extractions in context):
```
PIL_19_PROPERTY/01_INPUT/2026-02/market_analysis.md
PIL_19_PROPERTY/01_INPUT/2026-02/market_analysis.md.extract_copy.json
PIL_19_PROPERTY/01_INPUT/2026-02/market_analysis.md.extract_copy.md
```

**Copy 2 — Central extraction store** (cross-cutting search):
```
04_KNOWLEDGE_LIBRARY/EXTRACTIONS/
├── by_mode/
│   ├── copy/2026-02/W3/market_analysis__PIL_19.extract_copy.json
│   ├── book/2026-02/W3/...
│   ├── domains/2026-02/W3/...
│   └── thread/2026-02/W3/...
├── by_category/
│   ├── usps.json             ← ALL USPs ever extracted, with provenance
│   ├── hooks.json            ← ALL hooks ever extracted
│   ├── benefits_user.json    ← ALL user benefits
│   ├── proof_points.json     ← ALL proof points
│   ├── arguments.json        ← ALL book arguments
│   ├── quotable_lines.json   ← ALL quotable lines
│   └── ...                   ← One file per category
└── EXTRACTION_INDEX.json     ← Master registry of every extraction
```

**How to search extractions:**

| Find | Where to Look |
|------|--------------|
| All copy extractions | `EXTRACTIONS/by_mode/copy/` |
| All book extractions | `EXTRACTIONS/by_mode/book/` |
| All extractions from PIL_19 | Filter `EXTRACTION_INDEX.json` by pillar |
| All extractions from February | `EXTRACTIONS/by_mode/*/2026-02/` |
| All extractions from this week | `EXTRACTIONS/by_mode/*/2026-02/W3/` |
| Every USP ever extracted | `EXTRACTIONS/by_category/usps.json` |
| Every hook ever extracted | `EXTRACTIONS/by_category/hooks.json` |
| All proofs for the book | `EXTRACTIONS/by_category/proofs.json` |
| What was extracted from a specific file | Check `.extract_*.json` next to the source file |
| Combined query (e.g. hooks from PIL_19 in Feb) | EXTRACTION_INDEX.json + by_category filter |

Each item in a `by_category/` file carries provenance: source file, pillar, project, date, extraction mode. So you can always trace any hook or USP back to where it came from.

### Script: `v7_extract.py`

```bash
# Single file extraction:
python v7_extract.py domains <file>          # 27-domain classification
python v7_extract.py thread <file>           # EKX-1 thread extraction
python v7_extract.py copy <file>             # Copy/sales extraction
python v7_extract.py book <file>             # Book extraction

# Batch extraction (checkpoints after every file):
python v7_extract.py batch <folder> --mode domains
python v7_extract.py batch <folder> --mode copy --resume    # Resume from checkpoint
python v7_extract.py batch <folder> --mode thread --ext .md # Filter by extension

# Options:
#   --api deepseek|claude    Choose API (default: deepseek)
#   --dry-run                Preview without calling API
#   --resume                 Resume batch from checkpoint
#   --output <folder>        Override output location
```

Output for each file:
- `<filename>.extract_<mode>.json` — Structured extraction data
- `<filename>.extract_<mode>.md` — Human-readable summary

### Gaps to Close
- PIL_03 canon files — 9 docs listed in index but not physically present
- Keyword matching upgrade — planned move from keyword scoring to API-based classification
- Copy formulas and templates — documented in DOCS.md but physical files not yet in subfolders

---

## 2. CONTENT ROUTING AND CLASSIFICATION

### What It Does
Decides where every piece of content belongs in the system. Routes to the correct pillar, project folder, or hold area.

### The Routing Rules

| Content Type | Goes To |
|-------------|---------|
| System governance, architecture | `00_SYSTEM_ROOT/` |
| Goals, priorities, state | `01_NAVIGATION_CENTRE/` |
| Session logs, agent work, task queue | `02_COMMAND_DECK/` |
| Scripts, indices, schemas, configs | `03_CORE_ENGINE/` |
| Raw content, extraction results | `04_KNOWLEDGE_LIBRARY/` |
| Reusable templates | `05_TEMPLATE_HUB/` |
| Domain knowledge (fits a pillar) | `06_DOMAIN_PILLARS/PIL_NN_*/` |
| Project deliverables | `07_BUILD_FACTORY/PRJ_*/` |
| Marketing, metrics, legal, finance | `08_OPERATIONS/` |
| Unknown / unsure | `04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/` |

### Within a Pillar

| Artifact Type | Subfolder |
|--------------|-----------|
| Canon (production-ready) | `00_CANON/` |
| Input threads | `01_threads/` or `01_INPUT/` |
| Extracted artifacts | `02_artifacts/` or `02_FRAMEWORKS/` |
| Schemas | `03_SCHEMAS/` |
| Prompts | `prompts/` |
| Archive | `90_ARCHIVE/` |

### Classification Scoring
`intake_processor.py` uses keyword lists from `DOMAIN_REGISTRY.json`. Each pillar has routing keywords. Content is scored against all 23 pillars. Highest score with 2+ hits wins. Below threshold goes to UNROUTED.

### Current State
- Routing manifest: **Complete** (`03_CORE_ENGINE/ROUTING_MANIFEST.md`)
- Intake processor: **Implemented** with dry-run support
- Routing logs: **Active**
- Domain registry: **Complete** with keywords for all 23 pillars

---

## 3. FILE INDEXING AND SEARCH

### Three Search Systems

| System | What It Stores | How to Search | Best For |
|--------|---------------|---------------|----------|
| **FILE_INDEX.json** | All files: path, type, pillar, size, date | Read the JSON, or use search API | Quick lookups, file existence checks |
| **PostgreSQL v7_registry** | 5,663+ files with metadata | SQL queries or search API | Structured queries, counts, reports |
| **ChromaDB** | 5,197+ vector embeddings | Semantic search via API | "Find files about [topic]" |

### FILE_INDEX.json
- Generated by `generate_indices.py`
- Lives at `03_CORE_ENGINE/INDICES/FILE_INDEX.json`
- Skips: archives, node_modules, __pycache__, .git, temp files
- Fields: path, type (extension), pillar (if in a pillar folder), size, last_modified

### PostgreSQL Registry
- Database: `enterprise_os` on localhost:5432
- Table: `v7_files`
- Updated by: `v7_registry.py` and `v7_daily.py`
- Supports: full SQL queries, JOIN with other tables, audit trail

### ChromaDB Vector Search
- Data at: `03_CORE_ENGINE/CONFIG/chromadb_data/`
- 5,197+ embeddings
- Searched via: `v7_search_api.py` on port 8100
- Endpoint: `GET /search?q=your+query`

### Search API (FastAPI)
When `v7_search_api.py` is running on port 8100:

| Endpoint | What It Does |
|----------|-------------|
| `GET /files` | Query files with filters |
| `GET /search` | Semantic search via ChromaDB |
| `GET /health` | System health summary |
| `GET /sessions` | Recent sessions |
| `GET /changes` | Audit trail |
| `GET /snapshots` | System state history |
| `GET /docs` | Interactive API documentation |

### Current State
- FILE_INDEX.json: **Implemented**
- PostgreSQL registry: **Implemented** (5,663 files)
- ChromaDB: **Implemented** (5,197 embeddings)
- Search API: **Implemented** (both port 8100 and port 5000)

---

## 4. SESSION MANAGEMENT AND CONTINUITY

### What It Does
Tracks every work session — what was done, what was created, what decisions were made — so the next session can pick up where the last one left off.

### The Session Lifecycle

```
SESSION START
  1. Read latest state snapshot (01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/)
  2. Read last session log (02_COMMAND_DECK/ACTIVE_SESSIONS/)
  3. Read SESSION_INDEX.md
  4. State context to LLM: "Last session did X. Next focus: Y."

SESSION WORK
  - Log progress with session_logger.py
  - Work in 90-120 minute blocks (2 hours max)
  - Max 3 major decisions per block
  - Save two outputs per block: full transcript + summary

SESSION END (10-step wrap-up — see OWNERS_MANUAL.md Section C for full detail)
  1. Session summary → 02_COMMAND_DECK/ACTIVE_SESSIONS/YYYY-MM/
  2. Full transcript → 04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/
  3. Verify file locations (no strays)
  4. Update FILE_INDEX.json (generate_indices.py)
  5. Update SESSION_INDEX.md
  6. Update PostgreSQL (v7_registry.py scan)
  7. Update ChromaDB (v7_registry.py chromadb-sync)
  8. Take DB snapshot (v7_registry.py snapshot)
  9. Git commit
  10. State snapshot if system state changed
```

### Session File Naming
- Session logs: `YYYY-MM-DD_session_NN.md` (NN = session number that day)
- Transcripts: `YYYY-MM-DD_session_NN_full.md`
- State snapshots: `YYYY-MM-DD.md`

### Session Summary Template
Every session summary must include:
- Focus (one-line description)
- What Got Done (numbered list)
- Key Decisions (with rationale)
- Files Created/Modified (full paths)
- Issues/Blockers
- Next Steps (checklist)
- Counts Verified (resource + count + method)

### Scripts
- `session_logger.py` — start, log, end, status, today
- `session_wrapup.py` — automated end-of-session (creates summary, transcript, updates index)

### Current State
- Session logger: **Implemented**
- Session wrap-up: **Implemented**
- SESSION_INDEX.md: **Active**
- State snapshots: **Active** (latest: 2026-02-20)

---

## 5. TEMPLATE AND SOP SYSTEM

### What It Does
Provides reusable scaffolds for every type of document, prompt, workflow, and project structure.

### Template Hub Contents (`05_TEMPLATE_HUB/`)

| Folder | Contains |
|--------|----------|
| `AGENT_TEMPLATES/` | Builder, Validator, Orchestrator agent definitions |
| `CODE_TEMPLATES/` | Code scaffolds |
| `CONTEXT_TEMPLATES/` | Context-loading templates |
| `DOCUMENT_TEMPLATES/` | Document scaffolds |
| `PLANNING_TEMPLATES/` | Goal planning session template |
| `PRD_TEMPLATES/` | Product requirements document templates |
| `PROMPT_TEMPLATES/` | Prompt templates (thread routing, etc.) |
| `SOP_TEMPLATES/` | Standard operating procedure templates |
| `WORKFLOW_TEMPLATES/` | Workflow scaffolds |
| `PILLAR_DOC_TEMPLATES.md` | Templates for pillar README, INDEX, ROUTING_RULES, CANON_STATUS |
| `PROJECT_STATE_TEMPLATE.md` | Project state tracking template |

### Pillar Document Templates
Every pillar should have 4 standard docs (templated in `PILLAR_DOC_TEMPLATES.md`):
1. **README.md** — Purpose, what belongs, folder structure, key frameworks, related pillars
2. **INDEX.md** — File listing per subfolder with status badges
3. **ROUTING_RULES.md** — Inbound/outbound/internal routing rules
4. **CANON_STATUS.md** — Production-ready, in-dev, needs-review, archived files

### PRD Screen Spec Template
Every screen in any PRD must define: route, layout code, permission level, states table, components table, modals table, features, benefits, data entities, API endpoints, S>C>E badges.

### Current State
- Template hub: **Populated** (all subfolders have content)
- Pillar doc templates: **Defined**
- PRD templates: **Defined**
- Not all pillars have their 4 standard docs yet

---

## 6. DOMAIN PILLAR KNOWLEDGE STRUCTURE

### What It Does
Organizes all knowledge into 23 specialist domains, each with its own internal structure, canon docs, routing rules, and artifact types.

### The 23 Pillars

| # | Pillar | Purpose | Status |
|---|--------|---------|--------|
| 01 | AVATARS | Customer personas, psychographics, ICPs | Empty |
| 02 | BRANDING | Visual + verbal brand identity rules | Has canon |
| 03 | COPY | Copywriting taxonomy, formulas, slot schemas | Has canon (286 files) |
| 04 | CONTENT | Content strategy, topics, distribution | Has canon |
| 05 | GRAPHICS | Visual asset systems, style recipes | Has canon |
| 06 | VIDEO | Video production workflows | Has canon |
| 07 | UI_LIBRARY | Component library (Figma to React pipeline) | Has canon (84 files) |
| 08 | KNOWLEDGE_INGESTION | How the system learns — pipelines, EKX-1 | Has canon |
| 09 | ROLES_SKILLS | Virtual workforce role definitions | Empty |
| 10 | WORKING_PRACTICES | SOPs, session protocols, workflows | Has canon |
| 11 | BUILD_STORY | Documentation of how things get built | Empty |
| 12 | KEYWORDS | Keyword research, mapping, seed lists | Has canon (68 files) |
| 13 | SEO | Technical SEO, site architecture | Has canon |
| 14 | NAVIGATION | Goals, routing logic, session management | Has canon |
| 15 | ENTERPRISE_OS | System governance, architecture, evolution | Covered by MASTER_CONTEXT |
| 16 | CONTENT_GENERATION | Automated content creation pipelines | Empty |
| 17 | RAG_SYSTEM | Chunking, embedding, retrieval config | Empty |
| 18 | AGENT_FRAMEWORK | Agent specs, task system, orchestration | Has canon (87 files, 40 roles) |
| 19 | PROPERTY | Property Connect London vertical | Has canon (173 files) |
| 20 | FITNESS | Fitness platform vertical | Has canon (590 files) |
| 21 | MARKET_RESEARCH | Research frameworks, competitor analysis | Has canon (69 files) |
| 22 | VOICE_TRAINING | Voice/speaking platform vertical | Empty |
| 23 | DOG_PLATFORM | Dog training platform vertical | Empty |

### Standard Pillar Internal Structure
```
PIL_NN_NAME/
├── 00_CANON/       → Production-ready docs (READ-ONLY without approval)
├── 01_threads/     → Source conversations and input
├── 02_artifacts/   → Extracted/processed outputs
├── 03_*            → Domain-specific subfolders (varies)
└── 90_ARCHIVE/     → Superseded content (never deleted)
```

### Pillar Dependencies
Pillars feed each other. Key dependencies:
- PIL_01 (AVATARS) depends on PIL_21 (MARKET_RESEARCH)
- PIL_02 (BRANDING) feeds PIL_03, PIL_05, PIL_07
- PIL_12 (KEYWORDS) feeds PIL_13 (SEO), PIL_04 (CONTENT)
- PIL_18 (AGENT_FRAMEWORK) depends on PIL_09 (ROLES_SKILLS)

### Current State
- All 23 pillar folders: **Exist**
- Pillar canon docs: **16 of 23 have content** (7 empty: 01, 09, 11, 16, 17, 22, 23)
- Domain registry: **Complete** with keywords, dependencies, priority levels

---

## 7. PROJECT SCAFFOLDING AND BUILD PIPELINE

### What It Does
Every project gets a standardized 9-folder structure with defined deliverables at each stage.

### The 9-Folder Project Scaffold

Every project in `07_BUILD_FACTORY/PRJ_[Name]/` uses:

| Folder | What Goes Here |
|--------|---------------|
| `01_Strategy/` | Vision, positioning, competitive analysis |
| `02_Product/` | PRDs, requirements, specifications, screen inventories |
| `03_Design/` | Design tokens, kit mappings, visual inventory, mockups |
| `04_Architecture/` | Database schemas, API design, system diagrams |
| `05_Development/` | Source code, configs, build files |
| `06_Testing/` | Test plans, test results, QA checklists |
| `07_Deployment/` | Deploy configs, CI/CD, infrastructure |
| `08_Marketing/` | Landing pages, content, campaigns, launch material |
| `90_Archive/` | Superseded files (never delete — move here) |

### Active Projects

| Project | Priority | Status |
|---------|----------|--------|
| Property Connect London | CRITICAL | PRDs done, UI kit match at 17% (needs re-run) |
| Enterprise OS Platform | CRITICAL | Infrastructure built, discipline locked in |
| UI Component Library | HIGH | COMPLETE: 40 kits, 3,633 screens, 1,785 templates, ~1,696 PNGs |
| Fitness Platform | HIGH | Befit processed, build not started |
| AI Chatbot Products | HIGH | PRD started |
| LeadEngine | MEDIUM | On hold |
| Dog Platform | LOW | Not started |
| Voice Training | LOW | Not started |

### PROJECT_STATE.md
Every project has a `PROJECT_STATE.md` file tracking:
- Vital counts (files, screens, templates, PNGs)
- Current paths (where everything lives)
- Carry-forward items (what the next session needs to know)
- Blockers and decisions pending

### Current State
- All 8 project folders: **Created**
- 9-folder scaffold: **Defined** in templates
- PROJECT_STATE.md: **Active** for main projects
- Figma pipeline: **Complete** (all extraction scripts working)

---

## 8. DATABASE SCHEMAS AND INFRASTRUCTURE

### PostgreSQL — enterprise_os / v7_registry

**Purpose:** System-wide file registry, session tracking, audit trail.

| Table | What It Stores |
|-------|---------------|
| `v7_files` | Every tracked file: path, type, pillar, size, last_modified |
| (audit tables) | Change history, session logs |

**Current:** 5,663+ files registered.

**Schema location:** `03_CORE_ENGINE/SCHEMAS/v7_registry.sql`

### PostgreSQL — ui_library

**Purpose:** UI component library catalog.

**Current:** 19,837 items across 183 kits.

**Schema location:** `03_CORE_ENGINE/SCRIPTS/schema_ui_library.sql`

### ChromaDB

**Purpose:** Vector embeddings for semantic search.

**Current:** 5,197+ embeddings.

**Data location:** `03_CORE_ENGINE/CONFIG/chromadb_data/`

### SQLite (backup)

**Purpose:** Local backup of registry data.

**Location:** `03_CORE_ENGINE/CONFIG/v7_registry.db`

---

## 9. AGENT FRAMEWORK

### What It Does
Defines virtual workforce roles that LLMs can embody during work sessions.

### The 6 Core Agents

| Agent | What It Does | Workspace |
|-------|-------------|-----------|
| Research Agent | Market research, competitive analysis | `02_COMMAND_DECK/AGENT_WORKSPACE/Research_Agent/` |
| Copy Agent | Writing copy across all formats | `02_COMMAND_DECK/AGENT_WORKSPACE/Copy_Agent/` |
| Code Agent | Development, scripting, automation | `02_COMMAND_DECK/AGENT_WORKSPACE/Code_Agent/` |
| Design Agent | UI/UX guidance, design system work | `02_COMMAND_DECK/AGENT_WORKSPACE/Design_Agent/` |
| Validator Agent | Quality control, validation, review | `02_COMMAND_DECK/AGENT_WORKSPACE/Validator_Agent/` |
| Orchestrator Agent | Coordinate multi-agent workflows | `02_COMMAND_DECK/AGENT_WORKSPACE/Orchestrator_Agent/` |

### The 40 Canonical Roles
PIL_18 (Agent Framework) defines 40 specialist roles that can be instantiated from the agent templates.

### Agent Templates
`05_TEMPLATE_HUB/AGENT_TEMPLATES/` provides three base templates:
- `builder_agent.md` — For agents that create things
- `validator_agent.md` — For agents that check things
- `orchestrator_agent.md` — For agents that coordinate things

---

## 10. GIT VERSION CONTROL AND BACKUP

### What It Does
Tracks every change to the system. Provides rollback capability when things go wrong.

### Git Workflow
- Repository root: `C:\Users\under\Downloads\ENTERPRISE_OS_V7`
- Branch: `master`
- Commit after every meaningful session
- Commit message format: `YYYY-MM-DD: Brief description of changes`

### Recovery Commands
```bash
# See recent commits:
git log --oneline -20

# See what changed in last commit:
git diff HEAD~1 --name-only

# Restore a specific file from last commit:
git checkout HEAD~1 -- path/to/file

# Restore entire system to last good state (CAREFUL — discards all changes since):
git checkout HEAD~1
```

### What's Tracked
Everything in the V7 folder except:
- `node_modules/`
- `__pycache__/`
- `.venv/`
- ChromaDB data files (too large)
- Temp files

---

## 11. THE 5A NAVIGATION FRAMEWORK

### What It Does
Provides a structured way to understand system state across 5 dimensions.

| A | Question It Answers | Where to Look |
|---|-------------------|---------------|
| **Alignment** | Why are we doing this? What are the goals? | `01_NAVIGATION_CENTRE/ACTIVE_GOALS/` |
| **Awareness** | What's the current state? What changed? | `01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/` |
| **Accountabilities** | Who owns what? What roles exist? | `02_COMMAND_DECK/AGENT_WORKSPACE/` |
| **Activities** | What's in flight? What's blocked? | `02_COMMAND_DECK/ACTIVE_SESSIONS/` |
| **Assets** | What's been created? Where is it? | `03_CORE_ENGINE/INDICES/` |

---

## 12. WHAT "FULLY OPERATIONAL" LOOKS LIKE

When this system is running at full capacity:

| Feature | Fully Operational Means |
|---------|----------------------|
| Knowledge ingestion | Any file dropped in RAW_INTAKE gets auto-routed within minutes |
| Content routing | Every file lands in the right pillar or UNROUTED — no strays |
| File indexing | FILE_INDEX.json, PostgreSQL, and ChromaDB all in sync, updated daily |
| Session management | Every session has a summary, transcript, and index entry |
| Search | Semantic search returns relevant results for any query |
| Pillar knowledge | All 23 pillars have canon docs, routing rules, and active content |
| Project builds | Every project follows the 9-folder scaffold with up-to-date PROJECT_STATE |
| Templates | Templates exist for every common document type |
| Agents | Agent roles are defined and LLMs can be given a role to work within |
| Git | Every session ends with a clean commit, rollback available |
| Health checks | Daily script runs automatically, catches stale content and broken routes |
| Databases | PostgreSQL and ChromaDB in sync, queryable via API |

### Current Gaps (as of 2026-02-20)
- 7 of 23 pillars have no canon docs
- Extraction script built (`v7_extract.py`) but not yet tested on real content
- Keyword-based routing planned for upgrade to API-based classification
- No automated daily script scheduling (run manually)
- Extraction not yet scripted into session wrap-up (manual step for now)
- Some PROJECT_STATE.md files not up to date
- Input staging paths for different content types not yet documented

---

*This document is part of the Owner's Manual suite. See also: OWNERS_MANUAL.md, RULES_AND_ENFORCEMENT.md, MAINTENANCE_DRILLS.md, PROMPT_LIBRARY.md*
