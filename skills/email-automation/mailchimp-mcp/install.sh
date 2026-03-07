#!/bin/bash
# Install Mailchimp MCP Skill Dependencies
echo "📦 Installing Mailchimp MCP skill dependencies..."

# Install Python dependencies
pip3 install requests python-dotenv

# Install Node.js dependencies
if [ -f package.json ]; then
    npm install
else
    echo "⚠️  package.json not found, creating basic one..."
    cat > package.json << 'PACKAGE_EOF'
{
  "name": "mailchimp-mcp",
  "version": "1.0.0",
  "description": "Mailchimp MCP server for email marketing automation",
  "main": "scripts/mailchimp_mcp_server.js",
  "scripts": {
    "start": "node scripts/mailchimp_mcp_server.js",
    "test": "bash test.sh"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.6.0",
    "mailchimp-api-v3": "^1.15.0",
    "dotenv": "^16.4.5"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
PACKAGE_EOF
    npm install
fi

echo "✅ Mailchimp MCP skill dependencies installed"
echo ""
echo "Next steps:"
echo "1. Copy .env.template to .env"
echo "2. Add your Mailchimp API credentials to .env"
echo "3. Run test.sh to verify installation"
