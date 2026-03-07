#!/bin/bash
# Health check for composable-ui-development

echo "🔍 Validating Composable UI engine..."

# Check 1: Node.js
if command -v node &> /dev/null; then
    echo "✅ Node.js found: $(node --version)"
else
    echo "❌ Node.js not found. Required for component generation."
    exit 1
fi

# Check 2: NPM
if command -v npm &> /dev/null; then
    echo "✅ NPM found: $(npm --version)"
else
    echo "❌ NPM not found."
    exit 1
fi

echo "🚀 Composable UI engine is ready."
exit 0
