# ENTERPRISE OS V7 — PROMPT LIBRARY

> **Copy-paste prompts for every common function.**
> Each prompt is self-contained — it tells the LLM what to read, what to do, and what rules to follow.
> Works with any LLM: Claude, ChatGPT, DeepSeek, Gemini.
> Last updated: 2026-02-20

---

## How to Use This Document

1. Find the prompt for what you want to do
2. Copy it
3. Replace anything in `[BRACKETS]` with your actual values
4. Paste it into your LLM session
5. Verify the LLM follows the instructions (check the rules)

**Tip:** For Claude Code, most of these prompts work as-is because it can read your filesystem. For other LLMs, you may need to paste the referenced files inline.

---

# SESSION PROMPTS

## Prompt 1: Start a New Session

```
I'm starting a new work session in Enterprise OS V7.

Before doing anything:
1. Read: 00_SYSTEM_ROOT/SYSTEM_MANIFEST.md
2. Read: 00_SYSTEM_ROOT/V7_OPERATIONS_MANUAL.md (Sections 1-2)
3. Read the latest file in: 01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/
4. Read the latest file in: 02_COMMAND_DECK/ACTIVE_SESSIONS/

Tell me:
- What was done in the last session
- What the current system state is
- What the top 3 priorities are

Then wait for my instruction. Do not start any work until I tell you what to focus on.

SESSION RULES:
- Never delete files (archive to 90_ARCHIVE/ instead)
- Never move or rename files without my explicit approval
- Never overwrite existing files (use _v2 or timestamp suffix)
- Never put outputs in root folders
- Never edit 00_CANON/ files without my approval
- Use only the 23 canonical pillar names
- Count before and after every batch operation
- Checkpoint after every item in batch processing
- If unsure where something goes, put it in 04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/
```

## Prompt 2: Start a Session on a Specific Project

```
I'm starting a work session on [PROJECT NAME] in Enterprise OS V7.

Before doing anything:
1. Read: 00_SYSTEM_ROOT/SYSTEM_MANIFEST.md
2. Read: 07_BUILD_FACTORY/[PRJ_FOLDER]/PROJECT_STATE.md
3. Read the latest file in: 01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/
4. Read the latest file in: 02_COMMAND_DECK/ACTIVE_SESSIONS/

Tell me:
- Current state of [PROJECT NAME]
- What was done last on this project
- What's blocked or pending
- What the next logical step is

SESSION RULES:
[same rules as Prompt 1]
```

**Project folder names:**
- Property Connect London: `PRJ_Property_Connect_London`
- Enterprise Platform: `PRJ_Enterprise_Platform`
- UI Component Library: `PRJ_UI_Component_Library`
- Fitness Platform: `PRJ_Fitness_Platform`
- AI Chatbot Products: `PRJ_AI_Chatbot_Products`
- LeadEngine: `PRJ_LeadEngine_Platform`
- Dog Platform: `PRJ_Dog_Platform`
- Voice Training: `PRJ_Voice_Training`

## Prompt 3: Wrap Up This Session

```
We're done for today. Wrap up this session (10-step protocol):

1. List everything you did this session:
   - Files created (full paths)
   - Files modified (full paths + what changed)
   - Decisions made
   - Anything left unfinished

2. Run: python 03_CORE_ENGINE/SCRIPTS/session_wrapup.py --quick -s "[ONE LINE SUMMARY]" -p "[PROJECTS TOUCHED]"

3. Verify all files are in correct locations (no strays in root or wrong folders).

4. Run: python 03_CORE_ENGINE/SCRIPTS/generate_indices.py

5. Update PostgreSQL: python 03_CORE_ENGINE/SCRIPTS/v7_registry.py scan

6. Update ChromaDB: python 03_CORE_ENGINE/SCRIPTS/v7_registry.py chromadb-sync

7. Take DB snapshot: python 03_CORE_ENGINE/SCRIPTS/v7_registry.py snapshot

8. Show me the git status. I'll review it before we commit.

9. Git commit (I'll approve the message).

10. Create a state snapshot at 01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/[TODAY'S DATE].md if the system state changed.

Do NOT push to git. Just stage and commit locally.
```

---

