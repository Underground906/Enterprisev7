# PIL_02_BRANDING — COMPLETE DOCUMENTATION SET

**Files:** 13 threads + 93 artifacts = **106 total**
**Date:** 2026-02-03

---

# SECTION 1: README

**Pillar ID:** PIL_02  
**Domain:** Foundation Core  
**Status:** Active (5-phase system complete)

## Purpose

The Branding pillar contains a **comprehensive 5-phase brand development system** covering discovery, strategy, social identity, visual identity, and operational management. Includes database schemas, question banks, workflow procedures, and platform-specific templates.

## Key Assets

| Asset Type | Count | Description |
|------------|-------|-------------|
| Phase Frameworks | 5 | Complete brand development journey |
| Question Banks | 5 | Discovery questions per phase |
| Brand Run Guides | 5 | Step-by-step procedures |
| Examples | 5 | Real-world demonstrations |
| JSON Schemas | 20+ | LLM/database-ready data |
| Visual Templates | 10+ | Social media, video, print specs |
| SQL Schemas | 2 | Database table definitions |

## Folder Structure

```
PIL_02_BRANDING/
├── 00_CANON/
│   ├── brand_system_source_of_truth.markdown
│   ├── brand_identity_system.md
│   └── comprehensive-brand-taxonomy.sql
├── 01_PHASE1_DISCOVERY/
├── 02_PHASE2_STRATEGY/
├── 03_PHASE3_SOCIAL_IDENTITY/
├── 04_PHASE4_VISUAL_IDENTITY/
├── 05_PHASE5_MANAGEMENT/
├── 06_SCHEMAS/
├── 07_TEMPLATES/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

# SECTION 2: CONTEXT DOC (For AI/Agents)

## System Overview

PIL_02_BRANDING provides a **complete brand development system** organized into 5 sequential phases. Each phase has frameworks, procedures, question banks, examples, and JSON schemas for automation.

## The 5-Phase Brand System

### PHASE 1: Discovery & Research

```
FRAMEWORKS:
├── Intake & Scope — Business model, niche, constraints
├── Objectives & Vision — 1/3/5 year goals, success metrics
├── Market & Competitors — Direct/indirect, category norms, white space
├── Audience & Personas — Demographics, psychographics, behaviors
├── Pain Points & Unmet Needs — Friction, emotions, workarounds
└── Synthesis Pass — Insights summary, hypotheses for Phase 2

PROCEDURES:
1. Confirm business model, niche, constraints, target markets
2. Collect prior brand docs, research, assets
3. Define 1, 3, 5+ year objectives and success metrics
4. Document constraints/risks, required milestones
5. Identify competitors, category norms, pricing bands
6. Map trends, underserved segments, white space
7. Build demographic/psychographic/behavioral patterns
8. Identify preferred channels and language cues
9. Document task friction, emotional needs, workarounds
10. Describe "ideal experience" gap
11. Summarize insights, list hypotheses
12. Flag unknowns needing validation
```

### PHASE 2: Brand Strategy & Copy

```
FRAMEWORKS:
├── Messaging Pillars Framework
├── Tagline Creation Process (Keyword + Emotion + Promise)
├── Funnel-Stage Messaging Map
└── Direct Response Copy Integration Model

PROCEDURES:
1. Extract high-value keywords & LSI terms
2. Build messaging pillars using competitive gaps
3. Test tagline variations for memorability
4. Develop channel-specific adaptations
5. Align copywriting frameworks with branding
```

### PHASE 3: Social Media Brand Identity

```
FRAMEWORKS:
├── Platform Persona Mapping
├── Content Pillar Model
├── Hashtag Research & Categorization
└── Engagement Protocol Framework

PROCEDURES:
1. Select 2-4 primary platforms based on audience
2. Create platform-specific style and tone guides
3. Define content categories & frequency
4. Implement hashtag research & monitoring
5. Document engagement rules & escalation paths
```

### PHASE 4: Visual Brand Identity

```
FRAMEWORKS:
├── Color System Framework — HEX, RGB, CMYK, usage rules
├── Typography Hierarchy System — Heading, body, caption styles
├── Logo Application Matrix — Placement, scaling, clear-space
├── Responsive Visual Identity — Desktop, mobile, print, social
├── Imagery & Iconography Style Guide
├── Accessibility-First Visual Design — WCAG compliance
├── Motion Design Framework — Animation speed, easing, transitions
└── Data Visualization Standards — Charts, labeling, color coding

