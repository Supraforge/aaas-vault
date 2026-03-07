#!/bin/bash
# Health check for distributed-debugging
echo "Testing distributed-debugging..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ distributed-debugging structure looks good"
exit 0
