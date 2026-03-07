#!/bin/bash
# Test Discord MCP installation

echo "Testing Discord MCP skill installation..."

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
    echo "⚠️  Warning: .env file not found"
    echo "   Copy .env.template to .env and add your Discord bot token"
fi

# Check dependencies
if [ -f package.json ]; then
    echo "Checking npm packages..."
    if ! npm list discord.js &> /dev/null; then
        echo "⚠️  discord.js not installed. Run install.sh"
    fi
fi

echo "✅ Basic checks passed"
echo ""
echo "To test Discord connection:"
echo "1. Ensure .env has DISCORD_BOT_TOKEN"
echo "2. Run: node scripts/discord_bot.js"
