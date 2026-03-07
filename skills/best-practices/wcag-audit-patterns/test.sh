#!/bin/bash
# Health check for wcag-audit-patterns skill

echo "🔍 Validating wcag-audit-patterns skill..."

# Check 1: SKILL.md exists
if [ ! -f "SKILL.md" ]; then
    echo "❌ SKILL.md not found"
    exit 1
fi

echo "✅ SKILL.md found"

# Check 2: YAML frontmatter exists
if ! head -10 "SKILL.md" | grep -q "^---$"; then
    echo "❌ YAML frontmatter not found"
    exit 1
fi

echo "✅ YAML frontmatter present"

# Check 3: Required sections exist
if ! grep -q "## When to Use This Skill" "SKILL.md"; then
    echo "⚠️  'When to Use This Skill' section not found"
fi

if ! grep -q "## Core Concepts" "SKILL.md"; then
    echo "⚠️  'Core Concepts' section not found"
fi

if ! grep -q "## Audit Checklist" "SKILL.md"; then
    echo "⚠️  'Audit Checklist' section not found"
fi

echo "✅ Skill structure validated"
echo "🚀 wcag-audit-patterns is ready for use"

exit 0
