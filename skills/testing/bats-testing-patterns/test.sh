#!/bin/bash
# Health check for bats-testing-patterns skill

echo "🔍 Validating bats-testing-patterns..."

# Check bats availability
if command -v bats &> /dev/null; then
    echo "✅ Bats is available."
else
    echo "❌ Bats is not installed. Please install bats-core."
    exit 1
fi

# Check skill structure
if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found."
else
    echo "❌ SKILL.md not found."
    exit 1
fi

echo "🚀 bats-testing-patterns is ready."
exit 0
