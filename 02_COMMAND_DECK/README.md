# 02_COMMAND_DECK — README

**Purpose:** Run your day. Log sessions. Track tasks. Never lose work in progress.

---

## THE MILESTONE ANCHOR LOOP

Every work session follows this pattern:

```
┌─────────────────────────────────────────────────────────────┐
│  MILESTONE ANCHOR LOOP (90-120 minutes)                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. INVENTORY (5 min)                                       │
│     What do I have? What's the context?                     │
│                        ↓                                    │
│  2. EXTRACT (30-45 min)                                     │
│     Pull value from source material                         │
│                        ↓                                    │
│  3. SYNTHESIZE (20-30 min)                                  │
│     Combine, structure, make coherent                       │
│                        ↓                                    │
│  4. DERIVE (15-20 min)                                      │
│     Create outputs: docs, decisions, actions                │
│                        ↓                                    │
│  5. FILE (10 min)                                           │
│     Route outputs to correct locations                      │
│                        ↓                                    │
│  6. LOG (5 min)                                             │
│     Update session log, flag next step                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## FOLDER STRUCTURE

```
02_COMMAND_DECK/
├── ACTIVE_SESSIONS/
│   └── 2026-02/
│       ├── 2026-02-04_session_01.md
│       ├── 2026-02-04_session_02.md
│       └── 2026-02-05_session_01.md
│
├── TASK_QUEUE/
│   ├── URGENT.md              ← Must do today
│   ├── THIS_WEEK.md           ← Must do this week
│   └── BACKLOG.md             ← Everything else
│
├── AGENT_WORKSPACE/           ← If using AI agents
│   ├── Research_Agent/
│   ├── Copy_Agent/
│   └── Code_Agent/
│
└── 90_ARCHIVE/
    └── 2026-01/               ← Past months
```

---

## SESSION LOG TEMPLATE

Create for each work session:

```markdown
# SESSION LOG — YYYY-MM-DD #[N]

**Start:** HH:MM
**End:** HH:MM
**Duration:** X hrs

## Activation Context
- **Goal:** [Which goal from NAVIGATION]
- **Phase:** [Planning / Research / Building / etc.]
- **Intent:** [What I'm trying to accomplish]

## Work Done
1. [Task completed]
2. [Task completed]
3. [Task completed]

## Outputs Created
- [ ] [Filename] → [Destination]
- [ ] [Filename] → [Destination]

## Decisions Made
- [Decision and rationale]

## Blockers Hit
- [None / Description]

## Next Session
- **Priority:** [What to do next]
- **Context needed:** [What to load]

## Notes
[Anything else]
```

---

## DAILY RHYTHM

### Morning Start (15 min)

```
1. Open NAVIGATION/STATE_SNAPSHOT → What's the priority?
2. Create session log → 02_COMMAND_DECK/ACTIVE_SESSIONS/
3. Set activation context → What am I doing?
4. Check TASK_QUEUE/URGENT.md → Anything critical?
5. Begin first Milestone Anchor Loop
```

### Work Blocks (90-120 min each)

```
1. Run Milestone Anchor Loop
2. Take 15-30 min break
3. Repeat (max 2-3 blocks per day)
```

### End of Day (15 min)

```
1. Complete session log
2. File any loose outputs
3. Update NAVIGATION/STATE_SNAPSHOT
4. Add tasks to TASK_QUEUE
5. Flag tomorrow's first action
```

---

## TASK QUEUE TEMPLATES

### URGENT.md
```markdown
# URGENT — Must Do Today

**Updated:** YYYY-MM-DD

## Tasks
- [ ] [Task] — [Context/Notes]
- [ ] [Task] — [Context/Notes]

## Deadline Items
- [ ] [Task] — Due: [Date]
```

### THIS_WEEK.md
```markdown
# THIS WEEK — Must Complete

**Week of:** YYYY-MM-DD

## Monday
- [ ] 

## Tuesday
- [ ] 

## Wednesday
- [ ] 

## Thursday
- [ ] 

## Friday
- [ ] 

## Flexible
- [ ] 
```

---

## TWO-HOUR WORK BLOCK RULES

For sustainable, high-quality work:

```
RULE 1: Maximum 3 decisions per block
        (More = decision fatigue)

RULE 2: One visible win per block
        (Something you can point to)

RULE 3: End with next step written down
        (Never stop in the middle)

RULE 4: 15-30 min break between blocks
        (Recovery is productive)

RULE 5: Maximum 3 blocks per day
        (6 hours focused > 12 hours scattered)
```

---

## FILE-AS-YOU-GO PROTOCOL

Don't wait until end of day to file:

```
DURING SESSION:
- Create output → Immediately decide destination
- Save to destination (or PROCESSING if unsure)
- Note in session log

END OF SESSION:
- Quick scan: anything unfiled?
- Move from PROCESSING → final location
- Update session log with all destinations
```

---

## MODEL SELECTION (If Using Multiple AIs)

| Task Type | Best Model |
|-----------|------------|
| Strategic thinking, synthesis | Claude Opus |
| Code, technical implementation | Claude Sonnet / Cursor |
| Quick questions, iterations | ChatGPT / Claude |
| Long documents, analysis | Claude with large context |
| Visual design feedback | Gemini / Claude |

---

## SESSION RECOVERY

If you get interrupted mid-session:

```
1. Quick note: "Stopped at: [point]"
2. Save any open files
3. Later: Open session log
4. Read "Next Session" from previous log
5. Resume where you left off
```

---

## INTEGRATION

| Connects To | How |
|-------------|-----|
| 01_NAVIGATION | Goals drive sessions |
| 04_KNOWLEDGE_LIBRARY | Outputs route there |
| 06_DOMAIN_PILLARS | Domain work lives there |
| 03_CORE_ENGINE | Scripts support sessions |

---

## ANTI-PATTERNS TO AVOID

```
❌ Starting without knowing today's goal
❌ Working without a session log
❌ Keeping 10+ browser tabs open
❌ Not filing outputs immediately
❌ Working more than 3 hours without break
❌ Ending without noting next step
❌ Having 20+ items on "urgent" list
```

---

*Command Deck is not about perfect productivity. It's about knowing what you did, what you decided, and what's next.*
