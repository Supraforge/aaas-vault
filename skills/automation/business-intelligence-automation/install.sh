#!/bin/bash
# Install dependencies for Business Intelligence Automation

echo "Installing Business Intelligence Automation skill dependencies..."

# Update package list
apt-get update -y

# Install system dependencies
apt-get install -y     python3-pip     python3-venv     jq     curl     unzip     sqlite3

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install --upgrade pip
pip install     pandas     numpy     matplotlib     seaborn     plotly     scikit-learn     sqlalchemy     psycopg2-binary     mysql-connector-python     openpyxl     requests     python-dotenv     schedule     tabulate     pyyaml     jinja2

# Install BI platform specific libraries
pip install     powerbiclient     tableauserverclient     google-analytics-data     google-auth-oauthlib

echo "Installation complete!"
echo "
Next steps:"
echo "1. Copy .env.template to .env"
echo "2. Add your BI platform API keys to .env"
echo "3. Run test.sh to verify setup"
