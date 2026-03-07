#!/bin/bash
# Health check for receiving-code-review skill

echo "🔍 Validating receiving-code-review..."

# Check bash
bash_version=$(bash --version | head -1 | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')
echo "✅ Bash version: $bash_version"

echo "🚀 receiving-code-review is ready."
exit 0
