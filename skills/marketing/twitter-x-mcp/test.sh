#!/bin/bash
# Health check for Twitter/X API MCP skill

echo "🔍 Testing Twitter/X API MCP skill..."

# Check if in correct directory
if [ ! -f "SKILL.md" ]; then
    echo "❌ Error: Not in Twitter/X MCP skill directory"
    exit 1
fi

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file missing. Create from .env.template"
    echo "   cp .env.template .env"
    echo "   Then add your Twitter API credentials"
fi

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Error: Node.js not found. Install with: apt-get install nodejs"
    exit 1
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ Error: npm not found. Install with: apt-get install npm"
    exit 1
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python3 not found. Install with: apt-get install python3"
    exit 1
fi

# Check jq
if ! command -v jq &> /dev/null; then
    echo "⚠️  Warning: jq not found. Install with: apt-get install jq"
fi

# Check if server.js exists
if [ ! -f "server.js" ]; then
    echo "⚠️  Warning: server.js not found. Run install.sh first"
fi

# Check package.json
if [ ! -f "package.json" ]; then
    echo "⚠️  Warning: package.json not found. Run install.sh first"
fi

echo "✅ All basic checks passed!"
echo ""
echo "📋 Next steps:"
echo "   1. Edit .env file with your Twitter API credentials"
echo "   2. Run 'npm install' to install dependencies"
echo "   3. Start server: 'node server.js'"
echo "   4. Connect using any MCP client"
