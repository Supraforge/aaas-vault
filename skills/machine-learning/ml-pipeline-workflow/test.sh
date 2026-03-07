#!/bin/bash
# Health check for ml-pipeline-workflow
echo "Testing ml-pipeline-workflow..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ ml-pipeline-workflow structure looks good"
exit 0
