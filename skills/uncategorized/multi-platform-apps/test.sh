#!/bin/bash
# Health check for multi-platform-apps
echo "Testing multi-platform-apps..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ multi-platform-apps structure looks good"
exit 0
