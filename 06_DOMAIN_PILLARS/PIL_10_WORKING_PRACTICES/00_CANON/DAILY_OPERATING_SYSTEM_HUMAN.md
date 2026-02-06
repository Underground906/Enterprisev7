# ENTERPRISE_OS V7 — DAILY OPERATING SYSTEM

**Location:** PIL_10_WORKING_PRACTICES/00_CANON/
**Version:** 1.0
**Purpose:** How to run the system every day

---

## PART 1: HUMAN GUIDE

### The 3 Rituals

Your entire system runs on three rituals:

1. **Morning Start** (10 min)
2. **Work Blocks** (90-120 min each)
3. **End of Day** (10 min)

That's it. Do these consistently and the system works.

---

### RITUAL 1: MORNING START

**Time:** First 10 minutes of work day
**Location:** 01_NAVIGATION_CENTRE/

#### Steps:

1. **Open STATE_SNAPSHOT**
   ```
   01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/[today].md
   ```
   - If doesn't exist, create from yesterday's
   - Read: What's the #1 priority?

2. **Check ACTIVE_GOALS**
   ```
   01_NAVIGATION_CENTRE/ACTIVE_GOALS/
   ```
   - Which goal does today serve?
   - Any blockers to clear?

3. **Create SESSION_LOG**
   ```
   02_COMMAND_DECK/ACTIVE_SESSIONS/[YYYY-MM]/[today]_session_01.md
   ```
   - Log: Start time, goal, intent

4. **Load Context**
   - Open relevant PIL_XX/00_CANON/DOCS.md
   - Open relevant PRJ_XX/ if building

5. **Begin Work**

---

### RITUAL 2: WORK BLOCKS

**Time:** 90-120 minutes focused
**Location:** Wherever the work lives

#### The Milestone Anchor Loop:

Every work block follows this:

```
1. INVENTORY (5 min)
   What do I have? What do I need?

2. EXTRACT (30-45 min)
   Do the actual work

3. SYNTHESIZE (20-30 min)
   Turn work into usable output

4. DERIVE (15-20 min)
   What does this mean? What's next?

5. FILE (10 min)
   Put outputs in correct locations

6. LOG (5 min)
   Update session log
```

#### Rules:

- Maximum 3 work blocks per day
- 15-30 min break between blocks
- One primary deliverable per block
- End each block with "next step" noted

---

### RITUAL 3: END OF DAY

**Time:** Last 10 minutes of work day
**Location:** 01_NAVIGATION_CENTRE/

#### Steps:

1. **Complete SESSION_LOG**
   - End time
   - Work completed (bullets)
   - Outputs created (with paths)
   - Decisions made
   - Next session: first action

2. **File Any Loose Outputs**
   - Nothing stays in Downloads
   - Everything to correct PIL_XX or PRJ_XX

3. **Update STATE_SNAPSHOT**
   ```
   01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/[today].md
   ```
   - Progress made
   - Blockers encountered
   - Tomorrow's #1 priority

4. **Clear Workspace**
   - Close tabs
   - Save drafts
   - Note anything in UNROUTED

---

### WEEKLY: TRIAGE & ROUTE

**Time:** 30-60 minutes, once per week
**Purpose:** Clear the backlog

1. Process `04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/`
2. Route threads to correct PIL_XX/01_threads/
3. Route artifacts to correct PIL_XX/02_artifacts/
4. Archive completed work to 90_ARCHIVE folders
5. Update MASTER_CANON_REGISTRY if new docs created

---

### WHERE THINGS GO

| What You Create | Where It Goes |
|-----------------|---------------|
| Strategy/framework docs | PIL_XX/00_CANON/ |
| Thread transcripts | PIL_XX/01_threads/ |
| Generated artifacts | PIL_XX/02_artifacts/ |
| Active code/builds | 07_BUILD_FACTORY/PRJ_XX/ |
| Session logs | 02_COMMAND_DECK/ACTIVE_SESSIONS/ |
| State/goals | 01_NAVIGATION_CENTRE/ |
| Templates | 05_TEMPLATE_HUB/ |
| Unknown/mixed | 04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/ |

---

### PROJECT WORK FLOW

When building any platform:

```
1. GOAL lives in → 01_NAVIGATION_CENTRE/ACTIVE_GOALS/GOAL_XX/
2. DOMAIN expertise lives in → 06_DOMAIN_PILLARS/PIL_XX/00_CANON/
3. BUILD execution lives in → 07_BUILD_FACTORY/PRJ_XX/
4. SESSION tracking lives in → 02_COMMAND_DECK/
```

Example for Property Connect London:

```
Goal: 01_NAVIGATION_CENTRE/ACTIVE_GOALS/GOAL_Property_Connect_London/
Property knowledge: PIL_19_PROPERTY/00_CANON/DOCS.md
Copy frameworks: PIL_03_COPY/00_CANON/DOCS.md
UI components: PIL_07_UI_LIBRARY/00_CANON/DOCS.md
Build work: 07_BUILD_FACTORY/PRJ_Property_Connect_London/
Sessions: 02_COMMAND_DECK/ACTIVE_SESSIONS/2026-02/
```

---

### ANTI-PATTERNS (Don't Do These)

- ❌ Starting work without checking STATE_SNAPSHOT
- ❌ Working without a session log open
- ❌ Leaving outputs unfiled at end of day
- ❌ More than 3 work blocks without breaks
- ❌ Vague session notes ("did stuff")
- ❌ Letting UNROUTED pile up for weeks
- ❌ Working in Downloads instead of the system

---

### THE COMPOUND EFFECT

Every day you run this system:
- Pillar DOCS get richer
- Project folders fill with assets
- State history shows progress
- Patterns become visible
- Context gets easier to load

**The system gets smarter because you used it.**

---

## PART 2: QUICK REFERENCE CARD

```
┌─────────────────────────────────────────────────────────────┐
│  MORNING (10 min)                                           │
│  1. STATE_SNAPSHOT → What's priority?                       │
│  2. ACTIVE_GOALS → Which goal today?                        │
│  3. SESSION_LOG → Create, log start                         │
│  4. LOAD CONTEXT → Open DOCS.md                             │
├─────────────────────────────────────────────────────────────┤
│  WORK BLOCK (90-120 min)                                    │
│  Inventory → Extract → Synthesize → Derive → File → Log    │
│  Max 3 blocks/day. Breaks between. One deliverable each.   │
├─────────────────────────────────────────────────────────────┤
│  END OF DAY (10 min)                                        │
│  1. Complete SESSION_LOG                                    │
│  2. File all outputs                                        │
│  3. Update STATE_SNAPSHOT                                   │
│  4. Note tomorrow's first action                            │
├─────────────────────────────────────────────────────────────┤
│  WEEKLY                                                     │
│  Triage UNROUTED → Route to pillars → Archive completed    │
└─────────────────────────────────────────────────────────────┘
```

---

**END OF HUMAN GUIDE**
