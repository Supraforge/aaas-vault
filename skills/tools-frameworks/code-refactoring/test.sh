#!/bin/bash
# Health check for code-refactoring
echo "Testing code-refactoring..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ code-refactoring structure looks good"
exit 0
