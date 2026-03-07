#!/bin/bash
# Health check for api-design-principles
echo "Testing api-design-principles..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ api-design-principles structure looks good"
exit 0
