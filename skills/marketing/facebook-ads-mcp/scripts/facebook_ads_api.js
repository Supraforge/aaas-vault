// Facebook Ads API JavaScript client
const { FacebookAdsApi, AdAccount, Campaign, AdSet, Ad } = require('facebook-nodejs-business-sdk');
const fs = require('fs');
const path = require('path');

// Load environment variables
require('dotenv').config({ path: path.join(__dirname, '..', '.env') });

class FacebookAdsClient {
    constructor() {
        this.accessToken = process.env.FACEBOOK_ADS_ACCESS_TOKEN;
        this.accountId = process.env.FACEBOOK_ADS_ACCOUNT_ID;
        this.appId = process.env.FACEBOOK_ADS_APP_ID;
        this.appSecret = process.env.FACEBOOK_ADS_APP_SECRET;
        this.apiVersion = process.env.FACEBOOK_ADS_API_VERSION || 'v19.0';
        
        if (!this.accessToken || !this.accountId || !this.appId || !this.appSecret) {
            throw new Error('Missing Facebook Ads credentials in environment variables');
        }
        
        FacebookAdsApi.init(this.accessToken, this.appId, this.appSecret, this.accountId, this.apiVersion);
        this.account = new AdAccount(`act_${this.accountId}`);
    }
    
    async listCampaigns(limit = 10) {
        try {
            const campaigns = await this.account.getCampaigns([
                'id', 'name', 'objective', 'status',
                'daily_budget', 'lifetime_budget', 'created_time'
            ], { limit });
            
            return campaigns.map(campaign => ({
                id: campaign.id,
                name: campaign.name,
                objective: campaign.objective,
                status: campaign.status,
                daily_budget: campaign.daily_budget,
                lifetime_budget: campaign.lifetime_budget,
                created_time: campaign.created_time
            }));
        } catch (error) {
            console.error('Error listing campaigns:', error.message);
            throw error;
        }
    }
    
    async getCampaignInsights(campaignId, dateRange = 'last_7_days') {
        try {
            const campaign = new Campaign(campaignId);
            
            // Calculate date range
            const endDate = new Date();
            let startDate = new Date();
            
            switch(dateRange) {
                case 'today':
                    startDate.setHours(0, 0, 0, 0);
                    break;
                case 'yesterday':
                    startDate.setDate(startDate.getDate() - 1);
                    startDate.setHours(0, 0, 0, 0);
                    endDate.setHours(0, 0, 0, 0);
                    break;
                case 'last_7_days':
                    startDate.setDate(startDate.getDate() - 7);
                    break;
                case 'last_30_days':
                    startDate.setDate(startDate.getDate() - 30);
                    break;
                default:
                    startDate.setDate(startDate.getDate() - 7);
            }
            
            const params = {
                time_range: {
                    since: startDate.toISOString().split('T')[0],
                    until: endDate.toISOString().split('T')[0]
                },
                level: 'campaign'
            };
            
            const fields = [
                'impressions',
                'clicks',
                'spend',
                'cpc',
                'cpm',
                'ctr',
                'conversions',
                'conversion_rate',
                'frequency',
                'reach'
            ];
            
            const insights = await campaign.getInsights(fields, params);
            return insights.map(insight => ({
                impressions: insight.impressions,
                clicks: insight.clicks,
                spend: insight.spend,
                cpc: insight.cpc,
                cpm: insight.cpm,
                ctr: insight.ctr,
                conversions: insight.conversions,
                conversion_rate: insight.conversion_rate,
                frequency: insight.frequency,
                reach: insight.reach,
                date_start: insight.date_start,
                date_stop: insight.date_stop
            }));
        } catch (error) {
            console.error('Error getting campaign insights:', error.message);
            throw error;
        }
    }
    
    async createCampaign(name, objective = 'OUTCOME_TRAFFIC', budget = 1000) {
        try {
            const campaignParams = {
                name,
                objective,
                status: 'PAUSED',
                special_ad_categories: []
            };
            
            const campaign = await this.account.createCampaign([], campaignParams);
            
            // Create ad set
            const adSetParams = {
                name: `${name} - Ad Set`,
                campaign_id: campaign.id,
                daily_budget: budget,
                billing_event: 'IMPRESSIONS',
                optimization_goal: 'LINK_CLICKS',
                bid_amount: 100,
                targeting: {
                    geo_locations: { countries: ['US'] },
                    age_min: 18,
                    age_max: 65,
                    publisher_platforms: ['facebook', 'instagram']
                },
                status: 'PAUSED'
            };
            
            const adSet = await this.account.createAdSet([], adSetParams);
            
            return {
                campaignId: campaign.id,
                adSetId: adSet.id,
                name,
                budget,
                status: 'PAUSED'
            };
        } catch (error) {
            console.error('Error creating campaign:', error.message);
            throw error;
        }
    }
}

// Command line interface
async function main() {
    const args = process.argv.slice(2);
    const command = args[0];
    
    try {
        const client = new FacebookAdsClient();
        
        switch(command) {
            case '--list-campaigns':
                const limit = args[1] ? parseInt(args[1]) : 10;
                const campaigns = await client.listCampaigns(limit);
                console.log(JSON.stringify(campaigns, null, 2));
                break;
                
            case '--campaign-insights':
                if (!args[1]) {
                    console.error('Campaign ID required');
                    process.exit(1);
                }
                const dateRange = args[2] || 'last_7_days';
                const insights = await client.getCampaignInsights(args[1], dateRange);
                console.log(JSON.stringify(insights, null, 2));
                break;
                
            case '--create-campaign':
                if (!args[1] || !args[2]) {
                    console.error('Campaign name and budget required');
                    console.error('Usage: node facebook_ads_api.js --create-campaign "Campaign Name" 1000');
                    process.exit(1);
                }
                const campaign = await client.createCampaign(args[1], 'OUTCOME_TRAFFIC', parseInt(args[2]));
                console.log(JSON.stringify(campaign, null, 2));
                break;
                
            case '--help':
                console.log('Facebook Ads API Commands:');
                console.log('  --list-campaigns [limit]          List campaigns');
                console.log('  --campaign-insights <id> [range]  Get campaign insights');
                console.log('  --create-campaign <name> <budget> Create campaign');
                console.log('  --help                            Show this help');
                break;
                
            default:
                console.error('Unknown command. Use --help for usage.');
                process.exit(1);
        }
    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    }
}

if (require.main === module) {
    main();
}

module.exports = FacebookAdsClient;
