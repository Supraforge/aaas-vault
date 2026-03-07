#!/bin/bash
# Installation script for json-to-pydantic skill

echo "Installing dependencies for json-to-pydantic skill..."

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.7+ first."
    exit 1
fi

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is not installed. Please install pip3 first."
    exit 1
fi

# Install pydantic
echo "Installing pydantic..."
pip3 install pydantic

if [ $? -eq 0 ]; then
    echo "✅ pydantic installed successfully."
    echo "Run 'bash test.sh' to verify the installation."
else
    echo "❌ Failed to install pydantic. Please check your pip installation."
    exit 1
fi
