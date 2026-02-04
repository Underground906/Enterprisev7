# PIL_10_WORKING_PRACTICES — CONTEXT DOC

**Purpose:** Complete context for any AI/agent working with session design and work practices  
**Version:** 1.0  
**Status:** Production-ready

---

## SYSTEM OVERVIEW

The Working Practices pillar defines **how work gets done** in Enterprise_OS. It contains session design patterns, sustainable pacing protocols, AI guidance, and the milestone-based workflow system that structures all execution.

**Core Function:** Convert goals into sustainable, trackable work sessions with clear handoff procedures.

---

## THE 7-MILESTONE SYSTEM

### Milestone Dependency Graph

```
FOUNDATION LAYER (Infrastructure):
├── M1: Build RAG Knowledge Base & Database ────┐
├── M6: Untangle ENTERPRISE Folder ────────────┤
│                                               │
OPERATIONAL LAYER (Procedures):                 │
├── M2: Hand-off to Coder/Agent (Aider) ───────┤
├── M3: Working Best Practices & Session Hygiene┤
│                                               │
STRATEGIC LAYER (Integration):                  │
├── M4: Create Big-Picture PRD ────────────────┤
├── M5: Analyse Claude Files & ~78 Files ──────┤
└── M7: Recent Chats - Project Goals & Context ─┘
```

### Milestone Summaries

| Milestone | Purpose | Key Deliverable |
|-----------|---------|-----------------|
| M1 | Database infrastructure | brain.db with PARA mapping |
| M2 | Automation handoff | Agent-ready procedures |
| M3 | Session discipline | PARA + file-as-you-go |
| M4 | PRD methodology | Fast-lane synthesis |
| M5 | Batch processing | Deep extraction workflow |
| M6 | Folder correction | Clean workspace structure |
| M7 | Goal alignment | Three-lane ingestion |

---

## MILESTONE ANCHOR LOOP (90-120 minutes)

The core work cycle for any focused session:

```
┌──────────┐   ┌──────────┐   ┌───────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ INVENTORY│ → │ EXTRACT  │ → │ SYNTHESIZE│ → │  DERIVE  │ → │   FILE   │ → │   LOG    │
└──────────┘   └──────────┘   └───────────┘   └──────────┘   └──────────┘   └──────────┘
     ↓              ↓              ↓              ↓              ↓              ↓
  List files    Capture       Create        Spawn SOPs      PARA route    DECISIONS.md
  Find gaps     decisions     Anchor doc    templates       Update        Next step
  Update        with          Overview      scripts         indices       
  manifest      evidence      + SOPs
```

### Stage Details

| Stage | Duration | Output |
|-------|----------|--------|
| **INVENTORY** | 10-15 min | files_manifest.csv updated |
| **EXTRACT** | 20-30 min | per-doc JSON with evidence |
| **SYNTHESIZE** | 20-30 min | Anchor_[Milestone].md |
| **DERIVE** | 15-20 min | SOPs, templates, scripts |
| **FILE** | 10-15 min | PARA routing, index updates |
| **LOG** | 5 min | DECISIONS.md entry, next step |

---

## THREE-LANE INGESTION FRAMEWORK

All content enters through one of three lanes:

```
┌─────────────────────────────────────────────────────────────────┐
│                    THREE-LANE INGESTION                          │
├─────────────────┬─────────────────┬─────────────────────────────┤
│   LANE A        │    LANE B       │         LANE C              │
│   Historical    │    Fresh        │         External            │
│   Backlog       │    Real-time    │         Media               │
├─────────────────┼─────────────────┼─────────────────────────────┤
│ Stage           │ Drop to staging │ Medium-specific checklist   │
│ Pair names      │ Mini-manifest   │ Convert to readable         │
│ Textify         │ Hot-path route  │ Output JSON + .deep.md      │
│ Complete report │ Quarantine miss │ Join shared indices         │
├─────────────────┴─────────────────┴─────────────────────────────┤
│                         ↓                                        │
│              Shared Indices + per-doc JSON                       │
└─────────────────────────────────────────────────────────────────┘
```

### Lane A: Historical Backlog
- Process accumulated content
- Resume/skip logic for large batches
- Completeness before moving forward

### Lane B: Fresh Work
- Real-time capture
- Subject rule routing
- Quarantine uncertain items

### Lane C: External Media
- Books, YouTube, Web, PDF, Podcasts
- Medium-specific processing
- Full extraction to shared format

---

## TWO-HOUR WORK BLOCK SYSTEM

Sustainable pacing for knowledge work:

```yaml
work_block:
  duration: 90-120 minutes
  max_decisions: 3 per cycle
  requirements:
    - Visible win achieved
    - One tiny next step defined
    - DECISIONS.md updated
    
recovery:
  between_blocks: 15-30 min
  full_recovery: End of day
  
cognitive_load:
  track: Decision density
  limit: Avoid decision fatigue
  reset: When overwhelmed, 60-second PARA reset
```

---

## SESSION HYGIENE PROTOCOLS

### Capture Every Q→A Turn

```yaml
must_capture:
  - Turn index (which exchange)
  - User prompt (verbatim)
  - Assistant reply (verbatim)
  - Artifacts produced
  - Version status (draft/candidate/approved)
  - Evidence for finals
```

### Two-Lane Staging

```yaml
review_mode:
  trigger: Confidence < 0.90
  action: Hold for human review
  
auto_mode:
  trigger: Confidence >= 0.90 AND non-"Other"
  action: Route automatically
```

### Manifest-First Discipline

```yaml
never_ingest_without:
  - qa[] array populated
  - definitive flag set
  - ingest_mode specified
  - PARA suggestion included
```

