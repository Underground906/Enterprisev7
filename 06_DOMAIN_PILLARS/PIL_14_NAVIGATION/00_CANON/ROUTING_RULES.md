# PIL_14_NAVIGATION — ROUTING RULES

---

## Inbound Routing (What comes here)

### From Goal Intake (any source)

```
IF content_type == "goal" OR content_type == "objective" OR content_type == "outcome"
THEN route_to PIL_14_NAVIGATION

IF input CONTAINS ["goal", "want to", "need to", "planning to", "objective", "target"]
AND NOT (input CONTAINS ["keyword", "copy", "content", "UI", "code"])
THEN route_to PIL_14_NAVIGATION/02_artifacts/
```

### From Thread Analysis

```
IF thread_topic CONTAINS ["navigation", "goals", "5A", "alignment", "accountability", 
                          "90-day", "quarterly", "planning", "roadmap", "priority"]
THEN route_to PIL_14_NAVIGATION/01_threads/

IF thread produces goal_spec OR prd
THEN copy_to PIL_14_NAVIGATION/03_GOAL_FLOW/GOAL_LIBRARY/
```

### From Other Pillars

| Source Pillar | Trigger | Destination |
|---------------|---------|-------------|
| PIL_08_KNOWLEDGE_INGESTION | Goal extracted from thread | 03_GOAL_FLOW/GOAL_LIBRARY/ |
| PIL_15_ENTERPRISE_OS | System-level goal defined | 03_GOAL_FLOW/GOAL_LIBRARY/ |
| 01_NAVIGATION_CENTRE | Active goal created | 03_GOAL_FLOW/ |
| 02_COMMAND_DECK | Session produces goal refinement | 02_artifacts/ |

---

## Outbound Routing (What leaves here)

| Destination | Trigger | Content Type |
|-------------|---------|--------------|
| PIL_10_WORKING_PRACTICES | Session design needed | Session protocols |
| PIL_09_ROLES_SKILLS | Agent/role definition needed | Role specs |
| PIL_15_ENTERPRISE_OS | System architecture impact | Architecture docs |
| 07_BUILD_FACTORY | Goal becomes project | Project initiation |
| 02_COMMAND_DECK | Goal ready for execution | Active tasks |
| 05_TEMPLATE_HUB | Template created | Reusable templates |
| 90_ARCHIVE | Content superseded | Old versions |

### Specific Outbound Rules

```
IF artifact_type == "template" OR artifact_type == "wizard"
THEN move_to 05_TEMPLATE_HUB/NAVIGATION_TEMPLATES/

IF goal_status == "ready_for_execution"
THEN create_project_in 07_BUILD_FACTORY/

IF content_topic == "working_practices" OR "session_design"
THEN move_to PIL_10_WORKING_PRACTICES/

IF content_topic == "ai_roles" OR "agent_definition"
THEN move_to PIL_09_ROLES_SKILLS/
```

---

## Internal Routing

### Promotion Path
```
02_artifacts/ → 00_CANON/        (when tested and production-ready)
02_artifacts/ → 03_GOAL_FLOW/    (when goal spec finalized)
01_threads/   → 90_ARCHIVE/      (after extraction complete)
```

### Archive Path
```
02_artifacts/ → 90_ARCHIVE/superseded_versions/  (when newer version exists)
*_FULL.md supersedes base version (e.g., NAVIGATION_BUSINESS_FULL supersedes NAVIGATION_BUSINESS)
USER_TURNS_*.md → 90_ARCHIVE/raw_user_turns/     (after insights extracted)
```

### Goal Lifecycle
```
RAW_INTAKE → 02_artifacts/                      (initial capture)
           → 03_GOAL_FLOW/GOAL_LIBRARY/         (when classified)
           → 01_NAVIGATION_CENTRE/GOAL_[Name]/  (when active)
           → 07_BUILD_FACTORY/PRJ_[Name]/       (when project starts)
           → 90_ARCHIVE/                        (when complete)
```

---

## Cross-References

### This pillar references:

| Pillar | Reference Type | Purpose |
|--------|---------------|---------|
| PIL_08_KNOWLEDGE_INGESTION | Extraction rules | How to extract goals from threads |
| PIL_10_WORKING_PRACTICES | Session protocols | How to execute daily activities |
| PIL_15_ENTERPRISE_OS | System architecture | Where navigation fits in system |
| PIL_18_AGENT_FRAMEWORK | Agent definitions | AI agents that manage navigation |

### This pillar is referenced by:

| Pillar | Reference Type | Purpose |
|--------|---------------|---------|
| PIL_08_KNOWLEDGE_INGESTION | Routing destination | Where to send extracted goals |
| PIL_10_WORKING_PRACTICES | Goal source | What drives session priorities |
| 01_NAVIGATION_CENTRE | System implementation | Active goal management |
| 02_COMMAND_DECK | Task source | Daily execution queue |
| 07_BUILD_FACTORY | Project source | Project initiation |

---

## Classification Rules

### Goal Type Classification
```yaml
vision:      "Long-term north star, 3+ years"
outcome:     "Measurable result, specific target"
project:     "Bounded deliverable with start/end"
task:        "Single action, hours to days"
problem:     "Issue to resolve, blocker"
awareness:   "Thing to track, not actionable yet"
```

### Domain Classification
```yaml
personal:    "Health, relationships, identity, learning"
business:    "Revenue, products, market, operations"
platform:    "Specific platform (Property, Fitness, etc.)"
founder:     "Founder-specific (energy, skills, capacity)"
enterprise:  "Company-wide systems, architecture"
```

### Routing by Domain
```
personal   → NAVIGATION_PERSONAL_FULL.md
business   → NAVIGATION_BUSINESS_FULL.md
enterprise → NAVIGATION_ENTERPRISE_FULL.md
skills     → NAVIGATION_SKILLS_FULL.md
platform   → Route to specific PIL_19/20/22/23
```

---

## Validation Rules

- [ ] All files in 00_CANON/ have status: production
- [ ] No duplicate goal IDs in GOAL_LIBRARY
- [ ] All threads have extraction_status: complete | in_progress | pending
- [ ] Cross-references are bidirectional (if A→B then B←A documented)
- [ ] Templates are in 05_TEMPLATE_HUB, not 00_CANON
- [ ] Superseded files are in 90_ARCHIVE, not 02_artifacts

---

## File Naming Conventions

```
Goals:          GOAL_XXX_[NAME].md (e.g., GOAL_001_NAVIGATION_SYSTEM.md)
Navigation:     NAVIGATION_[DOMAIN]_[TYPE].md (e.g., NAVIGATION_BUSINESS_FULL.md)
Templates:      TEMPLATE_[TYPE]_[VARIANT].md
User Turns:     USER_TURNS_[TOPIC].md
Combined:       _COMBINED_[TOPIC].md (underscore prefix = synthesis doc)
```

---

**Last Updated:** 2026-02-03
