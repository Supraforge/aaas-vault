#!/usr/bin/env node

const { Server } = require('@modelcontextprotocol/sdk/server');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio');
const PinterestAPI = require('./pinterest_api.js');

class PinterestMCPServer {
    constructor() {
        this.server = new Server(
            {
                name: 'pinterest-mcp',
                version: '1.0.0'
            },
            {
                capabilities: {
                    tools: {}
                }
            }
        );
        
        this.api = new PinterestAPI();
        this.setupTools();
    }
    
    setupTools() {
        // Tool: Create Pinterest pin
        this.server.setRequestHandler('tools/call', async (request) => {
            const { name, arguments: args } = request.params;
            
            switch (name) {
                case 'pinterest_create_pin':
                    try {
                        const result = await this.api.createPin(
                            args.board_id,
                            args.image_url,
                            args.description,
                            args.title
                        );
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
                    
                case 'pinterest_get_analytics':
                    try {
                        const result = await this.api.getAnalytics(
                            args.entity_type,
                            args.entity_id,
                            args.metric_types
                        );
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
                    
                case 'pinterest_search_pins':
                    try {
                        // Note: Pinterest search API may require additional setup
                        return {
                            content: [{
                                type: 'text',
                                text: 'Search functionality requires Pinterest Business account'
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
                    
                default:
                    return {
                        content: [{
                            type: 'text',
                            text: `Unknown tool: ${name}`
                        }],
                        isError: true
                    };
            }
        });
    }
    
    async run() {
        const transport = new StdioServerTransport();
        await this.server.connect(transport);
        console.error('Pinterest MCP server running on stdio');
    }
}

if (require.main === module) {
    const server = new PinterestMCPServer();
    server.run().catch(console.error);
}

module.exports = PinterestMCPServer;
