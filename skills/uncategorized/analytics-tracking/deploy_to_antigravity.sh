#!/bin/bash
# Deploy analytics-tracking skill to Antigravity

SKILL_NAME="analytics-tracking"
TARGET_DIR="$HOME/.gemini/skills/$SKILL_NAME"
SOURCE_DIR="$(dirname "$0")"

echo "Deploying $SKILL_NAME to Antigravity..."
echo "Source: $SOURCE_DIR"
echo "Target: $TARGET_DIR"

# Create target directory
mkdir -p "$TARGET_DIR"

# Copy all files
cp -r "$SOURCE_DIR/"* "$TARGET_DIR/" 2>/dev/null

# Make scripts executable
chmod +x "$TARGET_DIR/"*.sh
chmod +x "$TARGET_DIR/scripts/"*.py 2>/dev/null

# Create .env from template if it doesn't exist
if [ ! -f "$TARGET_DIR/.env" ] && [ -f "$TARGET_DIR/.env.template" ]; then
    cp "$TARGET_DIR/.env.template" "$TARGET_DIR/.env"
    echo "Created .env from template. Please edit with your API keys."
fi

echo ""
echo "✅ Analytics-tracking skill deployed to: $TARGET_DIR"
echo ""
echo "Next steps:"
echo "1. Edit $TARGET_DIR/.env with your API keys"
echo "2. Run test: bash $TARGET_DIR/test.sh"
echo "3. Install dependencies: bash $TARGET_DIR/install.sh"
echo ""
echo "Usage examples:"
echo "  python3 $TARGET_DIR/scripts/analytics_setup.py --provider google-analytics --url https://example.com"
echo "  python3 $TARGET_DIR/scripts/tracking_verifier.py https://example.com"
