#!/bin/bash
# Checks if the skill has the necessary context files to run against

echo "🔍 Checking Hardest-Shift requirements..."

# Check if a spec or plan exists to analyze
if [ -f "docs/specs/SPEC.md" ] || [ -f "PLAN.md" ] || [ -f "README.md" ]; then
    echo "✅ Context files found. The Operator is ready."
    exit 0
else
    echo "⚠️  No context found (SPEC.md, PLAN.md, or README.md)."
    echo "   The Operator will likely need to ask clarifying questions first."
    exit 0 # Non-fatal, just a warning
fi