# KNOWLEDGE MANAGEMENT PROMPTS

## Prompt 4: Ingest a Document Into V7

```
I have a document to ingest into Enterprise OS V7.

File: [PATH TO FILE or paste content below]

1. Read the document fully (do not truncate)
2. Read: 03_CORE_ENGINE/ROUTING_MANIFEST.md
3. Read: 03_CORE_ENGINE/INDICES/DOMAIN_REGISTRY.json

Classify this document:
- Which of the 23 pillars does it belong to? (Use only canonical names)
- Which extraction domains does it cover? (from the 27 extraction domains list)
- What artifact type is it? (Framework, Schema, Prompt, Template, Reference, Execution, or raw input)

Tell me your routing decision BEFORE moving the file. I'll approve or redirect.

If you're not sure which pillar, say so — I'd rather it goes to UNROUTED than the wrong pillar.

After I approve:
- Copy the file to the correct pillar subfolder
- Log the routing decision to 03_CORE_ENGINE/ROUTING_ENGINE/routing_logs/
- Run: python 03_CORE_ENGINE/SCRIPTS/generate_indices.py
```

## Prompt 5: Run the Intake Pipeline

```
Process all files in the intake queue.

1. Run: python 03_CORE_ENGINE/SCRIPTS/intake_processor.py --dry-run
2. Show me the proposed routing for each file
3. Wait for my approval before processing

After I approve:
4. Run: python 03_CORE_ENGINE/SCRIPTS/intake_processor.py
5. Check: ls 04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/ — anything end up here?
6. Tell me: how many files processed, how many routed, how many unrouted

Do NOT process without showing me the dry-run first.
```

## Prompt 6: Extract Knowledge From an AI Thread

```
I have an AI conversation thread to extract knowledge from.

Thread: [PATH TO FILE or paste content below]

1. Read the ENTIRE thread (do not truncate — if it's long, process in chunks)
2. Read: 03_CORE_ENGINE/ROUTING_MANIFEST.md

Extract:
- Key decisions made
- Frameworks or systems discussed
- Action items or next steps
- Specific deliverables produced
- Knowledge that should be preserved

For each extracted item:
- Classify it to a pillar (use only the 23 canonical names)
- Determine the artifact type (Framework, Schema, Prompt, Template, Reference)
- Suggest the target location (pillar + subfolder)

Present the extraction summary. I'll review and approve before you create any files.

IMPORTANT: Do not lose any content. If the thread is long, process it in sections but cover EVERYTHING.
```

---

# SEARCH AND DISCOVERY PROMPTS

## Prompt 7: Search for Files Related to a Topic

```
I need to find all files related to [TOPIC] in Enterprise OS V7.

Search using these methods:
1. Read: 03_CORE_ENGINE/INDICES/FILE_INDEX.json — search for relevant filenames and paths
2. If the search API is available (localhost:8100): GET /search?q=[TOPIC]
3. Search file contents for keywords: [KEYWORD1], [KEYWORD2], [KEYWORD3]

For each result, show:
- Full file path
- File type (md, json, py, etc.)
- Which pillar it belongs to (if any)
- Brief description of what it contains (1 line)

Sort results by relevance, not alphabetically.
```

## Prompt 8: Find Everything About a Specific Pillar

```
Give me a complete inventory of PIL_[NUMBER]_[NAME].

1. List every file in 06_DOMAIN_PILLARS/PIL_[NUMBER]_[NAME]/ recursively
2. Read the 00_CANON/ docs (if they exist)
3. Check DOMAIN_REGISTRY.json for this pillar's definition, keywords, and dependencies

Report:
- Total file count
- Canon docs available (list them)
- Routing keywords defined
- Dependencies (what this pillar feeds into, what feeds into it)
- Content health: is this pillar well-populated or sparse?
- Files by subfolder breakdown
```

---

# INDEX AND DATABASE PROMPTS

## Prompt 9: Rebuild the File Index

```
Rebuild the Enterprise OS V7 file index.

1. Run: python 03_CORE_ENGINE/SCRIPTS/generate_indices.py
2. Show me the output — how many files were indexed?
3. Show the SYSTEM_HEALTH.md that was generated
4. Are there any warnings or issues?

Tell me:
- Total files indexed
- Files per component (00-08)
- Any files that were skipped and why
- Any pillars with zero files (these need attention)
```

