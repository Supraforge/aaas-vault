#!/bin/bash
# Health check for turborepo-caching skill

echo "🔍 Validating turborepo-caching..."

# Check 1: Node.js
if command -v node &> /dev/null; then
    echo "✅ Node.js is installed: $(node --version)"
else
    echo "⚠️  Node.js is not installed. Install with: apt-get install nodejs"
fi

# Check 2: npm
if command -v npm &> /dev/null; then
    echo "✅ npm is installed: $(npm --version)"
else
    echo "⚠️  npm is not installed. Install with: apt-get install npm"
fi

# Check 3: Git
if command -v git &> /dev/null; then
    echo "✅ Git is installed: $(git --version | cut -d' ' -f3)"
else
    echo "⚠️  Git is not installed. Install with: apt-get install git"
fi

# Check 4: Skill file
if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found."
else
    echo "❌ SKILL.md missing!"
    exit 1
fi

echo "🚀 turborepo-caching is ready."
exit 0
