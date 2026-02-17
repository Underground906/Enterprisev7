# CLAUDE.md — Enterprise_OS V7 Context

> This file is read by Claude Code at the start of every session.
> Keep it updated. It's the system's memory.

## Session Startup Protocol (READ FIRST)

Every new chat session MUST begin by reading these files in order:

```
1. 00_SYSTEM_ROOT/V7_OPERATIONS_MANUAL.md → Foundational procedures for ALL tasks
2. 01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/  → Read the LATEST file (system-wide status)
3. 02_COMMAND_DECK/ACTIVE_SESSIONS/       → Read the LATEST session log (what happened last, what's next)
4. 04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/SESSION_INDEX.md → Session history and context
```

Then ask: "I've read the latest state. Last session covered [X]. Next session focus is [Y]. Ready to start?"

**End-of-session protocol:**
1. Save VERBATIM transcript → `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/YYYY-MM-DD_session_NN_full.md`
2. Save TOKEN-EFFICIENT summary → `02_COMMAND_DECK/ACTIVE_SESSIONS/YYYY-MM/YYYY-MM-DD_session_NN.md`
3. Update SESSION_INDEX.md with new entry
4. Update STATE_SNAPSHOTS if system-wide state changed
5. Commit to git

## V7 Quick Ops Reference (Always Loaded)

```
TASK RISKS: R/SR/AN/PL/TS=None | LG/CM=Low | W/E/RT/IG/CV/IX/BD/PU/TB=Med | D/MV/RN=HIGH(need approval)
ROUTING: Governance→00 | Goals→01 | Sessions→02 | Scripts→03 | Content→04 | Templates→05 | Domain→06 | Projects→07 | PostLaunch→08 | Unsure→04/UNROUTED
NAMES: Folders=UPPERCASE | Canon=UPPERCASE.md | Working=lowercase.md | Dated=YYYY-MM-DD_desc.md
SCAFFOLD: 01_Strategy|02_Product|03_Design|04_Architecture|05_Development|06_Testing|07_Deployment|08_Marketing|90_Archive
BEFORE WRITE: Check name+route+no-overwrite → AFTER: Verify content+index
BEFORE EDIT: Read first+check canon+backup → AFTER: Verify edit+no side effects
NEVER: Delete(archive instead) | Move/Rename without approval | Overwrite | Guess routing | Truncate | Skip checkpoints
SESSION: Start→read ops manual+state+last session | End→save verbatim+summary+update index+commit
FULL MANUAL: 00_SYSTEM_ROOT/V7_OPERATIONS_MANUAL.md
```

---

## What Is This Repo?

Enterprise_OS is a knowledge architecture and business automation platform. It's a structured folder system with 8 top-level components and 23 domain pillars, designed to store, route, index, and retrieve every piece of knowledge a business produces. Think of it as an operating system for knowledge work — not a SaaS app (yet), but the file-based backbone that makes everything else possible.

**Owner:** John  
**Stage:** Active buildout — transitioning from architecture-defined to operational  
**Primary revenue target:** Property Connect London (AI property chatbot)

## Architecture

```
ENTERPRISE_OS_V7/
├── 00_SYSTEM_ROOT/           # Governance docs, master context, naming rules
├── 01_NAVIGATION_CENTRE/     # Goals (5A framework), state snapshots, priorities
├── 02_COMMAND_DECK/          # Daily sessions, agent workspaces, task queue
├── 03_CORE_ENGINE/           # Scripts, indices, routing engine, schemas, config
├── 04_KNOWLEDGE_LIBRARY/     # Ongoing intake, extraction pipeline, RAG bundles
├── 05_TEMPLATE_HUB/          # Reusable templates for agents, docs, prompts, SOPs
├── 06_DOMAIN_PILLARS/        # 23 specialist knowledge domains (PIL_01 through PIL_23)
├── 07_BUILD_FACTORY/         # Active platform builds (PRJ_* project folders)
└── 08_OPERATIONS/            # Post-launch: marketing, metrics, legal, financial
```

## Active Goals (UPDATE DAILY)

| Priority | Goal | Target Date | Progress |
|----------|------|-------------|----------|
| 1 | Property Connect London MVP (81+ pages, visual production) | 2026-02-28 | 45% |
| 2 | Enterprise OS Platform | 2026-03-31 | 35% |
| 3 | UI Component Library | Ongoing | 80% |
| 4 | 90-Day Goal Intake (Business + Fitness + Personal) | 2026-02-14 | 0% |
| 5 | Fitness Platform PRDs + App | 2026-04-30 | 5% |

**Priority stack:** PCL > Enterprise OS > UI Library > Chatbot > Fitness > Dog > Voice

## Current Sprint

**Week of 2026-02-10:**
- Complete 90-day goal intake (business + fitness + personal combined)
- Outline all screens per build (PCL Platform MVP, client promo, customer promo)
- Identify boilerplate page layouts and kit-to-page component mapping
- Stress test system works for any LLM (not just Claude)

## How to Find Things

| What | Where |
|------|-------|
| System overview | `00_SYSTEM_ROOT/MASTER_CONTEXT.md` |
| All file locations | `03_CORE_ENGINE/INDICES/FILE_INDEX.json` |
| All pillar definitions | `03_CORE_ENGINE/INDICES/DOMAIN_REGISTRY.json` |
| Routing rules | `03_CORE_ENGINE/ROUTING_MANIFEST.md` |
| Naming conventions | `00_SYSTEM_ROOT/NAMING_CONVENTIONS.md` |
| Agent definitions | `02_COMMAND_DECK/AGENT_WORKSPACE/[Agent_Name]/AGENT.md` |
| Current state | `01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/` (latest file) |
| Templates | `05_TEMPLATE_HUB/` |

