#!/bin/bash
# Install script for auth-implementation-patterns skill

echo "🔧 Installing dependencies for auth-implementation-patterns..."

# Check and install Node.js if not present
if ! command -v node >/dev/null 2>&1; then
    echo "📦 Node.js not found. Installing..."
    apt-get update && apt-get install -y nodejs npm
    if command -v node >/dev/null 2>&1; then
        echo "✅ Node.js installed successfully."
    else
        echo "❌ Failed to install Node.js."
        exit 1
    fi
else
    echo "✅ Node.js already installed."
fi

# Check and install Python3 if not present
if ! command -v python3 >/dev/null 2>&1; then
    echo "📦 Python3 not found. Installing..."
    apt-get update && apt-get install -y python3 python3-pip
    if command -v python3 >/dev/null 2>&1; then
        echo "✅ Python3 installed successfully."
    else
        echo "❌ Failed to install Python3."
        exit 1
    fi
else
    echo "✅ Python3 already installed."
fi

echo "🚀 All dependencies for auth-implementation-patterns are ready."
exit 0
