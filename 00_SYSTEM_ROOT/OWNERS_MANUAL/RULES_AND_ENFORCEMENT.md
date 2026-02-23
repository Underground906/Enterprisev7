# ENTERPRISE OS V7 — RULES AND ENFORCEMENT

> **Every rule in one place.** Each rule has: what it is, why it exists, how to check it, what to do when it's broken.
> Last updated: 2026-02-20

---

## How to Use This Document

When starting a session with any LLM, paste the relevant rules or tell it to read this file. During a session, use this as your reference when something looks wrong. After a session, use the "How to Check" column to verify nothing was violated.

---

# PART 1: FILE OPERATION RULES

## Rule 1: Never Delete Files

| | |
|---|---|
| **The Rule** | No file is ever deleted. Unwanted files are moved to `90_ARCHIVE/` in their current folder. |
| **Why It Exists** | Disaster 3: Claude Code deleted 11 raw files from current_work during a "cleanup". Hours spent recovering from Downloads folder. |
| **How to Check** | After any session: `git diff --name-only HEAD` — look for "D" (deleted) entries. If any show deleted, investigate immediately. |
| **When It's Broken** | 1. Check `git log` for the last commit before deletion. 2. Restore with `git checkout HEAD~1 -- path/to/deleted/file`. 3. Move restored file to `90_ARCHIVE/` if it genuinely needs retiring. |

## Rule 2: Never Move Files Without Explicit Approval

| | |
|---|---|
| **The Rule** | No file is moved from one location to another without the human stating "Yes, move [file] from [A] to [B]." |
| **Why It Exists** | Disaster 1: An unsolicited "reorganization" destroyed the provenance mapping between 681 raw threads and their EKX1 summaries. 9+ hours to partially fix. |
| **How to Check** | After any session: `git diff --name-only HEAD` — look for pairs where the same filename appears as both deleted (old location) and added (new location). |
| **When It's Broken** | 1. Identify all moved files from `git diff`. 2. Move them back to their original locations. 3. Run `generate_indices.py` to rebuild the index. |

## Rule 3: Never Rename Files Without Explicit Approval

| | |
|---|---|
| **The Rule** | No file is renamed without the human approving the old name to new name mapping. |
| **Why It Exists** | Same as Rule 2. Renaming breaks provenance links, references in other files, and any script that uses the old name. |
| **How to Check** | `git diff --name-only HEAD` — renames show as delete + add. |
| **When It's Broken** | Rename back to the original name. Search the codebase for references to the new name and revert those too. |

## Rule 4: Never Overwrite Existing Files

| | |
|---|---|
| **The Rule** | If a file already exists at a path, never write to that path. Use `_v2`, `_new`, or a timestamp suffix instead. |
| **Why It Exists** | Disaster 14: File contents were "updated" without backup — original content lost forever. |
| **How to Check** | During a session, if the LLM says "updating" or "writing to" a file — ask: "Does that file already exist? If yes, are you creating a new version or overwriting?" |
| **When It's Broken** | If caught immediately: `git checkout HEAD -- path/to/overwritten/file` restores the original. If not caught: check `git log -p -- path/to/file` to find the last version with original content. |

## Rule 5: Never Put Outputs in Root Folders

| | |
|---|---|
| **The Rule** | The V7 root should contain only the 8 component folders (00-08), `.git`, and `CLAUDE.md`. Nothing else. All outputs go to designated subfolders. |
| **Why It Exists** | Disaster 4: Analysis files dumped in the root violated the 8-component structure. Had to manually relocate them. |
| **How to Check** | `ls` the V7 root directory. Count the items. Should be exactly: `00_SYSTEM_ROOT`, `01_NAVIGATION_CENTRE`, `02_COMMAND_DECK`, `03_CORE_ENGINE`, `04_KNOWLEDGE_LIBRARY`, `05_TEMPLATE_HUB`, `06_DOMAIN_PILLARS`, `07_BUILD_FACTORY`, `08_OPERATIONS`, plus `.git` and `CLAUDE.md`. Anything else is wrong. |
| **When It's Broken** | Identify the stray file. Determine its correct location using the routing table. Move it there. |

---

# PART 2: NAMING RULES

## Rule 6: Folder Naming Convention

| | |
|---|---|
| **The Rule** | Top-level: `NN_NAME` (uppercase). Pillars: `PIL_NN_NAME`. Projects: `PRJ_Name` (Title_Case). Goals: `GOAL_Name`. Archives: `90_ARCHIVE/`. |
| **Why It Exists** | Disaster 6: Legacy folder names (Pillars/, Factory/, Shared/) were used instead of V7 names, creating files in wrong locations. |
| **How to Check** | Look at any new folders created during a session. Do they follow the pattern? Are they under the correct parent? |
| **When It's Broken** | Rename the folder to the correct convention. Update any references to the old name. Run `generate_indices.py`. |

