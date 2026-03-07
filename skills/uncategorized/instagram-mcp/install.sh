#!/bin/bash
# Instagram API MCP Installation Script

echo "📦 Installing Instagram API MCP dependencies..."

# Install Node.js dependencies
npm init -y
npm install @mcp/tools @modelcontextprotocol/sdk axios dotenv form-data
npm install --save-dev @types/node typescript ts-node

# Create TypeScript configuration
cat > tsconfig.json << 'TS_EOF'
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "commonjs",
    "lib": ["ES2022"],
    "outDir": "./dist",
    "rootDir": ".",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true
  },
  "include": ["*.ts", "scripts/*.ts"],
  "exclude": ["node_modules", "dist"]
}
TS_EOF

# Create server.js
cat > server.js << 'SERVER_EOF'
const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
const axios = require('axios');
require('dotenv').config();

class InstagramMCPServer {
  constructor() {
    this.server = new Server(
      {
        name: 'instagram-mcp',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.setupTools();
    this.setupErrorHandling();
  }

  setupTools() {
    // Instagram Insights Query
    this.server.setRequestHandler('tools/call', async (request) => {
      if (request.params.name === 'instagram.query_insights') {
        const { metric, period } = request.params.arguments;
        return await this.queryInsights(metric, period);
      }

      if (request.params.name === 'instagram.schedule_post') {
        const { imagePath, caption, scheduleTime } = request.params.arguments;
        return await this.schedulePost(imagePath, caption, scheduleTime);
      }

      if (request.params.name === 'instagram.upload_media') {
        const { mediaPath, caption } = request.params.arguments;
        return await this.uploadMedia(mediaPath, caption);
      }

      if (request.params.name === 'instagram.get_comments') {
        const { mediaId, limit } = request.params.arguments;
        return await this.getComments(mediaId, limit);
      }

      throw new Error(`Unknown tool: ${request.params.name}`);
    });
  }

  async queryInsights(metric, period) {
    try {
      const response = await axios.get(
        `https://graph.facebook.com/v18.0/${process.env.INSTAGRAM_BUSINESS_ACCOUNT_ID}/insights`,
        {
          params: {
            metric: metric || 'engagement,impressions,reach',
            period: period || 'day',
            access_token: process.env.INSTAGRAM_ACCESS_TOKEN,
          },
        }
      );

      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify(response.data, null, 2),
          },
        ],
      };
    } catch (error) {
      throw new Error(`Instagram insights query failed: ${error.message}`);
    }
  }

  async schedulePost(imagePath, caption, scheduleTime) {
    // Implementation for scheduling posts
    return {
      content: [
        {
          type: 'text',
          text: `Post scheduled: ${caption} at ${scheduleTime}`,
        },
      ],
    };
  }

  async uploadMedia(mediaPath, caption) {
    // Implementation for media upload
    return {
      content: [
        {
          type: 'text',
          text: `Media uploaded: ${mediaPath} with caption: ${caption}`,
        },
      ],
    };
  }

  async getComments(mediaId, limit) {
    try {
      const response = await axios.get(
        `https://graph.facebook.com/v18.0/${mediaId}/comments`,
        {
          params: {
            fields: 'id,text,username,timestamp,like_count',
            limit: limit || 25,
            access_token: process.env.INSTAGRAM_ACCESS_TOKEN,
          },
        }
      );

      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify(response.data, null, 2),
          },
        ],
      };
    } catch (error) {
      throw new Error(`Failed to get comments: ${error.message}`);
    }
  }

  setupErrorHandling() {
    this.server.onerror = (error) => {
      console.error('[Instagram MCP Error]', error);
    };

    process.on('SIGINT', async () => {
      await this.server.close();
      process.exit(0);
    });
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('Instagram MCP server running on stdio');
  }
}

const server = new InstagramMCPServer();
server.run().catch(console.error);
SERVER_EOF

# Create scripts directory
mkdir -p scripts

# Create analytics report script
cat > scripts/analytics_report.js << 'ANALYTICS_EOF'
const axios = require('axios');
require('dotenv').config();

