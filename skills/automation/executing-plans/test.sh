#!/bin/bash
# Health check for executing-plans skill

echo "🔍 Validating executing-plans (v2.2.0)..."

# Check 1: Bash version
if [ -n "$BASH_VERSION" ]; then
    echo "✅ Bash is available."
else
    echo "❌ Bash not found."
    exit 1
fi

# Check 2: Directory integrity (using relative path to script location)
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "$SKILL_DIR/SKILL.md" ]; then
    echo "✅ SKILL.md located at $SKILL_DIR/SKILL.md"
else
    echo "❌ SKILL.md missing."
    exit 1
fi

echo "🚀 executing-plans is ready."
exit 0
