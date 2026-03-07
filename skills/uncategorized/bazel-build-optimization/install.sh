#!/bin/bash
# Install dependencies for bazel-build-optimization

echo "📦 Installing dependencies for bazel-build-optimization..."

# Install Bazel
if command -v apt-get >/dev/null 2>&1; then
    echo "Installing Bazel..."
    apt-get update
    apt-get install -y curl gnupg
    curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > /etc/apt/trusted.gpg.d/bazel.gpg
    echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list
    apt-get update
    apt-get install -y bazel
    echo "✅ Bazel installed"
else
    echo "❌ apt-get not available. Please install Bazel manually."
    exit 1
fi

# Install Python3
if ! command -v python3 >/dev/null 2>&1; then
    echo "Installing Python3..."
    apt-get install -y python3
    echo "✅ Python3 installed"
fi

echo "🚀 Installation complete."
exit 0
