# UI Assembly Pipeline — Architecture Spec

> **Status:** LOCKED IN — 2026-02-16
> **Owner:** John
> **Scope:** All 38 UI kits → All Enterprise OS projects

---

## The Vision

Turn 38 Figma UI kits (7,683 items) into a searchable, structured component inventory that an LLM can cross-reference against any PRD to automatically find, extract, convert, and assemble the right UI components into working React pages.

---

## Pipeline Overview

```
STAGE 1: EXPORT          Figma API → PNG screens per kit
STAGE 2: IDENTIFY         AI Vision (Gemini Flash) → structured JSON inventory
STAGE 3: STRUCTURE        Inventory → 4-level hierarchy in database
STAGE 4: MATCH            PRD screens → inventory cross-reference
STAGE 5: EXTRACT          Figma → React component conversion
STAGE 6: ASSEMBLE         Canvas rendering → page assembly from components
```

---

## Stage 1: EXPORT (Done for Brainwave)

**Script:** `enterprise-os-hub/scripts/export-figma-screens.js`

- Input: Figma file key from KIT_INDEX.json
- Process: Figma API → export frames as PNGs (batch of 8, 120s timeout)
- Output: `public/figma-exports/{file_key}/screens/*.png` + `manifest.json`
- Run per kit. 38 kits total.

**Status:** Working. Brainwave 2.0 exported (48 screens).

---

## Stage 2: IDENTIFY (Done for Brainwave)

**Script:** `enterprise-os-hub/scripts/identify-screens-gemini.js`

- Input: Directory of PNG screens
- Process: Each PNG → Gemini 2.0 Flash → structured JSON
- Output: `component_inventory.json` per kit
- Cost: ~$0.001/image. ~$0.05 per kit. ~$2 for all 38 kits.
- Checkpoints after every screen. Resume-safe.

**Per-screen output structure:**
```json
{
  "screen_slug": "filename",
  "screen_name": "Human readable name",
  "screen_type": "full_page | modal | overlay | state_variant",
  "layout": {
    "type": "sidebar_content | split | centered | full_canvas | grid",
    "has_sidebar": true,
    "sidebar_style": "expanded | collapsed | none",
    "has_topbar": true,
    "has_footer": false
  },
  "components": [
    {
      "type": "sidebar | card | button | input | modal | table | ...",
      "name": "descriptive name",
      "location": "left | right | top | center | bottom | overlay",
      "approximate_dimensions": "WxH",
      "details": "visual details",
      "reusable": true,
      "reuse_category": "navigation | data_display | input | feedback | layout | action | overlay"
    }
  ],
  "color_palette": ["#hex1", "#hex2"],
  "primary_purpose": "what this screen is for",
  "enterprise_os_potential": "how this layout could be reused"
}
```

**Status:** Working. Brainwave 2.0 identified (48 screens, 411KB inventory data). User will run Gemini for remaining 37 kits.

---

## Stage 3: STRUCTURE — The Inventory Database

### 4-Level Hierarchy

```
PAGES (full screen layouts)
  └── BOILERPLATES (reusable page templates — dashboard, settings, auth, etc.)
       └── BLOCKS (sections — hero, pricing grid, feature list, sidebar nav, etc.)
            └── COMPONENTS (atomic — button, card, input, avatar, badge, etc.)
```

### Tagging System

Every item at every level gets tagged with:
- **Source kit** — which of the 38 kits it came from
- **Page associations** — which PRD pages/screens it maps to
- **Reuse category** — navigation, data_display, input, feedback, layout, action, overlay
- **Layout context** — where it sits (sidebar, topbar, main content, overlay)
- **Screen type** — full_page, modal, overlay, state_variant
- **Domain fitness** — which projects it fits (Property, Fitness, LeadEngine, etc.)

### Database Schema (PostgreSQL — extends existing `ui_library`)

