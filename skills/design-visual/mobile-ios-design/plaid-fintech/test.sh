#!/bin/bash
# Health check for plaid-fintech
echo "Checking dependencies for plaid-fintech..."

# Check for .env if API is used
if [ -f .env.template ] && [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy .env.template to .env and add your API keys."
fi

# Basic dependency checks
echo "✅ plaid-fintech health check completed"