## Prompt 10: Update the Database Registry

```
Update the PostgreSQL v7_registry database.

1. Check: pg_isready -h localhost -p 5432
2. If running: python 03_CORE_ENGINE/SCRIPTS/v7_registry.py scan
3. Report: How many files registered? Any errors?

If PostgreSQL is NOT running:
- Tell me — don't try to start it automatically
- Fall back to FILE_INDEX.json for file tracking
```

---

# EXTRACTION PROMPTS

## Prompt 10A: Run a 27-Domain Extraction Pass

```
Run a 27-domain extraction on this file:
[PATH TO FILE]

Command: python 03_CORE_ENGINE/SCRIPTS/v7_extract.py domains [PATH TO FILE]

This will:
- Classify the content across all 27 extraction domains
- Save JSON + markdown alongside the source file
- Save a copy to 04_KNOWLEDGE_LIBRARY/EXTRACTIONS/by_mode/domains/
- Update the EXTRACTION_INDEX.json
- Update the category aggregate files
- Log to PostgreSQL v7_extractions table

Show me the output summary when done. How many domains had content? What were the top 3?
```

## Prompt 10B: Run Copy/Sales Extraction

```
Run a copy/sales extraction on this file:
[PATH TO FILE]

Command: python 03_CORE_ENGINE/SCRIPTS/v7_extract.py copy [PATH TO FILE]

This extracts: benefits, features, problems, problems solved, USPs, unique mechanisms,
hooks, sales arguments, objections, proof points, and CTAs.

Show me the output summary. What are the top hooks? What are the strongest USPs?
```

## Prompt 10C: Run Book Extraction

```
Run a book extraction on this file:
[PATH TO FILE]

Command: python 03_CORE_ENGINE/SCRIPTS/v7_extract.py book [PATH TO FILE]

This extracts: proofs, arguments, facts, hooks, rhetorical devices, objections & myths,
beliefs to challenge, solutions, key concepts, and quotable lines.

Show me the strongest material. What are the best quotable lines? What myths can I disprove?
```

## Prompt 10D: Run EKX-1 Thread Extraction

```
Run an EKX-1 thread extraction on this AI chat thread:
[PATH TO FILE]

Command: python 03_CORE_ENGINE/SCRIPTS/v7_extract.py thread [PATH TO FILE]

This extracts the 20 EKX-1 sections: narrative, objectives, decisions, SOPs,
scripts, errors, status, dependencies, reusable assets, and more.

Show me the summary. What are the key decisions? What reusable assets were found?
```

## Prompt 10E: Batch Extract a Folder

```
I have a folder of files to extract. Run a batch extraction:

Folder: [PATH TO FOLDER]
Mode: [domains|copy|book|thread]

Step 1 — Preview first (safe, no API calls):
  python 03_CORE_ENGINE/SCRIPTS/v7_extract.py batch [FOLDER] --mode [MODE] --dry-run

Step 2 — Show me the dry-run output. How many files? I'll approve before running.

Step 3 — After I approve:
  python 03_CORE_ENGINE/SCRIPTS/v7_extract.py batch [FOLDER] --mode [MODE]

If it crashes or I need to stop: resume with --resume flag.
Report: how many processed, how many errors, any files that failed.
```

## Prompt 10G: Ingest Content Into the System

```
I have content to ingest. Help me get it into the right place.

Content type: [threads / books / api_scrapes / youtube / research / prds / general]
File: [PATH or paste content]
Related to: [project name or pillar, if known]

Steps:
1. Save the file to: 04_KNOWLEDGE_LIBRARY/EXTRACTION_PIPELINE/RAW_INTAKE/[type]/
   Use naming: YYYY-MM-DD_source_description.md

2. Route it: python 03_CORE_ENGINE/SCRIPTS/intake_processor.py --dry-run
   Show me where it wants to route BEFORE actually routing.

3. After I approve routing: python 03_CORE_ENGINE/SCRIPTS/intake_processor.py

4. Extract it using the appropriate mode:
   - threads → v7_extract.py thread <file>
   - books → v7_extract.py book <file>
   - api_scrapes → v7_extract.py domains <file>
   - youtube → v7_extract.py domains <file> (then v7_extract.py copy <file> if commercial)
   - research → v7_extract.py domains <file> (then v7_extract.py copy <file>)
   - prds → v7_extract.py domains <file> (then v7_extract.py copy <file>)
   - general → v7_extract.py domains <file>

5. Verify: extraction output exists alongside the file AND in EXTRACTIONS/by_mode/

ANNOUNCE every action: OPERATION, TARGET path, RULES that apply.
```

