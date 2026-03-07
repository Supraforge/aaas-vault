#!/bin/bash
# Health check for adk-tool-scaffold
echo "Testing adk-tool-scaffold..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ adk-tool-scaffold structure looks good"
exit 0
