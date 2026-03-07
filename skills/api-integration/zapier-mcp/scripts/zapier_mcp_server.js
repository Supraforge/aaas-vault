#!/usr/bin/env node
"""
Zapier MCP Server for Model Context Protocol
"""
const { Server } = require('@modelcontextprotocol/sdk');
const { ZapierAPI } = require('./zapier_api.js');
const dotenv = require('dotenv');

dotenv.config();

const server = new Server(
  {
    name: 'zapier-mcp',
    version: '1.0.0',
  },
  {
    capabilities: {
      resources: {},
      tools: {},
    },
  }
);

const zapier = new ZapierAPI(process.env.ZAPIER_API_KEY);

// Tool: List zaps
server.setRequestHandler('tools/list_zaps', async () => {
  try {
    const zaps = await zapier.listZaps();
    return {
      content: [{
        type: 'text',
        text: JSON.stringify(zaps, null, 2)
      }]
    };
  } catch (error) {
    return {
      content: [{
        type: 'text',
        text: `Error: ${error.message}`
      }],
      isError: true
    };
  }
});

// Tool: Trigger zap
server.setRequestHandler('tools/trigger_zap', async (request) => {
  const { zap_id, data } = request.params.arguments;
  
  try {
    const result = await zapier.triggerZap(zap_id, data);
    return {
      content: [{
        type: 'text',
        text: JSON.stringify(result, null, 2)
      }]
    };
  } catch (error) {
    return {
      content: [{
        type: 'text',
        text: `Error: ${error.message}`
      }],
      isError: true
    };
  }
});

// Tool: Get zap executions
server.setRequestHandler('tools/get_executions', async (request) => {
  const { zap_id, limit } = request.params.arguments;
  
  try {
    const executions = await zapier.getExecutions(zap_id, limit || 10);
    return {
      content: [{
        type: 'text',
        text: JSON.stringify(executions, null, 2)
      }]
    };
  } catch (error) {
    return {
      content: [{
        type: 'text',
        text: `Error: ${error.message}`
      }],
      isError: true
    };
  }
});

// Tool: Create webhook zap
server.setRequestHandler('tools/create_webhook_zap', async (request) => {
  const { name, trigger_app, action_app } = request.params.arguments;
  
  try {
    const zap = await zapier.createWebhookZap(name, trigger_app, action_app);
    return {
      content: [{
        type: 'text',
        text: JSON.stringify(zap, null, 2)
      }]
    };
  } catch (error) {
    return {
      content: [{
        type: 'text',
        text: `Error: ${error.message}`
      }],
      isError: true
    };
  }
});

// Start server
server.listen().catch(console.error);

console.log('🚀 Zapier MCP server running...');