## Rule 7: File Naming Convention

| | |
|---|---|
| **The Rule** | Canon/system files: `UPPERCASE_UNDERSCORES.md`. Working files: `lowercase_underscores.md`. Date-based: `YYYY-MM-DD_description.ext`. PRDs: `PRD_Descriptive_Name.md`. Backups: `filename_BACKUP_YYYYMMDD.ext`. |
| **Why It Exists** | Consistent naming makes files findable and parseable by scripts. Generic names like `temp.md` or `untitled.md` create confusion. |
| **How to Check** | After a session, list newly created files. Check each name against the convention. Forbidden names: anything with spaces, special characters (except hyphens/underscores), or generic names (temp, test, new, untitled, draft). |
| **When It's Broken** | Rename the file to follow the convention. Update any references. |

## Rule 8: Use Only the 23 Canonical Pillar Names

| | |
|---|---|
| **The Rule** | The only valid pillar names are: |

```
PIL_01_AVATARS          PIL_02_BRANDING         PIL_03_COPY
PIL_04_CONTENT          PIL_05_GRAPHICS         PIL_06_VIDEO
PIL_07_UI_LIBRARY       PIL_08_KNOWLEDGE_INGESTION
PIL_09_ROLES_SKILLS     PIL_10_WORKING_PRACTICES
PIL_11_BUILD_STORY      PIL_12_KEYWORDS         PIL_13_SEO
PIL_14_NAVIGATION       PIL_15_ENTERPRISE_OS
PIL_16_CONTENT_GENERATION   PIL_17_RAG_SYSTEM
PIL_18_AGENT_FRAMEWORK  PIL_19_PROPERTY         PIL_20_FITNESS
PIL_21_MARKET_RESEARCH  PIL_22_VOICE_TRAINING   PIL_23_DOG_PLATFORM
```

| | |
|---|---|
| **Why It Exists** | Disaster 5: An LLM invented "DOG_PLATFORM" and "WILD_CARD_EXPERIMENTS" as pillar names. Broke the taxonomy and made all outputs useless. |
| **How to Check** | If the LLM references a pillar, check it against this list. If you see PIL_24 or higher, or any name not on this list — stop immediately. |
| **When It's Broken** | Correct the pillar reference. Re-route any misclassified content to the correct pillar. |

---

# PART 3: COUNTING AND DATA INTEGRITY RULES

## Rule 9: Count Before and After Every Operation

| | |
|---|---|
| **The Rule** | Before any batch operation, state the file count. After the operation, state the new count. The difference must be explained. |
| **Why It Exists** | Disasters 2, 13: File counts changed between questions in the same session. "About 700" is not a count. Different methods gave different numbers. |
| **How to Check** | When the LLM gives a count, ask: "What exactly did you count? Which folder? Which extensions? Recursive?" If the count changes, demand an explanation. |
| **When It's Broken** | Stop all work. Recount using a single, explicit method. Cache the result. Don't continue until counts are stable and explained. |

## Rule 10: State Exactly What You're Counting

| | |
|---|---|
| **The Rule** | Every count must specify: what folder, what file extension filter (if any), whether recursive, whether hidden files are included. |
| **Why It Exists** | Disaster 13: "Historic has 679 files" then "Historic has 682 files" then "678 files" — all in the same session, because different things were being counted each time. |
| **How to Check** | If the LLM says "there are N files", ask: "N files WHERE? Counted HOW?" |
| **When It's Broken** | Demand specifics. Reject "approximately" or "about" — only exact numbers. |

## Rule 11: Checkpoint After Every Batch Item

| | |
|---|---|
| **The Rule** | During batch processing, save a checkpoint after every single item. Not every 5. Not every 10. Every one. |
| **Why It Exists** | Disaster 11: Processing 768 threads, no checkpoints. Crash at thread 400. Full restart. Wasted API costs. |
| **How to Check** | Before a batch operation starts, ask: "Where will checkpoints be saved? Will you checkpoint after every item?" |
| **When It's Broken** | Stop the batch. Implement checkpointing. Resume from the last successful checkpoint. |

## Rule 12: Never Create Temp Files in Data Folders

| | |
|---|---|
| **The Rule** | Temporary files (lock files, scratch files, intermediate outputs) must never be created inside the V7 data folders. Use a separate temp directory. |
| **Why It Exists** | Disaster 12: Word-style `~$` lock files got counted as real files, corrupting file counts. |
| **How to Check** | After a session, search for temp-looking files: `~$*`, `*.tmp`, `*.bak`, `.~*`. |
| **When It's Broken** | Delete the temp files (they're temp — this is the one case where deletion is appropriate). Recount affected folders. |

