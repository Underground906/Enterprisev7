# CLAUDE CODE WALKTHROUGH — Enterprise_OS V7 Setup

> **Instructions for Claude Code:** Read this file at the start of every session.
> Walk John through ONE STEP at a time. Do not dump information.
> After each step, confirm it worked, then ask "Ready for the next step?"
> If something breaks, fix it before moving on.
> Track progress by checking off completed steps below.

---

## HOW TO USE THIS FILE

John — just open Claude Code and say:
"Read WALKTHROUGH.md and take me through the next step."

Claude Code will find where you left off and guide you through it.

---

## PROGRESS TRACKER

Mark each step [x] when done. Claude Code should update this file after each step.

### PHASE 1: GET THE SYSTEM ON GITHUB (30 min)
- [ ] Step 1.1 — Place the foundation files
- [ ] Step 1.2 — Git init and first commit
- [ ] Step 1.3 — Push to GitHub
- [ ] Step 1.4 — Verify CLAUDE.md works

### PHASE 2: MAKE THE SCRIPTS WORK (30 min)
- [ ] Step 2.1 — Place scripts in correct folders
- [ ] Step 2.2 — Test generate_indices.py
- [ ] Step 2.3 — Test session_logger.py
- [ ] Step 2.4 — Test intake_processor.py

### PHASE 3: START YOUR FIRST REAL SESSION (20 min)
- [ ] Step 3.1 — Start a session
- [ ] Step 3.2 — Create your first goal
- [ ] Step 3.3 — Do one small task and log it
- [ ] Step 3.4 — End the session

### PHASE 4: FILL THE CRITICAL PILLARS (1-2 hours, can split across days)
- [ ] Step 4.1 — PIL_15 Enterprise OS canon doc
- [ ] Step 4.2 — PIL_01 Avatars canon doc
- [ ] Step 4.3 — PIL_17 RAG System canon doc
- [ ] Step 4.4 — Run generate_indices.py to verify health

### PHASE 5: TEST THE FULL LOOP (30 min)
- [ ] Step 5.1 — Drop 3 real files through intake
- [ ] Step 5.2 — Check routing worked
- [ ] Step 5.3 — Update indices
- [ ] Step 5.4 — Review system health report

### PHASE 6: PROPERTY CONNECT LONDON KICKOFF (1 hour)
- [ ] Step 6.1 — Create the PRD
- [ ] Step 6.2 — Set up the goal tracker entry
- [ ] Step 6.3 — First sprint plan
- [ ] Step 6.4 — Commit and snapshot

---

## STEP-BY-STEP INSTRUCTIONS

### Step 1.1 — Place the foundation files

**What we're doing:** Putting 5 new files into the root of your ENTERPRISE_OS_V7 folder.

**Claude Code should:**
1. Check if ENTERPRISE_OS_V7 exists at expected location (likely `C:\Users\under\ENTERPRISE_OS_V7` or `C:\Users\under\Documents\ENTERPRISE_OS_V7`)
2. Copy these files to the ROOT of that folder:
   - `README.md` — repo overview
   - `CLAUDE.md` — context file for you (Claude Code)
   - `.gitignore` — keeps the repo clean
   - `DOMAIN_REGISTRY.json` → goes to `03_CORE_ENGINE/INDICES/DOMAIN_REGISTRY.json`
3. Confirm each file is in place

**Verify:** Run `dir` or `ls` in the ENTERPRISE_OS_V7 root. You should see README.md, CLAUDE.md, .gitignore alongside the 00-08 folders.

---

### Step 1.2 — Git init and first commit

**What we're doing:** Turning this folder into a git repo.

**Claude Code should:**
1. `cd` into the ENTERPRISE_OS_V7 folder
2. Run `git init`
3. Run `git add .`
4. Run `git status` — confirm V7_ARCHIVE files are NOT being tracked (gitignore working)
5. Run `git commit -m "V7.0 — Initial structure with 23 domain pillars"`

**Verify:** `git log` shows one commit. `git status` shows clean working tree.

---

### Step 1.3 — Push to GitHub

**What we're doing:** Getting this on GitHub so it's backed up and versioned.

**Claude Code should:**
1. Ask John: "Do you have a GitHub account? Do you have the GitHub CLI (`gh`) installed?"
2. If yes to both: `gh repo create enterprise-os-v7 --private --source=. --push`
3. If no CLI: Guide through creating a repo on github.com and pushing manually
4. If no account: Help set one up, or skip this step and come back later

**Verify:** `git remote -v` shows a GitHub URL. The repo exists on GitHub.

---

### Step 1.4 — Verify CLAUDE.md works

