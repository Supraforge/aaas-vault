#!/bin/bash
# Health check for typescript-advanced-types
echo "Testing typescript-advanced-types..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ typescript-advanced-types structure looks good"
exit 0
