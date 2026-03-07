#!/bin/bash
# Health check for requesting-code-review skill

echo "🔍 Validating requesting-code-review..."

# Check bash
bash_version=$(bash --version | head -1 | grep -oE '[0-9]+\\.[0-9]+\\.[0-9]+')
echo "✅ Bash version: $bash_version"

echo "🚀 requesting-code-review is ready."
exit 0
