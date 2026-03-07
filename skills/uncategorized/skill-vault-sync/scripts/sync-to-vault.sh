#!/bin/bash
# Skill Vault Sync - De-branding and Sync Script
# Usage: ./sync-to-vault.sh <project-dir> <skill-name> [--dry-run]

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PROJECT_DIR="${1:-}"
SKILL_NAME="${2:-}"
DRY_RUN="${3:-}"
VAULT_DIR="$HOME/.gemini/antigravity-vault/skills"
TEMP_DIR="/tmp/skill-vault-sync-$$"

# Validation
if [ -z "$PROJECT_DIR" ] || [ -z "$SKILL_NAME" ]; then
    echo -e "${RED}Usage: $0 <project-dir> <skill-name> [--dry-run]${NC}"
    echo "Example: $0 /Users/user/.gemini/enora brand-identity"
    exit 1
fi

if [ ! -d "$PROJECT_DIR/skills/$SKILL_NAME" ]; then
    echo -e "${RED}Error: Skill '$SKILL_NAME' not found in $PROJECT_DIR/skills/${NC}"
    exit 1
fi

echo -e "${BLUE}=== Skill Vault Sync ===${NC}"
echo "Project: $PROJECT_DIR"
echo "Skill: $SKILL_NAME"
echo "Vault: $VAULT_DIR"
echo ""

# Create temp directory
mkdir -p "$TEMP_DIR"

# Step 1: Copy skill to temp directory
echo -e "${YELLOW}[1/5] Copying skill to temp directory...${NC}"
cp -r "$PROJECT_DIR/skills/$SKILL_NAME" "$TEMP_DIR/$SKILL_NAME"

# Step 2: Detect brand-specific content
echo -e "${YELLOW}[2/5] Detecting brand-specific content...${NC}"

# Extract brand name from design-tokens.json if it exists
BRAND_NAME=""
if [ -f "$TEMP_DIR/$SKILL_NAME/resources/design-tokens.json" ]; then
    BRAND_NAME=$(jq -r '.meta.brand_name // empty' "$TEMP_DIR/$SKILL_NAME/resources/design-tokens.json" 2>/dev/null || echo "")
fi

if [ -n "$BRAND_NAME" ]; then
    echo -e "  ${GREEN}✓${NC} Detected brand: $BRAND_NAME"
else
    echo -e "  ${YELLOW}⚠${NC} No brand detected, will use generic de-branding"
fi

# Step 3: De-brand files
echo -e "${YELLOW}[3/5] De-branding files...${NC}"

REPLACEMENTS=0

# Function to de-brand JSON files
debrand_json() {
    local file="$1"
    if [ ! -f "$file" ]; then return; fi
    
    echo -e "  Processing: $(basename $file)"
    
    # Backup original
    cp "$file" "$file.original"
    
    # Replace brand-specific values with placeholders
    if [ -n "$BRAND_NAME" ]; then
        sed -i.bak "s/\"$BRAND_NAME\"/\"[BRAND_NAME]\"/g" "$file"
        ((REPLACEMENTS++))
    fi
    
    # Replace hex colors
    sed -i.bak 's/"#[0-9A-Fa-f]\{6\}"/"[COLOR_HEX]"/g' "$file"
    ((REPLACEMENTS+=3))
    
    # Replace specific color names
    sed -i.bak 's/"Electric Blue"/"[PRIMARY_COLOR_NAME]"/g' "$file"
    sed -i.bak 's/"Neon Green"/"[ACCENT_COLOR_NAME]"/g' "$file"
    sed -i.bak 's/"Deep Space"/"[BACKGROUND_COLOR_NAME]"/g' "$file"
    
    # Replace font families
    sed -i.bak 's/"JetBrains Mono[^"]*"/"[HEADER_FONT]"/g' "$file"
    sed -i.bak 's/"Fira Code[^"]*"/"[HEADER_FONT_ALT]"/g' "$file"
    sed -i.bak 's/"Inter"/"[BODY_FONT]"/g' "$file"
    
    # Add sync metadata
    if command -v jq &> /dev/null; then
        local project_name=$(basename "$PROJECT_DIR")
        local sync_date=$(date +%Y-%m-%d)
        
        jq --arg proj "$project_name" --arg date "$sync_date" --arg brand "$BRAND_NAME" \
           '.meta.synced_from = $proj | .meta.sync_date = $date | .meta.original_brand = ($brand + " (de-branded)")' \
           "$file" > "$file.tmp" && mv "$file.tmp" "$file"
    fi
    
    # Clean up backup
    rm -f "$file.bak"
    
    echo -e "    ${GREEN}✓${NC} De-branded"
}