## Prompt 10F: Search My Extractions

```
I want to find extracted content across my system.

[PICK ONE OR MORE:]
- Show me all [USPs / hooks / benefits / proof_points / arguments / quotable_lines] I've ever extracted
  → Read: 04_KNOWLEDGE_LIBRARY/EXTRACTIONS/by_category/[CATEGORY].json

- Show me all [copy / book / thread / domain] extractions
  → List: 04_KNOWLEDGE_LIBRARY/EXTRACTIONS/by_mode/[MODE]/

- Show me all extractions from [PILLAR NAME]
  → Query EXTRACTION_INDEX.json filtering by pillar

- Show me all extractions from this week
  → List: 04_KNOWLEDGE_LIBRARY/EXTRACTIONS/by_mode/*/[YYYY-MM]/[WN]/

- How many total extractions have I run?
  → Read: 04_KNOWLEDGE_LIBRARY/EXTRACTIONS/EXTRACTION_INDEX.json

- Database query (if PostgreSQL running):
  → psql -d enterprise_os -c "SELECT mode, COUNT(*), SUM(item_count) FROM v7_extractions GROUP BY mode;"
```

---

# PROJECT BUILD PROMPTS

## Prompt 11: Create a New PRD

```
I need a Product Requirements Document for [FEATURE/PRODUCT NAME].

1. Read: 05_TEMPLATE_HUB/PRD_TEMPLATES/ (use the latest template)
2. Read: 07_BUILD_FACTORY/PRJ_[PROJECT]/PROJECT_STATE.md (for context)

Create the PRD following the template exactly. Every screen must have:
- Route (URL path)
- Layout code (SB, SP, CT, FC, GR)
- Permission level (L1-L7)
- States table (default, loading, empty, error)
- Components table (name, type, location, details)
- Features list
- Benefits list (with user role and impact)
- Data entities (table, key fields)
- API endpoints

Save to: 07_BUILD_FACTORY/PRJ_[PROJECT]/02_Product/PRD_[NAME].md

Do NOT overwrite any existing PRD. If one exists with the same name, use _v2 suffix.
```

## Prompt 12: Scaffold a New Project

```
Create the project scaffold for [PROJECT NAME].

1. Read: 05_TEMPLATE_HUB/PROJECT_STATE_TEMPLATE.md
2. Create the folder: 07_BUILD_FACTORY/PRJ_[Project_Name]/

Create exactly these 9 subfolders:
- 01_Strategy/
- 02_Product/
- 03_Design/
- 04_Architecture/
- 05_Development/
- 06_Testing/
- 07_Deployment/
- 08_Marketing/
- 90_Archive/

Create PROJECT_STATE.md in the project root using the template.

Do NOT create any folders outside of 07_BUILD_FACTORY/.
Do NOT add content to the subfolders — just create the structure.
```

---

# UI KIT AND DESIGN PROMPTS

## Prompt 13: Run the UI Kit Pipeline on a Kit

```
Process the UI kit: [KIT NAME]

1. Read: 03_CORE_ENGINE/SCRIPTS/figma_extractor.py for available commands
2. Read: 07_BUILD_FACTORY/PRJ_UI_Component_Library/PROJECT_STATE.md for current status

Steps:
a. Extract structure: python 03_CORE_ENGINE/SCRIPTS/figma_structure_analyzer.py [KIT_FILE_KEY]
b. Extract frames: python 03_CORE_ENGINE/SCRIPTS/figma_frame_inventory.py [KIT_FILE_KEY]
c. Classify: python 03_CORE_ENGINE/SCRIPTS/figma_classify.py [KIT_FILE_KEY]
d. Export PNGs: python 03_CORE_ENGINE/SCRIPTS/figma_export_pngs.py [KIT_FILE_KEY]

Save all outputs to: 07_BUILD_FACTORY/PRJ_UI_Component_Library/03_Design/[kit_name]/

Report after each step:
- What was extracted
- File count
- Any errors

Do NOT continue past an error. Stop and report.
```

