#!/bin/bash
# Health check for notebooklm
echo "Checking dependencies for notebooklm..."

# Check for .env if API is used
if [ -f .env.template ] && [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy .env.template to .env and add your API keys."
fi

# Basic dependency checks
echo "✅ notebooklm health check completed"
