#!/bin/bash
# YouTube MCP Installation Script

echo "🚀 Installing YouTube MCP dependencies..."

# Update package list
apt-get update

# Install Node.js and npm if not present
if ! command -v node &> /dev/null; then
    echo "📦 Installing Node.js..."
    apt-get install -y nodejs npm
fi

# Navigate to skill directory
cd "$(dirname "$0")"

# Install npm dependencies
if [ -f package.json ]; then
    echo "📦 Installing npm packages..."
    npm install
    
    # Check for specific packages
    if ! npm list googleapis &> /dev/null; then
        echo "📦 Installing googleapis..."
        npm install googleapis
    fi
    
    if ! npm list @modelcontextprotocol/sdk &> /dev/null; then
        echo "📦 Installing MCP SDK..."
        npm install @modelcontextprotocol/sdk
    fi
else
    echo "❌ package.json not found. Creating..."
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
  }
}
PKG_EOF
    npm install
fi

# Create scripts directory
mkdir -p scripts

# Create basic scripts
cat > scripts/upload_video.js << 'SCRIPT_EOF'
const { google } = require('googleapis');
const fs = require('fs');
const path = require('path');
require('dotenv').config();

class YouTubeUploader {
  constructor() {
    this.youtube = null;
    this.initialize();
  }
  
  async initialize() {
    const oauth2Client = new google.auth.OAuth2(
      process.env.GOOGLE_CLIENT_ID,
      process.env.GOOGLE_CLIENT_SECRET,
      process.env.GOOGLE_REDIRECT_URI
    );
    
    if (process.env.GOOGLE_ACCESS_TOKEN) {
      oauth2Client.setCredentials({
        access_token: process.env.GOOGLE_ACCESS_TOKEN,
        refresh_token: process.env.GOOGLE_REFRESH_TOKEN
      });
    }
    
    this.youtube = google.youtube({ version: 'v3', auth: oauth2Client });
  }
  
  async uploadVideo(videoPath, title, description, tags = [], privacyStatus = 'private') {
    try {
      const fileSize = fs.statSync(videoPath).size;
      
      const response = await this.youtube.videos.insert({
        part: ['snippet', 'status'],
        requestBody: {
          snippet: {
            title,
            description,
            tags,
            categoryId: '22'  // People & Blogs
          },
          status: {
            privacyStatus,
            selfDeclaredMadeForKids: false
          }
        },
        media: {
          body: fs.createReadStream(videoPath)
        }
      });
      
      console.log(`✅ Video uploaded successfully: ${response.data.id}`);
      console.log(`📊 Video URL: https://youtu.be/${response.data.id}`);
      
      return {
        success: true,
        videoId: response.data.id,
        url: `https://youtu.be/${response.data.id}`,
        title: response.data.snippet.title
      };
    } catch (error) {
      console.error('❌ Error uploading video:', error.message);
      return {
        success: false,
        error: error.message
      };
    }
  }
}

// Export for use in MCP server
module.exports = { YouTubeUploader };
SCRIPT_EOF

cat > scripts/get_analytics.js << 'SCRIPT_EOF'
const { google } = require('googleapis');
const { createObjectCsvWriter } = require('csv-writer');
require('dotenv').config();

class YouTubeAnalytics {
  constructor() {
    this.youtube = null;
    this.initialize();
  }
  
  async initialize() {
    const oauth2Client = new google.auth.OAuth2(
      process.env.GOOGLE_CLIENT_ID,
      process.env.GOOGLE_CLIENT_SECRET,
      process.env.GOOGLE_REDIRECT_URI
    );
    
    if (process.env.GOOGLE_ACCESS_TOKEN) {
      oauth2Client.setCredentials({
        access_token: process.env.GOOGLE_ACCESS_TOKEN,
        refresh_token: process.env.GOOGLE_REFRESH_TOKEN
      });
    }
    
    this.youtube = google.youtube({ version: 'v3', auth: oauth2Client });
  }
  
  async getChannelStats() {
    try {
      const response = await this.youtube.channels.list({
        part: ['snippet', 'contentDetails', 'statistics'],
        id: process.env.YOUTUBE_CHANNEL_ID,
        mine: true
      });
      
      const channel = response.data.items[0];
      return {
        title: channel.snippet.title,
        subscribers: channel.statistics.subscriberCount,
        views: channel.statistics.viewCount,
        videos: channel.statistics.videoCount,
        joined: channel.snippet.publishedAt
      };
    } catch (error) {
      console.error('Error fetching channel stats:', error);
      throw error;
    }
  }
  
  async exportAnalyticsToCSV() {
    try {
      const stats = await this.getChannelStats();
      const csvWriter = createObjectCsvWriter({
        path: 'youtube_analytics.csv',
        header: [
          { id: 'metric', title: 'Metric' },
          { id: 'value', title: 'Value' },
          { id: 'date', title: 'Date' }
        ]
      });
      
      const records = [
        { metric: 'Subscribers', value: stats.subscribers, date: new Date().toISOString().split('T')[0] },
        { metric: 'Total Views', value: stats.views, date: new Date().toISOString().split('T')[0] },
        { metric: 'Total Videos', value: stats.videos, date: new Date().toISOString().split('T')[0] },
        { metric: 'Channel Created', value: stats.joined, date: new Date().toISOString().split('T')[0] }
      ];
      
      await csvWriter.writeRecords(records);
      console.log('✅ Analytics exported to youtube_analytics.csv');
      
      return {
        success: true,
        file: 'youtube_analytics.csv',
        stats
      };
    } catch (error) {
      console.error('Error exporting analytics:', error);
      return {
        success: false,
        error: error.message
      };
    }
  }
}

module.exports = { YouTubeAnalytics };
SCRIPT_EOF

# Make scripts executable
chmod +x scripts/*.js

# Make shell scripts executable
chmod +x test.sh install.sh

echo "\n✅ YouTube MCP installation complete!"
echo "\n📋 Setup instructions:"
echo "1. Go to Google Cloud Console: https://console.cloud.google.com/"
echo "2. Create a new project or select existing"
echo "3. Enable YouTube Data API v3"
echo "4. Create OAuth 2.0 credentials"
echo "5. Add http://localhost:3000/oauth2callback as redirect URI"
echo "6. Copy credentials to .env file"
echo "7. Run 'npm start' to start server"
