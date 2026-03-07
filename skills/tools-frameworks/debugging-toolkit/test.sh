#!/bin/bash
# Health check for debugging-toolkit
echo "Testing debugging-toolkit..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ debugging-toolkit structure looks good"
exit 0
