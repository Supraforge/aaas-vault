# YouTube API MCP

Model Context Protocol (MCP) server for YouTube Data API v3 integration.

## Features

### Video Management
- Upload videos with metadata (title, description, tags)
- Update existing video information
- Delete videos
- Set privacy status (public, private, unlisted)

### Analytics & Reporting
- Channel statistics (subscribers, views, videos)
- Video performance metrics
- Audience demographics
- Traffic sources
- Export to CSV format

### Content Operations
- Create and manage playlists
- Schedule content publishing
- Bulk operations
- Thumbnail management

### Live Streaming
- Schedule live broadcasts
- Manage live chat
- Stream health monitoring

## Setup

1. **Google Cloud Console Setup**
   - Create project at [Google Cloud Console](https://console.cloud.google.com/)
   - Enable YouTube Data API v3
   - Create OAuth 2.0 credentials
   - Add redirect URI: `http://localhost:3000/oauth2callback`

2. **Environment Configuration**
   ```bash
   cp .env.template .env
   # Edit .env with your credentials
   ```

3. **Install Dependencies**
   ```bash
   bash install.sh
   ```

4. **Test Installation**
   ```bash
   bash test.sh
   ```

5. **Start Server**
   ```bash
   npm start
   ```

## Usage

### As MCP Server
Connect to this server from any MCP-compatible client:

```bash
# Example connection string
mcp connect youtube-mcp --config path/to/config.json
```

### Direct API Usage
```javascript
const { YouTubeUploader } = require('./scripts/upload_video');
const uploader = new YouTubeUploader();

// Upload video
await uploader.uploadVideo(
  '/path/to/video.mp4',
  'My Video Title',
  'Video description here',
  ['tag1', 'tag2'],
  'public'
);
```

## API Reference

### Tools Available

#### upload_youtube_video
Uploads a video to YouTube.

**Parameters:**
- `videoPath` (string): Path to video file
- `title` (string): Video title
- `description` (string): Video description
- `tags` (array): Array of tags
- `privacyStatus` (string): 'public', 'private', or 'unlisted'

#### get_youtube_analytics
Retrieves YouTube channel analytics.

**Parameters:**
- `format` (string): Output format ('json' or 'csv')

## Rate Limits

YouTube Data API v3 has quotas:
- 10,000 units per day
- Varies by operation type
- Monitor usage in Google Cloud Console

## Security

- Store OAuth tokens securely
- Use environment variables
- Implement token refresh
- Follow principle of least privilege

## Support

For issues or questions:
1. Check Google API status: https://status.youtube.com/
2. Review API documentation: https://developers.google.com/youtube/v3
3. Check server logs for errors

## License

MIT License - See LICENSE file for details.
