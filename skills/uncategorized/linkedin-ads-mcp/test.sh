#!/bin/bash
# LinkedIn Ads MCP Skill - Health Check

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "🔍 Testing LinkedIn Ads MCP skill setup..."

# Check for required commands
for cmd in python3 node npm curl jq; do
    if ! command -v $cmd &> /dev/null; then
        echo "❌ Missing required command: $cmd"
        exit 1
    fi
echo "✅ $cmd found"
done

# Check Python version
python3 --version

# Check Node.js version
node --version

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy from .env.template"
    echo "   cp .env.template .env"
    echo "   Then add your LinkedIn Marketing API credentials"
else
    echo "✅ .env file found"
    # Check for required environment variables
    if grep -q "LINKEDIN_CLIENT_ID" .env && grep -q "LINKEDIN_CLIENT_SECRET" .env; then
        echo "✅ LinkedIn API credentials found in .env"
    else
        echo "⚠️  LinkedIn API credentials missing in .env"
    fi
fi

# Check script files exist
for script in scripts/linkedin_ads_manager.py scripts/linkedin_ads_api.js; do
    if [ -f "$script" ]; then
        echo "✅ $script found"
    else
        echo "❌ $script missing"
        exit 1
    fi
done

echo "\n✅ LinkedIn Ads MCP skill health check passed!"
echo "📋 Next steps:"
echo "1. Add LinkedIn Marketing API credentials to .env"
echo "2. Run ./install.sh to install dependencies"
echo "3. Test with: python3 scripts/linkedin_ads_manager.py --test"
