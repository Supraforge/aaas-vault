#!/bin/bash
# Health check for architecting-growth-libraries v2.5.0

# Simple absolute path check based on current working directory
SKILL_PATH="$(pwd)/SKILL.md"

echo "🔍 Checking architecting-growth-libraries v2.5.0..."
echo "📂 Skill Path: ${SKILL_PATH}"

if [ ! -f "$SKILL_PATH" ]; then
    echo "❌ SKILL.md not found."
    exit 1
fi

grep -q "version: 2.5.0" "$SKILL_PATH" || { echo "❌ Version 2.5.0 missing"; exit 1; }
grep -q "inputs:" "$SKILL_PATH" || { echo "❌ Inputs missing"; exit 1; }
grep -q "outputs:" "$SKILL_PATH" || { echo "❌ Outputs missing"; exit 1; }
grep -q "# 📚 Original Reference" "$SKILL_PATH" || { echo "❌ Reference missing"; exit 1; }

echo "✅ Skill is healthy."
exit 0
