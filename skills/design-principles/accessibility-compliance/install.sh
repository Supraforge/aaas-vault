#!/bin/bash
# Accessibility Compliance Skill - Installation Script

echo "📦 Installing dependencies for accessibility-compliance skill..."

# Update package list
echo "\n🔄 Updating package lists..."
apt-get update

# Install Node.js if not present
if ! command -v node &> /dev/null; then
    echo "\n📥 Installing Node.js..."
    apt-get install -y nodejs npm
fi

# Install Python3 if not present
if ! command -v python3 &> /dev/null; then
    echo "\n🐍 Installing Python3..."
    apt-get install -y python3 python3-pip
fi

# Install global npm packages for accessibility testing
echo "\n📦 Installing accessibility testing tools..."
npm install -g axe-core lighthouse

# Install Python accessibility libraries
echo "\n🐍 Installing Python accessibility libraries..."
pip3 install --upgrade pip
pip3 install accessibility colorcontrast

echo "\n✅ Installation complete!"
echo "\n📋 Available commands:"
echo "  • npx axe https://example.com"
echo "  • lighthouse https://example.com --output=html --output-path=report.html --only-categories=accessibility"
echo "  • python3 -c 'import accessibility; print(accessibility.__version__)'"

exit 0
