#!/usr/bin/env python3
"""
LinkedIn Ads Manager - Python implementation for LinkedIn Marketing API
"""

import os
import json
import sys
import argparse
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import requests
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

class LinkedInAdsManager:
    """Manager for LinkedIn Advertising API operations"""
    
    def __init__(self):
        self.client_id = os.getenv('LINKEDIN_CLIENT_ID')
        self.client_secret = os.getenv('LINKEDIN_CLIENT_SECRET')
        self.access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')
        self.ad_account_id = os.getenv('LINKEDIN_AD_ACCOUNT_ID')
        self.base_url = 'https://api.linkedin.com/v2'
        
        if not all([self.client_id, self.client_secret, self.access_token, self.ad_account_id]):
            raise ValueError("Missing LinkedIn API credentials in .env file")
    
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """Make authenticated request to LinkedIn API"""
        url = f"{self.base_url}{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
            'X-Restli-Protocol-Version': '2.0.0'
        }
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, json=data)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError(f"Unsupported method: {method}")
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API Request failed: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"Response: {e.response.text}")
            raise
    
    def refresh_access_token(self) -> str:
        """Refresh LinkedIn access token"""
        refresh_token = os.getenv('LINKEDIN_REFRESH_TOKEN')
        if not refresh_token:
            raise ValueError("Refresh token not available in .env")
        
        token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        
        response = requests.post(token_url, data=data)
        response.raise_for_status()
        token_data = response.json()
        
        # Update environment variable
        self.access_token = token_data['access_token']
        os.environ['LINKEDIN_ACCESS_TOKEN'] = self.access_token
        
        # Save new refresh token if provided
        if 'refresh_token' in token_data:
            os.environ['LINKEDIN_REFRESH_TOKEN'] = token_data['refresh_token']
        
        return self.access_token
    
    def create_campaign(self, name: str, daily_budget: float, objective: str = 'WEBSITE_VISITS', 
                       start_date: Optional[str] = None, end_date: Optional[str] = None) -> Dict:
        """Create a new LinkedIn campaign"""
        if not start_date:
            start_date = datetime.now().strftime('%Y-%m-%d')
        if not end_date:
            end_date = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
        
        campaign_data = {
            'account': f"urn:li:sponsoredAccount:{self.ad_account_id}",
            'name': name,
            'objectiveType': objective,
            'status': 'ACTIVE',
            'runSchedule': {
                'start': start_date,
                'end': end_date
            },
            'dailyBudget': {
                'amount': daily_budget,
                'currencyCode': 'USD'
            }
        }
        
        return self._make_request('POST', '/adCampaignsV2', campaign_data)
    
    def get_campaigns(self, status: Optional[str] = None) -> List[Dict]:
        """Get list of campaigns"""
        endpoint = f"/adCampaignsV2?q=account&account=urn:li:sponsoredAccount:{self.ad_account_id}"
        if status:
            endpoint += f"&status={status}"
        
        response = self._make_request('GET', endpoint)
        return response.get('elements', [])
    
    def get_campaign_analytics(self, campaign_id: str, date_range: str = 'LAST_30_DAYS') -> Dict:
        """Get analytics for a specific campaign"""
        endpoint = f"/adAnalyticsV2?q=analytics&pivot=CAMPAIGN&dateRange={date_range}&campaigns[0]=urn:li:sponsoredCampaign:{campaign_id}"
        
        response = self._make_request('GET', endpoint)
        return response
    
    def create_ad_creative(self, campaign_id: str, creative_data: Dict) -> Dict:
        """Create ad creative for a campaign"""
        creative_data['campaign'] = f"urn:li:sponsoredCampaign:{campaign_id}"
        return self._make_request('POST', '/adCreativesV2', creative_data)
    
    def get_account_analytics(self, date_range: str = 'LAST_30_DAYS') -> Dict:
        """Get overall account analytics"""
        endpoint = f"/adAnalyticsV2?q=analytics&pivot=ACCOUNT&dateRange={date_range}&accounts[0]=urn:li:sponsoredAccount:{self.ad_account_id}"
        
        response = self._make_request('GET', endpoint)
        return response
    
    def generate_report(self, report_type: str = 'performance', format: str = 'json') -> Any:
        """Generate performance report"""
        analytics = self.get_account_analytics()
        
        if format == 'json':
            return json.dumps(analytics, indent=2)
        elif format == 'csv':
            # Convert to DataFrame and then CSV
            df = pd.DataFrame(analytics.get('elements', []))
            return df.to_csv(index=False)
        else:
            return analytics

# Command-line interface
def main():
    parser = argparse.ArgumentParser(description='LinkedIn Ads Manager')
    parser.add_argument('--test', action='store_true', help='Test API connection')
    parser.add_argument('--create-campaign', type=str, help='Create new campaign with given name')
    parser.add_argument('--budget', type=float, default=50.0, help='Daily budget for campaign')
    parser.add_argument('--list-campaigns', action='store_true', help='List all campaigns')
    parser.add_argument('--get-analytics', type=str, help='Get analytics for campaign ID')
    parser.add_argument('--generate-report', action='store_true', help='Generate performance report')
    parser.add_argument('--format', type=str, default='json', choices=['json', 'csv'], help='Report format')
    
    args = parser.parse_args()
    
    try:
        manager = LinkedInAdsManager()
        
        if args.test:
            print("Testing LinkedIn API connection...")
            campaigns = manager.get_campaigns()
            print(f"✅ Connected successfully. Found {len(campaigns)} campaigns.")
        
        elif args.create_campaign:
            print(f"Creating campaign: {args.create_campaign}")
            result = manager.create_campaign(args.create_campaign, args.budget)
            print(f"✅ Campaign created: {json.dumps(result, indent=2)}")
        
        elif args.list_campaigns:
            campaigns = manager.get_campaigns()
            print(f"Found {len(campaigns)} campaigns:")
            for campaign in campaigns:
                print(f"- {campaign.get('name')} (ID: {campaign.get('id')}, Status: {campaign.get('status')})")
        
        elif args.get_analytics:
            analytics = manager.get_campaign_analytics(args.get_analytics)
            print(f"Campaign Analytics: {json.dumps(analytics, indent=2)}")
        
        elif args.generate_report:
            report = manager.generate_report(format=args.format)
            if args.format == 'csv':
                filename = f"linkedin_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                with open(filename, 'w') as f:
                    f.write(report)
                print(f"✅ Report saved to: {filename}")
            else:
                print(report)
        
        else:
            parser.print_help()
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
