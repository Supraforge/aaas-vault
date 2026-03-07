#!/bin/bash
# Health check for attack-tree-construction skill

echo "🔍 Validating attack-tree-construction..."

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

# Check for template files
if [ -d "templates" ]; then
    echo "✅ Templates directory found."
    echo "   Available templates:"
    ls -la templates/ 2>/dev/null || echo "   (No templates found)"
else
    echo "ℹ️  No templates directory found. This skill may use inline templates."
fi

echo "🚀 attack-tree-construction is ready."
exit 0
