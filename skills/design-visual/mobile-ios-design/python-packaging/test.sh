#!/bin/bash
# Health check for python-packaging skill

echo "🔍 Validating python-packaging dependencies..."

# Check Python
if command -v python3 &> /dev/null; then
    echo "✅ Python3 is installed"
else
    echo "❌ Python3 is not installed"
    exit 1
fi

# Check pip
if command -v pip &> /dev/null || command -v pip3 &> /dev/null; then
    echo "✅ pip is installed"
else
    echo "❌ pip is not installed"
    exit 1
fi

# Check build tool
if python3 -c "import build" 2>/dev/null; then
    echo "✅ build module is available"
else
    echo "⚠️  build module not installed (run install.sh)"
fi

# Check twine
if command -v twine &> /dev/null || python3 -c "import twine" 2>/dev/null; then
    echo "✅ twine is available"
else
    echo "⚠️  twine not installed (run install.sh)"
fi

# Check setuptools
if python3 -c "import setuptools" 2>/dev/null; then
    echo "✅ setuptools is available"
else
    echo "⚠️  setuptools not installed (run install.sh)"
fi

# Check wheel
if python3 -c "import wheel" 2>/dev/null; then
    echo "✅ wheel is available"
else
    echo "⚠️  wheel not installed (run install.sh)"
fi

echo "🚀 python-packaging skill is ready for use."
exit 0
