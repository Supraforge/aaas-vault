#!/usr/bin/env node

const PinterestAPI = require('./pinterest_api.js');
const fs = require('fs');
const path = require('path');

class PinterestAnalytics {
    constructor() {
        this.api = new PinterestAPI();
    }
    
    async generateReport(boardId, outputFormat = 'csv') {
        try {
            console.log(`📊 Generating analytics report for board ${boardId}...`);
            
            // Get board pins
            const pins = await this.api.getBoardPins(boardId, 100);
            
            // Get analytics for each pin
            const reportData = [];
            
            for (const pin of pins) {
                try {
                    const analytics = await this.api.getAnalytics('pin', pin.id);
                    
                    reportData.push({
                        pin_id: pin.id,
                        pin_url: pin.url,
                        description: pin.description,
                        created_at: pin.created_at,
                        impressions: this.getMetricValue(analytics.metrics, 'IMPRESSION'),
                        saves: this.getMetricValue(analytics.metrics, 'SAVE'),
                        clicks: this.getMetricValue(analytics.metrics, 'CLICKTHROUGH'),
                        engagement_rate: this.calculateEngagementRate(analytics.metrics)
                    });
                    
                    console.log(`  Processed pin: ${pin.id}`);
                } catch (error) {
                    console.log(`  Skipped pin ${pin.id}: ${error.message}`);
                }
            }
            
            // Generate output
            const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
            const filename = `pinterest_report_${boardId}_${timestamp}.${outputFormat}`;
            
            if (outputFormat === 'csv') {
                this.generateCSV(reportData, filename);
            } else if (outputFormat === 'json') {
                this.generateJSON(reportData, filename);
            }
            
            console.log(`✅ Report generated: ${filename}`);
            console.log(`📈 Total pins analyzed: ${reportData.length}`);
            
            return { filename, data: reportData };
            
        } catch (error) {
            console.error('❌ Failed to generate report:', error.message);
            throw error;
        }
    }
    
    getMetricValue(metrics, metricName) {
        const metric = metrics.find(m => m.name === metricName);
        return metric ? metric.value : 0;
    }
    
    calculateEngagementRate(metrics) {
        const impressions = this.getMetricValue(metrics, 'IMPRESSION');
        const saves = this.getMetricValue(metrics, 'SAVE');
        const clicks = this.getMetricValue(metrics, 'CLICKTHROUGH');
        
        if (impressions === 0) return 0;
        return ((saves + clicks) / impressions * 100).toFixed(2);
    }
    
    generateCSV(data, filename) {
        const headers = ['pin_id', 'pin_url', 'description', 'created_at', 'impressions', 'saves', 'clicks', 'engagement_rate'];
        const csvRows = [];
        
        // Add headers
        csvRows.push(headers.join(','));
        
        // Add data rows
        for (const row of data) {
            const values = headers.map(header => {
                const value = row[header];
                // Escape quotes and wrap in quotes if contains comma
                const escaped = String(value).replace(/"/g, '\"');
                return escaped.includes(',') ? `"${escaped}"` : escaped;
            });
            csvRows.push(values.join(','));
        }
        
        fs.writeFileSync(filename, csvRows.join('\n'));
    }
    
    generateJSON(data, filename) {
        fs.writeFileSync(filename, JSON.stringify(data, null, 2));
    }
}

// Command line interface
if (require.main === module) {
    const analytics = new PinterestAnalytics();
    
    const command = process.argv[2];
    
    if (command === 'report' && process.argv[3]) {
        const boardId = process.argv[3];
        const format = process.argv[4] || 'csv';
        analytics.generateReport(boardId, format);
    } else {
        console.log('Usage: node analytics.js report <boardId> [format]');
        console.log('Formats: csv, json');
        console.log('Example: node analytics.js report 123456789 json');
    }
}

module.exports = PinterestAnalytics;
