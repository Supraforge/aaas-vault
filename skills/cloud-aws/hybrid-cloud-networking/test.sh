#!/bin/bash
# Health check for hybrid-cloud-networking
echo "Testing hybrid-cloud-networking..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ hybrid-cloud-networking structure looks good"
exit 0
