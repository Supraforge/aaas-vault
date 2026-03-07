#!/usr/bin/env node
"""
Airtable Workflow Automation Script
"""
const Airtable = require('airtable');
require('dotenv').config();

// Initialize Airtable
const airtable = new Airtable({ apiKey: process.env.AIRTABLE_TOKEN });
const base = airtable.base(process.env.AIRTABLE_BASE_ID);

class AirtableWorkflow {
    constructor() {
        this.tables = {
            customers: process.env.AIRTABLE_CUSTOMERS_TABLE || 'Customers',
            leads: process.env.AIRTABLE_LEADS_TABLE || 'Leads',
            products: process.env.AIRTABLE_PRODUCTS_TABLE || 'Products',
            orders: process.env.AIRTABLE_ORDERS_TABLE || 'Orders',
        };
    }
    
    async syncCRMData(sourceTable, targetTable, mapping) {
        console.log(`Syncing data from ${sourceTable} to ${targetTable}...`);
        
        try {
            const sourceRecords = await base(sourceTable).select().all();
            const targetRecords = await base(targetTable).select().all();
            
            const sourceMap = new Map(sourceRecords.map(r => [r.id, r]));
            const targetMap = new Map(targetRecords.map(r => [r.get('source_id'), r]));
            
            let created = 0;
            let updated = 0;
            
            for (const [sourceId, sourceRecord] of sourceMap) {
                const targetRecord = targetMap.get(sourceId);
                const fields = {};
                
                // Map fields according to mapping
                for (const [sourceField, targetField] of Object.entries(mapping)) {
                    fields[targetField] = sourceRecord.get(sourceField);
                }
                
                if (targetRecord) {
                    // Update existing record
                    await base(targetTable).update(targetRecord.id, fields);
                    updated++;
                } else {
                    // Create new record
                    fields.source_id = sourceId;
                    await base(targetTable).create(fields);
                    created++;
                }
            }
            
            console.log(`✅ Sync complete: ${created} created, ${updated} updated`);
            return { created, updated };
            
        } catch (error) {
            console.error(`❌ Sync failed: ${error.message}`);
            throw error;
        }
    }
    
    async generateReport(tableName, filters = {}) {
        console.log(`Generating report for ${tableName}...`);
        
        try {
            let query = base(tableName).select();
            
            // Apply filters
            if (filters.formula) {
                query = query.filterByFormula(filters.formula);
            }
            
            const records = await query.all();
            
            const report = {
                table: tableName,
                totalRecords: records.length,
                timestamp: new Date().toISOString(),
                summary: {},
                records: records.map(r => ({
                    id: r.id,
                    fields: r.fields,
                })),
            };
            
            // Calculate summary statistics
            if (records.length > 0) {
                const numericFields = Object.keys(records[0].fields)
                    .filter(key => typeof records[0].fields[key] === 'number');
                
                for (const field of numericFields) {
                    const values = records.map(r => r.fields[field]).filter(v => v != null);
                    if (values.length > 0) {
                        report.summary[field] = {
                            sum: values.reduce((a, b) => a + b, 0),
                            avg: values.reduce((a, b) => a + b, 0) / values.length,
                            min: Math.min(...values),
                            max: Math.max(...values),
                            count: values.length,
                        };
                    }
                }
            }
            
            console.log(`✅ Report generated: ${records.length} records analyzed`);
            return report;
            
        } catch (error) {
            console.error(`❌ Report generation failed: ${error.message}`);
            throw error;
        }
    }
    
    async automateLeadScoring() {
        console.log('Automating lead scoring...');
        
        try {
            const leads = await base(this.tables.leads).select({
                filterByFormula: '{Status} != "Converted" AND {Status} != "Disqualified"',
            }).all();
            
            let updated = 0;
            
            for (const lead of leads) {
                let score = 0;
                const fields = lead.fields;
                
                // Scoring logic
                if (fields['Email']) score += 10;
                if (fields['Phone']) score += 10;
                if (fields['Company']) score += 5;
                if (fields['Title']) score += 5;
                
                // Engagement scoring
                if (fields['Last Contact']) {
                    const lastContact = new Date(fields['Last Contact']);
                    const daysSince = (new Date() - lastContact) / (1000 * 60 * 60 * 24);
                    if (daysSince < 7) score += 20;
                    else if (daysSince < 30) score += 10;
                }
                
                // Update lead score
                if (fields['Lead Score'] !== score) {
                    await base(this.tables.leads).update(lead.id, {
                        'Lead Score': score,
                        'Score Updated': new Date().toISOString(),
                    });
                    updated++;
                }
            }
            
            console.log(`✅ Lead scoring complete: ${updated} leads updated`);
            return { updated };
            
        } catch (error) {
            console.error(`❌ Lead scoring failed: ${error.message}`);
            throw error;
        }
    }
}

// Command line interface
if (require.main === module) {
    const workflow = new AirtableWorkflow();
    const command = process.argv[2];
    
    switch (command) {
        case 'sync-crm':
            workflow.syncCRMData('Leads', 'Customers', {
                'Name': 'Customer Name',
                'Email': 'Email',
                'Company': 'Company',
                'Status': 'Status',
            }).then(console.log).catch(console.error);
            break;
            
        case 'generate-report':
            const tableName = process.argv[3] || 'Customers';
            workflow.generateReport(tableName).then(report => {
                console.log(JSON.stringify(report, null, 2));
            }).catch(console.error);
            break;
            
        case 'score-leads':
            workflow.automateLeadScoring().then(console.log).catch(console.error);
            break;
            
        default:
            console.log('Available commands:');
            console.log('  sync-crm           - Sync leads to customers');
            console.log('  generate-report [table] - Generate report for table');
            console.log('  score-leads       - Automate lead scoring');
            break;
    }
}

module.exports = AirtableWorkflow;
