# Enterprise OS V7 — Working Practices PRD

**Version:** 1.0
**Date:** 2026-02-17
**Owner:** John
**Purpose:** How to work WITHIN Enterprise OS — daily habits, workflows, discipline, session management, ADHD-friendly protocols
**Status:** DEFINITIVE — the operational manual for using the system
**Source:** PIL_10_WORKING_PRACTICES canon docs, Notebook summaries, session transcripts
**Companion:** PRD_COMPLETE_BUILD_SPEC.md (the platform itself), PIL_10 canon (raw frameworks)

---

## 1. WHY THIS DOCUMENT EXISTS

Enterprise OS is an incredibly powerful system. It is also incredibly easy to misuse.

**The problem:** John (and eventually users) can spend 20 hours in an unstructured session, generate 200K tokens of context, create dozens of scattered files, and end the day with more chaos than they started with. The system grows in complexity without growing in value. Knowledge evaporates in chat histories. Files pile up in wrong locations. Context is lost between sessions. The anxiety spiral begins.

**The solution:** A set of non-negotiable rituals and guardrails that make the system work FOR you, not against you. This PRD codifies the exact protocols for productive work within Enterprise OS.

**Key insight from John:**
> "I woke up this morning and realized the 10 months of graft I put into creating my 8 component system and a real time, updating, hardcoded enforced rules system was a mirage. Each day we work and you create new folders and docs on the file and they are not put in database, the system is not updated... that's untenable."

The system must enforce its own discipline. These practices are the bridge until the platform automates them.

---

## 2. THE THREE RITUALS

Everything in Enterprise OS revolves around three non-negotiable rituals. Skip any one and the system degrades.

### RITUAL 1: Morning Start (10 minutes)

**When:** First thing after waking up, before checking email or social media.

**Steps:**

| Step | Duration | Action | Why |
|---|---|---|---|
| 1. Body First | 15 min | Exercise (walk, stretch, gym) | Physical state drives mental state. Non-negotiable. |
| 2. State Check | 5 min | Read today's State Snapshot (NAV_G) or yesterday's session log | Context before action. Never start cold. |
| 3. Priorities | 3 min | Read Morning Brief (NAV_C) — yesterday's wins, today's top 3 | Focus before chaos. The system tells you what matters. |
| 4. Declare Intent | 2 min | Start Session (CMD_A) with one-line intent | Commitment before work. "I will accomplish X in this block." |

**Anti-patterns:**
- Opening 20 browser tabs before declaring intent
- Checking Slack/email before Morning Start
- Starting work without reading yesterday's session log
- Skipping exercise ("I'll do it later" = never)

**The rule:** If you haven't done the Morning Start, you haven't started work. Everything before this is just anxiety-driven tab-opening.

---

### RITUAL 2: Work Blocks (90-120 minutes each, max 3 per day)

**The Milestone Anchor Loop:**

```
INVENTORY (10-15 min)
    → List what exists, identify gaps, check manifest
EXTRACT (20-30 min)
    → Do the actual work, capture decisions with evidence
SYNTHESIZE (20-30 min)
    → Create/update anchor documents, connect to existing knowledge
DERIVE (15-20 min)
    → Spawn SOPs, templates, scripts, components from synthesis
FILE (10-15 min)
    → Route outputs to correct locations (PARA), update indices
LOG (5 min)
    → Update DECISIONS.md, set ONE tiny next step for next block
```

**Block rules:**

| Rule | Detail |
|---|---|
| **Max 3 decisions per block** | Decision fatigue is real. If you've made 3 significant decisions, stop the block. |
| **One project per block** | Context-switching kills depth. One intent, one block. |
| **Visible win required** | Every block must produce at least one tangible output. If it didn't, something went wrong. |
| **One tiny next step** | Before closing the block, write the exact first action for the next block. Not "continue working on X" — the specific next step. |
| **Read last session log first** | 5 minutes of context loading prevents 60 minutes of repeated work. |
| **Timer-based, not feeling-based** | Set 90-120 min timer. When it rings, you're done. Don't "just finish one more thing." |
| **4-5 blocks per day** | A full working day = 4-5 blocks of 90-120 min with breaks between. This is 6-10 hours of deep work. |
| **Commit at every block end** | Save BOTH a verbatim transcript AND a token-efficient summary. Builds the habit. Preserves everything. |
| **15-30 min recovery between blocks** | Walk, eat, stretch. Not "check Slack." Physical recovery. |

