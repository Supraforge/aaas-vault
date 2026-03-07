#!/bin/bash
# Health check for code-review-checklist
echo "Checking dependencies for code-review-checklist..."

# Check for .env if API is used
if [ -f .env.template ] && [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy .env.template to .env and add your API keys."
fi

# Basic dependency checks
echo "✅ code-review-checklist health check completed"
