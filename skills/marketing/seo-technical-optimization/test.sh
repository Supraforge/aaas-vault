#!/bin/bash
# Health check for seo-technical-optimization
echo "Testing seo-technical-optimization..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ seo-technical-optimization structure looks good"
exit 0
