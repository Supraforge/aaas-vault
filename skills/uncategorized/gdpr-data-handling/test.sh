#!/bin/bash
# Health check for gdpr-data-handling
echo "Testing gdpr-data-handling..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ gdpr-data-handling structure looks good"
exit 0
