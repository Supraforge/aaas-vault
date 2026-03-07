#!/bin/bash
# Health check for terraform-module-library
echo "Testing terraform-module-library..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ terraform-module-library structure looks good"
exit 0
