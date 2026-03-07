#!/bin/bash
# Health check for anti-reversing-techniques
echo "Testing anti-reversing-techniques..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ anti-reversing-techniques structure looks good"
exit 0
