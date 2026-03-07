#!/bin/bash
# Test script for visual-designer skill
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Testing visual-designer skill..."

# Check SKILL.md exists
if [ -f "SKILL.md" ]; then
    echo "✓ SKILL.md found"
else
    echo "✗ SKILL.md missing"
    exit 1
fi

# Check scripts directory
if [ -d "scripts" ]; then
    echo "✓ scripts/ directory found"
else
    echo "✗ scripts/ directory missing"
    exit 1
fi

# Check generate_image.js exists
if [ -f "scripts/generate_image.js" ]; then
    echo "✓ generate_image.js found"
else
    echo "✗ generate_image.js missing"
    exit 1
fi

# Check Node.js availability
if command -v node &> /dev/null; then
    echo "✓ Node.js available"
else
    echo "✗ Node.js not available"
    exit 1
fi

# Check if puter.js module is installed (from project root)
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
if [ -d "$PROJECT_ROOT/node_modules/@heyputer/puter.js" ]; then
    echo "✓ @heyputer/puter.js module installed"
else
    echo "⚠ @heyputer/puter.js not installed (run: npm install @heyputer/puter.js)"
fi

echo ""
echo "Test completed successfully"
