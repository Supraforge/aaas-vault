#!/bin/bash
# Health check for cloud-infrastructure
echo "Testing cloud-infrastructure..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ cloud-infrastructure structure looks good"
exit 0
