#!/bin/bash
# Health check for api-scaffolding
echo "Testing api-scaffolding..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ api-scaffolding structure looks good"
exit 0
