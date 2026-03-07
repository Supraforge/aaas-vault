#!/bin/bash
# Health check for performance-testing-review
echo "Testing performance-testing-review..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ performance-testing-review structure looks good"
exit 0
