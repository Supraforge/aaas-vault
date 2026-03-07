#!/bin/bash
# Health check for incident-runbook-templates
echo "Testing incident-runbook-templates..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ incident-runbook-templates structure looks good"
exit 0
