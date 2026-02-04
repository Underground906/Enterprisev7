# ENTERPRISE_OS V7.0 — COMPLETE STRUCTURE

**Version:** 7.0 (Revised)  
**Date:** 2026-02-02  
**Purpose:** Thread debt escape + operational system

---

## TOP-LEVEL (8 COMPONENTS)

```
ENTERPRISE_OS_V7/
├── 00_SYSTEM_ROOT/           # Governance + context docs
├── 01_NAVIGATION_CENTRE/     # Goals, state, priorities
├── 02_COMMAND_DECK/          # Daily execution, sessions
├── 03_CORE_ENGINE/           # Infrastructure, routing, scripts
├── 04_KNOWLEDGE_LIBRARY/     # Simplified: ongoing threads only
├── 05_TEMPLATE_HUB/          # Reusable scaffolds
├── 06_DOMAIN_PILLARS/        # 20 domains (from routing docs + new)
├── 07_BUILD_FACTORY/         # Platform builds only
└── 08_OPERATIONS/            # Post-launch
```

---

## 00_SYSTEM_ROOT

```
00_SYSTEM_ROOT/
├── MASTER_CONTEXT.md           # Universal AI context
├── SESSION_ROUTER.md           # Where new chats go
├── ROUTING_RULES.md            # Routing decision logic
├── AGENT_REGISTRY.md           # All defined agents
├── NAMING_CONVENTIONS.md
└── VERSION_HISTORY/
```

---

## 01_NAVIGATION_CENTRE

```
01_NAVIGATION_CENTRE/
├── 00_README.md
├── ACTIVE_GOALS/
│   └── GOAL_[Name]/
│       ├── 01_Alignment/
│       ├── 02_Awareness/
│       ├── 03_Accountabilities/
│       ├── 04_Activities/
│       ├── 05_Assets/
│       ├── 06_State/
│       ├── 07_Decisions/
│       ├── 08_Learning/
│       ├── 09_Iterations/
│       └── 10_AI_Dialogue/
├── GOAL_INTAKE/
├── STATE_SNAPSHOTS/
└── 90_ARCHIVE/
```

---

## 02_COMMAND_DECK

```
02_COMMAND_DECK/
├── 00_README.md
├── ACTIVE_SESSIONS/
│   └── [YYYY-MM-DD]/
│       ├── session_log.md
│       └── decisions.md
├── AGENT_WORKSPACE/
│   ├── Research_Agent/
│   ├── Copy_Agent/
│   ├── Code_Agent/
│   ├── Design_Agent/
│   ├── Validator_Agent/
│   └── Orchestrator_Agent/
├── TASK_QUEUE/
├── DASHBOARDS/
└── 90_ARCHIVE/
```

---

## 03_CORE_ENGINE

```
03_CORE_ENGINE/
├── 00_README.md
├── INDICES/
│   ├── THREAD_MASTER_INDEX.json
│   ├── DOMAIN_REGISTRY.json
│   ├── ARTIFACT_INDEX.json
│   └── ROUTING_LOG.json
├── ROUTING_ENGINE/
│   ├── routing_rules.py
│   ├── intake_processor.py
│   └── routing_logs/
├── SCRIPTS/
│   ├── thread_finder.py
│   ├── batch_mover.py
│   ├── thread_router.py
│   └── context_generator.py
├── SCHEMAS/
├── CONFIG/
└── 90_ARCHIVE/
```

---

## 04_KNOWLEDGE_LIBRARY (SIMPLIFIED)

```
04_KNOWLEDGE_LIBRARY/
├── 00_README.md
├── ONGOING/
│   ├── By_Month/
│   │   └── 2026-02/
│   ├── By_Domain/
│   └── UNROUTED/
├── EXTRACTION_PIPELINE/
│   ├── RAW_INTAKE/
│   ├── PROCESSING/
│   └── OUTPUTS/
├── RAG_BUNDLES/
├── _MASTER_INDICES/
└── 90_ARCHIVE/
```

---

## 05_TEMPLATE_HUB

