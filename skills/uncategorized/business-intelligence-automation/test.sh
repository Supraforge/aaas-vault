#!/bin/bash
# Test script for Business Intelligence Automation

echo "Testing Business Intelligence Automation skill..."

# Check for virtual environment
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Run install.sh first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check Python dependencies
echo "Checking Python dependencies..."
python3 -c "import pandas, numpy, matplotlib, seaborn, plotly, sklearn, sqlalchemy, requests, dotenv, schedule, tabulate, yaml, jinja2;print('✅ All core dependencies installed')" || echo "❌ Some dependencies missing"

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found. Copy .env.template to .env and add API keys."
else
    echo "✅ .env file found"
fi

# Test data processing script
echo "
Testing data processing capabilities..."
python3 -c "import pandas as pd;import numpy as np;df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]});print(f'✅ Pandas working: DataFrame shape {df.shape}')"

# Test API connectivity
echo "
Testing API connectivity..."
python3 -c "import requests;try:    response = requests.get('https://httpbin.org/get', timeout=5);    print(f'✅ Network connectivity: Status {response.status_code}');except Exception as e:    print(f'❌ Network issue: {e}')"

echo "
✅ Business Intelligence Automation skill test completed!"
echo "
Ready to use:"
echo "- Run 'python scripts/bi_manager.py --help' for usage"
echo "- Check templates/ for sample configurations"
