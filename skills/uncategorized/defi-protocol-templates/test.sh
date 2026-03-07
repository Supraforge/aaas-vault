#!/bin/bash
# Health check for defi-protocol-templates
echo "Testing defi-protocol-templates..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ defi-protocol-templates structure looks good"
exit 0
