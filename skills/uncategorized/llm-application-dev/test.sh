#!/bin/bash
# Health check for llm-application-dev
echo "Testing llm-application-dev..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ llm-application-dev structure looks good"
exit 0
