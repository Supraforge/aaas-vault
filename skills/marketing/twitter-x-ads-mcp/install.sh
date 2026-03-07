#!/bin/bash
# Twitter/X Ads MCP Skill - Installation

echo "🚀 Installing Twitter/X Ads MCP Skill dependencies..."

# Python dependencies
echo "📦 Installing Python packages..."
pip install tweepy pandas python-dotenv requests tweepy-auth

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
cat > scripts/twitter_ads_manager.py << 'PYEOF'
#!/usr/bin/env python3
"""
Twitter/X Ads Manager - Core campaign operations using Twitter Ads API
"""
import os
import json
import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import argparse
import sys
import tweepy

# Load environment variables
load_dotenv()

class TwitterAdsManager:
    def __init__(self):
        self.api_key = os.getenv('TWITTER_API_KEY')
        self.api_secret = os.getenv('TWITTER_API_SECRET')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_secret = os.getenv('TWITTER_ACCESS_SECRET')
        self.ads_account_id = os.getenv('TWITTER_ADS_ACCOUNT_ID')
        
        # Initialize Twitter API v2 client
        self.client = tweepy.Client(
            consumer_key=self.api_key,
            consumer_secret=self.api_secret,
            access_token=self.access_token,
            access_token_secret=self.access_secret
        )
        
        # Initialize Twitter Ads API
        self.ads_base_url = 'https://ads-api.twitter.com/12'
        self.ads_headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
    
    def create_campaign(self, name, objective, daily_budget, **kwargs):
        """Create a new Twitter Ads campaign"""
        url = f'{self.ads_base_url}/accounts/{self.ads_account_id}/campaigns'
        
        payload = {
            'name': name,
            'objective': objective,
            'daily_budget_amount_local_micro': daily_budget * 1000000,  # Convert to micros
            'status': 'ACTIVE',
            **kwargs
        }
        
        response = requests.post(url, headers=self.ads_headers, json=payload)
        return response.json()
    
    def get_campaigns(self):
        """Get all campaigns for account"""
        url = f'{self.ads_base_url}/accounts/{self.ads_account_id}/campaigns'
        
        response = requests.get(url, headers=self.ads_headers)
        return response.json()
    
    def create_promoted_tweet(self, campaign_id, tweet_id, **kwargs):
        """Create promoted tweet within campaign"""
        url = f'{self.ads_base_url}/accounts/{self.ads_account_id}/promoted_tweets'
        
        payload = {
            'campaign_id': campaign_id,
            'tweet_id': tweet_id,
            'status': 'ACTIVE',
            **kwargs
        }
        
        response = requests.post(url, headers=self.ads_headers, json=payload)
        return response.json()
    
    def create_tweet(self, text, **kwargs):
        """Create a new tweet"""
        try:
            response = self.client.create_tweet(text=text, **kwargs)
            return response.data
        except Exception as e:
            return {'error': str(e)}
    
    def get_analytics(self, entity_type, entity_ids, metrics, **kwargs):
        """Get analytics for campaigns, line items, or promoted tweets"""
        url = f'{self.ads_base_url}/stats/accounts/{self.ads_account_id}'
        
        params = {
            'entity': entity_type,
            'entity_ids': ','.join(entity_ids),
            'metric_groups': ','.join(metrics),
            'granularity': 'DAY',
            'placement': 'ALL_ON_TWITTER',
            **kwargs
        }
        
        response = requests.get(url, headers=self.ads_headers, params=params)
        return response.json()
    
    def get_tweet_engagement(self, tweet_id):
        """Get engagement metrics for a tweet"""
        url = f'https://api.twitter.com/2/tweets/{tweet_id}'
        
        params = {
            'tweet.fields': 'public_metrics,organic_metrics',
            'expansions': 'author_id'
        }
        
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        
        response = requests.get(url, headers=headers, params=params)
        return response.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Twitter/X Ads Manager')
    parser.add_argument('--action', required=True,
                       choices=['create_campaign', 'get_campaigns', 'create_tweet',
                                'create_promoted_tweet', 'get_analytics', 'get_tweet_engagement'],
                       help='Action to perform')
    parser.add_argument('--name', help='Campaign or tweet name')
    parser.add_argument('--objective', help='Campaign objective')
    parser.add_argument('--daily-budget', type=float, help='Daily budget in USD')
    parser.add_argument('--campaign-id', help='Campaign ID')
    parser.add_argument('--tweet-id', help='Tweet ID')
    parser.add_argument('--text', help='Tweet text')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    manager = TwitterAdsManager()
    
    try:
        if args.action == 'create_campaign':
            result = manager.create_campaign(
                name=args.name,
                objective=args.objective or 'WEBSITE_CLICKS',
                daily_budget=args.daily_budget or 10.0
            )
        elif args.action == 'get_campaigns':
            result = manager.get_campaigns()
        elif args.action == 'create_tweet':
            result = manager.create_tweet(text=args.text or 'Test tweet from Twitter Ads MCP Skill')
        elif args.action == 'create_promoted_tweet':
            if not args.campaign_id or not args.tweet_id:
                print("Error: --campaign-id and --tweet-id required for create_promoted_tweet")
                exit(1)
            result = manager.create_promoted_tweet(args.campaign_id, args.tweet_id)
        elif args.action == 'get_analytics':
            # Example: Get analytics for all campaigns
            campaigns = manager.get_campaigns()
            if 'data' in campaigns:
                campaign_ids = [str(c['id']) for c in campaigns['data']]
                result = manager.get_analytics(
                    entity_type='CAMPAIGN',
                    entity_ids=campaign_ids,
                    metrics=['ENGAGEMENT', 'BILLING', 'VIDEO']
                )
            else:
                result = campaigns
        elif args.action == 'get_tweet_engagement':
            if not args.tweet_id:
                print("Error: --tweet-id required for get_tweet_engagement")
                exit(1)
            result = manager.get_tweet_engagement(args.tweet_id)
        
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
cat > scripts/twitter_analytics.py << 'PYEOF'
#!/usr/bin/env python3
"""
Twitter/X Analytics - Performance reporting and insights
"""
import os
import json
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import argparse
import requests

