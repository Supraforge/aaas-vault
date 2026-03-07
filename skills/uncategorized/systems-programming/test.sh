#!/bin/bash
# Health check for systems-programming
echo "Testing systems-programming..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ systems-programming structure looks good"
exit 0
