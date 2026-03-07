#!/bin/bash
# Health check for database-migrations
echo "Testing database-migrations..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ database-migrations structure looks good"
exit 0
