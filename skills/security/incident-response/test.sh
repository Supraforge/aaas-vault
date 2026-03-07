#!/bin/bash
# Health check for incident-response
echo "Testing incident-response..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ incident-response structure looks good"
exit 0
