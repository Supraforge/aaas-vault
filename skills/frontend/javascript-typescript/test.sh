#!/bin/bash
# Health check for javascript-typescript
echo "Testing javascript-typescript..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ javascript-typescript structure looks good"
exit 0
