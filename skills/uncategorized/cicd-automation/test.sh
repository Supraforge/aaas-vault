#!/bin/bash
# Health check for cicd-automation
echo "Testing cicd-automation..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ cicd-automation structure looks good"
exit 0
