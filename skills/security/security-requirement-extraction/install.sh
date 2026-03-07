#!/bin/bash
# Install script for security-requirement-extraction skill

echo "Installing dependencies for security-requirement-extraction..."

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is required but not installed. Installing..."
    apt-get update && apt-get install -y python3 python3-pip
fi

echo "✅ Dependencies installed."
echo "This skill provides templates and frameworks for extracting security requirements from threat models."
echo "No additional packages required beyond Python3."
