#!/bin/bash
# Health check for temporal-python-testing
echo "Testing temporal-python-testing..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ temporal-python-testing structure looks good"
exit 0
