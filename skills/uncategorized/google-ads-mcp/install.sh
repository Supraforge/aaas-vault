#!/bin/bash
# Install dependencies for Google Ads MCP

echo "📦 Installing Google Ads MCP dependencies..."

# Install Python dependencies
pip install google-ads pandas numpy matplotlib seaborn

# Install Node.js dependencies (if needed)
if [ -f package.json ]; then
    npm install
fi

# Install system dependencies
apt-get update && apt-get install -y jq curl

echo "✅ Installation complete"
echo ""
echo "🔧 Configuration:"
echo "1. Copy .env.template to .env"
echo "2. Add your Google Ads API credentials to .env"
echo "3. Run test.sh to verify setup"
