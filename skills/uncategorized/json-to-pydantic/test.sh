#!/bin/bash
# Health check for json-to-pydantic skill

echo "🔍 Validating json-to-pydantic skill..."

# Check 1: Python availability
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 is available."
    python_version=$(python3 --version)
    echo "   Version: $python_version"
else
    echo "❌ Python 3 is not installed or not in PATH."
    exit 1
fi

# Check 2: Pydantic installation
if python3 -c "import pydantic" 2>/dev/null; then
    echo "✅ Pydantic is installed."
    pydantic_version=$(python3 -c "import pydantic; print(pydantic.__version__)" 2>/dev/null || echo "unknown")
    echo "   Version: $pydantic_version"
else
    echo "⚠️  Pydantic is not installed. Run install.sh to install it."
    echo "   You can install with: pip install pydantic"
fi

# Check 3: Example files exist
if [ -f "examples/input_data.json" ] && [ -f "examples/output_model.py" ]; then
    echo "✅ Example files are present."
else
    echo "⚠️  Some example files are missing."
fi

echo "🚀 json-to-pydantic skill is ready."
exit 0
