#!/bin/bash
# Health check for employment-contract-templates
echo "Testing employment-contract-templates..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ employment-contract-templates structure looks good"
exit 0
