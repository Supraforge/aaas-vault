#!/bin/bash
# Health check for Airtable MCP skill
echo "🔍 Checking dependencies for Airtable MCP..."

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js 18+."
    exit 1
else
    echo "✅ Node.js: $(node --version)"
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+."
    exit 1
else
    echo "✅ Python3: $(python3 --version)"
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm."
    exit 1
else
    echo "✅ npm: $(npm --version)"
fi

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Create from .env.template"
    echo "   Required variables: AIRTABLE_TOKEN, AIRTABLE_BASE_ID"
fi

# Check if dependencies are installed
if [ -f package.json ]; then
    echo "📦 Checking Node dependencies..."
    if [ -d node_modules ]; then
        echo "✅ Node dependencies installed"
    else
        echo "⚠️  Node dependencies not installed. Run: npm install"
    fi
fi

if [ -f requirements.txt ]; then
    echo "🐍 Checking Python dependencies..."
    if python3 -c "import airtable-python-wrapper" 2>/dev/null; then
        echo "✅ Python dependencies installed"
    else
        echo "⚠️  Python dependencies not installed. Run: pip install -r requirements.txt"
    fi
fi

echo "✅ Airtable MCP skill health check passed!"
