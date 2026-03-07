#!/bin/bash
# Installation script for uv-package-manager skill

echo "Installing uv-package-manager skill..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "uv not found. Installing uv..."
    # Install uv using the official installer
    curl -LsSf https://astral.sh/uv/install.sh | sh
    echo "Please restart your shell or run 'source ~/.bashrc' to update PATH"
else
    echo "✅ uv is already installed: $(uv --version)"
fi

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "python3 not found. Please install python3 via your package manager."
    echo "For Debian/Ubuntu: sudo apt-get install python3"
    echo "For macOS: brew install python"
    exit 1
else
    echo "✅ Python3 is already installed: $(python3 --version)"
fi

echo "\n📚 Skill installation complete. Run 'bash test.sh' to verify."