```
05_TEMPLATE_HUB/
├── 00_README.md
├── DOCUMENT_TEMPLATES/
├── CODE_TEMPLATES/
├── PRD_TEMPLATES/
├── SOP_TEMPLATES/
├── WORKFLOW_TEMPLATES/
├── PROMPT_TEMPLATES/
├── AGENT_TEMPLATES/
│   ├── builder_agent.md
│   ├── validator_agent.md
│   └── orchestrator_agent.md
├── CONTEXT_TEMPLATES/
└── 90_ARCHIVE/
```

---

## 06_DOMAIN_PILLARS — 20 DOMAINS

Each pillar follows its routing doc structure. Below is the complete list with internal structures.

---

### PIL_01_AVATARS
*Source: brand_avatar_bucket_structure_and_routing.md*

```
PIL_01_AVATARS/
├── 00_CANON/
│   └── AVATAR_SYSTEM_CANON.md
├── 01_INPUT/
│   └── AVATAR_INPUT_WIZARD.md
├── 02_FRAMEWORKS/
│   ├── psychographic_profile_template.md
│   └── decision_logic_model.md
├── 03_KEYWORD_MAPPING/
│   └── avatar_keyword_overlay.md
├── 04_OUTPUTS/
│   ├── CONSUMER/
│   └── COMMERCIAL/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_02_BRANDING
*Source: brand_avatar_bucket_structure_and_routing.md*

```
PIL_02_BRANDING/
├── 00_CANON/
│   └── BRAND_SYSTEM_CANON.md
├── 01_INPUT/
│   └── BRAND_INPUT_DISCOVERY_WIZARD.md
├── 02_RULES/
│   ├── BRAND_TO_COPY_RULES.md
│   └── BRAND_TO_VISUAL_RULES.md
├── 03_STRATEGY/
│   ├── brand_purpose_context.md
│   └── branding_process_notes.md
├── 04_VISUAL_IDENTITY/
│   ├── color_palette.json
│   ├── animation_style.json
│   └── infographic_style.json
├── 05_COPY_INTERFACE/
│   ├── brand_copy_principles.md
│   ├── brand_copy_schema.sql
│   └── brand_taxonomy.sql
├── 90_PROCESS_RUNS/
├── 01_threads/
├── 02_artifacts/
└── 99_ARCHIVE/
```

---

### PIL_03_COPY
*Source: copy_system_folder_structure_and_routing.md*

```
PIL_03_COPY/
├── 00_CANON/
│   └── (read-only governing rules)
├── 01_INPUT/
│   └── (wizards / briefs)
├── 02_TAXONOMY_SCHEMA/
│   └── (classification, funnels, SQL)
├── 03_FRAMEWORKS/
│   └── (copy behavior frameworks)
├── 04_FORMULAS_PATTERNS/
│   └── (named formulas & patterns)
├── 05_AWARENESS_JOURNEY/
│   └── (awareness, journeys, channels)
├── 06_OFFERS_PERSUASION/
│   └── (offer structures & devices)
├── 07_RHETORIC_STYLE/
│   └── (rhetoric / charm systems)
├── 08_SLOT_SCHEMAS/
│   └── (copy slot definitions)
├── 09_OUTPUTS/
│   └── (generated copy ONLY)
├── 01_threads/
├── 02_artifacts/
└── 99_ARCHIVE/
```

---

### PIL_04_CONTENT
*Source: content_system_folder_structure_and_routing.md*

```
PIL_04_CONTENT/
├── 00_CANON/
│   ├── content_system_prd.md
│   └── CONTENT_SYSTEM_CONTEXT.md
├── 01_RESEARCH/
│   ├── market/
│   ├── competitors/
│   └── audience/
├── 02_STRATEGY/
│   ├── pillars/
│   ├── positioning/
│   └── messaging_logic/
├── 03_TOPICS/
│   ├── topic_maps/
│   └── opportunity_lists/
├── 04_CONTENT_PLANS/
│   ├── editorial_calendars/
│   ├── publishing_sequences/
│   └── process_threads/
├── 05_DRAFTS/
│   ├── articles/
│   ├── posts/
│   └── reports/
├── 06_DISTRIBUTION/
│   ├── channel_rules/
│   └── repurposing_maps/
├── 07_OUTPUTS/
│   ├── published/
│   └── syndicated/
├── 01_threads/
├── 02_artifacts/
└── 99_ARCHIVE/
```

---

### PIL_05_GRAPHICS
*Source: graphics_library_context_and_routing.md*

```
PIL_05_GRAPHICS/
├── 00_CANON/
│   ├── README.md
│   ├── taxonomy_reference.md
│   └── routing_manifest.json
├── 01_hero_and_banner_systems/
│   ├── full_bleed_photography/
│   ├── gradients_duotone_glass/
│   ├── abstract_geometric/
│   ├── illustration_based/
│   ├── video_and_motion_heroes/
│   └── parallax_interactive/
├── 02_iconography/
│   ├── line_icons/
│   ├── filled_icons/
│   ├── duotone_and_gradient/
│   ├── 3d_icons/
│   ├── animated_lottie_icons/
│   └── category_sets/
├── 03_illustration_systems/
│   ├── flat_and_minimal/
│   ├── isometric_and_3d/
│   ├── hand_drawn_and_whimsical/
│   ├── characters_and_scenes/
│   └── conceptual_and_abstract/
├── 04_photography_library/
│   ├── lifestyle/
│   ├── product/
│   ├── editorial/
│   ├── corporate_and_tech/
│   ├── environment_and_space/
│   └── subject_based_sets/
├── 05_motion_and_lottie/
│   ├── loading_and_progress/
│   ├── success_error_states/
│   ├── ui_micro_interactions/
│   ├── data_visualisation_motion/
│   └── ambient_backgrounds/
├── 06_mockups_and_frames/
│   ├── device_mockups/
│   ├── browser_and_app_frames/
│   ├── print_and_physical/
│   └── social_media_context/
├── 07_product_and_feature_visuals/
│   ├── saas_and_tech/
│   ├── ecommerce/
│   ├── before_after/
│   ├── explainer_visuals/
│   └── comparison_and_proof/
├── 08_data_visualisation/
│   ├── charts_and_graphs/
│   ├── infographics/
│   ├── dashboards_visuals/
│   └── maps_and_networks/
├── 09_ui_visual_elements/
│   ├── cards_and_containers/
│   ├── dividers_and_patterns/
│   ├── background_textures/
│   └── visual_utilities/
├── 10_effects_and_post_processing/
│   ├── color_grading_luts/
│   ├── overlays_and_textures/
│   ├── shadows_and_depth/
│   ├── distortions_and_glitch/
│   └── artistic_filters/
├── 11_brand_visual_components/
│   ├── logos_and_marks/
│   ├── typography_assets/
│   ├── color_palettes/
│   └── graphic_patterns/
├── 01_threads/
├── 02_artifacts/
└── 99_ARCHIVE/
```

---

### PIL_06_VIDEO
*Source: video_library_full_routing_all_files.md*

```
PIL_06_VIDEO/
├── 00_CANON/
│   └── VIDEO_LIBRARY_CONTEXT.md
├── 01_PROCESS_LOGIC/
│   └── (threads as process reference)
├── 02_SOURCE_CONTENT/
│   ├── research/
│   ├── audience/
│   └── strategy/
├── 03_VIDEO_SCRIPTS/
│   └── (generated later)
├── 04_PLATFORM_FORMATS/
│   └── (rules per platform)
├── 05_OUTPUTS/
│   └── (rendered videos)
├── 01_threads/
├── 02_artifacts/
└── 99_ARCHIVE/
```

---

### PIL_07_UI_LIBRARY
*Source: ui_library_artifact_mapping_from_zip.md*

```
PIL_07_UI_LIBRARY/
├── 00_CANON/
│   └── (system context)
├── 01_TEMPLATES/
│   ├── marketing/
│   ├── dashboards/
│   └── apps/
├── 02_BLOCKS/
│   ├── heroes/
│   ├── navigation/
│   ├── content_sections/
│   ├── forms/
│   ├── tables_lists/
│   └── footers/
├── 03_COMPONENTS/
│   ├── buttons/
│   ├── inputs/
│   ├── cards/
│   ├── modals/
│   ├── alerts/
│   └── icons/
├── 04_SLOTS/
│   ├── copy_slots/
│   ├── graphic_slots/
│   └── interaction_slots/
├── 05_LAYOUTS/
│   ├── grid_systems/
│   ├── spacing_rules/
│   ├── breakpoints/
│   └── responsive_patterns/
├── 06_STYLES/
│   ├── typography/
│   ├── color/
│   ├── elevation/
│   ├── motion/
│   └── effects/
├── 07_METADATA/
│   ├── template_manifests/
│   ├── block_manifests/
│   ├── component_manifests/
│   └── slot_manifests/
├── 08_GENERATION/
│   ├── instantiation_rules/
│   ├── variant_logic/
│   └── assembly_playbooks/
├── 09_OUTPUTS/
├── 01_threads/
├── 02_artifacts/
└── 99_ARCHIVE/
```

---

### PIL_08_KNOWLEDGE_INGESTION
*Source: knowledge_ingestion_folder_structure_routing.md*

```
PIL_08_KNOWLEDGE_INGESTION/
├── 00_READ_ME_FIRST/
│   └── system_overview.md
├── 01_INPUTS/
│   ├── threads_raw/
│   └── external_docs/
├── 02_INVENTORIES/
│   ├── thread_inventory.md
│   └── artifact_inventory.md
├── 03_PIPELINES/
│   ├── ai_chats.md
│   ├── monitoring.md
│   └── documents.md
├── 04_CANON_RULES/
│   └── canonisation_rules.md
├── 05_DISTRIBUTION/
│   └── routing_logic.md
├── 06_GOVERNANCE/
│   └── guardrails.md
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_09_ROLES_SKILLS
*Source: roles_and_skills_folder_structure_routing.md*

