#!/bin/bash
# Health check for grafana-dashboards
echo "Testing grafana-dashboards..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ grafana-dashboards structure looks good"
exit 0
