#!/bin/bash
# Health check for postmortem-writing
echo "Testing postmortem-writing..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ postmortem-writing structure looks good"
exit 0