**ADHD-specific adaptations:**

| Challenge | Solution |
|---|---|
| Can't start | The "one tiny next step" from last block IS the start. Open that file. Do that one thing. Momentum follows. |
| Hyperfocused for 6 hours | Timer is non-negotiable. Set phone alarm. When it rings, LOG and STOP. |
| Context-switching urge | Write the distracting idea in a scratch file (0_INBOX). It's captured. Return to current block. |
| Overwhelmed by scope | The block is 90 minutes. Not the whole project. Just this block. What's the visible win? |
| Decision paralysis | Max 3 decisions. If you're stuck on decision #1, timebox it to 15 min → default option wins. |
| "I should reorganise the system" | NO. That's anxiety disguised as productivity. Only reorganise if it's in the block's declared intent. |

---

### RITUAL 3: End of Day (15 minutes)

**Steps:**

| Step | Duration | Action |
|---|---|---|
| 1. Complete Session Log | 5 min | End the active session (CMD_A). Let AI auto-synthesize. Review the summary. |
| 2. File Outputs | 5 min | Route any unrouted items from today. Nothing left in 0_INBOX older than today. |
| 3. Update State | 3 min | State snapshot gets updated. Note what changed today. |
| 4. Tomorrow's First Action | 2 min | Write the exact first action for tomorrow. Not a to-do list — THE first action. |

**The rule:** If you skip End of Day, you WILL lose context. Tomorrow becomes a 30-minute context-recovery session instead of a 2-minute intent declaration.

---

## 3. WEEKLY RHYTHM

### Sunday Review (30-60 minutes)

| Step | Action |
|---|---|
| 1. Triage Inbox | Process anything in 0_INBOX. Route to correct pillar/project or archive. |
| 2. Review Work Blocks | How many blocks this week? How many produced visible wins? Identify patterns. |
| 3. Goal Health Check | Open NAV_D. Any goals in red? Any milestones past due? |
| 4. Plan Next Week | 3 priorities for the week. Map them to specific work blocks (Mon-Fri). |
| 5. System Health | Any pillar stale? Any routing errors? Any unrouted pile-up? |

### Monthly Review (2 hours)

| Step | Action |
|---|---|
| 1. Goal Cascade | Are individual tasks still serving 90-day goals? Kill zombie tasks. |
| 2. PARA Maintenance | Completed projects → 4_ARCHIVES. Promote resources that became areas. |
| 3. Anti-Pattern Audit | Review Build Story (BLD_E) entries. Any recurring anti-patterns? |
| 4. System Evolution | Are the working practices themselves working? What needs adjusting? |

---

## 4. SESSION MANAGEMENT

### Session Types

| Type | Duration | Intent Pattern | Example |
|---|---|---|---|
| **Build Block** | 90-120 min | "Build [specific thing]" | "Build the Goal Intake Wizard screen" |
| **Research Block** | 60-90 min | "Research [topic] for [purpose]" | "Research Anima conversion workflow for component library" |
| **Extract Block** | 60-90 min | "Extract and route [content] to [pillar]" | "Extract key decisions from yesterday's session into PIL_14" |
| **Planning Block** | 45-60 min | "Plan [deliverable]" | "Plan Sprint 2 deliverables for Enterprise OS" |
| **Triage Block** | 30-45 min | "Triage [inbox/backlog]" | "Triage unrouted items from this week" |
| **Review Block** | 30-45 min | "Review [items] for promotion" | "Review staging items in PIL_03 for canonical promotion" |

### Session Start Protocol

1. Declare intent (one sentence)
2. Link to goal (which strategic goal does this serve?)
3. Select agent role (what expertise is needed?)
4. Load context (last session log + relevant pillar canon)
5. Begin work

### Session End Protocol (EVERY block, no exceptions)

1. Save **verbatim transcript** → `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/YYYY-MM-DD_session_NN_full.md`
2. Save **token-efficient summary** → `02_COMMAND_DECK/ACTIVE_SESSIONS/YYYY-MM/YYYY-MM-DD_session_NN.md`
3. Route all outputs to correct locations
4. Note ONE tiny next step
5. Close the session

