#!/bin/bash
# Instagram API MCP Health Check

echo "🔍 Checking Instagram API MCP dependencies..."

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Install with: apt-get install nodejs"
    exit 1
else
    echo "✅ Node.js $(node --version) installed"
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Install with: apt-get install npm"
    exit 1
else
    echo "✅ npm $(npm --version) installed"
fi

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy from .env.template"
    echo "   cp .env.template .env"
    echo "   Then edit .env with your Instagram API credentials"
fi

# Check required environment variables
if [ -f .env ]; then
    source .env
    if [ -z "$INSTAGRAM_ACCESS_TOKEN" ]; then
        echo "⚠️  INSTAGRAM_ACCESS_TOKEN not set in .env"
    else
        echo "✅ Instagram access token configured"
    fi
    
    if [ -z "$INSTAGRAM_BUSINESS_ACCOUNT_ID" ]; then
        echo "⚠️  INSTAGRAM_BUSINESS_ACCOUNT_ID not set in .env"
    else
        echo "✅ Instagram business account ID configured"
    fi
fi

# Check if server.js exists
if [ ! -f "server.js" ]; then
    echo "⚠️  server.js not found. Run install.sh first"
else
    echo "✅ MCP server implementation found"
fi

echo "\n📊 Instagram API MCP health check completed!"
echo "\nNext steps:"
echo "1. Edit .env with your Instagram API credentials"
echo "2. Run: npm install"
echo "3. Test with: node server.js"