## Prompt 14: Match PRD Screens to UI Kits

```
Match the screens in [PRD FILE] to available UI kit templates.

1. Read the PRD: 07_BUILD_FACTORY/PRJ_[PROJECT]/02_Product/[PRD_FILE]
2. Read the kit inventory: 03_CORE_ENGINE/SCRIPTS/v7_kit_inventory.py
3. Read existing match data (if any): 07_BUILD_FACTORY/PRJ_[PROJECT]/03_Design/

For each screen in the PRD:
- Screen name and route
- Best matching kit template (kit name + frame name)
- Match confidence (high/medium/low)
- What's covered vs. what needs custom work

Present the match table. I'll review before any files are created.
```

---

# SYSTEM HEALTH PROMPTS

## Prompt 15: Run System Health Check

```
Run a full health check on Enterprise OS V7.

1. Run: python 03_CORE_ENGINE/SCRIPTS/v7_daily.py
2. Show the complete output

Then verify:
a. V7 root has only the 8 component folders + .git + CLAUDE.md (nothing else)
b. Latest state snapshot date (should be today or yesterday)
c. Latest session log exists and is recent
d. FILE_INDEX.json modification date
e. PostgreSQL status: pg_isready -h localhost -p 5432
f. Git status: git status (should be clean or only expected changes)

Report as a checklist:
- [PASS/FAIL] Root folder clean
- [PASS/FAIL] State snapshot current
- [PASS/FAIL] Session log recent
- [PASS/FAIL] File index current
- [PASS/FAIL] PostgreSQL running
- [PASS/FAIL] Git status clean
- [PASS/FAIL] No stale files in critical pillars

For any FAIL: explain what's wrong and how to fix it.
```

## Prompt 16: Run Post-Incident Recovery

```
Something went wrong in the last session. Help me assess and recover.

1. Run: git diff --name-status HEAD
2. Run: git log --oneline -5
3. Check: ls C:/Users/under/Downloads/ENTERPRISE_OS_V7/ (root folder clean?)
4. Check: git diff HEAD -- "*/00_CANON/*" (canon files touched?)

For each change, classify:
- INTENDED: I approve this change
- UNINTENDED: This needs to be reverted
- INVESTIGATE: I need to look at this before deciding

Show me the list. I'll mark each one. Then revert only the ones I mark as UNINTENDED.

Do NOT revert anything without my explicit approval on each file.
```

---

# CONTENT CREATION PROMPTS

## Prompt 17: Write Copy for a Specific Pillar

```
I need copy for [DESCRIBE WHAT YOU NEED].

Before writing:
1. Read: 06_DOMAIN_PILLARS/PIL_02_BRANDING/00_CANON/ (brand voice rules)
2. Read: 06_DOMAIN_PILLARS/PIL_03_COPY/00_CANON/ (copywriting frameworks)
3. Read: 06_DOMAIN_PILLARS/PIL_01_AVATARS/00_CANON/ (if populated — target audience)

Write the copy following the brand voice and frameworks.

Save to: 06_DOMAIN_PILLARS/PIL_03_COPY/01_INPUT/[YYYY-MM-DD]_[descriptive_name].md

Do NOT save to 00_CANON — this is input/staging, not canonical.
```

## Prompt 18: Create a Canon Doc for a Pillar

```
I need a canon document for PIL_[NUMBER]_[NAME].

1. Read: 05_TEMPLATE_HUB/PILLAR_DOC_TEMPLATES.md (use the README template)
2. Read: 03_CORE_ENGINE/INDICES/DOMAIN_REGISTRY.json (for pillar definition)
3. Read everything currently in 06_DOMAIN_PILLARS/PIL_[NUMBER]_[NAME]/ (all subfolders)

Using the template and existing content, draft a README.md for the pillar's 00_CANON/ folder.

Include:
- Pillar purpose
- What belongs here vs. what doesn't
- Folder structure
- Key frameworks (extracted from existing content)
- Related pillars (from domain registry dependencies)
- Quick start for working in this pillar

Show me the draft. I'll review it before it goes into 00_CANON/.

Remember: 00_CANON/ is read-only without my approval. Show me the draft first.
```

