#!/bin/bash
echo "Checking TikTok MCP dependencies..."

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found"
    exit 1
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found"
    exit 1
fi

# Check .env file
if [ ! -f .env ]; then
    echo "⚠️  .env file missing - copy from .env.template"
fi

echo "✅ All dependencies verified"
exit 0
