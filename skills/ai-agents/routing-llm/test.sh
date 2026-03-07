#!/bin/bash
# Test the router with different strategies

echo "Testing LLM Router..."

SPEED_MODEL=$(python3 skills/routing-llm/scripts/router.py --strategy speed)
echo "⚡ Speed Model:     $SPEED_MODEL"

REASONING_MODEL=$(python3 skills/routing-llm/scripts/router.py --strategy reasoning)
echo "🧠 Reasoning Model: $REASONING_MODEL"

if [[ -z "$SPEED_MODEL" ]] || [[ -z "$REASONING_MODEL" ]]; then
    echo "❌ Router returned empty model ID."
    exit 1
else
    echo "✅ Router operational."
fi
