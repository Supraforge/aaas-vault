#!/bin/bash
# Health check for deployment-strategies
echo "Testing deployment-strategies..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ deployment-strategies structure looks good"
exit 0
