---
name: daily-review
version: 1.0.0
description: >-
  Comprehensive daily performance review with communication tracking, meeting
  analysis, output metrics, and focus time monitoring. Your AI performance
  coach.
author: henrino3
tags:
  - productivity
  - performance
  - tracking
  - review
  - coach
compatibility: 'agent-zero, claude-code, cursor'
---

# Daily Review Skill

Generate comprehensive daily performance reviews with AI coaching insights.

## Features

| Feature | Source | Status |
|---------|--------|--------|
| Emails sent | Gmail API | ✅ |
| Slack messages | Slack API | ✅ |
| X.com mentions | Bird CLI | ✅ |
| Meetings attended | Fireflies (speaker verified) | ✅ |
| Git commits | git log | ✅ |
| Docs modified | Google Drive API | ✅ |
| Screen Time | macOS knowledgeC.db | ✅ |
| ActivityWatch | AW API | ✅ |

## Usage

```bash
# Run daily review for today
~/clawd/skills/daily-review/scripts/daily-review.sh

# Run for specific date
~/clawd/skills/daily-review/scripts/daily-review.sh 2026-01-15
```

## Sample Output

```
🏆 Daily Performance Review - 2026-01-15
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📬 COMMUNICATION
  • Emails sent: 6
  • Slack messages: 203
  • X.com mentions: 5

📅 MEETINGS (Fireflies - speaker verified)
  • CEO Chat (70 min)
  • Meeting with Perfectos (27 min)
  • US Squad Standup (27 min)
  Total: 3 meetings (~2.0 hrs)

💻 OUTPUT
  • Git commits: 6
  • Docs modified: 20
  • Messages to Ada: 73

⏱️ FOCUS TIME
  Screen Time: 9.7 hrs
  • Atlas: 203min
  • Slack: 163min
  • Telegram: 45min
  
  ActivityWatch: 8.5 hrs
  • Telegram: 120min
  • Ghostty: 90min
  • Chrome: 45min
```

## Requirements

### APIs & Services
- **Gmail**: Google Workspace service account or gog OAuth
- **Slack**: Slack API token (user_token for search)
- **Fireflies**: API key for meeting transcripts
- **Google Drive**: Service account for docs tracking

### Tools
- **Bird CLI**: For X.com/Twitter (requires auth_token + ct0 cookies)
- **ActivityWatch**: Local app tracking (http://localhost:5600)

### macOS (for Screen Time)
- SSH access to Mac
- `get_screentime.py` script for knowledgeC.db queries

## Installation

1. Copy skill to your clawd workspace:
```bash
cp -r daily-review ~/clawd/skills/
```

2. Install dependencies:
```bash
# Bird CLI (on Mac)
cd ~/Code && git clone https://github.com/steipete/bird.git
cd bird && npm install && npm run build:dist

# ActivityWatch
# Download from https://activitywatch.net/
```

3. Configure secrets:
```bash
# Bird (X.com)
cat > ~/clawd/secrets/bird.env << 'EOF'
AUTH_TOKEN=your_auth_token
CT0=your_ct0
EOF

# Fireflies
echo "your_api_key" > ~/clawd/secrets/fireflies.key

# Slack
echo '{"user_token": "xoxp-xxx"}' > ~/clawd/secrets/slack-super-ada.json
```

4. Add cron job for daily 09:00 review:
```bash
clawdbot cron add --name "daily-review" --schedule "0 9 * * *"
```

## Screen Time Query

The skill queries macOS Screen Time directly from `knowledgeC.db`:

```python
SELECT 
  ZVALUESTRING as app,
  SUM(ZENDDATE - ZSTARTDATE) as seconds
FROM ZOBJECT 
WHERE ZSTREAMNAME = '/app/usage' 
AND date(ZSTARTDATE + 978307200, 'unixepoch') = '2026-01-15'
GROUP BY ZVALUESTRING
ORDER BY seconds DESC
```

## Fireflies Speaker Verification

Meetings are verified by checking if user actually spoke (not just invited):

```graphql
{
  transcripts(limit: 30) {
    title dateString duration
    sentences { speaker_name }
  }
}
```

Only meetings where `speaker_name` contains user's name are counted.

## License

MIT
