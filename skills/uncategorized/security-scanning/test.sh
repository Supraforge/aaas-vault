#!/bin/bash
# Health check for security-scanning
echo "Testing security-scanning..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ security-scanning structure looks good"
exit 0
