#!/bin/bash
# Health check for julia-development
echo "Testing julia-development..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ julia-development structure looks good"
exit 0
