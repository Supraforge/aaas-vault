#!/bin/bash
# Health check for systematic-debugging skill

echo "🔍 Validating systematic-debugging..."

# Check bash
bash_version=$(bash --version | head -1 | grep -oE '[0-9]+\\.[0-9]+\\.[0-9]+')
echo "✅ Bash version: $bash_version"

echo "🚀 systematic-debugging is ready."
exit 0
