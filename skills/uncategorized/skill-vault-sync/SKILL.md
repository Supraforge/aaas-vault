---
name: skill-vault-sync
description: >-
  Intelligently de-brands project-specific skills and syncs improvements back to
  the global vault. Detects brand-specific content, replaces it with
  placeholders, and updates vault skills while preserving project-specific
  versions.
version: 1.0.0
dependencies: []
compatibility: 'agent-zero, claude-code, cursor'
---

# Skill Vault Sync

**Purpose:** Upgrade global vault skills with improvements from project-specific implementations while automatically de-branding them.

## 🎯 When to Use This Skill

- After creating or improving skills in a project directory
- When you want to share skill improvements across all projects
- To maintain a clean separation between project-specific and generic skills
- Before archiving a project to preserve learnings

## 🔍 How It Works

### 1. **Detection Phase**
Scans a project's `skills/` directory and identifies:
- Skills that exist in both project and vault
- Skills that are new to the project
- Files that contain brand-specific content

### 2. **Analysis Phase**
For each skill, analyzes:
- **SKILL.md**: Usually generic, check for brand references
- **Resource files**: Likely contain brand-specific values
- **Scripts**: May contain hardcoded paths or brand names

### 3. **De-branding Phase**
Automatically replaces brand-specific content with placeholders:

#### **Brand Identifiers to Replace:**
- Brand names (e.g., "Enora.ai" → "[BRAND_NAME]")
- Product descriptions (e.g., "AI Quality Layer" → "[PRODUCT_DESCRIPTION]")
- Color values (e.g., "#0047FF" → "[PRIMARY_COLOR]")
- Font families (e.g., "JetBrains Mono" → "[HEADER_FONT]")
- URLs and domains
- Company-specific terminology

#### **Placeholder Format:**
```
[BRAND_NAME]
[PRODUCT_DESCRIPTION]
[PRIMARY_COLOR]
[ACCENT_COLOR]
[BACKGROUND_COLOR]
[HEADER_FONT]
[BODY_FONT]
[COMPANY_TAGLINE]
[TARGET_AUDIENCE]
```

### 4. **Sync Phase**
- Creates backup of vault skill (if exists)
- Updates vault skill with de-branded version
- Preserves project-specific version unchanged
- Logs all changes for review

## 📋 Workflow

### **Step 1: Identify Skills to Sync**
```bash
# User provides:
PROJECT_DIR="/Users/user/.gemini/enora"
VAULT_DIR="/Users/user/.gemini/antigravity-vault/skills"
```

### **Step 2: Scan and Compare**
For each skill in `$PROJECT_DIR/skills/`:
1. Check if skill exists in vault
2. Compare file structures
3. Identify resource files with brand content

### **Step 3: De-brand Resources**
For each resource file:
1. **JSON files** (`design-tokens.json`, etc.):
   - Replace specific hex colors with `[PRIMARY_COLOR]`, `[ACCENT_COLOR]`
   - Replace brand name with `[BRAND_NAME]`
   - Replace descriptions with `[DESCRIPTION]`

2. **Markdown files** (`tech-stack.md`, `voice-tone.md`):
   - Replace brand-specific language with placeholders
   - Preserve structure and formatting
   - Keep generic instructions

3. **Scripts** (`test.sh`, etc.):
   - Replace hardcoded paths with `~/.gemini/skills/[SKILL_NAME]`
   - Remove project-specific logic

### **Step 4: Validate**
Before syncing, verify:
- [ ] All brand references replaced
- [ ] Placeholders use consistent naming
- [ ] File structure preserved
- [ ] No broken references

### **Step 5: Sync to Vault**
```bash
# Backup existing vault skill
cp -r "$VAULT_DIR/skill-name" "$VAULT_DIR/skill-name.backup.$(date +%s)"

# Copy de-branded version
cp -r "$TEMP_DIR/skill-name-debranded" "$VAULT_DIR/skill-name"

# Log changes
echo "Synced: skill-name from $PROJECT_DIR to vault" >> sync.log
```

## 🛠️ Implementation Guide

### **Detection Patterns**

#### **Brand Name Detection:**
```regex
# Common patterns:
- Capitalized product names: [A-Z][a-z]+\.[a-z]{2,3}
- Company names in quotes: "CompanyName"
- Repeated proper nouns across files
```

#### **Color Detection:**
```regex
# Hex colors: #[0-9A-Fa-f]{6}
# RGB: rgb\(\d+,\s*\d+,\s*\d+\)
# Named colors in design tokens
```

#### **Font Detection:**
```regex
# Font families: "FontName", 'FontName'
# Google Fonts imports
# @font-face declarations
```

### **De-branding Rules**

#### **Rule 1: Preserve Structure**
- Keep all file paths and directory structure
- Maintain JSON schema
- Preserve markdown formatting

