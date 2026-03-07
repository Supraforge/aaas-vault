#!/bin/bash
# Health check for content-marketing
echo "Testing content-marketing..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ content-marketing structure looks good"
exit 0
