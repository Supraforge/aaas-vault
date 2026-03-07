#!/bin/bash
# Health check for debugging-strategies skill
echo "🔍 Checking debugging-strategies skill..."
if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found."
else
    echo "❌ SKILL.md missing."
    exit 1
fi
echo "🚀 debugging-strategies skill is ready."
exit 0
