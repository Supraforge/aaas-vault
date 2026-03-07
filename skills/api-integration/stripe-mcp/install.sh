#!/bin/bash
# Installation script for Stripe MCP skill

echo "Installing Stripe MCP skill dependencies..."

# Install Python dependencies
if command -v pip3 &> /dev/null; then
    echo "Installing Python dependencies..."
    pip3 install stripe python-dotenv
elif command -v pip &> /dev/null; then
    echo "Installing Python dependencies..."
    pip install stripe python-dotenv
else
    echo "⚠️  pip not found. Please install pip for Python package management."
fi

# Install Node.js dependencies
if command -v npm &> /dev/null; then
    echo "Installing Node.js dependencies..."
    npm install
else
    echo "⚠️  npm not found. Please install Node.js and npm."
fi

echo "✅ Stripe MCP skill dependencies installed!"
echo "\nNext steps:"
echo "1. Copy .env.template to .env and add your Stripe API keys"
echo "2. Run 'bash test.sh' to verify installation"
echo "3. Start the MCP server with 'npm start'"
