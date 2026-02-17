# META-PRD: Enterprise OS V7 Infrastructure Layer

**Version:** 1.0
**Created:** 2026-02-17
**Owner:** John
**Status:** Implemented (Phase 1)

---

## 1. Problem Statement

Enterprise OS V7 has a well-defined folder structure and governance docs, but no persistent infrastructure underneath. Every LLM session starts from scratch — no database, no file tracking, no change audit trail, no way to quickly understand what exists. The FILE_INDEX.json was stale and incomplete. 3,800+ files sit scattered across Downloads folders with no systematic inventory.

## 2. Solution: Track 2 — The Operating System for the Operating System

A local-first infrastructure layer that:
- **Tracks every file** in V7 with content hashes, metadata, and classification
- **Logs every session** with DB-backed tracking and markdown logs
- **Audits every change** with before/after hashes and timestamps
- **Inventories scattered files** for deduplication and consolidation
- **Provides semantic search** via ChromaDB embeddings
- **Exposes a REST API** for programmatic access
- **Runs daily maintenance** with zero LLM tokens

## 3. Architecture

```
┌─────────────────────────────────────────────┐
│                  FastAPI (8100)              │
│  /files  /search  /health  /sessions        │
└────────┬──────────────┬─────────────────────┘
         │              │
    PostgreSQL     ChromaDB
    (enterprise_os)  (v7_documents)
         │              │
    ┌────┴────┐    ┌────┴────┐
    │ v7_files│    │ Markdown │
    │ sessions│    │  chunks  │
    │ changes │    │ embedded │
    │ external│    └──────────┘
    │ state   │
    └─────────┘
         ▲
         │
    v7_registry.py scan
    (filesystem → DB)
```

## 4. Components

### 4.1 Database Schema (`v7_registry.sql`)
- **v7_files** — Master file registry (path, hash, component, pillar, project, metadata)
- **v7_sessions** — Session tracking (start/end, files created/modified, log path)
- **v7_changes** — Audit trail (change type, old/new hash, session context)
- **v7_external_sources** — Scattered file inventory (source, group, status, target)
- **v7_system_state** — Daily snapshots (totals, breakdowns, health indicators)

### 4.2 Registry CLI (`v7_registry.py`)
| Command | Purpose |
|---------|---------|
| `scan` | Full filesystem scan → v7_files |
| `scan --diff` | Compare filesystem vs DB, show changes |
| `health` | Generate system health report |
| `stale` | List files not modified in N days |
| `snapshot` | Save system state snapshot |
| `session start` | Start tracked work session |
| `session end` | End session with stats |
| `session log` | Log entry to current session |
| `chromadb-sync` | Sync markdown to vector store |

### 4.3 Consolidation Tool (`v7_consolidate.py`)
| Command | Purpose |
|---------|---------|
| `inventory` | Scan external sources → v7_external_sources |
| `dedup` | Compare hashes, mark duplicates |
| `plan` | Generate consolidation plan (markdown) |
| `execute` | Move files with explicit approval |

### 4.4 Search API (`v7_search_api.py`)
FastAPI on port 8100 with endpoints for files, search, health, sessions, changes, snapshots, stats.

### 4.5 Daily Runner (`v7_daily.py`)
One command: scan diff → full scan → health report → snapshot → stale check.

## 5. Data Flow

### Session Workflow
```
Session Start → DB row + markdown log → Work → Session Log entries
    → Session End → Diff scan → Update stats → Snapshot
```

### Daily Maintenance
```
v7_daily.py → scan --diff → scan → health → snapshot → stale
              (2 min total, zero LLM tokens)
```

### Consolidation Workflow
```
inventory → dedup → plan (review) → execute --approved
(nothing moves without explicit approval)
```

## 6. Key Decisions

| Decision | Rationale |
|----------|-----------|
| PostgreSQL (not SQLite) | Already running for ui_library, consistent tooling |
| Separate database (enterprise_os) | Don't pollute ui_library with system tables |
| SHA-256 hashing | Reliable dedup, change detection |
| Port 8100 | Avoids conflict with existing search_api on 5000 |
| ChromaDB optional | Core functionality works without it |
| Copy (not move) for consolidation | Safety first — originals preserved |

## 7. Metrics (First Scan)

| Metric | Value |
|--------|-------|
| Total files registered | 5,657 |
| Total size | 4,887 MB |
| Files by component (top) | BUILD_FACTORY: 5,552 |
| Empty pillars | 8 / 23 |
| External files inventoried | 1,276 |
| External duplicates of V7 | 150 |
| Unique external files | 1,126 |

## 8. File Inventory

| # | File | Location | Lines |
|---|------|----------|-------|
| 1 | v7_registry.sql | 03_CORE_ENGINE/SCHEMAS/ | ~165 |
| 2 | v7_registry.py | 03_CORE_ENGINE/SCRIPTS/ | ~700 |
| 3 | v7_consolidate.py | 03_CORE_ENGINE/SCRIPTS/ | ~310 |
| 4 | v7_search_api.py | 03_CORE_ENGINE/SCRIPTS/ | ~300 |
| 5 | v7_daily.py | 03_CORE_ENGINE/SCRIPTS/ | ~90 |
| 6 | This document | 07_BUILD_FACTORY/PRJ_Enterprise_Platform/02_Product/ | — |

## 9. Future Enhancements (Not in Scope)

- DeepSeek API enrichment (AI summaries, domain classification)
- Dashboard UI (Next.js frontend for search API)
- Automated pillar routing for new files
- Git hook integration (auto-scan on commit)
- Cross-session analytics (productivity trends)

---

*This PRD documents the infrastructure layer built on 2026-02-17. All scripts are operational and tested.*
