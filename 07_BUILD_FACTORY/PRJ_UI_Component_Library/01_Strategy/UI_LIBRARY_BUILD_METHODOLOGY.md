# UI Component Library — Build Methodology (CANON)

> **Location:** `07_BUILD_FACTORY/PRJ_UI_Component_Library/01_Strategy/UI_LIBRARY_BUILD_METHODOLOGY.md`
> **Created:** 2026-02-18
> **Status:** CANON — Proven methodology, verified on 5 kits
> **Supersedes:** Sections of BUILD_FACTORY_PIPELINE.md (Stage 2 approach) and UI_ASSEMBLY_PIPELINE_SPEC.md (Stage 2 approach)
> **What changed:** Stage 2 no longer uses Gemini AI vision ($2). We now pull the complete Figma document tree via API and parse it mechanically. $0 cost. More accurate. Fully reproducible.

---

## Purpose

This document defines the **complete, proven methodology** for building a searchable UI component library from Figma kits. Every step has been validated on 5 kits (Brainwave 2.0, Real Estate SaaS Kit, Chroma, Majin, Befit). This is the single source of truth for how the library gets built.

---

## The Goal

One tokenized React component library that assembles ANY platform:

| Platform | Status | Primary Kit Sources |
|----------|--------|-------------------|
| Property Connect London | MVP target | Real Estate SaaS, Brainwave, Chroma |
| Fitness App | Personal imperative | Befit, Brainwave |
| Enterprise OS | Internal | Brainwave, Majin |
| LeadEngine | Production | Brainwave, Chroma, Majin |
| Client Websites | Marketing | Chroma, Aimate |
| Future Platforms | Swap brand tokens | Same library, different theme |

---

## Source Materials

### 1. Figma UI Kits (38 target kits)

Master index: `03_Design/KIT_INDEX.json`

Each kit is a Figma file containing 20-150+ screens with full component hierarchies. The kits span dashboard apps, landing pages, e-commerce, fitness, property, AI tools, and more.

**4 Foundation Kits (processed first):**

| Kit | File Key | Screens | Templates | Role |
|-----|----------|---------|-----------|------|
| Brainwave 2.0 | `6hCuwRI0GsBmIOJelAVpND` | 103 | 49 | Dashboard shell, app foundation, Inter font |
| Real Estate SaaS Kit | `88CZ1cuAGLBYxXI743aO1I` | 62 | 46 | Platform/marketplace screens |
| Chroma | `TWNCPNCVswFQwUKMq99dYI` | 48 | 29 | Landing/brochure pages, DM Sans font |
| Majin | `FcQ8RuwXhtMfNXOJDlZYS7` | 29 | 28 | Additional dashboard/promo screens |

**Priority Vertical Kit:**

| Kit | File Key | Screens | Templates | Role |
|-----|----------|---------|-----------|------|
| Befit | `T7pFT3vP0bqKpxiYdNkNGn` | 102 | 34 | Fitness dashboard, workout, nutrition |

### 2. Component Naming Taxonomy (47 files)

Source: `Downloads/UI Component System/Component names.zip`

27 UI component categories with hyper-granular naming conventions:
- Headers & Topbars, Sidebars & Drawers, Buttons, Charts & Graphs
- Dashboard Blocks, Search & Filters, FAQs & Accordions, Footers
- Forms & Inputs, Grids & Layouts, Hero Sections & CTAs
- Login & Signup, Modals & Toasts, Navigation & Menus
- Onboarding Flows, Pricing Sections, Profile & User Panels
- Project & Task Panels, Tables & Lists, Testimonials & Reviews
- UI Cards, Visual Design & Image Blocks, Chat Components
- Ecommerce Sections, Mobile Elements, Icon Buttons & Actions
- Social Media Components, Banners & Alerts

Each file defines: core structures, purpose variants, style variants, content elements, placement/behavior, interactive elements, responsive adaptations, trigger-based names, context-specific names, and utility/scripting tags.

**Integration:** These names become the **search vocabulary** for the component database. When searching for "dismissable-alert" or "sticky-banner", these taxonomy files define what those terms map to.

### 3. Copy Asset Artifacts (136 structure files)

Source: `Downloads/Copywriting System/Copy Asset Artifacts.zip`

