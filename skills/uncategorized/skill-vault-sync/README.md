# Skill Vault Sync

**De-brand project-specific skills and sync them to the global vault.**

## Quick Start

### Sync a Single Skill
```bash
# Dry run (preview changes)
~/.gemini/antigravity-vault/skills/skill-vault-sync/scripts/sync-to-vault.sh \
  /Users/user/.gemini/enora \
  brand-identity \
  --dry-run

# Actually sync
~/.gemini/antigravity-vault/skills/skill-vault-sync/scripts/sync-to-vault.sh \
  /Users/user/.gemini/enora \
  brand-identity
```

### Sync All Skills from a Project
```bash
# List all skills in project
ls /Users/user/.gemini/enora/skills/

# Sync each one
for skill in brand-identity ui-ux-pro-max market-intelligence-gather; do
  ~/.gemini/antigravity-vault/skills/skill-vault-sync/scripts/sync-to-vault.sh \
    /Users/user/.gemini/enora \
    $skill
done
```

## What It Does

1. **Detects** brand-specific content in your project skills
2. **Replaces** brand names, colors, fonts with placeholders
3. **Backs up** existing vault skills
4. **Syncs** de-branded version to vault
5. **Logs** all changes

## Placeholders Used

| Original | Placeholder |
|----------|-------------|
| "Enora.ai" | `[BRAND_NAME]` |
| "#0047FF" | `[COLOR_HEX]` |
| "Electric Blue" | `[PRIMARY_COLOR_NAME]` |
| "JetBrains Mono" | `[HEADER_FONT]` |
| "AI Quality Layer" | `[PRODUCT_CATEGORY]` |

## Safety Features

- ✅ **Backups**: Creates timestamped backups before overwriting
- ✅ **Dry Run**: Preview changes before applying
- ✅ **Validation**: Checks for remaining brand references
- ✅ **Logging**: Tracks all sync operations

## Example Output

```
=== Skill Vault Sync ===
Project: /Users/user/.gemini/enora
Skill: brand-identity
Vault: /Users/user/.gemini/antigravity-vault/skills

[1/5] Copying skill to temp directory...
[2/5] Detecting brand-specific content...
  ✓ Detected brand: Enora.ai
[3/5] De-branding files...
  Processing: design-tokens.json
    ✓ De-branded
  Processing: tech-stack.md
    ✓ De-branded
  ✓ Completed 12 replacements
[4/5] Validating de-branding...
  ✓ No brand references found
[5/5] Syncing to vault...
  ✓ Backed up to: /vault/skills/brand-identity.backup.1738073681
  ✓ Synced to vault

=== Sync Complete ===
Skill: brand-identity
Replacements: 12
Vault location: /vault/skills/brand-identity
```

## Files Modified

- `resources/design-tokens.json` - Colors, fonts, brand name
- `resources/tech-stack.md` - Product descriptions
- `resources/voice-tone.md` - Brand-specific language

## Verification

After syncing, verify the vault skill:

```bash
# Check the de-branded skill
cat ~/.gemini/antigravity-vault/skills/brand-identity/resources/design-tokens.json

# Should see placeholders like:
# "brand_name": "[BRAND_NAME]"
# "hex": "[COLOR_HEX]"
```

## Troubleshooting

### "Skill not found"
- Check the skill name matches the directory name
- Ensure the project path is correct

### "Brand references remain"
- Review the warnings
- Manually update remaining references
- Re-run the sync

### "Permission denied"
- Ensure the script is executable: `chmod +x sync-to-vault.sh`

## Related Documentation

- See `SKILL.md` for full workflow details
- Check `sync.log` in vault for sync history
