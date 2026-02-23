-- ============================================================
-- Enterprise OS V7 — System Registry Schema
-- Database: enterprise_os (PostgreSQL)
-- Created: 2026-02-17
--
-- 5 tables for file tracking, session management, audit trail,
-- external source inventory, and system state snapshots.
--
-- Usage:
--   psql -U postgres -d enterprise_os -f v7_registry.sql
--
-- NOTE: Does NOT touch the ui_library database.
-- ============================================================

-- ============================================================
-- TABLE 1: v7_files — Master file registry
-- Every file in ENTERPRISE_OS_V7 gets a row here.
-- ============================================================

CREATE TABLE IF NOT EXISTS v7_files (
    id              SERIAL PRIMARY KEY,
    relative_path   TEXT NOT NULL UNIQUE,
    filename        TEXT NOT NULL,
    extension       TEXT,

    -- Classification
    component       TEXT,           -- Top-level: SYSTEM_ROOT, CORE_ENGINE, etc.
    pillar          TEXT,           -- PIL_01_AVATARS through PIL_23_DOG_PLATFORM
    project         TEXT,           -- PRJ_* project name if applicable
    file_type       TEXT,           -- context_doc, script, data, document, etc.

    -- Content metadata
    content_hash    TEXT,           -- SHA-256 of file contents
    size_bytes      BIGINT,
    line_count      INTEGER,
    word_count      INTEGER,
    title           TEXT,           -- First # heading from markdown
    summary         TEXT,           -- First 500 chars of content

    -- Timestamps
    file_modified   TIMESTAMP WITH TIME ZONE,
    first_seen      TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_scanned    TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Status
    is_deleted      BOOLEAN DEFAULT FALSE,
    deleted_at      TIMESTAMP WITH TIME ZONE
);

CREATE INDEX IF NOT EXISTS idx_v7_files_component ON v7_files(component);
CREATE INDEX IF NOT EXISTS idx_v7_files_pillar ON v7_files(pillar);
CREATE INDEX IF NOT EXISTS idx_v7_files_project ON v7_files(project);
CREATE INDEX IF NOT EXISTS idx_v7_files_file_type ON v7_files(file_type);
CREATE INDEX IF NOT EXISTS idx_v7_files_hash ON v7_files(content_hash);
CREATE INDEX IF NOT EXISTS idx_v7_files_extension ON v7_files(extension);
CREATE INDEX IF NOT EXISTS idx_v7_files_search ON v7_files USING gin(to_tsvector('english', COALESCE(title, '') || ' ' || COALESCE(filename, '')));


-- ============================================================
-- TABLE 2: v7_sessions — Session tracking
-- One row per work session (start/end).
-- ============================================================

CREATE TABLE IF NOT EXISTS v7_sessions (
    id              SERIAL PRIMARY KEY,
    date            DATE NOT NULL,
    session_number  INTEGER NOT NULL,
    description     TEXT NOT NULL,

    -- Timing
    started_at      TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    ended_at        TIMESTAMP WITH TIME ZONE,

    -- Stats (populated on session end)
    files_created   INTEGER DEFAULT 0,
    files_modified  INTEGER DEFAULT 0,
    files_deleted   INTEGER DEFAULT 0,
    log_entries     INTEGER DEFAULT 0,

    -- References
    log_path        TEXT,           -- Path to markdown session log
    next_steps      TEXT,           -- Captured on session end

    -- Status
    status          TEXT DEFAULT 'active' CHECK (status IN ('active', 'complete', 'abandoned')),

    UNIQUE(date, session_number)
);

CREATE INDEX IF NOT EXISTS idx_v7_sessions_date ON v7_sessions(date);
CREATE INDEX IF NOT EXISTS idx_v7_sessions_status ON v7_sessions(status);


-- ============================================================
-- TABLE 3: v7_changes — Audit trail
-- Every file create/modify/delete logged here.
-- ============================================================

