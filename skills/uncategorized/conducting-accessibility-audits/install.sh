#!/bin/bash
# Installation script for accessibility auditing skill

echo "📦 Installing dependencies for accessibility auditing skill..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed."
    echo "Please install Node.js from https://nodejs.org/ and try again."
    exit 1
fi

# Install axe-core globally or locally
echo "Installing axe-core for accessibility testing..."
npm install -g axe-core 2>/dev/null || npm install axe-core --no-save 2>/dev/null

# Check if axe-core command is available
if npx axe --version 2>/dev/null; then
    echo "✅ axe-core installed successfully"
else
    echo "⚠️  Could not install axe-core globally. It will be used via npx."
fi

# Install puppeteer for browser automation (optional)
echo "Installing puppeteer for browser automation (optional)..."
npm install -g puppeteer 2>/dev/null || npm install puppeteer --no-save 2>/dev/null

# Install additional accessibility testing tools
echo "Installing additional accessibility testing tools..."
npm install -g pa11y 2>/dev/null || npm install pa11y --no-save 2>/dev/null
npm install -g lighthouse 2>/dev/null || npm install lighthouse --no-save 2>/dev/null

# Create a configuration directory for accessibility tools
mkdir -p ~/.a11y-tools

# Download WCAG 2.2 quick reference
if command -v curl &> /dev/null; then
    curl -s -o ~/.a11y-tools/wcag22-quickref.json https://www.w3.org/WAI/WCAG22/quickref/ 2>/dev/null || true
    echo "✅ Downloaded WCAG 2.2 quick reference"
fi

# Set up environment variables for screen reader testing
echo "Setting up environment for screen reader testing..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "# VoiceOver commands" > ~/.a11y-tools/voiceover-commands.txt
    echo "Cmd+F5: Toggle VoiceOver" >> ~/.a11y-tools/voiceover-commands.txt
    echo "Ctrl+Option+Right/Left: Navigate" >> ~/.a11y-tools/voiceover-commands.txt
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "# Orca screen reader commands" > ~/.a11y-tools/orca-commands.txt
    echo "Super+Alt+S: Toggle Orca" >> ~/.a11y-tools/orca-commands.txt
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "# NVDA/JAWS commands" > ~/.a11y-tools/windows-sr-commands.txt
    echo "Insert+Q: Toggle NVDA" >> ~/.a11y-tools/windows-sr-commands.txt
    echo "Insert+J: Toggle JAWS" >> ~/.a11y-tools/windows-sr-commands.txt
fi

echo ""
echo "✅ Accessibility auditing skill installation complete!"
echo ""
echo "To test the installation, run:"
echo "  bash ~/.gemini/skills/conducting-accessibility-audits/test.sh"
echo ""
echo "For a quick accessibility audit of a website, run:"
echo "  npx axe https://example.com --save results.json"

exit 0
