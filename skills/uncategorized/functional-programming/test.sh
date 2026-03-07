#!/bin/bash
# Health check for functional-programming
echo "Testing functional-programming..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ functional-programming structure looks good"
exit 0
