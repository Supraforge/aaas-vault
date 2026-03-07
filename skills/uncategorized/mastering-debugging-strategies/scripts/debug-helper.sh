#!/bin/bash
# Debug Helper Script
# Collects common debugging info from the current environment.

echo "--- Environment Info ---"
echo "User: $(whoami)"
echo "PWD: $(pwd)"
echo "Shell: $SHELL"

echo ""
echo "--- Runtime Versions ---"
command -v python3 &> /dev/null && python3 --version
command -v node &> /dev/null && node --version
command -v go &> /dev/null && go version

echo ""
echo "--- Git Status ---"
git status --short 2>/dev/null || echo "Not a git repository."

echo ""
echo "--- Recent Commits ---"
git log --oneline -5 2>/dev/null || echo "No git history."
