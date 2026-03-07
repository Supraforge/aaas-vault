#!/bin/bash
# Pinterest Ads MCP Skill - Installation

echo "🚀 Installing Pinterest Ads MCP Skill dependencies..."

# Python dependencies
echo "📦 Installing Python packages..."
pip install requests pandas python-dotenv

# Node.js dependencies (optional)
if command -v npm &> /dev/null && [ -f "scripts/package.json" ]; then
    echo "📦 Installing Node.js packages..."
    cd scripts
    npm install
    cd ..
fi

# Create scripts directory if it doesn't exist
mkdir -p scripts

# Create Python scripts
cat > scripts/pinterest_ads_manager.py << 'PYEOF'
#!/usr/bin/env python3
"""
Pinterest Ads Manager - Core campaign operations
"""
import os
import json
import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import argparse
import sys

# Load environment variables
load_dotenv()

PINTEREST_ACCESS_TOKEN = os.getenv('PINTEREST_ACCESS_TOKEN')
PINTEREST_AD_ACCOUNT_ID = os.getenv('PINTEREST_AD_ACCOUNT_ID')
API_BASE_URL = 'https://api.pinterest.com/v5'

class PinterestAdsManager:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {PINTEREST_ACCESS_TOKEN}',
            'Content-Type': 'application/json'
        })
    
    def create_campaign(self, name, objective, status='ACTIVE', budget=1000, **kwargs):
        """Create a new Pinterest campaign"""
        url = f'{API_BASE_URL}/ad_accounts/{PINTEREST_AD_ACCOUNT_ID}/campaigns'
        
        payload = {
            'name': name,
            'objective_type': objective,
            'status': status,
            'budget': budget,
            **kwargs
        }
        
        response = self.session.post(url, json=payload)
        return response.json()
    
    def get_campaigns(self, page_size=100):
        """Get all campaigns for account"""
        url = f'{API_BASE_URL}/ad_accounts/{PINTEREST_AD_ACCOUNT_ID}/campaigns'
        params = {'page_size': page_size}
        
        response = self.session.get(url, params=params)
        return response.json()
    
    def create_ad_group(self, campaign_id, name, budget, targeting_spec, **kwargs):
        """Create ad group within campaign"""
        url = f'{API_BASE_URL}/ad_accounts/{PINTEREST_AD_ACCOUNT_ID}/ad_groups'
        
        payload = {
            'campaign_id': campaign_id,
            'name': name,
            'budget': budget,
            'targeting_spec': targeting_spec,
            **kwargs
        }
        
        response = self.session.post(url, json=payload)
        return response.json()
    
    def create_ad(self, ad_group_id, pin_id, **kwargs):
        """Create ad within ad group"""
        url = f'{API_BASE_URL}/ad_accounts/{PINTEREST_AD_ACCOUNT_ID}/ads'
        
        payload = {
            'ad_group_id': ad_group_id,
            'pin_id': pin_id,
            **kwargs
        }
        
        response = self.session.post(url, json=payload)
        return response.json()
    
    def get_analytics(self, entity_type, entity_ids, start_date, end_date, columns):
        """Get analytics for campaigns, ad groups, or ads"""
        url = f'{API_BASE_URL}/ad_accounts/{PINTEREST_AD_ACCOUNT_ID}/analytics'
        
        params = {
            'entity_type': entity_type,
            'entity_ids': entity_ids,
            'start_date': start_date,
            'end_date': end_date,
            'columns': columns,
            'granularity': 'DAY'
        }
        
        response = self.session.get(url, params=params)
        return response.json()
    
    def get_pins(self, board_id=None):
        """Get pins for account or specific board"""
        url = f'{API_BASE_URL}/pins'
        params = {}
        if board_id:
            params['board_id'] = board_id
        
        response = self.session.get(url, params=params)
        return response.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pinterest Ads Manager')
    parser.add_argument('--action', required=True, 
                       choices=['create_campaign', 'get_campaigns', 'create_ad_group', 
                                'create_ad', 'get_analytics', 'get_pins'],
                       help='Action to perform')
    parser.add_argument('--name', help='Campaign or ad group name')
    parser.add_argument('--objective', help='Campaign objective')
    parser.add_argument('--campaign_id', help='Campaign ID')
    parser.add_argument('--ad_group_id', help='Ad group ID')
    parser.add_argument('--pin_id', help='Pin ID')
    parser.add_argument('--budget', type=float, help='Budget amount')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    manager = PinterestAdsManager()
    
    try:
        if args.action == 'create_campaign':
            result = manager.create_campaign(
                name=args.name,
                objective=args.objective,
                budget=args.budget or 1000
            )
        elif args.action == 'get_campaigns':
            result = manager.get_campaigns()
        elif args.action == 'create_ad_group':
            result = manager.create_ad_group(
                campaign_id=args.campaign_id,
                name=args.name,
                budget=args.budget or 100,
                targeting_spec={}
            )
        elif args.action == 'create_ad':
            result = manager.create_ad(
                ad_group_id=args.ad_group_id,
                pin_id=args.pin_id
            )
        elif args.action == 'get_analytics':
            # Default to last 7 days
            end_date = datetime.now().strftime('%Y-%m-%d')
            start_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
            result = manager.get_analytics(
                entity_type='CAMPAIGN',
                entity_ids='all',
                start_date=start_date,
                end_date=end_date,
                columns=['IMPRESSIONS', 'CLICKS', 'SPEND', 'CPC']
            )
        elif args.action == 'get_pins':
            result = manager.get_pins()
        
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

