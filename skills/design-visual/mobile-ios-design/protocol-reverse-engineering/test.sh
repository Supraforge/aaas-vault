#!/bin/bash
# Health check for protocol-reverse-engineering
echo "Testing protocol-reverse-engineering..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ protocol-reverse-engineering structure looks good"
exit 0
