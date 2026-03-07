#!/bin/bash
# Health check for tailwind-design-system
echo "Testing tailwind-design-system..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ tailwind-design-system structure looks good"
exit 0
