#!/bin/bash
# Install Salesforce MCP Dependencies

echo "📦 Installing Salesforce MCP dependencies..."

# Python dependencies
pip install simple-salesforce pandas python-dotenv requests

# Node.js dependencies (if package.json exists)
if [ -f "package.json" ]; then
    npm install
fi

# Install jq for JSON processing
if ! command -v jq &> /dev/null; then
    echo "Installing jq..."
    apt-get update && apt-get install -y jq
fi

echo "✅ Salesforce MCP dependencies installed"
echo "   Next: Copy .env.template to .env and add your Salesforce credentials"
