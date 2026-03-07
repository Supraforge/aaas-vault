#!/bin/bash
# Health check for error-handling-patterns skill
echo "🔍 Checking error-handling-patterns skill..."
if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found."
else
    echo "❌ SKILL.md missing."
    exit 1
fi
echo "🚀 error-handling-patterns skill is ready."
exit 0
