#!/bin/bash
# Health check for c4-architecture
echo "Testing c4-architecture..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ c4-architecture structure looks good"
exit 0
