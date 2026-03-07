#!/bin/bash
# Health check for market-sizing-analysis
echo "Testing market-sizing-analysis..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ market-sizing-analysis structure looks good"
exit 0
