#!/usr/bin/env node

// Google Analytics MCP Query Script
// Connects to Google Analytics MCP server and retrieves analytics data

const { Client } = require('@modelcontextprotocol/sdk');
const { writeFileSync } = require('fs');
const { join } = require('path');
require('dotenv').config();

async function main() {
    console.log('🔍 Google Analytics MCP Query Tool');
    console.log('====================================');
    
    // Configuration
    const config = {
        host: process.env.MCP_SERVER_HOST || 'localhost',
        port: process.env.MCP_SERVER_PORT || 3001,
        propertyId: process.env.GA_PROPERTY_ID || 'properties/YOUR_PROPERTY_ID',
        dateRange: process.env.DEFAULT_DATE_RANGE || '7daysAgo',
        endDate: process.env.DEFAULT_END_DATE || 'today',
        metrics: process.env.DEFAULT_METRICS || 'sessions,users,pageviews',
        dimensions: process.env.DEFAULT_DIMENSIONS || 'date,country'
    };
    
    console.log(`📊 Configuration:`);
    console.log(`   Property: ${config.propertyId}`);
    console.log(`   Date Range: ${config.dateRange} to ${config.endDate}`);
    console.log(`   Metrics: ${config.metrics}`);
    console.log(`   Dimensions: ${config.dimensions}`);
    
    try {
        // Connect to MCP server
        console.log('\n🔌 Connecting to Google Analytics MCP server...');
        const client = new Client({
            name: 'google-analytics-query-tool',
            version: '1.0.0'
        });
        
        await client.connect({
            host: config.host,
            port: config.port
        });
        
        console.log('✅ Connected to MCP server');
        
        // Query analytics data
        console.log('\n📈 Querying analytics data...');
        const query = {
            method: 'analytics.query',
            params: {
                propertyId: config.propertyId,
                dateRanges: [{
                    startDate: config.dateRange,
                    endDate: config.endDate
                }],
                metrics: config.metrics.split(',').map(m => ({ name: m.trim() })),
                dimensions: config.dimensions.split(',').map(d => ({ name: d.trim() })),
                limit: 1000
            }
        };
        
        const response = await client.request(query);
        
        if (response.result && response.result.rows) {
            const data = response.result;
            console.log(`✅ Retrieved ${data.rows.length} rows of data`);
            console.log(`📊 Total sessions: ${data.totals[0]?.values[0] || 'N/A'}`);
            console.log(`👥 Total users: ${data.totals[0]?.values[1] || 'N/A'}`);
            
            // Save to JSON
            const jsonPath = join(process.cwd(), 'exports', `analytics_${Date.now()}.json`);
            writeFileSync(jsonPath, JSON.stringify(data, null, 2));
            console.log(`💾 Data saved to: ${jsonPath}`);
            
            // Generate CSV
            if (data.rows.length > 0) {
                const csvPath = join(process.cwd(), 'exports', `analytics_${Date.now()}.csv`);
                const csvHeader = [...data.dimensionHeaders.map(h => h.name), ...data.metricHeaders.map(h => h.name)].join(',');
                const csvRows = data.rows.map(row => 
                    [...row.dimensionValues.map(v => v.value), ...row.metricValues.map(v => v.value)].join(',')
                );
                const csvContent = [csvHeader, ...csvRows].join('\n');
                writeFileSync(csvPath, csvContent);
                console.log(`📄 CSV saved to: ${csvPath}`);
            }
            
            // Display sample data
            console.log('\n📋 Sample Data (first 3 rows):');
            data.rows.slice(0, 3).forEach((row, i) => {
                console.log(`  Row ${i + 1}:`);
                row.dimensionValues.forEach((dim, j) => {
                    console.log(`    ${data.dimensionHeaders[j].name}: ${dim.value}`);
                });
                row.metricValues.forEach((metric, j) => {
                    console.log(`    ${data.metricHeaders[j].name}: ${metric.value}`);
                });
                console.log('');
            });
        } else {
            console.log('⚠️  No data returned from query');
        }
        
        // Disconnect
        await client.disconnect();
        console.log('\n✅ Query completed successfully!');
        
    } catch (error) {
        console.error('❌ Error:', error.message);
        if (error.code === 'ECONNREFUSED') {
            console.log('\n💡 Troubleshooting:');
            console.log('1. Make sure Google Analytics MCP server is running:');
            console.log('   google-analytics-mcp-server');
            console.log('2. Check server host and port in .env file');
            console.log('3. Verify Google OAuth credentials are valid');
        }
        process.exit(1);
    }
}

// Run the script
if (require.main === module) {
    main();
}

module.exports = { main };
