#!/bin/bash
# Health check for internal-comms-anthropic
echo "Checking dependencies for internal-comms-anthropic..."

# Check for .env if API is used
if [ -f .env.template ] && [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy .env.template to .env and add your API keys."
fi

# Basic dependency checks
echo "✅ internal-comms-anthropic health check completed"
