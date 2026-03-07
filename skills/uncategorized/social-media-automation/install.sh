#!/bin/bash
# Install dependencies for social media automation

echo "Installing social media automation dependencies..."

# Update package list
apt-get update -y

# Install system dependencies
apt-get install -y     python3     python3-pip     python3-venv     jq     curl     wget     git

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install --upgrade pip
pip install     tweepy     python-linkedin     facebook-sdk     instagram-private-api     openai     anthropic     google-api-python-client     google-auth-httplib2     google-auth-oauthlib     pandas     numpy     matplotlib     seaborn     schedule     python-dotenv     requests     beautifulsoup4     pillow     moviepy     textblob     vaderSentiment     scikit-learn

echo "Installation complete!"
echo "
Next steps:"
echo "1. Copy .env.template to .env"
echo "2. Add your API keys to .env"
echo "3. Run test.sh to verify setup"
echo "4. Create your content strategy in templates/content_strategy.json"
