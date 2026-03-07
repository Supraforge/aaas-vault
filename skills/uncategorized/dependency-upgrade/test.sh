#!/bin/bash
# Health check for dependency-upgrade
echo "Testing dependency-upgrade..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ dependency-upgrade structure looks good"
exit 0
