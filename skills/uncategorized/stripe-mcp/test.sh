#!/bin/bash
# Health check for Stripe MCP skill

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "🔍 Testing Stripe MCP skill..."

# Check for required dependencies
echo "1. Checking dependencies..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install python3."
    exit 1
fi

if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install node."
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm."
    exit 1
fi

echo "✅ Python3, Node.js, and npm are available"

# Check for .env file
echo "2. Checking environment configuration..."
if [ ! -f "$SKILL_DIR/.env" ]; then
    echo "⚠️  .env file not found. Creating from template..."
    if [ -f "$SKILL_DIR/.env.template" ]; then
        cp "$SKILL_DIR/.env.template" "$SKILL_DIR/.env"
        echo "✅ Created .env from template. Please add your Stripe API keys."
    else
        echo "❌ .env.template not found. Cannot create .env file."
        exit 1
    fi
else
    echo "✅ .env file exists"
fi

# Check Python dependencies
echo "3. Checking Python dependencies..."
if python3 -c "import stripe" 2>/dev/null; then
    echo "✅ Stripe Python library is installed"
else
    echo "⚠️  Stripe Python library not installed. Run 'pip install stripe'"
fi

# Check Node.js dependencies
echo "4. Checking Node.js dependencies..."
if [ -f "$SKILL_DIR/package.json" ]; then
    echo "✅ package.json exists"
else
    echo "⚠️  package.json not found. Creating..."
    cat > "$SKILL_DIR/package.json" << 'PACKAGE_EOF'
{
  "name": "stripe-mcp",
  "version": "1.0.0",
  "description": "Stripe MCP server for payment processing",
  "main": "scripts/stripe_mcp_server.js",
  "scripts": {
    "start": "node scripts/stripe_mcp_server.js",
    "test": "bash test.sh"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.6.0",
    "stripe": "^14.0.0",
    "dotenv": "^16.4.5"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
PACKAGE_EOF
    echo "✅ Created package.json"
fi

echo "\n🎉 Stripe MCP skill health check completed!"
echo "Next steps:"
echo "1. Add your Stripe API keys to .env file"
echo "2. Run 'npm install' to install Node.js dependencies"
echo "3. Run 'pip install stripe' for Python dependencies"
echo "4. Start the MCP server with 'npm start'"
