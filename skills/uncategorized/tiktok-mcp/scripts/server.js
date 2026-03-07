// TikTok MCP Server
const { Server } = require('@modelcontextprotocol/sdk/server');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio');
const axios = require('axios');
require('dotenv').config();

const server = new Server(
  { name: 'tiktok-mcp', version: '1.0.0' },
  { capabilities: { tools: {} } }
);

// TikTok API client
class TikTokClient {
  constructor() {
    this.accessToken = process.env.TIKTOK_ACCESS_TOKEN;
    this.advertiserId = process.env.TIKTOK_ADVERTISER_ID;
    this.baseUrl = 'https://business-api.tiktok.com/open_api/v1.3';
  }

  async getVideoAnalytics(videoId) {
    const url = `${this.baseUrl}/video/analytics/`;
    const params = {
      advertiser_id: this.advertiserId,
      video_id: videoId,
      fields: 'video_info,engagement,play,share,comment,like,follower' 
    };
    
    const headers = {
      'Access-Token': this.accessToken,
      'Content-Type': 'application/json'
    };
    
    try {
      const response = await axios.get(url, { params, headers });
      return response.data;
    } catch (error) {
      console.error('Error fetching video analytics:', error.response?.data || error.message);
      throw error;
    }
  }

  async uploadVideo(videoPath, caption, scheduleTime) {
    const url = `${this.baseUrl}/video/upload/`;
    
    const formData = new FormData();
    formData.append('advertiser_id', this.advertiserId);
    formData.append('video_file', fs.createReadStream(videoPath));
    formData.append('post_info', JSON.stringify({
      caption: caption,
      schedule_time: scheduleTime
    }));
    
    const headers = {
      'Access-Token': this.accessToken
    };
    
    try {
      const response = await axios.post(url, formData, { headers });
      return response.data;
    } catch (error) {
      console.error('Error uploading video:', error.response?.data || error.message);
      throw error;
    }
  }

  async getAdCampaigns() {
    const url = `${this.baseUrl}/campaign/get/`;
    const params = {
      advertiser_id: this.advertiserId,
      page_size: 100
    };
    
    const headers = {
      'Access-Token': this.accessToken,
      'Content-Type': 'application/json'
    };
    
    try {
      const response = await axios.get(url, { params, headers });
      return response.data;
    } catch (error) {
      console.error('Error fetching campaigns:', error.response?.data || error.message);
      throw error;
    }
  }
}

// Tool definitions
server.setRequestHandler('tools/list', async () => ({
  tools: [
    {
      name: 'tiktok_get_video_analytics',
      description: 'Get analytics for a TikTok video',
      inputSchema: {
        type: 'object',
        properties: {
          videoId: { type: 'string', description: 'TikTok video ID' }
        },
        required: ['videoId']
      }
    },
    {
      name: 'tiktok_upload_video',
      description: 'Upload and schedule a TikTok video',
      inputSchema: {
        type: 'object',
        properties: {
          videoPath: { type: 'string', description: 'Path to video file' },
          caption: { type: 'string', description: 'Video caption' },
          scheduleTime: { type: 'string', description: 'Schedule time (ISO format)', format: 'date-time' }
        },
        required: ['videoPath', 'caption']
      }
    },
    {
      name: 'tiktok_get_campaigns',
      description: 'Get TikTok advertising campaigns',
      inputSchema: {
        type: 'object',
        properties: {}
      }
    }
  ]
}));

// Tool handlers
const tiktokClient = new TikTokClient();

server.setRequestHandler('tools/call', async (request) => {
  const { name, arguments: args } = request.params;
  
  switch (name) {
    case 'tiktok_get_video_analytics':
      const { videoId } = args;
      const analytics = await tiktokClient.getVideoAnalytics(videoId);
      return { content: [{ type: 'text', text: JSON.stringify(analytics, null, 2) }] };
      
    case 'tiktok_upload_video':
      const { videoPath, caption, scheduleTime } = args;
      const uploadResult = await tiktokClient.uploadVideo(videoPath, caption, scheduleTime);
      return { content: [{ type: 'text', text: JSON.stringify(uploadResult, null, 2) }] };
      
    case 'tiktok_get_campaigns':
      const campaigns = await tiktokClient.getAdCampaigns();
      return { content: [{ type: 'text', text: JSON.stringify(campaigns, null, 2) }] };
      
    default:
      throw new Error(`Unknown tool: ${name}`);
  }
});

// Start server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('TikTok MCP server running on stdio');
}

main().catch(console.error);
