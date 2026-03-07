#!/bin/bash
# Autonomous Health Check for defining-brand-context
echo "🔍 Validating Brand Context Skill environment..."

# Check for python
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 is not installed. Scripted tone-checks will fail."
    exit 1
fi

# Check if templates directory exists
if [ -d "$(dirname "$0")/templates" ]; then
    echo "✅ Templates directory located."
else
    echo "❌ Error: Templates folder missing."
    exit 1
fi

echo "🚀 Skill is ready for autonomous use."
