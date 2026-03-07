#!/bin/bash
# CRM Automation Skill - Test Script

echo "Testing CRM Automation Skill setup..."

# Check for required commands
for cmd in python3 pip curl jq; do
    if ! command -v $cmd &> /dev/null; then
        echo "❌ Missing required command: $cmd"
        exit 1
    else
        echo "✅ $cmd found"
    fi
done

# Check Python dependencies
echo "
Checking Python dependencies..."
python3 -c "import requests, pandas, numpy" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ Core Python dependencies found"
else
    echo "❌ Missing Python dependencies"
    echo "Run: pip install requests pandas numpy"
fi

# Check for .env file
if [ -f ".env" ]; then
    echo "✅ .env file found"

    # Check for common CRM API keys
    if grep -q "HUBSPOT" .env || grep -q "SALESFORCE" .env || grep -q "ZOHO" .env; then
        echo "✅ CRM API keys detected in .env"
    else
        echo "⚠️  No CRM API keys found in .env"
        echo "Add your API keys to .env file"
    fi
else
    echo "⚠️  .env file not found"
    echo "Copy .env.template to .env and add your API keys"
fi

# Test Python scripts
echo "
Testing Python scripts..."
if [ -f "scripts/crm_manager.py" ]; then
    python3 scripts/crm_manager.py --test
    if [ $? -eq 0 ]; then
        echo "✅ CRM manager script test passed"
    else
        echo "❌ CRM manager script test failed"
    fi
fi

echo "
Test complete!"
echo "If all checks pass, your CRM automation skill is ready to use."
