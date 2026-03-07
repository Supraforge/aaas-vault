#!/bin/bash
# Installation script for TDD Workflows skill

echo "📦 Installing TDD Workflows dependencies..."

# Update package list
if command -v apt-get &> /dev/null; then
    echo "Updating apt package list..."
    apt-get update -y
fi

# Install Python if not present
if ! command -v python3 &> /dev/null; then
    echo "Installing Python3..."
    if command -v apt-get &> /dev/null; then
        apt-get install -y python3 python3-pip
    elif command -v yum &> /dev/null; then
        yum install -y python3 python3-pip
    elif command -v brew &> /dev/null; then
        brew install python3
    else
        echo "❌ Cannot install Python3. Please install manually."
        exit 1
    fi
fi

# Install Git if not present
if ! command -v git &> /dev/null; then
    echo "Installing Git..."
    if command -v apt-get &> /dev/null; then
        apt-get install -y git
    elif command -v yum &> /dev/null; then
        yum install -y git
    elif command -v brew &> /dev/null; then
        brew install git
    else
        echo "⚠️  Git not installed. Some features may be limited."
    fi
fi

# Install jq if not present
if ! command -v jq &> /dev/null; then
    echo "Installing jq..."
    if command -v apt-get &> /dev/null; then
        apt-get install -y jq
    elif command -v yum &> /dev/null; then
        yum install -y jq
    elif command -v brew &> /dev/null; then
        brew install jq
    else
        echo "⚠️  jq not installed. JSON parsing features may be limited."
    fi
fi

# Install Python testing packages
echo "Installing Python testing packages..."
pip3 install --upgrade pip
pip3 install pytest coverage pytest-cov pytest-xdist pytest-html

# Verify installations
echo "Verifying installations..."
if python3 -c "import pytest" 2>/dev/null; then
    echo "✅ pytest installed successfully"
else
    echo "❌ Failed to install pytest"
    exit 1
fi

if python3 -c "import coverage" 2>/dev/null; then
    echo "✅ coverage installed successfully"
else
    echo "❌ Failed to install coverage"
    exit 1
fi

if python3 -c "import pytest_cov" 2>/dev/null; then
    echo "✅ pytest-cov installed successfully"
else
    echo "❌ Failed to install pytest-cov"
    exit 1
fi

echo ""
echo "🎉 TDD Workflows dependencies installed successfully!"
echo ""
echo "Next steps:"
echo "1. Run test.sh to verify installation: bash test.sh"
echo "2. Review SKILL.md for TDD workflow guidance"
echo "3. Begin TDD orchestration with RED-GREEN-REFACTOR cycles"

exit 0
