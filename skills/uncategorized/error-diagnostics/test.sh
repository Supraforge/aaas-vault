#!/bin/bash
# Health check for error-diagnostics
echo "Testing error-diagnostics..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ error-diagnostics structure looks good"
exit 0
