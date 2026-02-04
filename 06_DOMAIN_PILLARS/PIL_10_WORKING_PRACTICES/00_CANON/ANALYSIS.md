# PIL_10_WORKING_PRACTICES — CANON EXTRACTION ANALYSIS

**Files:** 1 thread + 21 artifacts = 22 total
**Date:** 2026-02-03

---

## EXECUTIVE SUMMARY

The Working Practices pillar contains a **comprehensive milestone-based workflow system** with 7 interrelated milestones covering session design, PARA methodology, agent handoff, and knowledge extraction practices. The content is mature and well-structured, with clear dependency chains between milestones.

**Core Framework:** Milestone Anchor Loop (90-120 minute work cycles)
**Key Innovation:** Three-lane ingestion (Historical, Fresh, External)

---

## CLASSIFICATION

### TIER 1: PRODUCTION-READY CANON (8 files)

| File | Purpose | Status |
|------|---------|--------|
| `master_milestone_map.md` | 7-milestone dependency graph | ✅ Canon |
| `milestone_best_practices.md` | PARA + session hygiene + quality control | ✅ Canon |
| `milestone_anchor_doc.md` | RAG/database milestone spec | ✅ Canon |
| `milestone_hand_off_aider.md` | Agent handoff protocols | ✅ Canon |
| `milestone_recent_chats.md` | Project goals + 3-lane ingestion | ✅ Canon |
| `milestone_big_picture_prd.md` | PRD creation methodology | ✅ Canon |
| `milestone_analyse_claude.md` | Claude file analysis workflow | ✅ Canon |
| `milestone_untangle_enterprise_final.md` | Folder structure correction | ✅ Canon |

### TIER 2: DUPLICATES/VARIANTS (consolidate)

| File | Duplicate Of | Action |
|------|--------------|--------|
| `master_milestone_map (1).md` | master_milestone_map.md | Archive |
| `ekx_1_methodology_guide.md` | PIL_08 version | → Move to PIL_08 or archive |
| `ekx_1_methodology_guide (1).md` | PIL_08 version | Archive |
| `milestone_best_practices_separate.md` | milestone_best_practices.md | Merge or archive |
| `milestone_best_practices_standalone.md` | milestone_best_practices.md | Merge or archive |
| `milestone_analyse_claude_separate.md` | milestone_analyse_claude.md | Merge or archive |
| `milestone_hand_off_aider_separate.md` | milestone_hand_off_aider.md | Merge or archive |
| `milestone_hand_off_aider (1).md` | milestone_hand_off_aider.md | Archive |
| `milestone_big_picture_prd_separate.md` | milestone_big_picture_prd.md | Merge or archive |
| `milestone_create_big_picture_prd.md` | milestone_big_picture_prd.md | Merge or archive |
| `milestone_create_prd.md` | milestone_big_picture_prd.md | Merge or archive |
| `milestone_create_prd (1).md` | milestone_big_picture_prd.md | Archive |
| `milestone_untangle_enterprise.md` | milestone_untangle_enterprise_final.md | Archive (superseded) |

### TIER 3: THREADS (1 file)

| Thread | Topic | Action |
|--------|-------|--------|
| `Knowledge_management_workflow_design.md` | Core methodology development | Keep for reference |

---

## KEY FRAMEWORKS EXTRACTED

### 1. The 7 Milestones (Dependency Order)

```
FOUNDATION LAYER (Infrastructure):
├── M1: Build RAG Knowledge Base & Database
├── M6: Untangle ENTERPRISE Folder

OPERATIONAL LAYER (Procedures):
├── M2: Hand-off to Coder/Agent (Aider)
├── M3: Working Best Practices & Session Hygiene

STRATEGIC LAYER (Integration):
├── M4: Create Big-Picture PRD
├── M5: Analyse Claude Files & ~78 Files
└── M7: Recent Chats - Project Goals & Context
```

### 2. Milestone Anchor Loop (90-120 minutes)

```
1. INVENTORY  → List files, identify gaps, update manifest
2. EXTRACT    → Capture decisions/rules/specs with evidence
3. SYNTHESIZE → Create Anchor_[Milestone].md
4. DERIVE     → Spawn SOPs, templates, scripts
5. FILE       → Apply PARA routing, update indices
6. LOG        → Add to DECISIONS.md, set one tiny next step
```

### 3. Three-Lane Ingestion Framework

