#!/bin/bash
# Health check for helm-chart-scaffolding
echo "Testing helm-chart-scaffolding..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ helm-chart-scaffolding structure looks good"
exit 0
