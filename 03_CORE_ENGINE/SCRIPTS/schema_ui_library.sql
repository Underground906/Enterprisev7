-- UI Library Schema v2 - from monday_plan_v2.md
-- Drop old tables if they exist and recreate fresh

-- ============================================================
-- TAXONOMY DIMENSIONS (the classification system)
-- ============================================================

DROP TABLE IF EXISTS platform_collections CASCADE;
DROP TABLE IF EXISTS assembly_plans CASCADE;
DROP TABLE IF EXISTS graphic_slots CASCADE;
DROP TABLE IF EXISTS copy_slots CASCADE;
DROP TABLE IF EXISTS page_archetypes CASCADE;
DROP TABLE IF EXISTS video_library CASCADE;
DROP TABLE IF EXISTS assets_library CASCADE;
DROP TABLE IF EXISTS platform_captures CASCADE;
DROP TABLE IF EXISTS platform_registry CASCADE;
DROP TABLE IF EXISTS design_tokens CASCADE;
DROP TABLE IF EXISTS brand_systems CASCADE;
DROP TABLE IF EXISTS kits CASCADE;
DROP TABLE IF EXISTS component_library CASCADE;
DROP TABLE IF EXISTS components_raw CASCADE;
DROP TABLE IF EXISTS component_names CASCADE;
DROP TABLE IF EXISTS component_type_subsections CASCADE;
DROP TABLE IF EXISTS component_type_sections CASCADE;
DROP TABLE IF EXISTS component_types CASCADE;
DROP TABLE IF EXISTS industry_verticals CASCADE;
DROP TABLE IF EXISTS functional_categories CASCADE;
DROP TABLE IF EXISTS image_specs CASCADE;

-- Component Types: what a component IS (from naming convention docs)
CREATE TABLE component_types (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    sort_order INTEGER,
    section_count INTEGER,
    total_component_names INTEGER
);

-- Sections within component types
CREATE TABLE component_type_sections (
    id TEXT PRIMARY KEY,
    component_type_id TEXT REFERENCES component_types(id),
    name TEXT NOT NULL,
    sort_order INTEGER,
    direct_component_count INTEGER,
    subsection_count INTEGER
);

-- Subsections within sections
CREATE TABLE component_type_subsections (
    id TEXT PRIMARY KEY,
    section_id TEXT REFERENCES component_type_sections(id),
    component_type_id TEXT REFERENCES component_types(id),
    name TEXT NOT NULL,
    sort_order INTEGER,
    component_count INTEGER
);

-- Canonical component names (~12,464 naming conventions)
CREATE TABLE component_names (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    component_type_id TEXT REFERENCES component_types(id),
    section_id TEXT REFERENCES component_type_sections(id),
    subsection_id TEXT,
    has_suffix BOOLEAN DEFAULT FALSE,
    suffix_type TEXT,
    base_name TEXT
);

-- Functional Categories: what PAGE PURPOSE (from PRD)
CREATE TABLE functional_categories (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    example_pages TEXT[],
    sort_order INTEGER
);

-- Industry Verticals: what NICHE (from PRD)
CREATE TABLE industry_verticals (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    specialized_pages TEXT[],
    sort_order INTEGER
);

-- ============================================================
-- CORE LIBRARY (the actual scraped/indexed items)
-- ============================================================

-- Raw Figma extraction data
CREATE TABLE components_raw (
    id TEXT PRIMARY KEY,
    figma_node_id TEXT,
    parent_id TEXT,
    raw_json JSONB,
    image_path TEXT,
    thumbnail_url TEXT,
    bounds JSONB,
    child_count INTEGER,
    source_file TEXT,
    file_key TEXT,
    file_name TEXT,
    page_name TEXT,
    project_name TEXT,
    width INTEGER,
    height INTEGER,
    extracted_at TIMESTAMP DEFAULT NOW()
);

