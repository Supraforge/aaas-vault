#!/bin/bash
# Health check for startup-business-analyst
echo "Testing startup-business-analyst..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ startup-business-analyst structure looks good"
exit 0
