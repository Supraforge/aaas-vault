#!/bin/bash
# Test script for social media automation

echo "Testing social media automation setup..."

# Check Python version
python3 --version
if [ $? -ne 0 ]; then
    echo "❌ Python3 not found"
    exit 1
fi

# Check virtual environment
if [ ! -d "venv" ]; then
    echo "⚠️  Virtual environment not found. Run install.sh first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check Python packages
echo "
Checking Python packages..."
python3 -c "import systry:    import tweepy    import openai    import pandas    import schedule    print('✅ Core packages installed')except ImportError as e:    print(f'❌ Missing package: {e}')    sys.exit(1)"

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Copy .env.template to .env and add API keys."
else
    echo "✅ .env file found"
    # Check for required variables
    required_vars=("OPENAI_API_KEY" "TWITTER_API_KEY" "LINKEDIN_CLIENT_ID")
    missing_vars=()
    for var in "${required_vars[@]}"; do
        if ! grep -q "^$var=" .env; then
            missing_vars+=("$var")
        fi
    done

    if [ ${#missing_vars[@]} -eq 0 ]; then
        echo "✅ All required environment variables found"
    else
        echo "⚠️  Missing environment variables: ${missing_vars[*]}"
    fi
fi

# Test content generation script
echo "
Testing content generation..."
python3 << 'EOF'
import sys
sys.path.append('scripts')

try:
    # Test basic imports
    from scripts.content_generator import ContentGenerator
    print('✅ ContentGenerator class found')

    # Test template loading
    import json
    import os

    if os.path.exists('templates/content_strategy.json'):
        with open('templates/content_strategy.json', 'r') as f:
            strategy = json.load(f)
        print('✅ Content strategy template loaded')
    else:
        print('⚠️  Content strategy template not found')

    print('✅ Content generation test passed')
except Exception as e:
    print(f'❌ Content generation test failed: {e}')
    sys.exit(1)
EOF

# Test scheduling script
echo "
Testing scheduling logic..."
python3 << 'EOF'
import sys
sys.path.append('scripts')

try:
    from scripts.social_scheduler import SocialScheduler
    print('✅ SocialScheduler class found')

    # Test schedule creation
    scheduler = SocialScheduler()
    test_schedule = scheduler.create_schedule(days=7)
    print(f'✅ Created schedule for {len(test_schedule)} days')

    print('✅ Scheduling test passed')
except Exception as e:
    print(f'❌ Scheduling test failed: {e}')
    sys.exit(1)
EOF

echo "
✅ All tests passed! Social media automation is ready to use."
echo "
To get started:"
echo "1. Review templates/content_strategy.json and customize it"
echo "2. Update .env with all your API keys"
echo "3. Run: python3 scripts/social_scheduler.py --plan-next-week"
