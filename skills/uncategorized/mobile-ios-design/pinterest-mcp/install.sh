#!/bin/bash
# Install dependencies for Pinterest MCP skill
echo "📦 Installing Pinterest MCP skill dependencies..."

# Install Node.js dependencies
if [ -f "package.json" ]; then
    npm install
else
    # Create minimal package.json
    cat > package.json << 'PACKAGE_EOF'
{
  "name": "pinterest-mcp",
  "version": "1.0.0",
  "description": "Pinterest API MCP integration",
  "main": "scripts/pinterest_api.js",
  "scripts": {
    "test": "node scripts/pinterest_api.js test",
    "start": "node scripts/mcp_server.js"
  },
  "dependencies": {
    "axios": "^1.6.0",
    "dotenv": "^16.3.0",
    "@modelcontextprotocol/sdk": "^0.4.0"
  },
  "engines": {
    "node": ">=16.0.0"
  }
}
PACKAGE_EOF
    
    npm install axios dotenv @modelcontextprotocol/sdk
fi

# Install Python dependencies for analytics
if command -v pip3 &> /dev/null; then
    pip3 install pandas matplotlib
elif command -v pip &> /dev/null; then
    pip install pandas matplotlib
else
    echo "⚠️  pip not found. Python analytics features may not work."
fi

echo "✅ Pinterest MCP skill installation complete!"
echo ""
echo "To start the MCP server:"
echo "1. Configure .env file with your Pinterest token"
echo "2. Run: npm start"
echo ""
echo "To test the API:"
echo "Run: npm test"