**What we're doing:** Making sure Claude Code can read the system context.

**Claude Code should:**
1. Read CLAUDE.md from the repo root
2. Confirm it can see: architecture overview, pillar list, active goals, rules
3. Read 00_SYSTEM_ROOT/MASTER_CONTEXT.md
4. Confirm it understands the 27 extraction domains
5. Say back to John in 2-3 sentences: "Here's what I understand about your system..."

**Verify:** Claude Code can accurately describe the system without being told.

---

### Step 2.1 — Place scripts in correct folders

**What we're doing:** Putting the 3 core scripts where they belong.

**Claude Code should:**
1. Copy `generate_indices.py` → `03_CORE_ENGINE/SCRIPTS/generate_indices.py`
2. Copy `session_logger.py` → `03_CORE_ENGINE/SCRIPTS/session_logger.py`
3. Copy `intake_processor.py` → `03_CORE_ENGINE/SCRIPTS/intake_processor.py`
4. Make all three executable: `chmod +x` on each (Linux/Mac) or just confirm they're .py files (Windows)

**Verify:** `ls 03_CORE_ENGINE/SCRIPTS/` shows all 3 scripts.

---

### Step 2.2 — Test generate_indices.py

**What we're doing:** Scanning the system and creating the first machine-readable index.

**Claude Code should:**
1. Run: `python 03_CORE_ENGINE/SCRIPTS/generate_indices.py`
2. Check output: should say "Found XX files (excluding archives)"
3. Verify `03_CORE_ENGINE/INDICES/FILE_INDEX.json` was created
4. Verify `03_CORE_ENGINE/INDICES/SYSTEM_HEALTH.md` was created
5. Read SYSTEM_HEALTH.md and tell John the headlines: total files, empty dirs, pillar health

**If it fails:** Check Python 3 is installed (`python3 --version` or `python --version`). The script has zero dependencies — just Python standard library.

---

### Step 2.3 — Test session_logger.py

**What we're doing:** Making sure work tracking works.

**Claude Code should:**
1. Run: `python 03_CORE_ENGINE/SCRIPTS/session_logger.py start "Testing the session logger"`
2. Confirm it says "Session started"
3. Run: `python 03_CORE_ENGINE/SCRIPTS/session_logger.py log "This is a test entry"`
4. Confirm it says "Logged"
5. Run: `python 03_CORE_ENGINE/SCRIPTS/session_logger.py status`
6. Confirm it shows the active session
7. Run: `python 03_CORE_ENGINE/SCRIPTS/session_logger.py end`
8. Confirm session ended
9. Show John the session file that was created in `02_COMMAND_DECK/ACTIVE_SESSIONS/`

**If it fails:** Same as above — just needs Python 3, no dependencies.

---

### Step 2.4 — Test intake_processor.py

**What we're doing:** Making sure the routing engine works.

**Claude Code should:**
1. Create a test file: write a short .md file about "property market keywords and London estate agents" and save it to `04_KNOWLEDGE_LIBRARY/EXTRACTION_PIPELINE/RAW_INTAKE/test_property.md`
2. Run: `python 03_CORE_ENGINE/SCRIPTS/intake_processor.py --dry-run`
3. Confirm it routes to PIL_19_PROPERTY
4. Create another test file about "copywriting formulas and headlines" → save to RAW_INTAKE
5. Run dry-run again — confirm it routes to PIL_03_COPY
6. Now run WITHOUT dry-run: `python 03_CORE_ENGINE/SCRIPTS/intake_processor.py`
7. Confirm files moved to correct pillar folders
8. Check the routing log was created in `03_CORE_ENGINE/ROUTING_ENGINE/routing_logs/`

**If it fails:** Make sure DOMAIN_REGISTRY.json is in `03_CORE_ENGINE/INDICES/`.

---

### Step 3.1 — Start a real session

**What we're doing:** Using the system for real work for the first time.

**Claude Code should:**
1. Run: `python 03_CORE_ENGINE/SCRIPTS/session_logger.py start "Enterprise OS V7 — First operational session"`
2. Confirm session started
3. Tell John: "You're now inside the system. Everything from here gets logged."

---

### Step 3.2 — Create your first goal

**What we're doing:** Setting up the Property Connect London goal in the navigation centre.

**Claude Code should:**
1. Create the folder: `01_NAVIGATION_CENTRE/ACTIVE_GOALS/GOAL_Property_Connect_London/`
2. Inside it, create these subfolders: `01_Alignment/`, `02_Awareness/`, `03_Accountabilities/`, `04_Activities/`, `05_Assets/`, `06_State/`
3. Create `06_State/progress.md` with this content:

