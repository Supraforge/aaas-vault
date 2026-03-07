#!/bin/bash
# Install dependencies for Slack MCP skill
echo "Installing Slack MCP skill dependencies..."

# Update package list
apt-get update

# Install Node.js and npm
if ! command -v node &> /dev/null; then
    echo "Installing Node.js..."
    apt-get install -y nodejs npm
fi

# Install Python3 and pip
if ! command -v python3 &> /dev/null; then
    echo "Installing Python3..."
    apt-get install -y python3 python3-pip
fi

# Create package.json if it doesn't exist
if [ ! -f package.json ]; then
    cat > package.json << 'PACKAGE_EOF'
{
  "name": "slack-mcp-server",
  "version": "1.0.0",
  "description": "MCP server for Slack API integration",
  "main": "scripts/slack_mcp_server.js",
  "scripts": {
    "start": "node scripts/slack_mcp_server.js",
    "dev": "nodemon scripts/slack_mcp_server.js"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.6.0",
    "@slack/web-api": "^6.8.1",
    "@slack/bolt": "^3.13.0",
    "express": "^4.18.2",
    "axios": "^1.6.0",
    "dotenv": "^16.3.1",
    "winston": "^3.11.0"
  },
  "devDependencies": {
    "nodemon": "^3.0.1"
  }
}
PACKAGE_EOF
fi

# Install npm dependencies
echo "Installing npm packages..."
npm install

# Install Python dependencies
echo "Installing Python packages..."
pip3 install slack-sdk python-dotenv schedule

echo "\n✅ Slack MCP skill installation complete!"
echo "Next steps:"
echo "1. Configure your .env file with Slack tokens"
echo "2. Run test.sh to verify installation"
echo "3. Start the MCP server with: npm start"
