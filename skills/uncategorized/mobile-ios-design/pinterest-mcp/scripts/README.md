# Pinterest MCP Scripts

## 📁 Scripts Overview

### pinterest_api.js
Main API client for Pinterest API v5. Provides:
- Authentication and connection testing
- Pin creation and management
- Board operations
- Analytics retrieval

### mcp_server.js
Model Context Protocol server exposing Pinterest functionality to AI agents.

### analytics.js
Analytics and reporting tools:
- Generate CSV/JSON reports
- Calculate engagement metrics
- Track performance over time

### scheduler.js
Content scheduling system:
- Schedule pins for future posting
- Process due scheduled pins
- Manage content calendar

## 🚀 Quick Start

1. Configure `.env` with your Pinterest access token
2. Test connection: `node pinterest_api.js test`
3. Create a pin: `node pinterest_api.js create-pin <boardId> <imageUrl> "Description"`
4. Generate report: `node analytics.js report <boardId>`
5. Schedule content: `node scheduler.js add <boardId> <imageUrl> "Description" <datetime>`

## 🔧 API Reference

All scripts use the PinterestAPI class from `pinterest_api.js`.
Key methods:
- `testConnection()` - Verify API access
- `createPin(boardId, imageUrl, description, title)` - Create new pin
- `getBoardPins(boardId, limit)` - Retrieve pins from board
- `getAnalytics(entityType, entityId, metricTypes)` - Get performance metrics
