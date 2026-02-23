# ENTERPRISE OS V7 — OWNER'S MANUAL

> **For:** John (the human)
> **Not for:** LLMs — they have their own docs
> **Last updated:** 2026-02-20
> **Keep this open during every session.**

---

## How to Use This Document

This is your operating guide for Enterprise OS V7. It tells you exactly what to do at three points:

1. **Starting a session** — how to open, what to tell the LLM, how to verify it loaded correctly
2. **During a session** — what to watch for, when to intervene, how to spot problems
3. **Ending a session** — how to wrap up, what to check, how to verify nothing got broken

The other four docs in this folder cover:
- `SYSTEM_CAPABILITIES.md` — What the system can do when everything's working
- `RULES_AND_ENFORCEMENT.md` — Every rule, why it exists, how to enforce it
- `MAINTENANCE_DRILLS.md` — Health checks you can run at any time
- `PROMPT_LIBRARY.md` — Copy-paste prompts for every common task

---

# SECTION A: SESSION STARTUP

## A1. Before You Open Any LLM

Open these files in your text editor (or have them ready to paste):

| File | Location | Why |
|------|----------|-----|
| SYSTEM_MANIFEST.md | `00_SYSTEM_ROOT/SYSTEM_MANIFEST.md` | The master routing doc — tells the LLM how the system works |
| V7_OPERATIONS_MANUAL.md | `00_SYSTEM_ROOT/V7_OPERATIONS_MANUAL.md` | Task procedures and QA checklists |
| Latest state snapshot | `01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/` (newest file) | What happened last time, current status |
| Latest session log | `02_COMMAND_DECK/ACTIVE_SESSIONS/` (newest folder, newest file) | What was done in the last session |

**Quick check:** Look at the state snapshot date. If it's more than 3 days old, the system is stale — your first task should be running `v7_daily.py` (see Section B5).

## A2. Opening a Session — Claude Code

Claude Code reads `CLAUDE.md` files automatically. You don't need to paste context.

**What to do:**
1. Open Claude Code in your terminal
2. Navigate to `C:\Users\under\Downloads\ENTERPRISE_OS_V7`
3. Tell it what you want to do

**Verify it loaded correctly — ask:**
> "What are the 8 top-level folders in V7? What's the latest state snapshot date?"

**Good answer:** Lists all 8 (`00_SYSTEM_ROOT` through `08_OPERATIONS`) and gives today's or recent date.
**Bad answer:** Makes up folder names, says "I don't have that information", or gives V6 names.

**If it didn't load correctly:**
> "Read the file at 00_SYSTEM_ROOT/SYSTEM_MANIFEST.md and 00_SYSTEM_ROOT/V7_OPERATIONS_MANUAL.md before doing anything else."

## A3. Opening a Session — ChatGPT, DeepSeek, or Gemini

These don't auto-read your files. You need to feed them context.

**Step 1: Paste the system context.** Copy the contents of `SYSTEM_MANIFEST.md` and paste it at the start of your conversation. Say:

> "This is my system architecture. Read it fully before responding. Confirm you understand by listing the 8 top-level components."

**Step 2: Paste the rules.** Copy the contents of `RULES_AND_ENFORCEMENT.md` (from this manual suite) and paste it. Say:

> "These are the rules you must follow in this session. The most important ones: never delete files, never move files without my approval, never invent folder or pillar names."

**Step 3: Paste the current state.** Copy the latest state snapshot and paste it. Say:

> "This is the current system state. Tell me what the top 3 priorities are."

**Step 4: Give your task.** Now give the LLM your actual instruction.

**Verify it loaded correctly — same test as above:**
> "What are the 8 top-level folders? What pillar is PIL_19?"

**Good answer:** Lists all 8 correctly, says PIL_19 is PROPERTY.
**Bad answer:** Invents names, gets pillars wrong, says "based on what you've shared..."

## A4. Opening a Session — For a Specific Project

If you're working on a specific project (e.g., Property Connect London), also load:

> "Read the PROJECT_STATE.md file at `07_BUILD_FACTORY/PRJ_Property_Connect_London/PROJECT_STATE.md` before we start."

