# UI Component Library — Build Factory Pipeline

> Location: `07_BUILD_FACTORY/PRJ_UI_Component_Library/01_Strategy/BUILD_FACTORY_PIPELINE.md`
> Created: 2026-02-16
> Status: LOCKED IN — read this every session

## The Goal

One tokenized React component library → assemble ANY platform:
- Enterprise OS (personal — MVP screens)
- Fitness App (personal — MVP screens)
- Property Connect London (client — full screens)
- LeadEngine (production-ready — all screens)
- Client website (marketing)
- Future platforms (same components, swap brand tokens)

---

## Pipeline Stages

### STAGE 1: PRDs
Granular screen-by-screen spec for every platform.
- Every screen, state, modal, component listed
- Drives everything downstream — can't convert what isn't specified

### STAGE 2: Visual Inventory (AUTOMATED)
Export + AI-identify every page/frame across 38 Figma kits.
- Script: `enterprise-os-hub/scripts/batch-export-all-kits.js`
- Progress: `figma-exports/batch_progress.json`
- Output: Per-kit JSON with screen names, types, component lists
- Status as of 2026-02-16: 8/38 kits complete, ~15hrs for remainder

### STAGE 3: Selection & Matching
Cross-reference PRDs against visual inventories.
1. For each needed screen/component → which kit has the best version?
2. Build localhost thumbnail browser for visual selection
3. John picks winners from variants
4. Selections logged to manifest
5. **Zero in on 5-10 key pages per kit** — ignore the other 100+ screens

### STAGE 4: Figma → React Conversion (BOTTLENECK)
Convert selected frames via Anima (200/month limit).

Strategy:
- Convert COMPONENT PAGES first (buttons, cards, inputs) — one conversion = dozens of components
- Then convert key full-screen layouts
- Budget: ~150-200 conversions gets complete P0+P1 library across 2 months

Per conversion:
1. Open Figma link → select frame → run Anima → get React output
2. Save raw output to `04_Raw_Conversions/[kit_name]/[frame_name].tsx`
3. Log in conversion manifest

### STAGE 5: Decomposition & Tokenization (Claude Code)
Take raw Anima output → decompose into library.

1. Extract repeating patterns into individual components:
   - `atoms/` — Button, Input, Toggle, Badge, Avatar
   - `blocks/` — Card, StatCard, NavItem, ChatMessage
   - `layouts/` — Sidebar, Topbar, Modal, Drawer, SplitView
   - `boilerplates/` — Full page shells (Dashboard, Auth, Settings)
2. Replace ALL hardcoded values with CSS custom properties
3. Create TypeScript prop interfaces
4. Build brand token system:
   ```css
   .brand-enterprise { --brand-primary: #0B8C00; --font-heading: 'Inter'; }
   .brand-fitness { --brand-primary: #E36323; --font-heading: 'Inter'; }
   .brand-property { --brand-primary: #3582FF; --font-heading: 'DM Sans'; }
   .brand-leadengine { --brand-primary: #8755E9; --font-heading: 'Inter'; }
   ```

### STAGE 6: Assembly & Deploy
New screen = pick boilerplate + drop in components + apply brand tokens + connect data.
Building gets FAST here. Minutes per screen, not hours.

---

## Kit → Role Mapping

| Need | Primary Kit(s) |
|------|---------------|
| Dashboard shell, sidebar, topbar | Brainwave |
| Design system (buttons, inputs, modals) | Untitled UI Pro |
| Landing pages, marketing, front-end | Chroma, Multi-concept Landing |
| AI chat, prompt builder | Source Fusion AI, Triply AI |
| Property search, listings | Triply, Huose Property |
| Social feeds, activity | Social Dashboards, Travel Planner Light |
| Onboarding sequences | Briefberry, Strivo |
| Data views, tables, charts | Square Dashboard, Zip Formate |
| Collaboration | Nexus |
| Video conference | Confiss |
| Project management | Strivo |
| Fitness cards, components, layouts | Befit |
| E-commerce | eCommerce UI Kit |
| Directory/search | Finder |
| Jobs/hiring | Adify |
| Promo/marketing | Aimate, Majin |
| Collapsed sidebar | Aitentico, Trakr |
| Green tone variant | Caresync |
| Live streaming | Beatrix |
| Sales pages, lead gen | Separate batch (not in 38 core kits) |

---

## Page Types Needed (77 total)

### P0 — Every platform needs these (11)
1. Sign In / Login
2. Create Account / Register
3. Dashboard Overview (stats + charts + feed)
4. Settings (tabbed — general, profile, security, notifications, billing)
5. Profile (own + public)
6. Notifications
7. Card Grid / Browser
8. Data Table / List
9. Detail / Preview (lightbox or full page)
10. Search Results
11. 404 / Error

### P1 — Most platforms need these (10)
12. Landing Page / Home
13. Pricing / Plans
14. AI Chat Interface
15. Onboarding Wizard
16. Property Listing + Detail
17. Feed / Stream
18. Form / Data Entry
19. Split View (list + detail)
20. Calendar / Scheduler
21. File Manager

### P2 — Specific platforms or can wait (56)
About, Contact, Blog, FAQ, Legal, Case Studies, Coming Soon,
Sales Page, Lead Capture, Webinar, Thank You, Comparison, Feature Page,
Forgot Password, Reset Password, 2FA, Email Confirmation,
Welcome, Feature Tour, Import/Connect, Invite Team,
Dashboard Analytics, Kanban, Timeline, Map View,
Billing, Team Management, AI Results, AI Prompt Builder,
Inbox/Messages, Video Conference,
Product Listing/Detail/Cart/Checkout/Confirmation/History,
Agent Profile, Valuation Tool, Property Comparison,
Workout Plan, Exercise Detail, Progress Tracking, Meal Plan, Trainer Profile,
Maintenance, Empty States

---

## Component Types Needed (96 total)

### P0 — Universal (~23)
Sidebar, Topbar, Button (primary/secondary/ghost/icon), Input, Textarea,
Select/Dropdown, Toggle, Checkbox, Search (⌘K), Avatar, Badge,
Card (image), Card (stat), Modal, Toast, Tooltip, Table, Pagination,
Tab bar, Breadcrumbs, Empty state, Skeleton loader

### P1 — Common (~13)
Chat message, Prompt input bar, Accordion, Notification item, Date picker,
File upload, Progress bar, Tag/Chip, Menu/Context menu, Drawer/Sheet,
Alert/Banner, Stepper, Masonry grid

### P2 — Specialist (~15+)
Property card, Workout card, Product card, Chart components, Calendar,
Kanban, Video player, Comparison table, Pricing card, Countdown timer,
Carousel, Rich text editor, OTP input, Color picker, Slider/Range

---

## Tomorrow's Action Plan (2026-02-17)

**Inputs arriving:**
- PRDs (from script — need to check status)
- 38-kit visual inventory data (batch export — 8/38 done, rest incoming)

**Actions:**
1. Review PRDs → list exact screens per platform
2. Review kit inventories → identify 5-10 key pages per kit to convert
3. Build thumbnail browser (localhost) for visual selection
4. Start Anima conversions on highest-priority component pages
5. I decompose + tokenize the output

**The bottleneck is temporary.** Once ~150-200 conversions are done across 2 months, the library is complete and every platform builds fast.
