#!/usr/bin/env node
"""
HubSpot MCP Server
Model Context Protocol server for HubSpot integration
"""

const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
const { HubSpot } = require('@hubspot/api-client');
require('dotenv').config();

class HubSpotMCPServer {
    constructor() {
        this.server = new Server(
            {
                name: 'hubspot-mcp-server',
                version: '1.0.0',
            },
            {
                capabilities: {
                    resources: {},
                    tools: {},
                },
            }
        );
        
        // Initialize HubSpot client
        this.hubspotClient = new HubSpot({
            accessToken: process.env.HUBSPOT_ACCESS_TOKEN,
        });
        
        this.setupTools();
        this.setupResources();
    }
    
    setupTools() {
        // Tool: Get contacts
        this.server.setRequestHandler('tools/call', async (request) => {
            if (request.params.name === 'get_contacts') {
                try {
                    const limit = request.params.arguments?.limit || 100;
                    const response = await this.hubspotClient.crm.contacts.getAll(limit);
                    return {
                        content: [{
                            type: 'text',
                            text: JSON.stringify(response.results, null, 2)
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
            
            // Tool: Create contact
            if (request.params.name === 'create_contact') {
                try {
                    const contactData = request.params.arguments?.contact_data;
                    if (!contactData) {
                        throw new Error('Contact data required');
                    }
                    
                    const response = await this.hubspotClient.crm.contacts.basicApi.create({
                        properties: contactData
                    });
                    
                    return {
                        content: [{
                            type: 'text',
                            text: `Contact created: ${response.id}`
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
            
            // Tool: Get companies
            if (request.params.name === 'get_companies') {
                try {
                    const limit = request.params.arguments?.limit || 100;
                    const response = await this.hubspotClient.crm.companies.getAll(limit);
                    return {
                        content: [{
                            type: 'text',
                            text: JSON.stringify(response.results, null, 2)
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
            
            // Tool: Get deals
            if (request.params.name === 'get_deals') {
                try {
                    const limit = request.params.arguments?.limit || 100;
                    const response = await this.hubspotClient.crm.deals.getAll(limit);
                    return {
                        content: [{
                            type: 'text',
                            text: JSON.stringify(response.results, null, 2)
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
            
            // Tool: Analyze pipeline
            if (request.params.name === 'analyze_pipeline') {
                try {
                    const deals = await this.hubspotClient.crm.deals.getAll(1000);
                    
                    // Calculate pipeline metrics
                    const pipelineStats = {
                        total_deals: deals.results.length,
                        total_value: deals.results.reduce((sum, deal) => {
                            return sum + (parseFloat(deal.properties.amount) || 0);
                        }, 0),
                        by_stage: {},
                        won_deals: deals.results.filter(d => d.properties.dealstage === 'closedwon').length,
                        lost_deals: deals.results.filter(d => d.properties.dealstage === 'closedlost').length
                    };
                    
                    // Group by stage
                    deals.results.forEach(deal => {
                        const stage = deal.properties.dealstage || 'unknown';
                        if (!pipelineStats.by_stage[stage]) {
                            pipelineStats.by_stage[stage] = {
                                count: 0,
                                value: 0
                            };
                        }
                        pipelineStats.by_stage[stage].count++;
                        pipelineStats.by_stage[stage].value += parseFloat(deal.properties.amount) || 0;
                    });
                    
                    return {
                        content: [{
                            type: 'text',
                            text: JSON.stringify(pipelineStats, null, 2)
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
    
    setupResources() {
        // Resource: HubSpot API documentation
        this.server.setRequestHandler('resources/list', async () => {
            return {
                resources: [
                    {
                        uri: 'hubspot://api/docs',
                        mimeType: 'text/markdown',
                        name: 'HubSpot API Documentation',
                        description: 'Official HubSpot API documentation'
                    },
                    {
                        uri: 'hubspot://crm/schema',
                        mimeType: 'application/json',
                        name: 'CRM Schema',
                        description: 'HubSpot CRM object schema and properties'
                    }
                ]
            };
        });
    }
    
    async run() {
        const transport = new StdioServerTransport();
        await this.server.connect(transport);
        console.error('HubSpot MCP server running on stdio');
    }
}

// Start server
const server = new HubSpotMCPServer();
server.run().catch(console.error);
