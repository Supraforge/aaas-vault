#!/bin/bash
# Install dependencies for Facebook Ads MCP skill

echo "📦 Installing Facebook Ads MCP dependencies..."

# Install Python dependencies
if command -v pip3 &> /dev/null; then
    pip3 install facebook-business pandas numpy matplotlib
elif command -v pip &> /dev/null; then
    pip install facebook-business pandas numpy matplotlib
else
    echo "❌ pip not found. Please install pip first."
    exit 1
fi

echo "✅ Python dependencies installed"

# Install Node.js dependencies (optional)
if command -v npm &> /dev/null; then
    cd scripts
    npm install facebook-nodejs-business-sdk axios csv-writer
    cd ..
    echo "✅ Node.js dependencies installed"
else
    echo "⚠️  npm not found. Skipping Node.js dependencies."
fi

# Create scripts directory
mkdir -p scripts

echo "\n✅ Installation complete!"
echo "Next steps:"
echo "1. Copy .env.template to .env"
echo "2. Add your Facebook Ads credentials to .env"
echo "3. Run ./test.sh to verify setup"
