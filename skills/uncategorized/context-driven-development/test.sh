#!/bin/bash
# Health check for context-driven-development
echo "Testing context-driven-development..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ context-driven-development structure looks good"
exit 0
