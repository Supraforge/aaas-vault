#!/bin/bash
# Health check for data-quality-frameworks
echo "Testing data-quality-frameworks..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ data-quality-frameworks structure looks good"
exit 0
