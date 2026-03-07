#!/bin/bash
# Installation script for python-performance-optimization skill

echo "Installing python-performance-optimization dependencies..."

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing python3..."
    apt-get update && apt-get install -y python3 python3-pip
fi

# Install optional profiling tools
echo "Installing optional profiling tools..."
pip3 install memory_profiler line_profiler

# Install additional performance tools
pip3 install py-spy snakeviz

echo "✅ python-performance-optimization dependencies installed."
echo ""
echo "To use this skill:"
echo "1. Run the health check: bash test.sh"
echo "2. Review SKILL.md for usage examples"
echo "3. Use python profiling tools as described in the skill"
