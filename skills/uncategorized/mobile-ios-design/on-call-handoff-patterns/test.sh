#!/bin/bash
# Health check for on-call-handoff-patterns
echo "Testing on-call-handoff-patterns..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ on-call-handoff-patterns structure looks good"
exit 0
