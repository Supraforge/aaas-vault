#!/bin/bash
# Health check for application-performance
echo "Testing application-performance..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ application-performance structure looks good"
exit 0
