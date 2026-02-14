# Master Screen Outline — All Builds
## Combined Screen Count, Boilerplate Analysis, Kit Mapping

**Date:** 2026-02-14
**Purpose:** Single reference for every screen across all active builds

---

## TOTAL SCREEN COUNT

| Build | MVP Screens | Full Screens | Source Doc |
|-------|------------|-------------|-----------|
| **PCL Marketing Site** | 17 | 17 | PCL_PAGE_INVENTORY.md |
| **PCL Spokes** | 12 | 12 | PCL_PAGE_INVENTORY.md |
| **PCL Platform Public** | 8 | 11 | PCL_PAGE_INVENTORY.md |
| **PCL Pro Dashboard** | 26 | 26 | PCL_PAGE_INVENTORY.md |
| **PCL Consumer Dashboard** | 18 | 18 | PCL_PAGE_INVENTORY.md |
| **Fitness App** | 16 | 27 | SCREEN_INVENTORY.md |
| **TOTAL** | **97** | **111** | — |

---

## BOILERPLATE LAYOUTS (Shared Across ALL Builds)

These are the reusable page structures. Design these ONCE, then populate with different content for each specific page.

### Layout 1: MARKETING PAGE
**Used by:** PCL Homepage, Service pages, About, Platform landing pages
**Structure:**
```
[MainNav]
[Hero Section — interchangeable: video/split/centered]
[Content Blocks — features, benefits, process, testimonials]
[CTA Section]
[Footer]
```
**Base Kit:** Real Estate SaaS Kit
**Font:** DM Sans
**Screens using this:** ~22 screens (PCL marketing + landing pages)

### Layout 2: FUNNEL PAGE
**Used by:** PCL Free Video funnel, Sponsorship application, Newsletter signup
**Structure:**
```
[Minimal Nav — logo + back only]
[Hero — headline + benefit statement]
[Form or Multi-step Form]
[Social Proof — testimonials, logos]
[FAQ]
```
**Base Kit:** Real Estate SaaS Kit + Briefberry (onboarding)
**Font:** DM Sans
**Screens using this:** ~8 screens

### Layout 3: SPOKE HOME (Content Hub)
**Used by:** PCL Magazine, Podcast, Video/CTV, Blog Index
**Structure:**
```
[MainNav]
[Hero — featured/latest content]
[Content Grid — cards with filters]
[Subscribe/CTA Section]
[Footer]
```
**Base Kit:** Real Estate SaaS Kit + Social Dashboards UI
**Font:** DM Sans
**Screens using this:** ~8 screens

### Layout 4: CONTENT DETAIL
**Used by:** PCL Blog post, Podcast episode, Area detail, Content hub detail
**Structure:**
```
[MainNav]
[Hero — title, author, date, category]
[Content Body — rich text / video player / audio player]
[Sidebar — related content, author info]
[Related Items Grid]
[Footer]
```
**Base Kit:** Social Dashboards UI + Podcast Platform
**Font:** DM Sans
**Screens using this:** ~10 screens

### Layout 5: DASHBOARD HOME
**Used by:** PCL Pro Dashboard, PCL Consumer Dashboard, Fitness App Dashboard
**Structure:**
```
[Sidebar Nav]
[Top Header — search, notifications, avatar]
[Stat Cards Row]
[Activity Feed / Today's Content]
[Quick Actions]
```
**Base Kit:** Brainwave 2.0
**Font:** Inter
**Screens using this:** 3 screens (but critical — highest daily usage)

### Layout 6: DASHBOARD LIST/GRID
**Used by:** PCL Content Library, Client Database, Fitness Exercise Browse, Video Library
**Structure:**
```
[Sidebar Nav]
[Top Header]
[Filter Bar — search, category, sort, view toggle]
[Data Table or Card Grid]
[Pagination]
```
**Base Kit:** Brainwave 2.0 + Trakr
**Font:** Inter
**Screens using this:** ~18 screens

### Layout 7: DASHBOARD DETAIL
**Used by:** PCL Client detail, Lead detail, Fitness Exercise detail, Session log
**Structure:**
```
[Sidebar Nav]
[Top Header]
[Detail Header — name, status, actions]
[Tab Navigation]
[Content Panels — info, history, notes, media]
```
**Base Kit:** Brainwave 2.0 + Huose Property (for property/lead cards)
**Font:** Inter
**Screens using this:** ~12 screens

### Layout 8: DASHBOARD FORM
**Used by:** PCL Create Article/Video/Event/Job, Fitness Profile/Settings, Program Builder
**Structure:**
```
[Sidebar Nav]
[Top Header]
[Form Header — title, save/cancel]
[Form Body — sections with inputs]
[Action Bar — save, publish, draft]
```
**Base Kit:** Brainwave 2.0 + Strivo (onboarding)
**Font:** Inter
**Screens using this:** ~15 screens

### Layout 9: ANALYTICS
**Used by:** PCL Analytics Dashboard, Fitness Progress Dashboard, Body Metrics
**Structure:**
```
[Sidebar Nav]
[Top Header]
[Date Range Selector]
[Stat Cards Row]
[Charts Grid (2-3 charts)]
[Data Table below charts]
```
**Base Kit:** Brainwave 2.0 + Zipformat (graph elements)
**Font:** Inter
**Screens using this:** ~8 screens