```
PIL_09_ROLES_SKILLS/
├── 00_READ_ME_FIRST/
│   └── system_overview.md
├── 01_ARTIFACT_INVENTORY/
│   └── artifact_inventory.md
├── 02_ROLE_MODEL/
│   └── role_definition_schema.md
├── 03_SKILL_MODEL/
│   └── skill_definition_schema.md
├── 04_AI_AGENTS/
│   └── agent_behaviour_rules.md
├── 05_GOVERNANCE/
│   └── drift_control.md
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_10_WORKING_PRACTICES
*Source: working_practices_folder_structure_routing.md*

```
PIL_10_WORKING_PRACTICES/
├── 00_READ_ME_FIRST/
│   └── system_overview.md
├── 01_SESSION_DESIGN/
│   └── session_structure.md
├── 02_PACING_RULES/
│   └── limits_and_thresholds.md
├── 03_RECOVERY/
│   └── recovery_loops.md
├── 04_AI_GUIDANCE/
│   └── ai_rules.md
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_11_BUILD_STORY
*Source: build_story_folder_structure_routing.md*

```
PIL_11_BUILD_STORY/
├── 00_READ_ME_FIRST/
│   └── intent_and_scope.md
├── 01_SOURCES/
│   ├── threads/
│   └── artifacts/
├── 02_NARRATIVE_ARCHITECTURE/
│   └── canonical_phases.md
├── 03_OUTPUTS/
│   ├── book_outlines/
│   ├── brand_story/
│   └── launch_copy/
├── 04_GOVERNANCE/
│   └── usage_rules.md
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_12_KEYWORDS
*New domain*

```
PIL_12_KEYWORDS/
├── 00_CANON/
│   └── keyword_system_context.md
├── 01_RESEARCH/
│   ├── seed_keywords/
│   ├── competitor_keywords/
│   └── gap_analysis/
├── 02_LATTICES/
│   ├── by_intent/
│   ├── by_topic/
│   └── by_funnel_stage/
├── 03_PERMUTATIONS/
│   └── generated_variants/
├── 04_MAPPINGS/
│   ├── keyword_to_page/
│   ├── keyword_to_copy/
│   └── keyword_to_avatar/
├── 05_DATABASES/
│   ├── property_keywords.db
│   └── fitness_keywords.db
├── 06_OUTPUTS/
│   └── export_files/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_13_SEO
*New domain*

