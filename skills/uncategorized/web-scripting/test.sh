#!/bin/bash
# Health check for web-scripting skill

echo "🔍 Validating web-scripting skill..."

# Check 1: Ruby
if command -v ruby &> /dev/null; then
    echo "✅ Ruby is installed: $(ruby --version | head -1)"
else
    echo "❌ Ruby is not installed. Install with: apt-get install ruby"
    exit 1
fi

# Check 2: PHP
if command -v php &> /dev/null; then
    echo "✅ PHP is installed: $(php --version | head -1)"
else
    echo "❌ PHP is not installed. Install with: apt-get install php"
    exit 1
fi

# Check 3: Rails (optional but recommended)
if command -v rails &> /dev/null; then
    echo "✅ Rails is installed: $(rails --version 2>/dev/null || echo 'Rails found')"
else
    echo "⚠️  Rails is not installed. You can install it with: gem install rails"
fi

# Check 4: Composer
if command -v composer &> /dev/null; then
    echo "✅ Composer is installed: $(composer --version 2>/dev/null | head -1)"
else
    echo "⚠️  Composer is not installed. You can install it from: https://getcomposer.org/"
fi

echo "🚀 web-scripting skill is ready."
exit 0
