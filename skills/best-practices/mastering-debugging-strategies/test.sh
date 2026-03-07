#!/bin/bash
# Health check for mastering-debugging-strategies skill

echo "🔍 Validating Debugging Strategies (v3) environment..."

# Check for python3
if command -v python3 &> /dev/null; then
    echo "✅ python3: $(python3 --version)"
else
    echo "⚠️  python3 not found."
fi

# Check for git
if command -v git &> /dev/null; then
    echo "✅ git: $(git --version)"
else
    echo "⚠️  git not found."
fi

echo "🚀 Debugging Strategies (v3) is ready."
exit 0
