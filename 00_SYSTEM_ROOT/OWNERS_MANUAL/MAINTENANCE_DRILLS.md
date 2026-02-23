# ENTERPRISE OS V7 — MAINTENANCE DRILLS

> **Health checks and audits you can run at any time.**
> Each drill: what to run, what to look for, what healthy looks like, what to do if unhealthy.
> Last updated: 2026-02-20

---

## How to Use This Document

Pick the drill based on your situation:

| Situation | Which Drill |
|-----------|-------------|
| Start of day, quick sanity check | **Daily Quick Health Check** (5 min) |
| End of week, verify system integrity | **Weekly Audit** (15-30 min) |
| Monthly review, deep dive | **Monthly Deep Health** (45-60 min) |
| After a bad session / LLM mistakes | **Post-Incident Check** |
| After a large batch operation | **Post-Batch Verification** |
| Something feels off but you're not sure what | **Targeted Diagnostics** |

---

# DRILL 1: DAILY QUICK HEALTH CHECK (5 minutes)

Run this every morning or at the start of your first session.

## Step 1: Run the Daily Script

```bash
python 03_CORE_ENGINE/SCRIPTS/v7_daily.py --quick
```

**What it does:** Scans for changes since last run, generates health report.

**Healthy result:** Shows recent changes, no errors, health report generated.

**Unhealthy result:** Script errors, missing database connection, or unexpected file changes.

## Step 2: Check the V7 Root

```bash
ls C:/Users/under/Downloads/ENTERPRISE_OS_V7/
```

**What to look for:** Only the 8 component folders (00-08), `.git`, and `CLAUDE.md`.

**Healthy:** Exactly those items, nothing else.

**Unhealthy:** Extra files or folders in the root. These are strays from a bad session.

**Fix:** Identify the stray. Route it to the correct location per the routing manifest.

## Step 3: Check Latest State Snapshot

Open the latest file in `01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/`.

**What to look for:** Date should be recent (today or yesterday). Content should reflect the actual system state.

**Healthy:** Date matches today or yesterday. Priorities and status are current.

**Unhealthy:** Snapshot is more than 3 days old. Run `v7_daily.py` (full run) to generate a fresh one.

## Step 4: Check Git Status

```bash
cd C:/Users/under/Downloads/ENTERPRISE_OS_V7
git status
```

**Healthy:** `nothing to commit, working tree clean` — or only expected uncommitted changes from current work.

**Unhealthy:** Hundreds of uncommitted changes, or unexpected modifications to files you didn't touch. Investigate before doing anything else.

## Step 5: Quick Gut Check

Ask yourself:
- Did the last session end cleanly? (Check session log exists)
- Were any batch operations running? (Check for incomplete outputs)
- Is anything blocked that needs attention?

**Time: ~5 minutes total.**

---

# DRILL 2: WEEKLY AUDIT (15-30 minutes)

Run this at the end of each work week.

## 2A: Naming Convention Audit

**What to check:** All files created in the past week follow naming conventions.

**How to run:**
```bash
# See what files changed this week:
git log --since="7 days ago" --name-only --pretty=format: | sort -u
```

**For each file, verify:**
- [ ] No spaces in name (underscores only)
- [ ] No special characters except hyphens and underscores
- [ ] Canon/system files are UPPERCASE_UNDERSCORES.md
- [ ] Date-based files use YYYY-MM-DD format
- [ ] No generic names (temp, test, new, untitled, draft)

**If violations found:** Rename the file. Update any references to the old name.

## 2B: Routing Audit

**What to check:** All files are in the correct location per the routing manifest.

**How to run:**
```bash
# Check for files in UNROUTED:
ls 04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/
```

**For UNROUTED files:**
- Can any of them now be routed? (New context, more keywords defined)
- Are there files that have been UNROUTED for more than 2 weeks? Flag them.

**Also check:**
- Were any files placed in odd locations this week? (Cross-reference with `git log --name-only`)
- Are project files in project folders? (Not scattered across pillars)

## 2C: Stale Content Check

