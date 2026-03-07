# Enumeration Commands

## All 16 Enumeration Commands

Run these in parallel to populate manifests.

### 1. Classes

```bash
grep -rn "^class \|^abstract class \|^trait \|^interface " --include="*.php" <path> | \
  grep -v "vendor\|node_modules\|tests" | \
  awk -F: '{print "[ ] " $2 " | " $1 ":" $2 " | status:pending"}'
```

### 2. Functions

```bash
grep -rn "^function [a-z_]" --include="*.php" <path> | \
  grep -v "vendor\|node_modules\|tests" | \
  awk -F: '{print "[ ] " $3 " | " $1 ":" $2 " | status:pending"}'
```

### 3. Action Hooks

```bash
grep -roh "do_action\s*(\s*['\"][^'\"]*['\"]" --include="*.php" <path> | \
  grep -v "vendor" | \
  sed "s/do_action\s*(\s*['\"]//; s/['\"].*//" | \
  sort -u | \
  awk '{print "[ ] " $1 " | action | status:pending"}'
```

### 4. Filter Hooks

```bash
grep -roh "apply_filters\s*(\s*['\"][^'\"]*['\"]" --include="*.php" <path> | \
  grep -v "vendor" | \
  sed "s/apply_filters\s*(\s*['\"]//; s/['\"].*//" | \
  sort -u | \
  awk '{print "[ ] " $1 " | filter | status:pending"}'
```

### 5. REST Endpoints

```bash
grep -rn "register_rest_route" --include="*.php" <path> | \
  grep -v "vendor" | \
  awk '{print "[ ] " $0 " | status:pending"}'
```

### 6. AJAX Handlers

```bash
grep -rn "wp_ajax_\|admin-ajax" --include="*.php" <path> | \
  grep -v "vendor" | \
  awk '{print "[ ] " $0 " | status:pending"}'
```

### 7. JavaScript Files

```bash
find <path> -name "*.js" -not -path "*/node_modules/*" -not -path "*/vendor/*" -not -name "*.min.js" | \
  awk '{print "[ ] " $0 " | status:pending"}'
```

### 8. Database Tables

```bash
grep -rn "CREATE TABLE\|\$wpdb->prefix\s*\.\s*['\"]" --include="*.php" <path> | \
  grep -v "vendor" | \
  awk '{print "[ ] " $0 " | status:pending"}'
```

### 9. Templates

```bash
find <path> -name "*.php" -path "*/templates/*" -o -name "*-template.php" | \
  awk '{print "[ ] " $0 " | status:pending"}'
```

### 10. Blocks

```bash
find <path> -name "block.json" | \
  awk '{print "[ ] " $0 " | status:pending"}'

grep -rn "register_block_type" --include="*.php" <path> | \
  grep -v "vendor" | \
  awk '{print "[ ] " $0 " | status:pending"}'
```

### 11. Shortcodes

```bash
grep -rn "add_shortcode" --include="*.php" <path> | \
  grep -v "vendor" | \
  awk '{print "[ ] " $0 " | status:pending"}'
```

### 12. Widgets

```bash
grep -rn "extends WP_Widget\|register_widget" --include="*.php" <path> | \
  grep -v "vendor" | \
  awk '{print "[ ] " $0 " | status:pending"}'
```

### 13. CPT & Taxonomies

```bash
grep -rn "register_post_type\|register_taxonomy" --include="*.php" <path> | \
  grep -v "vendor" | \
  awk '{print "[ ] " $0 " | status:pending"}'
```

### 14. Admin Pages

```bash
grep -rn "add_menu_page\|add_submenu_page\|add_options_page" --include="*.php" <path> | \
  grep -v "vendor" | \
  awk '{print "[ ] " $0 " | status:pending"}'
```

### 15. Cron Jobs

```bash
grep -rn "wp_schedule_event\|wp_schedule_single_event" --include="*.php" <path> | \
  grep -v "vendor" | \
  awk '{print "[ ] " $0 " | status:pending"}'
```

### 16. CLI Commands

```bash
grep -rn "WP_CLI::add_command\|extends WP_CLI_Command" --include="*.php" <path> | \
  grep -v "vendor" | \
  awk '{print "[ ] " $0 " | status:pending"}'
```

## Post-Enumeration Count

After running all commands, count totals:

```bash
for file in manifest/*.txt; do
  category=$(basename "$file" .txt)
  total=$(grep -c "status:pending\|status:documented" "$file" 2>/dev/null || echo 0)
  documented=$(grep -c "status:documented" "$file" 2>/dev/null || echo 0)
  echo "$category: $documented / $total"
done
```

## Exclusion Patterns

Always exclude:
- `vendor/` - Composer dependencies
- `node_modules/` - npm dependencies
- `tests/` - Test files (optional)
- `*.min.js` - Minified files
