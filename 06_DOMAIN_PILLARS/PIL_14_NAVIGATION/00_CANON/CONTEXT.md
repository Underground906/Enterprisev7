# PIL_14_NAVIGATION — CONTEXT DOC

**Purpose:** Complete context for any AI/agent working with the Navigation system  
**Version:** 1.0  
**Status:** Production-ready

---

## SYSTEM OVERVIEW

The Navigation System is the **decision and execution engine** for Enterprise_OS. It sits above all projects, platforms, tools, and agents. While projects come and go, the Navigation System endures.

**Core Function:** Convert chaotic goals into structured, AI-managed execution paths.

---

## THE 5A + 5 DYNAMIC LAYERS FRAMEWORK

### Foundation Layer (The 5 As)

| Layer | Purpose | Refresh Cycle |
|-------|---------|---------------|
| **A1. ALIGNMENT** | Direction, meaning, coherence | 90 days |
| **A2. AWARENESS** | Risk/gap/constraint surfacing | Continuous |
| **A3. ACCOUNTABILITIES** | Outcome ownership | 90 days |
| **A4. ACTIVITIES** | Weekly execution rhythm | Weekly |
| **A5. ASSETS** | Leverage and compounding | Quarterly |

### Dynamic Layer (AI-Managed)

| Layer | Purpose | Refresh Cycle |
|-------|---------|---------------|
| **D6. STATE** | Current reality snapshot | Daily |
| **D7. DECISIONS** | Course change log | Real-time |
| **D8. LEARNING** | Pattern extraction | Weekly |
| **D9. ITERATIONS** | Plan version control | Per change |
| **D10. AI DIALOGUE** | System challenges/alerts | Continuous |

---

## GOAL CLASSIFICATION SCHEMA

### Goal Type
```
vision      → Long-term north star
outcome     → Measurable result
project     → Bounded deliverable
task        → Single action
problem     → Issue to resolve
awareness   → Thing to track
```

### Domain
```
personal    → Health, relationships, identity
business    → Revenue, products, operations
platform    → Specific platform (Property, Fitness, etc.)
founder     → Founder-specific (energy, skills, capacity)
enterprise  → Company-wide systems
```

### Specificity
```
vague       → "I want to be wealthy"
directional → "Increase revenue"
defined     → "£100K MRR by Q2"
detailed    → Full PRD with specs
```

### Urgency
```
survival    → Business depends on this
critical    → Major trajectory impact
important   → Significant but not existential
improvement → Would help but not essential
```

---

## GOAL INTAKE PIPELINE

```
┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
│ CAPTURE │ → │  PARSE  │ → │  GRADE  │ → │  PLACE  │ → │ SCHEDULE│
└─────────┘   └─────────┘   └─────────┘   └─────────┘   └─────────┘
     ↓             ↓             ↓             ↓             ↓
  Raw dump     Extract       Score 1-10    Route to      Time block
  any format   type/domain   readiness     domain        allocation

┌─────────┐   ┌─────────┐
│  TRACK  │ → │ REVIEW  │
└─────────┘   └─────────┘
     ↓             ↓
  Log state    Adjust course
  AI refresh   Extract learning
```

### Stage Details

**CAPTURE:** Accept any input format
- Vague visions, dreams, problems, specs
- No structure required
- Log: timestamp, raw text, emotional charge

**PARSE:** AI extracts
- Goal type, domain, specificity
- Dependency hints, conflict hints
- Source context

**GRADE:** Score readiness
- Clarity (1-10)
- Actionability (1-10)
- Resource alignment (1-10)
- Priority signal (1-10)

**PLACE:** Route to correct domain
- Personal → Personal Navigation
- Business → Business Navigation
- Platform-specific → Platform pillar
- Cross-domain → Flag for splitting

**SCHEDULE:** Allocate time
- 90-day accountability assignment
- Weekly activity blocks
- Daily task generation

**TRACK:** Maintain state
- AI-refreshed daily
- Health metrics calculated
- Red flags detected

**REVIEW:** Adjust and learn
- What worked/failed
- Assumptions tested
- Course corrections logged

---

## NAVIGATION VARIANTS

### Personal Navigation
**Domains:** Health, energy, relationships, identity, learning  
**Intake Focus:** Emotional charge, life impact, energy cost

