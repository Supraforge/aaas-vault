#!/bin/bash
# Health check for machine-learning-ops
echo "Testing machine-learning-ops..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ machine-learning-ops structure looks good"
exit 0
