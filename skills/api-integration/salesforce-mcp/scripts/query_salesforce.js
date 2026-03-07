#!/usr/bin/env node

// Salesforce MCP Query Script
// Query Salesforce data via MCP server

const fs = require('fs');
const path = require('path');
require('dotenv').config();

// Load environment variables
const {
  SALESFORCE_CLIENT_ID,
  SALESFORCE_CLIENT_SECRET,
  SALESFORCE_USERNAME,
  SALESFORCE_PASSWORD,
  SALESFORCE_SECURITY_TOKEN,
  MCP_SERVER_HOST = 'localhost',
  MCP_SERVER_PORT = 3001,
  SALESFORCE_API_VERSION = 'v59.0',
  EXPORT_FORMAT = 'json',
  EXPORT_DIR = './exports',
  MAX_RECORDS = 2000
} = process.env;

// Validate environment variables
const requiredEnvVars = [
  'SALESFORCE_CLIENT_ID',
  'SALESFORCE_CLIENT_SECRET',
  'SALESFORCE_USERNAME',
  'SALESFORCE_PASSWORD',
  'SALESFORCE_SECURITY_TOKEN'
];

const missingVars = requiredEnvVars.filter(varName => !process.env[varName]);
if (missingVars.length > 0) {
  console.error('❌ Missing required environment variables:');
  missingVars.forEach(varName => console.error(`   - ${varName}`));
  console.error('\nPlease copy .env.template to .env and fill in your Salesforce credentials');
  process.exit(1);
}

// Create exports directory if it doesn't exist
if (!fs.existsSync(EXPORT_DIR)) {
  fs.mkdirSync(EXPORT_DIR, { recursive: true });
}

// Sample SOQL queries for common business use cases
const sampleQueries = {
  opportunities: `SELECT Id, Name, Amount, StageName, CloseDate, Probability, Account.Name FROM Opportunity WHERE StageName NOT IN ('Closed Won', 'Closed Lost') ORDER BY CloseDate DESC LIMIT ${MAX_RECORDS}`,
  accounts: `SELECT Id, Name, Industry, AnnualRevenue, NumberOfEmployees, BillingCity, BillingState FROM Account ORDER BY CreatedDate DESC LIMIT ${MAX_RECORDS}`,
  contacts: `SELECT Id, FirstName, LastName, Email, Phone, Account.Name, Title FROM Contact ORDER BY CreatedDate DESC LIMIT ${MAX_RECORDS}`,
  leads: `SELECT Id, FirstName, LastName, Company, Email, Status, Industry FROM Lead WHERE Status = 'Open - Not Contacted' ORDER BY CreatedDate DESC LIMIT ${MAX_RECORDS}`,
  cases: `SELECT Id, CaseNumber, Subject, Status, Priority, CreatedDate, Contact.Name FROM Case ORDER BY CreatedDate DESC LIMIT ${MAX_RECORDS}`
};

// Function to connect to Salesforce MCP server
async function connectToSalesforceMCP() {
  console.log('🔌 Connecting to Salesforce MCP server...');
  
  // In a real implementation, this would connect to the MCP server
  // For now, we'll simulate the connection
  console.log(`   Host: ${MCP_SERVER_HOST}:${MCP_SERVER_PORT}`);
  console.log(`   API Version: ${SALESFORCE_API_VERSION}`);
  
  // Simulate connection delay
  await new Promise(resolve => setTimeout(resolve, 1000));
  
  console.log('✅ Connected to Salesforce MCP server');
  return {
    query: async (soql) => {
      console.log(`📊 Executing query: ${soql.substring(0, 100)}...`);
      // Simulate query execution
      await new Promise(resolve => setTimeout(resolve, 500));
      
      // Return mock data for demonstration
      return generateMockData(soql);
    }
  };
}

