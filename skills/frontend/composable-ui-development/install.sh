#!/bin/bash
# Install dependencies for composable-ui-development

echo "Installing dependencies for composable UI development..."

# Install Node.js if not present
if ! command -v node &> /dev/null; then
    echo "Installing Node.js..."
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
    apt-get install -y nodejs
fi

# Install npm packages for common frameworks
echo "Installing common UI development tools..."
npm install -g create-react-app vue-cli @sveltejs/kit

# Install utility packages
npm install -g prettier eslint stylelint

# Create package.json if it doesn't exist
if [ ! -f package.json ]; then
    echo "Creating package.json..."
    cat > package.json << EOF
{
  "name": "composable-ui-components",
  "version": "1.0.0",
  "description": "Composable UI components library",
  "scripts": {
    "build": "node scripts/compose-ui.js",
    "test": "node scripts/validate-composition.js",
    "lint": "eslint . && stylelint '**/*.css'"
  },
  "dependencies": {
    "react": "^18.0.0",
    "vue": "^3.0.0",
    "svelte": "^4.0.0"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "@types/react": "^18.0.0",
    "@types/node": "^20.0.0",
    "prettier": "^3.0.0",
    "eslint": "^8.0.0",
    "stylelint": "^15.0.0"
  }
}
EOF
fi

echo "
✅ Installation complete!"
echo "Run 'bash test.sh' to verify setup."
