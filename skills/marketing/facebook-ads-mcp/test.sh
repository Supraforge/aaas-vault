#!/bin/bash
# Health check for Facebook Ads MCP skill

echo "🔍 Testing Facebook Ads MCP skill setup..."

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python3."
    exit 1
fi

echo "✅ Python3 is installed"

# Check Node.js installation
if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js not found (optional for JavaScript API)"
fi

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  .env file missing. Creating from template..."
    if [ -f .env.template ]; then
        cp .env.template .env
        echo "✅ .env created from template. Please add your Facebook Ads credentials."
    else
        echo "❌ .env.template not found"
        exit 1
    fi
else
    echo "✅ .env file exists"
fi

# Check required environment variables
if [ -f .env ]; then
    if grep -q "FACEBOOK_ADS_ACCESS_TOKEN" .env && grep -q "FACEBOOK_ADS_ACCOUNT_ID" .env; then
        echo "✅ Required Facebook Ads credentials found in .env"
    else
        echo "⚠️  Missing required Facebook Ads credentials in .env"
    fi
fi

# Test Python dependencies
python3 -c "import facebook_business" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ Facebook Business SDK installed"
else
    echo "⚠️  Facebook Business SDK not installed. Run: pip install facebook-business"
fi

echo "\n✅ Facebook Ads MCP skill is ready!"
echo "Next steps:"
echo "1. Add your Facebook Ads credentials to .env"
echo "2. Run: pip install facebook-business"
echo "3. Test with: python3 scripts/facebook_ads_manager.py --help"
