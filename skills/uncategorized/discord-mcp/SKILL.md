---
name: discord-mcp
description: >-
  Integrates with Discord API for community engagement, server management, and
  automated interactions
version: 1.0.0
dependencies:
  - nodejs
  - npm
  - python3
  - curl
inputs:
  - name: discord_token
    description: Discord bot token for authentication
  - name: server_id
    description: Discord server ID for targeted operations
  - name: channel_id
    description: Channel ID for message operations
outputs:
  - type: stdout
    description: JSON response from Discord API operations
  - type: file
    description: Log files and exported data
compatibility: 'agent-zero, claude-code, cursor'
---

# Discord API MCP Integration

## 🎯 Triggers
- When you need to manage Discord communities
- When automating community engagement
- When monitoring Discord channels for mentions
- When sending announcements to Discord servers
- When analyzing community activity and engagement

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/discord-mcp/test.sh`.
- [ ] Check `.env` contains required Discord bot token.
- [ ] Ensure Node.js and npm are installed.

## 📋 Workflow
1. **Authentication Setup**: Configure Discord bot token in `.env`
2. **Server Connection**: Connect to Discord gateway
3. **Event Handling**: Set up listeners for messages, reactions, members
4. **Automation**: Implement scheduled tasks and triggers
5. **Analytics**: Collect and analyze community data

## 🛠️ Script Reference
- Use `scripts/discord_bot.js` for Discord bot operations
- Use `scripts/community_analytics.py` for engagement analysis
- Use `scripts/automation_tasks.js` for scheduled tasks

## 🔧 Discord Bot Setup

### 1. Create Discord Application
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Name your application
4. Navigate to "Bot" section
5. Click "Add Bot"
6. Copy the bot token

### 2. Bot Permissions
Required permissions:
- Read Messages/View Channels
- Send Messages
- Manage Messages
- Read Message History
- Add Reactions
- Use Slash Commands
- Manage Webhooks

### 3. Invite Bot to Server
Generate OAuth2 URL with:
- `bot` scope
- Required permissions
- Copy and open URL in browser

## 📊 Discord API Capabilities

### Message Operations
- Send messages to channels
- Edit existing messages
- Delete messages
- Bulk delete messages
- React to messages
- Pin/unpin messages

### Channel Management
- Create text/voice channels
- Edit channel properties
- Delete channels
- Manage channel permissions
- Create thread discussions

### Server Management
- List server members
- Manage server roles
- Kick/ban members
- Create server invites
- Manage server emojis/stickers

### Webhook Operations
- Create webhooks
- Send messages via webhooks
- Edit/delete webhooks
- Execute webhook with files

## 🤖 MCP Server Implementation

### Discord MCP Server
```javascript
// scripts/discord_mcp_server.js
const { Server } = require('@modelcontextprotocol/sdk/server');
const { DiscordClient } = require('./discord_client');

class DiscordMCPServer {
  constructor() {
    this.server = new Server({
      name: 'discord-mcp',
      version: '1.0.0'
    });
    
    this.discord = new DiscordClient();
    
    this.setupResources();
    this.setupTools();
  }
  
  setupResources() {
    this.server.setResourceHandler('discord:servers', async () => {
      const servers = await this.discord.getGuilds();
      return {
        contents: [{
          type: 'text',
          text: JSON.stringify(servers, null, 2)
        }]
      };
    });
  }
  
  setupTools() {
    this.server.setToolHandler('send_message', async (params) => {
      const { channelId, content, embed } = params;
      return await this.discord.sendMessage(channelId, content, embed);
    });
    
    this.server.setToolHandler('get_channel_messages', async (params) => {
      const { channelId, limit } = params;
      return await this.discord.getChannelMessages(channelId, limit);
    });
  }
}
```

### Discord Client
```javascript
// scripts/discord_client.js
const { Client, GatewayIntentBits } = require('discord.js');

class DiscordClient {
  constructor() {
    this.client = new Client({
      intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMembers
      ]
    });
    
    this.client.on('ready', () => {
      console.log(`Logged in as ${this.client.user.tag}!`);
    });
  }
  
  async login(token) {
    await this.client.login(token);
  }
  
  async sendMessage(channelId, content, embed = null) {
    const channel = await this.client.channels.fetch(channelId);
    const options = embed ? { embeds: [embed] } : {};
    return await channel.send({ content, ...options });
  }
}
```

## 📈 Community Analytics

### Engagement Metrics
- Daily active members
- Message volume trends
- Reaction usage patterns
- Most active channels
- Peak activity times

### Member Analysis
- New member retention
- Role distribution
- Join/leave patterns
- Top contributors
- Inactive members

### Content Analysis
- Most discussed topics
- Popular emoji usage
- Link sharing patterns
- Media upload trends
- Command usage statistics

## 🔌 Integration Examples

### With Social Media
```javascript
// When new Instagram post is published
await discord.sendMessage({
  channelId: 'announcements-channel',
  content: `📸 New Instagram post! Check it out: ${postUrl}`,
  embed: {
    title: postTitle,
    description: postDescription,
    image: { url: postImage }
  }
});
```

### With E-commerce
```javascript
// When new order is placed
await discord.sendMessage({
  channelId: 'sales-channel',
  content: `🛒 New order #${orderId} from ${customerName}`,
  embed: {
    title: 'New Order Alert',
    fields: [
      { name: 'Amount', value: `$${orderAmount}`, inline: true },
      { name: 'Items', value: orderItems.join(', '), inline: true }
    ]
  }
});
```

### With Support Systems
```javascript
// When support ticket is created
await discord.sendMessage({
  channelId: 'support-alerts',
  content: `🆘 New support ticket from ${userName}`,
  embed: {
    title: ticketSubject,
    description: ticketDescription,
    color: 0xff0000
  }
});
```

## 🚀 Advanced Features

### Slash Commands
- `/announce` - Send announcement to channel
- `/poll` - Create interactive poll
- `/stats` - Show server statistics
- `/welcome` - Configure welcome messages
- `/moderate` - Moderation tools

### Automated Moderation
- Spam detection
- Bad word filtering
- Link verification
- Role assignment automation
- Welcome message automation

### Scheduled Tasks
- Daily announcements
- Weekly statistics
- Birthday announcements
- Event reminders
- Content scheduling

## 📁 File Structure
```
discord-mcp/
├── SKILL.md
├── .env.template
├── install.sh
├── test.sh
├── scripts/
│   ├── discord_bot.js
│   ├── discord_mcp_server.js
│   ├── discord_client.js
│   ├── community_analytics.py
│   ├── automation_tasks.js
│   └── moderation_tools.js
└── templates/
    ├── welcome_message.md
    ├── announcement_template.md
    └── embed_templates.json
```
