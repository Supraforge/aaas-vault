#!/bin/bash
# Health check for architecture-decision-records
echo "Testing architecture-decision-records..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ architecture-decision-records structure looks good"
exit 0
