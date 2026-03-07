#!/bin/bash
echo "🔍 Checking SDD Environment..."

# Ensure docs directory exists
if [ ! -d "./docs/specs" ]; then
    echo "📂 Creating missing directory: docs/specs"
    mkdir -p ./docs/specs
fi

# Check for Constitution
if [ ! -f "./constitution.md" ]; then
    echo "⚠️  WARNING: No constitution.md found in root. The /plan command will be limited."
else
    echo "✅ constitution.md detected."
fi

echo "🚀 Spec-Driven Architect is ready."
