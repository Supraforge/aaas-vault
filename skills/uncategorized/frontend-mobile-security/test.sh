#!/bin/bash
# Health check for frontend-mobile-security
echo "Testing frontend-mobile-security..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ frontend-mobile-security structure looks good"
exit 0
