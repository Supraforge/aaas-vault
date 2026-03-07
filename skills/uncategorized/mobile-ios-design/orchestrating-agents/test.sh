#!/bin/bash
# Health check for orchestrating-agents skill

echo "🔍 Validating orchestrating-agents skill..."

# Check 1: Verify skill directory structure
if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found"
else
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check 2: Verify YAML frontmatter
if grep -q "^---$" SKILL.md && grep -q "^name: orchestrating-agents$" SKILL.md; then
    echo "✅ YAML frontmatter valid"
else
    echo "❌ YAML frontmatter invalid"
    exit 1
fi

# Check 3: Verify dependencies
REQUIRED_DEPS=("python3" "jq" "git")
for dep in "${REQUIRED_DEPS[@]}"; do
    if command -v "$dep" >/dev/null 2>&1; then
        echo "✅ $dep installed"
    else
        echo "⚠️  $dep not found (some features may not work)"
    fi
done

# Check 4: Verify scripts directory (optional)
if [ -d "scripts" ]; then
    echo "✅ scripts directory found"
    SCRIPTS_COUNT=$(find scripts -name "*.sh" -o -name "*.py" | wc -l)
    echo "📊 Found $SCRIPTS_COUNT script files"
else
    echo "ℹ️  No scripts directory (optional)"
fi

echo "🚀 orchestrating-agents skill is ready for use."
echo "\n📋 Skill Overview:"
echo "- Agent performance optimization and analysis"
echo "- Multi-agent coordination and task decomposition"
echo "- Context management and distribution"
echo "- Continuous improvement workflows"

exit 0
