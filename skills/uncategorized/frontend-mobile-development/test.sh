#!/bin/bash
# Health check for frontend-mobile-development
echo "Testing frontend-mobile-development..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ frontend-mobile-development structure looks good"
exit 0
