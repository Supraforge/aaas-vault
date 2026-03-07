#!/bin/bash
# HubSpot MCP Skill - Health Check

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "🔍 Testing HubSpot MCP skill at: $SKILL_DIR"

# Check for required dependencies
echo "📦 Checking dependencies..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install python3."
    exit 1
fi

if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install node."
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm."
    exit 1
fi

# Check Python version
echo "🐍 Python version: $(python3 --version)"

# Check Node version
echo "🟢 Node version: $(node --version)"

# Check for .env file
if [ ! -f "$SKILL_DIR/.env" ]; then
    echo "⚠️  Warning: .env file missing. Create it from .env.template"
    echo "   Required variables: HUBSPOT_ACCESS_TOKEN, HUBSPOT_PORTAL_ID"
fi

# Check Python dependencies
echo "🔧 Checking Python packages..."
python3 -c "import hubspot, requests, json" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Some Python packages missing. Run 'pip install -r requirements.txt'"
fi

# Check Node dependencies
if [ -f "$SKILL_DIR/package.json" ]; then
    echo "📦 Checking Node packages..."
    if [ ! -d "$SKILL_DIR/node_modules" ]; then
        echo "⚠️  node_modules missing. Run 'npm install'"
    fi
fi

echo "✅ HubSpot MCP skill health check completed!"
echo "   Next steps:"
echo "   1. Configure .env with HubSpot credentials"
echo "   2. Run 'bash install.sh' to install dependencies"
echo "   3. Start MCP server: 'node scripts/hubspot_mcp_server.js'"
