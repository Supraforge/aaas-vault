#!/bin/bash
# Health check for bazel-build-optimization

echo "🔍 Validating bazel-build-optimization..."

# Check Bazel
if command -v bazel >/dev/null 2>&1; then
    echo "✅ Bazel installed: $(bazel version 2>/dev/null | head -1)"
else
    echo "❌ Bazel not installed"
    exit 1
fi

# Check Python3
if command -v python3 >/dev/null 2>&1; then
    echo "✅ Python3 installed: $(python3 --version)"
else
    echo "❌ Python3 not installed"
    exit 1
fi

echo "🚀 bazel-build-optimization is ready."
exit 0
