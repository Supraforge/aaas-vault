#!/bin/bash
# Health check for license-header-adder skill

echo "🔍 Validating license-header-adder..."

# Check 1: Template file exists
if [ -f "templates/HEADER_TEMPLATE.txt" ]; then
    echo "✅ Template file found."
else
    echo "❌ ERROR: Template file not found at templates/HEADER_TEMPLATE.txt"
    exit 1
fi

# Check 2: Template is readable
if [ -r "templates/HEADER_TEMPLATE.txt" ]; then
    echo "✅ Template file is readable."
else
    echo "❌ ERROR: Template file is not readable"
    exit 1
fi

# Check 3: Template has content
if [ -s "templates/HEADER_TEMPLATE.txt" ]; then
    echo "✅ Template file has content."
else
    echo "❌ ERROR: Template file is empty"
    exit 1
fi

echo "🚀 license-header-adder is ready."
exit 0
