#!/bin/bash
# Simple health check for lead generation automation

echo "Checking dependencies for lead-generation-automation..."

# Check for python3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install python3."
    exit 1
fi

# Check for pip
if ! command -v pip &> /dev/null; then
    echo "❌ pip not found. Please install pip."
    exit 1
fi

# Check for .env if API keys are needed
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Create one from .env.template"
fi

# Check for required Python packages
REQUIRED_PACKAGES=("requests" "pandas" "beautifulsoup4" "selenium")
for package in "${REQUIRED_PACKAGES[@]}"; do
    if ! python3 -c "import $package" 2>/dev/null; then
        echo "⚠️  Python package $package not installed. Run install.sh"
    fi

done

echo "✅ Basic checks passed. Run 'python3 scripts/lead_generator.py --help' for usage."