136 screen/asset structure definitions covering:
- **Funnel pages:** Sales pages, tripwire, upsell, downsell, lead magnets, quiz results
- **Email sequences:** Welcome, cart abandonment, product launch, re-engagement, nurture
- **Social media:** Facebook, Instagram, LinkedIn, TikTok, Twitter, YouTube
- **E-commerce:** Product pages, checkout, order confirmation, product CTAs
- **App/in-app:** Onboarding modals, push notifications, tooltips, upgrade prompts
- **Events:** Webinar registration/invite/replay, virtual summit landing pages
- **Community:** Forum guidelines, welcome messages, referral programs

Each structure file is a table with: Element Name, Purpose, Tone & Style, Key Components, Copy Type (DR/Brand/Hybrid), Image Type.

**Integration:** These define **what copy elements each screen type needs**. When assembling a sales page, the structure file tells you: Hero Headline, Problem Statement, Primary CTA, Social Proof Block, etc. They extend the PRD screen requirements with copy-level granularity.

### 4. PRD Screen Requirements

File: `03_Design/PRD_SCREEN_REQUIREMENTS.json`

201 screens across 3 platforms:
- Property Connect: 102 screens
- Property AI Apps: 56 screens (with AI capabilities)
- Fitness: 16 screens + shared components

Each screen defines: layout code, components needed, priority, notes.

---

## The Pipeline (5 Phases)

All scripts live in `03_CORE_ENGINE/SCRIPTS/`. All output goes to `07_BUILD_FACTORY/PRJ_UI_Component_Library/kit_screens/`.

### Overview

```
Phase 1: EXTRACT     Figma API -> full JSON tree per kit           $0 (free API)
Phase 2: ANALYZE     JSON tree -> structured screen/layout data    $0 (local parse)
Phase 3: DEDUPLICATE Screens -> unique layout templates            $0 (local)
Phase 4: VISUALIZE   Representative PNGs per template              $0 (free API)
Phase 5: MATCH       PRD screens -> layout template matches        $0 (local)
```

**Total cost: $0.** All Figma API calls are free. All analysis is mechanical JSON parsing.

---

### Phase 1: Full Figma JSON Extraction

**Script:** `figma_deep_extract.py`
**API:** `GET /v1/files/{file_key}` (no depth param = full tree)
**Output:** `kit_screens/{KitName}/FIGMA_FULL.json`

Pulls the COMPLETE Figma document tree for each kit. No depth limit. This gives every node, its type, name, position, size, children, and full structure.

**What the API returns per node:**
- `id` — unique node ID (e.g., "919:33809")
- `name` — designer-given name
- `type` — FRAME, COMPONENT, INSTANCE, SECTION, GROUP, TEXT, VECTOR, etc.
- `absoluteBoundingBox` — x, y, width, height (can be null)
- `children` — full nested tree
- `componentId` — for INSTANCE nodes, links to master component
- `characters` — for TEXT nodes, the actual text content
- `fills`, `strokes`, `effects` — visual properties

**Settings:**
- Timeout: 300s (large files can take 30-60s to download)
- Rate delay: 5s between kits
- Checkpoint after each kit
- Save compact JSON (`separators=(',',':')`) for kits > 50MB to avoid MemoryError

**Verified results (5 kits):**

| Kit | File Size | Nodes | Max Depth |
|-----|-----------|-------|-----------|
| Brainwave 2.0 | 113.8 MB | 27,485 | 13 |
| Real Estate SaaS Kit | 92.8 MB | 33,555 | 14 |
| Chroma | 91.8 MB | 29,632 | 15 |
| Majin | 144.5 MB | 34,724 | 14 |
| Befit | 130.5 MB | 68,480 | 16 |

**Known issues:**
- Some kits produce 400+ MB pretty-printed JSON. Always save compact.
- The `absoluteBoundingBox` field can be `null` on some nodes. Code handles this with `or {}`.

---

### Phase 2: Structure Analysis

**Script:** `figma_structure_analyzer.py`
**Input:** `kit_screens/{KitName}/FIGMA_FULL.json`
**Output:** `kit_screens/{KitName}/SCREEN_ANALYSIS.json` + `kit_screens/CORE_KITS_LIBRARY.json` (combined)

Walks the full JSON tree and builds structured analysis. No AI — pure mechanical parsing.

#### Screen Detection

A "screen" is any node that meets ALL of:
- Type: FRAME, COMPONENT, or INSTANCE (not SECTION, GROUP, TEXT, VECTOR)
- Width >= 1200px AND height >= 600px
- NOT a canvas board (see below)

