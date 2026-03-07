#!/bin/bash
# Health check for security-compliance
echo "Testing security-compliance..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ security-compliance structure looks good"
exit 0