## How to Add Content

**New file from a work session:**
1. Save to `04_KNOWLEDGE_LIBRARY/EXTRACTION_PIPELINE/RAW_INTAKE/`
2. Run: `python 03_CORE_ENGINE/SCRIPTS/intake_processor.py`
3. Check: `04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/` for anything that didn't auto-route

**New file you know where it goes:**
1. Place directly in the correct pillar subfolder
2. Run: `python 03_CORE_ENGINE/SCRIPTS/generate_indices.py` to update indices

**New AI chat thread to extract:**
1. Export chat as markdown
2. Save to `04_KNOWLEDGE_LIBRARY/EXTRACTION_PIPELINE/RAW_INTAKE/`
3. Run: `python 03_CORE_ENGINE/SCRIPTS/ingestors/thread_ingester.py [filename]`

## How to Log Work

```bash
# Start a work session
python 03_CORE_ENGINE/SCRIPTS/session_logger.py start "Building property chatbot MVP"

# Log progress during session
python 03_CORE_ENGINE/SCRIPTS/session_logger.py log "Completed React chat component"

# End session
python 03_CORE_ENGINE/SCRIPTS/session_logger.py end
```

## How to Manage Goals

```bash
# List current goals
python 03_CORE_ENGINE/SCRIPTS/goal_tracker.py list

# Update goal progress
python 03_CORE_ENGINE/SCRIPTS/goal_tracker.py update "Property Connect London" --progress 30

# Create daily snapshot
python 03_CORE_ENGINE/SCRIPTS/goal_tracker.py snapshot
```

## Rules for Claude Code

### MUST DO
- Always update `FILE_INDEX.json` after creating or moving files
- Log all routing decisions to `03_CORE_ENGINE/ROUTING_ENGINE/routing_logs/`
- Use naming convention: `YYYY-MM-DD_descriptive_name.ext`
- Follow the pillar subfolder structure (00_CANON, 01_INPUT, 02_*, etc.)
- Commit to git after completing a meaningful unit of work
- Read the relevant pillar's `00_CANON/README.md` before working in that pillar

### MUST NOT
- Never edit files in `00_CANON/` without explicit user confirmation
- Never delete files — move to `90_ARCHIVE/` instead
- Never guess a routing destination — use `UNROUTED/` if unsure
- Never modify `RAG_BUNDLES/V7_ARCHIVE/` — it's read-only historical reference
- Never create files outside the V7 folder structure

### SHOULD DO
- Cross-reference related content across pillars
- Flag stale content (last modified > 30 days in fast-changing pillars)
- Suggest improvements to canon docs when you notice gaps
- Batch similar operations for efficiency
- Use templates from `05_TEMPLATE_HUB/` when creating new docs

## Domain Pillar Quick Reference

| ID | Name | Purpose | Canon Status |
|----|------|---------|-------------|
| 01 | AVATARS | Customer personas, psychographics, ICPs | ❌ Empty |
| 02 | BRANDING | Visual + verbal brand identity rules | ✅ Has DOCS.md |
| 03 | COPY | Copywriting taxonomy, formulas, slot schemas | ✅ Has DOCS.md |
| 04 | CONTENT | Content strategy, topics, distribution plans | ✅ Has DOCS.md |
| 05 | GRAPHICS | Visual asset systems, style recipes | ✅ Has DOCS.md |
| 06 | VIDEO | Video production workflows | ✅ Has DOCS.md |
| 07 | UI_LIBRARY | Component library (Figma→React pipeline) | ✅ Has DOCS.md |
| 08 | KNOWLEDGE_INGESTION | How the system learns — pipelines, EKX-1 | ✅ Has README + MASTER_SYSTEM + CONTEXT |
| 09 | ROLES_SKILLS | Virtual workforce role definitions | ❌ Empty |
| 10 | WORKING_PRACTICES | SOPs, session protocols, workflows | ✅ Has README + CONTEXT + ANALYSIS |
| 11 | BUILD_STORY | Documentation of how things get built | ❌ Empty |
| 12 | KEYWORDS | Keyword research, mapping, seed lists | ✅ Has DOCS.md |
| 13 | SEO | Technical SEO, site architecture | ✅ Has DOCS.md |
| 14 | NAVIGATION | Goals, routing logic, session management | ✅ Has README + CONTEXT + ANALYSIS + ROUTING_RULES |
| 15 | ENTERPRISE_OS | System governance, architecture, evolution | ❌ Empty (MASTER_CONTEXT covers this) |
| 16 | CONTENT_GENERATION | Automated content creation pipelines | ❌ Empty |
| 17 | RAG_SYSTEM | Chunking, embedding, retrieval config | ❌ Empty |
| 18 | AGENT_FRAMEWORK | Agent specs, task system, orchestration | ✅ Has DOCS.md |
| 19 | PROPERTY | Property Connect London vertical | ✅ Has DOCS.md |
| 20 | FITNESS | Fitness platform vertical | ✅ Has DOCS.md |
| 21 | MARKET_RESEARCH | Research frameworks, competitor analysis | ✅ Has DOCS.md |
| 22 | VOICE_TRAINING | Voice/speaking platform vertical | ❌ Empty |
| 23 | DOG_PLATFORM | Dog training platform vertical | ❌ Empty |

## 27 Extraction Domains (Reference)

When processing any content, it can be categorised across these extraction domains:
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

## Tech Stack

- **Language:** Python 3.11+ for all scripts
- **CLI:** Click for command-line tools
- **Vector Store:** ChromaDB (local development)
- **LLM:** Claude API for classification and extraction
- **VCS:** Git + GitHub
- **Frontend (future):** Next.js + React
- **Database (future):** Supabase/PostgreSQL
