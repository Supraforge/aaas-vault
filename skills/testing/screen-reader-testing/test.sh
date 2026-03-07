#!/bin/bash
# Health check for screen-reader-testing skill

echo "🔍 Validating screen-reader-testing skill..."

# Check 1: Directory structure
if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found."
else
    echo "❌ SKILL.md missing!"
    exit 1
fi

# Check 2: YAML frontmatter
if grep -q '^---' SKILL.md && grep -q 'name: screen-reader-testing' SKILL.md; then
    echo "✅ YAML frontmatter valid."
else
    echo "❌ YAML frontmatter invalid!"
    exit 1
fi

# Check 3: Required sections
if grep -q '## When to Use This Skill' SKILL.md && grep -q '## Core Concepts' SKILL.md; then
    echo "✅ Required sections present."
else
    echo "❌ Required sections missing!"
    exit 1
fi

echo "🚀 screen-reader-testing skill is ready for use."
exit 0