**Canvas board detection (critical fix):** Some kits (e.g., Befit) arrange screens on huge design canvases. A node > 5000px in either dimension is a **canvas board**, not a screen. The script recurses INTO these to find the actual screens nested inside.

```
Without canvas detection: Befit = 5 "screens" (actually giant canvases)
With canvas detection:    Befit = 102 screens (the real screens inside the canvases)
```

Screens are found at ANY depth in the tree, not just top-level. This catches screens nested inside SECTIONs, inside other FRAMEs, or inside COMPONENTs.

#### Layout Classification

For each screen, direct children are analyzed by their position relative to the screen bounds:

| Position Rule | Classification |
|---------------|---------------|
| Child at x < 350, height > 60% of screen | Left sidebar |
| Child at x > (width - 400), height > 60% of screen | Right panel |
| Child at y < 100, width > 80% of screen | Top header/nav |
| Child at y > (height - 80), width > 80% of screen | Bottom bar/footer |
| Everything else | Main content area |

**Layout types:**
- `sidebar_content` — left nav + main area
- `three_panel` — left + center + right
- `full_canvas` — no sidebar, one main area
- `split_panel` — two roughly equal columns
- `header_content_footer` — stacked vertically
- `cards_grid` — main area contains repeated similar-sized children

#### Data Extraction

For each screen, the script extracts:

```json
{
  "screen_id": "919:33809",
  "screen_name": "AI Canvas Editor",
  "page": "Pre-made templates",
  "node_type": "FRAME",
  "dimensions": {"width": 1440, "height": 900},
  "is_light": true,
  "layout": {
    "type": "three_panel",
    "description": "...",
    "panels": [
      {"position": "left", "width_approx": 240, "role": "sidebar", "components": [...], "text_labels": [...]},
      {"position": "center", "width_approx": 880, "role": "main_content", "components": [...]},
      {"position": "right", "width_approx": 320, "role": "properties_panel", "components": [...]}
    ]
  },
  "capabilities": ["file_management", "property_controls", "layer_management"],
  "all_text_content": ["My Files", "Shared", "Recent", "Properties", "Layers", "Export"],
  "component_count": 47,
  "nested_components": [
    {"name": "Button/Primary", "type": "INSTANCE", "text": "Export"},
    {"name": "Input/Search", "type": "INSTANCE", "text": "Search files..."}
  ]
}
```

**Key insight:** TEXT nodes give us the actual labels, headings, and content on every screen. INSTANCE nodes tell us exactly which master components are used. Combined, this gives a complete picture of what each screen does — without any AI.

#### Verified Results

| Kit | Screens Found | Avg Components/Screen |
|-----|--------------|----------------------|
| Brainwave 2.0 | 103 | ~40-60 |
| Real Estate SaaS Kit | 62 | ~30-50 |
| Chroma | 48 | ~25-45 |
| Majin | 29 | ~35-55 |
| Befit | 102 | ~30-50 |

---

### Phase 3: Layout Deduplication

**Script:** `layout_deduplicator.py`
**Input:** `kit_screens/{KitName}/SCREEN_ANALYSIS.json`
**Output:** `kit_screens/{KitName}/LAYOUT_TEMPLATES.json` + `kit_screens/CORE_LAYOUT_LIBRARY.json` (combined)

Most kits have 50-100 screens but only 10-50 unique layout patterns. This phase groups screens by structure to find the unique templates.

#### Algorithm

1. **Group by layout type** (sidebar_content, three_panel, full_canvas, etc.)
2. **Within each group, compare panel signatures** — a string like `left:sidebar:narrow|center:main_content:wide|right:properties:medium`
3. **Within same signature, merge by component overlap** — Jaccard similarity >= 0.6 (60%) means same template, different content/state
4. **Pick representative** — the screen with the most components becomes the template's representative

#### What Each Template Contains

```json
{
  "layout_id": "BW_L1",
  "name": "AI Canvas Editor",
  "type": "three_panel",
  "panel_signature": "left:sidebar:narrow|center:main_content:wide|right:properties:medium",
  "screens_using": ["AI Canvas Editor", "Scene View", "Material Editor"],
  "count": 12,
  "representative_screen": "919:33809",
  "core_components": ["accordion", "avatar", "breadcrumb", "button", "card", ...],
  "capabilities": ["3d_editing", "file_management", "property_controls"]
}
```

#### Verified Deduplication Results