-- Classified, searchable library (main query table)
CREATE TABLE component_library (
    id TEXT PRIMARY KEY,
    raw_id TEXT REFERENCES components_raw(id),
    name TEXT NOT NULL,

    -- Multi-dimensional classification
    component_type_id TEXT REFERENCES component_types(id),
    section_id TEXT,
    subsection_id TEXT,
    functional_category_id TEXT REFERENCES functional_categories(id),
    industry_vertical_id TEXT,
    component_level TEXT CHECK (component_level IN ('page', 'block', 'component', 'atom')),
    device_type TEXT CHECK (device_type IN ('desktop', 'tablet', 'mobile', 'responsive')),

    -- Patterns
    primary_pattern TEXT,
    layout_signature TEXT,
    interaction_capabilities TEXT[],
    variants JSONB,
    confidence_score DECIMAL(3,2),

    -- Search and discovery
    tags TEXT[],
    search_text TEXT,

    -- Thumbnail and visual
    thumbnail_path TEXT,
    thumbnail_url TEXT,
    width INTEGER,
    height INTEGER,

    -- Source kit metadata
    file_key TEXT,
    file_name TEXT,
    page_name TEXT,
    project_name TEXT,

    -- Niche
    niche TEXT,
    niche_tags TEXT[],
    niche_specific BOOLEAN DEFAULT FALSE,

    -- Suffix tracking
    has_variant_suffixes BOOLEAN DEFAULT FALSE,
    variant_suffixes TEXT[],

    -- Curation and workflow status
    review_status TEXT DEFAULT 'unreviewed' CHECK (review_status IN ('unreviewed', 'kept', 'discarded', 'flagged')),
    quality_rating INTEGER CHECK (quality_rating BETWEEN 1 AND 5),
    brand_applied BOOLEAN DEFAULT FALSE,
    storybook_ready BOOLEAN DEFAULT FALSE,
    react_converted BOOLEAN DEFAULT FALSE,
    matched_component_name_id INTEGER,

    -- LLM classification from earlier pass
    llm_category TEXT,
    llm_subcategory TEXT,

    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- ============================================================
-- KIT-LEVEL METADATA
-- ============================================================

CREATE TABLE kits (
    file_key TEXT PRIMARY KEY,
    file_name TEXT NOT NULL,
    project_name TEXT,
    niche TEXT,
    niche_tags TEXT[],
    style_keywords TEXT[],
    density TEXT,
    item_count INTEGER,
    quality_rating INTEGER CHECK (quality_rating BETWEEN 1 AND 5),
    is_niche_specific BOOLEAN DEFAULT FALSE
);

-- ============================================================
-- DESIGN TOKENS
-- ============================================================

CREATE TABLE design_tokens (
    id TEXT PRIMARY KEY,
    layer TEXT CHECK (layer IN ('global', 'semantic', 'component')),
    category TEXT NOT NULL,
    subcategory TEXT,
    name TEXT NOT NULL,
    value TEXT NOT NULL,
    semantic_role TEXT,
    component_scope TEXT,
    kit_source TEXT,
    usage_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE brand_systems (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    brand_id TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    color_tokens JSONB,
    typography JSONB,
    spacing_scale JSONB,
    border_tokens JSONB,
    shadow_tokens JSONB,
    icon_style JSONB,
    illustration_style JSONB,
    photography_style JSONB,
    motion_patterns JSONB,
    tailwind_config JSONB,
    css_variables TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- ============================================================
-- IMAGE SPECS
-- ============================================================

CREATE TABLE image_specs (
    id TEXT PRIMARY KEY,
    slot_type TEXT NOT NULL,
    width INTEGER NOT NULL,
    height INTEGER NOT NULL,
    format TEXT NOT NULL,
    purpose TEXT
);

INSERT INTO image_specs VALUES
    ('library-thumbnail', 'Library Thumbnail', 800, 600, 'png/webp', 'Browse gallery preview'),
    ('hero-visual', 'Hero Visual', 1440, 800, 'png/svg', 'Primary page hero image'),
    ('section-background', 'Section Background', 1920, 1080, 'png/jpg', 'Full-width backgrounds'),
    ('product-screenshot', 'Product Screenshot', 1200, 800, 'png', 'App/dashboard mockups'),
    ('icon-24', 'Icon Set 24', 24, 24, 'svg', 'UI icons'),
    ('icon-32', 'Icon Set 32', 32, 32, 'svg', 'UI icons'),
    ('icon-48', 'Icon Set 48', 48, 48, 'svg', 'UI icons'),
    ('icon-64', 'Icon Set 64', 64, 64, 'svg', 'UI icons'),
    ('illustration-flat', 'Illustration (Flat)', 600, 400, 'svg/png', 'Feature illustrations'),
    ('illustration-iso', 'Illustration (Isometric)', 800, 600, 'svg/png', 'Complex visuals'),
    ('avatar', 'Avatar/Profile', 128, 128, 'png/jpg', 'User placeholders'),
    ('logo-mark', 'Logo Mark', 64, 64, 'svg', 'Brand logos'),
    ('logo-full', 'Logo Full', 200, 60, 'svg', 'Header logos'),
    ('card-image', 'Card Image', 400, 300, 'png/jpg/webp', 'Content cards'),
    ('chart-dataviz', 'Chart/Data Viz', 600, 400, 'svg/png', 'Dashboard charts'),
    ('video-thumbnail', 'Video Thumbnail', 1280, 720, 'jpg/png', 'Video previews'),
    ('og-social', 'OG/Social Image', 1200, 630, 'png/jpg', 'Social sharing');

-- ============================================================
-- INDEXES
-- ============================================================

CREATE INDEX idx_library_search ON component_library USING gin(to_tsvector('english', search_text));
CREATE INDEX idx_library_name ON component_library USING gin(to_tsvector('english', name));
CREATE INDEX idx_library_type ON component_library(component_type_id);
CREATE INDEX idx_library_functional ON component_library(functional_category_id);
CREATE INDEX idx_library_vertical ON component_library(industry_vertical_id);
CREATE INDEX idx_library_level ON component_library(component_level);
CREATE INDEX idx_library_device ON component_library(device_type);
CREATE INDEX idx_library_niche ON component_library(niche);
CREATE INDEX idx_library_review ON component_library(review_status);
CREATE INDEX idx_library_file ON component_library(file_key);
CREATE INDEX idx_library_section ON component_library(section_id);
CREATE INDEX idx_library_subsection ON component_library(subsection_id);
CREATE INDEX idx_library_llm_cat ON component_library(llm_category);
CREATE INDEX idx_library_llm_subcat ON component_library(llm_subcategory);

CREATE INDEX idx_names_type ON component_names(component_type_id);
CREATE INDEX idx_names_section ON component_names(section_id);
CREATE INDEX idx_names_text ON component_names USING gin(to_tsvector('english', name));

CREATE INDEX idx_library_tags ON component_library USING gin(tags);
CREATE INDEX idx_library_niche_tags ON component_library USING gin(niche_tags);

CREATE INDEX idx_tokens_category ON design_tokens(category);
CREATE INDEX idx_tokens_layer ON design_tokens(layer);
CREATE INDEX idx_tokens_kit ON design_tokens(kit_source);

-- Done
SELECT 'Schema created successfully' as status;
