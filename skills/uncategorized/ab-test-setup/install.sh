#!/bin/bash
# Install dependencies for A/B Test Setup skill

echo "Installing Python dependencies for A/B testing..."

pip install pandas numpy scipy matplotlib

# Optional: Install additional packages for advanced analysis
# pip install statsmodels seaborn

echo "✅ Dependencies installed."
echo "
You can now run the health check:"
echo "bash ~/.gemini/skills/ab-test-setup/test.sh"