PROCEDURES:
1. Define brand color palette with full codes
2. Select and approve typography styles
3. Create logo usage guidelines, export formats
4. Build visual identity kit
5. Establish multi-medium adaptation rules
6. Document accessibility requirements
7. Define image and illustration preferences
8. Develop motion/animation style guides
9. Create chart and infographic templates
10. Specify file formats and resolutions
11. Train team on visual identity
12. Implement review/approval process
13. Create campaign variations
14. Maintain centralized asset library
```

### PHASE 5: Operational Brand Management

```
FRAMEWORKS:
├── Brand Governance Model
├── Asset Approval Workflow
└── Audit & Compliance Checklist

PROCEDURES:
1. Assign brand governance roles
2. Train teams on brand usage
3. Set quarterly brand audits
4. Maintain central guideline repository
```

## Database Schema

```sql
-- Core Tables
CREATE TABLE QuestionBank (
    question_id UUID PRIMARY KEY,
    phase VARCHAR(50),
    section VARCHAR(50),
    question TEXT,
    priority VARCHAR(10)
);

CREATE TABLE BrandDiscovery (
    project_id UUID PRIMARY KEY,
    objectives JSONB,
    market_competitors JSONB,
    audience_personas JSONB,
    pains_unmet_needs JSONB,
    synthesis JSONB
);

CREATE TABLE BrandCore (
    brand_id UUID PRIMARY KEY,
    project_id UUID REFERENCES BrandDiscovery(project_id),
    mission TEXT,
    vision TEXT,
    values JSONB,
    positioning JSONB
);

CREATE TABLE Messaging (
    messaging_id UUID PRIMARY KEY,
    brand_id UUID REFERENCES BrandCore(brand_id),
    pillars JSONB,
    taglines JSONB,
    voice_guidelines JSONB
);

CREATE TABLE SocialIdentity (
    social_id UUID PRIMARY KEY,
    brand_id UUID REFERENCES BrandCore(brand_id),
    platform_profiles JSONB,
    content_pillars JSONB,
    hashtag_strategy JSONB
);

CREATE TABLE VisualIdentity (
    visual_id UUID PRIMARY KEY,
    brand_id UUID REFERENCES BrandCore(brand_id),
    color_palette JSONB,
    typography JSONB,
    logo_specs JSONB,
    imagery_style JSONB
);
```

## Social Media Specifications

```
PROFILE PICTURE LOGOS:
├── Square format: 1080x1080px (high-res)
├── Circular crop: 800x800px safe zone
├── Simplified icon version
├── High contrast version
└── Monogram version

PLATFORM SIZES:
├── YouTube Channel Art: 2560x1440px
├── Facebook Cover: 1200x630px
├── Instagram Profile: 320x320px
├── Twitter Header: 1500x500px
├── LinkedIn Banner: 1192x220px
├── TikTok Profile: 200x200px
└── Pinterest Profile: 165x165px

