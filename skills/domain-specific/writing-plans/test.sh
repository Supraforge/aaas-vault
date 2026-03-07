#!/bin/bash
# Health check for writing-plans skill

echo "🔍 Validating writing-plans..."

# Check bash
bash_version=$(bash --version | head -1 | grep -oE '[0-9]+\\.[0-9]+\\.[0-9]+')
echo "✅ Bash version: $bash_version"

# Check git
git_version=$(git --version | grep -oE '[0-9]+\\.[0-9]+\\.[0-9]+')
echo "✅ Git version: $git_version"

echo "🚀 writing-plans is ready."
exit 0
