#!/bin/bash
# Health check for nodejs-backend-patterns
echo "Testing nodejs-backend-patterns..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ nodejs-backend-patterns structure looks good"
exit 0
