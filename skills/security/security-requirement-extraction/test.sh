#!/bin/bash
# Health check for security-requirement-extraction skill

echo "🔍 Validating security-requirement-extraction..."

# Check Python availability
if command -v python3 &> /dev/null; then
    echo "✅ Python3 is available."
else
    echo "❌ Python3 is not installed. Please install python3."
    exit 1
fi

# Check skill structure
if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found."
else
    echo "❌ SKILL.md not found."
    exit 1
fi

echo "🚀 security-requirement-extraction is ready."
exit 0
