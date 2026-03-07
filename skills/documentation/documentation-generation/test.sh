#!/bin/bash
# Health check for documentation-generation
echo "Testing documentation-generation..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ documentation-generation structure looks good"
exit 0
