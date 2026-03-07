# Manifest Format

## Directory Structure

```
<output-dir>/manifest/
├── PROGRESS.md             # Master progress tracker
├── classes.txt             # Class manifest
├── functions.txt           # Function manifest
├── hooks.txt               # Hooks manifest (actions + filters)
├── rest-endpoints.txt      # REST API manifest
├── ajax-handlers.txt       # AJAX manifest
├── js-files.txt            # JavaScript manifest
├── db-tables.txt           # Database tables manifest
├── templates.txt           # Templates manifest
├── blocks.txt              # Blocks manifest
├── shortcodes.txt          # Shortcodes manifest
├── widgets.txt             # Widgets manifest
├── cpt-taxonomies.txt      # CPT/Taxonomy manifest
├── admin-pages.txt         # Admin pages manifest
├── cron-jobs.txt           # Cron jobs manifest
└── cli-commands.txt        # CLI commands manifest
```

## Manifest File Format

Each manifest file uses this format:

```
# <Category> Manifest
# Generated: 2025-12-30T12:00:00Z
# Source: /path/to/plugin
# Total: <count>

[ ] item_name | file.php:123 | status:pending
[ ] item_name | file.php:456 | status:pending
[x] item_name | file.php:789 | status:documented
[!] item_name | file.php:999 | status:error | reason:file not found
```

### Status Values

- `status:pending` - Not yet documented
- `status:documented` - Successfully documented
- `status:error` - Could not document (with reason)
- `status:manual-review` - Needs human review

### Markers

- `[ ]` - Pending
- `[x]` - Documented
- `[!]` - Error

## PROGRESS.md Format

```markdown
# Documentation Progress

## Overall Status
- **Started:** 2025-12-30T12:00:00Z
- **Current Phase:** Phase 2 - Documentation
- **Coverage:** 58%

## Category Progress
| Category | Discovered | Documented | Coverage |
|----------|------------|------------|----------|
| Classes | 45 | 45 | 100% |
| Functions | 146 | 120 | 82% |
| Hooks | 143 | 89 | 62% |
| REST Endpoints | 12 | 12 | 100% |
| AJAX Handlers | 8 | 8 | 100% |
| JS Files | 20 | 6 | 30% |
| DB Tables | 5 | 5 | 100% |
| Templates | 50 | 30 | 60% |
| Blocks | 0 | 0 | N/A |
| Shortcodes | 3 | 3 | 100% |
| Widgets | 2 | 2 | 100% |
| CPT/Taxonomies | 4 | 4 | 100% |
| Admin Pages | 6 | 6 | 100% |
| Cron Jobs | 2 | 0 | 0% |
| CLI Commands | 5 | 5 | 100% |

## Verification Runs
| Run | Timestamp | Coverage | Gaps Found |
|-----|-----------|----------|------------|
| 1 | 2025-12-30T12:30:00Z | 45% | 234 |
| 2 | 2025-12-30T13:00:00Z | 78% | 89 |
| 3 | 2025-12-30T13:30:00Z | 95% | 21 |

## Gap Log
<!-- Items that couldn't be documented -->
- functions.txt:145 - `deprecated_function` - Removed in latest version
- hooks.txt:89 - `legacy_filter` - Undocumented internal hook
```

## Updating Manifests

When documenting an item:

1. Find the item in the manifest file
2. Change `[ ]` to `[x]`
3. Change `status:pending` to `status:documented`
4. Update PROGRESS.md category count

Example:
```bash
# Before
[ ] BP_Core_User | bp-core/classes/class-bp-core-user.php:45 | status:pending

# After
[x] BP_Core_User | bp-core/classes/class-bp-core-user.php:45 | status:documented
```

When encountering an error:

```bash
# Error entry
[!] Legacy_Class | old-file.php:100 | status:error | reason:file deleted
```
