#!/bin/bash
# Health check for context-management
echo "Testing context-management..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ context-management structure looks good"
exit 0
