#!/bin/bash
# Health check for github-actions-templates
echo "Testing github-actions-templates..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ github-actions-templates structure looks good"
exit 0
