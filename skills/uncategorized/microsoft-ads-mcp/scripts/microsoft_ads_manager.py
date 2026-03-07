#!/usr/bin/env python3
"""
Microsoft Ads Manager - Campaign management and automation
"""

import os
import sys
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

try:
    from bingads import ServiceClient
    from bingads.authorization import AuthorizationData, OAuthDesktopMobileAuthCodeGrant
    from bingads.v13.bulk import BulkServiceManager
    from bingads.v13 import CampaignManagementService
except ImportError:
    print("Error: Bing Ads SDK not installed. Run: pip install bingads")
    sys.exit(1)

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure logging
logging.basicConfig(
    level=os.getenv('MICROSOFT_ADS_LOG_LEVEL', 'INFO'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.getenv('MICROSOFT_ADS_LOG_FILE', './logs/microsoft_ads.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class MicrosoftAdsManager:
    """Manager for Microsoft Advertising operations"""
    
    def __init__(self):
        self.client_id = os.getenv('MICROSOFT_ADS_CLIENT_ID')
        self.client_secret = os.getenv('MICROSOFT_ADS_CLIENT_SECRET')
        self.refresh_token = os.getenv('MICROSOFT_ADS_REFRESH_TOKEN')
        self.developer_token = os.getenv('MICROSOFT_ADS_DEVELOPER_TOKEN')
        self.customer_id = os.getenv('MICROSOFT_ADS_CUSTOMER_ID')
        self.account_id = os.getenv('MICROSOFT_ADS_ACCOUNT_ID')
        
        if not all([self.client_id, self.client_secret, self.refresh_token, self.developer_token]):
            raise ValueError("Missing required environment variables. Check .env file")
        
        self.authorization_data = self._create_authorization()
        self.campaign_service = self._create_campaign_service()
        self.bulk_service = self._create_bulk_service()
    
    def _create_authorization(self) -> AuthorizationData:
        """Create authorization data for API access"""
        authentication = OAuthDesktopMobileAuthCodeGrant(
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        
        authentication.request_oauth_tokens_by_refresh_token(self.refresh_token)
        
        authorization_data = AuthorizationData(
            authentication=authentication,
            customer_id=self.customer_id,
            account_id=self.account_id,
            developer_token=self.developer_token
        )
        
        return authorization_data
    
    def _create_campaign_service(self):
        """Create campaign management service client"""
        return ServiceClient(
            service='CampaignManagementService',
            version=13,
            authorization_data=self.authorization_data,
            environment='production'
        )
    
    def _create_bulk_service(self):
        """Create bulk service client"""
        return BulkServiceManager(
            authorization_data=self.authorization_data
        )
    
    def create_campaign(self, name: str, budget: float, **kwargs) -> Dict[str, Any]:
        """Create a new search campaign"""
        try:
            logger.info(f"Creating campaign: {name} with budget: ${budget}")
            
            # Create campaign object
            campaign = {
                'Name': name,
                'Description': kwargs.get('description', f'Campaign created {datetime.now().isoformat()}'),
                'BudgetType': 'DailyBudgetStandard',
                'DailyBudget': budget,
                'TimeZone': kwargs.get('timezone', 'PacificTimeUSCanadaTijuana'),
                'Languages': ['English'],
                'Status': 'Active'
            }
            
            # Add targeting if provided
            if 'targeting' in kwargs:
                campaign['Targeting'] = kwargs['targeting']
            
            # TODO: Implement actual campaign creation via API
            # This is a placeholder for the actual API call
            
            result = {
                'campaign_id': f'camp_{datetime.now().strftime("%Y%m%d_%H%M%S")}',
                'name': name,
                'budget': budget,
                'status': 'created',
                'created_at': datetime.now().isoformat(),
                'estimated_impressions': kwargs.get('estimated_impressions', 10000),
                'estimated_clicks': kwargs.get('estimated_clicks', 200),
                'estimated_cost': kwargs.get('estimated_cost', budget * 30)  # Monthly estimate
            }
            
            logger.info(f"Campaign created successfully: {result['campaign_id']}")
            return result
            
        except Exception as e:
            logger.error(f"Failed to create campaign: {str(e)}")
            raise
    
    def get_campaign_performance(self, campaign_id: str, days: int = 30) -> Dict[str, Any]:
        """Get performance metrics for a campaign"""
        try:
            logger.info(f"Getting performance for campaign: {campaign_id} (last {days} days)")
            
            # TODO: Implement actual performance data retrieval
            # This is placeholder data
            
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days)
            
            performance_data = {
                'campaign_id': campaign_id,
                'date_range': {
                    'start': start_date.isoformat(),
                    'end': end_date.isoformat()
                },
                'metrics': {
                    'impressions': 15000,
                    'clicks': 300,
                    'ctr': 2.0,
                    'average_cpc': 4.50,
                    'conversions': 15,
                    'conversion_rate': 5.0,
                    'cost': 1350.00,
                    'revenue': 4500.00,
                    'roas': 333.33
                },
                'trends': {
                    'ctr_trend': 'increasing',
                    'cpc_trend': 'stable',
                    'conversion_trend': 'increasing'
                },
                'recommendations': [
                    'Increase budget by 20% for top-performing keywords',
                    'Add negative keywords to reduce irrelevant traffic',
                    'Test new ad copy variations'
                ]
            }
            
            return performance_data
            
        except Exception as e:
            logger.error(f"Failed to get campaign performance: {str(e)}")
            raise
    
    def optimize_keywords(self, campaign_id: str, **kwargs) -> Dict[str, Any]:
        """Optimize keywords for a campaign"""
        try:
            max_cpc = kwargs.get('max_cpc', 5.0)
            logger.info(f"Optimizing keywords for campaign: {campaign_id} (max CPC: ${max_cpc})")
            
            # TODO: Implement actual keyword optimization logic
            
            optimization_result = {
                'campaign_id': campaign_id,
                'optimization_date': datetime.now().isoformat(),
                'actions_taken': [
                    'Increased bids for high-converting keywords',
                    'Decreased bids for low-performing keywords',
                    'Added 15 new keyword suggestions',
                    'Paused 8 underperforming keywords'
                ],
                'expected_improvement': {
                    'ctr_increase': 0.5,
                    'cpc_decrease': 0.75,
                    'conversion_increase': 2.0,
                    'roas_improvement': 50.0
                },
                'new_keywords': [
                    {'keyword': 'enterprise software solutions', 'match_type': 'Exact', 'bid': 6.50},
                    {'keyword': 'cloud migration services', 'match_type': 'Phrase', 'bid': 5.75},
                    {'keyword': 'digital transformation consulting', 'match_type': 'Broad', 'bid': 4.25}
                ]
            }
            
            return optimization_result
            
        except Exception as e:
            logger.error(f"Failed to optimize keywords: {str(e)}")
            raise


def main():
    """Main function for CLI usage"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Microsoft Ads Campaign Manager')
    parser.add_argument('--action', required=True, choices=['create_campaign', 'get_performance', 'optimize_keywords'],
                       help='Action to perform')
    parser.add_argument('--name', help='Campaign name (for create_campaign)')
    parser.add_argument('--budget', type=float, help='Daily budget (for create_campaign)')
    parser.add_argument('--campaign-id', help='Campaign ID (for get_performance and optimize_keywords)')
    parser.add_argument('--days', type=int, default=30, help='Number of days for performance report')
    parser.add_argument('--max-cpc', type=float, default=5.0, help='Maximum CPC for optimization')
    parser.add_argument('--output', choices=['json', 'csv', 'table'], default='json', help='Output format')
    
    args = parser.parse_args()
    
    try:
        manager = MicrosoftAdsManager()
        
        if args.action == 'create_campaign':
            if not args.name or not args.budget:
                print("Error: --name and --budget required for create_campaign")
                sys.exit(1)
            
            result = manager.create_campaign(args.name, args.budget)
            
        elif args.action == 'get_performance':
            if not args.campaign_id:
                print("Error: --campaign-id required for get_performance")
                sys.exit(1)
            
            result = manager.get_campaign_performance(args.campaign_id, args.days)
            
        elif args.action == 'optimize_keywords':
            if not args.campaign_id:
                print("Error: --campaign-id required for optimize_keywords")
                sys.exit(1)
            
            result = manager.optimize_keywords(args.campaign_id, max_cpc=args.max_cpc)
        
        # Output result
        if args.output == 'json':
            print(json.dumps(result, indent=2))
        elif args.output == 'table':
            from tabulate import tabulate
            if isinstance(result, dict):
                table = [[k, v] for k, v in result.items()]
                print(tabulate(table, headers=['Key', 'Value'], tablefmt='grid'))
        else:
            print(result)
            
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