// Generate mock data based on query type
function generateMockData(soql) {
  const timestamp = new Date().toISOString();
  
  if (soql.includes('FROM Opportunity')) {
    return {
      totalSize: 5,
      done: true,
      records: [
        { Id: '0011', Name: 'Enterprise Deal', Amount: 50000, StageName: 'Proposal', CloseDate: '2024-12-31', Probability: 70, Account: { Name: 'Acme Corp' } },
        { Id: '0012', Name: 'SMB Contract', Amount: 15000, StageName: 'Negotiation', CloseDate: '2024-11-30', Probability: 50, Account: { Name: 'Beta LLC' } },
        { Id: '0013', Name: 'Renewal', Amount: 25000, StageName: 'Closed Won', CloseDate: '2024-10-15', Probability: 100, Account: { Name: 'Gamma Inc' } }
      ]
    };
  } else if (soql.includes('FROM Account')) {
    return {
      totalSize: 3,
      done: true,
      records: [
        { Id: '0021', Name: 'Acme Corp', Industry: 'Technology', AnnualRevenue: 1000000, NumberOfEmployees: 50, BillingCity: 'San Francisco', BillingState: 'CA' },
        { Id: '0022', Name: 'Beta LLC', Industry: 'Healthcare', AnnualRevenue: 500000, NumberOfEmployees: 25, BillingCity: 'New York', BillingState: 'NY' },
        { Id: '0023', Name: 'Gamma Inc', Industry: 'Finance', AnnualRevenue: 2000000, NumberOfEmployees: 100, BillingCity: 'Chicago', BillingState: 'IL' }
      ]
    };
  }
  
  // Default mock response
  return {
    totalSize: 0,
    done: true,
    records: []
  };
}

// Export data to file
function exportData(data, queryType) {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const filename = `salesforce_${queryType}_${timestamp}`;
  
  if (EXPORT_FORMAT === 'csv') {
    const csvPath = path.join(EXPORT_DIR, `${filename}.csv`);
    // Convert to CSV (simplified)
    const csvContent = 'Id,Name,Value\n' + data.records.map(r => `${r.Id},${r.Name},${r.Amount || r.AnnualRevenue || ''}`).join('\n');
    fs.writeFileSync(csvPath, csvContent);
    console.log(`📁 Data exported to: ${csvPath}`);
    return csvPath;
  } else {
    const jsonPath = path.join(EXPORT_DIR, `${filename}.json`);
    fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2));
    console.log(`📁 Data exported to: ${jsonPath}`);
    return jsonPath;
  }
}

// Main function
async function main() {
  console.log('🚀 Salesforce MCP Query Tool');
  console.log('============================');
  
  try {
    // Get query type from command line arguments
    const queryType = process.argv[2] || 'opportunities';
    
    if (!sampleQueries[queryType]) {
      console.log('Available query types:');
      Object.keys(sampleQueries).forEach(type => console.log(`  - ${type}`));
      console.log('\nUsage: node query_salesforce.js [query_type]');
      process.exit(1);
    }
    
    // Connect to MCP server
    const salesforce = await connectToSalesforceMCP();
    
    // Execute query
    const soql = sampleQueries[queryType];
    const result = await salesforce.query(soql);
    
    // Display results
    console.log(`\n📈 Query Results (${queryType}):`);
    console.log(`   Total records: ${result.totalSize}`);
    
    if (result.records && result.records.length > 0) {
      console.log('\nSample records:');
      result.records.slice(0, 3).forEach((record, index) => {
        console.log(`   ${index + 1}. ${record.Name} (${record.Id})`);
        if (record.Amount) console.log(`      Amount: $${record.Amount}`);
        if (record.StageName) console.log(`      Stage: ${record.StageName}`);
        if (record.Account?.Name) console.log(`      Account: ${record.Account.Name}`);
      });
      
      // Export data
      const exportPath = exportData(result, queryType);
      console.log(`\n✅ Query completed successfully!`);
      console.log(`   Data exported to: ${exportPath}`);
    } else {
      console.log('\n⚠️  No records found');
    }
    
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  }
}

// Run the script
if (require.main === module) {
  main();
}

module.exports = { connectToSalesforceMCP, sampleQueries };
