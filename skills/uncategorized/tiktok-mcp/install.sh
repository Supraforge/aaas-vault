#!/bin/bash
echo "Installing TikTok MCP dependencies..."
npm init -y
npm install axios dotenv node-cache
npm install -g @modelcontextprotocol/sdk

echo "✅ Installation complete"
echo "\nNext steps:"
echo "1. Copy .env.template to .env"
echo "2. Add your TikTok API credentials"
echo "3. Run test.sh to verify setup"
