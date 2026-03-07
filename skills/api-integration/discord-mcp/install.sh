#!/bin/bash
# Install Discord MCP dependencies

echo "Installing Discord MCP skill dependencies..."

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "Node.js not found. Installing..."
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
    apt-get install -y nodejs
fi

# Install npm packages
cd "$(dirname "$0")"
npm init -y
npm install discord.js @modelcontextprotocol/sdk axios dotenv
npm install -D nodemon

# Install Python dependencies if needed
if command -v python3 &> /dev/null; then
    pip3 install discord.py python-dotenv pandas matplotlib
fi

echo "✅ Discord MCP dependencies installed successfully!"
echo ""
echo "Next steps:"
echo "1. Create a Discord bot at https://discord.com/developers/applications"
echo "2. Copy the bot token to .env file"
echo "3. Invite the bot to your server"
echo "4. Run test.sh to verify installation"
