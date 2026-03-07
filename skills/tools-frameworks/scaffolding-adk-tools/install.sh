#!/bin/bash
# Installation script for scaffolding-adk-tools skill

set -e

echo "Installing scaffolding-adk-tools..."

# Check for python3
if ! command -v python3 &> /dev/null; then
    echo "Python3 is required but not found. Please install python3 first."
    exit 1
fi

# Check if pip is available
if command -v pip3 &> /dev/null; then
    echo "pip3 is available"
else
    echo "Note: pip3 not found. Some dependencies may need manual installation."
fi

echo "✅ scaffolding-adk-tools installation complete."
echo "Run 'bash test.sh' to verify the skill."
