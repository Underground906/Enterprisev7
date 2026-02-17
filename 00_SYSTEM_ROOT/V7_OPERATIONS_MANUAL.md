# V7 OPERATIONS MANUAL

> **Version:** 1.0
> **Date:** 2026-02-17
> **Purpose:** Foundational operating procedures for ALL interactions with Enterprise OS V7. Every task, every component, every LLM session follows this document.
> **Authority:** This document is CANONICAL. It overrides ad-hoc decisions. Update it — don't ignore it.

---

## 0. HOW TO USE THIS DOCUMENT

**At session start:** Read Section 1 (Session Protocol) and Section 2 (Task Taxonomy — just the table).
**Before any task:** Find the task type in Section 2, follow its procedure in Section 3.
**Before touching any component:** Check Section 4 for that component's rules.
**Before creating any file:** Check Section 5 (Naming) and Section 6 (Routing).
**After any operation:** Run the QA checklist in Section 7.
**If something goes wrong:** Section 8 (Error Recovery).

---

## 1. SESSION PROTOCOL

### 1.1 Session Start (Every New Chat)

```
STEP 1: Read 01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/ → latest file
STEP 2: Read 02_COMMAND_DECK/ACTIVE_SESSIONS/ → latest session log
STEP 3: Read 04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/SESSION_INDEX.md
STEP 4: State to user: "Last session: [X]. Next focus: [Y]. Ready?"
```

### 1.2 During Session

- Work in 90-120 minute blocks (4-5 blocks per day)
- At EACH block end, save TWO outputs:
  1. **Verbatim transcript** → `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/YYYY-MM-DD_session_NN_full.md`
  2. **Token-efficient summary** → `02_COMMAND_DECK/ACTIVE_SESSIONS/YYYY-MM/YYYY-MM-DD_session_NN.md`
- Update `SESSION_INDEX.md` with new entry after each save

### 1.3 Session End

```
STEP 1: Save verbatim transcript (full conversation)
STEP 2: Save summary (key decisions, files created/modified, next steps)
STEP 3: Update SESSION_INDEX.md
STEP 4: Update STATE_SNAPSHOTS if system-wide state changed
STEP 5: Commit to git with descriptive message
```

### 1.4 Context Preservation

- CLAUDE.md files are auto-loaded every session (never compressed)
- V7_OPERATIONS_MANUAL.md should be READ at session start
- If session runs >90 minutes, re-read this manual's QA checklist before continuing

---

## 2. TASK TAXONOMY

Every interaction with V7 falls into one of these task types:

| Code | Task Type | Description | Risk Level |
|------|-----------|-------------|------------|
| `R` | **READ** | View file contents, check status, inspect structure | None |
| `W` | **WRITE** | Create new files from scratch | Medium |
| `E` | **EDIT** | Modify existing file contents | Medium |
| `D` | **DELETE** | Remove files (actually: move to 90_ARCHIVE) | HIGH |
| `MV` | **MOVE** | Relocate files between folders | HIGH |
| `RN` | **RENAME** | Change file or folder names | HIGH |
| `RT` | **ROUTE** | Decide where content belongs in V7 structure | Medium |
| `IG` | **INGEST** | Process raw input into V7-compatible format | Medium |
| `CV` | **CONVERT** | Transform between formats (MD→JSON, Figma→React, etc.) | Medium |
| `IX` | **INDEX** | Update FILE_INDEX.json, DOMAIN_REGISTRY, or other indices | Medium |
| `LG` | **LOG** | Record session activity, routing decisions, changes | Low |
| `CM` | **COMMIT** | Git add + commit | Low |
| `PU` | **PUSH** | Git push to remote | Medium |
| `BD` | **BUILD** | Create project deliverables (code, designs, docs) | Medium |
| `TS` | **TEST** | Verify functionality, run scripts, validate outputs | Low |
| `TB` | **TROUBLESHOOT** | Diagnose and fix issues | Medium |
| `PL` | **PLAN** | Design approach before executing | None |
| `AN` | **ANALYSE** | Research, compare, summarize existing content | None |
| `SR` | **SEARCH** | Find files, content, or information within V7 | None |

