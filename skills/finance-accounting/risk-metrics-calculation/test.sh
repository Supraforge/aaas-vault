#!/bin/bash
# Health check for risk-metrics-calculation
echo "Testing risk-metrics-calculation..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ risk-metrics-calculation structure looks good"
exit 0