---

# PART 4: CONTENT AND STRUCTURE RULES

## Rule 13: Never Edit 00_CANON Without Explicit Approval

| | |
|---|---|
| **The Rule** | Files in any `00_CANON/` folder are production-ready, reviewed, stable. They cannot be edited without the human explicitly saying "Yes, edit [file] in 00_CANON." |
| **Why It Exists** | Canon docs are the source of truth. If an LLM "improves" a canon doc, the source of truth becomes unreliable. |
| **How to Check** | `git diff HEAD -- "*/00_CANON/*"` — if any canon files show changes, verify each one was approved. |
| **When It's Broken** | Revert with `git checkout HEAD -- path/to/canon/file`. If the edit was good but unapproved, save it as a `_proposed_v2` file in `01_INPUT/` for review. |

## Rule 14: Unsure Routing Goes to UNROUTED

| | |
|---|---|
| **The Rule** | If the system (or the LLM) can't determine where content belongs, it goes to `04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/`. Never guess. |
| **Why It Exists** | Guessing creates misrouted content that's harder to find than unrouted content. UNROUTED is a known location you can review regularly. |
| **How to Check** | After ingestion, check UNROUTED. Everything there should have a clear reason why it couldn't be routed. |
| **When It's Broken** | Move the misrouted file to UNROUTED. Manually route it to the correct pillar after review. |

## Rule 15: Never Truncate Content Without Warning

| | |
|---|---|
| **The Rule** | If content is too long to process in one pass, split it into chunks and process all chunks. Never silently cut off content at an arbitrary limit. |
| **Why It Exists** | Disaster 8: Important content at the end of long threads was silently dropped. Analysis based on incomplete data. |
| **How to Check** | For any large file processed: "Did you process the entire file? What was the total length? Did you truncate anything?" |
| **When It's Broken** | Reprocess the full content. Compare outputs from truncated vs full processing. Discard the truncated results. |

## Rule 16: All Outputs Go to a Single Designated Folder

| | |
|---|---|
| **The Rule** | Before any batch or multi-file operation, define the output folder. All outputs go there. No exceptions. No "some here, some there." |
| **Why It Exists** | Disaster 9: Partial outputs scattered across multiple folders. Days spent finding everything. |
| **How to Check** | Before a batch operation: "Where will all outputs be saved?" During: spot-check that outputs are going to the stated folder. After: list the output folder and verify the count matches expectations. |
| **When It's Broken** | Search for scattered outputs. Consolidate to the correct folder. Verify count. |

## Rule 17: Never "Fix" a Structure That Wasn't Complained About

| | |
|---|---|
| **The Rule** | If the folder structure exists and the human hasn't said anything is wrong with it, it is correct. Don't touch it. |
| **Why It Exists** | Disaster 10: Correctly organized epoch folders were "fixed" by an LLM. Files moved between epochs. Folders renamed. Full day to repair. |
| **How to Check** | If the LLM says "I noticed the structure could be improved" or "Let me fix the organization" — that's the trigger. Stop it. |
| **When It's Broken** | Revert with git. Do not let the LLM attempt a "fix of the fix." |

---

# PART 5: SESSION RULES

## Rule 18: Every Session Gets a Log

| | |
|---|---|
| **The Rule** | Every work session must produce a session summary in `02_COMMAND_DECK/ACTIVE_SESSIONS/YYYY-MM/` and a transcript in `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/`. |
| **Why It Exists** | Without session logs, the next session has no context. Continuity breaks. Work gets repeated. |
| **How to Check** | After a session, verify the files exist at the expected paths with the correct naming format (`YYYY-MM-DD_session_NN.md`). |
| **When It's Broken** | Create the missing log retroactively. Include: what was done, what files were touched, what was left unfinished. |

## Rule 19: Git Commit After Every Session

| | |
|---|---|
| **The Rule** | Every session ends with a git commit. Commit message format: `YYYY-MM-DD: Brief description of changes`. |
| **Why It Exists** | Git is the safety net. Without commits, you can't rollback. Without good messages, you can't find what changed when. |
| **How to Check** | `git log --oneline -1` — is the latest commit from today with a descriptive message? |
| **When It's Broken** | Commit now. Better late than never. Include a note that this is a retroactive commit. |

## Rule 20: Verify Paths Exist Before Storing References

| | |
|---|---|
| **The Rule** | Before writing a file path into any document, script, or config — verify the path actually exists on disk. |
| **Why It Exists** | Disaster 15: Provenance files referenced `Enterprise_OS/ai_threads/Historic` but actual location was `Enterprise_OS/Core_Engine/ai_threads/epoch/historic`. All links broken. |
| **How to Check** | When the LLM writes paths in output files, spot-check 2-3 of them: "Does the path [X] actually exist?" |
| **When It's Broken** | Find all incorrect paths. Update them to the actual, verified paths. Test that the corrected paths resolve. |