# Function to de-brand Markdown files
debrand_markdown() {
    local file="$1"
    if [ ! -f "$file" ]; then return; fi
    
    echo -e "  Processing: $(basename $file)"
    
    # Backup original
    cp "$file" "$file.original"
    
    # Replace brand name
    if [ -n "$BRAND_NAME" ]; then
        sed -i.bak "s/$BRAND_NAME/[BRAND_NAME]/g" "$file"
        ((REPLACEMENTS++))
    fi
    
    # Replace common brand-specific phrases
    sed -i.bak 's/AI Quality Layer/[PRODUCT_CATEGORY]/g' "$file"
    sed -i.bak 's/Automotive Engineering/[TARGET_INDUSTRY]/g' "$file"
    
    # Clean up backup
    rm -f "$file.bak"
    
    echo -e "    ${GREEN}✓${NC} De-branded"
}

# Process all resource files
if [ -d "$TEMP_DIR/$SKILL_NAME/resources" ]; then
    for json_file in "$TEMP_DIR/$SKILL_NAME/resources"/*.json; do
        [ -f "$json_file" ] && debrand_json "$json_file"
    done
    
    for md_file in "$TEMP_DIR/$SKILL_NAME/resources"/*.md; do
        [ -f "$md_file" ] && debrand_markdown "$md_file"
    done
fi

echo -e "  ${GREEN}✓${NC} Completed $REPLACEMENTS replacements"

# Step 4: Validate de-branding
echo -e "${YELLOW}[4/5] Validating de-branding...${NC}"

# Check for remaining brand references
if [ -n "$BRAND_NAME" ]; then
    REMAINING=$(grep -r "$BRAND_NAME" "$TEMP_DIR/$SKILL_NAME" 2>/dev/null | wc -l || echo "0")
    if [ "$REMAINING" -gt 0 ]; then
        echo -e "  ${YELLOW}⚠${NC} Warning: $REMAINING potential brand references remain"
        grep -r "$BRAND_NAME" "$TEMP_DIR/$SKILL_NAME" 2>/dev/null || true
    else
        echo -e "  ${GREEN}✓${NC} No brand references found"
    fi
fi

# Step 5: Sync to vault (or show diff if dry-run)
if [ "$DRY_RUN" == "--dry-run" ]; then
    echo -e "${YELLOW}[5/5] Dry run - showing changes...${NC}"
    
    if [ -d "$VAULT_DIR/$SKILL_NAME" ]; then
        echo -e "\n${BLUE}Diff between vault and de-branded version:${NC}"
        diff -r "$VAULT_DIR/$SKILL_NAME" "$TEMP_DIR/$SKILL_NAME" || true
    else
        echo -e "\n${BLUE}New skill - would create:${NC}"
        find "$TEMP_DIR/$SKILL_NAME" -type f
    fi
    
    echo -e "\n${YELLOW}No changes made (dry-run mode)${NC}"
else
    echo -e "${YELLOW}[5/5] Syncing to vault...${NC}"
    
    # Backup existing vault skill
    if [ -d "$VAULT_DIR/$SKILL_NAME" ]; then
        BACKUP_DIR="$VAULT_DIR/$SKILL_NAME.backup.$(date +%s)"
        cp -r "$VAULT_DIR/$SKILL_NAME" "$BACKUP_DIR"
        echo -e "  ${GREEN}✓${NC} Backed up to: $BACKUP_DIR"
    fi
    
    # Copy de-branded skill to vault
    rm -rf "$VAULT_DIR/$SKILL_NAME"
    cp -r "$TEMP_DIR/$SKILL_NAME" "$VAULT_DIR/$SKILL_NAME"
    
    # Remove original backups
    find "$VAULT_DIR/$SKILL_NAME" -name "*.original" -delete
    
    echo -e "  ${GREEN}✓${NC} Synced to vault"
    
    # Generate sync log
    LOG_FILE="$VAULT_DIR/sync.log"
    echo "[$(date +%Y-%m-%d\ %H:%M:%S)] Synced: $SKILL_NAME from $(basename $PROJECT_DIR) ($REPLACEMENTS replacements)" >> "$LOG_FILE"
    
    echo -e "\n${GREEN}=== Sync Complete ===${NC}"
    echo "Skill: $SKILL_NAME"
    echo "Replacements: $REPLACEMENTS"
    echo "Vault location: $VAULT_DIR/$SKILL_NAME"
fi

# Cleanup
rm -rf "$TEMP_DIR"

echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "1. Review the de-branded skill in: $VAULT_DIR/$SKILL_NAME"
echo "2. Test with a new project to ensure placeholders work"
echo "3. Update skill catalog if needed"
