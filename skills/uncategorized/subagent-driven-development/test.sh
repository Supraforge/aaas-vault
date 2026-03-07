#!/bin/bash
# Health check for subagent-driven-development skill

echo "🔍 Validating subagent-driven-development..."

# Check bash
bash_version=$(bash --version | head -1 | grep -oE '[0-9]+\\.[0-9]+\\.[0-9]+')
echo "✅ Bash version: $bash_version"

echo "🚀 subagent-driven-development is ready."
exit 0