```markdown
# Property Connect London — Progress

**Target:** 2026-02-28
**Priority:** 1
**Status:** In Progress
**Progress:** 10%

## Milestones
- [ ] System infrastructure operational
- [ ] Market research complete
- [ ] Avatar definitions done
- [ ] Keyword research done
- [ ] MVP chatbot built
- [ ] Landing page live
- [ ] First customer onboarded

## Latest Update
2026-02-04: Enterprise_OS V7 operational. Beginning structured buildout.
```

4. Log the action: `python 03_CORE_ENGINE/SCRIPTS/session_logger.py log "Created GOAL_Property_Connect_London with progress tracking"`

---

### Step 3.3 — Do one small task and log it

**What we're doing:** Proving the system works end-to-end.

**Claude Code should:**
1. Create a simple state snapshot: `01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/2026-02-04_operational.md`
2. Put in it:

```markdown
# STATE SNAPSHOT — 2026-02-04

## System Status
- Enterprise_OS V7: Operational
- Core scripts: Working (indices, sessions, intake)
- GitHub: [Connected/Pending]

## Active Goals
1. Property Connect London — 10% — Target Feb 28
2. Enterprise_OS Core Scripts — 80% — Scripts built and tested

## Today's Wins
- System went operational
- 3 core scripts tested and working
- First session logged
- First goal created

## Tomorrow's Focus
- Fill critical pillar canon docs (PIL_15, PIL_01, PIL_17)
- Drop first real content through intake pipeline
```

3. Log it: `python 03_CORE_ENGINE/SCRIPTS/session_logger.py log "Created first operational state snapshot"`

---

### Step 3.4 — End the session

**Claude Code should:**
1. Run: `python 03_CORE_ENGINE/SCRIPTS/session_logger.py end`
2. Run: `python 03_CORE_ENGINE/SCRIPTS/generate_indices.py` to capture all new files
3. Commit to git: `git add . && git commit -m "System operational — core scripts, first goal, first snapshot"`
4. Push if remote is set up: `git push`
5. Tell John: "Session complete. Here's what was created: [list files]. Tomorrow we fill the pillars."

---

### Step 4.1 — PIL_15 Enterprise OS canon doc

**What we're doing:** The meta-pillar that governs the system itself needs a README.

**Claude Code should:**
1. Start a session: `python 03_CORE_ENGINE/SCRIPTS/session_logger.py start "Filling PIL_15 Enterprise OS canon"`
2. Create `06_DOMAIN_PILLARS/PIL_15_ENTERPRISE_OS/00_CANON/README.md`
3. Content should cover: what Enterprise_OS is, the 8 components, the 23 pillars, governance rules (canon vs staging), how the system evolves, versioning approach
4. Pull key info from `00_SYSTEM_ROOT/MASTER_CONTEXT.md` — don't duplicate, reference it
5. Log: `session_logger.py log "Created PIL_15 canon README"`

---

### Step 4.2 — PIL_01 Avatars canon doc

**What we're doing:** Customer avatars power everything downstream — copy, content, keywords.

**Claude Code should:**
1. Create `06_DOMAIN_PILLARS/PIL_01_AVATARS/00_CANON/README.md`
2. Content should include:
   - What an avatar is and why it matters
   - The avatar template structure (demographics, psychographics, pain points, desires, objections, language)
   - How avatars connect to PIL_03_COPY, PIL_12_KEYWORDS, PIL_04_CONTENT
   - The 7 property market pillars (buying, selling, renting, letting, investing, renovating, building)
3. Create one example avatar file: `06_DOMAIN_PILLARS/PIL_01_AVATARS/02_FRAMEWORKS/avatar_template.md`
4. Log it

---

### Step 4.3 — PIL_17 RAG System canon doc

**What we're doing:** The RAG system powers search and AI products.

**Claude Code should:**
1. Create `06_DOMAIN_PILLARS/PIL_17_RAG_SYSTEM/00_CANON/README.md`
2. Content should cover:
   - Purpose: making all Enterprise_OS knowledge searchable and retrievable
   - Chunking rules (by header for markdown, by function for code, max 500 tokens)
   - Embedding model choice (text-embedding-3-small recommended)
   - Local vector store (ChromaDB for development)
   - Retrieval strategy (hybrid: vector + keyword)
   - What gets indexed (canon docs first, then ongoing, then archive)
3. Log it

---

### Step 4.4 — Run indices and verify

**Claude Code should:**
1. Run: `python 03_CORE_ENGINE/SCRIPTS/generate_indices.py`
2. Read SYSTEM_HEALTH.md
3. Confirm: PIL_15, PIL_01, PIL_17 now show as "has_docs" instead of "empty"
4. Tell John the updated pillar health summary
5. End session and commit: `git add . && git commit -m "Filled critical pillar canon docs — PIL_15, PIL_01, PIL_17"`