Same for any project:
- `PRJ_Fitness_Platform`
- `PRJ_Enterprise_Platform`
- `PRJ_UI_Component_Library`
- `PRJ_LeadEngine_Platform`
- `PRJ_Dog_Platform`
- `PRJ_Voice_Training`
- `PRJ_AI_Chatbot_Products`

## A5. The 30-Second Startup Checklist

Before giving your first real instruction, confirm:

- [ ] LLM knows the 8 top-level components
- [ ] LLM knows the current state (latest snapshot)
- [ ] LLM knows what was done last session
- [ ] LLM knows the rules (especially: no deleting, no moving, no inventing names)
- [ ] If project-specific: LLM has read that project's PROJECT_STATE.md

---

# SECTION B: IN-SESSION WORK PRACTICES

## B1. Types of Work and What to Watch For

### Building (code, features, platform work)
- Code → `07_BUILD_FACTORY/PRJ_[Name]/05_Development/`
- PRDs → `02_Product/`, Design → `03_Design/`, Architecture → `04_Architecture/`
- Watch for: files outside project folder, invented folders, root dumps

### Writing (copy, content, docs)
- Copy → `PIL_03_COPY` or `PIL_04_CONTENT` under `01_INPUT/`
- Canon docs → `00_CANON/` (needs your approval)
- Watch for: wrong pillar placement, unapproved canon edits, generic filenames

### Extracting (processing content through v7_extract.py)
- Drop source content in `RAW_INTAKE/[type]/` (see B1A below)
- Extraction outputs go alongside source + central store
- Watch for: wrong extraction mode, truncated content, missing central store copy

### Ingesting (routing content to pillars)
- `intake_processor.py` scores against pillar keywords, needs 2+ hits to auto-route
- Below threshold → `UNROUTED/`
- Watch for: manual routing instead of script, no routing log, files vanishing

### Research (market research, competitor analysis, data gathering)
- Research outputs → `PIL_21_MARKET_RESEARCH/01_INPUT/` or relevant pillar
- API scrape data → `RAW_INTAKE/api_scrapes/`
- Watch for: data saved to wrong pillar, no extraction run on raw data

### Planning (goals, strategy, roadmaps)
- Goal docs → `01_NAVIGATION_CENTRE/ACTIVE_GOALS/`
- Strategy docs → project's `01_Strategy/` folder
- State snapshots → `01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/`
- Watch for: planning docs scattered outside Navigation Centre

### PRD Creation (product specs, screen inventories)
- PRDs → `07_BUILD_FACTORY/PRJ_[Name]/02_Product/`
- Use templates from `05_TEMPLATE_HUB/PRD_TEMPLATES/`
- Watch for: missing screen specs, no layout codes, PRDs outside project folders

### Schema / Database Work
- SQL schemas → `03_CORE_ENGINE/SCHEMAS/`
- Config → `03_CORE_ENGINE/CONFIG/`
- Watch for: schema changes not reflected in docs, no backup before changes

### Design Pipeline (UI kits, visual assets, mockups)
- Kit outputs → `07_BUILD_FACTORY/PRJ_UI_Component_Library/03_Design/[kit_name]/`
- Design tokens → project's `03_Design/`
- Watch for: kit outputs scattered, PNGs not catalogued, match data stale

### Maintenance (health checks, audits, index rebuilds)
- Run scripts from `03_CORE_ENGINE/SCRIPTS/`
- Reports go to `03_CORE_ENGINE/INDICES/` (SYSTEM_HEALTH.md etc.)
- See MAINTENANCE_DRILLS.md for specific procedures

## B1A. Where to Put Content for Ingestion

This is the complete map of where every type of content enters the system.

**Staging location:** `04_KNOWLEDGE_LIBRARY/EXTRACTION_PIPELINE/RAW_INTAKE/`

