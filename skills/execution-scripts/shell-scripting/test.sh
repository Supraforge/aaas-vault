#!/bin/bash
# Health check for shell-scripting
echo "Testing shell-scripting..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ shell-scripting structure looks good"
exit 0
