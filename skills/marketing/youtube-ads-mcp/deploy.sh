#!/bin/bash
# Deploy YouTube Ads MCP skill to AntiGravity

SKILL_NAME="youtube-ads-mcp"
TARGET_DIR="$HOME/.gemini/skills/$SKILL_NAME"

echo "🚀 Deploying YouTube Ads MCP skill..."

# Create target directory
mkdir -p "$TARGET_DIR"

# Copy all files
cp -r . "$TARGET_DIR/"

# Set permissions
chmod +x "$TARGET_DIR/test.sh"
chmod +x "$TARGET_DIR/install.sh"
chmod +x "$TARGET_DIR/scripts/"*.py

# Install Node.js dependencies if npm is available
if command -v npm &> /dev/null; then
    echo "📦 Installing Node.js dependencies..."
    cd "$TARGET_DIR/scripts"
    npm install --silent
    cd ..
fi

echo "✅ YouTube Ads MCP skill deployed to: $TARGET_DIR"
echo ""
echo "📋 Next steps:"
echo "1. cd $TARGET_DIR"
echo "2. cp .env.template .env"
echo "3. Add your Google API credentials to .env"
echo "4. Run ./test.sh to verify setup"
echo "5. Run ./install.sh to install dependencies"
echo ""
echo "🚀 Next: Creating Snapchat Ads MCP skill..."
