#!/bin/bash
# Team Collaboration Skill - Health Check

echo "🔍 Validating team-collaboration skill..."

# Check 1: Directory structure
if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found"
else
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check 2: Dependencies
for dep in git jq curl; do
    if command -v $dep >/dev/null 2>&1; then
        echo "✅ $dep installed"
    else
        echo "⚠️  $dep not found (optional for some features)"
    fi
done

# Check 3: Git configuration
git config --get user.name >/dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Git user configured"
else
    echo "⚠️  Git user not configured (standup notes may be limited)"
fi

# Check 4: YAML frontmatter
if grep -q '^---$' SKILL.md && grep -q 'name: team-collaboration' SKILL.md; then
    echo "✅ YAML frontmatter valid"
else
    echo "❌ YAML frontmatter missing or incorrect"
    exit 1
fi

echo ""
echo "🚀 Team collaboration skill is ready!"
echo ""
echo "Available capabilities:"
echo "• Standup notes generation from Git history"
echo "• Developer experience optimization"
echo "• Issue investigation and resolution"
echo "• Team communication workflows"

exit 0
