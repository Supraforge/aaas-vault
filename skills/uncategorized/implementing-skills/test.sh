#!/bin/bash
# Health check for implementing-skills

echo "🔍 Validating Skill Implementer..."

# Check 1: Bash
if [ -n "$BASH_VERSION" ]; then
    echo "✅ Bash is available."
else
    echo "❌ Bash not found."
    exit 1
fi

# Check 2: SKILL.md presence
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "$SKILL_DIR/SKILL.md" ]; then
    echo "✅ SKILL.md located."
else
    echo "❌ SKILL.md missing."
    exit 1
fi

echo "🚀 Skill Implementer is ready to execute."
exit 0
