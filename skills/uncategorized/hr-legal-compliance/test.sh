#!/bin/bash
# Health check for hr-legal-compliance
echo "Testing hr-legal-compliance..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ hr-legal-compliance structure looks good"
exit 0
