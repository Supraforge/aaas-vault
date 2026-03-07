#!/bin/bash
# Health check for ui-design
echo "Testing ui-design..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ ui-design structure looks good"
exit 0
