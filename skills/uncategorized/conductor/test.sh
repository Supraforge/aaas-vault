#!/bin/bash
# Health check for conductor
echo "Testing conductor..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ conductor structure looks good"
exit 0
