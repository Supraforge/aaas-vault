#!/bin/bash
# Install dependencies for this skill

# Python dependencies
if command -v python3 &> /dev/null; then
    echo "Installing Python dependencies..."
    pip install -r requirements.txt 2>/dev/null || echo "No requirements.txt found"
else
    echo "Python3 not found. Please install Python3."
fi

# System packages
if command -v apt-get &> /dev/null; then
    echo "Installing system packages: bash"
    apt-get update && apt-get install -y bash
else
    echo "apt-get not available. Please install packages manually."
fi
