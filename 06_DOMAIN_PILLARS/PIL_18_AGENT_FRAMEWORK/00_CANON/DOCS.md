# PIL_18_AGENT_FRAMEWORK — COMPLETE DOCUMENTATION SET

**Files:** 4 threads + 83 artifacts = **87 total**
**Date:** 2026-02-03

---

# SECTION 1: README

**Pillar ID:** PIL_18  
**Domain:** System Core  
**Status:** Active (40 roles defined)

## Purpose

The Agent Framework pillar contains **40 canonical roles** for AI-native organizations, each with detailed role specs and concrete skill stacks. Roles can be filled by humans, AI agents, or hybrids. Includes team structures for organizing roles into functional units.

## Key Assets

| Asset Type | Count | Description |
|------------|-------|-------------|
| Role Definitions | 40 | Complete role specs |
| Skill Stacks | 40 | Concrete tool requirements |
| Team Structures | 11 | Functional team groupings |
| Master Index | 1 | All 40 roles listed |

## Folder Structure

```
PIL_18_AGENT_FRAMEWORK/
├── 00_CANON/
│   └── all_roles_canonical_list_40.md
├── 01_ROLES/
│   ├── executive/
│   ├── product_strategy/
│   ├── platform_engineering/
│   ├── knowledge_automation/
│   ├── go_to_market/
│   ├── operations_delivery/
│   ├── risk_sustainability/
│   └── partnerships/
├── 02_SKILL_STACKS/
├── 03_TEAM_STRUCTURES/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

# SECTION 2: CONTEXT DOC (For AI/Agents)

## System Overview

PIL_18_AGENT_FRAMEWORK defines **every role needed to run an AI-native platform business**. Each role has:
- Role identity (Human/AI/Hybrid)
- Mission and accountability
- Domain stakeholder map
- Produce/consume matrix
- Decision authority
- Interface contracts
- Tool stack

## The 40 Canonical Roles

### Executive Leadership (2)
1. **Founder / CEO** — Vision, capital allocation, existential risk
2. **Executive Lead** — Operational execution

### Product & Strategy (5)
3. **Product Director** — Product vision and roadmap
4. **Product Manager** — Feature delivery
5. **Product Designer** — UX/UI design
6. **User/Customer Research Lead** — User insights
7. **Analytics & Insights Lead** — Data analysis

### Platform Engineering (10)
8. **Platform Engineering Lead** — Technical leadership
9. **Backend Engineer** — Server-side systems
10. **Frontend Engineer** — Client-side interfaces
11. **Data Engineer** — Data pipelines
12. **AI/ML Engineer** — ML models and AI systems
13. **DevOps/CI-CD Engineer** — Deployment automation
14. **Site Reliability Engineer (SRE)** — System reliability
15. **Security Engineer** — Security implementation
16. **Infrastructure/Cloud Architect** — Cloud architecture
17. **Technical Program Manager (TPM)** — Technical coordination
18. **Solutions/Implementation Engineer** — Customer implementation

### Knowledge & Automation (3)
19. **Knowledge Architect/Extraction Lead** — Knowledge systems
20. **Automation Engineer** — Process automation
21. **AI Systems/Orchestration Engineer** — Agent orchestration

### Go-To-Market (5)
22. **Marketing Lead** — Marketing strategy
23. **Growth/Performance Marketer** — Growth execution
24. **Sales Lead** — Sales strategy
25. **Customer Success Lead** — Customer retention
26. **Content/Editorial Lead** — Content creation

### Operations & Delivery (4)
27. **Operations Lead** — Operational efficiency
28. **Delivery Manager** — Project delivery
29. **QA/Quality Engineer** — Quality assurance
30. **Support/Incident Response Lead** — Support operations

### Risk & Sustainability (7)
31. **Finance Lead/CFO** — Financial management
32. **Revenue Operations (RevOps) Lead** — Revenue optimization
33. **Legal/Compliance Lead** — Legal compliance
34. **Privacy & Data Protection Officer (DPO)** — Data privacy
35. **Risk & Sustainability Lead** — Risk management
36. **People Operations Lead** — HR operations
37. **Talent/Hiring Lead** — Recruitment

### Partnerships & Business Development (3)
38. **Partnerships Lead** — Strategic partnerships
39. **Business Development Lead** — Business growth
40. **RevOps/Commercial Operations Lead** — Commercial ops

## Role Definition Schema

```yaml
role:
  identity:
    name: "Role Name"
    type: Human | AI | Hybrid
    class: Executive | Manager | IC | Agent
    authority_level: Override | Approve | Recommend | Execute
    temporal_mode: Continuous | Triggered | Periodic
  
  intent:
    mission: "One-line purpose"
    primary_accountability: "What they own"
    success_definition: "How success is measured"
  
  stakeholder_map:
    primary: [domain_ids]     # Deep involvement
    secondary: [domain_ids]   # Regular interaction
    aware: [domain_ids]       # Informed only
  
  produce_consume:
    produces:
      - output → recipient
    consumes:
      - input ← source
  
  decision_authority:
    unilateral: [decisions]   # Can decide alone
    escalated: [decisions]    # Need approval
    veto: [decisions]         # Can block
    constraints: [limitations]
  
  interface_contracts:
    - role_a → role_b (data flow)
  
  perspective:
    optimises_for: [priorities]
    deprioritises: [tradeoffs]
    blind_spots: [weaknesses]
    detects_early: [signals]
  
  operational_modes:
    normal: "Standard operation"
    crisis: "Emergency mode"
    scale_up: "Growth mode"
    degraded: "Reduced capacity"
  
  tooling:
    access: [systems]
    permissions: [levels]
