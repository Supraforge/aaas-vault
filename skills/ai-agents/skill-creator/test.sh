#!/bin/bash
# Health check for Antigravity Skill Creator
# This script verifies the meta-skill is properly installed

set -e

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="skill-creator"

echo "🔍 Checking dependencies for ${SKILL_NAME}..."
echo ""

# Check 1: SKILL.md exists
if [[ -f "${SKILL_DIR}/SKILL.md" ]]; then
    echo "✅ SKILL.md found"
else
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check 2: SKILL.md has proper frontmatter
if head -n 20 "${SKILL_DIR}/SKILL.md" | grep -q "inputs:"; then
    echo "✅ SKILL.md contains 'inputs' definition (v2.4+)"
else
    echo "⚠️  SKILL.md frontmatter might be outdated (missing 'inputs')."
fi

if head -1 "${SKILL_DIR}/SKILL.md" | grep -q "^---$"; then
    echo "✅ YAML frontmatter detected"
else
    echo "❌ YAML frontmatter missing or malformed"
    exit 1
fi

# Check 3: bash is available
if command -v bash &> /dev/null; then
    echo "✅ bash is available ($(bash --version | head -1))"
else
    echo "❌ bash is not available"
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 Antigravity Skill Creator is operational!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "You can now use this skill to create new agent capabilities."
echo "Location: ${SKILL_DIR}"