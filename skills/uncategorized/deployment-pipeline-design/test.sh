#!/bin/bash
# Health check for deployment-pipeline-design
echo "Testing deployment-pipeline-design..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ deployment-pipeline-design structure looks good"
exit 0
