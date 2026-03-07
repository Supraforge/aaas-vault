#!/bin/bash
# Health check for auth-implementation-patterns skill

echo "🔍 Validating auth-implementation-patterns..."

# Check dependencies
if command -v node >/dev/null 2>&1; then
    echo "✅ Node.js is installed."
else
    echo "❌ Node.js is not installed. Please install it."
    exit 1
fi

if command -v python3 >/dev/null 2>&1; then
    echo "✅ Python3 is installed."
else
    echo "❌ Python3 is not installed. Please install it."
    exit 1
fi

# Check if SKILL.md exists
if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found."
else
    echo "❌ SKILL.md not found."
    exit 1
fi

echo "🚀 auth-implementation-patterns is ready for use."
exit 0
