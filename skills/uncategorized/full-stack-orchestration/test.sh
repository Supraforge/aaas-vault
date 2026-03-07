#!/bin/bash
# Health check for full-stack-orchestration
echo "Testing full-stack-orchestration..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ full-stack-orchestration structure looks good"
exit 0
