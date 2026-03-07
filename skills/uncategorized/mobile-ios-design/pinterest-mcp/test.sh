#!/bin/bash
# Health check for Pinterest MCP skill
echo "🔍 Testing Pinterest MCP skill..."

# Check for required dependencies
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js."
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm."
    exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3."
    exit 1
fi

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Create from .env.template"
    echo "   Required: PINTEREST_ACCESS_TOKEN"
fi

# Check for required directories
if [ ! -d "scripts" ]; then
    echo "⚠️  Warning: scripts directory missing"
fi

# Test Node.js environment
node --version
npm --version

# Test Python environment
python3 --version

# Test curl for API calls
if command -v curl &> /dev/null; then
    echo "✅ curl available for API testing"
else
    echo "⚠️  curl not found (optional but recommended)"
fi

echo "✅ Pinterest MCP skill health check passed!"
echo ""
echo "Next steps:"
echo "1. Copy .env.template to .env"
echo "2. Add your Pinterest access token"
echo "3. Run: node scripts/pinterest_api.js test"
