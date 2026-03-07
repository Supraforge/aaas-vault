#!/bin/bash
# Simple health check for 3D Web Experience skill
echo "Checking dependencies for 3d-web-experience..."

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "⚠️  Warning: Node.js not found. Required for Three.js/React Three Fiber."
else
    echo "✓ Node.js found: $(node --version)"
fi

# Check for npm
if ! command -v npm &> /dev/null; then
    echo "⚠️  Warning: npm not found. Required for package management."
else
    echo "✓ npm found: $(npm --version)"
fi

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "⚠️  Warning: Python 3 not found. Required for some optimization scripts."
else
    echo "✓ Python 3 found: $(python3 --version)"
fi

# Check for .env if API is used
if [ ! -f .env ]; then
    echo "ℹ️  No .env file required for this skill (no external APIs needed)."
fi

echo "
✅ 3D Web Experience skill dependencies checked."
echo "This skill focuses on marketing and content creation using 3D web technologies."
