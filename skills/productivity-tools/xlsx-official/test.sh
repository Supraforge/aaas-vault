#!/bin/bash
# Test script for xlsx-official
echo "Testing skill..."
if [ -f "SKILL.md" ]; then
    echo "✓ SKILL.md found"
else
    echo "✗ SKILL.md missing"
    exit 1
fi
echo "Test completed successfully"
