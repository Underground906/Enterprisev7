# SESSION ROUTER

## Purpose
Determines where new chat sessions should be directed based on intent.

## Routing Logic

### If goal-related:
- New goal → 01_NAVIGATION_CENTRE/GOAL_INTAKE/
- Existing goal work → 01_NAVIGATION_CENTRE/ACTIVE_GOALS/GOAL_[Name]/

### If task execution:
- Active session → 02_COMMAND_DECK/ACTIVE_SESSIONS/
- Agent work → 02_COMMAND_DECK/AGENT_WORKSPACE/

### If domain-specific:
- Route to appropriate pillar in 06_DOMAIN_PILLARS/

### If project work:
- Route to 07_BUILD_FACTORY/PRJ_[Name]/

## Default
Unclassifiable → 04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/
