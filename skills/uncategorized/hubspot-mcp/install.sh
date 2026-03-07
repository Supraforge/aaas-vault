#!/bin/bash
# HubSpot MCP Skill - Installation Script

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "📦 Installing HubSpot MCP skill dependencies..."

# Install Python packages
echo "🐍 Installing Python dependencies..."
pip install hubspot-api-client requests python-dotenv pandas

# Install Node.js packages if package.json exists
if [ -f "$SKILL_DIR/package.json" ]; then
    echo "🟢 Installing Node.js dependencies..."
    npm install
fi

# Create scripts directory if it doesn't exist
mkdir -p "$SKILL_DIR/scripts"

# Make all scripts executable
chmod +x "$SKILL_DIR/scripts/"*.py 2>/dev/null || true
chmod +x "$SKILL_DIR/scripts/"*.sh 2>/dev/null || true
chmod +x "$SKILL_DIR/scripts/"*.js 2>/dev/null || true

echo "✅ Installation complete!"
echo "   Run 'bash test.sh' to verify installation."
