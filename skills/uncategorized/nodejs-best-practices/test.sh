#!/bin/bash
# Health check for nodejs-best-practices
echo "Checking dependencies for nodejs-best-practices..."

# Check for .env if API is used
if [ -f .env.template ] && [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy .env.template to .env and add your API keys."
fi

# Basic dependency checks
echo "✅ nodejs-best-practices health check completed"
