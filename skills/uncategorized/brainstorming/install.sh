#!/bin/bash
# Installation script for brainstorming skill

echo "Installing dependencies for brainstorming skill..."

# Check if git is installed
if command -v git &> /dev/null; then
    echo "✅ Git is already installed."
else
    echo "❌ Git is not installed. Please install git using your package manager."
    echo "For Debian/Ubuntu: sudo apt-get install git"
    echo "For macOS: brew install git"
    echo "For other systems, visit: https://git-scm.com/downloads"
    exit 1
fi

echo "✅ Brainstorming skill dependencies are satisfied."
exit 0
