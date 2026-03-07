#!/bin/bash
# CE Research Agent - Test Script
# Validates skill structure and basic functionality

set -e

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "Testing CE Research Agent skill..."
echo "Skill directory: $SKILL_DIR"
echo ""

# Check required files exist
echo "Checking required files..."

required_files=(
    "SKILL.md"
    "requirements.txt"
    "scripts/run.py"
    "scripts/research_base.py"
    "scripts/research_company.py"
    "scripts/research_competitors.py"
    "scripts/research_market.py"
    "scripts/research_audience.py"
    "scripts/research_brand.py"
    "scripts/research_strategy.py"
    "scripts/validate_research.py"
    "scripts/synthesize_framework.py"
    "resources/ce_prompts.json"
    "resources/section_map.json"
    "resources/squr_template.md"
)

all_passed=true

for file in "${required_files[@]}"; do
    if [ -f "$SKILL_DIR/$file" ]; then
        echo "  OK: $file"
    else
        echo "  MISSING: $file"
        all_passed=false
    fi
done

echo ""

# Check directories
echo "Checking directories..."
required_dirs=(
    "scripts"
    "resources"
    "output"
)

for dir in "${required_dirs[@]}"; do
    if [ -d "$SKILL_DIR/$dir" ]; then
        echo "  OK: $dir/"
    else
        echo "  MISSING: $dir/"
        all_passed=false
    fi
done

echo ""

# Test run.py help output
echo "Testing run.py..."
cd "$SKILL_DIR"
if python3 scripts/run.py 2>&1 | grep -q "CE Research Agent"; then
    echo "  OK: run.py executes correctly"
else
    echo "  FAIL: run.py did not execute correctly"
    all_passed=false
fi

echo ""

# Validate JSON files
echo "Validating JSON resources..."

if python3 -c "import json; json.load(open('$SKILL_DIR/resources/ce_prompts.json'))" 2>/dev/null; then
    echo "  OK: ce_prompts.json is valid JSON"
else
    echo "  FAIL: ce_prompts.json is invalid"
    all_passed=false
fi

if python3 -c "import json; json.load(open('$SKILL_DIR/resources/section_map.json'))" 2>/dev/null; then
    echo "  OK: section_map.json is valid JSON"
else
    echo "  FAIL: section_map.json is invalid"
    all_passed=false
fi

echo ""

# Summary
if $all_passed; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed!"
    exit 1
fi
