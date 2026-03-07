#!/usr/bin/env node

const express = require('express');
const bodyParser = require('body-parser');
const { WebClient } = require('@slack/web-api');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 3003;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const slack = new WebClient(process.env.SLACK_BOT_TOKEN);

// Incoming webhook endpoint
app.post('/webhook/slack', async (req, res) => {
  try {
    const { event, challenge } = req.body;
    
    // URL verification challenge
    if (challenge) {
      return res.json({ challenge });
    }
    
    // Handle different event types
    if (event && event.type === 'message') {
      console.log('Message event received:', event);
      
      // Example: Echo message back
      if (!event.subtype || event.subtype === 'message_changed') {
        await slack.chat.postMessage({
          channel: event.channel,
          text: `I received your message: ${event.text}`,
          thread_ts: event.thread_ts || event.ts
        });
      }
    }
    
    res.status(200).send('OK');
  } catch (error) {
    console.error('Webhook error:', error);
    res.status(500).send('Error processing webhook');
  }
});

// Outgoing webhook simulation
app.post('/webhook/outgoing', async (req, res) => {
  try {
    const { text, channel_name, user_name } = req.body;
    
    console.log(`Outgoing webhook: ${user_name} in ${channel_name}: ${text}`);
    
    // Process command
    if (text.includes('help')) {
      await slack.chat.postMessage({
        channel: '#' + channel_name,
        text: `Here are available commands:\n• help - Show this message\n• status - Check system status\n• users - List team members`,
      });
    }
    
    res.status(200).json({ text: 'Command processed' });
  } catch (error) {
    console.error('Outgoing webhook error:', error);
    res.status(500).json({ error: 'Processing failed' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Slack webhook server listening on port ${port}`);
  console.log(`Incoming webhook: POST http://localhost:${port}/webhook/slack`);
  console.log(`Outgoing webhook: POST http://localhost:${port}/webhook/outgoing`);
});