#### **Rule 2: Consistent Placeholders**
- Use UPPERCASE_SNAKE_CASE for placeholders
- Wrap in square brackets: `[PLACEHOLDER]`
- Add comments explaining expected values

#### **Rule 3: Context Preservation**
- Keep usage descriptions generic
- Preserve technical constraints
- Maintain workflow instructions

#### **Rule 4: Metadata Update**
```json
{
  "meta": {
    "brand_name": "[BRAND_NAME]",
    "description": "[PRODUCT_DESCRIPTION]",
    "synced_from": "project-name",
    "sync_date": "2026-01-28",
    "original_brand": "Enora.ai (de-branded)"
  }
}
```

## 📝 Example Transformations

### **Before (Project-Specific):**
```json
{
  "meta": {
    "brand_name": "Enora.ai",
    "description": "AI Quality Layer for Automotive Engineering"
  },
  "colors": {
    "primary": {
      "hex": "#0047FF",
      "name": "Electric Blue",
      "usage": "Core brand, primary actions"
    }
  }
}
```

### **After (De-branded):**
```json
{
  "meta": {
    "brand_name": "[BRAND_NAME]",
    "description": "[PRODUCT_DESCRIPTION]",
    "synced_from": "enora",
    "sync_date": "2026-01-28"
  },
  "colors": {
    "primary": {
      "hex": "[PRIMARY_COLOR]",
      "name": "[PRIMARY_COLOR_NAME]",
      "usage": "Core brand, primary actions"
    }
  }
}
```

## 🚨 Safety Checks

Before syncing, verify:
1. **No data loss**: Vault skill is backed up
2. **No brand leakage**: All brand-specific content replaced
3. **Functionality preserved**: Skill still works with placeholders
4. **Documentation updated**: README reflects de-branding

## 🔄 Reverse Operation: Brand a Vault Skill

When starting a new project, this skill can also:
1. Copy vault skill to project
2. Prompt for brand-specific values
3. Replace placeholders with actual values
4. Validate and test

## 📊 Sync Report Template

```markdown
# Skill Vault Sync Report
**Date:** 2026-01-28
**Project:** enora
**Skills Synced:** 3

## Updated Skills:
1. **brand-identity**
   - Files: SKILL.md, design-tokens.json, tech-stack.md, voice-tone.md
   - Replacements: 12 brand references → placeholders
   - Status: ✅ Synced

2. **ui-ux-pro-max**
   - Files: SKILL.md, resources/design-system.md
   - Replacements: 5 brand references → placeholders
   - Status: ✅ Synced

3. **market-intelligence-gather**
   - Files: SKILL.md
   - Replacements: 0 (already generic)
   - Status: ⏭️ Skipped

## Backups Created:
- /vault/skills/brand-identity.backup.1738073681
- /vault/skills/ui-ux-pro-max.backup.1738073681

## Manual Review Required:
- [ ] Verify placeholder naming consistency
- [ ] Test vault skills with new project
- [ ] Update skill catalog
```

## 🎯 Usage Examples

### **Example 1: Sync All Skills**
```
User: "Sync all skills from the Enora project to the vault"

Agent:
1. Scans /Users/user/.gemini/enora/skills/
2. Identifies 5 skills
3. De-brands each skill
4. Syncs to vault
5. Generates report
```

### **Example 2: Sync Specific Skill**
```
User: "Sync the brand-identity skill to the vault"

Agent:
1. Analyzes brand-identity skill
2. Detects Enora.ai references
3. Replaces with placeholders
4. Syncs to vault
5. Confirms completion
```

### **Example 3: Preview Changes**
```
User: "Show me what would change if I synced brand-identity"

Agent:
1. Performs dry-run de-branding
2. Shows diff of changes
3. Lists all replacements
4. Waits for confirmation
```

## 🔧 Advanced Features

### **Smart Brand Detection**
- Uses frequency analysis to identify brand terms
- Learns from existing vault skills
- Suggests placeholder names

### **Conflict Resolution**
- Detects when vault skill is newer
- Offers merge strategies
- Preserves manual customizations

### **Batch Operations**
- Sync multiple skills at once
- Apply consistent de-branding rules
- Generate comprehensive reports

## 📚 Related Skills
- `skill-creator`: Create new skills
- `brand-identity`: Apply brand guidelines
- `defining-brand-context`: Extract brand from URLs

## 🎓 Best Practices

1. **Always review before syncing**: Check the de-branding preview
2. **Test vault skills**: Verify they work in a new project
3. **Document changes**: Keep sync logs for audit trail
4. **Version control**: Commit vault changes separately
5. **Incremental sync**: Sync one skill at a time initially

## 🚀 Future Enhancements

- [ ] Auto-detect brand terms using NLP
- [ ] Generate brand configuration wizard
- [ ] Support for multi-brand projects
- [ ] Skill versioning and rollback
- [ ] Integration with git for change tracking
