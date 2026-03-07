#!/bin/bash
# Health check for Google Analytics MCP skill

echo "🔍 Testing Google Analytics MCP skill..."

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy from .env.template"
    echo "   Required variables: GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET"
fi

# Check Python dependencies
if command -v python3 &> /dev/null; then
    echo "✅ Python3 available"
    python3 -c "import google.auth" 2>/dev/null && echo "✅ Google Auth library installed" || echo "⚠️  Install: pip install google-auth google-auth-oauthlib google-auth-httplib2"
else
    echo "❌ Python3 not found"
fi

# Check Node.js dependencies
if command -v node &> /dev/null; then
    echo "✅ Node.js available"
    if [ -f "scripts/node/package.json" ]; then
        echo "✅ Node.js package.json found"
    fi
else
    echo "⚠️  Node.js not found (optional for Node implementation)"
fi

# Check for required tools
for cmd in jq curl; do
    if command -v $cmd &> /dev/null; then
        echo "✅ $cmd available"
    else
        echo "⚠️  $cmd not found"
    fi
done

echo "\n📊 Google Analytics MCP skill health check complete"
echo "Next steps:"
echo "1. Set up Google Cloud project with Analytics API enabled"
echo "2. Create OAuth credentials and add to .env"
echo "3. Run examples to test connectivity"
