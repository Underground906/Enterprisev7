# BOILERPLATE KIT SELECTIONS
> Locked: 2026-02-14 | Based on user-specified kit roles + DB coverage analysis

---

## TIER 1 — PRIMARY BOILERPLATES (Cover ~80% of all pages)

### 1. Brainwave 2.0 — DASHBOARD SHELL / LAYOUT FRAMEWORK
- **Role**: The base layout for ALL dashboard/app screens. Everything else plugs into this.
- **Page-level items**: 99 (media 36, icons 15, other 11, profile 10, navigation 6)
- **Font**: Inter (apps/dashboards)
- **Use for**: Enterprise OS all 8 tabs, Fitness dashboard, PCL agent dashboard
- **Pre-made templates**: 54 items covering auth, content, dashboard, empty states, forms

### 2. Untitled UI Pro — DESIGN SYSTEM / COMPONENT BACKBONE
- **Role**: Most comprehensive design system. Provides tokens, form components, profile components, content blocks that work INSIDE the Brainwave shell.
- **Page-level items**: 741 (forms 114, profile 107, content 100, dashboard 95)
- **Use for**: Every build. Color scales, shadows, typography tokens. Form components, profile pages, content layouts.
- **Dominates**: Auth flows, settings pages, forms, profile screens, content pages

### 3. Fleet Travel — TOP-LEVEL PLATFORM
- **Role**: User said "top level." Best kit for ecommerce/marketplace layouts, card grids, navigation patterns.
- **Page-level items**: 190 (ecommerce 36, forms 27, cards 22, navigation 20, profile 20)
- **Use for**: Marketplace front-ends, trainer directory, property listings, card-based browsing
- **Strength**: Broadest category coverage of any primary kit (18 categories)

### 4. Source Fusion AI — AI FEATURES
- **Role**: User's explicit choice for AI chat/assistant interfaces.
- **Page-level items**: 165 (forms 27, navigation 17, dashboard 16, tables 15, modals 14, content 14)
- **Use for**: Fitness AI workout generator, Enterprise AI assistant panel, any AI chat interface
- **Unique**: Only kit with strong modals (14) + forms (27) combo needed for AI interaction patterns

### 5. Chroma — CORE FONT STACK + PROMO/SaaS STYLE GUIDE
- **Role**: **REPLACES Real Estate SaaS Kit** as core font stack for promo front-end and SaaS. Has pre-header elements, clean black/white/grey aesthetic with few accent colours.
- **Page-level items**: 11 (content 5, hero 3, dashboard 1, forms 1)
- **Font**: DM Sans (same as Real Estate SaaS — need to verify font sizes match)
- **Use for**: ALL promo/SaaS front-end typography and style guide. The design system reference.
- **Note**: If Chroma's design system conflicts with Brainwave, keep Inter for Brainwave/back-end dashboards and DM Sans only for front-end/promo.

### 6. Square Dashboard Desktop — DASHBOARD CONTENT VIEWS (NOT top-level boilerplate)
- **Role**: Heavy data dashboard screens. Nice profile styles. Fills in where Brainwave provides the shell. **Not a top-level boilerplate** — provides specific components, not overall aesthetic.
- **Page-level items**: 144 (dashboard 52, forms 36, auth 15, content 14, tables 10)
- **Use for**: Enterprise data views, analytics, project management, sales views, profile components
- **Unique sections**: Social Media (26), Education (10), Job Search (18), Messaging (14), Project Management (16), Sales Analytics (16), Knowledge Base (14), Login/Sign Up (15)

### 7. Tripie Travel — PLATFORM FRONT-END
- **Role**: User's explicit choice for platform front-end experience.
- **Page-level items**: 47 (content 11, ecommerce 9, forms 7, profile 5, auth 3, tables 3)
- **Use for**: Consumer-facing platform pages, browsing/discovery, content display