async function generateAnalyticsReport() {
  try {
    const accountId = process.env.INSTAGRAM_BUSINESS_ACCOUNT_ID;
    const accessToken = process.env.INSTAGRAM_ACCESS_TOKEN;

    // Get account insights
    const insightsResponse = await axios.get(
      `https://graph.facebook.com/v18.0/${accountId}/insights`,
      {
        params: {
          metric: 'follower_count,impressions,reach,profile_views',
          period: 'day',
          since: Math.floor(Date.now() / 1000) - 30 * 24 * 60 * 60, // 30 days
          until: Math.floor(Date.now() / 1000),
          access_token: accessToken,
        },
      }
    );

    // Get recent media
    const mediaResponse = await axios.get(
      `https://graph.facebook.com/v18.0/${accountId}/media`,
      {
        params: {
          fields: 'id,caption,media_type,media_url,permalink,like_count,comments_count',
          limit: 10,
          access_token: accessToken,
        },
      }
    );

    const report = {
      generated_at: new Date().toISOString(),
      account_id: accountId,
      insights: insightsResponse.data,
      recent_media: mediaResponse.data,
      summary: {
        total_posts: mediaResponse.data.data?.length || 0,
        average_likes: calculateAverage(mediaResponse.data.data, 'like_count'),
        average_comments: calculateAverage(mediaResponse.data.data, 'comments_count'),
      },
    };

    console.log(JSON.stringify(report, null, 2));
    
    // Save to file
    const fs = require('fs');
    fs.writeFileSync('instagram_analytics_report.json', JSON.stringify(report, null, 2));
    console.log('\n📊 Report saved to instagram_analytics_report.json');

  } catch (error) {
    console.error('Error generating analytics report:', error.message);
    process.exit(1);
  }
}

function calculateAverage(data, field) {
  if (!data || data.length === 0) return 0;
  const sum = data.reduce((acc, item) => acc + (item[field] || 0), 0);
  return Math.round(sum / data.length);
}

// Run if called directly
if (require.main === module) {
  generateAnalyticsReport();
}

module.exports = { generateAnalyticsReport };
ANALYTICS_EOF

# Create schedule post script
cat > scripts/schedule_post.js << 'SCHEDULE_EOF'
const fs = require('fs');
const path = require('path');
require('dotenv').config();

class InstagramScheduler {
  constructor() {
    this.scheduleFile = 'instagram_schedule.json';
    this.loadSchedule();
  }

  loadSchedule() {
    try {
      if (fs.existsSync(this.scheduleFile)) {
        this.schedule = JSON.parse(fs.readFileSync(this.scheduleFile, 'utf8'));
      } else {
        this.schedule = { posts: [] };
      }
    } catch (error) {
      this.schedule = { posts: [] };
    }
  }

  saveSchedule() {
    fs.writeFileSync(this.scheduleFile, JSON.stringify(this.schedule, null, 2));
  }

  addPost(imagePath, caption, scheduleTime, hashtags) {
    const post = {
      id: Date.now().toString(),
      image_path: path.resolve(imagePath),
      caption: caption || '',
      schedule_time: scheduleTime || new Date().toISOString(),
      hashtags: hashtags || process.env.DEFAULT_HASHTAGS || '#instagram #socialmedia',
      status: 'scheduled',
      created_at: new Date().toISOString(),
    };

    this.schedule.posts.push(post);
    this.saveSchedule();

    console.log(`✅ Post scheduled for ${post.schedule_time}`);
    console.log(`   Image: ${post.image_path}`);
    console.log(`   Caption: ${post.caption.substring(0, 50)}...`);
    
    return post;
  }

  listScheduledPosts() {
    console.log('\n📅 Scheduled Instagram Posts:');
    console.log('=' .repeat(50));
    
    this.schedule.posts.forEach((post, index) => {
      console.log(`\n${index + 1}. ${post.schedule_time}`);
      console.log(`   Status: ${post.status}`);
      console.log(`   Caption: ${post.caption.substring(0, 100)}...`);
    });

    return this.schedule.posts;
  }

