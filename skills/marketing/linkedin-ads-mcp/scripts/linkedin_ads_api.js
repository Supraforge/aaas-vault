#!/usr/bin/env node
/**
 * LinkedIn Ads API - Node.js implementation
 */

const axios = require('axios');
const fs = require('fs');
const path = require('path');
require('dotenv').config();

class LinkedInAdsAPI {
    constructor() {
        this.clientId = process.env.LINKEDIN_CLIENT_ID;
        this.clientSecret = process.env.LINKEDIN_CLIENT_SECRET;
        this.accessToken = process.env.LINKEDIN_ACCESS_TOKEN;
        this.adAccountId = process.env.LINKEDIN_AD_ACCOUNT_ID;
        this.baseURL = 'https://api.linkedin.com/v2';
        
        this.validateCredentials();
        
        this.axiosInstance = axios.create({
            baseURL: this.baseURL,
            headers: {
                'Authorization': `Bearer ${this.accessToken}`,
                'Content-Type': 'application/json',
                'X-Restli-Protocol-Version': '2.0.0'
            }
        });
    }
    
    validateCredentials() {
        const required = ['LINKEDIN_CLIENT_ID', 'LINKEDIN_CLIENT_SECRET', 'LINKEDIN_ACCESS_TOKEN', 'LINKEDIN_AD_ACCOUNT_ID'];
        const missing = required.filter(key => !process.env[key]);
        
        if (missing.length > 0) {
            throw new Error(`Missing LinkedIn API credentials: ${missing.join(', ')}`);
        }
    }
    
    async makeRequest(method, endpoint, data = null) {
        try {
            const config = {
                method,
                url: endpoint
            };
            
            if (data && (method === 'POST' || method === 'PUT')) {
                config.data = data;
            }
            
            const response = await this.axiosInstance.request(config);
            return response.data;
        } catch (error) {
            console.error('API Request failed:', error.message);
            if (error.response) {
                console.error('Response:', error.response.data);
            }
            throw error;
        }
    }
    
    async refreshToken() {
        const refreshToken = process.env.LINKEDIN_REFRESH_TOKEN;
        if (!refreshToken) {
            throw new Error('Refresh token not available');
        }
        
        const tokenURL = 'https://www.linkedin.com/oauth/v2/accessToken';
        const params = new URLSearchParams({
            grant_type: 'refresh_token',
            refresh_token: refreshToken,
            client_id: this.clientId,
            client_secret: this.clientSecret
        });
        
        try {
            const response = await axios.post(tokenURL, params.toString(), {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            });
            
            // Update environment variables
            process.env.LINKEDIN_ACCESS_TOKEN = response.data.access_token;
            this.accessToken = response.data.access_token;
            
            if (response.data.refresh_token) {
                process.env.LINKEDIN_REFRESH_TOKEN = response.data.refresh_token;
            }
            
            // Update axios instance headers
            this.axiosInstance.defaults.headers['Authorization'] = `Bearer ${this.accessToken}`;
            
            return response.data.access_token;
        } catch (error) {
            console.error('Token refresh failed:', error.message);
            throw error;
        }
    }
    
    async getCampaigns(status = null) {
        let endpoint = `/adCampaignsV2?q=account&account=urn:li:sponsoredAccount:${this.adAccountId}`;
        if (status) {
            endpoint += `&status=${status}`;
        }
        
        return this.makeRequest('GET', endpoint);
    }
    
    async createCampaign(name, dailyBudget, objective = 'WEBSITE_VISITS') {
        const campaignData = {
            account: `urn:li:sponsoredAccount:${this.adAccountId}`,
            name,
            objectiveType: objective,
            status: 'ACTIVE',
            dailyBudget: {
                amount: dailyBudget,
                currencyCode: 'USD'
            }
        };
        
        return this.makeRequest('POST', '/adCampaignsV2', campaignData);
    }
    
    async getCampaignAnalytics(campaignId, dateRange = 'LAST_30_DAYS') {
        const endpoint = `/adAnalyticsV2?q=analytics&pivot=CAMPAIGN&dateRange=${dateRange}&campaigns[0]=urn:li:sponsoredCampaign:${campaignId}`;
        return this.makeRequest('GET', endpoint);
    }
    
    async getAccountAnalytics(dateRange = 'LAST_30_DAYS') {
        const endpoint = `/adAnalyticsV2?q=analytics&pivot=ACCOUNT&dateRange=${dateRange}&accounts[0]=urn:li:sponsoredAccount:${this.adAccountId}`;
        return this.makeRequest('GET', endpoint);
    }
}

// MCP Server integration
class LinkedInAdsMCPServer {
    constructor() {
        this.api = new LinkedInAdsAPI();
    }
    
    async handleRequest(method, params) {
        switch (method) {
            case 'get_campaigns':
                return await this.api.getCampaigns(params.status);
            case 'create_campaign':
                return await this.api.createCampaign(params.name, params.budget, params.objective);
            case 'get_campaign_analytics':
                return await this.api.getCampaignAnalytics(params.campaignId, params.dateRange);
            case 'get_account_analytics':
                return await this.api.getAccountAnalytics(params.dateRange);
            case 'refresh_token':
                return await this.api.refreshToken();
            default:
                throw new Error(`Unknown method: ${method}`);
        }
    }
}

// Command-line interface
if (require.main === module) {
    const args = process.argv.slice(2);
    const api = new LinkedInAdsAPI();
    
    if (args.includes('--test')) {
        api.getCampaigns()
            .then(data => {
                console.log('✅ LinkedIn API connection successful');
                console.log(`Found ${data.elements?.length || 0} campaigns`);
            })
            .catch(error => {
                console.error('❌ LinkedIn API connection failed:', error.message);
                process.exit(1);
            });
    } else if (args.includes('--list-campaigns')) {
        api.getCampaigns()
            .then(data => {
                console.log('Campaigns:');
                data.elements?.forEach(campaign => {
                    console.log(`- ${campaign.name} (ID: ${campaign.id}, Status: ${campaign.status})`);
                });
            })
            .catch(console.error);
    } else {
        console.log('Usage:');
        console.log('  node linkedin_ads_api.js --test');
        console.log('  node linkedin_ads_api.js --list-campaigns');
    }
}

module.exports = { LinkedInAdsAPI, LinkedInAdsMCPServer };
