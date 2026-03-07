#!/bin/bash
# Health check for Slack MCP skill
echo "🔍 Testing Slack MCP skill dependencies..."

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Install with: apt-get install nodejs"
    exit 1
else
    echo "✅ Node.js: $(node --version)"
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Install with: apt-get install npm"
    exit 1
else
    echo "✅ npm: $(npm --version)"
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Install with: apt-get install python3"
    exit 1
else
    echo "✅ Python3: $(python3 --version)"
fi

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Create from .env.template"
    echo "   Required: SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET"
fi

# Check MCP server dependencies
if [ -f package.json ]; then
    echo "📦 Checking npm dependencies..."
    if [ ! -d node_modules ]; then
        echo "⚠️  node_modules not found. Run: npm install"
    else
        echo "✅ node_modules present"
    fi
fi

echo "\n✅ Slack MCP skill health check completed!"
echo "Next steps:"
echo "1. Copy .env.template to .env and add your Slack tokens"
echo "2. Run: npm install"
echo "3. Start MCP server: node scripts/slack_mcp_server.js"
