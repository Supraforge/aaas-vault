#!/bin/bash
# Health check for microservices-patterns
echo "Testing microservices-patterns..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

# Check if scripts directory exists (if applicable)
if [ -d scripts ]; then
    echo "✅ scripts directory found"
fi

echo "✅ microservices-patterns structure looks good"
exit 0