Both saves happen EVERY block. The verbatim preserves everything. The summary restores context fast next session.

### Context Management (Token Budgeting)

**The problem:** Enterprise OS sessions can consume 200K+ tokens loading context. This is wasteful and expensive.

**The solution:**

| Layer | What to Load | Token Budget |
|---|---|---|
| **Always** | CLAUDE.md + MEMORY.md + current session intent | ~5K tokens |
| **Per-session** | Relevant PRD + pillar canon doc + last session log | ~10-20K tokens |
| **On-demand** | Specific files referenced during work | Variable |
| **Never load** | Full session transcripts, full file indices, entire pillar contents | — |

**Rule:** If loading context takes more than 2 minutes, you're loading too much. The system should tell you what's relevant, not dump everything.

**Future solution (in-app):** Enterprise OS will manage context automatically — the Semantic Search (LIB_D) retrieves only what's needed per query. No more manual context loading.

---

## 5. FILE ROUTING IN ENTERPRISE OS

Enterprise OS V7 uses its own 8-component structure for routing, NOT PARA. The canonical folder structure IS the routing system:

| Component | Location | What Goes Here |
|---|---|---|
| **System Root** | `00_SYSTEM_ROOT/` | Governance, naming rules, master context |
| **Navigation** | `01_NAVIGATION_CENTRE/` | Goals, state snapshots, priorities |
| **Command Deck** | `02_COMMAND_DECK/` | Session logs, active sessions, agent workspaces |
| **Core Engine** | `03_CORE_ENGINE/` | Scripts, indices, routing rules, schemas |
| **Knowledge Library** | `04_KNOWLEDGE_LIBRARY/` | Ongoing intake, extraction pipeline, session archives |
| **Template Hub** | `05_TEMPLATE_HUB/` | Reusable templates for agents, docs, prompts, SOPs |
| **Domain Pillars** | `06_DOMAIN_PILLARS/PIL_*/` | 23 specialist knowledge domains |
| **Build Factory** | `07_BUILD_FACTORY/PRJ_*/` | Active platform builds |
| **Operations** | `08_OPERATIONS/` | Post-launch: marketing, metrics, legal, financial |

Content is routed by the Core Engine's semantic + keyword routing. If you don't know where something goes, put it in `04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/` — never in a root folder.

---

## 6. S>C>E GOVERNANCE IN DAILY PRACTICE

Every piece of content flows through three states:

### Staging (🟡 Yellow) — "Work in progress"
- AI-generated drafts
- Session notes
- Raw extractions
- Unreviewed outputs

**Daily practice:** Everything you create during a work block starts in Staging. This is fine. This is normal.

### Canonical (🟢 Green) — "Source of truth"
- Human-reviewed and approved
- AI agents read ONLY from Canonical
- The foundation of institutional memory

**Daily practice:** During End of Day or weekly review, promote your best Staging items to Canonical. This is the quality gate.

### Execution (🔵 Blue) — "Generated from Canonical"
- AI agents produce Execution outputs from Canonical inputs
- Templates, generated docs, automated outputs

**Daily practice:** You rarely create Execution items directly. The system generates them from Canonical.

**The rule:** If you skip promotion, Canonical gets stale. If Canonical gets stale, AI agents use outdated information. If AI uses outdated information, everything downstream is wrong.

**Weekly goal:** Promote at least 3-5 items from Staging to Canonical.

---

## 7. AGENT HANDOFF PROTOCOLS

When using AI agents (in Claude Code sessions or the in-app Agent OS):

### The Micro-Step Rule

| Principle | Detail |
|---|---|
| **One step at a time** | Never ask the agent to "do the whole thing." Break into steps. Verify each step. |
| **Confidence threshold** | Require 0.90+ confidence on any classification or routing decision. Below that, escalate to human. |
| **Dry-run first** | For any destructive or irreversible action, ask for a dry-run/preview before executing. |
| **Count before and after** | Any batch operation: count files/items before, execute, count after. Discrepancy = stop immediately. |
| **Checkpoint after every item** | Long-running processes save progress after EVERY item, not every batch. If it crashes, restart from last checkpoint. |

