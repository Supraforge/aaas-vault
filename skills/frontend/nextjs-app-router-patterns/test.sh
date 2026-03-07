#!/bin/bash
# Health check for nextjs-app-router-patterns
echo "Testing nextjs-app-router-patterns..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ nextjs-app-router-patterns structure looks good"
exit 0
