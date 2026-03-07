#!/bin/bash
# Health check for code-review skill

echo "🔍 Validating code-review skill dependencies..."

declare -a required_tools=(
    "python3" "node" "git" "jq" "yq" "curl" "docker" "npm" "pip"
)

declare -a security_tools=(
    "sonar-scanner" "semgrep" "bandit" "snyk" "npm" "pip" "shellcheck" "hadolint" "checkov" "trivy"
)

echo "
✅ Checking core tools:"
for tool in "${required_tools[@]}"; do
    if command -v "$tool" >/dev/null 2>&1; then
        echo "  ✓ $tool"
    else
        echo "  ✗ $tool (missing)"
    fi
done

echo "
🔒 Checking security analysis tools:"
# Check for sonar-scanner
if command -v sonar-scanner >/dev/null 2>&1; then
    echo "  ✓ sonar-scanner"
elif [ -f "/opt/sonar-scanner/bin/sonar-scanner" ]; then
    echo "  ✓ sonar-scanner (in /opt)"
else
    echo "  ✗ sonar-scanner (optional)"
fi

# Check for semgrep
if command -v semgrep >/dev/null 2>&1; then
    echo "  ✓ semgrep"
else
    echo "  ✗ semgrep (optional)"
fi

# Check for bandit
if command -v bandit >/dev/null 2>&1; then
    echo "  ✓ bandit"
else
    echo "  ✗ bandit (optional)"
fi

# Check for snyk
if command -v snyk >/dev/null 2>&1; then
    echo "  ✓ snyk"
else
    echo "  ✗ snyk (optional - requires API key)"
fi

# Check for shellcheck
if command -v shellcheck >/dev/null 2>&1; then
    echo "  ✓ shellcheck"
else
    echo "  ✗ shellcheck (optional)"
fi

# Check for hadolint
if command -v hadolint >/dev/null 2>&1; then
    echo "  ✓ hadolint"
else
    echo "  ✗ hadolint (optional)"
fi

# Check for checkov
if command -v checkov >/dev/null 2>&1; then
    echo "  ✓ checkov"
else
    echo "  ✗ checkov (optional)"
fi

# Check for trivy
if command -v trivy >/dev/null 2>&1; then
    echo "  ✓ trivy"
else
    echo "  ✗ trivy (optional)"
fi

# Check npm-audit availability
if command -v npm >/dev/null 2>&1; then
    echo "  ✓ npm-audit (via npm)"
else
    echo "  ✗ npm (required for npm-audit)"
fi

# Check pip-audit availability
if command -v pip >/dev/null 2>&1; then
    if pip show pip-audit >/dev/null 2>&1; then
        echo "  ✓ pip-audit"
    else
        echo "  ✗ pip-audit (install with 'pip install pip-audit')"
    fi
else
    echo "  ✗ pip (required for pip-audit)"
fi

echo "
📊 Summary:"
echo "- Core tools: $(command -v python3 >/dev/null 2>&1 && echo '✓' || echo '✗') Python3"
echo "- Security scanning: Multiple tools available for comprehensive analysis"
echo "- AI integration: Manual configuration required for commercial AI tools"
echo "- Reporting: jq and yq available for JSON/YAML processing"

echo "
🚀 Code-review skill is ready for use!"
echo "Note: Some security tools require additional configuration (API keys, rulesets)."
echo "Run 'bash install.sh' to install missing dependencies."

exit 0