| Content Type | Drop It In | Default Extraction | Where It Gets Routed |
|---|---|---|---|
| **AI chat threads** (Claude, ChatGPT, DeepSeek, Gemini exports) | `RAW_INTAKE/threads/` | `v7_extract.py thread` (EKX-1) | Pillar's `01_threads/` based on content |
| **Books, chapters, long-form writing** | `RAW_INTAKE/books/` | `v7_extract.py book` | Relevant pillar or project folder |
| **API scrapes** (property data, market data, structured exports) | `RAW_INTAKE/api_scrapes/` | `v7_extract.py domains` | Pillar or project based on content |
| **YouTube transcripts** | `RAW_INTAKE/youtube/` | `v7_extract.py domains` or `copy` | Pillar based on content |
| **Research notes, competitor analysis** | `RAW_INTAKE/research/` | `v7_extract.py domains` + `copy` | `PIL_21_MARKET_RESEARCH` or relevant pillar |
| **PRDs, design specs, screen inventories** | `RAW_INTAKE/prds/` | `v7_extract.py domains` + `copy` | Project's `02_Product/` folder |
| **Everything else** | `RAW_INTAKE/general/` | `v7_extract.py domains` | `intake_processor.py` decides, or UNROUTED |

**The flow for any content:**

```
1. YOU drop file in RAW_INTAKE/[type]/
       |
2. ROUTE: intake_processor.py --dry-run  (preview where it'll go)
   YOU approve → intake_processor.py     (moves it to the right pillar/project)
       |
3. EXTRACT: v7_extract.py [mode] <file>  (pulls structured intelligence)
       |
   Output Copy 1 → alongside the file (browse in context)
   Output Copy 2 → EXTRACTIONS/by_mode/[mode]/ (cross-cutting search)
   Output Copy 3 → EXTRACTIONS/by_category/ (aggregated hooks, USPs, etc.)
   Logged → PostgreSQL v7_extractions table
       |
4. FIND IT LATER:
   - By file: look next to the source file for .extract_*.json
   - By mode: EXTRACTIONS/by_mode/copy/ or /book/ or /thread/ or /domains/
   - By category: EXTRACTIONS/by_category/hooks.json, usps.json, etc.
   - By pillar: filter EXTRACTION_INDEX.json
   - By date: EXTRACTIONS/by_mode/*/YYYY-MM/WN/
   - By SQL: SELECT * FROM v7_extractions WHERE pillar = 'PIL_19_PROPERTY'
```

**Naming convention for inputs:**
`YYYY-MM-DD_source_description.md` — e.g. `2026-02-20_claude_extraction_engine_build.md`

## B1B. Narration Protocol — What the LLM Must Announce

Every action the LLM takes must be announced with three lines:

```
OPERATION: [WRITE / EDIT / ROUTE / EXTRACT / INDEX / COMMIT / BUILD]
TARGET: [full file path]
RULES: [which rules apply — e.g. "naming convention", "routing to PIL_19", "no overwrite"]
```

**Why this matters:** You can't verify work you can't see. If the LLM silently creates files, edits things, or routes content without announcing it, you have no idea what happened until something breaks.

**What to say if the LLM stops narrating:**
> "You just did something without announcing it. What operation did you perform? What file? What rules applied? Don't do anything else without announcing it first."

**Example of good narration:**
```
OPERATION: WRITE
TARGET: 07_BUILD_FACTORY/PRJ_Property_Connect_London/02_Product/PRD_Chat_Widget.md
RULES: PRD naming convention, no overwrite (file doesn't exist), 9-folder scaffold
```

## B2. The Five Red Flags

Stop the LLM immediately if you see any of these:

### Red Flag 1: "Let me clean up / reorganize / fix the structure"
**What to say:** "STOP. Do not move, rename, or reorganize anything. Tell me exactly what you want to change and I'll approve it file by file."

### Red Flag 2: "I'll delete the duplicates / remove the old versions"
**What to say:** "STOP. Do not delete anything. If something needs to go, move it to 90_ARCHIVE in its current folder. Show me the list first."

### Red Flag 3: Files appearing in root folders
**Check:** `ls` the V7 root. There should only be 8 folders (00 through 08) plus maybe a `.git` folder and `CLAUDE.md`. Anything else is wrong.
**What to say:** "You created [filename] in the root. Move it to [correct subfolder]. Nothing goes in the root."