VIDEO ELEMENTS:
├── Corner watermark: 200x200px PNG
├── Intro animation: 3-5 seconds
├── Outro logo: Static or animated
└── Lower third: 150x150px
```

## JSON Schema Assets

| Schema | Purpose |
|--------|---------|
| color_palette.json | Brand colors with codes |
| typography_pairings.json | Font combinations |
| voice_guidelines.json | Tone and style |
| messaging_pillars.json | Core messages |
| social_templates.json | Platform templates |
| visual_identity_guide.json | Visual specs |
| tagline_generator.json | Tagline patterns |
| persona_autogen.json | Audience generation |
| hashtag_generator.json | Hashtag strategies |
| positioning.json | Brand positioning |

---

# SECTION 3: INDEX

## 00_CANON/ (5 files)

| File | Purpose |
|------|---------|
| brand_system_source_of_truth.markdown | Master reference (41 files) |
| brand_identity_system.md | Social/digital brand kit |
| comprehensive-brand-taxonomy.sql | Full database schema |
| brand-identity-guide-template.md | Guide template |
| system_template_prompt.markdown | LLM prompt template |

## Phase Files (by phase)

**Phase 1 - Discovery:**
- phase1_discovery.markdown, phase1_questions.json/markdown, phase1_brand_run.markdown

**Phase 2 - Strategy:**
- phase2_strategy.markdown, phase2_questions.json/markdown, phase2_brand_run.markdown, phase2_examples.markdown

**Phase 3 - Social Identity:**
- phase3_identity.markdown, phase3_questions.json/markdown, phase3_brand_run.markdown, phase3_examples.markdown

**Phase 4 - Visual Identity:**
- phase4_visual_identity.markdown, phase4_questions.json/markdown, phase4_brand_run.markdown, phase4_examples.markdown

**Phase 5 - Management:**
- phase5_management.markdown, phase5_questions.json/markdown, phase5_brand_run.markdown, phase5_examples.markdown, phase5_management_workflow.json

## JSON Schemas (20+ files)

color_palette.json, typography_pairings.json, voice_guidelines.json, messaging_pillars.json, social_templates.json, visual_identity_guide.json, tagline_generator.json, persona_autogen.json, hashtag_generator.json, positioning.json, ad_formats.json, animation_style.json, video_graphics.json, infographic_style.json, content_plan.json, analytics_dashboard.json, governance_setup.json, training_program.json, accessibility_improvements.json, performance_dashboard.json, discovery_interview.json, competitor_synthesis.json, pain_map.json

---

# SECTION 4: ROUTING RULES

## Inbound
```
Keywords: brand, branding, identity, logo, color palette,
          typography, visual identity, brand voice, tagline,
          brand guidelines, brand strategy, brand management
→ PIL_02_BRANDING
```

## Outbound
| To | Content |
|----|---------|
| PIL_03_COPY | Brand voice for copy |
| PIL_05_GRAPHIC_DESIGN | Visual specifications |
| PIL_07_UI_LIBRARY | Brand colors/fonts for UI |
| All pillars | Brand consistency |

## Cross-References
- PIL_03_COPY → Uses brand voice guidelines
- PIL_05_GRAPHIC_DESIGN → Uses visual identity specs
- PIL_07_UI_LIBRARY → Uses brand colors/typography
- PIL_04_CONTENT → Uses brand messaging pillars

---

# SECTION 5: CANON STATUS

| Status | Count | Notes |
|--------|-------|-------|
| ✅ Canon | 5 | Core system files |
| ✅ Phase Docs | 25+ | 5 per phase |
| ✅ JSON Schemas | 20+ | Automation-ready |
| Keep threads | 13 | Source discussions |

---

# SECTION 6: KEY FRAMEWORKS

## Brand Development Journey

```
PHASE 1: DISCOVERY (Research)
    ↓ Outputs: Insights, Personas, Hypotheses
PHASE 2: STRATEGY (Positioning)
    ↓ Outputs: Messaging Pillars, Taglines, Voice
PHASE 3: SOCIAL IDENTITY (Platforms)
    ↓ Outputs: Platform Guides, Content Pillars
PHASE 4: VISUAL IDENTITY (Design)
    ↓ Outputs: Colors, Typography, Logo, Templates
PHASE 5: MANAGEMENT (Operations)
    ↓ Outputs: Governance, Audits, Training
```

## Tagline Creation Formula

```
KEYWORD + EMOTION + PROMISE

Examples:
- [Speed] + [Confidence] + [Results] = "Fast. Confident. Winning."
- [Simple] + [Relief] + [Freedom] = "Simplify. Breathe. Live."
```

## Color System Structure

```
PRIMARY COLORS (2-3)
├── Main brand color
├── Secondary accent
└── Neutral base

FUNCTIONAL COLORS
├── Success (green)
├── Warning (amber)
├── Error (red)
├── Info (blue)
└── Disabled (gray)

SPECIFICATIONS
├── HEX: #RRGGBB
├── RGB: rgb(R, G, B)
├── CMYK: C% M% Y% K%
└── Usage rules per context
```

## Typography Hierarchy

```
DISPLAY: Hero headlines (48-72px)
H1: Page titles (32-40px)
H2: Section headers (24-28px)
H3: Subsections (20-22px)
BODY: Main content (16-18px)
CAPTION: Secondary text (12-14px)
UI: Interface elements (14-16px)
```

---

**END OF PIL_02_BRANDING DOCUMENTATION**
