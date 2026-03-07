#!/bin/bash
# Test script for api-fuzzing-bug-bounty
echo "Testing skill..."
if [ -f "SKILL.md" ]; then
    echo "✓ SKILL.md found"
else
    echo "✗ SKILL.md missing"
    exit 1
fi
echo "Test completed successfully"