```
PIL_13_SEO/
├── 00_CANON/
│   └── seo_system_context.md
├── 01_AUDITS/
│   ├── technical_audits/
│   ├── content_audits/
│   └── backlink_audits/
├── 02_ON_PAGE/
│   ├── title_tags/
│   ├── meta_descriptions/
│   ├── schema_markup/
│   └── internal_linking/
├── 03_OFF_PAGE/
│   ├── link_building/
│   └── digital_pr/
├── 04_TECHNICAL/
│   ├── site_speed/
│   ├── crawlability/
│   └── indexation/
├── 05_TRACKING/
│   ├── rank_tracking/
│   └── performance_reports/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_14_NAVIGATION
*New domain - system navigation logic*

```
PIL_14_NAVIGATION/
├── 00_CANON/
│   └── navigation_system_context.md
├── 01_ROUTING_LOGIC/
│   ├── decision_trees/
│   ├── semantic_rules/
│   └── fallback_logic/
├── 02_SESSION_MANAGEMENT/
│   ├── session_start_protocol.md
│   ├── session_end_protocol.md
│   └── context_injection/
├── 03_GOAL_FLOW/
│   ├── goal_to_task/
│   └── task_to_session/
├── 04_CROSS_REFERENCES/
│   ├── domain_links/
│   └── project_links/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_15_ENTERPRISE_OS
*Domain (not project)*

