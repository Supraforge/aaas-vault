#!/bin/bash
# Installation script for nx-workspace-patterns skill

set -e

echo "Installing dependencies for nx-workspace-patterns..."

# Check if Node.js is installed
if ! command -v node >/dev/null 2>&1; then
    echo "Node.js is required but not installed. Please install Node.js first."
    exit 1
fi

echo "Node.js version: $(node --version)"

echo "Installing Nx CLI globally..."
npm install -g nx

echo "Nx CLI installed: $(nx --version 2>/dev/null || echo 'version unknown')"

echo "✅ nx-workspace-patterns dependencies installed."
