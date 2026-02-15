# DESIGN WORKBENCH & DAM — Build Spec
> Created: 2026-02-15 | Build: Tomorrow (2026-02-16)
> Purpose: Internal tool to mock up all 94 LeadEngine screens fast. Refine and sell later.

---

## WHAT THIS IS

A browser-based design workbench that lets you:
1. Browse UI kit components from PostgreSQL (38 kits, 19,837 items)
2. Render chosen components full-size via Figma API (SVG/PNG)
3. Drop onto a Fabric.js canvas
4. Edit colours, fonts, text, images
5. Have AI auto-generate copy per screen
6. Export as PNG mockup + JSON spec
7. Manage all images/videos in a simple DAM

---

## LAYER 1: DESIGN WORKBENCH MVP (Tomorrow Morning)

### Tech Stack
- **Canvas**: Fabric.js (free, open source, React-compatible)
- **Component Browser**: React UI querying PostgreSQL `ui_library` (existing DB)
- **Rendering**: Figma API → SVG/PNG export per frame
- **AI Copy**: Claude API generates text based on screen context
- **Frontend**: React + Brainwave shell
- **Backend**: Express or Next.js API routes

### Features (MVP)
| Feature | Description |
|---------|-------------|
| Component Browser | Search/filter by category, kit, page type. Shows thumbnails from DB. |
| Full Render | Click component → Figma API exports as SVG → loads on canvas |
| Canvas Editor | Move, resize, select objects. Fabric.js handles all manipulation. |
| Text Editing | Click any text on canvas → edit inline. Change font, size, colour. |
| Colour Override | Global colour swap (e.g. replace kit's blue with #0B8C00) |
| Image Swap | Click image placeholder → browse DAM → replace |
| AI Copy Fill | Select text block → "Generate copy" → Claude writes contextual copy |
| Export PNG | Export canvas as high-res PNG mockup |
| Save Composition | Save as JSON (kit source, colours, text, images, positions) |
| Load Composition | Reload saved JSON to continue editing |

### Component Browser Queries
```sql
-- Dashboard screens
SELECT * FROM component_library
WHERE llm_category = 'dashboard' AND width > 1200
ORDER BY file_key IN (target_kit_keys) DESC, width DESC;

-- AI chat interfaces
SELECT * FROM component_library
WHERE (llm_category IN ('forms', 'modals') OR search_text ILIKE '%chat%')
AND width > 800;

-- Landing page heroes
SELECT * FROM component_library
WHERE llm_category = 'hero' AND width > 1200;
```

### Kit-to-Screen Mapping (42 app screens)
For each LeadEngine screen, the workbench pre-filters to relevant kits:

| Screen | Categories | Primary Kits |
|--------|-----------|-------------|
| S.1 Dashboard/Home | dashboard | Brainwave, Square Dashboard, Huose Property |
| 1.1 Concierge Widget | forms, modals | Source Fusion AI, Triply AI |
| 1.2 Knowledge Base Manager | forms, content | Untitled UI Pro, Source Fusion AI |
| 1.3 Personality Config | forms | Untitled UI Pro, Brainwave |
| 1.4 Conversation History | tables, content | Square Dashboard, Untitled UI Pro |
| 1.5 Conversation Detail | content, profile | Untitled UI Pro, Source Fusion AI |
| 1.6 Concierge Analytics | dashboard | Square Dashboard, Zip Formate |
| 2.1 Live Visitors | dashboard | Brainwave, Square Dashboard |
| 2.2 Visitor List | tables | Square Dashboard, Untitled UI Pro |
| 2.3 Visitor Timeline | content, profile | Untitled UI Pro, Fleet Travel |
| 2.4 Company ID | tables, cards | Fleet Travel, Finder |
| 3.1 Lead List | tables | Square Dashboard, Untitled UI Pro |
| 3.2 Lead Detail | profile, content | Untitled UI Pro, Huose Property |
| 3.3 Progressive Profile Config | forms | Untitled UI Pro, Strivo |
| 3.4 Smart Forms Builder | forms | Untitled UI Pro, Source Fusion AI |
| 3.5 Scoring Rules | forms, dashboard | Untitled UI Pro, Square Dashboard |
| 4.1 Routing Rules | forms | Untitled UI Pro, Source Fusion AI |
| 4.2 Team Management | tables, profile | Untitled UI Pro, Square Dashboard |
| 4.3 Notification Config | forms | Untitled UI Pro, Brainwave |
| 4.4 Assignment Dashboard | dashboard, cards | Brainwave, Huose Property |
| 4.5 SLA Monitor | dashboard | Square Dashboard, Zip Formate |
| 5.1 Funnel Overview | dashboard | Square Dashboard, Zip Formate |
| 5.2 Page Performance | tables, dashboard | Square Dashboard, Untitled UI Pro |
| 5.3 Traffic Source ROI | dashboard | Square Dashboard, Zip Formate |
| 5.4 Content Gap Analysis | content, tables | Untitled UI Pro, Square Dashboard |
| 5.5 Drop-off Analysis | dashboard | Square Dashboard, Brainwave |
| 5.6 Weekly Report | content, dashboard | Untitled UI Pro, Briefberry |
| 6.1 Sequence Builder | forms, dashboard | Source Fusion AI, Untitled UI Pro |
| 6.2 Trigger Config | forms | Untitled UI Pro, Source Fusion AI |
| 6.3 Template Library | cards, content | Fleet Travel, Untitled UI Pro |
| 6.4 Sequence Performance | dashboard | Square Dashboard, Zip Formate |
| 6.5 A/B Testing | dashboard, forms | Square Dashboard, Untitled UI Pro |
| S.2 Onboarding Wizard | forms | Strivo, Briefberry, Untitled UI Pro |
| S.3 Settings | forms | Untitled UI Pro, Brainwave |
| S.4 Integration Hub | cards | Fleet Travel, Untitled UI Pro |
| S.5 Pixel Installation | content | Untitled UI Pro, Source Fusion AI |
| S.6 Auth Screens | auth | Square Dashboard, Untitled UI Pro |
| S.7 API & Developer | content, tables | Untitled UI Pro, Source Fusion AI |

### Marketing screens (18)
| Screen | Categories | Primary Kits |
|--------|-----------|-------------|
| M.1 Landing Page | hero, features, cta | Chroma, Multi-concept Landing |
| M.2 Features Page | features, content | Chroma, Fleet Travel |
| M.3 Pricing Page | pricing | Untitled UI Pro, Chroma |
| M.4 For Estate Agents | hero, content | Chroma, Huose Property |
| M.5 For Home & Retail | hero, content | Chroma, eCommerce UI Kit |
| M.6 ROI Calculator | forms, dashboard | Untitled UI Pro, Square Dashboard |
| M.7 Demo / Book a Call | forms, content | Chroma, Briefberry |
| M.8 Webinar Registration | forms, hero | Chroma, Briefberry |
| M.9 About / Trust | content | Chroma, Align |
| M.10 FAQ | content | Chroma, Untitled UI Pro |
| W.1 Webinar Deck | content | Chroma, Majin |
| W.3 Replay Page | content, media | Chroma, Video Streaming Web |
| SA.1 One-Pager | content | Chroma, Majin |
| SA.2 Proposal Template | content, forms | Untitled UI Pro, Chroma |

---

## LAYER 2: SIMPLE DAM (Tomorrow Afternoon)

### Tech Stack
- **Storage**: Local filesystem (S3 later)
- **Metadata**: PostgreSQL `assets` table
- **Thumbnails**: Sharp.js on upload (resize to 400px wide)
- **Search**: PostgreSQL full-text on tags + name
- **UI**: Grid view with lazy loading, upload dropzone

### Schema
```sql
CREATE TABLE assets (
    id SERIAL PRIMARY KEY,
    filename TEXT NOT NULL,
    original_name TEXT NOT NULL,
    mime_type TEXT NOT NULL,
    size_bytes INT,
    width INT,
    height INT,
    duration_seconds FLOAT,  -- for video
    storage_path TEXT NOT NULL,
    thumbnail_path TEXT,
    tags TEXT[],
    category TEXT,  -- image, video, document, font, icon
    project TEXT,   -- leadengine, fitness, pcl, enterprise
    brand TEXT,     -- which brand/client
    uploaded_at TIMESTAMP DEFAULT NOW(),
    search_vector TSVECTOR
);

CREATE INDEX idx_assets_tags ON assets USING GIN(tags);
CREATE INDEX idx_assets_search ON assets USING GIN(search_vector);
CREATE INDEX idx_assets_category ON assets(category);
CREATE INDEX idx_assets_project ON assets(project);
```

### Features (MVP)
| Feature | Implementation |
|---------|---------------|
| Upload | Drag-drop zone, multi-file, progress bar |
| Auto-thumbnail | Sharp.js resize on upload |
| Tag on upload | Tag input field, suggest from existing tags |
| Browse | Grid view, filter by category/project/tags |
| Search | Full-text search on name + tags |
| Preview | Lightbox for images, video player for video |
| Select for canvas | Click → sends to workbench canvas |
| Folder structure | Virtual folders via `project` + `category` |

---

## LAYER 3: FUTURE — SELLABLE DESIGN PLATFORM

For later refinement as part of PropertyConnect.London suite:

### Upgrade Path
| Current (MVP) | Future (Sellable) |
|--------------|-------------------|
| Fabric.js canvas | GrapesJS page builder (outputs HTML/CSS) |
| Local file storage | S3 + CDN (ImageKit or Cloudinary) |
| Manual colour edit | Brand kit system (colours, fonts, logos per client) |
| Claude copy for one screen | Template-based copy generation for entire sites |
| PNG export | React component export (Figma → React pipeline) |
| Single user | Multi-user with permissions |
| No versioning | Version history + undo |
| No templates | Template marketplace |

### Sellable Features
- White-label design editor for agencies
- Client brand kit management
- AI copy generation by context
- Component library marketplace
- Template system (save compositions as reusable templates)
- Video library with AI tagging
- Image transformation API (resize, crop, format via URL)
- Collaboration (comments, approvals)

---

## TOMORROW'S SCHEDULE

| Time | Task | Output |
|------|------|--------|
| AM Block 1 (2hrs) | Fabric.js canvas + component browser UI | Working canvas with kit browsing |
| AM Block 2 (2hrs) | Figma API SVG rendering + canvas loading | Click component → renders on canvas |
| PM Block 1 (2hrs) | DAM: upload, browse, search, thumbnails | Working asset library |
| PM Block 2 (2hrs) | Text editing + colour swap + AI copy + export | Full workbench MVP functional |
| Evening | Start rendering LeadEngine screens | First 10-15 screen mockups |

---

## CONNECTIONS

- Uses: PostgreSQL `ui_library` (existing), Figma API token, Claude API
- Feeds into: LeadEngine build sprint (provides mockups for all 94 screens)
- Later becomes: Part of PropertyConnect.London design suite
- Kit selections: Per BOILERPLATE_SELECTIONS.md
