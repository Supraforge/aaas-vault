#!/bin/bash
# Health check for dependency-management
echo "Testing dependency-management..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ dependency-management structure looks good"
exit 0
