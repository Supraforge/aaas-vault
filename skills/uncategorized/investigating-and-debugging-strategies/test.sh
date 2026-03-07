#!/bin/bash
# Health check for investigating-and-debugging-strategies skill

echo "🔍 Validating Debugging Strategies Skill environment..."

# Check for git (essential for git bisect)
if command -v git &> /dev/null; then
    echo "✅ git located: $(git --version)"
else
    echo "❌ git not found. Advanced techniques like bisect will fail."
    exit 1
fi

# Check for python3 (for profiling templates)
if command -v python3 &> /dev/null; then
    echo "✅ python3 located: $(python3 --version)"
else
    echo "⚠️  python3 not found. Python-specific templates will be reference-only."
fi

echo "🚀 Debugging Strategies Skill is ready for use."
exit 0
