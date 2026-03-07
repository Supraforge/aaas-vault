#!/bin/bash
# Health check for k8s-security-policies
echo "Testing k8s-security-policies..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ k8s-security-policies structure looks good"
exit 0
