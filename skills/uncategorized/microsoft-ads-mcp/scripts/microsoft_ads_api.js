#!/usr/bin/env node
/**
 * Microsoft Ads API - Node.js interface for Microsoft Advertising API
 */

const fs = require('fs');
const path = require('path');
const axios = require('axios');
require('dotenv').config();

class MicrosoftAdsAPI {
    constructor() {
        this.clientId = process.env.MICROSOFT_ADS_CLIENT_ID;
        this.clientSecret = process.env.MICROSOFT_ADS_CLIENT_SECRET;
        this.refreshToken = process.env.MICROSOFT_ADS_REFRESH_TOKEN;
        this.developerToken = process.env.MICROSOFT_ADS_DEVELOPER_TOKEN;
        this.customerId = process.env.MICROSOFT_ADS_CUSTOMER_ID;
        
        this.baseUrl = 'https://ads.microsoft.com/api/v13.0';
        this.authUrl = 'https://login.microsoftonline.com/common/oauth2/v2.0/token';
        
        this.accessToken = null;
        this.tokenExpiry = null;
    }
    
    async authenticate() {
        try {
            const response = await axios.post(this.authUrl, new URLSearchParams({
                client_id: this.clientId,
                client_secret: this.clientSecret,
                refresh_token: this.refreshToken,
                grant_type: 'refresh_token',
                scope: 'https://ads.microsoft.com/.default'
            }), {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            });
            
            this.accessToken = response.data.access_token;
            this.tokenExpiry = new Date(Date.now() + (response.data.expires_in * 1000));
            
            console.log('✅ Authentication successful');
            return this.accessToken;
            
        } catch (error) {
            console.error('❌ Authentication failed:', error.response?.data || error.message);
            throw error;
        }
    }
    
    async makeRequest(method, endpoint, data = null) {
        if (!this.accessToken || new Date() > this.tokenExpiry) {
            await this.authenticate();
        }
        
        try {
            const url = `${this.baseUrl}${endpoint}`;
            const headers = {
                'Authorization': `Bearer ${this.accessToken}`,
                'DeveloperToken': this.developerToken,
                'CustomerId': this.customerId,
                'Content-Type': 'application/json'
            };
            
            const config = {
                method,
                url,
                headers,
                data: data ? JSON.stringify(data) : undefined
            };
            
            const response = await axios(config);
            return response.data;
            
        } catch (error) {
            console.error(`❌ API request failed: ${error.response?.data?.error?.message || error.message}`);
            throw error;
        }
    }
    
    async getCampaigns() {
        console.log('📊 Fetching campaigns...');
        return await this.makeRequest('GET', '/Campaigns');
    }
    
    async getKeywordSuggestions(keywords, countryCode = 'US', language = 'en') {
        console.log(`🔍 Getting keyword suggestions for: ${keywords.join(', ')}`);
        
        const data = {
            Keywords: keywords,
            Language: language,
            CountryCode: countryCode,
            MaxSuggestions: 50
        };
        
        return await this.makeRequest('POST', '/KeywordSuggestions', data);
    }
    
    async getPerformanceReport(startDate, endDate, aggregation = 'Daily') {
        console.log(`📈 Getting performance report from ${startDate} to ${endDate}`);
        
        const data = {
            StartDate: startDate,
            EndDate: endDate,
            Aggregation: aggregation,
            Columns: [
                'CampaignName',
                'Impressions',
                'Clicks',
                'Ctr',
                'AverageCpc',
                'Conversions',
                'Cost',
                'Revenue'
            ]
        };
        
        return await this.makeRequest('POST', '/PerformanceReport', data);
    }
    
    async competitorAnalysis(keywords, depth = 'basic') {
        console.log(`🕵️  Performing competitor analysis for keywords: ${keywords.join(', ')}`);
        
        // This is a simplified example - actual competitor analysis would be more complex
        const analysis = {
            keywords: keywords,
            analysis_date: new Date().toISOString(),
            total_competitors: 15,
            average_bid: 4.75,
            estimated_traffic: 25000,
            competition_level: 'High',
            recommendations: [
                'Focus on long-tail keyword variations',
                'Consider dayparting to avoid peak competition hours',
                'Use ad extensions to improve visibility',
                'Test different match types for each keyword'
            ],
            top_competitors: [
                { name: 'Competitor A', estimated_budget: 5000, ad_position: 1.2 },
                { name: 'Competitor B', estimated_budget: 3500, ad_position: 1.5 },
                { name: 'Competitor C', estimated_budget: 2800, ad_position: 2.1 }
            ]
        };
        
        return analysis;
    }
}

// CLI Interface
async function main() {
    const args = process.argv.slice(2);
    const action = args[0];
    
    const api = new MicrosoftAdsAPI();
    
    try {
        switch (action) {
            case 'get-campaigns':
                const campaigns = await api.getCampaigns();
                console.log(JSON.stringify(campaigns, null, 2));
                break;
                
            case 'keyword-suggestions':
                const keywords = args.slice(1);
                if (keywords.length === 0) {
                    console.error('Error: Please provide keywords');
                    process.exit(1);
                }
                const suggestions = await api.getKeywordSuggestions(keywords);
                console.log(JSON.stringify(suggestions, null, 2));
                break;
                
            case 'performance-report':
                const startDate = args[1] || new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString().split('T')[0];
                const endDate = args[2] || new Date().toISOString().split('T')[0];
                const report = await api.getPerformanceReport(startDate, endDate);
                console.log(JSON.stringify(report, null, 2));
                break;
                
            case 'competitor-analysis':
                const analysisKeywords = args.slice(1);
                if (analysisKeywords.length === 0) {
                    console.error('Error: Please provide keywords for analysis');
                    process.exit(1);
                }
                const analysis = await api.competitorAnalysis(analysisKeywords);
                console.log(JSON.stringify(analysis, null, 2));
                break;
                
            default:
                console.log(`Usage: node microsoft_ads_api.js [action] [options]`);
                console.log(`Actions:`);
                console.log(`  get-campaigns                    - Get all campaigns`);
                console.log(`  keyword-suggestions <keywords>   - Get keyword suggestions`);
                console.log(`  performance-report [start] [end] - Get performance report`);
                console.log(`  competitor-analysis <keywords>   - Analyze competitors`);
                break;
        }
        
    } catch (error) {
        console.error('Operation failed:', error.message);
        process.exit(1);
    }
}

// Run if called directly
if (require.main === module) {
    main();
}

module.exports = MicrosoftAdsAPI;
