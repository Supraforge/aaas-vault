#!/usr/bin/env node
"use strict";

const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
const Mailchimp = require('mailchimp-api-v3');
require('dotenv').config();

class MailchimpMCPServer {
    constructor() {
        this.mailchimp = new Mailchimp(process.env.MAILCHIMP_API_KEY);
        this.server = new Server(
            {
                name: 'mailchimp-mcp',
                version: '1.0.0',
            },
            {
                capabilities: {
                    tools: {},
                },
            }
        );
        
        this.setupTools();
        this.setupErrorHandling();
    }
    
    setupTools() {
        // List audiences
        this.server.setRequestHandler('tools/call', async (request) => {
            if (request.params.name === 'mailchimp_list_audiences') {
                try {
                    const lists = await this.mailchimp.get('/lists');
                    return {
                        content: [{
                            type: 'text',
                            text: JSON.stringify(lists, null, 2)
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
            }
            
            // Create campaign
            if (request.params.name === 'mailchimp_create_campaign') {
                try {
                    const campaign = await this.mailchimp.post('/campaigns', {
                        type: 'regular',
                        recipients: {
                            list_id: request.params.arguments?.list_id || process.env.MAILCHIMP_DEFAULT_LIST_ID
                        },
                        settings: {
                            subject_line: request.params.arguments?.subject || 'New Campaign',
                            from_name: request.params.arguments?.from_name || process.env.MAILCHIMP_FROM_NAME,
                            reply_to: request.params.arguments?.reply_to || process.env.MAILCHIMP_FROM_EMAIL
                        }
                    });
                    return {
                        content: [{
                            type: 'text',
                            text: `Campaign created: ${campaign.id}`
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
            }
            
            // Get analytics
            if (request.params.name === 'mailchimp_get_analytics') {
                try {
                    const campaignId = request.params.arguments?.campaign_id;
                    if (!campaignId) {
                        throw new Error('Campaign ID required');
                    }
                    
                    const report = await this.mailchimp.get(`/reports/${campaignId}`);
                    return {
                        content: [{
                            type: 'text',
                            text: JSON.stringify({
                                opens: report.opens,
                                clicks: report.clicks,
                                bounces: report.bounces,
                                unsubscribes: report.unsubscribes
                            }, null, 2)
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
            }
            
            // Add subscriber
            if (request.params.name === 'mailchimp_add_subscriber') {
                try {
                    const listId = request.params.arguments?.list_id || process.env.MAILCHIMP_DEFAULT_LIST_ID;
                    const email = request.params.arguments?.email;
                    
                    if (!email) {
                        throw new Error('Email required');
                    }
                    
                    const subscriber = await this.mailchimp.post(`/lists/${listId}/members`, {
                        email_address: email,
                        status: 'subscribed'
                    });
                    
                    return {
                        content: [{
                            type: 'text',
                            text: `Subscriber added: ${subscriber.id}`
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
            }
            
            return {
                content: [{
                    type: 'text',
                    text: 'Unknown tool'
                }],
                isError: true
            };
        });
    }
    
    setupErrorHandling() {
        this.server.onerror = (error) => {
            console.error('[Mailchimp MCP Server Error]', error);
        };
        
        process.on('SIGINT', async () => {
            await this.server.close();
            process.exit(0);
        });
    }
    
    async run() {
        const transport = new StdioServerTransport();
        await this.server.connect(transport);
        console.error('Mailchimp MCP server running on stdio');
    }
}

const server = new MailchimpMCPServer();
server.run().catch(console.error);
