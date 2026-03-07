#!/bin/bash
# Health check for kubernetes-operations
echo "Testing kubernetes-operations..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ kubernetes-operations structure looks good"
exit 0