### Risk Levels

| Level | Meaning | Protocol |
|-------|---------|----------|
| None | Read-only, no side effects | Proceed freely |
| Low | Minor side effects, easily reversible | Proceed, log the action |
| Medium | Creates or modifies files | Announce intent, proceed, verify after |
| HIGH | Destructive or hard to reverse | **MUST get explicit user approval before executing** |

---

## 3. TASK PROCEDURES

### 3.1 READ (`R`)

```
1. Identify target file/folder path
2. Verify path exists before reading
3. If reading a pillar, check 00_CANON/README.md first
4. Report contents to user
```

**QA:** Did you read the right file? Did you read ALL of it (no truncation)?

---

### 3.2 WRITE (`W`) — Create New File

```
1. Determine file type (canon, working, date-based)
2. Apply naming convention (Section 5)
3. Determine destination using routing table (Section 6)
4. Verify destination folder exists
5. Verify NO existing file at target path (never overwrite)
6. Write the file
7. Log: "CREATED: [path]"
8. Update FILE_INDEX.json if it exists
```

**QA Checklist:**
- [ ] Naming follows Section 5 conventions?
- [ ] File is in the correct component/pillar/project folder?
- [ ] No existing file was overwritten?
- [ ] FILE_INDEX.json updated?
- [ ] Content complete (not truncated)?

---

### 3.3 EDIT (`E`) — Modify Existing File

```
1. READ the file first (mandatory — never edit blind)
2. State what you intend to change and why
3. If file is in 00_CANON/ → STOP, get user approval
4. Create backup: filename_BACKUP_YYYYMMDD.ext (if significant edit)
5. Make the edit
6. Verify the edit took effect (re-read the section)
7. Log: "EDITED: [path] — [what changed]"
```

**QA Checklist:**
- [ ] Read the file before editing?
- [ ] Not editing a 00_CANON file without approval?
- [ ] Backup created for significant edits?
- [ ] Edit verified (re-read)?

---

### 3.4 DELETE (`D`) — Remove File

**⚠️ V7 DOES NOT DELETE FILES. It archives them.**

```
1. STOP — confirm user explicitly requested this
2. State the file(s) to be archived and get approval
3. Move file to nearest 90_ARCHIVE/ folder (preserve original name)
4. Log: "ARCHIVED: [original_path] → [archive_path]"
5. Update FILE_INDEX.json
```

**QA:** User explicitly approved? File moved (not deleted)? Index updated?

---

### 3.5 MOVE (`MV`) — Relocate File

```
1. STOP — confirm user explicitly requested this
2. State: source path, destination path, reason
3. Get user approval
4. Verify destination folder exists
5. Verify no naming conflict at destination
6. Move the file
7. Log: "MOVED: [from] → [to]"
8. Update FILE_INDEX.json
```

---

### 3.6 RENAME (`RN`) — Rename File or Folder

```
1. STOP — confirm user explicitly requested this
2. State: current name → proposed new name, reason
3. Verify new name follows naming conventions (Section 5)
4. Get user approval
5. Rename
6. Log: "RENAMED: [old] → [new]"
7. Update FILE_INDEX.json
8. Check for broken references in other files
```

---

### 3.7 ROUTE (`RT`) — Decide Content Destination

```
1. Read the content to understand its nature
2. Classify against the 27 extraction domains (see CLAUDE.md)
3. Map to primary component (Section 4 routing table)
4. Map to primary pillar if applicable (Section 4.7)
5. If UNSURE → route to 04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/
6. Log routing decision to 03_CORE_ENGINE/ROUTING_ENGINE/routing_logs/
7. State: "Routed [file] to [destination] because [reason]"
```

**QA:** Did you log the routing decision? If unsure, did you use UNROUTED (not guess)?

---

