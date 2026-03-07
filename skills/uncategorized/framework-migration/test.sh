#!/bin/bash
# Health check for framework-migration
echo "Testing framework-migration..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ framework-migration structure looks good"
exit 0
