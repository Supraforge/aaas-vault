#!/bin/bash
# Health check for notebooklm-intelligence v2.5.0

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" \u0026\u0026 pwd)"
SKILL_PATH="${SCRIPT_DIR}/SKILL.md"
BASE_NOTEBOOK_PATH="/Users/user/.gemini/skills/notebooklm"

echo "🔍 Checking notebooklm-intelligence v2.5.0..."

# 1. Check Version
if grep -q "version: 2.5.0" "$SKILL_PATH"; then
    echo "✅ Version 2.5.0 detected."
else
    echo "❌ Version mismatch or not found."
    exit 1
fi

# 2. Check Dependencies
if [ -d "$BASE_NOTEBOOK_PATH" ]; then
    echo "✅ Base notebooklm skill found."
else
    echo "❌ Dependency missing: base notebooklm skill not found at $BASE_NOTEBOOK_PATH"
    exit 1
fi

# 3. Check Script Existence
if [ -f "${SCRIPT_DIR}/scripts/retrieval_agent.py" ]; then
    echo "✅ Retrieval agent script found."
else
    echo "❌ Retrieval agent script missing."
    exit 1
fi

echo "🚀 Skill is healthy (Structural Verification)."
exit 0
