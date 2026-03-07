#!/bin/bash
# Health check for jvm-languages
echo "Testing jvm-languages..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ jvm-languages structure looks good"
exit 0