```sql
-- Extends the existing ui_library database (19,837 items, 183 kits)

CREATE TABLE inventory_screens (
  id SERIAL PRIMARY KEY,
  kit_id INTEGER REFERENCES kits(id),
  screen_slug TEXT NOT NULL,
  screen_name TEXT,
  screen_type TEXT,          -- full_page, modal, overlay, state_variant
  hierarchy_level TEXT,      -- page, boilerplate, block
  layout_type TEXT,          -- sidebar_content, split, centered, full_canvas, grid
  has_sidebar BOOLEAN,
  sidebar_style TEXT,
  has_topbar BOOLEAN,
  has_footer BOOLEAN,
  color_palette JSONB,
  typography_notes TEXT,
  primary_purpose TEXT,
  enterprise_os_potential TEXT,
  figma_frame_id TEXT,       -- link back to Figma for extraction
  figma_file_key TEXT,
  png_path TEXT,             -- local path to exported PNG
  ai_confidence FLOAT,      -- how confident the AI was in identification
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE inventory_components (
  id SERIAL PRIMARY KEY,
  screen_id INTEGER REFERENCES inventory_screens(id),
  component_type TEXT NOT NULL,  -- sidebar, card, button, input, modal, table...
  component_name TEXT,
  location TEXT,             -- left, right, top, center, bottom, overlay
  approximate_dimensions TEXT,
  details TEXT,              -- visual details from AI
  reusable BOOLEAN,
  reuse_category TEXT,       -- navigation, data_display, input, feedback, layout, action, overlay
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE prd_screen_mapping (
  id SERIAL PRIMARY KEY,
  prd_screen_name TEXT NOT NULL,     -- e.g. "Dashboard Overview"
  prd_screen_path TEXT,              -- e.g. "/dashboard"
  prd_features JSONB,               -- features/elements this screen needs
  matched_screen_ids INTEGER[],     -- inventory_screens that match
  matched_component_ids INTEGER[],  -- inventory_components that match
  match_confidence FLOAT,
  project TEXT,                     -- which project PRD this is from
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for fast cross-referencing
CREATE INDEX idx_screens_kit ON inventory_screens(kit_id);
CREATE INDEX idx_screens_type ON inventory_screens(screen_type);
CREATE INDEX idx_screens_layout ON inventory_screens(layout_type);
CREATE INDEX idx_components_type ON inventory_components(component_type);
CREATE INDEX idx_components_reuse ON inventory_components(reuse_category);
CREATE INDEX idx_prd_project ON prd_screen_mapping(project);
```

---

## Stage 4: MATCH — PRD Cross-Reference

### How It Works

1. **Parse PRD** — Extract every screen, subpage, tab, popup, sidebar, menu structure, feature, layout requirement (masonry, grids, cards, etc.)
2. **Query inventory** — For each PRD screen, find matching pages/boilerplates/blocks/components by:
   - Screen type match (dashboard → dashboard layouts)
   - Component requirements (needs sidebar + table + chart → find screens with those)
   - Layout match (sidebar_content, grid, etc.)
   - Domain fitness (property screens for property project)
3. **Rank matches** — Score each match by how many requirements it satisfies
4. **Output mapping** — PRD screen → best matching inventory items with confidence scores

### PRD Input Format

The LLM needs a PRD that specifies for each screen:
- Page name and route
- Page type (dashboard, form, list, detail, settings, auth, landing)
- Required components (sidebar, topbar, cards, tables, charts, modals, etc.)
- Layout preference (sidebar+content, full-width, centered, grid)
- Key features (search, filters, pagination, real-time updates, etc.)
- Nested elements (tabs, accordions, popups, sub-menus)

### Example Match

```
PRD Screen: "Lead Dashboard"
  Needs: sidebar_content layout, data table, stat cards, line chart, filters

  MATCHES:
  1. Brainwave > CRM Dashboard (92% match) — has sidebar, cards, table, chart
  2. Square Dashboard > Analytics (78% match) — has cards, charts, table
  3. Huose Property > Lead Board (85% match) — domain fit, has cards, filters
```

