// Salesforce MCP Server
const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
const { Salesforce } = require('jsforce');
require('dotenv').config();

const server = new Server(
  {
    name: 'salesforce-mcp',
    version: '1.0.0',
  },
  {
    capabilities: {
      resources: {},
      tools: {},
    },
  }
);

// Initialize Salesforce connection
let sfConnection = null;

async function connectToSalesforce() {
  if (sfConnection) return sfConnection;
  
  sfConnection = new Salesforce({
    clientId: process.env.SALESFORCE_CLIENT_ID,
    clientSecret: process.env.SALESFORCE_CLIENT_SECRET,
    redirectUri: 'http://localhost:3000/oauth/callback',
  });
  
  try {
    await sfConnection.login(
      process.env.SALESFORCE_USERNAME,
      process.env.SALESFORCE_PASSWORD
    );
    console.error('✅ Connected to Salesforce');
    return sfConnection;
  } catch (error) {
    console.error('❌ Salesforce connection failed:', error.message);
    throw error;
  }
}

// Tool: Get Sales Pipeline
server.setRequestHandler('tools/call', async (request) => {
  if (request.params.name === 'get_sales_pipeline') {
    try {
      const sf = await connectToSalesforce();
      const result = await sf.query(
        `SELECT Id, Name, StageName, Amount, CloseDate, Probability,
                Account.Name, Owner.Name
         FROM Opportunity
         WHERE IsClosed = false
         ORDER BY CloseDate ASC`
      );
      
      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              total_opportunities: result.totalSize,
              opportunities: result.records,
              total_pipeline_value: result.records.reduce((sum, opp) => sum + (opp.Amount || 0), 0)
            }, null, 2)
          }
        ]
      };
    } catch (error) {
      return {
        content: [
          {
            type: 'text',
            text: `Error: ${error.message}`
          }
        ],
        isError: true
      };
    }
  }
  
  // Tool: Create Lead
  if (request.params.name === 'create_lead') {
    const args = request.params.arguments || {};
    
    try {
      const sf = await connectToSalesforce();
      const result = await sf.sobject('Lead').create({
        FirstName: args.firstName || '',
        LastName: args.lastName || '',
        Company: args.company || 'Unknown Company',
        Email: args.email || '',
        Phone: args.phone || '',
        LeadSource: args.leadSource || 'Web',
        Status: 'New',
        Description: args.description || ''
      });
      
      return {
        content: [
          {
            type: 'text',
            text: `Lead created successfully: ${result.id}`
          }
        ]
      };
    } catch (error) {
      return {
        content: [
          {
            type: 'text',
            text: `Error creating lead: ${error.message}`
          }
        ],
        isError: true
      };
    }
  }
  
  // Tool: Update Opportunity
  if (request.params.name === 'update_opportunity') {
    const args = request.params.arguments || {};
    
    try {
      const sf = await connectToSalesforce();
      const result = await sf.sobject('Opportunity').update({
        Id: args.opportunityId,
        StageName: args.stageName,
        Amount: args.amount,
        CloseDate: args.closeDate,
        Probability: args.probability,
        Description: args.description || ''
      });
      
      return {
        content: [
          {
            type: 'text',
            text: `Opportunity updated successfully: ${args.opportunityId}`
          }
        ]
      };
    } catch (error) {
      return {
        content: [
          {
            type: 'text',
            text: `Error updating opportunity: ${error.message}`
          }
        ],
        isError: true
      };
    }
  }
  
  // Tool: Get Sales Analytics
  if (request.params.name === 'get_sales_analytics') {
    try {
      const sf = await connectToSalesforce();
      
      // Get pipeline
      const pipeline = await sf.query(
        `SELECT StageName, SUM(Amount) totalAmount, COUNT(Id) opportunityCount
         FROM Opportunity
         WHERE IsClosed = false
         GROUP BY StageName`
      );
      
      // Get conversion rate
      const leads = await sf.query(
        `SELECT COUNT(Id) totalLeads,
                SUM(CASE WHEN IsConverted = true THEN 1 ELSE 0 END) convertedLeads
         FROM Lead
         WHERE CreatedDate = LAST_N_DAYS:90`
      );
      
      const conversionRate = leads.records[0].convertedLeads / leads.records[0].totalLeads * 100 || 0;
      
      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              pipeline_by_stage: pipeline.records,
              conversion_rate: conversionRate.toFixed(2),
              total_pipeline_value: pipeline.records.reduce((sum, stage) => sum + (stage.totalAmount || 0), 0),
              timestamp: new Date().toISOString()
            }, null, 2)
          }
        ]
      };
    } catch (error) {
      return {
        content: [
          {
            type: 'text',
            text: `Error: ${error.message}`
          }
        ],
        isError: true
      };
    }
  }
  
  return {
    content: [
      {
        type: 'text',
        text: `Unknown tool: ${request.params.name}`
      }
    ],
    isError: true
  };
});

// Start server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('🚀 Salesforce MCP server running on stdio');
}

main().catch((error) => {
  console.error('Server error:', error);
  process.exit(1);
});
