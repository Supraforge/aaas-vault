#!/bin/bash
# Install dependencies for python-packaging skill

echo "📦 Installing Python packaging tools..."

# Determine pip command
if command -v pip &> /dev/null; then
    PIP_CMD="pip"
elif command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
else
    echo "❌ pip not found. Installing pip..."
    apt-get update && apt-get install -y python3-pip
    PIP_CMD="pip3"
fi

# Install/upgrade core packaging tools
$PIP_CMD install --upgrade pip setuptools wheel

# Install build tool
if ! python3 -c "import build" 2>/dev/null; then
    echo "Installing build..."
    $PIP_CMD install build
else
    echo "✅ build already installed"
fi

# Install twine
if ! command -v twine &> /dev/null && ! python3 -c "import twine" 2>/dev/null; then
    echo "Installing twine..."
    $PIP_CMD install twine
else
    echo "✅ twine already available"
fi

# Install additional useful tools
$PIP_CMD install --upgrade check-manifest readme-renderer

echo "✅ Python packaging tools installed successfully"
echo "Run 'bash test.sh' to verify installation"
