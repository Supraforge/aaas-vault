#!/bin/bash
# Health check for data-validation-suite
echo "Testing data-validation-suite..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ data-validation-suite structure looks good"
exit 0