| Kit | Total Screens | Unique Templates | Reduction |
|-----|--------------|-----------------|-----------|
| Brainwave 2.0 | 103 | 49 | 52% |
| Real Estate SaaS Kit | 62 | 46 | 26% |
| Chroma | 48 | 29 | 40% |
| Majin | 29 | 28 | 3% |
| Befit | 102 | 34 | 67% |
| **Total** | **344** | **186** | **46%** |

Befit shows the best deduplication (67%) because fitness apps reuse the same layouts heavily (workout list, exercise detail, progress tracker all share the same sidebar_content layout with different data).

---

### Phase 4: Representative PNG Export

**Script:** `figma_export_representative.py`
**API:** `GET /v1/images/{file_key}` with `format=png&scale=0.5`
**Output:** `kit_screens/{KitName}/representative/{screen_id}_{name}.png`

Exports ONE PNG per unique layout template. Instead of exporting 344 screens, we export 186 (one per template). These serve as visual thumbnails for the browser UI and Anima conversion selection.

**Settings (proven stable):**
- Batch size: 3 (max node IDs per render request)
- Scale: 0.5 (half resolution — sufficient for visual reference)
- Rate delay: 3.0s between batches (well within Figma's 30 req/min limit)
- Download timeout: 60s per image
- Checkpoint after every successful download

**Verified results:**
- 4 core kits: 152/152 PNGs exported, zero failures
- Befit: 34 templates pending export

**Known issues:**
- Batches > 10 node IDs can trigger 400 render timeout from Figma
- SECTION nodes return null image URLs — the script only exports FRAME/COMPONENT/INSTANCE screens
- Some nodes produce very small PNGs (<500 bytes) — these are flagged as failures

---

### Phase 5: PRD Layout Matching

**Script:** `prd_layout_matcher.py`
**Input:** `CORE_LAYOUT_LIBRARY.json` + `PRD_SCREEN_REQUIREMENTS.json`
**Output:** `kit_screens/PRD_LAYOUT_MATCHES.json`

Matches each PRD screen requirement against the layout template library to find the best kit/template match.

#### Scoring System (0-100)

| Factor | Points | How |
|--------|--------|-----|
| Layout type match | 40 | PRD layout code maps to template layout type. Direct match = 40, fallback = 30. |
| Component coverage | 40 | What % of PRD's required components exist in the template. Uses alias matching (e.g., "topbar" matches "header", "navbar", "navigation"). |
| Capability overlap | 20 | How many PRD notes/features appear in the template's capability list. 5 pts each, max 20. |

#### Layout Code Mapping

| PRD Code | Maps To |
|----------|---------|
| FC (Full Canvas) | full_canvas, header_content_footer, cards_grid |
| SC (Sidebar Content) | sidebar_content, three_panel |
| TP (Three Panel) | three_panel |
| SP (Split Panel) | split_panel |
| CG (Cards Grid) | cards_grid, full_canvas |
| HCF (Header Content Footer) | header_content_footer, full_canvas |

#### Component Alias System

The matcher normalizes component names so "topbar", "header", "navbar", and "navigation" all match each other. 30+ canonical component types with 3-5 aliases each.

#### Verified Results (4 core kits vs 201 PRD screens)

| Match Quality | Count | Percentage |
|--------------|-------|------------|
| Perfect (70+) | 1 | 0.5% |
| Good (40-69) | 34 | 17% |
| Weak (10-39) | 163 | 81% |
| No match | 3 | 1.5% |

**Coverage improves as more kits are processed.** With only 4 kits (152 templates), 17% of PRD screens get good+ matches. The 40 target kits will provide 1000+ templates and dramatically improve coverage.

**Most commonly missing components:** card (131 screens), chart (64), badge (45), progress (25), map (18). These are specific component types that need targeted sourcing from specialist kits.

---

## Library Structure

### File Organization

```
kit_screens/
  ├── CORE_KITS_LIBRARY.json          # Combined screen analysis (all processed kits)
  ├── CORE_LAYOUT_LIBRARY.json        # Combined layout templates (all processed kits)
  ├── PRD_LAYOUT_MATCHES.json         # PRD-to-template matching results
  ├── DEEP_EXTRACT_CHECKPOINT.json    # Extraction progress tracker
  ├── REPRESENTATIVE_EXPORT_CHECKPOINT.json
  │
  ├── Brainwave 2.0/
  │   ├── FIGMA_FULL.json             # Raw Figma document tree
  │   ├── SCREEN_ANALYSIS.json        # Structured screen/layout/component data
  │   ├── LAYOUT_TEMPLATES.json       # Unique layout templates
  │   └── representative/             # One PNG per template
  │       ├── 919_33809_AI_Canvas_Editor.png
  │       └── ...
  │
  ├── Real Estate SaaS Kit/
  │   ├── (same structure)
  │
  ├── Chroma/
  │   ├── (same structure)
  │
  ├── Majin/
  │   ├── (same structure)
  │
  └── Befit/
      ├── (same structure)
```

### 4-Level Component Hierarchy

```
PAGES (full screen layouts — the 344 screens we extracted)
  └── BOILERPLATES (unique layout templates — the 186 deduplicated patterns)
       └── BLOCKS (sections within templates — sidebar, header, content area, card grid)
            └── COMPONENTS (atomic elements — buttons, inputs, cards, badges)
```

This maps directly to the Figma tree structure:
- **Pages** = screen-level FRAME/COMPONENT/INSTANCE nodes (>= 1200x600)
- **Boilerplates** = deduplicated layout templates (Phase 3 output)
- **Blocks** = direct children of screen nodes (panels, sections, headers)
- **Components** = INSTANCE nodes (references to master components)

---

## Database Design

### PostgreSQL Schema (extends existing `ui_library`)

```sql
-- Core screen inventory from Figma JSON extraction
CREATE TABLE figma_screens (
  id SERIAL PRIMARY KEY,
  kit_name TEXT NOT NULL,
  figma_file_key TEXT NOT NULL,
  figma_node_id TEXT NOT NULL,         -- e.g. "919:33809"
  screen_name TEXT,
  page_name TEXT,                      -- Figma page this screen lives in
  node_type TEXT,                      -- FRAME, COMPONENT, INSTANCE
  width INTEGER,
  height INTEGER,
  is_light BOOLEAN,
  layout_type TEXT,                    -- sidebar_content, three_panel, full_canvas, etc.
  layout_description TEXT,
  capabilities TEXT[],                 -- inferred from text/components
  all_text_content TEXT[],             -- every TEXT node's content
  component_count INTEGER,
  png_path TEXT,                       -- path to representative PNG
  figma_url TEXT,                      -- direct Figma link
  created_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(figma_file_key, figma_node_id)
);

-- Panel breakdown per screen
CREATE TABLE screen_panels (
  id SERIAL PRIMARY KEY,
  screen_id INTEGER REFERENCES figma_screens(id) ON DELETE CASCADE,
  position TEXT,                       -- left, center, right, top, bottom
  role TEXT,                           -- sidebar, main_content, properties_panel, header, footer
  width_approx INTEGER,
  height_approx INTEGER,
  components TEXT[],                   -- component names in this panel
  text_labels TEXT[]                   -- text content in this panel
);

-- Component instances found in screens
CREATE TABLE screen_components (
  id SERIAL PRIMARY KEY,
  screen_id INTEGER REFERENCES figma_screens(id) ON DELETE CASCADE,
  component_name TEXT NOT NULL,        -- e.g. "Button/Primary"
  component_type TEXT,                 -- INSTANCE, COMPONENT
  figma_component_id TEXT,             -- master component reference
  text_content TEXT,                   -- text visible on the component
  canonical_type TEXT                  -- normalized: "button", "card", "input", etc.
);

-- Deduplicated layout templates
CREATE TABLE layout_templates (
  id SERIAL PRIMARY KEY,
  layout_id TEXT UNIQUE NOT NULL,      -- e.g. "BW_L1"
  kit_name TEXT NOT NULL,
  template_name TEXT,
  layout_type TEXT,
  panel_signature TEXT,
  screens_using TEXT[],                -- list of screen names using this template
  screen_count INTEGER,
  representative_screen_id TEXT,       -- figma node ID of representative
  core_components TEXT[],
  capabilities TEXT[],
  png_path TEXT
);

-- PRD screen requirements
CREATE TABLE prd_screens (
  id SERIAL PRIMARY KEY,
  screen_id TEXT UNIQUE NOT NULL,      -- e.g. "PCL_DASH_01"
  screen_name TEXT,
  platform TEXT,                       -- property, fitness, ai_apps
  layout_code TEXT,                    -- FC, SC, TP, SP, CG, HCF
  components_needed TEXT[],
  priority TEXT,                       -- P0, P1, P2
  notes TEXT,
  copy_structure_file TEXT             -- link to copy asset artifact
);

-- PRD-to-template matches
CREATE TABLE prd_matches (
  id SERIAL PRIMARY KEY,
  prd_screen_id TEXT REFERENCES prd_screens(screen_id),
  template_id TEXT REFERENCES layout_templates(layout_id),
  score INTEGER,                       -- 0-100
  layout_match TEXT,                   -- direct, fallback, none
  component_coverage FLOAT,
  matched_components TEXT[],
  missing_components TEXT[],
  rank INTEGER                         -- 1 = best match, 2 = second, etc.
);

-- Component naming taxonomy (from Component names.zip)
CREATE TABLE component_taxonomy (
  id SERIAL PRIMARY KEY,
  category TEXT NOT NULL,              -- e.g. "Buttons", "Charts & Graphs"
  canonical_name TEXT NOT NULL,        -- e.g. "primary-button"
  variant_type TEXT,                   -- core, purpose, style, content, placement, interactive
  description TEXT,
  aliases TEXT[]                       -- all alternative names
);

-- Copy asset structures (from Copy Asset Artifacts.zip)
CREATE TABLE copy_structures (
  id SERIAL PRIMARY KEY,
  asset_name TEXT NOT NULL,            -- e.g. "core_offer_sales_page"
  channel_type TEXT,                   -- Funnel, Email, Social, App, etc.
  funnel_stage TEXT,                   -- TOFU, MOFU, BOFU
  copy_type TEXT,                      -- DR, Brand, Hybrid
  priority INTEGER,
  elements JSONB                       -- array of {name, purpose, tone, components, copy_type, image_type}
);

-- Indexes
CREATE INDEX idx_screens_kit ON figma_screens(kit_name);
CREATE INDEX idx_screens_layout ON figma_screens(layout_type);
CREATE INDEX idx_panels_screen ON screen_panels(screen_id);
CREATE INDEX idx_components_screen ON screen_components(screen_id);
CREATE INDEX idx_components_canonical ON screen_components(canonical_type);
CREATE INDEX idx_templates_kit ON layout_templates(kit_name);
CREATE INDEX idx_templates_type ON layout_templates(layout_type);
CREATE INDEX idx_prd_platform ON prd_screens(platform);
CREATE INDEX idx_prd_priority ON prd_screens(priority);
CREATE INDEX idx_matches_prd ON prd_matches(prd_screen_id);
CREATE INDEX idx_taxonomy_category ON component_taxonomy(category);
CREATE INDEX idx_copy_channel ON copy_structures(channel_type);

-- Full text search on screen text content
CREATE INDEX idx_screens_text ON figma_screens USING GIN(all_text_content);
CREATE INDEX idx_taxonomy_aliases ON component_taxonomy USING GIN(aliases);
```

### Example Queries

**Find all dashboard screens with sidebar + chart:**
```sql
SELECT fs.screen_name, fs.kit_name, fs.layout_type, fs.png_path
FROM figma_screens fs
WHERE fs.layout_type = 'sidebar_content'
AND EXISTS (SELECT 1 FROM screen_components sc WHERE sc.screen_id = fs.id AND sc.canonical_type = 'chart')
ORDER BY fs.component_count DESC;
```

**Find best template match for a PRD screen:**
```sql
SELECT lt.layout_id, lt.kit_name, lt.template_name, pm.score, pm.missing_components
FROM prd_matches pm
JOIN layout_templates lt ON lt.layout_id = pm.template_id
WHERE pm.prd_screen_id = 'PCL_DASH_01'
ORDER BY pm.score DESC
LIMIT 5;
```

**Search across all screens by text content:**
```sql
SELECT screen_name, kit_name, layout_type
FROM figma_screens
WHERE 'workout' = ANY(all_text_content)
   OR 'exercise' = ANY(all_text_content);
```

---

## End-to-End Workflow

### Step 1: Define What You Need (PRD)

Start with the PRD screen requirements. Each screen specifies:
- Layout type (sidebar_content, three_panel, etc.)
- Components needed (sidebar, cards, chart, table, etc.)
- Platform (property, fitness, etc.)
- Priority (P0/P1/P2)

Extend with copy asset artifacts to define what copy elements each screen needs (headlines, CTAs, social proof blocks, etc.).

### Step 2: Extract Figma Data (Phases 1-3)

Run the pipeline on target kits:

```bash
# Phase 1: Pull full JSON from Figma
python figma_deep_extract.py

# Phase 2: Parse into structured screen analysis
python figma_structure_analyzer.py

# Phase 3: Deduplicate into unique templates
python layout_deduplicator.py
```

Each phase takes 5-10 minutes. Total pipeline: ~20-30 minutes for 4 kits.

### Step 3: Get Visual References (Phase 4)

```bash
# Phase 4: Export representative PNGs
python figma_export_representative.py
```

~10 minutes for 150 PNGs. These become thumbnails in the visual browser.

### Step 4: Match PRDs to Templates (Phase 5)

```bash
# Phase 5: Cross-reference PRDs against template library
python prd_layout_matcher.py
```

Output tells you, for each PRD screen:
1. Which layout template is the best match (from which kit)
2. What components are already covered
3. What's missing and where to source it from other kits

### Step 5: Visual Review (Localhost Browser)

Open the visual browser to:
- Browse all templates as thumbnail grid
- Click to see full-size PNG
- Compare variants of the same layout type across kits
- Mark selections for Anima conversion
- Copy Figma URLs to clipboard

### Step 6: Anima Conversion

For each selected template:
1. Open the Figma URL (direct link to the specific frame)
2. Run Anima plugin on that frame
3. Get React/Tailwind output
4. Save to `04_Raw_Conversions/{kit_name}/{frame_name}.tsx`

**Budget:** 200 conversions/month free. With 186 unique templates, that's complete coverage in 1 month.

**Strategy:** Convert COMPONENT PAGES first (buttons, cards, inputs) because one conversion yields dozens of reusable components. Then convert full-screen layouts.

### Step 7: Decomposition & Tokenization

Take raw Anima output and decompose into the component library:

```
src/components/
  ├── atoms/          # Button, Input, Toggle, Badge, Avatar
  ├── blocks/         # Card, StatCard, NavItem, ChatMessage
  ├── layouts/        # Sidebar, Topbar, Modal, Drawer, SplitView
  └── boilerplates/   # Full page shells (Dashboard, Auth, Settings)
```

Replace ALL hardcoded values with CSS custom properties:
```css
:root {
  --brand-primary: #0B8C00;    /* Enterprise OS green */
  --brand-secondary: #49ba61;  /* Alt green */
  --font-heading: 'Inter';
  --font-body: 'Inter';
  --spacing-unit: 8px;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

.brand-fitness {
  --brand-primary: #E36323;
  --font-heading: 'Inter';
}

.brand-property {
  --brand-primary: #3582FF;
  --font-heading: 'DM Sans';
}
```

### Step 8: Assembly

New screen = pick boilerplate + drop in components + apply brand tokens + connect data.

```
PRD Screen: "Property Dashboard Overview"
  -> Template: RE_L3 (Real Estate SaaS Kit, sidebar_content)
  -> Boilerplate: DashboardShell (from Brainwave)
  -> Blocks: StatCardRow, PropertyGrid, RecentActivityFeed
  -> Components: Sidebar, Topbar, PropertyCard, StatCard, Chart
  -> Theme: brand-property (DM Sans, #3582FF)
  -> Route: /dashboard
```

---

## Scripts Reference

### Active Pipeline Scripts (03_CORE_ENGINE/SCRIPTS/)

| Script | Phase | Purpose | Cost |
|--------|-------|---------|------|
| `figma_deep_extract.py` | 1 | Pull full Figma JSON tree per kit | $0 |
| `figma_structure_analyzer.py` | 2 | Parse JSON into screen/layout/component data | $0 |
| `layout_deduplicator.py` | 3 | Group screens into unique templates | $0 |
| `figma_export_representative.py` | 4 | Export one PNG per unique template | $0 |
| `prd_layout_matcher.py` | 5 | Match PRD screens to templates | $0 |

### Legacy Scripts (still useful for specific tasks)

| Script | Purpose |
|--------|---------|
| `figma_frame_inventory.py` | Depth=2 frame listing (fast but misses nested screens) |
| `figma_export_pngs.py` | Batch PNG export (v2, used for the 5,131 PNGs from Monday) |
| `figma_extract_tokens.py` | Extract design tokens (colors, fonts, spacing) from Figma |
| `figma_catalog.py` | Catalog kit metadata |

### Scripts NOT Used Anymore

| Script | Why Replaced |
|--------|-------------|
| `figma_classify.py` | Used Groq AI vision — got IP-blocked, unreliable |
| `figma_subcategorize.py` | Same — AI vision approach replaced by JSON parsing |

---

## Known Issues & Mitigations

| Issue | Cause | Mitigation |
|-------|-------|-----------|
| Canvas boards detected as screens | Befit/some kits use giant canvases (>5000px) | Nodes > 5000px in either dimension are recursed into, not captured as screens |
| `absoluteBoundingBox` is null | Some Figma nodes lack position data | Handle with `or {}` fallback |
| MemoryError on large JSON | Pretty-printed JSON can be 400+ MB | Save compact with `separators=(',',':')` |
| Windows encoding errors | cp1252 can't handle Unicode arrows | Use ASCII-safe characters in print statements |
| Figma render timeout | >10 node IDs per batch = 400 error | Batch size capped at 3, with retry logic |
| SECTION nodes can't export as PNG | Figma returns null for SECTION type | Only export FRAME/COMPONENT/INSTANCE nodes |
| COMPONENT-typed screens | Some 1440x900 screens are typed COMPONENT not FRAME | Classify by dimensions, not Figma node type |

---

## Scaling Plan

### Current: 5 kits processed

344 screens, 186 unique templates, 152 representative PNGs.

### Next: 40 target kits

The same pipeline runs identically on any kit. Estimated:
- ~2,000-3,000 screens across 40 kits
- ~800-1,200 unique templates after deduplication
- Full pipeline for 40 kits: ~3-4 hours (mostly Figma API + PNG download time)
- Database import: ~30 minutes
- PRD matching improves dramatically with 1000+ templates to match against

### Kit Processing Priority

1. **Foundation kits** (done): Brainwave 2.0, Real Estate SaaS, Chroma, Majin
2. **Vertical priority** (done): Befit (fitness)
3. **Next batch**: Property-specific kits (Huose Property, Triply), AI kits (Source Fusion AI, Triply AI)
4. **Design system kits**: Untitled UI Pro (atomic components)
5. **Remaining 30+ kits**: Batch process all together

---

## Integration Points

### With Enterprise OS Pillars

| Pillar | How It Connects |
|--------|----------------|
| PIL_07_UI_LIBRARY | This IS the UI Library build process |
| PIL_03_COPY | Copy asset artifacts define text requirements per screen |
| PIL_12_KEYWORDS | Search vocabulary for component database |
| PIL_19_PROPERTY | Property Connect screens drive PRD requirements |
| PIL_20_FITNESS | Fitness screens drive PRD requirements |
| PIL_02_BRANDING | Brand tokens (colors, fonts) come from branding pillar |

### With Existing PostgreSQL Database

The existing `ui_library` database (19,837 items, 183 kits) was built from Figma frame metadata. The new tables extend it with:
- Deep structural analysis (layout type, panels, components)
- Text content extraction (actual labels and headings)
- Layout deduplication (unique templates)
- PRD matching scores
- Component taxonomy search
- Copy structure requirements

---

## Verification Checklist

After processing a new kit, verify:

- [ ] Phase 1: FIGMA_FULL.json is > 1MB and contains full tree (not truncated)
- [ ] Phase 2: Screen count is reasonable (20-150, not 3-5). If low, check for canvas boards.
- [ ] Phase 2: Screen dimensions are 1200-1920px wide (real screens, not icons)
- [ ] Phase 3: Template count < screen count (deduplication is working)
- [ ] Phase 3: Each template has >= 1 screen using it
- [ ] Phase 4: Representative PNGs download successfully and are > 1KB
- [ ] Phase 5: Every PRD screen gets at least 1 match (even if weak)

---

## What This Replaces

This methodology replaces the earlier approach documented in BUILD_FACTORY_PIPELINE.md (Stage 2) and UI_ASSEMBLY_PIPELINE_SPEC.md (Stage 2) which relied on:

- **Gemini 2.0 Flash vision** for screen identification (~$2 for 38 kits)
- **PNG-first approach** (export PNGs, then analyze them with AI)
- **Depth=2 Figma frame listing** (missed 80%+ of screens)

The new approach:
- **$0 cost** (no AI needed for structure extraction)
- **JSON-first** (pull the complete document tree, parse mechanically)
- **Full depth** (finds every screen at any nesting level)
- **More accurate** (actual component references, not AI guesses)
- **Reproducible** (same input = same output, no AI variance)

The original BUILD_FACTORY_PIPELINE.md and UI_ASSEMBLY_PIPELINE_SPEC.md remain valid for Stages 3-6 (Selection, Conversion, Decomposition, Assembly). Only Stage 2 (identification) has been replaced.

---

*This document is the single source of truth for the UI Library build methodology. Updated: 2026-02-18.*
