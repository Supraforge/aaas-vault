#!/bin/bash
# Health check for blockchain-web3
echo "Testing blockchain-web3..."

# Check if SKILL.md exists
if [ ! -f SKILL.md ]; then
    echo "❌ SKILL.md missing"
    exit 1
fi

echo "✅ blockchain-web3 structure looks good"
exit 0