### Red Flag 4: Pillar names you don't recognize
**Check against the 23 canonical names** (listed in `RULES_AND_ENFORCEMENT.md`). If the LLM references `PIL_24_ANYTHING` or uses names like `WILD_CARD`, `EXPERIMENTAL`, `MISC` — it's wrong.
**What to say:** "That pillar doesn't exist. Use only the 23 canonical pillar names. Which of the 23 does this belong to?"

### Red Flag 5: File counts changing between questions
**If you ask "how many files in X" and get different numbers each time:**
**What to say:** "You gave me [N1] last time and [N2] now. Which is correct? Count again, tell me exactly what you're counting (extension, recursive, which folders), and don't continue until the number is stable."

## B3. When to Intervene

| Situation | Action |
|-----------|--------|
| LLM says "I'll reorganize..." | STOP immediately. Ask for file-by-file approval. |
| LLM says "Cleaning up..." | STOP immediately. Ask what exactly it wants to delete/move. |
| LLM creates a file you didn't ask for | Ask why. If it's temp/scratch, tell it to delete the temp file. |
| LLM edits a `00_CANON/` file | Ask if you approved that. If not, tell it to revert. |
| You see an error flash by during batch work | STOP. Ask for the error. Don't let it "continue anyway". |
| Count doesn't match what you expected | STOP. Reconcile before continuing. |
| LLM says "approximately" or "about" for counts | Not acceptable. Demand exact numbers. |

## B4. Checking Work During a Session

At any point you can ask:

> "List every file you've created or modified this session, with full paths."

> "What's the current count of files in [folder]?"

> "Show me the contents of [file] — don't summarize, show the actual content."

> "Did you follow NAMING_CONVENTIONS.md for that file name?"

## B5. Running Scripts

These are the scripts you'll use most often. All are in `03_CORE_ENGINE/SCRIPTS/`.

### Start a work session log
```bash
python 03_CORE_ENGINE/SCRIPTS/session_logger.py start "Description of what I'm doing"
```

### Log progress during session
```bash
python 03_CORE_ENGINE/SCRIPTS/session_logger.py log "What I just did"
```

### Process new files through intake
```bash
# Preview what would happen (safe — doesn't move anything):
python 03_CORE_ENGINE/SCRIPTS/intake_processor.py --dry-run

# Actually process:
python 03_CORE_ENGINE/SCRIPTS/intake_processor.py
```

### Rebuild the file index
```bash
python 03_CORE_ENGINE/SCRIPTS/generate_indices.py
```

### Run daily maintenance
```bash
# Full run (scan, health, snapshot, stale check):
python 03_CORE_ENGINE/SCRIPTS/v7_daily.py

# Quick run (diff + health only):
python 03_CORE_ENGINE/SCRIPTS/v7_daily.py --quick
```

### Start the search API
```bash
python 03_CORE_ENGINE/SCRIPTS/v7_search_api.py
# Then browse to http://localhost:8100/docs for the API
```

### Wrap up a session
```bash
# Interactive mode:
python 03_CORE_ENGINE/SCRIPTS/session_wrapup.py

# Quick mode:
python 03_CORE_ENGINE/SCRIPTS/session_wrapup.py --quick -s "Summary of session" -p "PCL,UI Library"
```

## B6. Working with Databases

### PostgreSQL (v7_registry)
The main system database. Stores the file registry (5,663+ files), session logs, and system snapshots.

**Check if it's running:**
```bash
pg_isready -h localhost -p 5432
```

**Quick query examples** (run in psql or via the search API):
```sql
-- How many files are registered?
SELECT COUNT(*) FROM v7_files;

-- Files modified today:
SELECT file_path, last_modified FROM v7_files WHERE last_modified::date = CURRENT_DATE;

-- Files in a specific pillar:
SELECT file_path FROM v7_files WHERE file_path LIKE '%PIL_19%';
```

### ChromaDB (vector search)
Stores 5,197+ embeddings for semantic search. Used by the search API.

**Search via API** (if `v7_search_api.py` is running):
```
http://localhost:8100/search?q=property+chatbot+MVP
```

### UI Library Database (PostgreSQL)
Separate database for the UI component library. 19,837 items across 183 kits.