**What to check:** Files in active pillars that haven't been touched in too long.

**How to run:**
```bash
python 03_CORE_ENGINE/SCRIPTS/v7_daily.py
# Check the "stale files" section of the health report
```

**What "stale" means depends on the pillar:**
- Fast-changing pillars (PIL_19_PROPERTY, PIL_07_UI_LIBRARY): stale after 7-14 days
- Slow-changing pillars (PIL_02_BRANDING, PIL_13_SEO): stale after 30-60 days
- These thresholds are set in `DOMAIN_REGISTRY.json` under `freshness_days`

**If stale content found:** Decide whether to update it, archive it, or leave it (if it's still correct, reset the staleness clock).

## 2D: Orphaned Content Check

**What to check:** Files that exist on disk but aren't in FILE_INDEX.json or the database.

**How to run:**
```bash
# Regenerate the index:
python 03_CORE_ENGINE/SCRIPTS/generate_indices.py
# Compare the "new files found" output with what you expect
```

**Healthy:** All files are indexed. Any new files are ones you created.

**Unhealthy:** Files that shouldn't exist (temp files, accidental outputs), or files you created that didn't get indexed (wrong location or excluded extension).

## 2E: Extraction Health Check

**What to check:** Extraction outputs from the past week are complete and in both locations.

**How to run:**
```bash
# Check central store for this week's extractions:
ls 04_KNOWLEDGE_LIBRARY/EXTRACTIONS/by_mode/

# Check the extraction index:
# Read EXTRACTION_INDEX.json — does the count match what you extracted this week?

# If PostgreSQL running:
psql -d enterprise_os -c "SELECT mode, COUNT(*) FROM v7_extractions WHERE extracted_at > NOW() - INTERVAL '7 days' GROUP BY mode;"
```

**Verify:**
- Every extraction has both an alongside copy AND a central store copy
- Category aggregates in `by_category/` are up to date
- No extraction errors logged in `03_CORE_ENGINE/ROUTING_ENGINE/extraction_logs/`

## 2F: Session Log Completeness

**What to check:** Every work session this week has a log.

**How to run:**
Check `02_COMMAND_DECK/ACTIVE_SESSIONS/` for the current month folder. Count the session files. Does the count match how many sessions you actually had?

**Also check** `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/SESSION_INDEX.md` — does it list all sessions?

**If sessions are missing:** Create a retroactive summary for any missing session, even if brief.

**Time: 15-30 minutes total.**

---

# DRILL 3: MONTHLY DEEP HEALTH (45-60 minutes)

Run this at the end of each month. This is the thorough audit.

## 3A: Full Daily Run + Review

```bash
python 03_CORE_ENGINE/SCRIPTS/v7_daily.py
```

Read the full output carefully, not just the summary.

## 3B: Database Integrity Check

### PostgreSQL Registry
```bash
# Check if running:
pg_isready -h localhost -p 5432

# Count registered files:
psql -d enterprise_os -c "SELECT COUNT(*) FROM v7_files;"

# Compare with filesystem count:
python 03_CORE_ENGINE/SCRIPTS/generate_indices.py
# Compare the FILE_INDEX.json count with the database count
```

**Healthy:** Database count roughly matches filesystem count (within 5% — some files are excluded from indexing).

**Unhealthy:** Large discrepancy. Run a full database rescan:
```bash
python 03_CORE_ENGINE/SCRIPTS/v7_registry.py scan
```

### ChromaDB
```bash
# Start the search API and check health:
python 03_CORE_ENGINE/SCRIPTS/v7_search_api.py &
# Wait a few seconds, then:
curl http://localhost:8100/health
```

**Healthy:** Returns embedding count, no errors.

**Unhealthy:** Connection error, zero embeddings, or count way lower than expected.

### UI Library Database
```bash
psql -d ui_library -c "SELECT COUNT(*) FROM items;"
```

**Expected:** ~19,837 items. If significantly different, investigate.

## 3C: Pillar Completeness Audit

Go through each of the 23 pillars and check:

| Check | How |
|-------|-----|
| Folder exists | `ls 06_DOMAIN_PILLARS/` |
| Has 00_CANON | `ls 06_DOMAIN_PILLARS/PIL_NN_*/00_CANON/` |
| Has content (not empty) | File count > 0 in at least one subfolder |
| Has routing rules defined | Check `DOMAIN_REGISTRY.json` for `routing_keywords` |
| Canon docs are current | Check last modified date of canon files |

**Track progress:** Note which pillars gained canon docs this month. Target: fill at least 1 empty pillar per month.

**Current empty pillars (as of 2026-02-20):** PIL_01, PIL_09, PIL_11, PIL_16, PIL_17, PIL_22, PIL_23

## 3D: Goal Progress Review

Open `01_NAVIGATION_CENTRE/ACTIVE_GOALS/` and review:

- Are the goals still relevant?
- Have priorities changed?
- What percentage progress on each?
- Are any goals blocked? By what?

Update the goals document and create a new state snapshot.

## 3E: Project State Audit

For each active project in `07_BUILD_FACTORY/PRJ_*/`:

1. Open `PROJECT_STATE.md`
2. Is it up to date?
3. Do the vital counts match reality?
4. Are the carry-forward items still accurate?
5. Are there blocked items that need attention?

## 3F: Git History Review

```bash
git log --oneline -30
```

**Check:**
- Are commits regular? (At least one per work session)
- Are commit messages descriptive? (Not "update" or "changes")
- Are there any commits you don't recognize?

## 3G: Template Completeness Check

Open `05_TEMPLATE_HUB/` and verify:
- Agent templates exist and are current
- PRD templates match the current spec
- Pillar doc templates are complete
- Session templates match current workflow

**Time: 45-60 minutes total.**

---

# DRILL 4: POST-INCIDENT CHECK

Run this after something went wrong during a session (LLM deleted files, wrong routing, broken structure, etc.).

## Step 1: Stop Everything
Don't do more work until you've assessed the damage.

## Step 2: Assess the Damage

```bash
# What changed since the last good commit?
git diff --name-status HEAD

# What's the last good commit?
git log --oneline -10
```

**Read the output carefully:**
- `M` = Modified (check if the modification was intended)
- `D` = Deleted (this is a problem — files should never be deleted)
- `A` = Added (check if the file is in the right location)
- `R` = Renamed (was this approved?)

## Step 3: Categorize the Damage

| Damage Type | Severity | Action |
|-------------|----------|--------|
| Files deleted | HIGH | Restore from git: `git checkout HEAD -- path/to/file` |
| Files moved without approval | HIGH | Move them back: check git for original paths |
| Files in wrong location | MEDIUM | Route them correctly |
| Canon files edited without approval | MEDIUM | Revert: `git checkout HEAD -- path/to/canon/file` |
| Wrong naming convention | LOW | Rename to correct convention |
| Extra temp files created | LOW | Delete the temp files |
| Counts don't match | VARIES | Recount. Investigate discrepancy. |

## Step 4: Restore

For each damaged file:
```bash
# Restore a specific file to its state at the last commit:
git checkout HEAD -- "path/to/file"

# Or restore to a specific older commit:
git checkout <commit-hash> -- "path/to/file"
```

## Step 5: Verify Recovery

```bash
# Rebuild the index:
python 03_CORE_ENGINE/SCRIPTS/generate_indices.py

# Check the health:
python 03_CORE_ENGINE/SCRIPTS/v7_daily.py --quick
```

## Step 6: Document the Incident

Add to the disaster log (in your `CLAUDE.md` or a dedicated log file):
- What happened
- What went wrong
- How it was fixed
- How to prevent it next time

---

# DRILL 5: POST-BATCH VERIFICATION

Run this after any batch operation (processing many files, API calls, bulk ingestion, etc.).

## Step 1: Count Check

| What | Value |
|------|-------|
| Files/items expected | [The count you expected before the batch] |
| Files/items actually processed | [The count reported by the batch] |
| Match? | [Yes/No] |

If they don't match, identify the gap before continuing.

## Step 2: Output Location Check

```bash
# List the output folder:
ls [output_folder]/
# Count the files:
ls [output_folder]/ | wc -l
```

**Verify:** All outputs are in the single designated folder. None scattered elsewhere.

## Step 3: Error Check

If the batch had any errors:
- How many items failed?
- Which specific items failed?
- Were failures logged?
- Do the failed items need to be reprocessed?

## Step 4: Quality Spot-Check

Open 3-5 random output files and verify:
- Content is complete (not truncated)
- Content is correct (not garbled or mismatched)
- Naming is correct
- File is in the right location

## Step 5: Checkpoint Verification

If checkpoints were used:
- Does the last checkpoint match the total item count?
- Is the checkpoint file accessible for potential resume?

---

# DRILL 6: TARGETED DIAGNOSTICS

For when something specific feels off. Pick the symptom, follow the diagnostic.

## Symptom: "I can't find a file I know exists"

1. Search the file index: `grep "filename" 03_CORE_ENGINE/INDICES/FILE_INDEX.json`
2. Search the filesystem: `find . -name "filename*"` (in the V7 root)
3. Search git history: `git log --all --full-history -- "**/filename*"`
4. Check UNROUTED: `ls 04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/`
5. Check 90_ARCHIVE folders in the expected pillar

## Symptom: "File counts don't match what I expect"

1. State what you expect and why
2. Count using the explicit method: `ls [folder]/*.md | wc -l` (or equivalent)
3. Count using the index: `grep "[folder]" FILE_INDEX.json | wc -l`
4. Count using the database: `SELECT COUNT(*) FROM v7_files WHERE file_path LIKE '%[folder]%'`
5. If all three disagree: the filesystem count is truth. Rebuild the index and rescan the database.

## Symptom: "The LLM doesn't seem to know about recent changes"

1. Check the latest state snapshot: is it current?
2. Check the session index: does it include the last session?
3. Check if git commit was done after the last session
4. Verify the LLM is reading the right files (ask it: "What's the date of the latest state snapshot you've seen?")

## Symptom: "A script isn't working"

1. Check if PostgreSQL is running: `pg_isready -h localhost -p 5432`
2. Check Python version: `python --version` (needs 3.11+)
3. Check if dependencies are installed: `pip list | grep [package]`
4. Run the script with verbose output if available
5. Check the script's log files in `03_CORE_ENGINE/ROUTING_ENGINE/routing_logs/`

## Symptom: "Search returns wrong or no results"

1. Is the search API running? `curl http://localhost:8100/health`
2. Is ChromaDB populated? Check the health endpoint for embedding count
3. Is FILE_INDEX.json current? Check its modification date
4. Is PostgreSQL registry current? Run `v7_registry.py scan`
5. Try a different search method (SQL vs semantic vs file index)

## Symptom: "Git is in a weird state"

```bash
# Check what's going on:
git status

# If there are merge conflicts:
git diff --name-only --diff-filter=U

# If HEAD is detached:
git checkout master

# If you need to undo the last commit (but keep the files):
git reset --soft HEAD~1

# Nuclear option — discard everything since last commit:
# WARNING: This loses all uncommitted work
git checkout -- .
```

---

# SCHEDULE REFERENCE

| Drill | When | Time | Priority |
|-------|------|------|----------|
| Daily Quick Health Check | Every morning / session start | 5 min | Required |
| Weekly Audit | Friday or end of work week | 15-30 min | Required |
| Monthly Deep Health | Last day of month | 45-60 min | Required |
| Post-Incident Check | After any LLM mistake | As needed | Urgent |
| Post-Batch Verification | After any batch operation | 10-15 min | Required |
| Targeted Diagnostics | When something feels off | As needed | As needed |

---

*This document is part of the Owner's Manual suite. See also: OWNERS_MANUAL.md, SYSTEM_CAPABILITIES.md, RULES_AND_ENFORCEMENT.md, PROMPT_LIBRARY.md*
