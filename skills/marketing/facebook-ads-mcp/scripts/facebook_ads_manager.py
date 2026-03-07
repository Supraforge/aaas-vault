#!/usr/bin/env python3
"""
Facebook Ads Manager - Campaign creation and management
"""

import os
import sys
import json
import argparse
from datetime import datetime, timedelta
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad

def init_api():
    """Initialize Facebook Ads API"""
    access_token = os.getenv('FACEBOOK_ADS_ACCESS_TOKEN')
    app_id = os.getenv('FACEBOOK_ADS_APP_ID')
    app_secret = os.getenv('FACEBOOK_ADS_APP_SECRET')
    account_id = os.getenv('FACEBOOK_ADS_ACCOUNT_ID')
    api_version = os.getenv('FACEBOOK_ADS_API_VERSION', 'v19.0')
    
    if not all([access_token, app_id, app_secret, account_id]):
        print("❌ Missing Facebook Ads credentials in environment variables")
        print("Please set FACEBOOK_ADS_ACCESS_TOKEN, FACEBOOK_ADS_APP_ID,")
        print("FACEBOOK_ADS_APP_SECRET, and FACEBOOK_ADS_ACCOUNT_ID in .env")
        sys.exit(1)
    
    FacebookAdsApi.init(access_token=access_token, 
                       app_id=app_id, 
                       app_secret=app_secret,
                       api_version=api_version)
    return AdAccount(f'act_{account_id}')

def create_campaign(account, name, objective, budget, status='PAUSED'):
    """Create a new Facebook Ads campaign"""
    print(f"🚀 Creating campaign: {name}")
    
    campaign_params = {
        'name': name,
        'objective': objective,  # e.g., 'OUTCOME_TRAFFIC', 'OUTCOME_CONVERSIONS'
        'status': status,
        'special_ad_categories': [],
    }
    
    campaign = account.create_campaign(params=campaign_params)
    print(f"✅ Campaign created with ID: {campaign['id']}")
    
    # Create ad set
    adset_params = {
        'name': f'{name} - Ad Set',
        'campaign_id': campaign['id'],
        'daily_budget': budget,
        'billing_event': 'IMPRESSIONS',
        'optimization_goal': 'LINK_CLICKS',
        'bid_amount': 100,
        'targeting': {
            'geo_locations': {'countries': ['US']},
            'age_min': 18,
            'age_max': 65,
            'publisher_platforms': ['facebook', 'instagram'],
        },
        'status': 'PAUSED',
    }
    
    adset = account.create_ad_set(params=adset_params)
    print(f"✅ Ad Set created with ID: {adset['id']}")
    
    return {
        'campaign_id': campaign['id'],
        'adset_id': adset['id'],
        'name': name,
        'budget': budget,
        'status': status
    }

def list_campaigns(account, limit=10):
    """List all campaigns in the account"""
    print(f"📋 Listing campaigns (limit: {limit})")
    
    campaigns = account.get_campaigns(fields=[
        'id', 'name', 'objective', 'status', 
        'daily_budget', 'lifetime_budget', 'created_time'
    ], limit=limit)
    
    result = []
    for campaign in campaigns:
        result.append({
            'id': campaign['id'],
            'name': campaign.get('name', 'N/A'),
            'objective': campaign.get('objective', 'N/A'),
            'status': campaign.get('status', 'N/A'),
            'daily_budget': campaign.get('daily_budget', 'N/A'),
            'created_time': campaign.get('created_time', 'N/A')
        })
    
    return result

def update_campaign_budget(account, campaign_id, new_budget):
    """Update campaign budget"""
    print(f"💰 Updating campaign {campaign_id} budget to {new_budget}")
    
    campaign = Campaign(campaign_id)
    campaign.update({
        Campaign.Field.daily_budget: new_budget
    })
    
    return {
        'campaign_id': campaign_id,
        'new_budget': new_budget,
        'updated': True
    }

def main():
    parser = argparse.ArgumentParser(description='Facebook Ads Campaign Manager')
    parser.add_argument('--action', required=True, 
                       choices=['create', 'list', 'update-budget', 'pause', 'delete'],
                       help='Action to perform')
    parser.add_argument('--name', help='Campaign name (for create action)')
    parser.add_argument('--budget', type=int, help='Daily budget in cents (for create/update)')
    parser.add_argument('--objective', default='OUTCOME_TRAFFIC', 
                       help='Campaign objective (default: OUTCOME_TRAFFIC)')
    parser.add_argument('--campaign-id', help='Campaign ID (for update/pause/delete)')
    parser.add_argument('--limit', type=int, default=10, help='Limit for list action')
    parser.add_argument('--output', choices=['json', 'text'], default='text',
                       help='Output format')
    
    args = parser.parse_args()
    
    # Initialize API
    try:
        account = init_api()
    except Exception as e:
        print(f"❌ Failed to initialize Facebook Ads API: {e}")
        sys.exit(1)
    
    # Perform action
    if args.action == 'create':
        if not args.name or not args.budget:
            print("❌ --name and --budget are required for create action")
            sys.exit(1)
        
        result = create_campaign(account, args.name, args.objective, args.budget)
        
    elif args.action == 'list':
        result = list_campaigns(account, args.limit)
        
    elif args.action == 'update-budget':
        if not args.campaign_id or not args.budget:
            print("❌ --campaign-id and --budget are required for update-budget action")
            sys.exit(1)
        
        result = update_campaign_budget(account, args.campaign_id, args.budget)
        
    else:
        print(f"❌ Action '{args.action}' not implemented yet")
        sys.exit(1)
    
    # Output result
    if args.output == 'json':
        print(json.dumps(result, indent=2))
    else:
        if isinstance(result, list):
            for item in result:
                print(f"Campaign: {item['name']} (ID: {item['id']})")
                print(f"  Objective: {item['objective']}")
                print(f"  Status: {item['status']}")
                print(f"  Budget: {item.get('daily_budget', 'N/A')}")
                print(f"  Created: {item.get('created_time', 'N/A')}")
                print()
        else:
            for key, value in result.items():
                print(f"{key}: {value}")

if __name__ == '__main__':
    main()
