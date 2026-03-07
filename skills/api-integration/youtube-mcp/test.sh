#!/bin/bash
# YouTube MCP Health Check

echo "🔍 Checking YouTube MCP dependencies..."

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Install with: apt-get install nodejs"
    exit 1
else
    echo "✅ Node.js $(node --version)"
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Install with: apt-get install npm"
    exit 1
else
    echo "✅ npm $(npm --version)"
fi

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file missing. Copy from .env.template"
    if [ -f .env.template ]; then
        cp .env.template .env
        echo "📋 Created .env from template. Please update with your credentials."
    fi
else
    echo "✅ .env file present"
fi

# Check required environment variables
if [ -f .env ]; then
    required_vars=("GOOGLE_CLIENT_ID" "GOOGLE_CLIENT_SECRET" "GOOGLE_REDIRECT_URI" "YOUTUBE_CHANNEL_ID")
    missing_vars=()
    
    for var in "${required_vars[@]}"; do
        if ! grep -q "^$var=" .env; then
            missing_vars+=("$var")
        fi
    done
    
    if [ ${#missing_vars[@]} -eq 0 ]; then
        echo "✅ All required environment variables found"
    else
        echo "⚠️  Missing environment variables: ${missing_vars[*]}"
    fi
fi

# Check if server.js exists
if [ ! -f server.js ]; then
    echo "⚠️  server.js not found. Creating basic MCP server..."
    cat > server.js << 'SERVER_EOF'
const { Server } = require('@modelcontextprotocol/sdk/server');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio');
const { GoogleApis } = require('googleapis');
require('dotenv').config();

class YouTubeMCP {
  constructor() {
    this.youtube = null;
    this.initializeYouTube();
  }
  
  async initializeYouTube() {
    const { google } = require('googleapis');
    const oauth2Client = new google.auth.OAuth2(
      process.env.GOOGLE_CLIENT_ID,
      process.env.GOOGLE_CLIENT_SECRET,
      process.env.GOOGLE_REDIRECT_URI
    );
    
    // Set credentials if available
    if (process.env.GOOGLE_ACCESS_TOKEN) {
      oauth2Client.setCredentials({
        access_token: process.env.GOOGLE_ACCESS_TOKEN,
        refresh_token: process.env.GOOGLE_REFRESH_TOKEN
      });
    }
    
    this.youtube = google.youtube({ version: 'v3', auth: oauth2Client });
  }
  
  async getChannelAnalytics() {
    try {
      const response = await this.youtube.channels.list({
        part: ['snippet', 'contentDetails', 'statistics'],
        id: process.env.YOUTUBE_CHANNEL_ID,
        mine: true
      });
      return response.data.items[0];
    } catch (error) {
      console.error('Error fetching channel analytics:', error);
      throw error;
    }
  }
}

const server = new Server(
  { name: 'youtube-mcp', version: '1.0.0' },
  { capabilities: { tools: {} } }
);

const youtubeMCP = new YouTubeMCP();

server.setRequestHandler(async (request) => {
  if (request.method === 'tools/list') {
    return {
      tools: [
        {
          name: 'get_youtube_analytics',
          description: 'Get YouTube channel analytics',
          inputSchema: {
            type: 'object',
            properties: {}
          }
        }
      ]
    };
  }
  
  if (request.method === 'tools/call') {
    const { name, arguments: args } = request.params;
    
    if (name === 'get_youtube_analytics') {
      try {
        const analytics = await youtubeMCP.getChannelAnalytics();
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(analytics, null, 2)
            }
          ]
        };
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: `Error: ${error.message}`
            }
          ],
          isError: true
        };
      }
    }
  }
  
  return { error: { code: -32601, message: 'Method not found' } };
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch(console.error);
SERVER_EOF
    echo "📄 Created basic server.js"
else
    echo "✅ server.js present"
fi

# Check package.json
if [ ! -f package.json ]; then
    echo "📦 Creating package.json..."
    cat > package.json << 'PKG_EOF'
{
  "name": "youtube-mcp",
  "version": "1.0.0",
  "description": "YouTube API MCP integration",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "test": "bash test.sh"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.6.0",
    "googleapis": "^128.0.0",
    "express": "^4.18.2",
    "dotenv": "^16.3.1",
    "axios": "^1.6.0",
    "csv-writer": "^1.6.0"
  },
  "keywords": ["mcp", "youtube", "api", "analytics", "video"],
  "author": "SkillBuilder",
  "license": "MIT"
}
PKG_EOF
    echo "📄 Created package.json"
else
    echo "✅ package.json present"
fi

echo "\n✅ YouTube MCP health check completed!"
echo "\n📋 Next steps:"
echo "1. Update .env with your Google API credentials"
echo "2. Run 'npm install' to install dependencies"
echo "3. Run 'npm start' to start the MCP server"
echo "4. Configure OAuth 2.0 in Google Cloud Console"
