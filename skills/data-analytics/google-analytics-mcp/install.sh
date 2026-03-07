#!/bin/bash
# Install dependencies for Google Analytics MCP

echo "📦 Installing Google Analytics MCP dependencies..."

# Python dependencies
if command -v pip3 &> /dev/null; then
    echo "Installing Python packages..."
    pip3 install google-auth google-auth-oauthlib google-auth-httplib2 \
                 google-api-python-client pandas numpy matplotlib \
                 python-dotenv requests
else
    echo "pip3 not found, skipping Python packages"
fi

# Node.js dependencies (optional)
if command -v npm &> /dev/null && [ -f "scripts/node/package.json" ]; then
    echo "Installing Node.js packages..."
    cd scripts/node && npm install
    cd ../..
fi

# System packages
if command -v apt-get &> /dev/null; then
    echo "Installing system packages..."
    apt-get update && apt-get install -y jq curl
fi

echo "✅ Installation complete"
echo "\nNext: Configure .env file with your Google Cloud credentials"
