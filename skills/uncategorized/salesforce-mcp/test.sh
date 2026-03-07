#!/bin/bash
# Salesforce MCP Health Check

echo "🔍 Testing Salesforce MCP Skill..."

# Check Python dependencies
if ! python3 -c "import simple_salesforce, pandas" 2>/dev/null; then
    echo "⚠️  Missing Python packages. Run: pip install simple-salesforce pandas"
fi

# Check Node.js dependencies
if [ -f "package.json" ]; then
    if ! npm list @modelcontextprotocol/sdk 2>/dev/null | grep -q @modelcontextprotocol/sdk; then
        echo "⚠️  Node.js dependencies missing. Run: npm install"
    fi
fi

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  .env file missing. Create from .env.template"
    echo "    Required variables: SALESFORCE_CLIENT_ID, SALESFORCE_CLIENT_SECRET, SALESFORCE_USERNAME, SALESFORCE_PASSWORD, SALESFORCE_INSTANCE_URL"
fi

# Check for required binaries
for cmd in python3 node jq; do
    if ! command -v $cmd &> /dev/null; then
        echo "⚠️  Missing required command: $cmd"
    fi

done

echo "✅ Salesforce MCP health check completed"
echo "   Run 'python3 scripts/salesforce_operations.py --test' to test Salesforce connection"
