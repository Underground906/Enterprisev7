# PILLAR DOCUMENTATION TEMPLATES

Use these templates to create consistent documentation across all 23 pillars.

---

## TEMPLATE: README.md

```markdown
# [PILLAR_NAME]

**Pillar ID:** PIL_XX  
**Domain:** [core system | platform domain | operational]  
**Status:** [active | in development | archived]

---

## Purpose

[One paragraph: what this pillar does and why it exists]

---

## What Belongs Here

- [Type of content 1]
- [Type of content 2]
- [Type of content 3]

## What Does NOT Belong Here

- [Redirect to PIL_XX]
- [Redirect to PIL_YY]

---

## Folder Structure

```
PIL_XX_NAME/
├── 00_CANON/           → Production-ready frameworks and rules
├── 01_[SUBFOLDER]/     → [Description]
├── 02_[SUBFOLDER]/     → [Description]
├── 01_threads/         → Source conversations
├── 02_artifacts/       → Working documents
└── 90_ARCHIVE/         → Superseded/processed content
```

---

## Key Frameworks

1. **[Framework Name]** — [One-line description]
2. **[Framework Name]** — [One-line description]

---

## Related Pillars

| Pillar | Relationship |
|--------|--------------|
| PIL_XX | [feeds into / receives from / shares with] |

---

## Quick Start

1. [First thing to do]
2. [Second thing to do]
3. [Third thing to do]

---

**Last Updated:** [DATE]
```

---

## TEMPLATE: INDEX.md

```markdown
# [PILLAR_NAME] — INDEX

**Total Files:** [X]  
**Last Indexed:** [DATE]

---

## 00_CANON/ ([X] files)

| File | Purpose | Status |
|------|---------|--------|
| [filename.md] | [description] | ✅ Production |

## 01_[SUBFOLDER]/ ([X] files)

| File | Purpose | Status |
|------|---------|--------|
| [filename.md] | [description] | [status] |

## 01_threads/ ([X] files)

| File | Date | Topic |
|------|------|-------|
| [filename.md] | [date] | [topic] |

## 02_artifacts/ ([X] files)

| File | Type | Status |
|------|------|--------|
| [filename.md] | [type] | [status] |

## 90_ARCHIVE/ ([X] files)

Archived content. See archive for superseded versions.

---

**Index auto-generated. Update with:** `python index_pillar.py PIL_XX`
```

---

## TEMPLATE: ROUTING_RULES.md

```markdown
# [PILLAR_NAME] — ROUTING RULES

---

## Inbound Routing (What comes here)

### From Goal Intake
```
IF goal_type == "[type]" AND domain == "[domain]"
THEN route_to PIL_XX
```

### From Thread Analysis
```
IF thread_topic CONTAINS ["keyword1", "keyword2"]
THEN route_to PIL_XX/01_threads/
```

### From Other Pillars
| Source Pillar | Trigger | Destination |
|---------------|---------|-------------|
| PIL_YY | [condition] | [subfolder] |

---

## Outbound Routing (What leaves here)

| Destination | Trigger | Content Type |
|-------------|---------|--------------|
| PIL_YY | [condition] | [type] |
| 05_TEMPLATE_HUB | Template created | Templates |
| 90_ARCHIVE | Superseded | Old versions |

---

## Internal Routing

```
02_artifacts/ → 00_CANON/     (when production-ready)
02_artifacts/ → 90_ARCHIVE/   (when superseded)
01_threads/   → 90_ARCHIVE/   (after extraction complete)
```

---

## Cross-References

This pillar references:
- PIL_XX for [reason]
- PIL_YY for [reason]

This pillar is referenced by:
- PIL_XX for [reason]
- PIL_YY for [reason]

---

## Validation Rules

- [ ] All files in 00_CANON/ have status: production
- [ ] No duplicate filenames across subfolders
- [ ] All threads have been processed for extraction
- [ ] Cross-references are bidirectional
```

---

## TEMPLATE: CANON_STATUS.md

```markdown
# [PILLAR_NAME] — CANON STATUS

**Last Audit:** [DATE]

---

## Production Ready (✅)

| File | Type | Last Updated |
|------|------|--------------|
| [file.md] | [framework/schema/process] | [date] |

## In Development (🔨)

| File | Blocker | Owner |
|------|---------|-------|
| [file.md] | [what's needed] | [who] |

## Needs Review (⚠️)

| File | Issue | Action |
|------|-------|--------|
| [file.md] | [problem] | [next step] |

## Archived (📦)

See `90_ARCHIVE/` for superseded content.

---

## Canon Criteria

For a file to be in 00_CANON/:
- [ ] Complete (no TODOs or placeholders)
- [ ] Tested (used in real work)
- [ ] Consistent (follows system conventions)
- [ ] Documented (has clear purpose)
```

---

**END OF TEMPLATES**