---

### Step 5.1 — Drop 3 real files through intake

**What we're doing:** Testing the full pipeline with actual content.

**Claude Code should:**
1. Start a session
2. Ask John: "Do you have any markdown files, research notes, or chat exports you want to add to the system? Drop them in `04_KNOWLEDGE_LIBRARY/EXTRACTION_PIPELINE/RAW_INTAKE/`"
3. If John doesn't have files ready, Claude Code should create 3 realistic ones:
   - A property market research note (should route to PIL_19)
   - A UI component spec (should route to PIL_07)
   - A branding guidelines note (should route to PIL_02)
4. Run dry-run first: `python 03_CORE_ENGINE/SCRIPTS/intake_processor.py --dry-run`
5. Show John where each would go
6. Ask: "Happy with the routing? Run for real?"
7. Run actual: `python 03_CORE_ENGINE/SCRIPTS/intake_processor.py`

---

### Step 5.2 — Check routing worked

**Claude Code should:**
1. Check each destination folder — confirm files arrived
2. Check routing log in `03_CORE_ENGINE/ROUTING_ENGINE/routing_logs/`
3. Check UNROUTED folder — anything there?
4. Show John the results

---

### Step 5.3 — Update indices

**Claude Code should:**
1. Run: `python 03_CORE_ENGINE/SCRIPTS/generate_indices.py`
2. Confirm FILE_INDEX.json now includes the newly routed files
3. Show updated file counts per pillar

---

### Step 5.4 — Review system health

**Claude Code should:**
1. Read SYSTEM_HEALTH.md
2. Compare to the first health report (Step 2.2)
3. Tell John: "Here's what changed since we started: X more files, Y pillars improved, Z still empty"
4. End session, commit, push

---

### Step 6.1 — Create the Property Connect London PRD

**What we're doing:** Turning the revenue goal into a concrete product spec.

**Claude Code should:**
1. Start a session
2. Create `07_BUILD_FACTORY/PRJ_Property_Connect_London/02_Product/PRD_v1.md`
3. Work WITH John to fill in:
   - Product name and one-line description
   - Target user (pull from PIL_01 avatar if created)
   - Core features (AI property chatbot, market intelligence)
   - Tech stack (React + Claude API, as noted in LATEST_THINKING.md)
   - Revenue model (£149/mo as per existing docs)
   - MVP scope (what's in v1 vs later)
4. This should be CONVERSATIONAL — ask John questions, don't just generate

---

### Step 6.2 — Set up goal tracker entry

**Claude Code should:**
1. Update `01_NAVIGATION_CENTRE/ACTIVE_GOALS/GOAL_Property_Connect_London/06_State/progress.md`
2. Link to the PRD
3. Update milestones based on what was decided in the PRD
4. Log it

---

### Step 6.3 — First sprint plan

**Claude Code should:**
1. Create `07_BUILD_FACTORY/PRJ_Property_Connect_London/01_Strategy/sprint_2026-02-W1.md`
2. Work with John to define: what are the 3-5 things to build THIS WEEK?
3. Keep it concrete: each item should be completable in 1-2 hours
4. Log it

---

### Step 6.4 — Commit and snapshot

**Claude Code should:**
1. Create a state snapshot for today
2. Run generate_indices.py
3. End session
4. Git commit and push
5. Tell John: "Property Connect London is now set up in the system with a PRD, sprint plan, and goal tracking. Tomorrow we start building."

---

## AFTER THE WALKTHROUGH

Once all 6 phases are done, the daily workflow becomes:

1. Open Claude Code
2. Say: "Read CLAUDE.md. Start a session."
3. Work on whatever's next
4. Claude Code logs everything, routes files, updates indices
5. End session when done

The system is now self-maintaining. You work, it records.

---

## TROUBLESHOOTING

**"Can't find ENTERPRISE_OS_V7"**
→ Tell Claude Code where the folder is. It will update the scripts.

**"Python not found"**
→ Install Python 3.11+ from python.org. On Windows, check "Add to PATH" during install.

**"Git not found"**
→ Install from git-scm.com. Restart terminal after install.

**"Script throws an error"**
→ Tell Claude Code the error message. It can fix scripts in-place.

**"I don't know where to put a file"**
→ Drop it in RAW_INTAKE and run the intake processor. If it goes to UNROUTED, ask Claude Code to help classify it.

**"I want to change the pillar structure"**
→ Edit DOMAIN_REGISTRY.json, then run generate_indices.py. The system adapts.
