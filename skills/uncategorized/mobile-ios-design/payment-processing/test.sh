#!/bin/bash
# Health check for payment-processing
echo "Testing payment-processing..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ payment-processing structure looks good"
exit 0
