#!/bin/bash
# Health check for kpi-dashboard-design
echo "Testing kpi-dashboard-design..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ kpi-dashboard-design structure looks good"
exit 0
