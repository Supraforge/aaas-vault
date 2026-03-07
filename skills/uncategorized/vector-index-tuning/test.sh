#!/bin/bash
# Health check for vector-index-tuning
echo "Testing vector-index-tuning..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ vector-index-tuning structure looks good"
exit 0
