#!/bin/bash
# Install dependencies for this skill

# System packages
if command -v apt-get &> /dev/null; then
    echo "Installing system packages: -r"
    apt-get update && apt-get install -y -r
else
    echo "apt-get not available. Please install packages manually."
fi
