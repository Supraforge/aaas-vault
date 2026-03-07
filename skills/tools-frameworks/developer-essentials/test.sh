#!/bin/bash
# Health check for developer-essentials
echo "Testing developer-essentials..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ developer-essentials structure looks good"
exit 0
