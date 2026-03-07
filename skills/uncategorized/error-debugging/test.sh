#!/bin/bash
# Health check for error-debugging
echo "Testing error-debugging..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ error-debugging structure looks good"
exit 0
