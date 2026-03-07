#!/bin/bash
# Health check for quantitative-trading
echo "Testing quantitative-trading..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ quantitative-trading structure looks good"
exit 0