**Check:**
```bash
psql -d ui_library -c "SELECT COUNT(*) FROM items;"
```

## B7. The Hourly Gut Check

Every hour (or every major milestone), ask yourself:

1. Are files going where they should? (Check the last few created files)
2. Is the LLM following naming rules? (Check file names)
3. Has anything been deleted or moved that shouldn't have been?
4. Are counts still matching what I expect?
5. Has the LLM invented any new folders or pillar names?

If the answer to any of 3-5 is "yes" or "I'm not sure" — stop and investigate before continuing.

---

# SECTION C: END-SESSION PROTOCOL

## C1. The Wrap-Up Sequence

Do these steps in order. Don't skip any.

### Step 1: Ask for the session summary
> "List everything you did this session: files created, files modified, files moved, decisions made, and anything left unfinished."

Review the list. Does it match what you remember? If something's missing, ask about it.

### Step 2: Run the session wrap-up script
```bash
python 03_CORE_ENGINE/SCRIPTS/session_wrapup.py --quick -s "Session summary" -p "Projects touched"
```

This automatically creates:
- Session summary in `02_COMMAND_DECK/ACTIVE_SESSIONS/YYYY-MM/`
- Transcript in `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/`
- Updates to `SESSION_INDEX.md`
- Updates to `PROJECT_STATE.md` for touched projects

### Step 3: Verify files are in the right places

Spot-check 3-5 files that were created or modified:

> "Show me the full path of [file]. Is it in the correct location per the routing manifest?"

### Step 4: Check for strays

> "Are there any files in the V7 root folder that shouldn't be there?"

> "Did anything end up in UNROUTED that should have been routed?"

### Step 5: Update the file index
```bash
python 03_CORE_ENGINE/SCRIPTS/generate_indices.py
```

### Step 6: Update the PostgreSQL registry
```bash
python 03_CORE_ENGINE/SCRIPTS/v7_registry.py scan
```

This walks the entire filesystem, hashes every file, and upserts into PostgreSQL. Every new file, every modification, and every deletion gets logged to the `v7_changes` audit trail. This is how you answer "what did the LLM actually do to my system?" after any session.

**What to look for in the output:**
- **New files** — do these match what you expected? If there are more than you asked for, investigate.
- **Modified files** — did you approve all of these edits?
- **Deleted files** — there should be ZERO. If any show as deleted, something went wrong.

### Step 7: Update the semantic search (ChromaDB)
```bash
python 03_CORE_ENGINE/SCRIPTS/v7_registry.py chromadb-sync
```

This reads all markdown files from the PostgreSQL registry, chunks them by heading, and pushes the chunks to ChromaDB for semantic search. Without this, searching "find everything about property chatbots" won't include work from this session.

**Note:** This can take a few minutes if many files changed. If you only changed 2-3 files, it's still fast. You can skip this step if the session was small (just scripts or config, no markdown content), but run it at least once a day.

### Step 8: Take a system snapshot
```bash
python 03_CORE_ENGINE/SCRIPTS/v7_registry.py snapshot
```

This saves a point-in-time measurement to the `v7_system_state` table: total files, total size, breakdown by component/pillar/type, empty pillars, stale files. Over time this builds a history so you can see "is the system growing? Are pillars getting filled?"

### Step 9: Git commit
```bash
cd C:\Users\under\Downloads\ENTERPRISE_OS_V7
git add -A
git status
# Review what's being committed — look for anything unexpected
git commit -m "YYYY-MM-DD: Brief description of what this session did"
```

**Before committing, check `git status`:**
- Are there files you don't recognize? Ask about them before committing.
- Are there deleted files? Did you approve those deletions?
- Are there files outside the 8 component folders? They shouldn't be there.

### Step 10: Create or update the state snapshot (markdown)
If the system state changed meaningfully (new project milestone, new scripts, new pillar content):

> "Create a new state snapshot at `01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/2026-MM-DD.md` reflecting what we did today."

This is the human-readable version (the DB snapshot from Step 8 is the machine-readable version). Both are useful — the markdown one is what the next LLM session reads for context.

## C2. The End-Session Checklist