# Create analytics script
cat > scripts/pinterest_ads_analytics.py << 'PYEOF'
#!/usr/bin/env python3
"""
Pinterest Ads Analytics - Performance reporting
"""
import os
import json
import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import argparse

load_dotenv()

PINTEREST_ACCESS_TOKEN = os.getenv('PINTEREST_ACCESS_TOKEN')
PINTEREST_AD_ACCOUNT_ID = os.getenv('PINTEREST_AD_ACCOUNT_ID')
API_BASE_URL = 'https://api.pinterest.com/v5'

def get_campaign_performance(start_date, end_date):
    """Get campaign performance metrics"""
    headers = {
        'Authorization': f'Bearer {PINTEREST_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    url = f'{API_BASE_URL}/ad_accounts/{PINTEREST_AD_ACCOUNT_ID}/analytics'
    params = {
        'entity_type': 'CAMPAIGN',
        'entity_ids': 'all',
        'start_date': start_date,
        'end_date': end_date,
        'columns': ['IMPRESSIONS', 'CLICKS', 'SPEND', 'CPC', 'CTR', 'CONVERSIONS'],
        'granularity': 'DAY'
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def generate_report(data, output_format='csv'):
    """Generate performance report"""
    if not data.get('data'):
        return "No data available"
    
    df = pd.DataFrame(data['data'])
    
    if output_format == 'csv':
        return df.to_csv(index=False)
    elif output_format == 'json':
        return df.to_json(orient='records', indent=2)
    else:
        return df.to_string()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pinterest Ads Analytics')
    parser.add_argument('--start-date', default=(datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'),
                       help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', default=datetime.now().strftime('%Y-%m-%d'),
                       help='End date (YYYY-MM-DD)')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('--format', choices=['csv', 'json', 'table'], default='csv',
                       help='Output format')
    
    args = parser.parse_args()
    
    print(f"Fetching analytics from {args.start_date} to {args.end_date}...")
    data = get_campaign_performance(args.start_date, args.end_date)
    
    report = generate_report(data, args.format)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report saved to {args.output}")
    else:
        print(report)
PYEOF

# Create optimizer script
cat > scripts/pinterest_ads_optimizer.py << 'PYEOF'
#!/usr/bin/env python3
"""
Pinterest Ads Optimizer - Automated campaign optimization
"""
import os
import json
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import argparse

load_dotenv()

PINTEREST_ACCESS_TOKEN = os.getenv('PINTEREST_ACCESS_TOKEN')
PINTEREST_AD_ACCOUNT_ID = os.getenv('PINTEREST_AD_ACCOUNT_ID')
API_BASE_URL = 'https://api.pinterest.com/v5'

def optimize_bids(campaign_id, target_cpc=None):
    """Optimize bids based on performance"""
    headers = {
        'Authorization': f'Bearer {PINTEREST_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    # Get campaign performance
    url = f'{API_BASE_URL}/ad_accounts/{PINTEREST_AD_ACCOUNT_ID}/analytics'
    params = {
        'entity_type': 'CAMPAIGN',
        'entity_ids': campaign_id,
        'start_date': (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d'),
        'end_date': datetime.now().strftime('%Y-%m-%d'),
        'columns': ['SPEND', 'CLICKS', 'CONVERSIONS', 'CPC'],
        'granularity': 'DAY'
    }
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    if not data.get('data'):
        return {"status": "no_data", "message": "No performance data available"}
    
    # Calculate optimization recommendations
    # This is a simplified example - real implementation would use more sophisticated logic
    recommendations = []
    
    return {
        "status": "success",
        "campaign_id": campaign_id,
        "recommendations": recommendations,
        "data_summary": data.get('data', [])[0] if data.get('data') else {}
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pinterest Ads Optimizer')
    parser.add_argument('--campaign-id', required=True, help='Campaign ID to optimize')
    parser.add_argument('--target-cpc', type=float, help='Target CPC for optimization')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    result = optimize_bids(args.campaign_id, args.target_cpc)
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"Optimization results saved to {args.output}")
    else:
        print(json.dumps(result, indent=2))
PYEOF

# Create package.json for Node.js version
cat > scripts/package.json << 'EOF'
{
  "name": "pinterest-ads-mcp",
  "version": "1.0.0",
  "description": "Pinterest Ads MCP integration",
  "main": "pinterest_ads_api.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "dependencies": {
    "axios": "^1.6.0",
    "dotenv": "^16.3.0"
  },
  "keywords": ["pinterest", "ads", "mcp", "marketing", "automation"],
  "author": "SkillBuilder",
  "license": "MIT"
}
