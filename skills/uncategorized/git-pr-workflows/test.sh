#!/bin/bash
# Health check for git-pr-workflows
echo "Testing git-pr-workflows..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ git-pr-workflows structure looks good"
exit 0
