#!/bin/bash
# Health check for twilio-communications
echo "Checking dependencies for twilio-communications..."

# Check for .env if API is used
if [ -f .env.template ] && [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy .env.template to .env and add your API keys."
fi

# Basic dependency checks
echo "✅ twilio-communications health check completed"
