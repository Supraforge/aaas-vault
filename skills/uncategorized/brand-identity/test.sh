#!/bin/bash
# Health check for Brand Identity skill
# Verifies all required resource files exist

set -e

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="brand-identity"

echo "🔍 Checking dependencies for ${SKILL_NAME}..."
echo ""

# Check 1: SKILL.md exists
if [[ -f "${SKILL_DIR}/SKILL.md" ]]; then
    echo "✅ SKILL.md found"
else
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check 2: design-tokens.json exists
if [[ -f "${SKILL_DIR}/resources/design-tokens.json" ]]; then
    echo "✅ resources/design-tokens.json found"
else
    echo "❌ resources/design-tokens.json missing"
    exit 1
fi

# Check 3: tech-stack.md exists
if [[ -f "${SKILL_DIR}/resources/tech-stack.md" ]]; then
    echo "✅ resources/tech-stack.md found"
else
    echo "❌ resources/tech-stack.md missing"
    exit 1
fi

# Check 4: voice-tone.md exists
if [[ -f "${SKILL_DIR}/resources/voice-tone.md" ]]; then
    echo "✅ resources/voice-tone.md found"
else
    echo "❌ resources/voice-tone.md missing"
    exit 1
fi

# Check 5: Validate JSON syntax
if command -v python3 &> /dev/null; then
    if python3 -c "import json; json.load(open('${SKILL_DIR}/resources/design-tokens.json'))" 2>/dev/null; then
        echo "✅ design-tokens.json is valid JSON"
    else
        echo "❌ design-tokens.json has invalid JSON syntax"
        exit 1
    fi
else
    echo "⚠️  python3 not found, skipping JSON validation"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 Brand Identity skill is operational!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Remember to customize:"
echo "  - Brand name in SKILL.md"
echo "  - Color values in design-tokens.json"
echo "  - Terminology in voice-tone.md"
