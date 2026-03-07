#!/bin/bash
# Install dependencies for e2e-testing-patterns

echo "📦 Installing dependencies for e2e-testing-patterns..."

# Install Playwright
if command -v npm >/dev/null 2>&1; then
    echo "Installing Playwright..."
    npm init -y
    npm install --save-dev playwright
    npx playwright install
    echo "✅ Playwright installed"
else
    echo "❌ npm not installed. Please install Node.js first."
    exit 1
fi

# Install Cypress (optional)
echo "Cypress can be installed via: npm install --save-dev cypress"

echo "🚀 Installation complete."
exit 0
