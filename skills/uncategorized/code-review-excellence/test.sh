#!/bin/bash
# Health check for code-review-excellence skill
echo "🔍 Checking code-review-excellence skill..."
if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found."
else
    echo "❌ SKILL.md missing."
    exit 1
fi
echo "🚀 code-review-excellence skill is ready."
exit 0