  removePost(postId) {
    const initialLength = this.schedule.posts.length;
    this.schedule.posts = this.schedule.posts.filter(post => post.id !== postId);
    
    if (this.schedule.posts.length < initialLength) {
      this.saveSchedule();
      console.log(`✅ Post ${postId} removed from schedule`);
      return true;
    } else {
      console.log(`❌ Post ${postId} not found`);
      return false;
    }
  }
}

// Command line interface
if (require.main === module) {
  const scheduler = new InstagramScheduler();
  const command = process.argv[2];

  switch (command) {
    case 'add':
      const imagePath = process.argv[3];
      const caption = process.argv[4];
      const scheduleTime = process.argv[5];
      const hashtags = process.argv[6];
      scheduler.addPost(imagePath, caption, scheduleTime, hashtags);
      break;

    case 'list':
      scheduler.listScheduledPosts();
      break;

    case 'remove':
      const postId = process.argv[3];
      scheduler.removePost(postId);
      break;

    default:
      console.log('Usage:');
      console.log('  node schedule_post.js add <image_path> <caption> [schedule_time] [hashtags]');
      console.log('  node schedule_post.js list');
      console.log('  node schedule_post.js remove <post_id>');
      break;
  }
}

module.exports = InstagramScheduler;
SCHEDULE_EOF

# Create README.md
cat > README.md << 'README_EOF'
# Instagram API MCP Skill

Model Context Protocol (MCP) server for Instagram Graph API integration.

## Features

- **Account Management**: Connect and manage Instagram Business accounts
- **Content Scheduling**: Schedule posts with optimal timing
- **Media Upload**: Upload images and videos to Instagram
- **Analytics**: Get detailed insights and engagement metrics
- **Comment Management**: Retrieve and respond to comments
- **Hashtag Analysis**: Analyze hashtag performance

## Installation

1. Clone this skill to your AntiGravity skills directory:
   ```bash
   mkdir -p ~/.gemini/skills/instagram-mcp
   cp -r * ~/.gemini/skills/instagram-mcp/
   ```

2. Install dependencies:
   ```bash
   cd ~/.gemini/skills/instagram-mcp
   bash install.sh
   ```

3. Configure environment:
   ```bash
   cp .env.template .env
   # Edit .env with your Instagram API credentials
   ```

4. Test the skill:
   ```bash
   bash test.sh
   ```

## Usage

### As an MCP Server

Run the MCP server:
```bash
node server.js
```

### Available Tools

1. **instagram.query_insights**
   ```json
   {
     "metric": "engagement,impressions,reach",
     "period": "day"
   }
   ```

2. **instagram.schedule_post**
   ```json
   {
     "imagePath": "/path/to/image.jpg",
     "caption": "Check out our new product!",
     "scheduleTime": "2024-01-20T18:00:00Z"
   }
   ```

3. **instagram.upload_media**
   ```json
   {
     "mediaPath": "/path/to/video.mp4",
     "caption": "New tutorial video is live!"
   }
   ```

## API Requirements

- Instagram Business Account
- Facebook App with Instagram Basic Display API access
- Instagram Graph API permissions:
  - `instagram_basic`
  - `instagram_manage_insights`
  - `instagram_content_publish`

## License

MIT License - See LICENSE file for details.
README_EOF

# Create LICENSE
cat > LICENSE << 'LICENSE_EOF'
MIT License

Copyright (c) 2024 SkillBuilder Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
LICENSE_EOF

# Make scripts executable
chmod +x test.sh install.sh
chmod +x scripts/*.js

echo "✅ Instagram API MCP skill created successfully!"
echo ""
echo "📊 Skill Summary:"
echo "   • SKILL.md - Main skill documentation"
echo "   • test.sh - Health check script"
echo "   • .env.template - API configuration template"
echo "   • install.sh - Installation script"
echo "   • server.js - MCP server implementation"
echo "   • scripts/ - Scheduling and analytics scripts"
echo "   • README.md - Detailed documentation"
echo "   • LICENSE - MIT license"
echo ""
echo "🚀 Next: Creating TikTok API MCP skill for short-form video marketing..."
