# 01_NAVIGATION_CENTRE — README

> **What this does:** Tracks where you're going, what matters NOW, and your current state.

---

## FOLDER STRUCTURE

```
01_NAVIGATION_CENTRE/
├── ACTIVE_GOALS/          ← Your live goals (max 3-5)
│   └── GOAL_[Name]/       ← Each goal gets a folder
├── GOAL_INTAKE/           ← New ideas dumped here
├── STATE_SNAPSHOTS/       ← Daily "where am I" snapshots
└── 90_ARCHIVE/            ← Completed/abandoned goals
```

---

## DAILY USE (5-10 min total)

### Morning (5 min)
1. Create `STATE_SNAPSHOTS/YYYY-MM-DD.md`
2. Answer: What's my #1 priority today?
3. Check: Anything blocked?

### End of Day (5 min)
1. Update STATE_SNAPSHOT with progress
2. Flag tomorrow's first action
3. Log any decisions made

---

## STATE_SNAPSHOT TEMPLATE

Create daily in `STATE_SNAPSHOTS/`:

```markdown
# STATE — 2026-02-04

## Today's #1 Priority
[One sentence]

## Active Goals
1. **[Goal]** — [5-word status]
2. **[Goal]** — [5-word status]

## Blocked
[None / What's stuck]

## Decisions Needed
[None / What needs deciding]

## Tomorrow
[First action]
```

---

## GOAL FOLDER TEMPLATE

When you create a new goal in `ACTIVE_GOALS/`:

```markdown
# GOAL: [Name]

**Created:** YYYY-MM-DD
**Target:** [What done looks like]
**Deadline:** [When / None]

## Why This Matters
[1-2 sentences]

## Current Status
- Phase: [Planning / Building / Testing / Live]
- Progress: [X%]
- Next action: [...]

## Key Decisions
- [Date]: [Decision]

## Learning
- [What I've discovered]
```

---

## RULES

1. **Max 3-5 active goals** — More = chaos
2. **One #1 priority per day** — No ties
3. **Update STATE daily** — Prevents drift
4. **Archive, don't delete** — Completed goals → 90_ARCHIVE

---

## INTEGRATION

- Goals drive → **02_COMMAND_DECK** sessions
- Learning feeds → **04_KNOWLEDGE_LIBRARY**
- Outputs go to → **06_DOMAIN_PILLARS** or **07_BUILD_FACTORY**

---

*Navigation isn't about planning everything. It's about knowing what matters NOW.*
