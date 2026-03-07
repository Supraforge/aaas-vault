#!/bin/bash
# Health check for comprehensive-review
echo "Testing comprehensive-review..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ comprehensive-review structure looks good"
exit 0