CREATE TABLE IF NOT EXISTS v7_changes (
    id              SERIAL PRIMARY KEY,
    session_id      INTEGER REFERENCES v7_sessions(id),
    file_id         INTEGER REFERENCES v7_files(id),
    relative_path   TEXT NOT NULL,

    -- What changed
    change_type     TEXT NOT NULL CHECK (change_type IN ('created', 'modified', 'deleted', 'renamed')),
    old_hash        TEXT,
    new_hash        TEXT,
    old_size        BIGINT,
    new_size        BIGINT,

    -- Context
    description     TEXT,
    detected_by     TEXT DEFAULT 'scan',  -- 'scan', 'manual', 'session_log'

    -- Timestamp
    changed_at      TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_v7_changes_session ON v7_changes(session_id);
CREATE INDEX IF NOT EXISTS idx_v7_changes_file ON v7_changes(file_id);
CREATE INDEX IF NOT EXISTS idx_v7_changes_type ON v7_changes(change_type);
CREATE INDEX IF NOT EXISTS idx_v7_changes_time ON v7_changes(changed_at);


-- ============================================================
-- TABLE 4: v7_external_sources — Scattered file inventory
-- Tracks files outside V7 that need consolidation.
-- ============================================================

CREATE TABLE IF NOT EXISTS v7_external_sources (
    id              SERIAL PRIMARY KEY,
    source_path     TEXT NOT NULL,
    filename        TEXT NOT NULL,
    extension       TEXT,

    -- Grouping
    source_group    TEXT NOT NULL,   -- 'notebook', 'legacy', 'fitness', 'property', 'collective', 'missing'

    -- Content
    content_hash    TEXT,
    size_bytes      BIGINT,

    -- Consolidation status
    status          TEXT DEFAULT 'inventoried' CHECK (status IN (
                        'inventoried', 'duplicate', 'planned', 'approved', 'moved', 'skipped'
                    )),
    target_path     TEXT,           -- Where it should go in V7
    duplicate_of    INTEGER REFERENCES v7_files(id),

    -- Timestamps
    discovered_at   TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    processed_at    TIMESTAMP WITH TIME ZONE
);

CREATE INDEX IF NOT EXISTS idx_v7_external_group ON v7_external_sources(source_group);
CREATE INDEX IF NOT EXISTS idx_v7_external_status ON v7_external_sources(status);
CREATE INDEX IF NOT EXISTS idx_v7_external_hash ON v7_external_sources(content_hash);


-- ============================================================
-- TABLE 5: v7_system_state — Daily snapshots
-- Captures system metrics over time for trend tracking.
-- ============================================================

CREATE TABLE IF NOT EXISTS v7_system_state (
    id              SERIAL PRIMARY KEY,
    snapshot_date   DATE NOT NULL,
    snapshot_time   TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Counts
    total_files     INTEGER NOT NULL,
    total_size_mb   DECIMAL(10,2),

    -- Breakdown (stored as JSONB for flexibility)
    files_by_component  JSONB,      -- {"CORE_ENGINE": 42, "BUILD_FACTORY": 15, ...}
    files_by_type       JSONB,      -- {"document": 30, "script": 12, ...}
    files_by_pillar     JSONB,      -- {"PIL_01_AVATARS": 0, "PIL_02_BRANDING": 3, ...}

    -- Health indicators
    empty_pillars       INTEGER,
    stale_files         INTEGER,    -- Files not modified in 30+ days
    empty_directories   INTEGER,

    -- Session context
    session_id          INTEGER REFERENCES v7_sessions(id),
    triggered_by        TEXT DEFAULT 'manual'  -- 'daily', 'session_end', 'manual'
);

CREATE INDEX IF NOT EXISTS idx_v7_state_date ON v7_system_state(snapshot_date);


-- ============================================================
-- TABLE 6: v7_extractions — Extraction tracking
-- Every extraction pass run on any file gets a row here.
-- Supports search by: mode, pillar, project, date, category.
-- ============================================================

CREATE TABLE IF NOT EXISTS v7_extractions (
    id              SERIAL PRIMARY KEY,
    source_file     TEXT NOT NULL,           -- Relative path to source file
    mode            TEXT NOT NULL,           -- domains, thread, copy, book
    api_used        TEXT DEFAULT 'deepseek', -- deepseek, claude

    -- Classification
    pillar          TEXT,                    -- PIL_01_AVATARS through PIL_23_DOG_PLATFORM
    project         TEXT,                    -- PRJ_* project name if applicable

    -- Results
    item_count      INTEGER DEFAULT 0,      -- Total items extracted
    categories_found TEXT[],                 -- Array of category names with content
    summary         TEXT,                    -- LLM-generated summary
    extraction_data JSONB,                   -- Full extraction result (for querying)

    -- Output paths
    output_alongside TEXT,                   -- Path to JSON alongside source
    output_central   TEXT,                   -- Path to JSON in central store

    -- Token usage
    prompt_tokens   INTEGER DEFAULT 0,
    completion_tokens INTEGER DEFAULT 0,

    -- Timestamps
    extracted_at    TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Session context
    session_id      INTEGER REFERENCES v7_sessions(id)
);

CREATE INDEX IF NOT EXISTS idx_v7_extractions_mode ON v7_extractions(mode);
CREATE INDEX IF NOT EXISTS idx_v7_extractions_pillar ON v7_extractions(pillar);
CREATE INDEX IF NOT EXISTS idx_v7_extractions_project ON v7_extractions(project);
CREATE INDEX IF NOT EXISTS idx_v7_extractions_date ON v7_extractions(extracted_at);
CREATE INDEX IF NOT EXISTS idx_v7_extractions_source ON v7_extractions(source_file);
CREATE INDEX IF NOT EXISTS idx_v7_extractions_data ON v7_extractions USING gin(extraction_data);


-- ============================================================
-- Verify
-- ============================================================

SELECT 'v7_registry schema created successfully' AS status;
SELECT table_name FROM information_schema.tables
WHERE table_schema = 'public' AND table_name LIKE 'v7_%'
ORDER BY table_name;
