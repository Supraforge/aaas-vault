#!/bin/bash
# Instagram Ads MCP Skill - Health Check

echo "🔍 Testing Instagram Ads MCP Skill Setup..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+"
    exit 1
else
    echo "✅ Python3: $(python3 --version)"
fi

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js not found (optional for some features)"
else
    echo "✅ Node.js: $(node --version)"
fi

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  .env file not found. Creating from template..."
    if [ -f .env.template ]; then
        cp .env.template .env
        echo "📋 Created .env from template. Please add your Facebook/Instagram API credentials."
    else
        echo "❌ .env.template not found"
    fi
else
    echo "✅ .env file exists"
    
    # Check for required variables
    required_vars=("FACEBOOK_ACCESS_TOKEN" "FACEBOOK_AD_ACCOUNT_ID" "INSTAGRAM_BUSINESS_ACCOUNT_ID")
    missing_vars=()
    
    for var in "${required_vars[@]}"; do
        if ! grep -q "$var" .env; then
            missing_vars+=("$var")
        fi
    done
    
    if [ ${#missing_vars[@]} -eq 0 ]; then
        echo "✅ Required environment variables found"
    else
        echo "⚠️  Missing required environment variables in .env"
        echo "   Missing: ${missing_vars[*]}"
    fi
fi

# Check Python dependencies
echo "\n📦 Checking Python packages..."
python3 -c "
import sys
import pkg_resources

required = {
    'facebook-business': '16.0+',
    'pandas': '1.3+',
    'python-dotenv': '0.19+',
    'requests': '2.25+'
}

missing = []
outdated = []

for package, min_version in required.items():
    try:
        dist = pkg_resources.get_distribution(package)
        installed_version = pkg_resources.parse_version(dist.version)
        min_ver = pkg_resources.parse_version(min_version)
        
        if installed_version < min_ver:
            outdated.append(f'{package} (installed: {dist.version}, required: {min_version})')
        else:
            print(f'✅ {package}: {dist.version}')
    except pkg_resources.DistributionNotFound:
        missing.append(package)

if missing:
    print(f'\n❌ Missing packages: {missing}')
    print('Run: pip install ' + ' '.join(missing))
if outdated:
    print(f'\n⚠️  Outdated packages: {outdated}')
    print('Run: pip install --upgrade ' + ' '.join([o.split()[0] for o in outdated]))
if not missing and not outdated:
    print('\n✅ All Python dependencies satisfied')
"

# Check Node.js dependencies
if command -v npm &> /dev/null && [ -f "scripts/package.json" ]; then
    echo "\n📦 Checking Node.js packages..."
    cd scripts
    npm list --depth=0 2>/dev/null | grep -E "^(├──|└──)" || echo "No Node.js dependencies installed"
    cd ..
fi

echo "\n🎯 Instagram Ads MCP Skill is ready!"
echo "Next steps:"
echo "1. Add your Facebook/Instagram API credentials to .env"
echo "2. Run ./install.sh to install dependencies"
echo "3. Test with: python3 scripts/instagram_ads_manager.py --help"
