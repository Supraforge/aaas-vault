#!/usr/bin/env node

const axios = require('axios');
require('dotenv').config();

class PinterestAPI {
    constructor() {
        this.accessToken = process.env.PINTEREST_ACCESS_TOKEN;
        this.apiVersion = process.env.PINTEREST_API_VERSION || 'v5';
        this.baseURL = `https://api.pinterest.com/${this.apiVersion}`;
        
        if (!this.accessToken) {
            throw new Error('PINTEREST_ACCESS_TOKEN not found in .env');
        }
        
        this.client = axios.create({
            baseURL: this.baseURL,
            headers: {
                'Authorization': `Bearer ${this.accessToken}`,
                'Content-Type': 'application/json'
            }
        });
    }
    
    async testConnection() {
        try {
            const response = await this.client.get('/user_account');
            console.log('✅ Pinterest API connection successful');
            console.log(`User: ${response.data.username}`);
            console.log(`Account type: ${response.data.account_type}`);
            return response.data;
        } catch (error) {
            console.error('❌ Pinterest API connection failed:', error.message);
            if (error.response) {
                console.error('Status:', error.response.status);
                console.error('Data:', error.response.data);
            }
            throw error;
        }
    }
    
    async createPin(boardId, imageUrl, description, title = '') {
        try {
            const pinData = {
                board_id: boardId,
                media_source: {
                    source_type: 'image_url',
                    url: imageUrl
                },
                description: description,
                title: title
            };
            
            const response = await this.client.post('/pins', pinData);
            console.log('✅ Pin created successfully');
            console.log(`Pin ID: ${response.data.id}`);
            console.log(`URL: ${response.data.url}`);
            return response.data;
        } catch (error) {
            console.error('❌ Failed to create pin:', error.message);
            throw error;
        }
    }
    
    async getBoardPins(boardId, limit = 25) {
        try {
            const response = await this.client.get(`/boards/${boardId}/pins`, {
                params: { limit }
            });
            console.log(`📌 Found ${response.data.items.length} pins in board`);
            return response.data.items;
        } catch (error) {
            console.error('❌ Failed to get board pins:', error.message);
            throw error;
        }
    }
    
    async getAnalytics(entityType, entityId, metricTypes = ['IMPRESSION', 'SAVE', 'CLICKTHROUGH']) {
        try {
            const params = new URLSearchParams();
            metricTypes.forEach(metric => params.append('metric_types', metric));
            params.append('date', 'LAST_30_DAYS');
            
            const response = await this.client.get(`/${entityType}/${entityId}/analytics`, {
                params: params
            });
            
            console.log(`📊 Analytics for ${entityType} ${entityId}:`);
            response.data.metrics.forEach(metric => {
                console.log(`${metric.name}: ${metric.value}`);
            });
            
            return response.data;
        } catch (error) {
            console.error('❌ Failed to get analytics:', error.message);
            throw error;
        }
    }
}

// Command line interface
if (require.main === module) {
    const api = new PinterestAPI();
    
    const command = process.argv[2];
    
    switch (command) {
        case 'test':
            api.testConnection();
            break;
        case 'create-pin':
            if (process.argv.length < 6) {
                console.log('Usage: node pinterest_api.js create-pin <boardId> <imageUrl> <description> [title]');
                process.exit(1);
            }
            api.createPin(process.argv[3], process.argv[4], process.argv[5], process.argv[6]);
            break;
        case 'get-pins':
            if (process.argv.length < 4) {
                console.log('Usage: node pinterest_api.js get-pins <boardId> [limit]');
                process.exit(1);
            }
            api.getBoardPins(process.argv[3], process.argv[4] || 25);
            break;
        case 'analytics':
            if (process.argv.length < 5) {
                console.log('Usage: node pinterest_api.js analytics <entityType> <entityId>');
                console.log('Example: node pinterest_api.js analytics board 123456789');
                process.exit(1);
            }
            api.getAnalytics(process.argv[3], process.argv[4]);
            break;
        default:
            console.log('Available commands:');
            console.log('  test - Test API connection');
            console.log('  create-pin <boardId> <imageUrl> <description> [title]');
            console.log('  get-pins <boardId> [limit]');
            console.log('  analytics <entityType> <entityId>');
    }
}

module.exports = PinterestAPI;
