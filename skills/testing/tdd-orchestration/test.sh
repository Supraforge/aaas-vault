#!/bin/bash
# TDD orchestration skill health check

echo "🔍 Validating tdd-orchestration skill..."

# List of dependencies to check
dependencies=("python3" "git" "pytest" "jest" "mocha" "docker" "nodejs" "jq" "yq" "curl" "make" "npm" "pip")

all_ok=true
for cmd in "${dependencies[@]}"; do
    if command -v $cmd >/dev/null 2>&1; then
        echo "✅ $cmd installed"
    else
        echo "❌ $cmd not found"
        all_ok=false
    fi
done

# Check for specific tools
if [ -f /usr/bin/docker ] || command -v docker >/dev/null 2>&1; then
    echo "✅ Docker available"
else
    echo "❌ Docker not found"
    all_ok=false
fi

# Check Node.js version
if command -v node >/dev/null 2>&1; then
    node_version=$(node --version)
    echo "✅ Node.js $node_version"
else
    echo "❌ Node.js not found"
    all_ok=false
fi

# Check Python version
if command -v python3 >/dev/null 2>&1; then
    python_version=$(python3 --version)
    echo "✅ $python_version"
else
    echo "❌ Python3 not found"
    all_ok=false
fi

if [ "$all_ok" = true ]; then
    echo "🚀 tdd-orchestration skill is ready."
    exit 0
else
    echo "⚠️  Some dependencies are missing. Run install.sh to install them."
    exit 1
fi
