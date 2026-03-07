#!/bin/bash
# Health check for Facebook Marketing API MCP skill

echo "🔍 Testing Facebook Marketing API MCP skill..."

# Check for required files
required_files=("SKILL.md" "test.sh" ".env.template" "install.sh")
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Missing required file: $file"
        exit 1
    fi
done
echo "✅ All required files present"

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js not found. Required for MCP server."
else
    echo "✅ Node.js version: $(node --version)"
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo "⚠️  npm not found. Required for dependencies."
else
    echo "✅ npm version: $(npm --version)"
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "⚠️  Python 3 not found. Required for analytics scripts."
else
    echo "✅ Python 3 version: $(python3 --version)"
fi

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚠️  .env file missing. Copy .env.template to .env and add credentials."
    echo "   Required credentials:"
    echo "   - FACEBOOK_APP_ID"
    echo "   - FACEBOOK_APP_SECRET"
    echo "   - FACEBOOK_ACCESS_TOKEN"
    echo "   - FACEBOOK_AD_ACCOUNT_ID"
    echo "   - FACEBOOK_BUSINESS_ID"
else
    echo "✅ .env file present"
    # Check for required variables
    required_vars=("FACEBOOK_APP_ID" "FACEBOOK_APP_SECRET" "FACEBOOK_ACCESS_TOKEN")
    for var in "${required_vars[@]}"; do
        if ! grep -q "^$var=" .env; then
            echo "⚠️  Missing variable in .env: $var"
        fi
    done
fi

echo "\n🎉 Facebook Marketing API MCP skill health check complete!"
echo "\n📋 Next steps:"
echo "   1. Add Facebook API credentials to .env"
echo "   2. Run 'bash install.sh' to install dependencies"
echo "   3. Start MCP server with 'npm start'"
echo "   4. Connect using any MCP client"