- [ ] Session summary exists in `02_COMMAND_DECK/ACTIVE_SESSIONS/YYYY-MM/`
- [ ] Transcript saved in `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/`
- [ ] `SESSION_INDEX.md` updated
- [ ] `PROJECT_STATE.md` updated for each touched project
- [ ] No stray files in V7 root
- [ ] No unexpected files in UNROUTED
- [ ] `FILE_INDEX.json` regenerated
- [ ] PostgreSQL registry updated (`v7_registry.py scan` — check for unexpected deletions)
- [ ] ChromaDB synced (`v7_registry.py chromadb-sync` — at least daily)
- [ ] System snapshot taken (`v7_registry.py snapshot`)
- [ ] Git committed with descriptive message
- [ ] Markdown state snapshot updated (if system state changed)
- [ ] File counts match expectations (no mysterious gains or losses)
- [ ] Audit trail checked: `v7_changes` shows only expected create/modify actions, zero deletions

## C3. What to Do If a Session Went Wrong

If the LLM made a mess (deleted files, wrong locations, broken structure):

1. **Don't panic.** Git has your back. Check `git log` for the last good commit.
2. **Assess the damage:**
   > "List every destructive action taken this session: deletions, moves, renames, overwrites."
3. **If files were deleted:** Check `git diff --name-only HEAD~1` to see what changed. Use `git checkout HEAD~1 -- path/to/file` to restore specific files.
4. **If files were moved wrong:** Move them back manually or ask the LLM (with explicit paths).
5. **Nuclear option:** `git checkout HEAD~1` to restore the entire last good state. (This discards everything since the last commit.)
6. **After recovery:** Run `generate_indices.py` to rebuild the file index.
7. **Log the disaster:** Add it to the disaster log so it doesn't happen again.

## C4. Quick Reference — Session Commands

| When | Command | What It Does |
|------|---------|-------------|
| Start of session | `session_logger.py start "desc"` | Creates session log |
| During session | `session_logger.py log "msg"` | Logs progress |
| Check intake | `intake_processor.py --dry-run` | Preview routing (safe) |
| Process intake | `intake_processor.py` | Route files to pillars |
| Rebuild index | `generate_indices.py` | Update FILE_INDEX.json |
| Daily maintenance | `v7_daily.py` | Full health run |
| Quick health | `v7_daily.py --quick` | Diff + health only |
| End of session | `session_wrapup.py --quick -s "summary" -p "projects"` | Markdown wrap-up |
| Update PostgreSQL | `v7_registry.py scan` | Sync filesystem to DB + audit trail |
| Preview DB changes | `v7_registry.py scan --diff` | Show what changed (safe, read-only) |
| Update ChromaDB | `v7_registry.py chromadb-sync` | Sync markdown to semantic search |
| Take DB snapshot | `v7_registry.py snapshot` | Save point-in-time system metrics |
| Check DB health | `v7_registry.py health` | Health report from PostgreSQL |
| Check stale files | `v7_registry.py stale` | Files not modified in 30+ days |
| Extract: 27 domains | `v7_extract.py domains <file>` | Classify content across 27 domains |
| Extract: thread (EKX-1) | `v7_extract.py thread <file>` | 20-section structured thread summary |
| Extract: copy/sales | `v7_extract.py copy <file>` | Benefits, USPs, hooks, objections, proof |
| Extract: book | `v7_extract.py book <file>` | Proofs, arguments, rhetorical devices, myths |
| Extract: batch | `v7_extract.py batch <folder> --mode copy` | Run extraction on entire folder |
| Extract: dry run | `v7_extract.py domains <file> --dry-run` | Preview without API call |
| Extract: resume batch | `v7_extract.py batch <folder> --mode domains --resume` | Resume from checkpoint |
| Search files | `v7_search_api.py` (then localhost:8100) | Search API |

All scripts are in: `C:\Users\under\Downloads\ENTERPRISE_OS_V7\03_CORE_ENGINE\SCRIPTS\`

---

*This document is part of the Owner's Manual suite. See also: SYSTEM_CAPABILITIES.md, RULES_AND_ENFORCEMENT.md, MAINTENANCE_DRILLS.md, PROMPT_LIBRARY.md*
