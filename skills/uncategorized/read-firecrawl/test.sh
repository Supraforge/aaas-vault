#!/bin/bash
# Simple health check for Firecrawl Skill
echo "Checking dependencies for reading-firecrawl..."

# 1. Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 could not be found."
    exit 1
fi

# 2. Check Requests
if python3 -c "import requests" &> /dev/null; then
    echo "✅ Python 'requests' library found."
else
    echo "❌ Python 'requests' library NOT found."
    exit 1
fi

# 3. Check .env Key
if grep -q "FIRECRAWL_API_KEY=" ../../.env; then
    echo "✅ FIRECRAWL_API_KEY placeholder found in .env."
else
    # It might be there but filled, or missing. This is a soft check.
    echo "⚠️  Ensure FIRECRAWL_API_KEY is set in your .env file."
fi

echo "✅ Firecrawl Skill is ready to rock."
