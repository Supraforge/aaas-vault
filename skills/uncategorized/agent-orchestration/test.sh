#!/bin/bash
# Health check for agent-orchestration
echo "Testing agent-orchestration..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ agent-orchestration structure looks good"
exit 0
