#!/bin/bash
# Health check for implementing-error-handling-patterns skill

echo "🔍 Validating Error Handling Patterns Skill environment..."

# Check for python3
if command -v python3 &> /dev/null; then
    echo "✅ python3 located: $(python3 --version)"
else
    echo "❌ python3 not found. Some templates/scripts may fail."
    exit 1
fi

# Check for templates directory
if [ -d "/Users/user/.gemini/skills/implementing-error-handling-patterns/templates" ]; then
    echo "✅ Templates directory located."
else
    echo "❌ Templates directory missing."
    exit 1
fi

echo "🚀 Error Handling Patterns Skill is ready for use."
exit 0