### 8. Briefberry — ONBOARDING / PRESELL SEQUENCES (NOT general marketing)
- **Role**: **STRICTLY** for onboarding flows, step-by-step question sequences, and presell vertical presentations (bring people through a sequence → link to site at end).
- **Page-level items**: 57 (content 22, forms 17, auth 6, media 4, cta 2, pricing 2)
- **Use for**: Onboarding intake, presell landing sequences, step-by-step questionnaires
- **NOT for**: General marketing or landing pages

### DEMOTED: Real Estate SaaS Kit → TIER 2
- **Was**: Core font stack / landing typography
- **Now**: Secondary reference. Both Chroma and Real Estate SaaS use DM Sans — need to compare design systems.
- **Page-level items**: 93 (forms 24, dashboard 15, tables 7)
- **Use for**: PCL property-specific forms and dashboards (secondary to Huose Property)

---

## TIER 2 — SPECIALIST KITS (Remaining ~20%)

### 9. Huose Property — PROPERTY DASHBOARD + LEAD CARDS
- **Role**: Lead cards with 4 circular action icons. Property-specific dashboard views.
- **Page-level items**: 168 (dashboard 116!, forms 24, navigation 11)
- **Use for**: PCL agent dashboard, lead management, property-specific views
- **Note**: 116 dashboard items — strongest single-category kit after Stacks

### 10. Zip Formate — NICHE COLORS / PASTELS
- **Role**: Alternative color palette. Pastel tones for differentiation.
- **Page-level items**: 147 (dashboard 46, tables 30, ecommerce 16, forms 14, auth 10)
- **Use for**: Color reference, alternative dashboard themes

### 11. Social Dashboards — FEEDS / VIDEO / SOCIAL
- **Role**: Events cards, video player, feeds.
- **Page-level items**: 26 (dashboard 8, media 5, profile 4, content 3, auth 2)
- **Use for**: Fitness social feed, any social/community features

### 12. Aitentico — COLLAPSED SIDEBAR MENU
- **Role**: Sidebar navigation pattern (collapsed).
- **Page-level items**: 507 total but mostly testimonials (256) + icons (176). The sidebar component itself is what matters.
- **Use for**: Enterprise OS sidebar navigation pattern

### 13. Trakr — COOL SIDEBAR MENU
- **Role**: Alternative sidebar navigation pattern.
- **Page-level items**: 4 (component-level kit, not page-level)
- **Use for**: Optional sidebar style for specific builds

### 14. Strivo — ONBOARDING FLOWS + PROJECT COMPONENTS
- **Role**: Onboarding flow patterns.
- **Page-level items**: 7 (component-level kit)
- **Use for**: Fitness onboarding intake, Enterprise first-run, PCL agent onboarding

