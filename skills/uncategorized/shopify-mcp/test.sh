#!/bin/bash
# Health check for Shopify MCP skill
echo "🔍 Testing Shopify MCP skill dependencies..."

# Check for required commands
for cmd in python3 node npm; do
    if ! command -v $cmd &> /dev/null; then
        echo "❌ Missing required command: $cmd"
        exit 1
    else
        echo "✅ $cmd found: $(which $cmd)"
    fi
done

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Create from .env.template"
    if [ -f .env.template ]; then
        echo "   Template available: .env.template"
    fi
else
    echo "✅ .env file found"
fi

# Check Python dependencies
if python3 -c "import requests" 2>/dev/null; then
    echo "✅ Python requests library installed"
else
    echo "⚠️  Python requests library not installed"
fi

# Check Node dependencies
if [ -f package.json ]; then
    echo "✅ package.json found"
    if [ -d node_modules ]; then
        echo "✅ node_modules directory exists"
    else
        echo "⚠️  node_modules not found, run 'npm install'"
    fi
fi

echo "✅ Shopify MCP skill health check completed"
exit 0
