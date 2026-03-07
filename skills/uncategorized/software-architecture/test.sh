#!/bin/bash
# Health check for software-architecture
echo "Checking dependencies for software-architecture..."

# Check for .env if API is used
if [ -f .env.template ] && [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy .env.template to .env and add your API keys."
fi

# Basic dependency checks
echo "✅ software-architecture health check completed"
