#!/bin/bash
# Health check for using-git-worktrees skill

echo "🔍 Validating using-git-worktrees..."

# Check bash
bash_version=$(bash --version | head -1 | grep -oE '[0-9]+\\.[0-9]+\\.[0-9]+')
echo "✅ Bash version: $bash_version"

# Check git
git_version=$(git --version | grep -oE '[0-9]+\\.[0-9]+\\.[0-9]+')
echo "✅ Git version: $git_version"

echo "🚀 using-git-worktrees is ready."
exit 0
