#!/bin/bash
# Health check for writing-skills skill

echo "🔍 Validating writing-skills..."

# Check bash
bash_version=$(bash --version | head -1 | grep -oE '[0-9]+\\.[0-9]+\\.[0-9]+')
echo "✅ Bash version: $bash_version"

echo "🚀 writing-skills is ready."
exit 0
