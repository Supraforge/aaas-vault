#!/bin/bash
# Health check for dotnet-contribution
echo "Testing dotnet-contribution..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ dotnet-contribution structure looks good"
exit 0
