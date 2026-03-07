#!/bin/bash
# Health check for team-composition-analysis
echo "Testing team-composition-analysis..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ team-composition-analysis structure looks good"
exit 0
