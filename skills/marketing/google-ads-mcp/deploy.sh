#!/bin/bash
# Deploy Google Ads MCP skill to AntiGravity

SKILL_NAME="google-ads-mcp"
TARGET_DIR="$HOME/.gemini/skills/$SKILL_NAME"

echo "🚀 Deploying Google Ads MCP skill..."

# Create target directory
mkdir -p "$TARGET_DIR"

# Copy all files
cp -r . "$TARGET_DIR/"

# Set permissions
chmod +x "$TARGET_DIR/test.sh"
chmod +x "$TARGET_DIR/install.sh"
chmod +x "$TARGET_DIR/scripts/"*.py

echo "✅ Google Ads MCP skill deployed to: $TARGET_DIR"
echo ""
echo "📋 Next steps:"
echo "1. cd $TARGET_DIR"
echo "2. cp .env.template .env"
echo "3. Add your Google Ads credentials to .env"
echo "4. Run ./test.sh to verify setup"
