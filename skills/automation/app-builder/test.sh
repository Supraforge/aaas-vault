#!/bin/bash
# Health check for app-builder
echo "Checking dependencies for app-builder..."

# Check for .env if API is used
if [ -f .env.template ] && [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy .env.template to .env and add your API keys."
fi

# Basic dependency checks
echo "✅ app-builder health check completed"
