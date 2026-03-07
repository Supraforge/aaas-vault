#!/bin/bash
# Health check for k8s-manifest-generator
echo "Testing k8s-manifest-generator..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ k8s-manifest-generator structure looks good"
exit 0
