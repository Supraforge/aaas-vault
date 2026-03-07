#!/bin/bash
# Installs necessary python libs for analytics-tracking
pip install requests beautifulsoup4

echo "✅ Analytics-tracking dependencies installed"
echo ""
echo "To set up environment variables:"
echo "cp .env.template .env"
echo "# Edit .env with your API keys"