```

## Team Structures (11 teams)

| Team | Roles | Focus |
|------|-------|-------|
| Executive Leadership | 1-2 | Direction, decisions |
| Product & Strategy | 3-7 | Product vision |
| Platform Engineering | 8-18 | Technical build |
| Knowledge & Automation | 19-21 | AI/automation |
| Go-To-Market | 22-26 | Growth, sales |
| Operations & Delivery | 27-30 | Execution |
| Risk & Sustainability | 31-37 | Compliance, finance |
| Partnerships | 38-40 | Business dev |

## Skill Stack Schema

```yaml
skill_stack:
  role: "Role Name"
  intent: "Plain English mission"
  
  core_stack:
    category_1:
      real_tools:
        - Tool Name — purpose
    category_2:
      real_tools:
        - Tool Name — purpose
  
  agent_glue:
    skills_md: "Role-safe skills"
    integrations: [APIs]
```

---

# SECTION 3: INDEX

## 00_CANON/ (1 file)

| File | Purpose |
|------|---------|
| all_roles_canonical_list_40.md | Master role index |

## 01_ROLES/ (40 files)

**Executive:** role_founder_ceo.md, role_executive_lead.md

**Product:** role_product_director.md, role_product_designer.md, role_user_customer_research_lead.md, role_analytics_insights_lead.md

**Engineering:** role_platform_engineering_lead.md, role_backend_engineer.md, role_frontend_engineer.md, role_data_engineer.md, role_ai_ml_engineer.md, role_dev_ops_ci_cd_engineer.md, role_site_reliability_engineer_sre.md, role_security_engineer.md, role_infrastructure_cloud_architect.md, role_technical_program_manager_tpm.md, role_solutions_implementation_engineer.md

**Knowledge:** role_extraction_agent.md, role_automation_orchestrator_agent.md

**GTM:** role_marketing_director.md, role_sales_lead.md, role_customer_support_success_lead.md, role_content_editorial_lead.md

**Operations:** role_operations_manager.md, role_qa_testing_lead.md

**Risk:** role_finance_lead_cfo.md, role_revenue_operations_rev_ops_lead.md, role_legal_compliance_lead.md, role_privacy_data_protection_officer_dpo.md

**And more...**

## 02_SKILL_STACKS/ (40 files)

Each role has a corresponding `_concrete_skill_stack.md` file.

## 03_TEAM_STRUCTURES/ (11 files)

| File | Team |
|------|------|
| team_executive_leadership.md | Leadership |
| team_product_strategy.md | Product |
| team_platform_engineering.md | Engineering |
| team_knowledge_automation.md | Knowledge/AI |
| team_go_to_market_gtm.md | GTM |
| team_operations_delivery.md | Operations |
| team_risk_sustainability.md | Risk |
| team_partnerships_business_development.md | Partnerships |
| team_talent_people_operations.md | People |
| team_internal_agent_roles.md | AI Agents |
| team_folders_file_placement_map.md | File routing |

---

# SECTION 4: ROUTING RULES

## Inbound
```
Keywords: role, agent, team, skill stack, organizational,
          CEO, engineer, lead, manager, orchestration
→ PIL_18_AGENT_FRAMEWORK
```

## Outbound
| To | Content |
|----|---------|
| PIL_10_WORKING_PRACTICES | Role-based sessions |
| PIL_15_ENTERPRISE_OS | System architecture |
| All pillars | Role ownership mapping |

## Cross-References
- All pillars reference roles for ownership
- PIL_10_WORKING_PRACTICES → Role-based workflows
- PIL_15_ENTERPRISE_OS → System organization

---

# SECTION 5: CANON STATUS

| Status | Count | Notes |
|--------|-------|-------|
| ✅ Canon | 1 | Master index |
| ✅ Roles | 40 | Complete definitions |
| ✅ Skill Stacks | 40 | Tool requirements |
| ✅ Teams | 11 | Team structures |
| Archive | ~2 | Duplicate DPO files |

---

# SECTION 6: KEY FRAMEWORKS

## Role Authority Levels

```
OVERRIDE   → Can override any decision (CEO only)
APPROVE    → Final approval authority
RECOMMEND  → Provide recommendations
EXECUTE    → Carry out decisions
```

## Role Types

```
HUMAN     → Requires human judgment
AI        → Can be fully automated
HYBRID    → Human oversight + AI execution
```

## Team → Role Mapping

```
EXECUTIVE (2 roles)
├── Founder/CEO
└── Executive Lead

PRODUCT (5 roles)
├── Product Director
├── Product Manager
├── Product Designer
├── Research Lead
└── Analytics Lead

ENGINEERING (10 roles)
├── Engineering Lead
├── Backend/Frontend Engineers
├── Data/AI Engineers
├── DevOps/SRE
├── Security/Infrastructure
└── TPM/Solutions

KNOWLEDGE (3 roles)
├── Knowledge Architect
├── Automation Engineer
└── Orchestration Engineer

GTM (5 roles)
├── Marketing Lead
├── Growth Marketer
├── Sales Lead
├── Customer Success
└── Content Lead

OPERATIONS (4 roles)
├── Operations Lead
├── Delivery Manager
├── QA Lead
└── Support Lead

RISK (7 roles)
├── Finance/CFO
├── RevOps
├── Legal
├── DPO
├── Risk Lead
└── People/Talent

PARTNERSHIPS (3 roles)
├── Partnerships Lead
├── Business Dev
└── Commercial Ops
```

---

**END OF PIL_18_AGENT_FRAMEWORK DOCUMENTATION**
