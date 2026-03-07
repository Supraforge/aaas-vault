#!/bin/bash
# Health check for Google Ads MCP

echo "🔍 Checking Google Ads MCP dependencies..."

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+"
    exit 1
fi

# Check Node.js installation
if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js not found (optional for some features)"
fi

# Check .env file
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy from .env.template"
    echo "   cp .env.template .env"
    echo "   Then edit .env with your Google Ads credentials"
fi

# Check Python dependencies
if python3 -c "import google.ads" 2>/dev/null; then
    echo "✅ Google Ads Python library installed"
else
    echo "⚠️  Google Ads library not installed. Run:"
    echo "   pip install google-ads"
fi

# Check jq for JSON parsing
if ! command -v jq &> /dev/null; then
    echo "⚠️  jq not found. Install with: apt-get install jq"
fi

echo "✅ Google Ads MCP health check completed"
echo ""
echo "📋 Next steps:"
echo "1. Copy .env.template to .env and add your credentials"
echo "2. Run: pip install google-ads"
echo "3. Test with: python3 scripts/google_ads_manager.py --test"
