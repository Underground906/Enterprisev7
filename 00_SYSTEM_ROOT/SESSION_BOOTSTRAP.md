# SESSION BOOTSTRAP — Read This First

**Purpose:** This document tells any LLM (Claude, GPT, Gemini, DeepSeek) exactly what to read to understand Enterprise OS and pick up where the last session left off.

**Owner:** John
**System:** Enterprise OS V7
**Location:** `C:\Users\under\Downloads\ENTERPRISE_OS_V7\`

---

## Step 1: Read These 5 Files (In Order)

### 1.1 Operating Rules
```
00_SYSTEM_ROOT/CLAUDE.md
```
- System architecture (8 components, 23 pillars)
- Rules for file operations (what to do, what NOT to do)
- How to add content, log work, manage goals
- 27 extraction domains
- Tech stack

### 1.2 Current System State
```
01_NAVIGATION_CENTRE/STATE_SNAPSHOTS/[READ THE LATEST FILE]
```
- What's working, what's broken
- All active projects and their progress %
- Priority stack
- Pillar health status

### 1.3 Last Session
```
02_COMMAND_DECK/ACTIVE_SESSIONS/2026-02/[READ THE LATEST FILE]
```
- What was accomplished last session
- What's planned for next session
- Decisions made
- Blockers identified

### 1.4 Session History
```
04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/SESSION_INDEX.md
```
- Chronological list of all sessions
- Quick scan for context on recent work

### 1.5 Full Architecture (Only When Doing Deep Work)
```
00_SYSTEM_ROOT/MASTER_CONTEXT.md
```
- 680-line comprehensive system document
- 27 extraction domains (canonical)
- V7 architecture details
- Core frameworks (Activation Context, S→C→E, 17-Step Factory)
- Pillar integration map
- Read this when: building new features, routing content, architectural decisions

---

## Step 2: Confirm Context

After reading, say:

> "I've read the latest state. Last session covered [X]. Current priorities are [Y]. Ready to start — what's the focus today?"

---

## Step 3: Project-Specific Context (Read When Needed)

| If Working On... | Also Read... |
|-------------------|-------------|
| Property Connect London | `07_BUILD_FACTORY/PRJ_Property_Connect_London/` |
| LeadEngine Platform | `07_BUILD_FACTORY/PRJ_LeadEngine_Platform/02_Requirements/COMPLETE_BUILD_SPEC.md` |
| Fitness App | `07_BUILD_FACTORY/PRJ_Fitness_Platform/` + `06_DOMAIN_PILLARS/PIL_20_FITNESS/` |
| UI Library | `07_BUILD_FACTORY/PRJ_UI_Component_Library/03_Design/KIT_INDEX.json` |
| Content/Copy work | `06_DOMAIN_PILLARS/PIL_03_COPY/00_CANON/` + `PIL_04_CONTENT/00_CANON/` |
| System architecture | `00_SYSTEM_ROOT/MASTER_CONTEXT.md` (full read) |
| Ingesting content | `04_KNOWLEDGE_LIBRARY/README.md` |
| Any specific pillar | `06_DOMAIN_PILLARS/PIL_XX_NAME/00_CANON/README.md` |

---

## Critical Rules (Non-Negotiable)

1. **ALL outputs go in ENTERPRISE_OS_V7/** — never scatter files in Downloads or Desktop
2. **NEVER delete/move/rename files** without explicit approval from John
3. **23 pillars** (PIL_01 through PIL_23) — never invent new ones
4. **Log every session** — summary in Command Deck, transcript in Knowledge Library
5. **Count before and after** every batch operation
6. **Checkpoint after every batch** — never lose progress
7. **If unsure where something goes** → `04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/`

---

## The 23 Domain Pillars

| # | Name | Type |
|---|------|------|
| 01 | AVATARS | Customer personas |
| 02 | BRANDING | Brand identity |
| 03 | COPY | Copywriting systems |
| 04 | CONTENT | Content strategy |
| 05 | GRAPHICS | Visual assets |
| 06 | VIDEO | Video production |
| 07 | UI_LIBRARY | Component library |
| 08 | KNOWLEDGE_INGESTION | How system learns |
| 09 | ROLES_SKILLS | Workforce definitions |
| 10 | WORKING_PRACTICES | SOPs & workflows |
| 11 | BUILD_STORY | Build documentation |
| 12 | KEYWORDS | Keyword systems |
| 13 | SEO | Search optimization |
| 14 | NAVIGATION | Goals & routing |
| 15 | ENTERPRISE_OS | System governance |
| 16 | CONTENT_GENERATION | Auto content pipelines |
| 17 | RAG_SYSTEM | Retrieval & indexing |
| 18 | AGENT_FRAMEWORK | AI agent orchestration |
| 19 | PROPERTY | Property vertical |
| 20 | FITNESS | Fitness vertical |
| 21 | MARKET_RESEARCH | Research frameworks |
| 22 | VOICE_TRAINING | Voice/speaking vertical |
| 23 | DOG_PLATFORM | Dog training vertical |

---

## End of Session Protocol

Before ending ANY session:

1. Create/update session log: `02_COMMAND_DECK/ACTIVE_SESSIONS/YYYY-MM/YYYY-MM-DD_session_NN.md`
2. Export full transcript: `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/YYYY-MM/`
3. Update session index: `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/SESSION_INDEX.md`
4. Commit to git if meaningful work was done

---

**This document is the entry point. Everything else flows from here.**