### Business Navigation
**Domains:** Revenue, products, market, operations, team  
**Intake Focus:** Financial impact, runway, resource requirements

### Enterprise Navigation
**Domains:** Systems, platforms, architecture, governance  
**Intake Focus:** Scale impact, technical debt, integration

### Skills Navigation
**Domains:** Capabilities, expertise, certifications  
**Intake Focus:** Learning path, practice requirements, mastery level

---

## 90-DAY ACCOUNTABILITY MODEL

### Key Principles
- **3-6 critical outcomes** per 90-day period
- **ONE clear owner** per outcome
- Ownership is about **outcome, not effort**
- **Time-boxed** (30/60/90 days)
- **Reviewable and replaceable** (no identity lock-in)

### Accountability Structure
```yaml
accountability:
  id: ACC_001
  owner: [name]
  outcome: [specific measurable result]
  success_criteria:
    - [criterion 1]
    - [criterion 2]
  review_cadence: weekly | biweekly | monthly
  deadline: [date]
  status: active | blocked | complete | transferred
```

---

## FOLDER STRUCTURE

```
PIL_14_NAVIGATION/
├── 00_CANON/              → Production-ready frameworks
├── 01_ROUTING_LOGIC/      → Classification and routing rules
├── 02_SESSION_MANAGEMENT/ → Links to PIL_10
├── 03_GOAL_FLOW/
│   └── GOAL_LIBRARY/      → Individual goal specs
├── 04_CROSS_REFERENCES/   → Pillar dependencies
├── 01_threads/            → Source conversations
├── 02_artifacts/          → Working documents
└── 90_ARCHIVE/
    ├── raw_user_turns/
    ├── superseded_versions/
    └── source_materials/
```

---

## INTEGRATION POINTS

### Feeds Into
- **PIL_10_WORKING_PRACTICES** — Session design, daily execution
- **PIL_08_KNOWLEDGE_INGESTION** — Thread routing, extraction triggers
- **PIL_15_ENTERPRISE_OS** — System-wide orchestration
- **07_BUILD_FACTORY** — Project initiation

### Receives From
- **Goal intake** — Raw dumps from any source
- **Thread analysis** — Extracted goals from conversations
- **AI dialogue** — System suggestions and alerts

### AI Agent Interactions
- **Daily state refresh** — AI updates Current_State.md
- **Risk detection** — AI populates Red_Flags.md
- **Activity generation** — AI creates daily task lists
- **Health scoring** — AI calculates alignment health
- **Decision prompts** — AI challenges assumptions

---

## CANON FILES (Production-Ready)

| File | Purpose |
|------|---------|
| 01_5A_NAVIGATION_SYSTEM.md | Core framework definition |
| NAVIGATION_CENTRE_ENHANCED_SYSTEM.md | Full system + dynamic layers |
| GOAL_INTAKE_SYSTEM_V1.md | Intake pipeline spec |
| NAVIGATION_BUSINESS_FULL.md | Business goal wizard |
| NAVIGATION_PERSONAL_FULL.md | Personal goal wizard |
| NAVIGATION_ENTERPRISE_FULL.md | Enterprise goal wizard |
| NAVIGATION_SKILLS_FULL.md | Skills goal wizard |

---

## USAGE INSTRUCTIONS

### For AI/Agents

When working with Navigation:

1. **Goal intake:** Use GOAL_INTAKE_SYSTEM pipeline
2. **Classification:** Apply type/domain/specificity schema
3. **Routing:** Place in correct Navigation variant
4. **State updates:** Refresh Current_State.md daily
5. **Decision logging:** Record all course changes

### For Humans

1. **Dump goals freely** — System accepts any format
2. **Review AI classifications** — Correct if needed
3. **Check 90-day accountabilities** — Ensure ownership clear
4. **Weekly review** — Activities vs outcomes
5. **Quarterly realignment** — Full 5A refresh

---

## RELATED PILLARS

| Pillar | Relationship |
|--------|--------------|
| PIL_08_KNOWLEDGE_INGESTION | Thread → Goal extraction |
| PIL_10_WORKING_PRACTICES | Daily session execution |
| PIL_15_ENTERPRISE_OS | System architecture |
| PIL_18_AGENT_FRAMEWORK | AI agent orchestration |
| 07_BUILD_FACTORY | Project execution |

---

**END OF CONTEXT DOC**
