#!/bin/bash
# Health check for Notion MCP skill
echo "🔍 Checking dependencies for notion-mcp..."

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js first."
    exit 1
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm first."
    exit 1
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python3 first."
    exit 1
fi

# Check for .env
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Create one with NOTION_API_TOKEN."
    echo "Example .env content:"
    echo "NOTION_API_TOKEN=your_integration_token_here"
fi

# Check Node dependencies
if [ -f package.json ]; then
    echo "📦 Checking Node dependencies..."
    npm list @notionhq/client 2>/dev/null || echo "⚠️  @notionhq/client not installed. Run 'npm install'"
fi

# Check Python dependencies
if [ -f requirements.txt ]; then
    echo "🐍 Checking Python dependencies..."
    python3 -c "import notion_client" 2>/dev/null || echo "⚠️  notion-client not installed. Run 'pip install -r requirements.txt'"
fi

echo "✅ Notion MCP skill dependencies checked."
echo "To get started:"
echo "1. Get your Notion integration token from https://www.notion.so/my-integrations"
echo "2. Add it to your .env file as NOTION_API_TOKEN"
echo "3. Share a database with your integration"
echo "4. Run 'node scripts/notion_mcp_server.js' to start the MCP server"
