#!/bin/bash
# Sanity test for find-skills

echo "🔍 Testing find-skills locally..."
# Test for a known local skill
python3 skills/find-skills/scripts/discover.py "remotion" | grep -q "remotion-best-practices"

if [ $? -eq 0 ]; then
    echo "✅ Local discovery working."
else
    echo "❌ Local discovery failed."
    exit 1
fi

echo "🌐 Testing remote fallback (non-blocking)..."
# Just ensure it doesn't crash on a known miss
python3 skills/find-skills/scripts/discover.py "xyz-fake-remote-skill" > /dev/null

echo "✅ Sanity test complete."
exit 0