---

## Stage 5: EXTRACT — Figma to React

### Approach Options (in priority order)

1. **AI-Assisted Code Generation**
   - Feed the PNG + component inventory to an LLM
   - LLM generates React/Tailwind components matching the visual design
   - Cheapest, most flexible, handles any kit
   - Tools: Claude API, GPT-4o, Gemini Pro

2. **Figma Plugin Export**
   - Locofy.ai — Figma to React with Tailwind
   - Anima — Figma to React
   - Requires Figma plugin access per kit

3. **Figma Dev Mode API**
   - Extract CSS properties, spacing, colors via Figma API
   - Build component code from extracted properties
   - Most accurate but most engineering effort

### Component Output Structure

```
src/components/kit/{kit_name}/
  ├── pages/           # Full page layouts
  ├── boilerplates/    # Reusable page templates
  ├── blocks/          # Section-level components
  └── atoms/           # Individual components (button, card, input)
```

Each component includes:
- React TSX file
- Tailwind styles (or CSS module)
- Props interface
- Storybook story
- Source attribution (kit name, screen slug, Figma frame ID)

---

## Stage 6: ASSEMBLE — Canvas Page Builder

### How It Works

1. **Start with boilerplate** — Select the best-matching page template from inventory
2. **Inject blocks** — Replace placeholder sections with matched blocks
3. **Swap components** — Replace individual components based on PRD requirements
4. **Apply theme** — Override colors/fonts with project brand (e.g., #0B8C00 for Enterprise OS)
5. **Generate routes** — Wire up pages into Next.js app router structure

### Canvas System

- **Tech:** React + drag-and-drop (react-dnd or Fabric.js for visual editor)
- **Layout engine:** CSS Grid / Flexbox templates matching inventory layouts
- **Component slots:** Named slots in boilerplates that accept specific component types
- **Preview:** Live render of assembled page
- **Export:** Generate final React page files

### Assembly Flow

```
PRD Screen Definition
  → Match to inventory (Stage 4)
  → Load boilerplate React component
  → Inject matched blocks into slots
  → Swap atomic components
  → Apply project theme
  → Preview on canvas
  → Export as page file
  → Wire into Next.js routes
```

---

## Current Progress

| Stage | Status | Next Action |
|-------|--------|-------------|
| 1. Export | Brainwave done (48 screens) | User runs for remaining 37 kits |
| 2. Identify | Brainwave done (48 screens) | User runs Gemini for remaining 37 kits |
| 3. Structure | Schema designed | Import Brainwave inventory into PostgreSQL |
| 4. Match | Spec defined | Build PRD parser + matching engine |
| 5. Extract | Approaches identified | Prototype AI code gen on 5 components |
| 6. Assemble | Spec defined | Build canvas prototype |

---

## Scripts & Tools

| Script | Purpose | Location |
|--------|---------|----------|
| `export-figma-screens.js` | Export Figma frames as PNGs | `enterprise-os-hub/scripts/` |
| `identify-screens-gemini.js` | AI vision identification via Gemini Flash | `enterprise-os-hub/scripts/` |
| (TODO) `import-inventory-db.js` | Import JSON inventory into PostgreSQL | `enterprise-os-hub/scripts/` |
| (TODO) `parse-prd.js` | Extract screen definitions from PRD | `enterprise-os-hub/scripts/` |
| (TODO) `match-components.js` | Cross-reference PRD against inventory | `enterprise-os-hub/scripts/` |
| (TODO) `generate-react.js` | AI-assisted React component generation | `enterprise-os-hub/scripts/` |

---

## Key Numbers

- **38 UI kits** in KIT_INDEX.json
- **7,683 total items** across all kits
- **4,464 screen-level items** available for inventory
- **19,837 items** already in PostgreSQL ui_library database
- **48 Brainwave screens** identified (first kit complete)
- **47 Enterprise OS screens** in PRD (first project to match)
- **~$2 total** Gemini Flash cost to identify all 38 kits