load_dotenv()

class TwitterAnalytics:
    def __init__(self):
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.ads_account_id = os.getenv('TWITTER_ADS_ACCOUNT_ID')
        self.ads_base_url = 'https://ads-api.twitter.com/12'
        self.ads_headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
    
    def get_campaign_performance(self, start_date, end_date):
        """Get campaign performance for date range"""
        # First get all campaigns
        url = f'{self.ads_base_url}/accounts/{self.ads_account_id}/campaigns'
        response = requests.get(url, headers=self.ads_headers)
        campaigns = response.json()
        
        if 'data' not in campaigns:
            return []
        
        campaign_ids = [str(c['id']) for c in campaigns['data']]
        
        # Get analytics for campaigns
        analytics_url = f'{self.ads_base_url}/stats/accounts/{self.ads_account_id}'
        params = {
            'entity': 'CAMPAIGN',
            'entity_ids': ','.join(campaign_ids),
            'metric_groups': 'ENGAGEMENT,BILLING,VIDEO,CONVERSION',
            'granularity': 'DAY',
            'placement': 'ALL_ON_TWITTER',
            'start_time': start_date + 'T00:00:00Z',
            'end_time': end_date + 'T23:59:59Z'
        }
        
        analytics_response = requests.get(analytics_url, headers=self.ads_headers, params=params)
        analytics_data = analytics_response.json()
        
        # Combine campaign info with analytics
        results = []
        for campaign in campaigns['data']:
            campaign_id = str(campaign['id'])
            campaign_analytics = None
            
            if 'data' in analytics_data:
                for data in analytics_data['data']:
                    if data['id'] == campaign_id:
                        campaign_analytics = data
                        break
            
            result = {
                'campaign_id': campaign_id,
                'campaign_name': campaign.get('name', ''),
                'objective': campaign.get('objective', ''),
                'status': campaign.get('status', ''),
                'daily_budget': campaign.get('daily_budget_amount_local_micro', 0) / 1000000,
                'analytics': campaign_analytics
            }
            results.append(result)
        
        return results
    
    def generate_report(self, performance_data, output_format='csv'):
        """Generate performance report"""
        if not performance_data:
            return "No data available"
        
        # Flatten data for CSV
        flat_data = []
        for item in performance_data:
            flat_item = {
                'campaign_id': item['campaign_id'],
                'campaign_name': item['campaign_name'],
                'objective': item['objective'],
                'status': item['status'],
                'daily_budget': item['daily_budget']
            }
            
            if item['analytics'] and 'id_data' in item['analytics']:
                for id_data in item['analytics']['id_data']:
                    if 'metrics' in id_data:
                        for metric, value in id_data['metrics'].items():
                            flat_item[metric] = value
            
            flat_data.append(flat_item)
        
        df = pd.DataFrame(flat_data)
        
        if output_format == 'csv':
            return df.to_csv(index=False)
        elif output_format == 'json':
            return df.to_json(orient='records', indent=2)
        else:
            return df.to_string()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Twitter/X Analytics')
    parser.add_argument('--start-date', default=(datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'),
                       help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', default=datetime.now().strftime('%Y-%m-%d'),
                       help='End date (YYYY-MM-DD)')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('--format', choices=['csv', 'json', 'table'], default='csv',
                       help='Output format')
    
    args = parser.parse_args()
    
    print(f"Fetching Twitter/X analytics from {args.start_date} to {args.end_date}...")
    
    analytics = TwitterAnalytics()
    data = analytics.get_campaign_performance(args.start_date, args.end_date)
    
    report = analytics.generate_report(data, args.format)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report saved to {args.output}")
    else:
        print(report)
PYEOF

# Create engagement script
cat > scripts/twitter_engagement.py << 'PYEOF'
#!/usr/bin/env python3
"""
Twitter/X Engagement - Real-time conversation management
"""
import os
import json
import tweepy
from dotenv import load_dotenv
import argparse
import time
from datetime import datetime

load_dotenv()

class TwitterEngagement:
    def __init__(self):
        self.api_key = os.getenv('TWITTER_API_KEY')
        self.api_secret = os.getenv('TWITTER_API_SECRET')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_secret = os.getenv('TWITTER_ACCESS_SECRET')
        
        # Initialize Twitter API v2 client
        self.client = tweepy.Client(
            consumer_key=self.api_key,
            consumer_secret=self.api_secret,
            access_token=self.access_token,
            access_token_secret=self.access_secret
        )
        
        # Initialize OAuth1 for streaming
        self.auth = tweepy.OAuth1UserHandler(
            self.api_key, self.api_secret,
            self.access_token, self.access_secret
        )
        self.api = tweepy.API(self.auth)
    
    def monitor_mentions(self, keywords=None, duration_minutes=5):
        """Monitor mentions and keywords in real-time"""
        class MentionStream(tweepy.StreamingClient):
            def __init__(self, bearer_token, callback):
                super().__init__(bearer_token)
                self.callback = callback
                self.tweets = []
            
            def on_tweet(self, tweet):
                self.tweets.append(tweet)
                self.callback(tweet)
            
            def on_error(self, status):
                print(f"Stream error: {status}")
        
        stream = MentionStream(bearer_token=self.access_token, callback=self.process_mention)
        
        # Add rules for monitoring
        if keywords:
            for keyword in keywords:
                stream.add_rules(tweepy.StreamRule(keyword))
        
        # Start streaming
        print(f"Monitoring mentions for {duration_minutes} minutes...")
        stream.filter()
        
        # Stop after duration
        time.sleep(duration_minutes * 60)
        stream.disconnect()
        
        return stream.tweets
    
    def process_mention(self, tweet):
        """Process incoming mention"""
        print(f"New mention: {tweet.text}")
        print(f"From: {tweet.author_id}")
        print(f"Time: {datetime.now()}")
        print("-" * 50)
        
        # Example: Auto-reply to mentions
        # reply_text = f"Thanks for mentioning us! We'll get back to you soon. #CustomerService"
        # self.client.create_tweet(text=reply_text, in_reply_to_tweet_id=tweet.id)
    
    def get_conversation(self, tweet_id):
        """Get conversation thread for a tweet"""
        conversation = self.client.get_tweet(
            tweet_id,
            expansions=['referenced_tweets.id', 'in_reply_to_user_id'],
            tweet_fields=['conversation_id', 'author_id', 'created_at', 'public_metrics']
        )
        return conversation
    
    def analyze_sentiment(self, text):
        """Simple sentiment analysis (basic implementation)"""
        positive_words = ['great', 'good', 'excellent', 'awesome', 'love', 'thanks', 'thank']
        negative_words = ['bad', 'poor', 'terrible', 'awful', 'hate', 'disappointed', 'angry']
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        else:
            return 'neutral'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Twitter/X Engagement')
    parser.add_argument('--action', choices=['monitor', 'get_conversation', 'analyze_sentiment'],
                       help='Action to perform')
    parser.add_argument('--keywords', help='Comma-separated keywords to monitor')
    parser.add_argument('--duration', type=int, default=5, help='Monitoring duration in minutes')
    parser.add_argument('--tweet-id', help='Tweet ID for conversation analysis')
    parser.add_argument('--text', help='Text for sentiment analysis')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    engagement = TwitterEngagement()
    
    try:
        if args.action == 'monitor':
            keywords = args.keywords.split(',') if args.keywords else None
            tweets = engagement.monitor_mentions(keywords, args.duration)
            result = {
                'monitored_tweets': len(tweets),
                'tweets': [{'id': t.id, 'text': t.text, 'author_id': t.author_id} for t in tweets]
            }
        elif args.action == 'get_conversation':
            if not args.tweet_id:
                print("Error: --tweet-id required for get_conversation")
                exit(1)
            conversation = engagement.get_conversation(args.tweet_id)
            result = conversation.data if conversation.data else {'error': 'No conversation found'}
        elif args.action == 'analyze_sentiment':
            if not args.text:
                print("Error: --text required for analyze_sentiment")
                exit(1)
            sentiment = engagement.analyze_sentiment(args.text)
            result = {'text': args.text, 'sentiment': sentiment}
        else:
            result = {'error': 'No action specified'}
        
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
  "name": "twitter-x-ads-mcp",
  "version": "1.0.0",
  "description": "Twitter/X Ads MCP integration",
  "main": "twitter_ads_api.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "dependencies": {
    "axios": "^1.6.0",
    "dotenv": "^16.3.0",
    "twitter-api-v2": "^1.15.0"
  },
  "keywords": ["twitter", "x", "ads", "mcp", "social", "marketing", "engagement"],
  "author": "SkillBuilder",
  "license": "MIT"
}
