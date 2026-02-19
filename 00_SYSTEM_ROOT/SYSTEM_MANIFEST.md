# SYSTEM MANIFEST — Enterprise OS V7

> **READ THIS FIRST. EVERY SESSION. NO EXCEPTIONS.**
> This is the master routing document. It tells you what the system is, where everything lives, what rules to follow, and what to read next based on what work you're doing.
> **Last updated:** 2026-02-19

---

## DAILY STARTUP CHECKLIST

Do these in order. Every session. No shortcuts.

```
STEP 1: LOAD RULES
  Read: 00_SYSTEM_ROOT/SYSTEM_MANIFEST.md (this file)
  Read: 00_SYSTEM_ROOT/V7_OPERATIONS_MANUAL.md (Sections 1-2 minimum)
  State to user: "Rules loaded. Ready for project context."

STEP 2: LOAD LAST SESSION
  Read: 02_COMMAND_DECK/ACTIVE_SESSIONS/2026-MM/ → LATEST file
  Read: 01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/ → LATEST file
  If working on a specific project:
    Read: 07_BUILD_FACTORY/PRJ_{name}/PROJECT_STATE.md
  State to user: "Last session: [X]. Project state: [Y]."

STEP 3: LOAD GOALS & PRIORITIES
  Read: 01_NAVIGATION_CENTRE/ACTIVE_GOALS/GOALS_90DAY.md
  Read: 01_NAVIGATION_CENTRE/ACTIVE_GOALS/GOALS_6WEEK.md
  Check: What milestones are due this week? What constraints/blockers exist?
  State to user: "Current priorities: [list]. Blockers: [list]."

STEP 4: PLAN THE BLOCK
  Ask user: What project/task are we working on?
  Check: Does this task have a plan or mini-PRD already?
  Define: What are the outputs? Where do they get stored?
  Define: What quality standards apply?
  Define: What counts need tracking?
  State to user: "Block plan: [task], outputs to [path], quality checks [X]."

STEP 5: WORK IN RULES
  Follow V7_OPERATIONS_MANUAL procedures for the task type
  Follow the PROJECT_STATE.md constraints for that project
  Checkpoint after every batch operation
  Count before AND after every operation
  Never delete, move, or rename without explicit approval

STEP 6: CLOSE THE BLOCK
  Update PROJECT_STATE.md with: what was done, new counts, carry-forward
  Save session summary to Command Deck
  Save full transcript to Knowledge Library
  Update SESSION_INDEX.md
  Commit to git
```

---

## WHAT IS ENTERPRISE OS V7?

A knowledge architecture and business automation platform. 8 top-level components, 23 domain pillars, serving multiple revenue-generating platforms.

**Owner:** John
**Brand green:** #0B8C00 | **Alt green:** #49ba61
**Fonts:** Inter (apps/dashboards), DM Sans (website/landing)

### The 8 Components (Body Metaphor)

| # | Component | Metaphor | Purpose |
|---|-----------|----------|---------|
| 00 | SYSTEM_ROOT | DNA | Governance, naming, architecture, THIS manifest |
| 01 | NAVIGATION_CENTRE | Brain | Goals, priorities, state, decisions |
| 02 | COMMAND_DECK | Hands | Sessions, agent workspaces, task queue |
| 03 | CORE_ENGINE | Nerves | Scripts, indices, routing, schemas, config |
| 04 | KNOWLEDGE_LIBRARY | Stomach | Content intake, extraction, archives, RAG |
| 05 | TEMPLATE_HUB | DNA Templates | Reusable templates for docs, prompts, SOPs |
| 06 | DOMAIN_PILLARS | Organs | 23 specialist knowledge domains |
| 07 | BUILD_FACTORY | Kinetic Limbs | Active project builds (PRJ_*) |
| 08 | OPERATIONS | Immune System | Post-launch marketing, metrics, legal |

### The 23 Domain Pillars

