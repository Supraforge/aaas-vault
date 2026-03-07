#!/usr/bin/env node

// Simple HubSpot MCP query example
// This script demonstrates how to query HubSpot data via MCP

const fs = require('fs');
const path = require('path');

// Load environment variables
require('dotenv').config({ path: path.join(__dirname, '..', '.env') });

console.log('HubSpot MCP Query Example');
console.log('=========================');

// Check for required environment variables
const requiredVars = ['HUBSPOT_ACCESS_TOKEN', 'HUBSPOT_PORTAL_ID'];
const missingVars = requiredVars.filter(varName => !process.env[varName]);

if (missingVars.length > 0) {
    console.error(`❌ Missing required environment variables: ${missingVars.join(', ')}`);
    console.error('Please add them to your .env file');
    process.exit(1);
}

console.log(`✅ HubSpot Portal ID: ${process.env.HUBSPOT_PORTAL_ID}`);
console.log('✅ Environment variables loaded successfully');

// Example MCP client setup (simplified)
console.log('\n📊 Example MCP Queries:');
console.log('1. Get recent contacts');
console.log('2. Analyze deal pipeline');
console.log('3. Export company data');
console.log('4. Marketing analytics');

console.log('\n🔗 To use with actual MCP server:');
console.log('1. Install HubSpot MCP server: npm install -g @hubspot/mcp-server');
console.log('2. Start server: hubspot-mcp-server');
console.log('3. Connect using MCP client with your access token');

// Generate sample output
const sampleData = {
    query: 'recent_contacts',
    timestamp: new Date().toISOString(),
    portal_id: process.env.HUBSPOT_PORTAL_ID,
    sample_contacts: [
        { id: 'contact_001', email: 'sample1@example.com', created_at: '2024-01-15' },
        { id: 'contact_002', email: 'sample2@example.com', created_at: '2024-01-16' },
        { id: 'contact_003', email: 'sample3@example.com', created_at: '2024-01-17' }
    ],
    note: 'This is sample data. Connect to actual HubSpot MCP server for real data.'
};

console.log('\n📋 Sample Query Result:');
console.log(JSON.stringify(sampleData, null, 2));

// Save sample output to file
const outputDir = process.env.EXPORT_DIR || './exports';
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

const outputFile = path.join(outputDir, `hubspot_sample_${Date.now()}.json`);
fs.writeFileSync(outputFile, JSON.stringify(sampleData, null, 2));
console.log(`\n💾 Sample data saved to: ${outputFile}`);
