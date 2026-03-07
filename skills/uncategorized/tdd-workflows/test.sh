#!/bin/bash
# Health check for TDD Workflows skill

echo "🔍 Validating TDD Workflows environment..."

# Check 1: Python availability
if command -v python3 &> /dev/null; then
    echo "✅ Python3 is available"
else
    echo "❌ Python3 not found. Please install Python 3.8+"
    exit 1
fi

# Check 2: Git availability
if command -v git &> /dev/null; then
    echo "✅ Git is available"
else
    echo "❌ Git not found. Please install git"
    exit 1
fi

# Check 3: jq availability
if command -v jq &> /dev/null; then
    echo "✅ jq is available"
else
    echo "⚠️  jq not found. Some JSON parsing features may be limited"
fi

# Check 4: Python testing packages
if python3 -c "import pytest" 2>/dev/null; then
    echo "✅ pytest is installed"
else
    echo "⚠️  pytest not installed. Run install.sh to install dependencies"
fi

if python3 -c "import coverage" 2>/dev/null; then
    echo "✅ coverage is installed"
else
    echo "⚠️  coverage not installed. Run install.sh to install dependencies"
fi

# Check 5: Test directory structure
if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found"
else
    echo "❌ SKILL.md not found"
    exit 1
fi

echo "🚀 TDD Workflows environment is ready for orchestration"
echo ""
echo "Available TDD phases:"
echo "  • RED: Write failing tests"
echo "  • GREEN: Implement minimal solution"
echo "  • REFACTOR: Improve code quality"
echo "  • CYCLE: Complete RED-GREEN-REFACTOR cycle"

exit 0
