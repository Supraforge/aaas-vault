#!/bin/bash
# Health check for seo-analysis-monitoring
echo "Testing seo-analysis-monitoring..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ seo-analysis-monitoring structure looks good"
exit 0
