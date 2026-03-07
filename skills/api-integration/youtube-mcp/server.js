const { Server } = require('@modelcontextprotocol/sdk/server');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio');
const { YouTubeUploader } = require('./scripts/upload_video');
const { YouTubeAnalytics } = require('./scripts/get_analytics');
require('dotenv').config();

class YouTubeMCP {
  constructor() {
    this.uploader = new YouTubeUploader();
    this.analytics = new YouTubeAnalytics();
  }
  
  async handleUploadVideo(args) {
    const { videoPath, title, description, tags, privacyStatus } = args;
    return await this.uploader.uploadVideo(videoPath, title, description, tags, privacyStatus);
  }
  
  async handleGetAnalytics(args) {
    const { format } = args;
    if (format === 'csv') {
      return await this.analytics.exportAnalyticsToCSV();
    } else {
      return await this.analytics.getChannelStats();
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
          name: 'upload_youtube_video',
          description: 'Upload a video to YouTube',
          inputSchema: {
            type: 'object',
            properties: {
              videoPath: { type: 'string', description: 'Path to video file' },
              title: { type: 'string', description: 'Video title' },
              description: { type: 'string', description: 'Video description' },
              tags: { type: 'array', items: { type: 'string' }, description: 'Video tags' },
              privacyStatus: { type: 'string', enum: ['public', 'private', 'unlisted'], default: 'private' }
            },
            required: ['videoPath', 'title']
          }
        },
        {
          name: 'get_youtube_analytics',
          description: 'Get YouTube channel analytics',
          inputSchema: {
            type: 'object',
            properties: {
              format: { type: 'string', enum: ['json', 'csv'], default: 'json' }
            }
          }
        }
      ]
    };
  }
  
  if (request.method === 'tools/call') {
    const { name, arguments: args } = request.params;
    
    if (name === 'upload_youtube_video') {
      try {
        const result = await youtubeMCP.handleUploadVideo(args);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2)
            }
          ]
        };
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: `Error uploading video: ${error.message}`
            }
          ],
          isError: true
        };
      }
    }
    
    if (name === 'get_youtube_analytics') {
      try {
        const result = await youtubeMCP.handleGetAnalytics(args);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2)
            }
          ]
        };
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: `Error getting analytics: ${error.message}`
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
