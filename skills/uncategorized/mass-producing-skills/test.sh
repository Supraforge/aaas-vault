#!/bin/bash
echo "🔍 Checking Agent Zero Skill Factory..."

if [ -d "/Users/user/.gemini/skills/mass-producing-skills/templates" ]; then
    echo "✅ Templates loaded."
else
    echo "❌ Templates missing."
    exit 1
fi

echo "🚀 Agent Zero is ready to manufacture skills."
exit 0
