#!/bin/bash
# Health check for code-documentation
echo "Testing code-documentation..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ code-documentation structure looks good"
exit 0
