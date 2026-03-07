#!/bin/bash
# Health check for nx-workspace-patterns skill

set -e

echo "🔍 Validating nx-workspace-patterns..."

# Check Node.js
if command -v node >/dev/null 2>&1; then
    echo "✅ Node.js installed: $(node --version)"
else
    echo "❌ Node.js not found"
    exit 1
fi

# Check Nx CLI
if command -v nx >/dev/null 2>&1; then
    echo "✅ Nx CLI installed: $(nx --version 2>/dev/null || echo 'version unknown')"
else
    echo "⚠️  Nx CLI not found globally. You may need to install it with 'npm install -g nx'"
    echo "   or use npx nx for commands."
fi

# Check for templates directory
if [ -d "${SKILL_DIR:-.}/templates" ]; then
    echo "✅ Templates directory found"
else
    echo "ℹ️  No templates directory found (optional)"
fi

echo "🚀 nx-workspace-patterns is ready."
exit 0