### What Agents Should NOT Do

| Forbidden Action | Why |
|---|---|
| Delete files without explicit approval | [DISASTER 1, 3] Files have been permanently lost |
| Move files without explicit approval | [DISASTER 1, 10] Provenance broken, structure destroyed |
| Rename files without explicit approval | [DISASTER 6] Downstream references break |
| "Clean up" or "reorganise" | [DISASTER 10] Assumes it knows better than existing structure |
| Truncate content | [DISASTER 8] Important content at end of files gets lost |
| Continue after error | [DISASTER 7, 11] Silent failures compound into data loss |
| Create files in root folders | [DISASTER 4, 9] Outputs scattered, structure violated |
| Invent taxonomy names | [DISASTER 5] Use only canonical pillar names |

### What Agents SHOULD Do

| Required Action | Detail |
|---|---|
| Read before modifying | Never edit a file you haven't read first |
| Backup before overwrite | `filename_BACKUP_YYYYMMDD.ext` |
| Validate outputs | Count, verify, diff against expectations |
| Log every decision | Agent decisions logged to session events |
| Ask when uncertain | If confidence < 0.90, ask the human |

---

## 8. KNOWLEDGE EXTRACTION WORKFLOW (EKX-1)

The EKX-1 methodology is the 20-section extraction schema applied to all raw content:

### When To Extract

| Content Type | When to Run EKX-1 |
|---|---|
| AI chat transcript (ChatGPT, Claude) | Always — this is where most value hides |
| Session transcript | Always — the session log IS the raw material |
| Meeting notes | Always |
| Book/article/video notes | Always |
| Code changes | Only if architectural decisions were made |
| Casual notes | Skip — promote to proper format first |

### The 29 Artifact Types

When extracting, look for these specific types:

1. **Frameworks** — Named systems, methodologies, models
2. **SOPs** — Step-by-step procedures
3. **Decision Logs** — What was decided and why
4. **Code Snippets** — Reusable code patterns
5. **UI Specs** — Interface descriptions, layouts
6. **Database Schemas** — Table definitions, relationships
7. **Market Intel** — Competitor info, market data
8. **Hooks & Messaging** — Compelling phrases, positioning
9. **Unique Mechanisms** — Named proprietary approaches
10. **Process Maps** — Workflow visualisations
11. **Role Definitions** — Job specs, responsibilities
12. **Brand Rules** — Voice, tone, visual guidelines
13. **Copy Formulas** — Reusable copy patterns
14. **Content Strategies** — Editorial plans, topics
15. **Keyword Sets** — SEO/discovery terms
16. **Templates** — Reusable document structures
17. **Architecture Specs** — System design documents
18. **API Definitions** — Endpoint specs, integrations
19. **Test Plans** — QA procedures
20. **Deployment Configs** — Infrastructure setup
21. **Financial Models** — Revenue, cost projections
22. **Legal Docs** — Terms, policies
23. **Training Materials** — Onboarding, education
24. **Performance Metrics** — KPIs, measurement plans
25. **Risk Assessments** — Identified risks, mitigations
26. **Competitor Analysis** — Feature comparisons
27. **User Stories** — Feature requirements from user perspective
28. **Design Tokens** — Colour, typography, spacing values
29. **Prompt Patterns** — Reusable AI prompt structures

### Three-Lane Ingestion

| Lane | Content Type | Process |
|---|---|---|
| **Lane A: Historical Backlog** | Old threads, archived docs, legacy content | Stage → Pair filenames → Convert to text → Extract → Route |
| **Lane B: Fresh Work** | Today's session outputs, new files | Real-time staging → Mini-manifest → Hot-path routing |
| **Lane C: External Media** | Books, YouTube, PDFs, web content | Medium-specific checklists → Convert → Extract → Route |

---

## 9. THE COMPOUND EFFECT

Why these practices matter over time:

### Week 1
- Uncomfortable. Rituals feel forced.
- Session logs are sparse.
- Routing feels like overhead.

### Month 1
- Morning Brief starts being useful (enough data to synthesise).
- Session logs become your second brain.
- Routing means you can find things.

