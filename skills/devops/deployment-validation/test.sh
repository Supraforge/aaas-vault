#!/bin/bash
# Health check for deployment-validation
echo "Testing deployment-validation..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ deployment-validation structure looks good"
exit 0