```
PIL_01_AVATARS        PIL_02_BRANDING       PIL_03_COPY
PIL_04_CONTENT        PIL_05_GRAPHICS       PIL_06_VIDEO
PIL_07_UI_LIBRARY     PIL_08_KNOWLEDGE      PIL_09_ROLES_SKILLS
PIL_10_WORKING_PRAC   PIL_11_BUILD_STORY    PIL_12_KEYWORDS
PIL_13_SEO            PIL_14_NAVIGATION     PIL_15_ENTERPRISE_OS
PIL_16_CONTENT_GEN    PIL_17_RAG_SYSTEM     PIL_18_AGENT_FRAMEWORK
PIL_19_PROPERTY       PIL_20_FITNESS        PIL_21_MARKET_RESEARCH
PIL_22_VOICE          PIL_23_DOG_PLATFORM
```

**NEVER invent new pillar names. Use ONLY these 23.**

---

## ACTIVE PROJECTS

Each project has a `PROJECT_STATE.md` in its Build Factory folder. Read that file when working on that project.

| Project | Folder | Priority | Status |
|---------|--------|----------|--------|
| Property Connect London | PRJ_Property_Connect_London | 1 - CRITICAL | PRDs done, screens specced, UI matching started |
| Enterprise OS Platform | PRJ_Enterprise_Platform | 2 - CRITICAL | Infrastructure built, system discipline in progress |
| UI Component Library | PRJ_UI_Component_Library | 3 - HIGH | 5-phase pipeline proven, 5 kits processed, 35 more pending |
| Fitness Platform | PRJ_Fitness_Platform | 4 - HIGH | Befit kit processed, PRD exists, build not started |
| LeadEngine Platform | PRJ_LeadEngine_Platform | 5 - MEDIUM | Full spec done, deprioritized until library complete |
| AI Chatbot Products | PRJ_AI_Chatbot_Products | 6 - MEDIUM | Spec exists, no build work |
| Voice Training | PRJ_Voice_Training | 7 - LOW | Empty shell |
| Dog Platform | PRJ_Dog_Platform | 8 - LOW | Empty shell |

---

## WHERE TO FIND THINGS

### System Docs (read every session)
| Doc | Location | Purpose |
|-----|----------|---------|
| THIS MANIFEST | `00_SYSTEM_ROOT/SYSTEM_MANIFEST.md` | Master routing doc |
| Operations Manual | `00_SYSTEM_ROOT/V7_OPERATIONS_MANUAL.md` | Task procedures, QA checklists |
| Master Context | `00_SYSTEM_ROOT/MASTER_CONTEXT.md` | Full architecture (deep work only) |
| Naming Conventions | `00_SYSTEM_ROOT/NAMING_CONVENTIONS.md` | File/folder naming rules |

### Navigation (goals & state)
| Doc | Location | Purpose |
|-----|----------|---------|
| 90-Day Goals | `01_NAVIGATION_CENTRE/ACTIVE_GOALS/GOALS_90DAY.md` | Long-term outcomes |
| 6-Week Milestones | `01_NAVIGATION_CENTRE/ACTIVE_GOALS/GOALS_6WEEK.md` | Medium-term targets |
| State Snapshots | `01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/` | System-wide status (latest file) |

### Sessions & History
| Doc | Location | Purpose |
|-----|----------|---------|
| Session Summaries | `02_COMMAND_DECK/ACTIVE_SESSIONS/YYYY-MM/` | Quick session logs |
| Full Transcripts | `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/` | Verbatim records |
| Session Index | `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/SESSION_INDEX.md` | Master session list |
| Weekly Rollups | `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/YYYY-WNN_weekly.md` | Week summaries |

### Indices & Data
| Doc | Location | Purpose |
|-----|----------|---------|
| File Index | `03_CORE_ENGINE/INDICES/FILE_INDEX.json` | All tracked files |
| Domain Registry | `03_CORE_ENGINE/INDICES/DOMAIN_REGISTRY.json` | Pillar definitions |
| Kit Inventories | `03_CORE_ENGINE/INDICES/kit_inventories/` | 30 UI kit inventories |
| Consolidation Plan | `03_CORE_ENGINE/INDICES/CONSOLIDATION_PLAN.md` | 1,126 external files |

