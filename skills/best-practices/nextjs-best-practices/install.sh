#!/bin/bash
# Installation script for nextjs-best-practices
echo "Checking dependencies..."
if command -v python3 &> /dev/null; then
    echo "✓ Python3 found"
else
    echo "✗ Python3 not found"
fi
echo "Installation check completed"
