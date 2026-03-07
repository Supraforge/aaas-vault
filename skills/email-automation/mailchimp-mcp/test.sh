#!/bin/bash
# Mailchimp MCP Skill Health Check
echo "🔍 Testing Mailchimp MCP skill..."

# Check for required dependencies
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install python3."
    exit 1
fi

if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install node."
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm."
    exit 1
fi

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Create from .env.template"
    echo "   Required variables: MAILCHIMP_API_KEY, MAILCHIMP_SERVER_PREFIX"
fi

# Check Python dependencies
if python3 -c "import requests" 2>/dev/null; then
    echo "✅ Python requests library installed"
else
    echo "⚠️  Python requests library not installed"
fi

# Check Node.js dependencies
if [ -f package.json ]; then
    echo "✅ Node.js package.json found"
else
    echo "⚠️  Node.js package.json not found"
fi

echo "✅ Mailchimp MCP skill health check completed"
echo ""
echo "To start MCP server: node scripts/mailchimp_mcp_server.js"
echo "To run Python automation: python3 scripts/mailchimp_automation.py"