```
LANE A: Historical Backlog
├── Stage → Pair names → Textify → Completeness report
├── Handle resume/skip for large backlogs
└── Focus on completeness before moving forward

LANE B: Fresh Work (Real-time)
├── Drop into staging + mini-manifest
├── Pair and align naming
├── Hot-path routing via subject rules
└── Quarantine mismatches

LANE C: External Media
├── Medium-specific checklists (Book/YouTube/Web/PDF)
├── Convert to readable formats
├── Output per-doc JSON + .deep.md
└── Join shared indices
```

### 4. Two-Hour Work Block System

```
SUSTAINABLE MICRO-PROGRESS:
- ≤3 decisions per cycle
- Visible wins required
- One tiny next step always defined
- DECISIONS.md logging mandatory
```

### 5. PARA Implementation

```
FOLDER STRUCTURE:
0_INBOX     → Staging area (process weekly)
1_PROJECTS  → Active work with outcome + timeframe
2_AREAS     → Ongoing responsibilities (CAPS naming)
3_RESOURCES → Reference material (lowercase naming)
4_ARCHIVES  → Completed/inactive

RITUALS:
- 60-second reset when overwhelmed
- Weekly maintenance (~5 min)
- Evidence-based finals detection
```

### 6. Agent Handoff Protocol

```
MICRO-STEP EXECUTION:
- One step at a time
- ≥0.90 confidence threshold
- Always dry-run first
- DB rebuild after every batch
- Coverage tracking as north star

SAFETY MECHANISMS:
- High-confidence filtering
- Human confirmation required
- Plain English feedback
- Visible progress wins
```

### 7. Session Hygiene Protocols

```
CAPTURE EVERY Q→A TURN:
- Inputs/outputs with versions
- Definitive artifact detection
- Evidence-based status tracking

TWO-LANE STAGING:
- Review mode: uncertain routing
- Auto mode: confident routing

MANIFEST-FIRST DISCIPLINE:
- Never ingest without populated fields
- qa[], definitive, ingest_mode required
```

---

## CANON DOCUMENT STRUCTURE

After consolidation, PIL_10 should contain:

```
PIL_10_WORKING_PRACTICES/
├── 00_CANON/
│   ├── MASTER_MILESTONE_MAP.md         ← 7-milestone dependency graph
│   ├── MILESTONE_ANCHOR_LOOP.md        ← 90-120min work cycle SOP
│   ├── THREE_LANE_INGESTION.md         ← Historical/Fresh/External
│   ├── SESSION_HYGIENE.md              ← File-as-you-go + PARA
│   ├── AGENT_HANDOFF_PROTOCOL.md       ← Aider/automation handoff
│   └── TWO_HOUR_WORK_BLOCKS.md         ← Sustainable pacing
│
├── 01_SESSION_DESIGN/
│   └── work_block_templates.md
│
├── 02_PACING_RECOVERY/
│   └── energy_management.md
│
├── 03_AI_GUIDANCE/
│   └── model_selection_guide.md
│
├── 04_MILESTONES/
│   ├── M1_RAG_DATABASE.md
│   ├── M2_AGENT_HANDOFF.md
│   ├── M3_BEST_PRACTICES.md
│   ├── M4_BIG_PICTURE_PRD.md
│   ├── M5_CLAUDE_ANALYSIS.md
│   ├── M6_FOLDER_STRUCTURE.md
│   └── M7_PROJECT_GOALS.md
│
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
    └── superseded_versions/
```

---

## CROSS-PILLAR CONNECTIONS

| Related Pillar | Connection |
|----------------|------------|
| PIL_14_NAVIGATION | Goals drive session priorities |
| PIL_08_KNOWLEDGE_INGESTION | Three-lane ingestion originates content |
| PIL_15_ENTERPRISE_OS | System architecture alignment |
| PIL_18_AGENT_FRAMEWORK | Agent handoff protocols |
| 02_COMMAND_DECK | Daily execution interface |

---

## IMMEDIATE ACTIONS

1. **Move to 00_CANON:** 8 core milestone docs
2. **Archive duplicates:** 13 variant/duplicate files
3. **Create derived docs:** 
   - MILESTONE_ANCHOR_LOOP.md (extracted SOP)
   - THREE_LANE_INGESTION.md (extracted framework)
   - SESSION_HYGIENE.md (extracted protocols)
4. **Move EKX-1 docs** to PIL_08 (that's their home)

---

**END OF ANALYSIS**
