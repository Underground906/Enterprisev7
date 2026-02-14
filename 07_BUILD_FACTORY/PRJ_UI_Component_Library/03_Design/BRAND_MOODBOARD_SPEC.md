# Brand Moodboard — Figma File Spec
## Multi-Layout Color & Typography Visualization Tool

**Date:** 2026-02-14
**Purpose:** A single Figma file containing diverse real kit components and page layouts. Apply color styles and typography globally — change them once, everything updates. See your brand across every context before committing.

---

## HOW IT WORKS

### Setup (one-time)
1. Create a new Figma file: "BRAND_MOODBOARD"
2. Define **Color Styles** (not hard-coded hex values):
   - `brand/primary` → your green (#0B8C00 to start)
   - `brand/secondary` → TBD
   - `brand/accent` → TBD
   - `brand/dark` → near-black for text
   - `brand/light` → off-white for backgrounds
   - `brand/surface` → card/panel background
   - `brand/border` → subtle borders
   - `brand/success` → green
   - `brand/error` → red
   - `brand/warning` → amber
3. Define **Text Styles**:
   - `web/h1` through `web/caption` → DM Sans
   - `app/h1` through `app/caption` → Inter
4. Pull components from kits (listed below)
5. Apply your color styles and text styles TO the components (detach instances if needed)

### Usage
- To test a new color scheme: change the 7 color style definitions
- Every component on every page updates instantly
- Screenshot or compare side by side
- When you find the right palette, lock it

---

## MOODBOARD PAGES (Figma Pages)

### Page 1: TYPOGRAPHY SCALE

**What to include:**

```
DM Sans (Website/Landing)
─────────────────────────
H1: "Property Connect London" — 56px Bold
H2: "London Property Intelligence" — 40px SemiBold
H3: "Market Overview" — 28px SemiBold
H4: "Latest Insights" — 20px Medium
Body Large: "The complete property intelligence platform..." — 18px Regular
Body: "Connecting professionals with data-driven insights..." — 16px Regular
Body Small: "Updated daily from verified sources" — 14px Regular
Caption: "Source: Land Registry 2026" — 12px Regular

Inter (Dashboard/App)
─────────────────────
H1: "Dashboard" — 32px SemiBold
H2: "Analytics Overview" — 24px SemiBold
H3: "Client Pipeline" — 20px Medium
Body: "23 new leads this week" — 16px Regular
Label: "TOTAL REVENUE" — 12px Medium
Data: "£247,500" — 28px SemiBold
```

**Source kits:**
- Pull Chroma's DM Sans type scale page (as reference)
- Pull Brainwave's Inter type scale page (as reference)

---

### Page 2: HERO SECTIONS (5 variants)

These are full-width, so each sits as its own frame at 1440px wide.

| # | Variant | Source Kit | What to Pull |
|---|---------|-----------|-------------|
| 1 | **Video Background Hero** | Real Estate SaaS Kit | Their main homepage hero — headline over dark video/image |
| 2 | **Split Hero** (text left, image right) | Coreik | Hero section with headline + CTA left, visual right |
| 3 | **Centered Hero** (text center, gradient bg) | Chroma | SaaS landing hero with centered headline |
| 4 | **Dashboard Preview Hero** | Tripie | Platform landing hero showing app screenshot |
| 5 | **Minimal Hero** (text only, large heading) | Majin | Clean business hero with just headline + subline |

**Apply:** `brand/primary` to CTA buttons, `brand/dark` to headlines, `web/h1` text style to all main headings.

---

### Page 3: CARD COMPONENTS (10 types)

Arrange in a grid, 3 across. Each card at realistic size.

| # | Card Type | Source Kit | What to Pull |
|---|-----------|-----------|-------------|
| 1 | **Pricing Card** (3-tier) | Real Estate SaaS Kit | Their pricing card set (Free/Pro/Enterprise) |
| 2 | **Feature Card** (icon + title + text) | Align | Bento-style feature card |
| 3 | **Testimonial Card** (avatar + quote) | Real Estate SaaS Kit | Testimonial component |
| 4 | **Property Card** (image + details + price) | Huose Property | Property listing card |
| 5 | **Lead Card** (avatar + status + actions) | Huose Property | Lead/contact card with 4 circular icons |
| 6 | **Stat Card** (number + label + trend) | Brainwave 2.0 | Dashboard stat card |
| 7 | **Content Card** (thumbnail + title + meta) | Social Dashboards UI | Article/content feed card |
| 8 | **Event Card** (date + title + location) | Social Dashboards UI | Event listing card |
| 9 | **Profile Card** (avatar + name + role + stats) | Social Dashboards UI | User profile card |
| 10 | **Project Card** (progress + team + deadline) | Strivo | Project status card |

**Apply:** `brand/primary` to buttons/accents, `brand/surface` to card backgrounds, `brand/border` to card borders.

---

### Page 4: NAVIGATION & SIDEBARS (4 variants)

| # | Component | Source Kit | What to Pull |
|---|-----------|-----------|-------------|
| 1 | **Top Navigation** (full-width, mega menu) | Real Estate SaaS Kit | Main website nav bar |
| 2 | **Expanded Sidebar** (with labels + icons) | Trakr | Dashboard sidebar |
| 3 | **Collapsed Sidebar** (icons only) | Aitentico | Minimal sidebar |
| 4 | **Footer** (multi-column + social icons) | Real Estate SaaS Kit | Website footer |

**Apply:** `brand/primary` to active nav items, `brand/dark` to sidebar background (if dark mode), text styles for all labels.

---

### Page 5: DASHBOARD LAYOUTS (3 variants)

Full frames at 1440px wide showing realistic dashboard layouts.

| # | Layout | Source Kit | What to Pull |
|---|--------|-----------|-------------|
| 1 | **Analytics Dashboard** (stat cards + charts + table) | Brainwave 2.0 | Full dashboard page with sidebar |
| 2 | **List/Table View** (filters + data table + pagination) | Trakr | Dashboard list page |
| 3 | **Detail View** (header + tabs + content panels) | Brainwave 2.0 | Any detail/profile page |

**Apply:** `brand/primary` to accent elements (active tabs, chart highlights, buttons), Inter text styles throughout.

---

### Page 6: FORMS & AUTH (3 variants)

| # | Layout | Source Kit | What to Pull |
|---|--------|-----------|-------------|
| 1 | **Login** (split screen — brand left, form right) | Briefberry | Login page |
| 2 | **Multi-step Onboarding** (progress bar + form steps) | Strivo | Onboarding flow |
| 3 | **Contact/Lead Form** (form + supporting content) | Real Estate SaaS Kit | Contact page form section |

**Apply:** `brand/primary` to primary buttons and progress indicators, text styles to all labels and inputs.

---

### Page 7: SOCIAL & EMAIL (Brand Touchpoints)

These are the non-website/non-app brand surfaces. Critical for seeing if the brand works EVERYWHERE.

| # | Component | How to Build | Notes |
|---|-----------|-------------|-------|
| 1 | **Social Profile Card** (LinkedIn style) | Pull from Zipformat or Social Dashboards UI — profile card with banner, avatar, name, bio, stats | Shows how brand looks on social |
| 2 | **Social Post Mockup** | Pull from Social Dashboards UI — post card with image, text, engagement | Preview branded content posts |
| 3 | **Email Header** (newsletter) | Build from Real Estate SaaS Kit — top bar + logo + nav links at 600px wide | Newsletter brand treatment |
| 4 | **Email Body** (newsletter content) | Build from content cards at 600px wide — headline + image + body + CTA button | Email layout testing |
| 5 | **Email Footer** (unsubscribe + social links) | Build manually — logo, address, social icons, unsubscribe link | Legal compliance + brand |
| 6 | **Business Card** (horizontal) | Build manually — logo, name, title, contact details, brand colors | Physical brand check |
| 7 | **Favicon / App Icon** (various sizes) | Use cube logo at 16px, 32px, 180px, 512px in brand primary color | Digital brand check |

**Apply:** `brand/primary` to all buttons, links, accents. `brand/dark` to text. Logo in brand colors.

---

### Page 8: CONTENT & MEDIA (Editorial Layouts)

| # | Layout | Source Kit | What to Pull |
|---|--------|-----------|-------------|
| 1 | **Blog/Article Layout** (featured image + body + sidebar) | Social Dashboards UI | Article content page |
| 2 | **Podcast Player** (episode card + player controls) | Podcast Platform | Podcast page layout |
| 3 | **Video Player** (widescreen + title + description) | Unity or Social Dashboards UI | Video content page |
| 4 | **Magazine Cover** (editorial layout with headlines) | Build from Majin elements | Magazine front page feel |

**Apply:** `brand/primary` to play buttons, links, accents. DM Sans text styles for editorial content.

---

### Page 9: DATA VISUALIZATION

| # | Component | Source Kit | What to Pull |
|---|-----------|-----------|-------------|
| 1 | **Line Chart** (trend over time) | Brainwave 2.0 or Zipformat | Chart component |
| 2 | **Bar Chart** (comparison) | Brainwave 2.0 | Chart component |
| 3 | **Pie/Donut Chart** (distribution) | Brainwave 2.0 | Chart component |
| 4 | **Stat Cards Row** (4 KPIs in a row) | Brainwave 2.0 | Stat card set |
| 5 | **Data Table** (sortable, with status badges) | Trakr or Brainwave | Table component |
| 6 | **Heatmap / Calendar** (activity visualization) | Build from Brainwave elements | GitHub-style contribution grid |

**Apply:** Use `brand/primary` as the main chart color, pastels from Zipformat as secondary chart colors. This tests whether your primary color works in data context.

---

### Page 10: COLOR PALETTE REFERENCE

This page is your working palette — the definitions that drive everything else.

```
PRIMARY PALETTE
┌──────────┬──────────┬──────────┬──────────┬──────────┐
│ primary  │ primary  │ primary  │ primary  │ primary  │
│ 900      │ 700      │ 500      │ 300      │ 100      │
│ darkest  │          │ BASE     │          │ lightest │
└──────────┴──────────┴──────────┴──────────┴──────────┘

SECONDARY PALETTE
┌──────────┬──────────┬──────────┬──────────┬──────────┐
│ 900      │ 700      │ 500      │ 300      │ 100      │
└──────────┴──────────┴──────────┴──────────┴──────────┘

ACCENT PALETTE
┌──────────┬──────────┬──────────┬──────────┬──────────┐
│ 900      │ 700      │ 500      │ 300      │ 100      │
└──────────┴──────────┴──────────┴──────────┴──────────┘

NEUTRALS
┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ black    │ grey-900 │ grey-700 │ grey-500 │ grey-300 │ grey-100 │
│ #1A1A1A  │          │          │          │          │ #F5F5F5  │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘

FUNCTIONAL
┌──────────┬──────────┬──────────┬──────────┐
│ success  │ warning  │ error    │ info     │
│ green    │ amber    │ red      │ blue     │
└──────────┴──────────┴──────────┴──────────┘
```

**Source:** Pull the full color scale structure from Untitled UI — they have the best primitives (50 through 900 for every color). Then plug in your brand hues.

---

## KIT PULL LIST (Summary)

To build this moodboard you need components from these kits:

| Kit | Pages to Open | What to Copy |
|-----|--------------|-------------|
| **Real Estate SaaS Kit** | Homepage, Pricing, Contact, About | Hero, pricing cards, nav, footer, testimonials, contact form |
| **Brainwave 2.0** | Dashboard, Analytics, Components | Sidebar, stat cards, charts, tables, dashboard layouts |
| **Coreik** | Hero section page | Split hero variant |
| **Chroma** | Landing page, Typography | Centered hero, DM Sans type scale reference |
| **Majin** | Business landing | Minimal hero, editorial layout elements |
| **Align** | Landing page | Bento cards, feature cards |
| **Trakr** | Dashboard, Sidebar | Sidebar nav, data table, list view |
| **Aitentico** | Sidebar page | Collapsed sidebar |
| **Huose Property** | Property cards, Leads | Property card, lead card, circular action icons |
| **Social Dashboards UI** | Feed, Profile, Events, Chat | Content cards, event cards, profile cards, social posts, video player |
| **Strivo** | Onboarding, Projects | Onboarding flow, project cards |
| **Briefberry** | Login, Register | Auth pages, multi-step forms |
| **Zipformat** | Charts, Profile | Graph elements, social profile, pastel palette |
| **Tripie** | Platform pages | Dashboard preview hero |
| **Podcast Platform** | Player, Episodes | Podcast player component |
| **Unity** | Video page | Video player layout |
| **Untitled UI** | Color system | Full 50-900 color scale structure |

**Total: 17 kits to pull from.**

---

## BUILD ORDER FOR THE MOODBOARD

1. **Create the Figma file** — "BRAND_MOODBOARD" with 10 pages as listed above
2. **Page 10 first** — Set up the color palette and define all color styles from Untitled UI structure
3. **Page 1 second** — Set up typography styles (DM Sans web + Inter app)
4. **Pages 2-3** — Pull heroes and cards (highest visual impact, most useful for testing palettes)
5. **Page 4** — Pull navigation components
6. **Page 7** — Pull social/email (tests brand outside the website context)
7. **Pages 5-6** — Pull dashboard layouts and forms
8. **Pages 8-9** — Pull content/media and data viz

### Time Estimate
- Initial setup (styles + first pull): 2-3 hours
- Full moodboard complete: 4-6 hours across 2-3 sessions
- Then: instant palette testing forever after

---

## HOW TO TEST A NEW PALETTE

1. Go to Page 10 (Color Palette Reference)
2. Change the hex values in your color style definitions
3. Flip through all 10 pages
4. Ask: Does this feel right across heroes, cards, dashboards, social, email, data viz?
5. If not, change and try again
6. When it works everywhere, that's your brand palette — lock it

---

*17 kits. 10 pages. ~45 components. One file to rule all brand decisions.*