### 3.8 INGEST (`IG`) — Process Raw Input

```
1. Place raw file in 04_KNOWLEDGE_LIBRARY/EXTRACTION_PIPELINE/RAW_INTAKE/
2. Identify content type (chat thread, document, data file, media)
3. Extract structured information (EKX-1 methodology if applicable)
4. Route extracted content to appropriate locations (use ROUTE procedure)
5. Move raw file to PROCESSED/ after extraction
6. Log: "INGESTED: [filename] → [N] artifacts extracted → [destinations]"
```

**QA:** Raw file preserved? All artifacts routed? Processing logged?

---

### 3.9 CONVERT (`CV`) — Format Transformation

```
1. Identify source format and target format
2. Read source file completely (no truncation)
3. Apply conversion (MD→JSON, Figma→React, etc.)
4. Write output to appropriate location
5. Verify output is complete and valid
6. Log: "CONVERTED: [source] ([format]) → [output] ([format])"
```

**QA:** Source preserved? Output complete? Output valid (parseable if JSON, renderable if HTML)?

---

### 3.10 INDEX (`IX`) — Update System Indices

```
1. Identify which index needs updating (FILE_INDEX.json, DOMAIN_REGISTRY.json, etc.)
2. Read current index
3. Count entries BEFORE
4. Make additions/modifications
5. Count entries AFTER
6. State: "INDEX UPDATED: [index_name] — [before_count] → [after_count] entries"
7. Verify counts make sense (additions should increase count, not decrease)
```

**QA:** Before and after counts stated? Counts make sense? No entries lost?

---

### 3.11 LOG (`LG`) — Record Activity

```
1. Determine log type:
   - Session log → 02_COMMAND_DECK/ACTIVE_SESSIONS/
   - Routing log → 03_CORE_ENGINE/ROUTING_ENGINE/routing_logs/
   - Build log → 07_BUILD_FACTORY/PRJ_*/relevant_subfolder/
2. Append to existing log or create date-stamped new one
3. Include: timestamp, action taken, files affected, outcome
```

---

### 3.12 COMMIT (`CM`) and PUSH (`PU`) — Git Operations

```
COMMIT:
1. git status — review what's staged and unstaged
2. Stage specific files (NOT git add -A or git add .)
3. Write descriptive commit message
4. Commit
5. Verify: git log --oneline -1

PUSH:
1. Only if user explicitly requests
2. Confirm branch and remote
3. Push
4. Verify: git status shows up-to-date
```

---

### 3.13 BUILD (`BD`) — Create Project Deliverables

```
1. Identify target project (PRJ_*)
2. Read project's existing docs (01_Strategy and 02_Product first)
3. Identify which scaffold folder the deliverable belongs in
4. Follow that project's established patterns
5. Create deliverable in correct scaffold folder
6. Log progress
```

**Project Scaffold (9-folder structure):**

| Folder | Contains | Key Files |
|--------|----------|-----------|
| `01_Strategy/` | Vision, positioning, competitive analysis, market research | STRATEGY.md, COMPETITIVE_ANALYSIS.md |
| `02_Product/` | PRDs, requirements, specifications, screen inventories | PRD_*.md, SCREEN_INVENTORY.md |
| `03_Design/` | Design tokens, kit mappings, visual inventory, mockups | KIT_INDEX.json, DESIGN_TOKENS.json |
| `04_Architecture/` | Database schemas, API design, system diagrams | SCHEMA.sql, API_SPEC.md |
| `05_Development/` | Source code, configs, build files | App source code |
| `06_Testing/` | Test plans, test results, QA checklists | TEST_PLAN.md |
| `07_Deployment/` | Deploy configs, CI/CD, infrastructure | docker-compose.yml |
| `08_Marketing/` | Landing pages, content, campaigns, launch material | LAUNCH_PLAN.md |
| `90_Archive/` | Superseded files (never delete, archive here) | Previous versions |

---

### 3.14 TEST (`TS`) — Verify & Validate

