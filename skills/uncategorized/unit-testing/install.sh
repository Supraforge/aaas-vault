#!/bin/bash
# Installation script for unit-testing skill

echo "📦 Installing dependencies for unit-testing skill..."

# Update package list
echo "\n🔄 Updating package list..."
apt-get update -qq

# Install Python testing tools
echo "\n🐍 Installing Python testing tools..."
if ! command -v pytest &> /dev/null; then
    echo "Installing pytest..."
    pip3 install pytest
fi

if ! command -v coverage &> /dev/null; then
    echo "Installing coverage..."
    pip3 install coverage
fi

# Install additional Python testing libraries
echo "\n📚 Installing additional testing libraries..."
pip3 install pytest-cov pytest-mock pytest-xdist pytest-html

# Install jq for JSON processing
echo "\n📊 Installing jq for JSON test results..."
if ! command -v jq &> /dev/null; then
    apt-get install -y jq
fi

# Install git for version control integration
echo "\n🔧 Installing git..."
if ! command -v git &> /dev/null; then
    apt-get install -y git
fi

# Create test directory structure
echo "\n📁 Creating test directory structure..."
mkdir -p tests/unit tests/integration tests/e2e

# Create sample test configuration
echo "\n⚙️  Creating sample test configuration..."
cat > pytest.ini << 'PYTEST'
[pytest]
testpaths = tests
addopts = 
    -v
    --tb=short
    --strict-markers
    --disable-warnings
    --cov=.
    --cov-report=term-missing
    --cov-report=html
    --cov-report=xml

markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: integration tests
    e2e: end-to-end tests
    unit: unit tests
PYTEST

# Create .coveragerc for coverage configuration
cat > .coveragerc << 'COVERAGE'
[run]
source = .
omit = 
    */tests/*
    */venv/*
    */.venv/*
    */__pycache__/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    if self.debug:
    raise AssertionError
    raise NotImplementedError
    if 0:
    if __name__ == .__main__.:
    @abc.abstractmethod

[html]
directory = coverage_html_report
COVERAGE

echo "\n✅ Installation complete!"
echo "\n📋 Next steps:"
echo "1. Run './test.sh' to verify installation"
echo "2. Review SKILL.md for detailed usage instructions"
echo "3. Use the skill for test automation, debugging, and TDD"
