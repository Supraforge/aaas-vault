#!/bin/bash
# Installs necessary Python libraries for content strategy automation

echo "Installing dependencies for content-strategy-automation..."

# Update pip
python3 -m pip install --upgrade pip

# Install core dependencies
pip install openai requests pandas schedule

# Install Google APIs for analytics
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Install social media libraries (optional)
pip install tweepy python-linkedin

# Install email marketing libraries (optional)
pip install mailchimp-transactional

# Install content management libraries (optional)
pip install python-wordpress-xmlrpc

echo "✅ Dependencies installed. Don't forget to set up your .env file!"
echo "Copy .env.template to .env and add your API keys."
