#!/bin/bash
# Health check for data-engineering
echo "Testing data-engineering..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ data-engineering structure looks good"
exit 0