---

# MAINTENANCE PROMPTS

## Prompt 19: Generate a State Snapshot

```
Create a new system state snapshot.

1. Read the latest snapshot in: 01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/
2. Run: python 03_CORE_ENGINE/SCRIPTS/v7_daily.py --quick
3. Check: 07_BUILD_FACTORY/ for project status updates

Create: 01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/[TODAY'S DATE].md

Include:
- Date
- Overall system health (green/yellow/red)
- Active goals and progress
- Project status for each active project
- What was accomplished since last snapshot
- Current blockers
- Next priorities

Base this on actual data, not assumptions.
```

## Prompt 20: Audit Naming Conventions

```
Audit naming conventions across the V7 system.

1. Read: 00_SYSTEM_ROOT/NAMING_CONVENTIONS.md
2. Scan all files created or modified in the last [7/14/30] days:
   git log --since="[N] days ago" --name-only --pretty=format: | sort -u

For each file, check:
- [ ] No spaces (underscores only)
- [ ] No special characters except hyphens and underscores
- [ ] Canon/system files are UPPERCASE_UNDERSCORES.md
- [ ] Date-based files use YYYY-MM-DD format
- [ ] No forbidden names (temp, test, new, untitled, draft)
- [ ] File is in the correct location per routing rules

Report violations as a table:
| File | Violation | Suggested Fix |

Do NOT rename anything. Just report. I'll decide what to fix.
```

---

# MULTI-LLM COORDINATION PROMPTS

## Prompt 21: Hand Off to a Different LLM

```
I'm switching to a different LLM for the next part of this work.

Before I go, give me a handoff brief I can paste into the new session:

1. What we worked on today
2. Current state of the work (what's done, what's in progress, what's not started)
3. Files created or modified (full paths)
4. Decisions made that the next LLM needs to know
5. Critical rules that must be followed (the short version)
6. What the next step should be

Format it as a single block I can copy-paste.
```

## Prompt 22: Resume From a Previous LLM Session

```
I'm continuing work that was started in a previous LLM session.

Here's the handoff brief from that session:
[PASTE HANDOFF BRIEF HERE]

Before continuing:
1. Verify the files mentioned in the brief exist at the stated paths
2. Read the most recent session log in 02_COMMAND_DECK/ACTIVE_SESSIONS/
3. Tell me if anything in the handoff brief doesn't match the current state

Then pick up where the previous session left off.

SESSION RULES:
[same rules as Prompt 1]
```

---

# QUICK REFERENCE

| I Want To... | Use Prompt # |
|-------------|-------------|
| Start a new session | 1 |
| Work on a specific project | 2 |
| Wrap up a session | 3 |
| Ingest a document | 4 |
| Run the intake pipeline | 5 |
| Extract from an AI thread (manual) | 6 |
| Search for files | 7 |
| Inventory a pillar | 8 |
| Rebuild file index | 9 |
| Update database | 10 |
| **Extract: 27-domain pass** | **10A** |
| **Extract: copy/sales** | **10B** |
| **Extract: book** | **10C** |
| **Extract: EKX-1 thread** | **10D** |
| **Extract: batch folder** | **10E** |
| **Search my extractions** | **10F** |
| **Ingest content (full workflow)** | **10G** |
| Create a PRD | 11 |
| Start a new project | 12 |
| Process a UI kit | 13 |
| Match PRD to UI kits | 14 |
| Run health check | 15 |
| Recover from mistakes | 16 |
| Write copy | 17 |
| Create a canon doc | 18 |
| Generate state snapshot | 19 |
| Audit naming | 20 |
| Hand off to another LLM | 21 |
| Resume from another LLM | 22 |

---

*This document is part of the Owner's Manual suite. See also: OWNERS_MANUAL.md, SYSTEM_CAPABILITIES.md, RULES_AND_ENFORCEMENT.md, MAINTENANCE_DRILLS.md*
