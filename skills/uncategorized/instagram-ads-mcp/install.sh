#!/bin/bash
# Instagram Ads MCP Skill - Installation

echo "🚀 Installing Instagram Ads MCP Skill dependencies..."

# Python dependencies
echo "📦 Installing Python packages..."
pip install facebook-business pandas python-dotenv requests pillow

# Node.js dependencies (optional)
if command -v npm &> /dev/null && [ -f "scripts/package.json" ]; then
    echo "📦 Installing Node.js packages..."
    cd scripts
    npm install
    cd ..
fi

# Create scripts directory
mkdir -p scripts

# Create Python scripts
cat > scripts/instagram_ads_manager.py << 'PYEOF'
#!/usr/bin/env python3
"""
Instagram Ads Manager - Core campaign operations using Facebook Marketing API
"""
import os
import json
import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import argparse
import sys
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adcreative import AdCreative

# Load environment variables
load_dotenv()

class InstagramAdsManager:
    def __init__(self):
        self.access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
        self.ad_account_id = os.getenv('FACEBOOK_AD_ACCOUNT_ID')
        self.instagram_account_id = os.getenv('INSTAGRAM_BUSINESS_ACCOUNT_ID')
        
        # Initialize Facebook Ads API
        FacebookAdsApi.init(access_token=self.access_token)
        self.account = AdAccount(f'act_{self.ad_account_id}')
    
    def create_campaign(self, name, objective, status='ACTIVE', **kwargs):
        """Create a new Instagram campaign"""
        params = {
            'name': name,
            'objective': objective,
            'status': status,
            'special_ad_categories': [],
            **kwargs
        }
        
        campaign = self.account.create_campaign(params=params)
        return campaign
    
    def get_campaigns(self, fields=None):
        """Get all campaigns for account"""
        if fields is None:
            fields = ['id', 'name', 'objective', 'status', 'daily_budget', 'lifetime_budget']
        
        campaigns = self.account.get_campaigns(fields=fields)
        return campaigns
    
    def create_ad_set(self, campaign_id, name, targeting, optimization_goal, **kwargs):
        """Create ad set within campaign"""
        params = {
            'name': name,
            'campaign_id': campaign_id,
            'targeting': targeting,
            'optimization_goal': optimization_goal,
            'billing_event': 'IMPRESSIONS',
            'bid_amount': 100,
            'daily_budget': 1000,
            'status': 'ACTIVE',
            **kwargs
        }
        
        ad_set = self.account.create_ad_set(params=params)
        return ad_set
    
    def create_instagram_ad(self, ad_set_id, creative_data):
        """Create Instagram ad within ad set"""
        # Create creative
        creative = AdCreative(parent_id=self.ad_account_id)
        creative.update(creative_data)
        creative.remote_create()
        
        # Create ad
        params = {
            'name': creative_data.get('name', 'Instagram Ad'),
            'adset_id': ad_set_id,
            'creative': {'creative_id': creative['id']},
            'status': 'ACTIVE'
        }
        
        ad = self.account.create_ad(params=params)
        return ad
    
    def get_insights(self, level='campaign', fields=None, date_preset='last_30d'):
        """Get insights for campaigns, ad sets, or ads"""
        if fields is None:
            fields = [
                'impressions', 'reach', 'clicks', 'ctr',
                'spend', 'actions', 'action_values',
                'video_avg_time_watched', 'video_p25_watched',
                'video_p50_watched', 'video_p75_watched',
                'video_p95_watched', 'video_p100_watched'
            ]
        
        params = {
            'level': level,
            'fields': fields,
            'date_preset': date_preset
        }
        
        insights = self.account.get_insights(params=params)
        return insights
    
    def get_instagram_media(self, fields=None):
        """Get Instagram media for business account"""
        if fields is None:
            fields = ['id', 'caption', 'media_type', 'media_url', 'permalink', 'timestamp']
        
        url = f'https://graph.facebook.com/v18.0/{self.instagram_account_id}/media'
        params = {
            'access_token': self.access_token,
            'fields': ','.join(fields)
        }
        
        response = requests.get(url, params=params)
        return response.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Instagram Ads Manager')
    parser.add_argument('--action', required=True,
                       choices=['create_campaign', 'get_campaigns', 'create_ad_set',
                                'create_ad', 'get_insights', 'get_instagram_media'],
                       help='Action to perform')
    parser.add_argument('--name', help='Campaign or ad set name')
    parser.add_argument('--objective', help='Campaign objective')
    parser.add_argument('--campaign-id', help='Campaign ID')
    parser.add_argument('--ad-set-id', help='Ad set ID')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    manager = InstagramAdsManager()
    
    try:
        if args.action == 'create_campaign':
            result = manager.create_campaign(
                name=args.name,
                objective=args.objective or 'OUTCOME_TRAFFIC'
            )
            result = result.export_all_data()
        elif args.action == 'get_campaigns':
            campaigns = manager.get_campaigns()
            result = [campaign.export_all_data() for campaign in campaigns]
        elif args.action == 'create_ad_set':
            # Example targeting
            targeting = {
                'geo_locations': {'countries': ['US']},
                'age_min': 18,
                'age_max': 65,
                'facebook_positions': ['feed', 'story', 'explore'],
                'instagram_positions': ['feed', 'story', 'explore']
            }
            result = manager.create_ad_set(
                campaign_id=args.campaign_id,
                name=args.name,
                targeting=targeting,
                optimization_goal='REACH'
            )
            result = result.export_all_data()
        elif args.action == 'create_ad':
            creative_data = {
                'name': args.name or 'Instagram Ad',
                'object_story_spec': {
                    'page_id': os.getenv('FACEBOOK_PAGE_ID'),
                    'instagram_actor_id': os.getenv('INSTAGRAM_BUSINESS_ACCOUNT_ID'),
                    'link_data': {
                        'link': 'https://example.com',
                        'message': 'Check out our products!',
                        'call_to_action': {'type': 'LEARN_MORE'}
                    }
                }
            }
            result = manager.create_instagram_ad(args.ad_set_id, creative_data)
            result = result.export_all_data()
        elif args.action == 'get_insights':
            insights = manager.get_insights()
            result = [insight.export_all_data() for insight in insights]
        elif args.action == 'get_instagram_media':
            result = manager.get_instagram_media()
        
        # Output results
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"Results saved to {args.output}")
        else:
            print(json.dumps(result, indent=2))
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
PYEOF

