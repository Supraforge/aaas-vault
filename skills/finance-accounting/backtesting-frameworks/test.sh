#!/bin/bash
# Health check for backtesting-frameworks
echo "Testing backtesting-frameworks..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ backtesting-frameworks structure looks good"
exit 0