## Rule 17B: Extraction Outputs Always Go to Both Locations

| | |
|---|---|
| **The Rule** | Every extraction produces two copies: one alongside the source file, one in the central store (`04_KNOWLEDGE_LIBRARY/EXTRACTIONS/`). Never skip either copy. |
| **Why It Exists** | Alongside copies let you browse extractions in context. Central copies let you search across everything. Without both, you lose one dimension of findability. |
| **How to Check** | After an extraction, verify: (1) `.extract_*.json` exists next to the source file, (2) the file appears in `EXTRACTIONS/by_mode/`, (3) `EXTRACTION_INDEX.json` has a new entry. |
| **When It's Broken** | Re-run the extraction. If only one copy exists, manually copy it to the missing location. |

---

# PART 6: ERROR HANDLING RULES

## Rule 21: Validate Every API Response

| | |
|---|---|
| **The Rule** | Every API call must have its response validated. If the response is malformed, empty, or contains errors — stop and report. Don't continue as if it succeeded. |
| **Why It Exists** | Disaster 7: A JSON parse error on Cluster 1 (96 threads) was silently ignored. 52% of threads got no theme assignment. Discovered much later. |
| **How to Check** | During API batch operations, ask for a running count: "How many successful responses? How many errors? Show me any errors." |
| **When It's Broken** | Stop the batch. Identify which items failed. Reprocess only the failed items. Validate the reprocessed results before continuing. |

## Rule 22: Fail Loudly on Errors

| | |
|---|---|
| **The Rule** | If something goes wrong, stop and say so. Don't swallow errors. Don't say "let me try again" without explaining what went wrong. |
| **Why It Exists** | Multiple disasters involved silent failures that weren't caught until much later. |
| **How to Check** | If the LLM suddenly goes quiet during a batch operation, or says "continuing..." without mentioning results — ask: "Did that last operation succeed? Show me the output." |
| **When It's Broken** | Demand the error details. Assess impact. Decide whether to continue or revert. |

---

# PART 7: THE TASK RISK LEVELS

Every task type has an assigned risk level:

| Risk | Task Types | What It Means |
|------|-----------|---------------|
| **None** | READ, ANALYSE, PLAN, TEST, SEARCH | Safe. No approval needed. |
| **Low** | LOG, COMMIT | Creates new files but doesn't change existing ones. |
| **Medium** | WRITE, EDIT, ROUTE, INGEST, CONVERT, INDEX, BUILD, PUSH, TROUBLESHOOT | Changes or creates files. Follow naming/routing rules. |
| **HIGH** | DELETE, MOVE, RENAME | **Must get explicit human approval before executing.** |

### The HIGH Risk Protocol

When the LLM wants to DELETE, MOVE, or RENAME:

1. It must list every file affected, with full paths
2. It must state what will happen to each file (deleted, moved to [X], renamed to [Y])
3. **You say "Yes, approved" or "No, don't do that"**
4. Only after explicit approval does it proceed

If it does any of these without asking — that's a rule violation. Stop immediately and assess damage.

---

# PART 8: QUICK ENFORCEMENT REFERENCE

## Copy-Paste for Session Start

Give this to any LLM at the start of a session:

```
RULES FOR THIS SESSION:
1. NEVER delete files — archive to 90_ARCHIVE/ instead
2. NEVER move or rename files without my explicit approval
3. NEVER overwrite existing files — use _v2 or timestamp suffix
4. NEVER put outputs in root folders — use designated subfolders
5. NEVER edit 00_CANON/ files without my explicit approval
6. NEVER invent pillar or folder names — use only the canonical 23
7. NEVER truncate content silently — process the full file
8. Count before and after every batch operation
9. Checkpoint after every single item in batch processing
10. If unsure where content goes, put it in UNROUTED
11. Log every routing decision
12. Fail loudly on errors — don't swallow them

If you want to delete, move, or rename anything — ASK FIRST with the full file list.
```

## How to Verify Rule Compliance After a Session

```bash
# Check for deleted files:
git diff --name-status HEAD

# Check for changes to canon files:
git diff HEAD -- "*/00_CANON/*"

# Check for stray files in root:
ls C:/Users/under/Downloads/ENTERPRISE_OS_V7/

# Check for temp files:
# Search for: ~$*, *.tmp, *.bak

# Check session log exists:
ls 02_COMMAND_DECK/ACTIVE_SESSIONS/
```

---

*This document is part of the Owner's Manual suite. See also: OWNERS_MANUAL.md, SYSTEM_CAPABILITIES.md, MAINTENANCE_DRILLS.md, PROMPT_LIBRARY.md*
