#!/bin/bash
# Install Airtable MCP skill dependencies
echo "Installing Airtable MCP skill dependencies..."

# Install Node dependencies
if [ -f package.json ]; then
    echo "📦 Installing Node dependencies..."
    npm install
    if [ $? -eq 0 ]; then
        echo "✅ Node dependencies installed successfully"
    else
        echo "❌ Failed to install Node dependencies"
        exit 1
    fi
fi

# Install Python dependencies
if [ -f requirements.txt ]; then
    echo "🐍 Installing Python dependencies..."
    pip install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo "✅ Python dependencies installed successfully"
    else
        echo "❌ Failed to install Python dependencies"
        exit 1
    fi
fi

# Create .env file if it doesn't exist
if [ ! -f .env ] && [ -f .env.template ]; then
    echo "⚙️  Creating .env file from template..."
    cp .env.template .env
    echo "⚠️  Please update .env with your Airtable credentials"
fi

echo "✅ Airtable MCP skill installation complete!"
echo "Next steps:"
echo "1. Update .env with your Airtable credentials"
echo "2. Run test.sh to verify installation"
echo "3. Start the MCP server with: node scripts/airtable_mcp_server.js"
