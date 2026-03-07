#!/bin/bash
# Health check for openapi-spec-generation
echo "Testing openapi-spec-generation..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ openapi-spec-generation structure looks good"
exit 0
