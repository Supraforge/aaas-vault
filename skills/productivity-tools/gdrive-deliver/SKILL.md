---
name: gdrive-deliver
description: Intelligent file delivery to Google Drive with 3-tier format selection. Converts human-readable docs to Google Docs, uploads AI-targeted files as raw .md, and ensures dual-purpose files are well-formatted markdown that renders readably in Drive's preview.
license: MIT
metadata:
  version: 1.0.0
  author: Enora AI
  category: delivery
  domain: document-management
  updated: 2026-03-04
  tech-stack: Python, Google Drive API v3, Google Docs API v1
  service-account: enora-drive-builder@enora-ai-hub-2026.iam.gserviceaccount.com
  integrations: investor-outreach, linkedin-profiler, content-operations
---

# Google Drive Delivery Skill

Deliver files to Google Drive with automatic format selection based on audience.

## Format Decision Framework

**This is the core rule. Follow it every time you deliver files to Drive.**

### Tier 1: Human-Readable → Google Doc

Convert to native Google Docs when the primary audience is humans reading, commenting, or sharing.

**When to use:**
- Reports, analyses, summaries, briefs for stakeholders
- Investor updates, press materials, meeting notes
- Any document going to executives or external recipients
- Deliverables meant to be printed, commented on, or shared via link

**File patterns:** `*_REPORT.md`, `*_ANALYSIS.md`, `*_SUMMARY.md`, `*_BRIEF.md`, `*_UPDATE.md`

**Upload method:** `upload_as_google_doc()` from `scripts/gdrive_upload.py`

### Tier 2: AI/Machine-Only → Raw `.md`

Upload as-is when the primary consumer is an AI agent or automated pipeline.

**When to use:**
- Configuration files (YAML, JSON, TOML)
- Agent context files (SKILL.md, CLAUDE.md, prompts)
- Scripts and source code
- Data pipeline specs, search configs
- Template files with placeholders

**File patterns:** `SKILL.md`, `CLAUDE.md`, `*.yaml`, `*.yml`, `*.json`, `*.py`, `*.sh`, `config/*`, `scripts/*`

**Upload method:** `upload_file()` with `text/markdown` MIME type

### Tier 3: Both → `.md` + Google Doc Copy

Upload TWO files: the raw `.md` (for AI consumption) AND a Google Doc copy (for human reading). When a human opens the folder, they see a properly formatted Google Doc. When an agent needs the data, the `.md` is there unchanged.

**When to use:**
- Guides and references shared between humans and AI
- Profile indexes (readable by humans, parseable by agents)
- Documentation that serves as both README and agent context
- Any file where the user says "needs to work for both"

**File patterns:** `*_GUIDE.md`, `*_REFERENCE.md`, `*_PROFILES.md`, `*_DOCS.md`

**Upload method:** `upload_file()` for the raw `.md` + `upload_md_as_gdoc()` for the Google Doc copy

### Raw Files (No Conversion)

Data files uploaded as-is with their native MIME type.

**File types:** `.csv`, `.xlsx`, `.pdf`, `.png`, `.jpg`

**Upload method:** `upload_file()` with appropriate MIME type

---

## Classification Table

| Signal | Tier |
|--------|------|
| `*_REPORT.md`, `*_ANALYSIS.md`, `*_SUMMARY.md`, `*_BRIEF.md` | human |
| `*_GUIDE.md`, `*_REFERENCE.md`, `*_PROFILES.md` | both |
| `SKILL.md`, `CLAUDE.md`, `README.md` (agent context) | ai |
| `*.yaml`, `*.yml`, `*.json`, `*.py`, `*.sh`, `*.toml` | ai |
| `config/*`, `scripts/*`, `resources/*` | ai |
| `.csv`, `.xlsx`, `.pdf`, `.png`, `.jpg` | raw |
| `.md` with heavy prose, tables, executive summaries | human |
| `.md` with YAML frontmatter, code blocks, agent prompts | ai |
| `.md` ambiguous or dual-purpose | both |

---

## Workflow

When delivering files to Google Drive, follow these steps:

1. **Classify each file** using the table above (or `--format auto`)
2. **Create/find the target folder** in Drive (idempotent — won't duplicate)
3. **Upload each file** using the correct method for its tier
4. **Share** with configured recipients
5. **Report** what was uploaded, in what format, with Drive links

---

## Quick Start

```bash
# Single file (auto-classify format)
python3 skills/gdrive-deliver/scripts/gdrive_deliver.py \
  --file output/LINKEDIN_ENRICHMENT_REPORT.md \
  --folder-id <drive_folder_id>

# Multiple files
python3 skills/gdrive-deliver/scripts/gdrive_deliver.py \
  --files output/REPORT.md output/DATA.xlsx config/searches.yaml \
  --folder-id <drive_folder_id>

# Force a specific format
python3 skills/gdrive-deliver/scripts/gdrive_deliver.py \
  --file output/GUIDE.md \
  --folder-id <drive_folder_id> \
  --format human

# Dry run (preview what would happen)
python3 skills/gdrive-deliver/scripts/gdrive_deliver.py \
  --files output/*.md output/*.csv \
  --folder-id <drive_folder_id> \
  --dry-run

# Deliver entire directory
python3 skills/gdrive-deliver/scripts/gdrive_deliver.py \
  --folder output/ \
  --folder-id <drive_folder_id>
```

---

## Infrastructure

This skill wraps existing infrastructure — it does NOT reinvent upload logic.

| Component | Location |
|-----------|----------|
| Core upload functions | `scripts/gdrive_upload.py` |
| Service account key | `enora_drive_service_account.json` |
| Format classification rules | `skills/gdrive-deliver/config/format_rules.yaml` |
| Orchestration script | `skills/gdrive-deliver/scripts/gdrive_deliver.py` |

### Reused Functions from `scripts/gdrive_upload.py`

- `get_services()` — Service account auth (Drive + Docs API)
- `upload_as_google_doc(drive, docs, file_path, folder_id)` — Markdown → Google Doc with styled headings
- `upload_file(drive, file_path, folder_id)` — Raw file upload with MIME detection
- `find_or_create_folder(drive, name, parent_id)` — Idempotent folder creation
- `share_file(drive, file_id, email)` — Permission management
- `md_to_requests(content)` — Markdown → Google Docs API batchUpdate requests

---

## Markdown Best Practices for "Both" Tier

When creating `.md` files that need to render well in Drive's preview AND be machine-parseable:

1. Use a single `#` for the title (no YAML frontmatter visible to humans)
2. Keep blank lines around all headings
3. Use standard pipe tables (no complex HTML)
4. Use standard markdown links `[text](url)`
5. Avoid raw HTML
6. Keep line lengths reasonable (no 500-char lines)
7. If YAML frontmatter is needed, keep it minimal and clean
