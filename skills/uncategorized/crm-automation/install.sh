#!/bin/bash
# CRM Automation Skill - Installation Script

echo "Installing CRM Automation Skill..."

# Install Python dependencies
pip install requests python-dotenv pandas numpy

# Install optional dependencies for specific CRM platforms
pip install simple-salesforce  # Salesforce
pip install hubspot-api-client  # HubSpot
pip install zcrmsdk  # Zoho CRM

# Create virtual environment (optional but recommended)
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created. Activate with: source venv/bin/activate"
fi

echo "Installation complete!"
echo "Next steps:"
echo "1. Copy .env.template to .env"
echo "2. Add your CRM API keys to .env"
echo "3. Run test.sh to verify setup"
