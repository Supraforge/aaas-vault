#!/bin/bash
# Health check for scaffolding-adk-tools skill

set -e

echo "🔍 Validating scaffolding-adk-tools..."

# Check 1: Python availability
if command -v python3 &> /dev/null; then
    echo "✅ Python3 is available"
else
    echo "❌ Python3 not found. Please install python3."
    exit 1
fi

# Check 2: Script directory integrity
if [ -f "scripts/scaffold_tool.py" ]; then
    echo "✅ Scaffold script found"
else
    echo "❌ Scaffold script missing"
    exit 1
fi

# Check 3: Template file
if [ -f "templates/ToolTemplate.py.hbs" ]; then
    echo "✅ Template file found"
else
    echo "❌ Template file missing"
    exit 1
fi

# Check 4: Example file
if [ -f "examples/WeatherTool.py" ]; then
    echo "✅ Example file found"
else
    echo "❌ Example file missing"
    exit 1
fi

# Test 5: Dry run of scaffold script
cd /tmp
TEST_TOOL_NAME="TestTool$(date +%s)"
echo "Testing scaffold script with tool name: $TEST_TOOL_NAME"

if python3 "$OLDPWD/scripts/scaffold_tool.py" "$TEST_TOOL_NAME" 2>/dev/null; then
    echo "✅ Scaffold script executed successfully"
    if [ -f "${TEST_TOOL_NAME}Tool.py" ]; then
        echo "✅ Tool file generated"
        rm -f "${TEST_TOOL_NAME}Tool.py"
    else
        echo "❌ Tool file not generated"
        exit 1
    fi
else
    echo "❌ Scaffold script failed"
    exit 1
fi

cd "$OLDPWD"

echo "🚀 scaffolding-adk-tools is ready."
exit 0