### Databases
| Database | Location | Contents |
|----------|----------|----------|
| PostgreSQL `ui_library` | localhost:5432 | 19,837 items, 183 kits |
| PostgreSQL `v7_registry` | localhost:5432 | 5,663 files registered |
| ChromaDB | `03_CORE_ENGINE/CONFIG/chromadb_data/` | 5,197 embeddings |

### Project State Sheets
| Project | Location |
|---------|----------|
| UI Library | `07_BUILD_FACTORY/PRJ_UI_Component_Library/PROJECT_STATE.md` |
| Property Connect | `07_BUILD_FACTORY/PRJ_Property_Connect_London/PROJECT_STATE.md` |
| Fitness | `07_BUILD_FACTORY/PRJ_Fitness_Platform/PROJECT_STATE.md` |
| Enterprise Platform | `07_BUILD_FACTORY/PRJ_Enterprise_Platform/PROJECT_STATE.md` |

---

## THE RULES (NON-NEGOTIABLE)

### File Operations
- **NEVER** delete files. Archive to `90_ARCHIVE/` instead.
- **NEVER** move or rename files without explicit approval.
- **NEVER** overwrite existing files. Use `_v2`, `_new`, or timestamp suffix.
- **NEVER** put outputs in root folders. Use designated subfolders.
- **NEVER** create temp files in data folders.

### Counting & Data Integrity
- Count BEFORE and AFTER every operation.
- If counts don't match, STOP and investigate. Don't paper over it.
- Cache counts at session start. If they change, explain why.
- Checkpoint after EVERY batch item, not every 5 or 10.

### Pillar & Naming
- Use ONLY the canonical 23 pillar names.
- Follow `00_SYSTEM_ROOT/NAMING_CONVENTIONS.md` for all files.
- Folders = UPPERCASE, Canon docs = UPPERCASE.md, Working docs = lowercase.md

### Session Discipline
- Work in 90-120 minute blocks (2 hours max).
- Save outputs at block end (summary + transcript + index update).
- Update the PROJECT_STATE.md for whatever project was touched.
- Commit to git after each block.

### Fast Session Wrap-Up (< 3 Minutes)

**Script:** `03_CORE_ENGINE/SCRIPTS/session_wrapup.py`

```bash
# Quick (one command, auto-commit):
python 03_CORE_ENGINE/SCRIPTS/session_wrapup.py --quick -s "Summary here" -p "Project1,Project2"

# Interactive (prompts for everything):
python 03_CORE_ENGINE/SCRIPTS/session_wrapup.py
```

**What it does automatically:**
1. Creates session summary → `02_COMMAND_DECK/ACTIVE_SESSIONS/YYYY-MM/`
2. Creates transcript → `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/`
3. Updates `SESSION_INDEX.md` with new row
4. Updates `PROJECT_STATE.md` session links for each project touched
5. Git add, commit, push

**Human guide:** `C:\Users\under\Documents\V7_DAILY_GUIDE.md`

### Quality Checks
- Before writing: check name, route, no-overwrite.
- After writing: verify content, update index.
- Before editing: read first, check if canon, backup if needed.
- After editing: verify edit, check for side effects.

---

## WORKING PRACTICES

### John's Constraints (Respect These)
- Works in 2-hour blocks, max 3 decisions per block
- Gets into anxiety spirals with 20-hour unstructured sessions
- Health & fitness is a personal imperative — must exercise daily
- Prefers structured work with clear outputs per block
- Gets frustrated by context loss, wrong counts, and repeated work

### The 5A Framework
| A | Purpose | Where |
|---|---------|-------|
| Alignment | Why are we doing this? Business goals. | 01_NAVIGATION_CENTRE/ACTIVE_GOALS/ |
| Awareness | What's the current state? What happened? | 01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/ |
| Accountabilities | Who owns what? What are the roles? | 02_COMMAND_DECK/AGENT_WORKSPACE/ |
| Activities | What tasks are in flight? What's blocked? | 02_COMMAND_DECK/ACTIVE_SESSIONS/ |
| Assets | What's been created? Where does it live? | 03_CORE_ENGINE/INDICES/ |