```
PIL_15_ENTERPRISE_OS/
├── 00_CANON/
│   └── enterprise_os_context.md
├── 01_ARCHITECTURE/
│   ├── system_topology/
│   ├── component_boundaries/
│   └── integration_maps/
├── 02_GOVERNANCE/
│   ├── naming_conventions/
│   ├── versioning_rules/
│   └── migration_protocols/
├── 03_SCHEMAS/
│   ├── folder_schemas/
│   ├── file_schemas/
│   └── routing_schemas/
├── 04_DOCUMENTATION/
│   ├── user_guides/
│   ├── system_specs/
│   └── prd_docs/
├── 05_EVOLUTION/
│   ├── version_history/
│   └── roadmap/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_16_CONTENT_GENERATION
*Domain (not project)*

```
PIL_16_CONTENT_GENERATION/
├── 00_CANON/
│   └── content_gen_context.md
├── 01_PIPELINES/
│   ├── article_pipeline/
│   ├── social_pipeline/
│   └── video_script_pipeline/
├── 02_PROMPTS/
│   ├── generation_prompts/
│   ├── editing_prompts/
│   └── qa_prompts/
├── 03_WORKFLOWS/
│   ├── batch_generation/
│   └── single_piece/
├── 04_QUALITY_CONTROL/
│   ├── validation_rules/
│   └── review_checklists/
├── 05_OUTPUTS/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_17_RAG_SYSTEM
*Domain (not project)*

```
PIL_17_RAG_SYSTEM/
├── 00_CANON/
│   └── rag_system_context.md
├── 01_CHUNKING/
│   ├── strategies/
│   └── implementations/
├── 02_EMBEDDING/
│   ├── models/
│   └── configs/
├── 03_INDEXING/
│   ├── vector_stores/
│   └── metadata_schemas/
├── 04_RETRIEVAL/
│   ├── query_logic/
│   └── reranking/
├── 05_INTEGRATION/
│   ├── api_specs/
│   └── client_implementations/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_18_AGENT_FRAMEWORK
*Domain (not project)*

```
PIL_18_AGENT_FRAMEWORK/
├── 00_CANON/
│   └── agent_framework_context.md
├── 01_AGENT_TYPES/
│   ├── builder_agents/
│   ├── validator_agents/
│   ├── orchestrator_agents/
│   └── specialist_agents/
├── 02_TEAM_COMPOSITIONS/
│   ├── standard_teams/
│   └── custom_teams/
├── 03_TASK_SYSTEM/
│   ├── task_schemas/
│   ├── dependency_logic/
│   └── communication_protocols/
├── 04_VALIDATION/
│   ├── self_validation_hooks/
│   └── cross_validation/
├── 05_ORCHESTRATION/
│   ├── orchestration_prompts/
│   └── coordination_rules/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_19_PROPERTY
*Platform domain*

```
PIL_19_PROPERTY/
├── 00_CANON/
│   └── property_domain_context.md
├── 01_MARKET_INTELLIGENCE/
│   ├── london_market/
│   ├── competitors/
│   └── trends/
├── 02_AVATARS/
│   ├── consumer/
│   └── commercial/
├── 03_KEYWORDS/
│   └── property_keywords/
├── 04_CONTENT/
│   ├── magazine/
│   └── guides/
├── 05_DATA/
│   ├── listings/
│   └── analytics/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_20_FITNESS
*Platform domain*

```
PIL_20_FITNESS/
├── 00_CANON/
│   └── fitness_domain_context.md
├── 01_MARKET_INTELLIGENCE/
├── 02_AVATARS/
├── 03_KEYWORDS/
├── 04_CONTENT/
├── 05_PROGRAMS/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_21_MARKET_RESEARCH
*Source: market_research_routing_verbatim.md*

