#!/bin/bash
# Health check for seo-content-creation
echo "Testing seo-content-creation..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ seo-content-creation structure looks good"
exit 0
