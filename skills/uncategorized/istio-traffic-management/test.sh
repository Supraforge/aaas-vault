#!/bin/bash
# Health check for istio-traffic-management
echo "Testing istio-traffic-management..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ istio-traffic-management structure looks good"
exit 0
