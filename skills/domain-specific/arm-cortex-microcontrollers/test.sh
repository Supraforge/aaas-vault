#!/bin/bash
# Health check for arm-cortex-microcontrollers
echo "Testing arm-cortex-microcontrollers..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ arm-cortex-microcontrollers structure looks good"
exit 0