### Layout 10: AUTH FLOW
**Used by:** PCL Login/Register/Reset, Fitness App Login/Register
**Structure:**
```
[Split Screen: illustration/brand left + form right]
[OR: Centered card on gradient background]
[Form — fields, social login, links]
```
**Base Kit:** Briefberry (onboarding) + Strivo
**Font:** DM Sans (marketing context) or Inter (app context)
**Screens using this:** ~6 screens

### Layout 11: CHAT INTERFACE
**Used by:** Fitness AI Chat, PCL AI interface (future)
**Structure:**
```
[Sidebar Nav]
[Thread List (left panel)]
[Chat Messages (center)]
[Context Panel (right — optional)]
[Input Bar — text, attachments, send]
```
**Base Kit:** Source AI / Aimate + Triply
**Font:** Inter
**Screens using this:** ~3 screens

---

## COVERAGE ANALYSIS

| Layout | Screens Covered | % of Total |
|--------|----------------|------------|
| Marketing Page | 22 | 20% |
| Funnel Page | 8 | 7% |
| Spoke Home | 8 | 7% |
| Content Detail | 10 | 9% |
| Dashboard Home | 3 | 3% |
| Dashboard List/Grid | 18 | 16% |
| Dashboard Detail | 12 | 11% |
| Dashboard Form | 15 | 14% |
| Analytics | 8 | 7% |
| Auth Flow | 6 | 5% |
| Chat Interface | 3 | 3% |
| **TOTAL** | **113** | **~100%** |

**11 boilerplate layouts cover ALL 111 screens.** Some screens use a combination (e.g., Dashboard Home with Analytics elements), which explains the slight overcount.

---

## UNIQUE DESIGN PAGES (Cannot Be Templated)

These pages have layouts too specific for boilerplate — they need custom design:

### PCL (12 unique pages)
1. Homepage — multi-pathway hero + channel previews
2. Pricing — tier comparison + toggle (Pro/Consumer)
3. Property Search — map integration + results
4. Area Explorer — interactive London map + data layers
5. Pro Dashboard Home — custom widget grid
6. Consumer Dashboard Home — personalized feed
7. Magazine Home — editorial layout
8. Podcast Home — player + episodes grid
9. Register/Onboarding — multi-step + user type selection
10. Free Video Landing — funnel conversion page
11. Blog Index — content grid + categories
12. Professional Directory — search + categories

### Fitness App (4 unique pages)
1. Dashboard Home — today's routine timeline + streak + layers
2. Active Workout — video + timer + set logging (real-time mode)
3. AI Chat — chat interface
4. Progress Dashboard — multi-chart analytics view

**Total unique designs needed: 16 pages**
**Total templated from boilerplate: 95 pages**

---

## KIT ALLOCATION SUMMARY

### Website / Marketing / Public Pages (DM Sans)
| Kit | Primary Use |
|-----|------------|
| Real Estate SaaS Kit | Marketing page base, hero sections, pricing, features |
| Chroma | SaaS landing pages, DM Sans typography reference |
| Coreik | Hero sections, landing page elements |
| Majin | Business site presentations |
| Align | Bento cards, SaaS landing elements |
| Tripie | PCL platform public pages front-end |

### Dashboard / App Pages (Inter)
| Kit | Primary Use |
|-----|------------|
| Brainwave 2.0 | Dashboard base — sidebar, header, cards, charts, tables |
| Trakr | Dashboard components, sidebar menu variant |
| Befit | Fitness app dashboard, workout components |
| Fitness Pro | Fitness app components (441 components) |
| Triply | AI interface for dashboard areas |
| Source AI / Aimate | AI chat interface components |
| Social Dashboards UI | Video player, feeds, events, user profiles, inbox |
| Huose Property | Lead cards, property detail popups |
| Zipformat | Graph elements, data visualization |

### Shared / Cross-Context
| Kit | Primary Use |
|-----|------------|
| Untitled UI | Design tokens (color scales, shadows, typography) |
| Aitentico | Collapsed sidebar menu |
| Strivo | Onboarding flows |
| Briefberry | Onboarding, auth flows |
| Caresync | Green tones, design system reference |
| Stacks | Wireframe system |

### Specialized
| Kit | Primary Use |
|-----|------------|
| Adify | Jobs section (PCL) |
| Confiss | Video conference (PCL events) |
| Podcast Platform | Podcast UI (PCL) |
| Unity | Video layouts (PCL) |
| Video Streaming Web | Connected TV (PCL) |
| Beatrix | Live streaming (PCL CTV) |
| Ecommerce UI | Shop (PCL) |
| Track Apparel | E-commerce variant |
| Furniteuis | Home furnishing section (PCL) |
| Nexus | Collaboration UI (PCL community) |
| Travel Planner Light | Feed elements |
| Ofsp_ce | Elevated mockup presentations |

---

## BUILD ORDER

### Phase 1: Foundation (Week 1)
1. Design the 11 boilerplate layouts in Figma
2. Extract design tokens from Untitled UI + Chroma (DM Sans scale)
3. Set up Brainwave dashboard shell

### Phase 2: Unique Pages (Weeks 2-3)
4. Design 12 PCL unique pages
5. Design 4 Fitness App unique pages

### Phase 3: Template Application (Weeks 3-5)
6. Apply boilerplate layouts to all 95 templated pages
7. Populate with real content and placeholder data

### Phase 4: Fitness App Code (Weeks 2-6, parallel)
8. Scaffold React app with Brainwave dashboard
9. Import exercise data + video lookup
10. Build Daily Routine view → Active Workout → Exercise Library
11. Add AI Chat → Progress Logging

---

*16 unique designs + 11 boilerplate layouts = 111 screens covered. That's the plan.*
