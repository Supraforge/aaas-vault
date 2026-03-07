#!/bin/bash
# Installation script for HubSpot MCP Integration skill

echo "Installing dependencies for HubSpot MCP Integration..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Node.js not found. Installing Node.js..."
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
    apt-get install -y nodejs
fi

# Install MCP SDK globally
echo "Installing MCP SDK..."
npm install -g @modelcontextprotocol/sdk

# Install HubSpot MCP server
echo "Installing HubSpot MCP server..."
npm install -g @hubspot/mcp-server

# Create local node_modules for skill scripts
mkdir -p scripts
cd scripts
npm init -y
npm install @hubspot/api-client @modelcontextprotocol/client-node

# Make scripts executable
chmod +x ../test.sh
chmod +x ../install.sh

echo "\n✅ HubSpot MCP Integration skill installed successfully!"
echo "Next steps:"
echo "1. Copy .env.template to .env and add your HubSpot credentials"
echo "2. Run test.sh to verify installation"
echo "3. Start the MCP server: hubspot-mcp-server"
