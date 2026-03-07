#!/bin/bash
# TikTok Ads MCP Skill - Installation

echo "🚀 Installing TikTok Ads MCP Skill dependencies..."

# Python dependencies
echo "📦 Installing Python packages..."
pip install TikTokApi pandas python-dotenv requests moviepy pillow numpy

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
cat > scripts/tiktok_ads_manager.py << 'PYEOF'
#!/usr/bin/env python3
"""
TikTok Ads Manager - Core campaign operations using TikTok Marketing API
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

class TikTokAdsManager:
    def __init__(self):
        self.access_token = os.getenv('TIKTOK_ACCESS_TOKEN')
        self.app_id = os.getenv('TIKTOK_APP_ID')
        self.app_secret = os.getenv('TIKTOK_SECRET')
        self.advertiser_id = os.getenv('TIKTOK_ADVERTISER_ID')
        
        self.base_url = 'https://business-api.tiktok.com/open_api/v1.3'
        self.headers = {
            'Access-Token': self.access_token,
            'Content-Type': 'application/json'
        }
    
    def create_campaign(self, name, objective, budget_mode, **kwargs):
        """Create a new TikTok Ads campaign"""
        url = f'{self.base_url}/campaign/create/'
        
        payload = {
            'advertiser_id': self.advertiser_id,
            'campaign_name': name,
            'objective_type': objective,
            'budget_mode': budget_mode,
            **kwargs
        }
        
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()
    
    def get_campaigns(self):
        """Get all campaigns for advertiser"""
        url = f'{self.base_url}/campaign/get/'
        
        params = {
            'advertiser_id': self.advertiser_id,
            'page': 1,
            'page_size': 100
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
    
    def create_ad(self, campaign_id, adgroup_id, creative_data, **kwargs):
        """Create a new ad within ad group"""
        url = f'{self.base_url}/ad/create/'
        
        payload = {
            'advertiser_id': self.advertiser_id,
            'campaign_id': campaign_id,
            'adgroup_id': adgroup_id,
            'creative': creative_data,
            **kwargs
        }
        
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()
    
    def get_insights(self, start_date, end_date, level='CAMPAIGN', **kwargs):
        """Get performance insights"""
        url = f'{self.base_url}/report/integrated/get/'
        
        payload = {
            'advertiser_id': self.advertiser_id,
            'service_type': 'AUCTION',
            'report_type': 'BASIC',
            'data_level': level,
            'dimensions': ['campaign_id', 'stat_time_day'],
            'metrics': [
                'spend', 'impressions', 'clicks', 'ctr',
                'conversion', 'cost_per_conversion',
                'video_play_actions', 'video_watched_2s',
                'video_watched_6s', 'average_video_play'
            ],
            'start_date': start_date,
            'end_date': end_date,
            **kwargs
        }
        
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()
    
    def upload_video(self, video_path):
        """Upload video to TikTok for ad creation"""
        # Initialize upload
        init_url = f'{self.base_url}/file/video/ad/upload/'
        init_payload = {
            'advertiser_id': self.advertiser_id
        }
        
        init_response = requests.post(init_url, headers=self.headers, json=init_payload)
        init_data = init_response.json()
        
        if init_data.get('code') != 0:
            return init_data
        
        upload_url = init_data['data']['upload_url']
        video_id = init_data['data']['video_id']
        
        # Upload video file
        with open(video_path, 'rb') as f:
            files = {'video': f}
            upload_response = requests.post(upload_url, files=files)
        
        # Confirm upload
        confirm_url = f'{self.base_url}/file/video/ad/upload/confirm/'
        confirm_payload = {
            'advertiser_id': self.advertiser_id,
            'video_id': video_id
        }
        
        confirm_response = requests.post(confirm_url, headers=self.headers, json=confirm_payload)
        return confirm_response.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TikTok Ads Manager')
    parser.add_argument('--action', required=True,
                       choices=['create_campaign', 'get_campaigns', 'create_ad', 'get_insights', 'upload_video'],
                       help='Action to perform')
    parser.add_argument('--name', help='Campaign name')
    parser.add_argument('--objective', help='Campaign objective')
    parser.add_argument('--budget-mode', choices=['BUDGET_MODE_DAY', 'BUDGET_MODE_TOTAL'], default='BUDGET_MODE_DAY',
                       help='Budget mode')
    parser.add_argument('--campaign-id', help='Campaign ID')
    parser.add_argument('--adgroup-id', help='Ad Group ID')
    parser.add_argument('--creative-data', help='JSON string with creative data')
    parser.add_argument('--start-date', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', help='End date (YYYY-MM-DD)')
    parser.add_argument('--level', choices=['CAMPAIGN', 'ADGROUP', 'AD'], default='CAMPAIGN',
                       help='Insights level')
    parser.add_argument('--video-path', help='Path to video file for upload')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    manager = TikTokAdsManager()
    
    try:
        if args.action == 'create_campaign':
            result = manager.create_campaign(
                name=args.name or 'New Campaign',
                objective=args.objective or 'CONVERSIONS',
                budget_mode=args.budget_mode
            )
        elif args.action == 'get_campaigns':
            result = manager.get_campaigns()
        elif args.action == 'create_ad':
            if not args.campaign_id or not args.adgroup_id or not args.creative_data:
                print("Error: --campaign-id, --adgroup-id, and --creative-data required for create_ad")
                exit(1)
            creative_data = json.loads(args.creative_data)
            result = manager.create_ad(args.campaign_id, args.adgroup_id, creative_data)
        elif args.action == 'get_insights':
            start_date = args.start_date or (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            end_date = args.end_date or datetime.now().strftime('%Y-%m-%d')
            result = manager.get_insights(start_date, end_date, args.level)
        elif args.action == 'upload_video':
            if not args.video_path:
                print("Error: --video-path required for upload_video")
                exit(1)
            result = manager.upload_video(args.video_path)
        
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
cat > scripts/tiktok_analytics.py << 'PYEOF'
#!/usr/bin/env python3
"""
TikTok Analytics - Performance reporting and insights
"""
import os
import json
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import argparse
import requests

load_dotenv()

class TikTokAnalytics:
    def __init__(self):
        self.access_token = os.getenv('TIKTOK_ACCESS_TOKEN')
        self.advertiser_id = os.getenv('TIKTOK_ADVERTISER_ID')
        self.base_url = 'https://business-api.tiktok.com/open_api/v1.3'
        self.headers = {
            'Access-Token': self.access_token,
            'Content-Type': 'application/json'
        }
    
    def get_campaign_performance(self, start_date, end_date):
        """Get campaign performance for date range"""
        url = f'{self.base_url}/report/integrated/get/'
        
        payload = {
            'advertiser_id': self.advertiser_id,
            'service_type': 'AUCTION',
            'report_type': 'BASIC',
            'data_level': 'CAMPAIGN',
            'dimensions': ['campaign_id', 'stat_time_day'],
            'metrics': [
                'spend', 'impressions', 'clicks', 'ctr',
                'conversion', 'cost_per_conversion',
                'video_play_actions', 'video_watched_2s',
                'video_watched_6s', 'average_video_play',
                'likes', 'comments', 'shares', 'follows'
            ],
            'start_date': start_date,
            'end_date': end_date,
            'page': 1,
            'page_size': 1000
        }
        
        response = requests.post(url, headers=self.headers, json=payload)
        data = response.json()
        
        if data.get('code') != 0:
            return []
        
        # Get campaign names
        campaigns_url = f'{self.base_url}/campaign/get/'
        campaigns_params = {
            'advertiser_id': self.advertiser_id,
            'page': 1,
            'page_size': 100
        }
        campaigns_response = requests.get(campaigns_url, headers=self.headers, params=campaigns_params)
        campaigns_data = campaigns_response.json()
        
        campaign_map = {}
        if campaigns_data.get('code') == 0:
            for campaign in campaigns_data.get('data', {}).get('list', []):
                campaign_map[campaign['campaign_id']] = campaign['campaign_name']
        
        # Process performance data
        results = []
        if data.get('data', {}).get('list'):
            for item in data['data']['list']:
                campaign_id = item['dimensions']['campaign_id']
                campaign_name = campaign_map.get(campaign_id, f'Campaign {campaign_id}')
                
                result = {
                    'campaign_id': campaign_id,
                    'campaign_name': campaign_name,
                    'date': item['dimensions']['stat_time_day'],
                    'spend': item.get('metrics', {}).get('spend', 0),
                    'impressions': item.get('metrics', {}).get('impressions', 0),
                    'clicks': item.get('metrics', {}).get('clicks', 0),
                    'ctr': item.get('metrics', {}).get('ctr', 0),
                    'conversions': item.get('metrics', {}).get('conversion', 0),
                    'cost_per_conversion': item.get('metrics', {}).get('cost_per_conversion', 0),
                    'video_plays': item.get('metrics', {}).get('video_play_actions', 0),
                    'video_watched_2s': item.get('metrics', {}).get('video_watched_2s', 0),
                    'video_watched_6s': item.get('metrics', {}).get('video_watched_6s', 0),
                    'average_video_play': item.get('metrics', {}).get('average_video_play', 0),
                    'likes': item.get('metrics', {}).get('likes', 0),
                    'comments': item.get('metrics', {}).get('comments', 0),
                    'shares': item.get('metrics', {}).get('shares', 0),
                    'follows': item.get('metrics', {}).get('follows', 0)
                }
                results.append(result)
        
        return results
    
    def generate_report(self, performance_data, output_format='csv'):
        """Generate performance report"""
        if not performance_data:
            return "No data available"
        
        df = pd.DataFrame(performance_data)
        
        if output_format == 'csv':
            return df.to_csv(index=False)
        elif output_format == 'json':
            return df.to_json(orient='records', indent=2)
        else:
            return df.to_string()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TikTok Analytics')
    parser.add_argument('--start-date', default=(datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'),
                       help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', default=datetime.now().strftime('%Y-%m-%d'),
                       help='End date (YYYY-MM-DD)')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('--format', choices=['csv', 'json', 'table'], default='csv',
                       help='Output format')
    
    args = parser.parse_args()
    
    print(f"Fetching TikTok analytics from {args.start_date} to {args.end_date}...")
    
    analytics = TikTokAnalytics()
    data = analytics.get_campaign_performance(args.start_date, args.end_date)
    
    report = analytics.generate_report(data, args.format)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report saved to {args.output}")
    else:
        print(report)
PYEOF

# Create content optimizer script
cat > scripts/tiktok_content_optimizer.py << 'PYEOF'
#!/usr/bin/env python3
"""
TikTok Content Optimizer - Video content analysis and optimization
"""
import os
import json
import requests
from dotenv import load_dotenv
import argparse
import sys
from datetime import datetime

load_dotenv()

class TikTokContentOptimizer:
    def __init__(self):
        self.access_token = os.getenv('TIKTOK_ACCESS_TOKEN')
        self.advertiser_id = os.getenv('TIKTOK_ADVERTISER_ID')
        self.base_url = 'https://business-api.tiktok.com/open_api/v1.3'
        self.headers = {
            'Access-Token': self.access_token,
            'Content-Type': 'application/json'
        }
    
    def analyze_video_performance(self, video_ids):
        """Analyze performance of specific videos"""
        url = f'{self.base_url}/report/integrated/get/'
        
        payload = {
            'advertiser_id': self.advertiser_id,
            'service_type': 'AUCTION',
            'report_type': 'BASIC',
            'data_level': 'AD',
            'dimensions': ['ad_id', 'stat_time_day'],
            'metrics': [
                'spend', 'impressions', 'clicks', 'ctr',
                'video_play_actions', 'video_watched_2s',
                'video_watched_6s', 'average_video_play',
                'likes', 'comments', 'shares', 'follows',
                'profile_visits', 'website_visits'
            ],
            'start_date': (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d'),
            'end_date': datetime.now().strftime('%Y-%m-%d'),
            'filter': {
                'ad_id': {'in': video_ids}
            },
            'page': 1,
            'page_size': 1000
        }
        
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()
    
    def get_trending_hashtags(self, category=None, limit=20):
        """Get trending hashtags"""
        # Note: This is a simplified example
        # TikTok doesn't have a direct API for trending hashtags
        # In production, you would use web scraping or third-party services
        
        # Mock data for demonstration
        trending_hashtags = [
            {'hashtag': '#fyp', 'views': '100B+', 'posts': '50M+'},
            {'hashtag': '#foryou', 'views': '80B+', 'posts': '40M+'},
            {'hashtag': '#viral', 'views': '50B+', 'posts': '30M+'},
            {'hashtag': '#trending', 'views': '40B+', 'posts': '20M+'},
            {'hashtag': '#comedy', 'views': '30B+', 'posts': '15M+'},
            {'hashtag': '#dance', 'views': '25B+', 'posts': '12M+'},
            {'hashtag': '#music', 'views': '20B+', 'posts': '10M+'},
            {'hashtag': '#fashion', 'views': '15B+', 'posts': '8M+'},
            {'hashtag': '#beauty', 'views': '12B+', 'posts': '6M+'},
            {'hashtag': '#gaming', 'views': '10B+', 'posts': '5M+'},
        ]
        
        if category:
            trending_hashtags = [h for h in trending_hashtags if category.lower() in h['hashtag'].lower()]
        
        return trending_hashtags[:limit]
    
    def optimize_video_metadata(self, title, description, tags):
        """Optimize video metadata for better performance"""
        recommendations = []
        
        # Title optimization
        if len(title) < 10:
            recommendations.append("Title is too short. Aim for 10-50 characters.")
        elif len(title) > 100:
            recommendations.append("Title is too long. Keep under 100 characters.")
        
        if '?' in title:
            recommendations.append("Good: Question in title can increase engagement.")
        
        # Description optimization
        if len(description) < 50:
            recommendations.append("Description is too short. Add more context.")
        elif len(description) > 2200:
            recommendations.append("Description is too long. Keep under 2200 characters.")
        
        # Hashtag optimization
        if len(tags) < 3:
            recommendations.append("Add more hashtags (3-5 recommended).")
        elif len(tags) > 10:
            recommendations.append("Too many hashtags. Use 3-5 most relevant ones.")
        
        # Check for trending hashtags
        trending = self.get_trending_hashtags()
        trending_tags = [h['hashtag'].replace('#', '') for h in trending]
        
        for tag in tags:
            if tag in trending_tags:
                recommendations.append(f"Good: #{tag} is trending!")
        
        return {
            'title': title,
            'title_length': len(title),
            'description': description,
            'description_length': len(description),
            'tags': tags,
            'tag_count': len(tags),
            'recommendations': recommendations,
            'trending_hashtags': trending[:5]
        }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TikTok Content Optimizer')
    parser.add_argument('--action', choices=['analyze_videos', 'trending_hashtags', 'optimize_metadata'],
                       help='Action to perform')
    parser.add_argument('--video-ids', help='Comma-separated video IDs for analysis')
    parser.add_argument('--category', help='Category for trending hashtags')
    parser.add_argument('--limit', type=int, default=20, help='Limit for trending hashtags')
    parser.add_argument('--title', help='Video title for optimization')
    parser.add_argument('--description', help='Video description for optimization')
    parser.add_argument('--tags', help='Comma-separated tags for optimization')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    optimizer = TikTokContentOptimizer()
    
    try:
        if args.action == 'analyze_videos':
            if not args.video_ids:
                print("Error: --video-ids required for analyze_videos")
                exit(1)
            video_ids = args.video_ids.split(',')
            result = optimizer.analyze_video_performance(video_ids)
        elif args.action == 'trending_hashtags':
            result = optimizer.get_trending_hashtags(args.category, args.limit)
        elif args.action == 'optimize_metadata':
            if not args.title or not args.description or not args.tags:
                print("Error: --title, --description, and --tags required for optimize_metadata")
                exit(1)
            tags = args.tags.split(',')
            result = optimizer.optimize_video_metadata(args.title, args.description, tags)
        else:
            result = {'error': 'No action specified'}
        
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

# Create package.json for Node.js version
cat > scripts/package.json << 'EOF'
{
  "name": "tiktok-ads-mcp",
  "version": "1.0.0",
  "description": "TikTok Ads MCP integration",
  "main": "tiktok_ads_api.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "dependencies": {
    "axios": "^1.6.0",
    "dotenv": "^16.3.0",
    "tiktok-api": "^1.0.0"
  },
  "keywords": ["tiktok", "ads", "mcp", "social", "marketing", "video", "influencer"],
  "author": "SkillBuilder",
  "license": "MIT"
}
