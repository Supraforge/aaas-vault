#!/bin/bash
# Installation script for visual-designer skill
echo "Checking dependencies for visual-designer..."

# Check Node.js
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo "✓ Node.js found ($NODE_VERSION)"
else
    echo "✗ Node.js not found - please install Node.js"
    exit 1
fi

# Check npm
if command -v npm &> /dev/null; then
    echo "✓ npm found"
else
    echo "✗ npm not found - please install npm"
    exit 1
fi

# Check for @heyputer/puter.js in project
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

if [ -d "$PROJECT_ROOT/node_modules/@heyputer/puter.js" ]; then
    echo "✓ @heyputer/puter.js installed"
else
    echo "✗ @heyputer/puter.js not found"
    echo "  Run: npm install @heyputer/puter.js"
fi

echo ""
echo "Installation check completed"
