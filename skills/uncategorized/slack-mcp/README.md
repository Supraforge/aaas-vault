# Slack API MCP Skill

## 🚀 Quick Deployment

```bash
# 1. Clone or copy to AntiGravity skills directory
cp -r /path/to/slack-mcp ~/.gemini/skills/

# 2. Navigate to skill directory
cd ~/.gemini/skills/slack-mcp

# 3. Install dependencies
./install.sh

# 4. Configure environment
cp .env.template .env
# Edit .env with your Slack tokens

# 5. Test installation
./test.sh

# 6. Start MCP server
npm start
```

## 🔧 Slack App Setup

1. Create a new Slack app at https://api.slack.com/apps
2. Add OAuth Scopes:
   - `channels:read`
   - `channels:write`
   - `chat:write`
   - `files:write`
   - `users:read`
3. Install app to workspace
4. Copy tokens to `.env` file

## 📊 Business Use Cases

### Team Communication
- Automated standup reminders
- Meeting notifications
- Announcement broadcasts

### Customer Support
- Support ticket notifications
- Customer feedback collection
- Escalation alerts

### Sales & Marketing
- Lead notification routing
- Campaign performance alerts
- Team performance updates

### Operations
- System status alerts
- Deployment notifications
- Incident management

## 🔌 Integration Examples

### With CRM Systems
```javascript
// When new lead is created in CRM
await slack.chat.postMessage({
  channel: '#sales-leads',
  text: `🎯 New lead: ${lead.name} from ${lead.source}`
});
```

### With Monitoring Tools
```javascript
// When server goes down
await slack.chat.postMessage({
  channel: '#devops-alerts',
  text: `🚨 Server ${serverName} is down! Response time: ${responseTime}ms`
});
```

### With Project Management
```javascript
// When task is completed
await slack.chat.postMessage({
  channel: '#project-updates',
  text: `✅ Task completed: ${taskTitle} by ${assignee}`
});
```