```
1. Identify what's being tested (script, component, data integrity)
2. Define expected outcome BEFORE running
3. Run test
4. Compare actual vs expected
5. Report: PASS/FAIL with specifics
```

---

### 3.15 TROUBLESHOOT (`TB`) — Diagnose & Fix

```
1. Reproduce the problem — confirm it exists
2. Read relevant files/logs
3. Identify root cause (not just symptoms)
4. Propose fix to user
5. Get approval before applying fix
6. Apply fix
7. Verify fix resolved the issue
8. Log what happened and how it was fixed
```

---

### 3.16 PLAN (`PL`) — Design Approach

```
1. Read all relevant existing docs
2. Identify constraints and dependencies
3. Propose approach with clear steps
4. State trade-offs and alternatives
5. Get user approval before execution
```

---

### 3.17 ANALYSE (`AN`) — Research & Summarize

```
1. Define scope — what are we analysing?
2. Read all relevant files (completely, no truncation)
3. Cross-reference across components/pillars
4. Present findings in structured format
5. Route output to appropriate location
```

---

## 4. COMPONENT RULES

### 4.1 00_SYSTEM_ROOT — Governance

| Action | Rule |
|--------|------|
| READ | Always allowed |
| WRITE | Only governance docs, naming rules, this manual |
| EDIT | Requires user approval (these are canonical) |
| What lives here | MASTER_CONTEXT.md, NAMING_CONVENTIONS.md, V7_OPERATIONS_MANUAL.md, CLAUDE.md |

---

### 4.2 01_NAVIGATION_CENTRE — Goals & State

| Action | Rule |
|--------|------|
| READ | Always allowed |
| WRITE | State snapshots, goal definitions |
| EDIT | Goal updates, snapshot amendments |
| What lives here | STATE_SNAPSHOTS/, GOALS/, 5A framework documents |

**Special rule:** State snapshots are append-only. Create new snapshots, don't edit old ones.

---

### 4.3 02_COMMAND_DECK — Sessions & Tasks

