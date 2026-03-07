#!/bin/bash
# Health check for HubSpot MCP Integration skill
echo "Checking dependencies for hubspot-mcp-integration..."

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js v16+."
    exit 1
else
    echo "✅ Node.js is installed: $(node --version)"
fi

# Check for npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm."
    exit 1
else
    echo "✅ npm is installed: $(npm --version)"
fi

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Create one from .env.template"
    echo "   Required: HUBSPOT_ACCESS_TOKEN, HUBSPOT_PORTAL_ID"
else
    echo "✅ .env file found"
    # Check for required variables
    if grep -q "HUBSPOT_ACCESS_TOKEN" .env && grep -q "HUBSPOT_PORTAL_ID" .env; then
        echo "✅ Required environment variables found"
    else
        echo "⚠️  Warning: Some required environment variables missing"
    fi
fi

# Check for MCP client installation
if npm list -g @modelcontextprotocol/sdk 2>/dev/null | grep -q @modelcontextprotocol/sdk; then
    echo "✅ MCP SDK is installed"
else
    echo "⚠️  MCP SDK not installed globally. Run: npm install -g @modelcontextprotocol/sdk"
fi

echo "\n✅ HubSpot MCP Integration skill is ready for use!"
echo "To get started:"
echo "1. Configure your .env file with HubSpot credentials"
echo "2. Install HubSpot MCP server: npm install -g @hubspot/mcp-server"
echo "3. Start the MCP server: hubspot-mcp-server"
