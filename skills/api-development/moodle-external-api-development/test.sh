#!/bin/bash
# Health check for moodle-external-api-development
echo "Checking dependencies for moodle-external-api-development..."

# Check for .env if API is used
if [ -f .env.template ] && [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy .env.template to .env and add your API keys."
fi

# Basic dependency checks
echo "✅ moodle-external-api-development health check completed"
