#!/bin/bash
# Install dependencies for tdd-orchestration skill

echo "Installing dependencies for tdd-orchestration..."

# Update package list
echo "Updating package list..."
apt-get update -qq

# Install system packages
system_packages=("python3" "python3-pip" "git" "docker.io" "nodejs" "npm" "jq" "curl" "make")
for pkg in "${system_packages[@]}"; do
    if ! dpkg -l | grep -q "^ii  $pkg "; then
        echo "Installing $pkg..."
        apt-get install -y -qq $pkg
    else
        echo "✅ $pkg already installed"
    fi
done

# Install yq (YAML processor)
if ! command -v yq >/dev/null 2>&1; then
    echo "Installing yq..."
    wget -q https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/local/bin/yq
    chmod +x /usr/local/bin/yq
else
    echo "✅ yq already installed"
fi

# Install Python packages
python_packages=("pytest")
echo "Installing Python packages: ${python_packages[*]}..."
pip3 install --quiet ${python_packages[*]}

# Install Node.js packages
node_packages=("jest" "mocha")
echo "Installing Node.js packages: ${node_packages[*]}..."
npm install -g --silent ${node_packages[*]}

# Ensure pip is available
if ! command -v pip >/dev/null 2>&1; then
    ln -s /usr/bin/pip3 /usr/local/bin/pip 2>/dev/null || true
fi

# Start Docker service if not running
if systemctl is-active --quiet docker; then
    echo "✅ Docker service is running"
else
    echo "Starting Docker service..."
    systemctl start docker
    systemctl enable docker 2>/dev/null || true
fi

echo "✅ All dependencies installed successfully!"
echo "Run 'bash test.sh' to verify installation."