### Constraint-First Planning
When planning a block:
1. What CONSTRAINTS exist? (blocked tasks, missing data, dependencies)
2. Which constraint can we REMOVE today?
3. What's the MINIMUM OUTPUT that removes that constraint?
4. What QUALITY CHECK proves it's done?

---

## WEEKLY ROLLUP PROCESS

**Every Saturday or Sunday:**

1. Read all session summaries from the week
2. Create `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/YYYY-WNN_weekly.md` containing:
   - Per-project: what was done, what changed, locked counts
   - Decisions made and their rationale
   - Outstanding carry-forward work
   - Updated blocked/dependency status
3. Update `01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/` with fresh snapshot
4. Update `01_NAVIGATION_CENTRE/ACTIVE_GOALS/` progress
5. Copy week's files to `04_KNOWLEDGE_LIBRARY/DEEPSEEK_REVIEW/YYYY-WNN/` for external review
6. Commit everything

**Monthly (last day of month):**
- Roll up weekly summaries into monthly
- Archive completed project milestones
- Update all PROJECT_STATE.md files
- Full system health check

---

## DOCUMENT HIERARCHY (4 Tiers)

```
TIER 1: MAINFRAME (read EVERY session)
├── SYSTEM_MANIFEST.md         ← THIS FILE (routes everything)
├── V7_OPERATIONS_MANUAL.md    ← How to do tasks
├── Latest State Snapshot      ← System status
├── Latest Session Summary     ← What happened last

TIER 2: PROJECT STATE (read when working on THAT project)
├── PRJ_*/PROJECT_STATE.md     ← Vital paths, counts, databases, carry-forward
├── PRJ_*/02_Product/*.md      ← PRDs for that project

TIER 3: RULES & PROCEDURES (read when doing THAT type of work)
├── NAMING_CONVENTIONS.md      ← File naming
├── ROUTING_MANIFEST.md        ← Where files go
├── V7_OPERATIONS_MANUAL.md    ← (specific sections for task type)

TIER 4: DOMAIN KNOWLEDGE (read when working in THAT area)
├── PIL_*/00_CANON/            ← Pillar canon docs
├── 01_Strategy/ docs          ← Project strategy docs
├── Build methodology docs     ← (e.g., UI_LIBRARY_BUILD_METHODOLOGY.md)
```

---

## AD-HOC TASK HANDLING

Tasks pop up daily that aren't in any plan. Handle them like this:

1. **Classify:** Is this a blocker for a current goal? A new requirement? A nice-to-have?
2. **If blocker:** Do it now. It's removing a constraint.
3. **If new requirement:** Log it in the PROJECT_STATE.md carry-forward section.
4. **If nice-to-have:** Log it in `02_COMMAND_DECK/TASK_QUEUE/` and revisit during planning.
5. **Always:** Record what was done and why in the session summary.

---

## FOR JOHN (Human-Readable Quick Reference)

### What to give any new LLM session:
```
"Read 00_SYSTEM_ROOT/SYSTEM_MANIFEST.md, then read the latest file in
02_COMMAND_DECK/ACTIVE_SESSIONS/2026-02/ and the PROJECT_STATE.md for
[project name]. Then tell me what you understand."
```

### What to review yourself:
- **Daily:** Check the session summary from yesterday
- **Weekly:** Read the weekly rollup
- **When switching projects:** Read that project's PROJECT_STATE.md
- **When frustrated:** Read this manifest to re-orient

### Your docs vs LLM docs:
- LLM reads: SYSTEM_MANIFEST.md, V7_OPERATIONS_MANUAL.md, PROJECT_STATE.md, session logs
- You review: Weekly rollups, DeepSeek review folders, PROJECT_STATE.md (same one), goal progress

---

*This document is the root of the system. Update it when the system changes. Every LLM, every session, starts here.*