---

## PARA IMPLEMENTATION

### Folder Structure (Universal)

```
0_INBOX/      → Staging (process weekly)
1_PROJECTS/   → Active work (outcome + timeframe + completion)
2_AREAS/      → Ongoing responsibilities (CAPS naming)
3_RESOURCES/  → Reference material (lowercase naming)
4_ARCHIVES/   → Completed/inactive
```

### Naming Conventions

```yaml
projects: "📋 Project Name" (with emoji)
areas: "AREA_NAME" (all caps)
resources: "resource_name" (lowercase)
archives: "Archive_YYYYMMDD" (dated)
```

### Maintenance Rituals

| Ritual | Frequency | Duration |
|--------|-----------|----------|
| **60-second reset** | When overwhelmed | 1 min |
| **Weekly maintenance** | Every week | 5 min |
| **Monthly review** | Every month | 30 min |

---

## AGENT HANDOFF PROTOCOL

For automating routine work with AI agents:

### Micro-Step Execution

```yaml
rules:
  - One step at a time
  - Human confirmation between steps
  - Plain English feedback
  - Visible progress required
  
thresholds:
  confidence: >= 0.90
  subject: NOT "Other"
  
safety:
  - Always dry-run first
  - DB rebuild after every batch
  - Coverage tracking as verification
```

### Handoff Procedure

```
1. DRY-RUN:   Preview operation without changes
2. VERIFY:    Check "Plan items: N, Missing src: 0"
3. APPLY:     Execute with confidence filter
4. REBUILD:   Update database
5. MEASURE:   Run coverage report
6. LOG:       Record outcome
```

---

## QUALITY CONTROL FRAMEWORK

### Evidence-Based Finals

```yaml
definitive_artifact:
  requires:
    - Source evidence (citation)
    - Approval status (draft/candidate/approved)
    - Version tracking
  
detection:
  - Explicit "FINAL" markers
  - Version history complete
  - No pending TODOs
```

### Coverage Tracking

```yaml
metrics:
  - "Other/General/General" pile size (minimize)
  - High-confidence routing percentage
  - Unrouted items count
  
thresholds:
  anomaly_detection: IQR-based
  acceptable_other: < 10% of total
```

### High-Confidence Filtering

```yaml
automated_operations:
  require: Confidence >= 0.90
  exclude: Subject == "Other"
  
uncertain_items:
  action: Quarantine for review
  location: 0_INBOX or _staging/review/
```

---

## MODEL SELECTION GUIDANCE

| Task | Recommended Model | Reason |
|------|-------------------|--------|
| Synthesis | Claude 3.5 Sonnet | Best at combining information |
| Reasoning | GPT-4.1 / o3 | Strong logical chains |
| RAG | Cohere Command | Optimized for retrieval |
| Code | Claude / GPT-4 | Both strong |
| Quick tasks | Claude Haiku | Fast, cheap |

---

## FOLDER STRUCTURE

```
PIL_10_WORKING_PRACTICES/
├── 00_CANON/
│   ├── MASTER_MILESTONE_MAP.md
│   ├── MILESTONE_ANCHOR_LOOP.md
│   ├── THREE_LANE_INGESTION.md
│   ├── SESSION_HYGIENE.md
│   ├── AGENT_HANDOFF_PROTOCOL.md
│   └── TWO_HOUR_WORK_BLOCKS.md
├── 01_SESSION_DESIGN/
├── 02_PACING_RECOVERY/
├── 03_AI_GUIDANCE/
├── 04_MILESTONES/
│   ├── M1_RAG_DATABASE.md
│   ├── M2_AGENT_HANDOFF.md
│   ├── M3_BEST_PRACTICES.md
│   ├── M4_BIG_PICTURE_PRD.md
│   ├── M5_CLAUDE_ANALYSIS.md
│   ├── M6_FOLDER_STRUCTURE.md
│   └── M7_PROJECT_GOALS.md
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

## INTEGRATION POINTS

### Receives From
- **PIL_14_NAVIGATION** → Goals and priorities for sessions
- **PIL_08_KNOWLEDGE_INGESTION** → Content requiring processing
- **02_COMMAND_DECK** → Daily task queue

### Sends To
- **PIL_08_KNOWLEDGE_INGESTION** → Session outputs for routing
- **PIL_15_ENTERPRISE_OS** → System updates
- **07_BUILD_FACTORY** → Project execution guidance

### Agent Interactions
- Session planning assistance
- Progress tracking
- Quality assurance checks
- Coverage reporting

---

## USAGE INSTRUCTIONS

### For AI/Agents

When assisting with work sessions:
1. Check current milestone focus
2. Apply Milestone Anchor Loop structure
3. Enforce two-hour block limits
4. Track decisions in DECISIONS.md
5. Ensure visible progress before closing
6. Always define next tiny step

### For Humans

1. **Start session:** Choose milestone focus
2. **Follow loop:** Inventory → Extract → Synthesize → Derive → File → Log
3. **Respect limits:** Max 3 decisions per block
4. **Recovery:** Take breaks between blocks
5. **Close properly:** Log decisions, set next step

---

## RELATED PILLARS

| Pillar | Relationship |
|--------|--------------|
| PIL_14_NAVIGATION | Goals drive session priorities |
| PIL_08_KNOWLEDGE_INGESTION | Content enters through ingestion |
| PIL_15_ENTERPRISE_OS | System architecture |
| PIL_18_AGENT_FRAMEWORK | Agent handoff destination |
| 02_COMMAND_DECK | Daily execution interface |

---

**END OF CONTEXT DOC**
