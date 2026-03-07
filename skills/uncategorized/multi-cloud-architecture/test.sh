#!/bin/bash
# Health check for multi-cloud-architecture
echo "Testing multi-cloud-architecture..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ multi-cloud-architecture structure looks good"
exit 0
