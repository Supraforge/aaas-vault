#!/bin/bash
# Simple health check for content-strategy-automation

echo "Checking dependencies for content-strategy-automation..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+"
    exit 1
fi

# Check for .env if APIs are used
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Create from .env.template"
    echo "Required API keys: OPENAI_API_KEY, GOOGLE_ANALYTICS_KEY"
fi

# Check Python dependencies
echo "Checking Python packages..."
python3 -c "import openai, requests, pandas, schedule" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Some Python packages missing. Run install.sh"
fi

echo "✅ Basic checks passed. Run scripts/content_strategy.py to start."
