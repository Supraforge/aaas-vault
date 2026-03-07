#!/bin/bash
# Health check for Microsoft Ads MCP skill

echo "🔍 Testing Microsoft Ads MCP skill..."

# Check Python availability
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+"
    exit 1
fi

echo "✅ Python3: $(python3 --version)"

# Check Node.js availability
if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js not found (optional for JavaScript API)"
else
    echo "✅ Node.js: $(node --version)"
fi

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  .env file missing. Copy .env.template to .env and add credentials"
    echo "   cp .env.template .env"
    echo "   # Edit .env with your Microsoft Advertising API credentials"
else
    echo "✅ .env file found"
    # Check for required variables
    if grep -q "MICROSOFT_ADS_CLIENT_ID" .env && grep -q "MICROSOFT_ADS_CLIENT_SECRET" .env; then
        echo "✅ Required environment variables found"
    else
        echo "⚠️  Some required environment variables may be missing"
    fi
fi

# Check Python dependencies
if [ -f requirements.txt ]; then
    echo "📦 Checking Python dependencies..."
    python3 -c "
import pkg_resources
required = [line.strip() for line in open('requirements.txt') if line.strip() and not line.startswith('#')]
for package in required:
    try:
        dist = pkg_resources.get_distribution(package.split('==')[0].split('>=')[0])
        print(f'✅ {package}: {dist.version}')
    except:
        print(f'❌ {package}: Not installed')
"
fi

# Check Node.js dependencies
if [ -f scripts/package.json ]; then
    echo "📦 Checking Node.js dependencies..."
    if command -v npm &> /dev/null; then
        cd scripts && npm list --depth=0 2>/dev/null | head -20
        cd ..
    fi
fi

echo "\n✅ Microsoft Ads MCP skill health check completed"
echo "\n📋 Next steps:"
echo "1. Add your Microsoft Advertising API credentials to .env"
echo "2. Run ./install.sh to install dependencies"
echo "3. Test with: python scripts/microsoft_ads_manager.py --help"
