#!/bin/bash
# Health check for business-analytics
echo "Testing business-analytics..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ business-analytics structure looks good"
exit 0
