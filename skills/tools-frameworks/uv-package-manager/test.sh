#!/bin/bash
# Health check for uv-package-manager skill

echo "🔍 Validating uv-package-manager..."

# Check for uv
if command -v uv &> /dev/null; then
    echo "✅ uv found: $(uv --version)"
else
    echo "❌ uv not found. Install via: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Check for python3
if command -v python3 &> /dev/null; then
    echo "✅ Python3 found: $(python3 --version)"
else
    echo "❌ python3 not found. Install python3 via your package manager."
    exit 1
fi

echo "🚀 uv-package-manager skill validation complete."
exit 0
