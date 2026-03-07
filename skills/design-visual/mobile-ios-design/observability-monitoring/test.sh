#!/bin/bash
# Health check for observability-monitoring
echo "Testing observability-monitoring..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ observability-monitoring structure looks good"
exit 0
