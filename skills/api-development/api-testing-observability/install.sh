#!/bin/bash
# Installation script for api-testing-observability skill

echo "🔧 Installing dependencies for api-testing-observability..."

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check for pip
if ! command -v pip3 &> /dev/null; then
    echo "⚠️  pip3 not found. Attempting to install pip..."
    if command -v apt-get &> /dev/null; then
        apt-get update && apt-get install -y python3-pip
    elif command -v yum &> /dev/null; then
        yum install -y python3-pip
    elif command -v brew &> /dev/null; then
        brew install python3
    else
        echo "❌ Cannot install pip3 automatically. Please install pip3 manually."
        exit 1
    fi
fi

# Upgrade pip to latest version
echo "📦 Upgrading pip..."
pip3 install --upgrade pip

# Install Python packages
echo "📦 Installing Python packages..."
pip3 install fastapi uvicorn pydantic requests httpx openapi-spec-validator

# Note: swagger-ui is typically served by FastAPI automatically, but we can also install it for standalone use
# If you want to install the swagger-ui package for offline use, uncomment the next line
# pip3 install swagger-ui-bundle

echo "✅ Dependencies installed successfully!"
echo "\n🚀 Skill 'api-testing-observability' is now ready for use."
echo "\n📋 Next steps:"
echo "1. Review the SKILL.md file for usage instructions"
echo "2. Run test.sh to verify the installation"
echo "3. Use the skill to create mock APIs or generate API documentation"
