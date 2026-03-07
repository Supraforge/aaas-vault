#!/bin/bash
# Health check for backend-development
echo "Testing backend-development..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ backend-development structure looks good"
exit 0