| Action | Rule |
|--------|------|
| READ | Always allowed |
| WRITE | Session logs, task assignments |
| EDIT | Current session log only (don't edit past sessions) |
| What lives here | ACTIVE_SESSIONS/, AGENT_WORKSPACE/, TASK_QUEUE/ |

**Special rule:** Session logs follow format: `YYYY-MM-DD_session_NN.md`

---

### 4.4 03_CORE_ENGINE — Scripts & Config

| Action | Rule |
|--------|------|
| READ | Always allowed |
| WRITE | New scripts, index files, configs |
| EDIT | Scripts (with testing), configs (with backup) |
| What lives here | SCRIPTS/, INDICES/, ROUTING_ENGINE/, SCHEMAS/, CONFIG/ |

**Special rule:** Always test scripts after editing. Always backup configs before editing.

---

### 4.5 04_KNOWLEDGE_LIBRARY — Content Pipeline

| Action | Rule |
|--------|------|
| READ | Always allowed |
| WRITE | Ingested content, extraction outputs, session archives |
| EDIT | Rarely — prefer creating new versions |
| What lives here | EXTRACTION_PIPELINE/, ONGOING/, RAG_BUNDLES/, SESSION_ARCHIVE/ |

**Special rules:**
- RAG_BUNDLES/V7_ARCHIVE/ is READ-ONLY (historical reference)
- Raw intake goes to EXTRACTION_PIPELINE/RAW_INTAKE/
- Unclassified content goes to ONGOING/UNROUTED/

---

### 4.6 05_TEMPLATE_HUB — Reusable Templates

| Action | Rule |
|--------|------|
| READ | Always allowed — check here BEFORE creating any standard doc |
| WRITE | New templates (only if no existing template fits) |
| EDIT | With user approval (templates affect all future docs) |
| What lives here | Document templates, prompt templates, SOP templates |

---

### 4.7 06_DOMAIN_PILLARS — 23 Knowledge Domains

| Action | Rule |
|--------|------|
| READ | Always allowed — read 00_CANON/README.md FIRST for any pillar work |
| WRITE | New pillar content in appropriate subfolder |
| EDIT | Working docs freely; 00_CANON/ requires user approval |
| What lives here | PIL_01 through PIL_23, each with own subfolder structure |

**Pillar subfolder pattern:**

| Folder | Purpose |
|--------|---------|
| `00_CANON/` | Canonical docs — the truth for this domain. **READ-ONLY without approval.** |
| `01_threads/` or domain-specific | Input/working documents |
| `02_artifacts/` | Extracted/processed outputs |
| `03_*` through `04_*` | Domain-specific subfolders |
| `90_ARCHIVE/` | Superseded content |

**The 23 Pillars:**

| # | Name | Domain |
|---|------|--------|
| 01 | AVATARS | Customer personas, ICPs |
| 02 | BRANDING | Visual + verbal identity |
| 03 | COPY | Copywriting systems |
| 04 | CONTENT | Content strategy |
| 05 | GRAPHICS | Visual assets |
| 06 | VIDEO | Video production |
| 07 | UI_LIBRARY | Component library |
| 08 | KNOWLEDGE_INGESTION | Learning pipelines |
| 09 | ROLES_SKILLS | Virtual workforce |
| 10 | WORKING_PRACTICES | SOPs, workflows |
| 11 | BUILD_STORY | Build documentation |
| 12 | KEYWORDS | Keyword research |
| 13 | SEO | Technical SEO |
| 14 | NAVIGATION | Goals, routing |
| 15 | ENTERPRISE_OS | System governance |
| 16 | CONTENT_GENERATION | Auto-content pipelines |
| 17 | RAG_SYSTEM | Retrieval config |
| 18 | AGENT_FRAMEWORK | Agent orchestration |
| 19 | PROPERTY | Property Connect vertical |
| 20 | FITNESS | Fitness platform vertical |
| 21 | MARKET_RESEARCH | Research frameworks |
| 22 | VOICE_TRAINING | Voice platform |
| 23 | DOG_PLATFORM | Dog training platform |

---

### 4.8 07_BUILD_FACTORY — Active Projects

| Action | Rule |
|--------|------|
| READ | Always allowed |
| WRITE | Project deliverables in correct scaffold folder |
| EDIT | Active project files |
| What lives here | PRJ_* project folders, each with 9-folder scaffold |

**Special rules:**
- Every project uses the SAME 9-folder scaffold (Section 3.13)
- Never create a PRJ_ folder with a different structure
- PRDs go in 02_Product/, not anywhere else
- Design files go in 03_Design/, not 02_Product/
- Code goes in 05_Development/, not root

**Active Projects:**

| Project | Purpose |
|---------|---------|
| PRJ_Enterprise_Platform | Enterprise OS V7 web platform |
| PRJ_Property_Connect_London | Property AI chatbot (MVP Feb 28) |
| PRJ_Fitness_Platform | AI workout generator |
| PRJ_AI_Chatbot_Products | Revenue chatbot product |
| PRJ_UI_Component_Library | Figma→React component pipeline |
| PRJ_LeadEngine_Platform | AI conversion intelligence platform |

---

### 4.9 08_OPERATIONS — Post-Launch

| Action | Rule |
|--------|------|
| READ | Always allowed |
| WRITE | Metrics, marketing reports, legal docs, financial records |
| EDIT | Active operational docs |
| What lives here | Post-launch metrics, marketing, legal, financial |

---

## 5. NAMING CONVENTIONS

### 5.1 Folders

| Type | Pattern | Example |
|------|---------|---------|
| Top-level component | `NN_NAME` (UPPERCASE) | `00_SYSTEM_ROOT`, `07_BUILD_FACTORY` |
| Pillar | `PIL_NN_NAME` | `PIL_03_COPY`, `PIL_19_PROPERTY` |
| Project | `PRJ_Name` (Title_Case) | `PRJ_Property_Connect_London` |
| Goal | `GOAL_Name` | `GOAL_AI_Chatbot_Revenue` |
| Archive | `90_ARCHIVE/` | Always `90_ARCHIVE/` |

### 5.2 Files

| Type | Pattern | Example |
|------|---------|---------|
| Canon/System | UPPERCASE_UNDERSCORES.md | `MASTER_CONTEXT.md`, `ROUTING_RULES.md` |
| Working files | lowercase_underscores.md | `session_log.md`, `decisions.md` |
| Date-based | YYYY-MM-DD_description.ext | `2026-02-17_session_01.md` |
| PRDs | PRD_Descriptive_Name.md | `PRD_COMPLETE_BUILD_SPEC.md` |
| Backups | filename_BACKUP_YYYYMMDD.ext | `schema_BACKUP_20260217.sql` |

### 5.3 Forbidden Names

- No spaces in file or folder names (use underscores)
- No special characters except hyphens and underscores
- No generic names: `temp.md`, `test.md`, `new.md`, `untitled.md`
- Never invent pillar names — use only the 23 canonical names above

---

## 6. ROUTING TABLE

When content needs a home, use this table:

| Content Type | Destination |
|-------------|-------------|
| System governance, architecture rules | `00_SYSTEM_ROOT/` |
| Goals, 5A definitions, state snapshots | `01_NAVIGATION_CENTRE/` |
| Session logs, task queues, agent configs | `02_COMMAND_DECK/` |
| Scripts, indices, schemas, configs | `03_CORE_ENGINE/` |
| Raw content, extraction results, RAG bundles | `04_KNOWLEDGE_LIBRARY/` |
| Reusable templates, prompt templates | `05_TEMPLATE_HUB/` |
| Domain knowledge (fits a specific pillar) | `06_DOMAIN_PILLARS/PIL_NN_*/` |
| Project deliverables (PRDs, code, designs) | `07_BUILD_FACTORY/PRJ_*/` |
| Marketing metrics, legal, financial | `08_OPERATIONS/` |
| **DON'T KNOW** | `04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/` |

### Routing Decision Tree

```
Is it about system governance/rules?
  YES → 00_SYSTEM_ROOT
  NO ↓

Is it a goal, priority, or state snapshot?
  YES → 01_NAVIGATION_CENTRE
  NO ↓

Is it a session log or task assignment?
  YES → 02_COMMAND_DECK
  NO ↓

Is it a script, index, or config?
  YES → 03_CORE_ENGINE
  NO ↓

Is it raw content for processing or a session transcript?
  YES → 04_KNOWLEDGE_LIBRARY
  NO ↓

Is it a reusable template?
  YES → 05_TEMPLATE_HUB
  NO ↓

Does it belong to a specific knowledge domain (pillar)?
  YES → 06_DOMAIN_PILLARS/PIL_NN_*
  NO ↓

Is it a project deliverable (PRD, code, design, test, deploy)?
  YES → 07_BUILD_FACTORY/PRJ_*/(correct scaffold folder)
  NO ↓

Is it post-launch operational (metrics, legal, financial)?
  YES → 08_OPERATIONS
  NO ↓

Route to 04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/
Log the routing decision and reason for uncertainty.
```

---

## 7. QA CHECKLISTS

### 7.1 Post-Write Checklist

Run after creating ANY file:

- [ ] File name follows naming conventions (Section 5)?
- [ ] File is in the correct location (Section 6 routing)?
- [ ] File content is complete (not truncated)?
- [ ] No existing file was overwritten?
- [ ] FILE_INDEX.json updated (if applicable)?

### 7.2 Post-Edit Checklist

Run after modifying ANY file:

- [ ] File was READ before editing?
- [ ] Not a 00_CANON file (or user approved)?
- [ ] Backup created (if significant edit)?
- [ ] Edit verified (re-read modified section)?
- [ ] No unintended changes to surrounding content?

### 7.3 Post-Batch Checklist

Run after any operation touching multiple files:

- [ ] Count BEFORE stated?
- [ ] Count AFTER stated?
- [ ] Before + After counts reconcile (explain any difference)?
- [ ] All affected files logged?
- [ ] No files accidentally deleted/moved/renamed?
- [ ] Checkpoint saved?

### 7.4 Session End Checklist

- [ ] Verbatim transcript saved to SESSION_ARCHIVE?
- [ ] Summary saved to ACTIVE_SESSIONS?
- [ ] SESSION_INDEX.md updated?
- [ ] STATE_SNAPSHOTS updated (if system state changed)?
- [ ] All open files saved and verified?
- [ ] Git committed (if meaningful work done)?

### 7.5 PRD Quality Checklist

Every PRD must include (per the Granular Screens spec format):

- [ ] Route (URL path)?
- [ ] Layout code (SB, SP, CT, FC, GR)?
- [ ] Permission level (L1-L7)?
- [ ] States table (State | Description)?
- [ ] Components table (Component | Type | Location | Details)?
- [ ] Modals table (Modal | Trigger | Content)?
- [ ] Features list (what it does)?
- [ ] Benefits list (why it matters)?
- [ ] Database entities (which tables)?
- [ ] API endpoints (which APIs)?
- [ ] S>C>E badges where applicable?

---

## 8. ERROR RECOVERY

### 8.1 Wrong File Location

```
1. Do NOT move it yourself without approval
2. Report: "File [X] appears to be in wrong location. It should be in [Y]. Move it? [Y/N]"
3. Wait for approval
4. Move using MOVE procedure (Section 3.5)
```

### 8.2 Overwritten File

```
1. Check for backup (filename_BACKUP_YYYYMMDD.ext)
2. Check git: git log --oneline [filepath] and git show HEAD~1:[filepath]
3. If recoverable: restore from backup/git
4. If not: report to user immediately, explain what was lost
```

### 8.3 Wrong Count

```
1. STOP claiming counts until verified
2. Run explicit count: ls -1 [path] | wc -l
3. State EXACTLY what was counted (extension filter, recursive or not, hidden files or not)
4. Cache the count — reference it, don't recount
5. If count differs from expected: explain the difference, don't "fix" it
```

### 8.4 Script Failure Mid-Batch

```
1. Check for checkpoint file
2. Resume from last checkpoint (not from beginning)
3. If no checkpoint: report to user, propose resumption strategy
4. NEVER re-process already-processed items (wasteful, potentially destructive)
```

### 8.5 Uncertain Routing

```
1. Do NOT guess
2. Route to UNROUTED/
3. Log the uncertainty and reasoning
4. Ask user if high-value content
```

---

## 9. S>C>E GOVERNANCE IN PRACTICE

All content in V7 follows the Staging → Canonical → Execution flow:

| Stage | Badge | Meaning | Rules |
|-------|-------|---------|-------|
| Staging | 🟡 | Draft, unverified, work-in-progress | Can be freely edited, experimental |
| Canonical | 🟢 | Verified, approved, source of truth | Requires approval to edit |
| Execution | 🔵 | Deployed, live, operational | Changes require formal review |

**In practice:**
- New content starts as 🟡 Staging
- User/owner reviews and promotes to 🟢 Canonical
- Canonical content in 00_CANON/ folders is the ultimate authority
- Never edit 🟢 or 🔵 content without explicit approval

---

## 10. ANTI-PATTERNS (THINGS THAT WILL GET YOU KILLED)

| # | Anti-Pattern | Why It's Bad | What To Do Instead |
|---|-------------|--------------|-------------------|
| 1 | "Cleaning up" without being asked | Destroys provenance, loses work | Only reorganize if explicitly requested |
| 2 | Different file counts for same query | Destroys trust | Count once, cache, verify, explain method |
| 3 | Deleting "duplicates" | Originals may be needed for provenance | Archive, never delete; ask first |
| 4 | Dumping outputs in root folders | Breaks V7 structure | Use routing table (Section 6) |
| 5 | Inventing pillar/folder names | Breaks taxonomy | Use only canonical names |
| 6 | Truncating long files silently | Loses data | Process in chunks, never truncate |
| 7 | No checkpoints during batch ops | Risk of total restart | Checkpoint after EVERY item |
| 8 | Editing 00_CANON without approval | Corrupts source of truth | Always ask first |
| 9 | Assuming structure is wrong | Destroys working system | If it exists and user hasn't complained, IT'S CORRECT |
| 10 | Continuing after error without reporting | Cascading failures | Stop, report, get guidance |

---

## 11. CONDENSED REFERENCE (For CLAUDE.md Embedding)

The following block should be maintained in CLAUDE.md for always-on access:

```
## V7 Quick Ops Reference

TASK RISKS: R/SR/AN/PL/TS=None | LG/CM=Low | W/E/RT/IG/CV/IX/BD/PU/TB=Med | D/MV/RN=HIGH(need approval)
ROUTING: Governance→00 | Goals→01 | Sessions→02 | Scripts→03 | Content→04 | Templates→05 | Domain→06 | Projects→07 | PostLaunch→08 | Unsure→04/UNROUTED
NAMES: Folders=UPPERCASE | Canon=UPPERCASE.md | Working=lowercase.md | Dated=YYYY-MM-DD_desc.md
SCAFFOLD: 01_Strategy|02_Product|03_Design|04_Architecture|05_Development|06_Testing|07_Deployment|08_Marketing|90_Archive
BEFORE WRITE: Check name+route+no-overwrite → AFTER: Verify content+index
BEFORE EDIT: Read first+check canon+backup → AFTER: Verify edit+no side effects
NEVER: Delete(archive instead) | Move/Rename without approval | Overwrite | Guess routing | Truncate | Skip checkpoints
SESSION: Start→read state+last session | End→save verbatim+summary+update index+commit
FULL MANUAL: 00_SYSTEM_ROOT/V7_OPERATIONS_MANUAL.md
```

---

## APPENDIX A: PRD SCREEN SPEC TEMPLATE

Every screen in any PRD must follow this format:

```markdown
## SCREEN [ID]: [Name]

**Route:** `/module/path`
**Layout:** `[SB|SP|CT|FC|GR]`
**Permission:** L[N]+ (who can access)

### States

| State | Description |
|-------|-------------|
| `[SCREEN_ID].default` | Default view description |
| `[SCREEN_ID].loading` | Loading state description |
| `[SCREEN_ID].empty` | Empty/no-data state |
| `[SCREEN_ID].error` | Error state + recovery |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| [Name] | `[type]` | [where in layout] | [specifics, data shown, interactions] |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `[SCREEN_ID].modal.[name]` | [what opens it] | [what's inside] |

### Features

| Feature | Description |
|---------|-------------|
| [Feature name] | [What it does] |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| [Benefit] | [User role/persona] | [Business/productivity impact] |

### Data

| Entity | Table | Key Fields |
|--------|-------|------------|
| [Entity name] | [DB table] | [Relevant columns] |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET/POST/etc | `/api/v1/...` | [What it does] |
```

---

## APPENDIX B: SESSION LOG TEMPLATE

```markdown
# SESSION SUMMARY — YYYY-MM-DD Session NN

## Focus: [One-line description]

## What Got Done
1. [Action + outcome]
2. [Action + outcome]

## Key Decisions
- [Decision + rationale]

## Files Created/Modified
- CREATED: [path]
- EDITED: [path] — [what changed]

## Issues/Blockers
- [Issue + status]

## Next Steps
- [ ] [Task 1]
- [ ] [Task 2]

## Counts Verified
- [Resource]: [count] (method: [how counted])
```

---

## APPENDIX C: 27 EXTRACTION DOMAINS

When processing content through ingestion, classify against:

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

---

*This document is the foundation. Every session starts here. Every task follows these procedures. Every output meets these standards. No exceptions.*
