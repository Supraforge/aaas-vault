#!/bin/bash
# Health check for code-review-ai
echo "Testing code-review-ai..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ code-review-ai structure looks good"
exit 0
