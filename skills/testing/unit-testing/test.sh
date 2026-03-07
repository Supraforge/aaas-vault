#!/bin/bash
# Health check for unit-testing skill

echo "🔍 Validating unit-testing skill..."

# Check 1: Core dependencies
echo "\n📦 Checking core dependencies:"

if command -v python3 &> /dev/null; then
    echo "✅ Python3: $(python3 --version 2>&1)"
else
    echo "❌ Python3 not found"
    exit 1
fi

if command -v pytest &> /dev/null; then
    echo "✅ pytest: $(pytest --version 2>&1 | head -1)"
else
    echo "⚠️  pytest not found (will be installed via install.sh)"
fi

if command -v coverage &> /dev/null; then
    echo "✅ coverage: $(coverage --version 2>&1 | head -1)"
else
    echo "⚠️  coverage not found (will be installed via install.sh)"
fi

if command -v jq &> /dev/null; then
    echo "✅ jq: $(jq --version 2>&1)"
else
    echo "⚠️  jq not found (optional for JSON test results)"
fi

if command -v git &> /dev/null; then
    echo "✅ git: $(git --version 2>&1)"
else
    echo "⚠️  git not found (optional for version control integration)"
fi

# Check 2: Directory structure
echo "\n📁 Checking directory structure:"

if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found"
    # Check YAML frontmatter
    if head -5 SKILL.md | grep -q "^---"; then
        echo "✅ YAML frontmatter present"
    else
        echo "⚠️  YAML frontmatter may be missing"
    fi
else
    echo "❌ SKILL.md not found"
    exit 1
fi

if [ -f "install.sh" ]; then
    echo "✅ install.sh found"
    chmod +x install.sh
else
    echo "ℹ️  install.sh not found (optional)"
fi

# Check 3: Test capabilities
echo "\n🧪 Testing basic test generation:"

# Create a simple test to verify Python testing works
cat > test_sample.py << 'PYTEST'
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("✅ Basic test functions work")

if __name__ == "__main__":
    test_add()
PYTEST

python3 test_sample.py
rm test_sample.py

echo "\n🚀 unit-testing skill is ready for:"
echo "   • Test automation with modern frameworks"
echo "   • Debugging and root cause analysis"
echo "   • TDD implementation and tracking"
echo "   • Multi-language test generation"
echo "   • CI/CD integration and quality engineering"

exit 0
