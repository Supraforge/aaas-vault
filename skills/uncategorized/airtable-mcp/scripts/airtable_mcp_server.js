const { Server } = require('@modelcontextprotocol/sdk');
const Airtable = require('airtable');
require('dotenv').config();

// Initialize Airtable client
const airtable = new Airtable({ apiKey: process.env.AIRTABLE_TOKEN });
const base = airtable.base(process.env.AIRTABLE_BASE_ID);

// Create MCP server
const server = new Server(
    {
        name: 'airtable-mcp',
        version: '1.0.0',
    },
    {
        capabilities: {
            resources: {},
            tools: {},
        },
    }
);

// Resource: List tables in base
server.setRequestHandler('resources/list', async () => {
    try {
        const tables = await base._base.getTables();
        return {
            resources: tables.map(table => ({
                uri: `airtable://${process.env.AIRTABLE_BASE_ID}/${table.id}`,
                name: table.name,
                description: `Airtable table: ${table.name}`,
                mimeType: 'application/json',
            })),
        };
    } catch (error) {
        throw new Error(`Failed to list tables: ${error.message}`);
    }
});

// Resource: Read table data
server.setRequestHandler('resources/read', async (request) => {
    const { uri } = request.params;
    const [, baseId, tableId] = uri.match(/airtable:\/\/([^\/]+)\/([^\/]+)/) || [];
    
    if (!baseId || !tableId) {
        throw new Error('Invalid Airtable URI format');
    }
    
    try {
        const table = base.table(tableId);
        const records = await table.select().all();
        
        return {
            contents: [{
                uri,
                mimeType: 'application/json',
                text: JSON.stringify({
                    baseId,
                    tableId,
                    records: records.map(record => ({
                        id: record.id,
                        fields: record.fields,
                        createdTime: record._rawJson.createdTime,
                    })),
                    total: records.length,
                }, null, 2),
            }],
        };
    } catch (error) {
        throw new Error(`Failed to read table: ${error.message}`);
    }
});

// Tool: Create record
server.setRequestHandler('tools/call', async (request) => {
    const { name, arguments: args } = request.params;
    
    switch (name) {
        case 'create_record': {
            const { tableName, fields } = args;
            try {
                const table = base.table(tableName);
                const record = await table.create(fields);
                
                return {
                    content: [{
                        type: 'text',
                        text: JSON.stringify({
                            success: true,
                            recordId: record.id,
                            fields: record.fields,
                        }, null, 2),
                    }],
                };
            } catch (error) {
                return {
                    content: [{
                        type: 'text',
                        text: JSON.stringify({
                            success: false,
                            error: error.message,
                        }, null, 2),
                    }],
                };
            }
        }
        
        case 'update_record': {
            const { tableName, recordId, fields } = args;
            try {
                const table = base.table(tableName);
                const record = await table.update(recordId, fields);
                
                return {
                    content: [{
                        type: 'text',
                        text: JSON.stringify({
                            success: true,
                            recordId: record.id,
                            updatedFields: record.fields,
                        }, null, 2),
                    }],
                };
            } catch (error) {
                return {
                    content: [{
                        type: 'text',
                        text: JSON.stringify({
                            success: false,
                            error: error.message,
                        }, null, 2),
                    }],
                };
            }
        }
        
        case 'delete_record': {
            const { tableName, recordId } = args;
            try {
                const table = base.table(tableName);
                await table.destroy(recordId);
                
                return {
                    content: [{
                        type: 'text',
                        text: JSON.stringify({
                            success: true,
                            message: `Record ${recordId} deleted successfully`,
                        }, null, 2),
                    }],
                };
            } catch (error) {
                return {
                    content: [{
                        type: 'text',
                        text: JSON.stringify({
                            success: false,
                            error: error.message,
                        }, null, 2),
                    }],
                };
            }
        }
        
        case 'search_records': {
            const { tableName, formula } = args;
            try {
                const table = base.table(tableName);
                const records = await table.select({
                    filterByFormula: formula,
                }).all();
                
                return {
                    content: [{
                        type: 'text',
                        text: JSON.stringify({
                            success: true,
                            records: records.map(record => ({
                                id: record.id,
                                fields: record.fields,
                            })),
                            count: records.length,
                        }, null, 2),
                    }],
                };
            } catch (error) {
                return {
                    content: [{
                        type: 'text',
                        text: JSON.stringify({
                            success: false,
                            error: error.message,
                        }, null, 2),
                    }],
                };
            }
        }
        
        default:
            throw new Error(`Unknown tool: ${name}`);
    }
});

// Start server
server.start().catch(error => {
    console.error('Failed to start Airtable MCP server:', error);
    process.exit(1);
});

console.log('🚀 Airtable MCP server started on stdio');
