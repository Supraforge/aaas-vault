#!/bin/bash
# Health check for brainstorming skill

echo "🔍 Validating brainstorming skill..."

# Check 1: Git dependency
if command -v git &> /dev/null; then
    echo "✅ Git is available."
else
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

# Check 2: Directory structure
if [ -d "${SKILL_DIR:-.}/templates" ] || [ -d "${SKILL_DIR:-.}/scripts" ]; then
    echo "✅ Skill resources located."
else
    echo "ℹ️ No external resources required."
fi

echo "🚀 Brainstorming skill is ready for use."
exit 0
