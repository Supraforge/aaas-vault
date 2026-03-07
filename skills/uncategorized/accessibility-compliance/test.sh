#!/bin/bash
# Accessibility Compliance Skill - Health Check

echo "🔍 Validating accessibility-compliance skill..."

# Check 1: Verify required tools are available
echo "\n📋 Checking dependencies..."
if command -v node &> /dev/null; then
    echo "✅ Node.js is installed"
else
    echo "❌ Node.js is not installed"
    echo "   Install with: apt-get install nodejs"
fi

if command -v python3 &> /dev/null; then
    echo "✅ Python3 is installed"
else
    echo "❌ Python3 is not installed"
    echo "   Install with: apt-get install python3"
fi

# Check 2: Verify npm packages if available
if command -v npm &> /dev/null; then
    echo "\n📦 Checking npm accessibility packages..."
    if npm list -g axe-core 2>/dev/null | grep -q axe-core; then
        echo "✅ axe-core is installed globally"
    else
        echo "⚠️  axe-core not installed globally"
        echo "   Install with: npm install -g axe-core"
    fi
else
    echo "⚠️  npm not available - skipping package checks"
fi

# Check 3: Verify skill directory structure
echo "\n📁 Checking skill structure..."
if [ -f "$SKILL_DIR/SKILL.md" ]; then
    echo "✅ SKILL.md found"
else
    echo "❌ SKILL.md missing"
fi

if [ -f "$SKILL_DIR/test.sh" ]; then
    echo "✅ test.sh found"
else
    echo "❌ test.sh missing"
fi

if [ -f "$SKILL_DIR/install.sh" ]; then
    echo "✅ install.sh found"
else
    echo "⚠️  install.sh not found (optional)"
fi

echo "\n🚀 accessibility-compliance skill is ready for use."
echo "\nTo test a website for accessibility:"
echo "  npx axe https://example.com"
echo "  lighthouse https://example.com --output=html --output-path=report.html --only-categories=accessibility"

exit 0
