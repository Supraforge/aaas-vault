#!/bin/bash
# Health check for backend-api-security
echo "Testing backend-api-security..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ backend-api-security structure looks good"
exit 0
