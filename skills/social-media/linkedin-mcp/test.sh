#!/bin/bash
# LinkedIn MCP Health Check
set -e

echo "🔍 LinkedIn MCP Health Check"
echo "=========================="

# Check dependencies
echo "\n1. Checking dependencies..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found"
    exit 1
else
    echo "✅ Python3: $(python3 --version)"
fi

if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found"
    exit 1
else
    echo "✅ Node.js: $(node --version)"
fi

if ! command -v npm &> /dev/null; then
    echo "❌ npm not found"
    exit 1
else
    echo "✅ npm: $(npm --version)"
fi

if ! command -v jq &> /dev/null; then
    echo "⚠️  jq not found (optional but recommended)"
else
    echo "✅ jq: $(jq --version)"
fi

# Check for .env file
echo "\n2. Checking environment configuration..."
if [ ! -f .env ]; then
    echo "⚠️  .env file missing. Creating template..."
    if [ -f .env.template ]; then
        cp .env.template .env
        echo "✅ Created .env from template"
        echo "   Please edit .env with your LinkedIn API credentials"
    else
        echo "❌ .env.template not found"
        exit 1
    fi
else
    echo "✅ .env file exists"
    
    # Check for required variables
    required_vars=("LINKEDIN_CLIENT_ID" "LINKEDIN_CLIENT_SECRET" "LINKEDIN_ACCESS_TOKEN")
    missing_vars=()
    
    for var in "${required_vars[@]}"; do
        if ! grep -q "^${var}=" .env; then
            missing_vars+=("$var")
        fi
    done
    
    if [ ${#missing_vars[@]} -eq 0 ]; then
        echo "✅ All required LinkedIn variables found"
    else
        echo "⚠️  Missing variables: ${missing_vars[*]}"
        echo "   Please add them to .env"
    fi
fi

# Check Python dependencies
echo "\n3. Checking Python dependencies..."
python3 -c "
try:
    import requests
    print('✅ requests: ' + requests.__version__)
except ImportError:
    print('❌ requests not installed')
    
try:
    import pandas
    print('✅ pandas: ' + pandas.__version__)
except ImportError:
    print('⚠️  pandas not installed (optional)')
    
try:
    from linkedin_api import Linkedin
    print('✅ linkedin-api: Installed')
except ImportError:
    print('⚠️  linkedin-api not installed (run install.sh)')
"

# Check Node.js dependencies
echo "\n4. Checking Node.js dependencies..."
if [ -f package.json ]; then
    echo "✅ package.json exists"
    if [ -d node_modules ]; then
        echo "✅ node_modules directory exists"
    else
        echo "⚠️  node_modules not found (run 'npm install')"
    fi
else
    echo "⚠️  package.json not found"
fi

echo "\n✅ LinkedIn MCP health check completed!"
echo "\n📋 Next steps:"
echo "1. Edit .env with your LinkedIn API credentials"
echo "2. Run 'bash install.sh' to install dependencies"
echo "3. Test with: python3 scripts/linkedin_api.py --test"
