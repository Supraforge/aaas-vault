#!/bin/bash
# Health check for backend-scaffolding skill

echo "🔍 Validating backend-scaffolding skill..."

# Check 1: Core dependencies
echo "\n📦 Checking core dependencies:"

# Python 3.8+
if command -v python3 &> /dev/null; then
    python_version=$(python3 --version 2>&1 | awk '{print $2}')
    echo "✅ Python $python_version installed"
else
    echo "❌ Python3 not found"
    exit 1
fi

# UV package manager
if command -v uv &> /dev/null; then
    uv_version=$(uv --version 2>&1 | head -1)
    echo "✅ $uv_version installed"
else
    echo "⚠️  UV not found (recommended for Python package management)"
fi

# Git
if command -v git &> /dev/null; then
    git_version=$(git --version 2>&1)
    echo "✅ $git_version installed"
else
    echo "❌ Git not found"
    exit 1
fi

# Docker
if command -v docker &> /dev/null; then
    docker_version=$(docker --version 2>&1)
    echo "✅ $docker_version installed"
else
    echo "⚠️  Docker not found (required for containerized deployments)"
fi

# Docker Compose
if command -v docker-compose &> /dev/null; then
    docker_compose_version=$(docker-compose --version 2>&1)
    echo "✅ $docker_compose_version installed"
else
    echo "⚠️  Docker Compose not found (required for multi-container setups)"
fi

# Check 2: Skill directory structure
echo "\n📁 Checking skill structure:"
if [ -f "SKILL.md" ]; then
    echo "✅ SKILL.md found"
    
    # Check YAML frontmatter
    if head -10 SKILL.md | grep -q "^---"; then
        echo "✅ YAML frontmatter present"
    else
        echo "⚠️  YAML frontmatter missing or malformed"
    fi
else
    echo "❌ SKILL.md not found"
    exit 1
fi

if [ -f "test.sh" ]; then
    echo "✅ test.sh found (this file)"
fi

if [ -f "install.sh" ]; then
    echo "✅ install.sh found"
fi

# Check 3: Template directories (optional)
echo "\n🎨 Checking template directories (optional):"
if [ -d "templates" ]; then
    echo "✅ templates/ directory found"
    template_count=$(find templates -type f -name "*.py" -o -name "*.md" -o -name "*.yaml" -o -name "*.yml" -o -name "*.sh" 2>/dev/null | wc -l)
    echo "   Found $template_count template files"
else
    echo "ℹ️  templates/ directory not found (can be created later)"
fi

if [ -d "scripts" ]; then
    echo "✅ scripts/ directory found"
    script_count=$(find scripts -type f -name "*.sh" -o -name "*.py" 2>/dev/null | wc -l)
    echo "   Found $script_count script files"
else
    echo "ℹ️  scripts/ directory not found (can be created later)"
fi

echo "\n🚀 Backend-scaffolding skill is ready for use!"
echo "\n📋 Next steps:"
echo "1. Review SKILL.md for framework options"
echo "2. Run install.sh to install any missing dependencies"
echo "3. Use the skill to scaffold your backend project"

exit 0