# Create insights script
cat > scripts/instagram_insights.py << 'PYEOF'
#!/usr/bin/env python3
"""
Instagram Insights - Performance reporting and analytics
"""
import os
import json
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import argparse
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

load_dotenv()

class InstagramInsights:
    def __init__(self):
        self.access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
        self.ad_account_id = os.getenv('FACEBOOK_AD_ACCOUNT_ID')
        FacebookAdsApi.init(access_token=self.access_token)
        self.account = AdAccount(f'act_{self.ad_account_id}')
    
    def get_campaign_insights(self, start_date, end_date, fields=None):
        """Get campaign insights for date range"""
        if fields is None:
            fields = [
                'campaign_name', 'campaign_id', 'impressions', 'reach',
                'clicks', 'ctr', 'spend', 'cpm', 'cpp', 'actions',
                'action_values', 'conversions', 'conversion_values'
            ]
        
        params = {
            'level': 'campaign',
            'fields': fields,
            'time_range': {'since': start_date, 'until': end_date},
            'time_increment': 1
        }
        
        insights = self.account.get_insights(params=params)
        return insights
    
    def generate_report(self, insights, output_format='csv'):
        """Generate performance report"""
        if not insights:
            return "No data available"
        
        data = []
        for insight in insights:
            row = insight.export_all_data()
            data.append(row)
        
        df = pd.DataFrame(data)
        
        if output_format == 'csv':
            return df.to_csv(index=False)
        elif output_format == 'json':
            return df.to_json(orient='records', indent=2)
        else:
            return df.to_string()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Instagram Insights')
    parser.add_argument('--start-date', default=(datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'),
                       help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', default=datetime.now().strftime('%Y-%m-%d'),
                       help='End date (YYYY-MM-DD)')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('--format', choices=['csv', 'json', 'table'], default='csv',
                       help='Output format')
    
    args = parser.parse_args()
    
    print(f"Fetching Instagram insights from {args.start_date} to {args.end_date}...")
    
    insights = InstagramInsights()
    data = insights.get_campaign_insights(args.start_date, args.end_date)
    
    report = insights.generate_report(data, args.format)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report saved to {args.output}")
    else:
        print(report)
PYEOF

# Create creative optimizer script
cat > scripts/instagram_creative_optimizer.py << 'PYEOF'
#!/usr/bin/env python3
"""
Instagram Creative Optimizer - Visual content optimization
"""
import os
import json
from dotenv import load_dotenv
import argparse
import requests
from PIL import Image
import io

load_dotenv()

class InstagramCreativeOptimizer:
    def __init__(self):
        self.access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
        self.instagram_account_id = os.getenv('INSTAGRAM_BUSINESS_ACCOUNT_ID')
    
    def analyze_creative_performance(self, creative_id):
        """Analyze performance of a specific creative"""
        url = f'https://graph.facebook.com/v18.0/{creative_id}/insights'
        params = {
            'access_token': self.access_token,
            'metric': 'engagement,impressions,reach'
        }
        
        response = requests.get(url, params=params)
        return response.json()
    
    def get_creative_recommendations(self, creative_data):
        """Get recommendations for creative optimization"""
        recommendations = []
        
        # Analyze aspect ratio
        if 'image_url' in creative_data:
            try:
                response = requests.get(creative_data['image_url'])
                img = Image.open(io.BytesIO(response.content))
                width, height = img.size
                aspect_ratio = width / height
                
                if aspect_ratio < 0.8 or aspect_ratio > 1.91:
                    recommendations.append({
                        'type': 'aspect_ratio',
                        'message': f'Aspect ratio {aspect_ratio:.2f} is outside optimal range (0.8-1.91)',
                        'suggestion': 'Use square (1:1) or vertical (4:5) formats for Instagram'
                    })
            except:
                pass
        
        # Check for call-to-action
        if 'call_to_action' not in creative_data:
            recommendations.append({
                'type': 'call_to_action',
                'message': 'No call-to-action specified',
                'suggestion': 'Add clear CTA like "Shop Now", "Learn More", or "Sign Up"'
            })
        
        # Check for mobile optimization
        recommendations.append({
            'type': 'mobile_optimization',
            'message': 'Ensure creative is mobile-optimized',
            'suggestion': 'Test on mobile devices, use larger text, clear visuals'
        })
        
        return recommendations

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Instagram Creative Optimizer')
    parser.add_argument('--creative-id', help='Creative ID to analyze')
    parser.add_argument('--creative-data', help='JSON string of creative data')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    optimizer = InstagramCreativeOptimizer()
    
    results = {}
    
    if args.creative_id:
        performance = optimizer.analyze_creative_performance(args.creative_id)
        results['performance'] = performance
    
    if args.creative_data:
        creative_data = json.loads(args.creative_data)
        recommendations = optimizer.get_creative_recommendations(creative_data)
        results['recommendations'] = recommendations
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {args.output}")
    else:
        print(json.dumps(results, indent=2))
PYEOF

# Create shopping script
cat > scripts/instagram_shopping.py << 'PYEOF'
#!/usr/bin/env python3
"""
Instagram Shopping - Social commerce automation
"""
import os
import json
import requests
from dotenv import load_dotenv
import argparse

load_dotenv()

class InstagramShopping:
    def __init__(self):
        self.access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
        self.instagram_account_id = os.getenv('INSTAGRAM_BUSINESS_ACCOUNT_ID')
        self.catalog_id = os.getenv('PRODUCT_CATALOG_ID')
    
    def get_product_catalog(self):
        """Get product catalog for Instagram shopping"""
        if not self.catalog_id:
            return {"error": "PRODUCT_CATALOG_ID not configured in .env"}
        
        url = f'https://graph.facebook.com/v18.0/{self.catalog_id}/products'
        params = {
            'access_token': self.access_token,
            'fields': 'id,name,description,price,image_url,url,availability'
        }
        
        response = requests.get(url, params=params)
        return response.json()
    
    def create_shopping_ad(self, product_id, ad_set_id):
        """Create shopping ad for product"""
        url = f'https://graph.facebook.com/v18.0/{self.instagram_account_id}/product_tags'
        
        params = {
            'access_token': self.access_token,
            'product_id': product_id,
            'ad_set_id': ad_set_id
        }
        
        response = requests.post(url, params=params)
        return response.json()
    
    def get_shopping_insights(self):
        """Get shopping performance insights"""
        url = f'https://graph.facebook.com/v18.0/{self.instagram_account_id}/insights'
        params = {
            'access_token': self.access_token,
            'metric': 'product_saves,product_clicks,checkouts_initiated,checkouts_completed',
            'period': 'days_28'
        }
        
        response = requests.get(url, params=params)
        return response.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Instagram Shopping')
    parser.add_argument('--action', choices=['get_catalog', 'create_ad', 'get_insights'],
                       help='Action to perform')
    parser.add_argument('--product-id', help='Product ID for shopping ad')
    parser.add_argument('--ad-set-id', help='Ad set ID for shopping ad')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    shopping = InstagramShopping()
    
    try:
        if args.action == 'get_catalog':
            result = shopping.get_product_catalog()
        elif args.action == 'create_ad':
            if not args.product_id or not args.ad_set_id:
                print("Error: --product-id and --ad-set-id required for create_ad")
                exit(1)
            result = shopping.create_shopping_ad(args.product_id, args.ad_set_id)
        elif args.action == 'get_insights':
            result = shopping.get_shopping_insights()
        else:
            result = {"error": "No action specified"}
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"Results saved to {args.output}")
        else:
            print(json.dumps(result, indent=2))
            
    except Exception as e:
        print(f"Error: {e}")
PYEOF

# Create package.json for Node.js version
cat > scripts/package.json << 'EOF'
{
  "name": "instagram-ads-mcp",
  "version": "1.0.0",
  "description": "Instagram Ads MCP integration",
  "main": "instagram_ads_api.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "dependencies": {
    "axios": "^1.6.0",
    "dotenv": "^16.3.0",
    "facebook-nodejs-business-sdk": "^18.0.0"
  },
  "keywords": ["instagram", "ads", "mcp", "social", "marketing", "shopping"],
  "author": "SkillBuilder",
  "license": "MIT"
}
