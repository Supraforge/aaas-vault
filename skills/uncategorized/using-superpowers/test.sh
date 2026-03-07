#!/bin/bash
# Health check for using-superpowers skill

echo "🔍 Validating using-superpowers..."

# Check bash
bash_version=$(bash --version | head -1 | grep -oE '[0-9]+\\.[0-9]+\\.[0-9]+')
echo "✅ Bash version: $bash_version"

echo "🚀 using-superpowers is ready."
exit 0
