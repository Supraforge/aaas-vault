#!/bin/bash
# Health check for applying-debugging-strategies skill

echo "🔍 Validating Debugging Strategies environment..."

# Check for python3
if command -v python3 &> /dev/null; then
    echo "✅ python3 located: $(python3 --version)"
else
    echo "⚠️  python3 not found. Python-specific templates will be reference-only."
fi

# Check for git
if command -v git &> /dev/null; then
    echo "✅ git located: $(git --version)"
else
    echo "⚠️  git not found. Binary search debugging techniques may be limited."
fi

echo "🚀 Debugging Strategies Skill is ready."
exit 0
