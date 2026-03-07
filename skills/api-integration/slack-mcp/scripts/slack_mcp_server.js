#!/usr/bin/env node

const { Server } = require('@modelcontextprotocol/sdk');
const { WebClient } = require('@slack/web-api');
const { App } = require('@slack/bolt');
const express = require('express');
require('dotenv').config();

class SlackMCPServer {
  constructor() {
    this.server = new Server(
      {
        name: 'slack-mcp-server',
        version: '1.0.0',
      },
      {
        capabilities: {
          resources: {},
          tools: {},
        },
      }
    );

    // Initialize Slack clients
    this.slackWeb = new WebClient(process.env.SLACK_BOT_TOKEN);
    this.slackApp = new App({
      token: process.env.SLACK_BOT_TOKEN,
      signingSecret: process.env.SLACK_SIGNING_SECRET,
      socketMode: true,
      appToken: process.env.SLACK_APP_TOKEN,
    });

    this.setupTools();
    this.setupResources();
  }

  setupTools() {
    this.server.setRequestHandler('tools/list', async () => ({
      tools: [
        {
          name: 'slack_send_message',
          description: 'Send a message to a Slack channel',
          inputSchema: {
            type: 'object',
            properties: {
              channel: { type: 'string', description: 'Channel ID or name' },
              text: { type: 'string', description: 'Message text' },
              blocks: { type: 'array', description: 'Message blocks (optional)' },
            },
            required: ['channel', 'text'],
          },
        },
        {
          name: 'slack_list_channels',
          description: 'List all Slack channels',
          inputSchema: {
            type: 'object',
            properties: {
              types: { 
                type: 'array', 
                description: 'Channel types (public_channel, private_channel, mpim, im)',
                default: ['public_channel']
              },
              limit: { type: 'number', description: 'Maximum results', default: 100 },
            },
          },
        },
        {
          name: 'slack_get_user_info',
          description: 'Get information about a Slack user',
          inputSchema: {
            type: 'object',
            properties: {
              user: { type: 'string', description: 'User ID' },
            },
            required: ['user'],
          },
        },
        {
          name: 'slack_upload_file',
          description: 'Upload a file to Slack',
          inputSchema: {
            type: 'object',
            properties: {
              channel: { type: 'string', description: 'Channel ID' },
              filepath: { type: 'string', description: 'Path to file' },
              title: { type: 'string', description: 'File title (optional)' },
            },
            required: ['channel', 'filepath'],
          },
        },
        {
          name: 'slack_create_channel',
          description: 'Create a new Slack channel',
          inputSchema: {
            type: 'object',
            properties: {
              name: { type: 'string', description: 'Channel name' },
              is_private: { type: 'boolean', description: 'Private channel?', default: false },
            },
            required: ['name'],
          },
        },
      ],
    }));

    this.server.setRequestHandler('tools/call', async (request) => {
      const { name, arguments: args } = request.params;
      
      try {
        switch (name) {
          case 'slack_send_message':
            const result = await this.slackWeb.chat.postMessage({
              channel: args.channel,
              text: args.text,
              blocks: args.blocks,
            });
            return { content: [{ type: 'text', text: JSON.stringify(result, null, 2) }] };
            
          case 'slack_list_channels':
            const channels = await this.slackWeb.conversations.list({
              types: args.types?.join(','),
              limit: args.limit,
            });
            return { content: [{ type: 'text', text: JSON.stringify(channels, null, 2) }] };
            
          case 'slack_get_user_info':
            const user = await this.slackWeb.users.info({ user: args.user });
            return { content: [{ type: 'text', text: JSON.stringify(user, null, 2) }] };
            
          case 'slack_upload_file':
            const fs = require('fs');
            const fileStream = fs.createReadStream(args.filepath);
            const upload = await this.slackWeb.files.upload({
              channels: args.channel,
              file: fileStream,
              title: args.title || 'Uploaded file',
            });
            return { content: [{ type: 'text', text: JSON.stringify(upload, null, 2) }] };
            
          case 'slack_create_channel':
            const channel = await this.slackWeb.conversations.create({
              name: args.name,
              is_private: args.is_private,
            });
            return { content: [{ type: 'text', text: JSON.stringify(channel, null, 2) }] };
            
          default:
            throw new Error(`Unknown tool: ${name}`);
        }
      } catch (error) {
        return {
          content: [{ type: 'text', text: `Error: ${error.message}` }],
          isError: true,
        };
      }
    });
  }

  setupResources() {
    // Resource handlers would go here
  }

  async start() {
    await this.server.connect({
      transport: {
        type: 'stdio',
      },
    });
    console.error('Slack MCP server running on stdio');
  }
}

const server = new SlackMCPServer();
server.start().catch(console.error);