```
PIL_21_MARKET_RESEARCH/
├── 00_CANON/
│   └── MARKET_RESEARCH_SCOPE.md
├── 01_SEGMENTS/
│   ├── consumer/
│   ├── investor/
│   ├── commercial_b2b/
│   └── special_cases/
├── 02_SALES_CONTEXTS/
│   ├── off_market/
│   ├── auctions/
│   ├── probate_estate/
│   ├── distressed_quick_sale/
│   └── luxury/
├── 03_COMPETITION/
├── 04_DATA_SOURCES/
├── 05_STRATEGY_INPUTS/
├── 06_CONTENT_OPPORTUNITIES/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_22_VOICE_TRAINING
*Platform domain*

```
PIL_22_VOICE_TRAINING/
├── 00_CANON/
│   └── voice_training_context.md
├── 01_MARKET_INTELLIGENCE/
├── 02_AVATARS/
├── 03_CONTENT/
├── 04_PROGRAMS/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

### PIL_23_DOG_PLATFORM
*Platform domain*

```
PIL_23_DOG_PLATFORM/
├── 00_CANON/
│   └── dog_platform_context.md
├── 01_MARKET_INTELLIGENCE/
├── 02_AVATARS/
├── 03_CONTENT/
├── 04_DEVELOPMENT/
│   └── sprint_plans/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

## 07_BUILD_FACTORY — Platform Builds Only

```
07_BUILD_FACTORY/
├── 00_README.md
├── PRJ_Property_Connect_London/
│   ├── 01_Strategy/
│   ├── 02_Product/
│   ├── 03_Design/
│   ├── 04_Architecture/
│   ├── 05_Development/
│   ├── 06_Testing/
│   ├── 07_Deployment/
│   ├── 08_Marketing/
│   └── 90_Archive/
├── PRJ_Fitness_Platform/
├── PRJ_Voice_Training/
├── PRJ_Dog_Platform/
└── 90_ARCHIVE/
```

---

## 08_OPERATIONS

```
08_OPERATIONS/
├── 00_README.md
├── FINANCIAL/
├── LEGAL/
├── MARKETING/
├── METRICS/
├── COMMUNITY/
├── LEAD_GEN/
└── 90_ARCHIVE/
```

---

## DOMAIN PILLAR SUMMARY (23 Total)

| # | Pillar | Source |
|---|--------|--------|
| 01 | Avatars | routing doc |
| 02 | Branding | routing doc |
| 03 | Copy | routing doc |
| 04 | Content | routing doc |
| 05 | Graphics | routing doc |
| 06 | Video | routing doc |
| 07 | UI_Library | routing doc |
| 08 | Knowledge_Ingestion | routing doc |
| 09 | Roles_Skills | routing doc |
| 10 | Working_Practices | routing doc |
| 11 | Build_Story | routing doc |
| 12 | Keywords | new |
| 13 | SEO | new |
| 14 | Navigation | new |
| 15 | Enterprise_OS | domain |
| 16 | Content_Generation | domain |
| 17 | RAG_System | domain |
| 18 | Agent_Framework | domain |
| 19 | Property | platform domain |
| 20 | Fitness | platform domain |
| 21 | Market_Research | routing doc |
| 22 | Voice_Training | platform domain |
| 23 | Dog_Platform | platform domain |

---

## THREAD ROUTING RULES

Every thread gets `01_threads/` folder in its primary domain pillar.

```
IF thread is about copywriting → PIL_03_COPY/01_threads/
IF thread is about UI components → PIL_07_UI_LIBRARY/01_threads/
IF thread is about agent orchestration → PIL_18_AGENT_FRAMEWORK/01_threads/
IF thread is about property market → PIL_19_PROPERTY/01_threads/
IF thread spans multiple domains → primary domain + tags
IF thread is unclassifiable → 04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/
```

---

**END OF V7 COMPLETE STRUCTURE**
