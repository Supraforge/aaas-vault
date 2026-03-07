#!/usr/bin/env python3
"""
Google Ads Manager - Main interface for Google Ads API
"""

import os
import sys
import json
import argparse
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

# Google Ads imports
try:
    from google.ads.googleads.client import GoogleAdsClient
    from google.ads.googleads.errors import GoogleAdsException
    from google.auth.exceptions import RefreshError
    HAS_GOOGLE_ADS = True
except ImportError:
    HAS_GOOGLE_ADS = False
    print("❌ Google Ads library not installed. Run: pip install google-ads")

@dataclass
class Campaign:
    """Campaign data structure"""
    id: str
    name: str
    status: str
    budget: float
    clicks: int
    impressions: int
    cost: float
    conversions: float
    ctr: float
    cpc: float
    conversion_rate: float
    roas: float
    
@dataclass
class Keyword:
    """Keyword data structure"""
    text: str
    match_type: str
    cpc_bid: float
    clicks: int
    impressions: int
    cost: float
    conversions: float
    quality_score: int

class GoogleAdsManager:
    """Main manager for Google Ads operations"""
    
    def __init__(self, config_path: str = None):
        """Initialize Google Ads client"""
        if not HAS_GOOGLE_ADS:
            raise ImportError("Google Ads library not installed")
        
        # Load configuration
        self.config = self._load_config(config_path)
        
        # Initialize client
        try:
            self.client = GoogleAdsClient.load_from_dict(self.config)
            self.customer_id = self.config["login_customer_id"]
            print(f"✅ Connected to Google Ads account: {self.customer_id}")
        except Exception as e:
            print(f"❌ Failed to connect to Google Ads: {e}")
            raise
    
    def _load_config(self, config_path: str = None) -> Dict[str, Any]:
        """Load configuration from .env or environment"""
        if config_path and os.path.exists(config_path):
            # Load from JSON file
            with open(config_path, 'r') as f:
                return json.load(f)
        
        # Load from environment variables
        config = {
            "developer_token": os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN"),
            "client_id": os.getenv("GOOGLE_ADS_CLIENT_ID"),
            "client_secret": os.getenv("GOOGLE_ADS_CLIENT_SECRET"),
            "refresh_token": os.getenv("GOOGLE_ADS_REFRESH_TOKEN"),
            "login_customer_id": os.getenv("GOOGLE_ADS_CUSTOMER_ID"),
            "use_proto_plus": True
        }
        
        # Validate required fields
        required = ["developer_token", "client_id", "client_secret", "refresh_token", "login_customer_id"]
        missing = [field for field in required if not config[field]]
        
        if missing:
            raise ValueError(f"Missing required configuration: {missing}")
        
        return config
    
    def get_campaigns(self, status: str = None) -> List[Campaign]:
        """Retrieve all campaigns"""
        campaigns = []
        
        try:
            ga_service = self.client.get_service("GoogleAdsService")
            
            # Build query
            query = '''
                SELECT
                    campaign.id,
                    campaign.name,
                    campaign.status,
                    campaign.advertising_channel_type,
                    metrics.clicks,
                    metrics.impressions,
                    metrics.cost_micros,
                    metrics.conversions,
                    metrics.ctr,
                    metrics.average_cpc,
                    metrics.conversions_from_interactions_rate,
                    metrics.all_conversions_value
                FROM campaign
                WHERE segments.date DURING LAST_30_DAYS
            '''
            
            if status:
                query += f" AND campaign.status = '{status}'"
            
            # Execute query
            response = ga_service.search(
                customer_id=self.customer_id,
                query=query
            )
            
            for row in response:
                campaign = row.campaign
                metrics = row.metrics
                
                # Calculate ROAS
                cost = metrics.cost_micros / 1_000_000 if metrics.cost_micros else 0
                conversions_value = metrics.all_conversions_value if metrics.all_conversions_value else 0
                roas = (conversions_value / cost) if cost > 0 else 0
                
                campaigns.append(Campaign(
                    id=campaign.id,
                    name=campaign.name,
                    status=campaign.status.name,
                    budget=0,  # Would need separate query for budget
                    clicks=metrics.clicks,
                    impressions=metrics.impressions,
                    cost=cost,
                    conversions=metrics.conversions,
                    ctr=metrics.ctr if metrics.ctr else 0,
                    cpc=metrics.average_cpc / 1_000_000 if metrics.average_cpc else 0,
                    conversion_rate=metrics.conversions_from_interactions_rate if metrics.conversions_from_interactions_rate else 0,
                    roas=roas
                ))
            
            print(f"✅ Retrieved {len(campaigns)} campaigns")
            
        except GoogleAdsException as e:
            print(f"❌ Google Ads API error: {e}")
        except Exception as e:
            print(f"❌ Error retrieving campaigns: {e}")
        
        return campaigns
    
    def create_search_campaign(self, name: str, budget: float, keywords: List[str]) -> Optional[str]:
        """Create a new search campaign"""
        try:
            campaign_service = self.client.get_service("CampaignService")
            campaign_budget_service = self.client.get_service("CampaignBudgetService")
            
            # Create campaign budget
            budget_operation = self.client.get_type("CampaignBudgetOperation")
            budget_obj = budget_operation.create
            budget_obj.name = f"Budget for {name}"
            budget_obj.delivery_method = self.client.enums.BudgetDeliveryMethodEnum.STANDARD
            budget_obj.amount_micros = int(budget * 1_000_000)
            
            # Add budget
            budget_response = campaign_budget_service.mutate_campaign_budgets(
                customer_id=self.customer_id,
                operations=[budget_operation]
            )
            budget_id = budget_response.results[0].resource_name.split('/')[-1]
            
            print(f"✅ Created budget: {budget_id}")
            
            # TODO: Complete campaign creation with ad groups and keywords
            # This is a simplified version - full implementation would be longer
            
            return budget_id
            
        except Exception as e:
            print(f"❌ Failed to create campaign: {e}")
            return None
    
    def generate_performance_report(self, output_format: str = "json") -> str:
        """Generate campaign performance report"""
        campaigns = self.get_campaigns()
        
        if not campaigns:
            return "No campaigns found"
        
        # Prepare report data
        report_data = {
            "generated_at": datetime.now().isoformat(),
            "customer_id": self.customer_id,
            "total_campaigns": len(campaigns),
            "campaigns": [asdict(camp) for camp in campaigns],
            "summary": {
                "total_clicks": sum(c.clicks for c in campaigns),
                "total_impressions": sum(c.impressions for c in campaigns),
                "total_cost": sum(c.cost for c in campaigns),
                "total_conversions": sum(c.conversions for c in campaigns),
                "avg_ctr": sum(c.ctr for c in campaigns) / len(campaigns) if campaigns else 0,
                "avg_cpc": sum(c.cpc for c in campaigns) / len(campaigns) if campaigns else 0,
                "avg_roas": sum(c.roas for c in campaigns) / len(campaigns) if campaigns else 0
            }
        }
        
        # Generate output
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if output_format.lower() == "csv":
            import csv
            output_file = f"google_ads_report_{timestamp}.csv"
            
            with open(output_file, 'w', newline='') as csvfile:
                fieldnames = ["id", "name", "status", "clicks", "impressions", "cost", "conversions", "ctr", "cpc", "conversion_rate", "roas"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for camp in campaigns:
                    writer.writerow(asdict(camp))
            
            print(f"✅ Report saved to: {output_file}")
            return output_file
            
        else:  # JSON format
            output_file = f"google_ads_report_{timestamp}.json"
            
            with open(output_file, 'w') as jsonfile:
                json.dump(report_data, jsonfile, indent=2, default=str)
            
            print(f"✅ Report saved to: {output_file}")
            return output_file
    
    def optimize_bids(self, campaign_id: str = None) -> Dict[str, Any]:
        """Optimize bids for campaigns"""
        recommendations = {
            "timestamp": datetime.now().isoformat(),
            "recommendations": []
        }
        
        campaigns = self.get_campaigns()
        
        for campaign in campaigns:
            if campaign_id and campaign.id != campaign_id:
                continue
            
            rec = {
                "campaign_id": campaign.id,
                "campaign_name": campaign.name,
                "current_metrics": {
                    "ctr": campaign.ctr,
                    "cpc": campaign.cpc,
                    "conversion_rate": campaign.conversion_rate,
                    "roas": campaign.roas
                },
                "suggestions": []
            }
            
            # Bid optimization logic
            if campaign.ctr < 0.02:  # Low CTR
                rec["suggestions"].append({
                    "type": "bid_adjustment",
                    "action": "decrease",
                    "amount": "20%",
                    "reason": "Low CTR indicates poor ad relevance"
                })
            
            if campaign.roas > 3.0:  # High ROAS
                rec["suggestions"].append({
                    "type": "bid_adjustment",
                    "action": "increase",
                    "amount": "15%",
                    "reason": "High ROAS indicates profitable campaign"
                })
            
            if campaign.conversion_rate > 0.05:  # Good conversion rate
                rec["suggestions"].append({
                    "type": "budget_increase",
                    "action": "increase",
                    "amount": "25%",
                    "reason": "High conversion rate indicates effective targeting"
                })
            
            recommendations["recommendations"].append(rec)
        
        return recommendations

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Google Ads Manager")
    parser.add_argument("--test", action="store_true", help="Test connection")
    parser.add_argument("--list-campaigns", action="store_true", help="List all campaigns")
    parser.add_argument("--report", choices=["json", "csv"], help="Generate performance report")
    parser.add_argument("--optimize", help="Optimize bids for campaign ID")
    parser.add_argument("--config", help="Path to config file")
    
    args = parser.parse_args()
    
    try:
        manager = GoogleAdsManager(args.config)
        
        if args.test:
            print("✅ Connection test successful")
            
        elif args.list_campaigns:
            campaigns = manager.get_campaigns()
            print(f"\n📊 Found {len(campaigns)} campaigns:")
            for camp in campaigns:
                print(f"  • {camp.name} (ID: {camp.id}) - Status: {camp.status}")
                print(f"    Clicks: {camp.clicks}, Cost: ${camp.cost:.2f}, ROAS: {camp.roas:.2f}")
                
        elif args.report:
            report_file = manager.generate_performance_report(args.report)
            print(f"\n📈 Report generated: {report_file}")
            
        elif args.optimize:
            recommendations = manager.optimize_bids(args.optimize)
            print(f"\n🎯 Optimization recommendations:")
            for rec in recommendations["recommendations"]:
                print(f"\nCampaign: {rec['campaign_name']}")
                for suggestion in rec["suggestions"]:
                    print(f"  • {suggestion['action'].upper()} {suggestion['type']} by {suggestion['amount']}")
                    print(f"    Reason: {suggestion['reason']}")
                    
        else:
            parser.print_help()
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
