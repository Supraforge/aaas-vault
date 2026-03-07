#!/bin/bash
# Install dependencies for Notion MCP skill
echo "📦 Installing dependencies for Notion MCP..."

# Install Node dependencies
if [ -f package.json ]; then
    echo "📦 Installing Node packages..."
    npm install
fi

# Install Python dependencies
if [ -f requirements.txt ]; then
    echo "🐍 Installing Python packages..."
    pip install -r requirements.txt
fi

# Create scripts directory if it doesn't exist
mkdir -p scripts

echo "✅ Notion MCP skill installation complete."
echo "Next steps:"
echo "1. Copy .env.template to .env and add your Notion API token"
echo "2. Run './test.sh' to verify installation"
echo "3. Start the MCP server with 'node scripts/notion_mcp_server.js'"
