#!/bin/bash
# Health check for codebase-cleanup
echo "Testing codebase-cleanup..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ codebase-cleanup structure looks good"
exit 0
