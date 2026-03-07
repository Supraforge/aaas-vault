#!/bin/bash
# Installs necessary Python libraries for lead generation automation

echo "Installing dependencies for lead-generation-automation..."

# Update pip
pip install --upgrade pip

# Install core dependencies
pip install requests pandas beautifulsoup4 lxml

# Install optional dependencies for different platforms
pip install selenium webdriver-manager  # For browser automation
pip install salesforce-bulk  # For Salesforce integration
pip install hubspot  # For HubSpot integration

# Install data validation libraries
pip install email-validator phonenumbers

# Create virtual environment (optional)
echo "
To create a virtual environment:"
echo "  python3 -m venv venv"
echo "  source venv/bin/activate"
echo "  pip install -r requirements.txt"

# Create requirements.txt
cat > requirements.txt << EOF
requests>=2.28.0
pandas>=1.5.0
beautifulsoup4>=4.11.0
lxml>=4.9.0
selenium>=4.8.0
webdriver-manager>=3.8.0
salesforce-bulk>=2.2.0
hubspot>=3.0.0
email-validator>=1.3.0
phonenumbers>=8.13.0
EOF

echo "✅ Installation complete. Copy .env.template to .env and add your API keys."
