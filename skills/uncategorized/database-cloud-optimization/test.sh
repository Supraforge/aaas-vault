#!/bin/bash
# Health check for database-cloud-optimization
echo "Testing database-cloud-optimization..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ database-cloud-optimization structure looks good"
exit 0
