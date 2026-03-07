#!/bin/bash
# Health check for Zapier MCP skill
echo "🔍 Testing Zapier MCP skill dependencies..."

# Check Node.js version
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Install with: apt-get install nodejs"
    exit 1
fi

NODE_VERSION=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
    echo "❌ Node.js version must be 18+. Current: $(node --version)"
    exit 1
fi

echo "✅ Node.js $(node --version) detected"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found"
    exit 1
fi

echo "✅ Python3 $(python3 --version) detected"

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Create from .env.template"
    echo "   Required: ZAPIER_API_KEY=your_personal_access_token"
fi

# Check npm dependencies
if [ -f "package.json" ]; then
    echo "📦 Checking npm dependencies..."
    if [ ! -d "node_modules" ]; then
        echo "⚠️  node_modules missing. Run: npm install"
    else
        echo "✅ node_modules present"
    fi
fi

# Check Python dependencies
if [ -f "requirements.txt" ]; then
    echo "🐍 Checking Python dependencies..."
    if ! python3 -c "import requests" &> /dev/null; then
        echo "⚠️  Python requests module not installed"
    else
        echo "✅ Python requests module available"
    fi
fi

echo "\n✅ Zapier MCP skill health check passed!"
echo "\n📋 Next steps:"
echo "1. Copy .env.template to .env and add your Zapier API key"
echo "2. Run: npm install (for Node.js MCP server)"
echo "3. Run: pip install -r requirements.txt (for Python scripts)"
echo "4. Start MCP server: node scripts/zapier_mcp_server.js"
