#!/bin/bash
# Health check for customer-sales-automation
echo "Testing customer-sales-automation..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ customer-sales-automation structure looks good"
exit 0
