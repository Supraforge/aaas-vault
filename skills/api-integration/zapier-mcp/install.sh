#!/bin/bash
# Install dependencies for Zapier MCP skill
echo "📦 Installing Zapier MCP skill dependencies..."

# Install Node.js dependencies
if [ -f "package.json" ]; then
    echo "Installing npm packages..."
    npm install
fi

# Install Python dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing Python packages..."
    pip install -r requirements.txt
fi

# Make scripts executable
chmod +x scripts/*.py 2>/dev/null || true
chmod +x scripts/*.sh 2>/dev/null || true

echo "✅ Installation complete!"
echo "\n📋 Next steps:"
echo "1. Configure .env file with your Zapier API key"
echo "2. Run test.sh to verify installation"
echo "3. Start the MCP server: node scripts/zapier_mcp_server.js"
