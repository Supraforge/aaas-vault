#!/bin/bash
# Health check for python-development
echo "Testing python-development..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ python-development structure looks good"
exit 0