### Month 3
- State Snapshots accurately reflect reality.
- Goal Health Dashboard shows real trends.
- The system is managing YOU, not the other way around.

### Month 6
- Institutional memory is searchable.
- New projects pull from existing knowledge in minutes.
- AI agents give relevant, accurate answers from Canonical.

### Year 1
- Complete organisation knowledge base.
- Any question answered in seconds.
- New team members productive on Day 1.
- The system is worth more than any single person.

---

## 10. ANTI-PATTERNS & RECOVERY

### The 10 Anti-Patterns

| # | Anti-Pattern | Symptom | Recovery |
|---|---|---|---|
| 1 | **20-hour unstructured session** | Anxiety spiral, massive token costs, scattered outputs | STOP. Log what you did. End session. Tomorrow start with Morning Start ritual. |
| 2 | **Endless reorganisation** | Moving files instead of creating value | Only reorganise if it's the declared intent of a work block. Otherwise: stop. |
| 3 | **Not logging** | "I'll remember" (you won't) | Complete the session. If you didn't log, spend 10 min now reconstructing what happened. |
| 4 | **Skipping exercise** | Low energy, poor decisions, anxiety | Tomorrow: body first. Before screen. Non-negotiable. |
| 5 | **Decision fatigue** | Making the same decision 5 different ways | Max 3 decisions per block. Timebox to 15 min. Default option wins if time expires. |
| 6 | **Context loss between sessions** | "What was I doing?" for 30 minutes | Read last session log. If there isn't one, that's the anti-pattern (see #3). |
| 7 | **Building instead of routing** | Creating new docs instead of filing existing ones | Weekly triage: process the inbox BEFORE creating new content. |
| 8 | **AI reconstruction instead of conversion** | Getting AI to "approximate" instead of using proper tools | Use the right tool (Anima for Figma, API for data). AI reconstruction is lossy. |
| 9 | **Loading full context every session** | 200K tokens to "restore context" | Load only: MEMORY.md + last session + relevant PRD. The system should serve context, not dump it. |
| 10 | **Perfectionism before shipping** | Endlessly refining instead of promoting | "Good enough for Canonical" is the standard. Perfect is the enemy of shipped. |

---

## 11. MINIMUM VIABLE DAY

When everything is going wrong — anxiety, fatigue, ADHD chaos — this is the minimum:

| Time | Duration | Action |
|---|---|---|
| Morning | 15 min | Body: walk around the block |
| Morning | 5 min | Read: Morning Brief or yesterday's session log |
| Anytime | 90 min | ONE work block with declared intent |
| Block end | 5 min | Log: complete the session, file outputs |
| Evening | 5 min | Tomorrow: write the exact first action |
| **TOTAL** | **2h 0min** | One block, one win, one next step |

That's the minimum. Most days should be 4-5 blocks (6-10 hours deep work). But even on the worst days, one block still compounds.

---

## 12. PLATFORM ENFORCEMENT (FUTURE)

When Enterprise OS is fully built, the platform will enforce these practices automatically:

| Practice | Manual (Now) | Automated (Future) |
|---|---|---|
| Morning Brief | Read the file | Generated and delivered at 6 AM |
| Session start | Create file, write intent | Modal wizard in CMD_A |
| Session timer | Phone alarm | Built-in timer with warnings |
| Session end | Write summary manually | AI auto-synthesis with one-click approve |
| Output routing | Move files manually | Auto-routing with AI classification |
| State snapshot | Manual update | Auto-generated daily from system activity |
| Goal health | Manual score update | Auto-calculated from task velocity and session activity |
| Context loading | Read files manually | Semantic search loads only relevant context |
| Decision logging | Manual entry | Auto-captured from session events |
| Weekly triage | Manual inbox processing | Dashboard showing unrouted items with one-click routing |
| Promotion | Manual copy/move | Swipe-to-approve in CMD_E |
| Anti-pattern detection | Self-awareness | AI Challenge Console (NAV_F) proactively warns you |

**The goal:** The platform removes the friction from these practices. The rituals stay the same — the effort to execute them drops to near zero.

---

## 13. CLAUDE CODE SESSION PROTOCOL

Until the platform is built, Claude Code is the primary work interface. These are the exact steps for every Claude Code session:

### Session Start (Every Time)

```
1. CHECK STATE
   - Read: 02_COMMAND_DECK/ACTIVE_SESSIONS/YYYY-MM/ (latest file)
   - Read: ~/.claude/projects/C--Users-under/memory/MEMORY.md
   - Read: Current project's PRD or canon doc

2. CHECK FOR SESSION LOG
   - Does today's session log exist?
   - If resuming: read the last session log

3. LOAD CONTEXT
   - Only load files DIRECTLY relevant to today's intent
   - DO NOT load "everything"

4. CONFIRM READY
   - State: "I've loaded context from [files]. Your last session [date] focused on [topic].
     Today we're working on [intent]. Ready to begin."
```

### During Session

```
- Log decisions as they happen
- Route outputs immediately (don't pile up)
- Ask before any destructive action
- Count before and after any batch operation
- Checkpoint after every significant operation
```

### Session End

```
1. FILE OUTPUTS
   - Route every created/modified file to correct location
   - Update any indices affected

2. COMPLETE SESSION LOG
   - Create: 02_COMMAND_DECK/ACTIVE_SESSIONS/YYYY-MM/YYYY-MM-DD_session_NN.md
   - Content: What got done, what got rejected, key decisions, files created, tomorrow's focus

3. FULL TRANSCRIPT (if significant session)
   - Save to: 04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/YYYY-MM-DD_session_NN_full.md

4. UPDATE MEMORY
   - If any stable patterns learned, update MEMORY.md
   - If any kit roles or architectural decisions changed, update relevant memory files

5. CONFIRM CLOSED
   - State what was accomplished and what the next session's first action should be
```

---

## 14. FILE DESTINATION ROUTING TABLE

When you create something, here's where it goes:

| Output Type | Destination |
|---|---|
| Session summary | `02_COMMAND_DECK/ACTIVE_SESSIONS/YYYY-MM/` |
| Full transcript | `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/` |
| PRD | `07_BUILD_FACTORY/PRJ_*/02_Product/` |
| Screen inventory | `07_BUILD_FACTORY/PRJ_*/03_Design/` |
| React component | `07_BUILD_FACTORY/PRJ_*/05_Development/` |
| Framework/SOP | `06_DOMAIN_PILLARS/PIL_*/00_CANON/` (if canonical) or `02_artifacts/` |
| Decision log | `01_NAVIGATION_CENTRE/DECISION_LOG/` |
| State snapshot | `01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/` |
| Script/tool | `03_CORE_ENGINE/SCRIPTS/` |
| Index/report | `03_CORE_ENGINE/INDICES/` |
| Template | `05_TEMPLATE_HUB/` |
| Marketing content | `08_OPERATIONS/` |
| Raw intake (to process) | `04_KNOWLEDGE_LIBRARY/EXTRACTION_PIPELINE/RAW_INTAKE/` |
| Don't know | `04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/` — NEVER leave in root |

---

## 15. SUCCESS CRITERIA

### Personal (John — Month 1)

- [ ] Morning Start ritual executed 5+ days/week
- [ ] Average 2-3 work blocks per day, max 120 min each
- [ ] Every session produces a session log
- [ ] End of Day ritual executed 5+ days/week
- [ ] Weekly review completed every Sunday
- [ ] Zero files in root folders
- [ ] Zero unrouted items older than 7 days
- [ ] Exercise 5+ days/week before screen time

### System (Month 3)

- [ ] 100+ session logs searchable
- [ ] 50+ items promoted to Canonical
- [ ] State Snapshots auto-generated daily
- [ ] Morning Brief producing useful summaries
- [ ] Goal Health Dashboard reflecting reality

### Platform (Month 6)

- [ ] All rituals enforced by the platform UI
- [ ] Session management fully automated
- [ ] Context loading via semantic search (no manual file reading)
- [ ] AI Challenge Console active and generating useful challenges
- [ ] Anti-pattern detection operational

---

**END OF WORKING PRACTICES PRD**

**This document is the operational manual for Enterprise OS V7.**
**Read it at the start of every week. Internalize the rituals.**
**The system is only as good as the discipline applied to it.**
**Last Updated:** 2026-02-17
