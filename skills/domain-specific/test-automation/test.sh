#!/bin/bash
# Test automation skill health check

echo "🔍 Validating test-automation skill..."

# Check core dependencies
for cmd in python3 nodejs docker git; do
    if command -v $cmd >/dev/null 2>&1; then
        echo "✅ $cmd installed"
    else
        echo "❌ $cmd not found"
        exit 1
    fi
done

# Check testing tools
for cmd in playwright k6; do
    if command -v $cmd >/dev/null 2>&1; then
        echo "✅ $cmd installed"
    else
        echo "⚠️  $cmd not found (may need installation)"
    fi
done

# Check Python packages
if python3 -c "import selenium" 2>/dev/null; then
    echo "✅ selenium Python package installed"
else
    echo "⚠️  selenium Python package not found"
fi

if python3 -c "import playwright" 2>/dev/null; then
    echo "✅ playwright Python package installed"
else
    echo "⚠️  playwright Python package not found"
fi

echo "🚀 test-automation skill is ready for use."
exit 0
