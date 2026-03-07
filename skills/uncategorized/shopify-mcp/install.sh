#!/bin/bash
# Install dependencies for Shopify MCP skill
echo "📦 Installing Shopify MCP skill dependencies..."

# Python dependencies
pip install requests python-dotenv shopify-api-python

# Node dependencies
if [ -f package.json ]; then
    npm install
else
    echo "⚠️  package.json not found, creating basic one"
    cat > package.json << 'PACKAGE_EOF'
{
  "name": "shopify-mcp",
  "version": "1.0.0",
  "description": "Shopify MCP integration for e-commerce automation",
  "main": "scripts/shopify_mcp_server.js",
  "scripts": {
    "start": "node scripts/shopify_mcp_server.js",
    "test": "bash test.sh"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.6.0",
    "axios": "^1.6.0",
    "dotenv": "^16.4.5",
    "shopify-api-node": "^3.12.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
PACKAGE_EOF
    npm install
fi

echo "✅ Shopify MCP skill installation completed"
