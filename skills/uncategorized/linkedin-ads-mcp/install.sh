#!/bin/bash
# Install LinkedIn Ads MCP skill dependencies

echo "📦 Installing LinkedIn Ads MCP skill dependencies..."

# Python dependencies
pip install linkedin-api linkedin-mcp-client requests python-dotenv pandas numpy matplotlib seaborn

# Node.js dependencies
cd scripts
npm install linkedin-api-client axios dotenv csv-writer pdf-lib
cd ..

echo "✅ Dependencies installed successfully!"
echo "\n🔧 Configuration:"
echo "1. Get LinkedIn Marketing API credentials from: https://www.linkedin.com/developers/apps"
echo "2. Copy .env.template to .env"
echo "3. Add your credentials to .env"
echo "4. Run ./test.sh to verify setup"
