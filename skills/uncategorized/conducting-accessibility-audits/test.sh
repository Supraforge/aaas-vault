#!/bin/bash
# Health check for accessibility auditing skill

echo "🔍 Validating accessibility auditing skill..."

# Check 1: Node.js
if command -v node &> /dev/null; then
    echo "✅ Node.js found: $(node --version)"
else
    echo "❌ Node.js not found. Please install Node.js."
    exit 1
fi

# Check 2: npm or yarn
if command -v npm &> /dev/null; then
    echo "✅ npm found: $(npm --version)"
elif command -v yarn &> /dev/null; then
    echo "✅ yarn found: $(yarn --version)"
else
    echo "⚠️  No package manager found (npm or yarn). Some dependencies may not be installable."
fi

# Check 3: axe-core availability (try to run a simple check)
echo "Checking for axe-core..."
npx axe --version 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ axe-core is available via npx"
else
    echo "ℹ️  axe-core not installed globally. It will be installed when needed via npx."
fi

# Check 4: Basic browser automation tools
echo "Checking for browser automation..."
if command -v google-chrome &> /dev/null || command -v chromium &> /dev/null || command -v chromium-browser &> /dev/null; then
    echo "✅ Chrome/Chromium browser found"
else
    echo "⚠️  Chrome/Chromium not found. Puppeteer may install it, but manual installation might be needed."
fi

# Check 5: Screen reader testing tools (simulated check)
echo "Checking screen reader testing environment..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "✅ macOS detected - VoiceOver available"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "✅ Linux detected - Orca screen reader may be available"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "✅ Windows detected - NVDA/JAWS/Narrator available"
else
    echo "ℹ️  Unknown OS: $OSTYPE. Screen reader testing may require manual setup."
fi

echo "🚀 Accessibility auditing skill is ready."
echo ""
echo "To install dependencies, run:"
echo "  bash ~/.gemini/skills/conducting-accessibility-audits/install.sh"

exit 0
