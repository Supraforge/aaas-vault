#!/bin/bash
# Simple health check for analytics-tracking skill
echo "Checking dependencies for analytics-tracking..."

# Check for python3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install python3."
    exit 1
fi

# Check for curl
if ! command -v curl &> /dev/null; then
    echo "⚠️  curl not found. Some verification features may not work."
fi

# Check for jq
if ! command -v jq &> /dev/null; then
    echo "⚠️  jq not found. JSON parsing features may be limited."
fi

# Check for .env if API is used
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Create from .env.template if needed."
fi

echo "✅ All basic dependencies verified"
echo ""
echo "To test analytics setup generation:"
echo "python3 scripts/analytics_setup.py --provider google-analytics --url https://example.com"
