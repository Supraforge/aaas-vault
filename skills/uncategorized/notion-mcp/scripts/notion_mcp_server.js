const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
const { Client } = require('@notionhq/client');
require('dotenv').config();

class NotionMCPServer {
    constructor() {
        this.server = new Server(
            {
                name: 'notion-mcp',
                version: '1.0.0',
            },
            {
                capabilities: {
                    resources: {},
                    tools: {},
                },
            }
        );
        
        // Initialize Notion client
        const notionToken = process.env.NOTION_API_TOKEN;
        if (!notionToken) {
            console.error('❌ NOTION_API_TOKEN not found in environment variables');
            process.exit(1);
        }
        this.notion = new Client({ auth: notionToken });
        
        this.setupTools();
    }
    
    setupTools() {
        // Tool: Query database
        this.server.setRequestHandler('tools/call', async (request) => {
            if (request.params.name === 'query_database') {
                const { databaseId, filter, sorts } = request.params.arguments;
                try {
                    const response = await this.notion.databases.query({
                        database_id: databaseId,
                        filter: filter ? JSON.parse(filter) : undefined,
                        sorts: sorts ? JSON.parse(sorts) : undefined,
                    });
                    return {
                        content: [{
                            type: 'text',
                            text: JSON.stringify(response, null, 2)
                        }]
                    };
                } catch (error) {
                    return {
                        content: [{
                            type: 'text',
                            text: `Error querying database: ${error.message}`
                        }],
                        isError: true
                    };
                }
            }
            
            // Tool: Create page
            if (request.params.name === 'create_page') {
                const { parentDatabaseId, properties, children } = request.params.arguments;
                try {
                    const response = await this.notion.pages.create({
                        parent: { database_id: parentDatabaseId },
                        properties: properties ? JSON.parse(properties) : {},
                        children: children ? JSON.parse(children) : []
                    });
                    return {
                        content: [{
                            type: 'text',
                            text: JSON.stringify(response, null, 2)
                        }]
                    };
                } catch (error) {
                    return {
                        content: [{
                            type: 'text',
                            text: `Error creating page: ${error.message}`
                        }],
                        isError: true
                    };
                }
            }
            
            // Tool: Update page
            if (request.params.name === 'update_page') {
                const { pageId, properties } = request.params.arguments;
                try {
                    const response = await this.notion.pages.update({
                        page_id: pageId,
                        properties: properties ? JSON.parse(properties) : {}
                    });
                    return {
                        content: [{
                            type: 'text',
                            text: JSON.stringify(response, null, 2)
                        }]
                    };
                } catch (error) {
                    return {
                        content: [{
                            type: 'text',
                            text: `Error updating page: ${error.message}`
                        }],
                        isError: true
                    };
                }
            }
            
            // Tool: Retrieve page
            if (request.params.name === 'retrieve_page') {
                const { pageId } = request.params.arguments;
                try {
                    const response = await this.notion.pages.retrieve({
                        page_id: pageId
                    });
                    return {
                        content: [{
                            type: 'text',
                            text: JSON.stringify(response, null, 2)
                        }]
                    };
                } catch (error) {
                    return {
                        content: [{
                            type: 'text',
                            text: `Error retrieving page: ${error.message}`
                        }],
                        isError: true
                    };
                }
            }
            
            // Tool: Search
            if (request.params.name === 'search') {
                const { query } = request.params.arguments;
                try {
                    const response = await this.notion.search({
                        query: query || '',
                        sort: {
                            direction: 'descending',
                            timestamp: 'last_edited_time'
                        }
                    });
                    return {
                        content: [{
                            type: 'text',
                            text: JSON.stringify(response, null, 2)
                        }]
                    };
                } catch (error) {
                    return {
                        content: [{
                            type: 'text',
                            text: `Error searching: ${error.message}`
                        }],
                        isError: true
                    };
                }
            }
        });
    }
    
    async run() {
        const transport = new StdioServerTransport();
        await this.server.connect(transport);
        console.log('🚀 Notion MCP server running on stdio');
    }
}

// Start server
const server = new NotionMCPServer();
server.run().catch(console.error);
