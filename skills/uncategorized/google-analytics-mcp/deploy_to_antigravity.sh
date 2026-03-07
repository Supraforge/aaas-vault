#!/bin/bash
# Deploy Google Analytics MCP to AntiGravity

SKILL_NAME="google-analytics-mcp"
TARGET_DIR="$HOME/.gemini/skills/$SKILL_NAME"

echo "🚀 Deploying $SKILL_NAME to AntiGravity..."

# Create target directory
mkdir -p "$TARGET_DIR"

# Copy all files
cp -r ./* "$TARGET_DIR/" 2>/dev/null
cp -r ./.env.template "$TARGET_DIR/" 2>/dev/null

# Make scripts executable
chmod +x "$TARGET_DIR/test.sh"
chmod +x "$TARGET_DIR/install.sh"
chmod +x "$TARGET_DIR/scripts/python/analytics.py"
chmod +x "$TARGET_DIR/examples/python_usage.py"

echo "✅ Google Analytics MCP deployed to: $TARGET_DIR"
echo ""
echo "📋 Next steps:"
echo "1. cd $TARGET_DIR"
echo "2. cp .env.template .env"
echo "3. Add your Google Cloud credentials to .env"
echo "4. Run ./test.sh to verify setup"
echo "5. Run ./install.sh to install dependencies"
echo ""
echo "🔗 Skill will be available in AntiGravity as: $SKILL_NAME"
