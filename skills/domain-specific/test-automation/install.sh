#!/bin/bash
# Install dependencies for test-automation skill

echo "📦 Installing test-automation dependencies..."

# Update package list
echo "Updating package list..."
apt-get update -qq

# Install system dependencies
echo "Installing system packages..."
apt-get install -y -qq     python3     python3-pip     nodejs     npm     docker.io     git     curl     wget

# Install Python packages
echo "Installing Python packages..."
pip3 install -q     selenium     playwright     pytest     pytest-playwright     requests     allure-pytest

# Install Node.js packages
echo "Installing Node.js packages..."
npm install -g -q     k6     newman     artillery

# Install Playwright browsers
echo "Installing Playwright browsers..."
python3 -m playwright install --with-deps chromium

# Install additional testing tools
echo "Installing additional testing tools..."

# Install Postman (if not present)
if ! command -v postman >/dev/null 2>&1; then
    echo "Installing Postman..."
    wget -q https://dl.pstmn.io/download/latest/linux64 -O postman.tar.gz
    tar -xzf postman.tar.gz -C /opt
    ln -sf /opt/Postman/app/Postman /usr/local/bin/postman
    rm postman.tar.gz
fi

echo "✅ test-automation dependencies installed successfully!"
echo "Run 'bash test.sh' to verify installation."
