#!/bin/bash
# Health check for A/B Test Setup skill

echo "Checking dependencies for ab-test-setup..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install python3."
    exit 1
fi

# Check for required Python packages
REQUIRED_PACKAGES=("pandas" "numpy" "scipy" "matplotlib")
for package in "${REQUIRED_PACKAGES[@]}"; do
    if ! python3 -c "import $package" 2>/dev/null; then
        echo "⚠️  Package $package not installed. Run install.sh first."
    fi

done

echo "✅ All basic dependencies verified."
echo "
To install missing Python packages, run:"
echo "bash ~/.gemini/skills/ab-test-setup/install.sh"
