#!/bin/bash
# Health check for git-advanced-workflows skill
echo "🔍 Checking git-advanced-workflows skill..."
if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found."
else
    echo "❌ SKILL.md missing."
    exit 1
fi
echo "🚀 git-advanced-workflows skill is ready."
exit 0
