#!/bin/bash
# Installation script for code-review skill dependencies

echo "🔧 Installing code-review skill dependencies..."

# Update package list
echo "Updating package list..."
apt-get update -qq

# Core tools
echo "Installing core tools..."
apt-get install -y -qq     python3 python3-pip python3-venv     nodejs npm     git curl jq     docker.io docker-compose

# Install yq (YAML processor)
if ! command -v yq >/dev/null 2>&1; then
    echo "Installing yq..."
    wget -q https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/local/bin/yq
    chmod +x /usr/local/bin/yq
fi

# Install Python security tools
echo "Installing Python security tools..."
pip3 install --quiet     bandit     safety     pip-audit

# Install Node.js security tools
echo "Installing Node.js security tools..."
npm install -g --silent     npm-audit     snyk

# Install Docker security tools
echo "Installing Docker security tools..."
# trivy
if ! command -v trivy >/dev/null 2>&1; then
    wget -q https://github.com/aquasecurity/trivy/releases/latest/download/trivy_0.49.1_Linux-64bit.tar.gz
    tar -xzf trivy_0.49.1_Linux-64bit.tar.gz
    mv trivy /usr/local/bin/
    rm trivy_0.49.1_Linux-64bit.tar.gz
fi

# hadolint
if ! command -v hadolint >/dev/null 2>&1; then
    wget -q https://github.com/hadolint/hadolint/releases/latest/download/hadolint-Linux-x86_64 -O /usr/local/bin/hadolint
    chmod +x /usr/local/bin/hadolint
fi

# Install infrastructure security tools
echo "Installing infrastructure security tools..."
# checkov
pip3 install --quiet checkov

# Install shellcheck
if ! command -v shellcheck >/dev/null 2>&1; then
    apt-get install -y -qq shellcheck
fi

# Install semgrep (optional)
echo "Installing semgrep (optional)..."
pip3 install --quiet semgrep

# Install sonar-scanner (optional)
echo "Note: SonarQube Scanner requires manual installation:"
echo "1. Download from https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/"
echo "2. Extract to /opt/sonar-scanner"
echo "3. Add to PATH: export PATH=$PATH:/opt/sonar-scanner/bin"

# Configure Docker service
echo "Configuring Docker service..."
systemctl start docker
systemctl enable docker 2>/dev/null || true

# Create symbolic links for pip
echo "Creating symbolic links..."
if ! command -v pip >/dev/null 2>&1; then
    ln -s /usr/bin/pip3 /usr/local/bin/pip 2>/dev/null || true
fi

if ! command -v python >/dev/null 2>&1; then
    ln -s /usr/bin/python3 /usr/local/bin/python 2>/dev/null || true
fi

echo "
✅ Installation complete!"
echo "
Next steps:"
echo "1. Run 'bash test.sh' to verify installation"
echo "2. Configure API keys for commercial tools (Snyk, SonarQube)"
echo "3. Set up project-specific analysis rules in templates/"
echo "4. Test with a sample codebase: 'bash scripts/run-security-scan.sh /path/to/code'"