### 15. Caresync SAAS — GREEN TONES / DESIGN SYSTEM
- **Role**: Green color palette reference (#0B8C00 alignment).
- **Page-level items**: 12
- **Use for**: Color token reference, green-themed UI elements

### 16. Aimate + Majin — PROMO SITE CONTENDERS
- **Aimate**: 9 page-level items (content 3, CTA, auth, forms, hero, pricing, features)
- **Majin**: 25 page-level items (icons 18, content 2, hero 2, pricing 1)
- **Use for**: Alternative promo/landing page layouts

---

## TIER 3 — DOMAIN-SPECIFIC KITS

### 17. Fitness Pro — FITNESS BUILD
- **Page-level items**: 222 (navigation 110, features 32, content 22, forms 11)
- **Use for**: Exercise library, workout features, fitness content pages

### 18. Finder (Directory & Listings) — MARKETPLACE/DIRECTORY
- **Page-level items**: 158 (tables 25, content 18, profile 12)
- **Use for**: Trainer marketplace directory, expert finder, any listing/search UI

### 19. Adify (Job Finding) — DIRECTORY/LISTINGS
- **Page-level items**: 38 (features 10, content 9, navigation 4, auth 2)
- **Use for**: Secondary directory patterns, job/expert search

### 20. eCommerce UI Kit — E-COMMERCE
- **Page-level items**: 43 (hero 13, dashboard 9, icons 8, ecommerce 4)
- **Use for**: Ecommerce flows, product pages, hero sections

### ADDITIONAL KIT ROLES (user-specified, not yet in primary tiers)
- **Triply AI**: AI interface in dashboard area — serves BOTH Property Connect AND Fitness platforms
- **Confiss**: Video conference elements
- **Travel Planner Light**: Great feed elements
- **Podcast Platform**: Podcast player components
- **Unity Gaming**: Video layouts
- **Nexus**: Collaboration UI
- **Beatrix**: Live streaming UI components
- **Video Streaming Web**: Connected TV and video
- **TrackApparel**: E-commerce (apparel-specific)
- **Furniture UI Kit**: Furniture-specific
- **Multi-concept Landing (Ofsp_ce)**: Elevated elements for app presentations, mockup image layouts
- **Align**: Bento cards and SaaS landing page elements
- **Stacks Design System**: Wireframes reference
- **Coreik**: Hero + landing/web page design elements + potential colour scheme (**NOT YET IN 38 KITS — may need adding**)

---

## COVERAGE MAP BY BUILD

### Enterprise OS (47 screens)
| Page Type | Primary Kit | Secondary Kit | Status |
|-----------|------------|---------------|--------|
| Dashboard Shell (8 tabs) | Brainwave 2.0 | Untitled UI Pro | COVERED |
| Command Deck | Square Dashboard | Untitled UI Pro | COVERED |
| Core Engine Views | Square Dashboard | Huose Property | COVERED |
| Knowledge Library | Untitled UI Pro | Brainwave 2.0 | COVERED |
| Template Hub | Untitled UI Pro | Brainwave 2.0 | COVERED |
| Build Factory Pipeline | Square Dashboard | Untitled UI Pro | COVERED |
| Domain Pillars Grid | Untitled UI Pro | Fleet Travel | COVERED |
| Operations/Admin | Square Dashboard | Untitled UI Pro | COVERED |
| Auth/Permissions (7-level) | Untitled UI Pro | Square Dashboard | COVERED |
| Settings | Untitled UI Pro | Square Dashboard | COVERED |
| AI Assistant Panel | Source Fusion AI | Untitled UI Pro | COVERED |

### Fitness Platform (16 screens)
| Page Type | Primary Kit | Secondary Kit | Status |
|-----------|------------|---------------|--------|
| Landing Page | Briefberry | Fleet Travel | COVERED |
| Auth Flow | Untitled UI Pro | Square Dashboard | COVERED |
| Onboarding Intake | Strivo (flow) | Untitled UI Pro (forms) | COVERED |
| AI Workout Generator (CORE) | Source Fusion AI + Triply AI | Untitled UI Pro | COVERED |
| Active Workout Mode | Fitness Pro | Brainwave 2.0 | COVERED |
| Exercise Library | Fitness Pro | Untitled UI Pro | COVERED |
| Dashboard/Home | Brainwave 2.0 | Untitled UI Pro | COVERED |
| Progress/History | Square Dashboard | Zip Formate | COVERED |
| Trainer Marketplace | Finder | Fleet Travel | COVERED |
| Social Feed | Social Dashboards | Brainwave 2.0 | COVERED |

### Property Connect London (15 screens)
| Page Type | Primary Kit | Secondary Kit | Status |
|-----------|------------|---------------|--------|
| Landing Page | Chroma | Real Estate SaaS | COVERED |
| Property Search/Listings | Fleet Travel | Finder | COVERED |
| Property Detail | Tripie Travel | Untitled UI Pro | COVERED |
| Agent Dashboard | Huose Property | Brainwave 2.0 | COVERED |
| Lead Management | Huose Property | Fleet Travel | COVERED |
| Client Portal | Brainwave 2.0 | Untitled UI Pro | COVERED |
| Messaging | Source Fusion AI | Untitled UI Pro | COVERED |
| Blog/Content | Untitled UI Pro | Briefberry | COVERED |

### Promo Sites (~5 pages per build × 3 builds)
| Page Type | Primary Kit | Secondary Kit | Status |
|-----------|------------|---------------|--------|
| Hero Section | Multi-concept Landing | eCommerce UI Kit | COVERED |
| Features/Benefits | Fleet Travel | Fitness Pro | COVERED |
| Pricing | Untitled UI Pro | Briefberry | COVERED |
| Testimonials | Aitentico | Briefberry | COVERED |
| Contact/CTA | Briefberry | Untitled UI Pro | COVERED |

---

## COVERAGE SUMMARY

| Build | Total Screens | Covered | Outstanding |
|-------|:---:|:---:|:---:|
| Enterprise OS | 47 | 47 | 0 |
| Fitness Platform | 16 | 16 | 0 |
| Property Connect London | 15 | 15 | 0 |
| Promo Sites | 15 | 15 | 0 |
| **TOTAL** | **93** | **93** | **0** |

### By Kit Importance
| Rank | Kit | Builds Served | Primary For |
|:---:|-----|:---:|-------------|
| 1 | Untitled UI Pro | ALL | Forms, profiles, content, settings |
| 2 | Brainwave 2.0 | ALL | Dashboard shell/layout framework |
| 3 | Square Dashboard | Enterprise, Fitness | Data views, analytics, auth |
| 4 | Fleet Travel | ALL | Top-level platform, cards, marketplace |
| 5 | Source Fusion AI | Enterprise, Fitness | AI chat/assistant interfaces |
| 5b | Chroma | ALL Promo/SaaS | DM Sans font stack, style guide (replaces Real Estate SaaS) |
| 6 | Square Dashboard | Enterprise, Fitness | Data views, profiles (NOT top-level) |
| 7 | Briefberry | Onboarding | Presell sequences, step-by-step flows ONLY |
| 8 | Tripie Travel | PCL | Platform front-end |
| 9 | Huose Property | PCL | Property dashboard, lead cards |
| 10 | Fitness Pro | Fitness | Exercise content, workout features |
| 11 | Finder | Fitness, PCL | Directory/marketplace listings |

### OUTSTANDING GAPS (Not covered by any kit)
- **Video conferencing UI**: Video Streaming Web kit has 16 items only
- **Voice training UI**: No specific kit
- **Dog platform UI**: No specific kit
- **Podcast player**: Podcast Platform has 9 items only
- **Gamification patterns**: Unity Gaming has 91 items (unused currently)

> These gaps represent future builds not yet in the active pipeline.

---

## SIDEBAR DECISION

Two options for the collapsed sidebar navigation pattern:
1. **Aitentico** — Collapsed sidebar (user specified)
2. **Trakr** — Cool sidebar (user specified)

Both are component-level extracts, not full page boilerplates. Decision deferred to page component drill-down (Monday).

---

## FONT STACK CONFIRMED

| Context | Font | Source Kit |
|---------|------|-----------|
| Apps / Dashboards / Back-end | Inter | Brainwave 2.0 |
| Website / Landing / SaaS Promo | DM Sans | **Chroma** (replaces Real Estate SaaS Kit) |

> Both Chroma and Real Estate SaaS use DM Sans. Need to verify font sizes match.
> If Chroma's design system conflicts with Brainwave shell, keep Inter for all dashboard/back-end areas.

---

## NEXT STEPS (Monday)

1. Log this session (summary → Command Deck, full → Knowledge Library)
2. Clear memory / context
3. For each of the 93 screens, drill down into:
   - Features per page
   - User flows and states
   - Required blocks/sections
   - Specific components from the assigned primary kit
4. Use Figma API to search by frame name, niche tags for specialist components
5. Build selection shortlist (not 500 options — targeted 5-10 per page section)
