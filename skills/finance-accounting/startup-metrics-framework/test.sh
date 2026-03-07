#!/bin/bash
# Health check for startup-metrics-framework
echo "Testing startup-metrics-framework..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ startup-metrics-framework structure looks good"
exit 0
