#!/bin/bash
# Install script for bats-testing-patterns skill

echo "Installing dependencies for bats-testing-patterns..."

# Note: bats-core is not available in Kali repos by default
# Users may need to install from source or use alternative methods
echo "⚠️  bats-core is not available in standard Kali repositories."
echo "To install bats-core, use one of these methods:"
echo "1. From source: git clone https://github.com/bats-core/bats-core.git && cd bats-core && ./install.sh /usr/local"
echo "2. Using npm: npm install -g bats"
echo "3. Using Homebrew (if available): brew install bats-core"

echo "\n✅ Skill documentation is ready. Install bats-core manually as needed."
