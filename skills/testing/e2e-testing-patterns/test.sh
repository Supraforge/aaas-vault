#!/bin/bash
# Health check for e2e-testing-patterns

echo "🔍 Validating e2e-testing-patterns..."

# Check Node.js
if command -v node >/dev/null 2>&1; then
    echo "✅ Node.js installed: $(node --version)"
else
    echo "❌ Node.js not installed"
    exit 1
fi

# Check Playwright
if command -v npx >/dev/null 2>&1; then
    echo "✅ npx available"
else
    echo "❌ npx not available (install npm)"
    exit 1
fi

# Check Cypress (optional)
echo "ℹ️  Cypress can be installed via npm if needed"

echo "🚀 e2e-testing-patterns is ready."
exit 0
