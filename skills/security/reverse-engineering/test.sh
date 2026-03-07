#!/bin/bash
# Health check for reverse-engineering
echo "Testing reverse-engineering..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ reverse-engineering structure looks good"
exit 0
