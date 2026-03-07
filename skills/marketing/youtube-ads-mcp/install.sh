#!/bin/bash
# YouTube Ads MCP Skill - Installation

echo "🚀 Installing YouTube Ads MCP Skill dependencies..."

# Python dependencies
echo "📦 Installing Python packages..."
pip install google-api-python-client google-auth-oauthlib google-auth-httplib2 oauth2client pandas python-dotenv requests google-ads

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
cat > scripts/youtube_ads_manager.py << 'PYEOF'
#!/usr/bin/env python3
"""
YouTube Ads Manager - Core campaign operations using Google Ads API
"""
import os
import json
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import argparse
import sys
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

# Load environment variables
load_dotenv()

class YouTubeAdsManager:
    def __init__(self):
        self.client_id = os.getenv('GOOGLE_CLIENT_ID')
        self.client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
        self.refresh_token = os.getenv('GOOGLE_REFRESH_TOKEN')
        self.developer_token = os.getenv('GOOGLE_DEVELOPER_TOKEN')
        self.customer_id = os.getenv('GOOGLE_ADS_ACCOUNT_ID')
        
        # Initialize Google Ads client
        self.client = GoogleAdsClient.load_from_dict({
            'developer_token': self.developer_token,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token,
            'use_proto_plus': True
        })
    
    def create_campaign(self, name, campaign_type, budget_amount, **kwargs):
        """Create a new YouTube campaign"""
        try:
            campaign_budget_service = self.client.get_service('CampaignBudgetService')
            campaign_service = self.client.get_service('CampaignService')
            
            # Create campaign budget
            budget_operation = self.client.get_type('CampaignBudgetOperation')
            budget = budget_operation.create
            budget.name = f'Budget for {name}'
            budget.delivery_method = self.client.enums.BudgetDeliveryMethodEnum.STANDARD
            budget.amount_micros = int(budget_amount * 1_000_000)
            
            budget_response = campaign_budget_service.mutate_campaign_budgets(
                customer_id=self.customer_id,
                operations=[budget_operation]
            )
            budget_id = budget_response.results[0].resource_name
            
            # Create campaign
            campaign_operation = self.client.get_type('CampaignOperation')
            campaign = campaign_operation.create
            campaign.name = name
            campaign.advertising_channel_type = self.client.enums.AdvertisingChannelTypeEnum.VIDEO
            campaign.status = self.client.enums.CampaignStatusEnum.PAUSED
            campaign.manual_cpc.enhanced_cpc_enabled = True
            campaign.campaign_budget = budget_id
            campaign.network_settings.target_youtube = True
            
            # Set campaign type
            if campaign_type == 'VIDEO_ACTION':
                campaign.video_brand_safety_suitability = self.client.enums.BrandSafetySuitabilityEnum.EXPANDED_INVENTORY
                campaign.manual_cpc = self.client.get_type('ManualCpc')
            elif campaign_type == 'VIDEO_NON_SKIPPABLE_IN_STREAM':
                campaign.video_brand_safety_suitability = self.client.enums.BrandSafetySuitabilityEnum.STANDARD_INVENTORY
                campaign.manual_cpv = self.client.get_type('ManualCpv')
            
            campaign_response = campaign_service.mutate_campaigns(
                customer_id=self.customer_id,
                operations=[campaign_operation]
            )
            
            return {
                'success': True,
                'campaign_id': campaign_response.results[0].resource_name,
                'budget_id': budget_id
            }
            
        except GoogleAdsException as ex:
            return {
                'success': False,
                'error': str(ex),
                'details': [{
                    'error_code': error.error_code,
                    'message': error.message,
                    'trigger': error.trigger.string_value
                } for error in ex.failure.errors]
            }
    
    def get_campaigns(self):
        """Get all YouTube campaigns"""
        try:
            ga_service = self.client.get_service('GoogleAdsService')
            
            query = '''
                SELECT
                    campaign.id,
                    campaign.name,
                    campaign.status,
                    campaign.advertising_channel_type,
                    metrics.impressions,
                    metrics.clicks,
                    metrics.cost_micros,
                    metrics.video_views,
                    metrics.average_cpm
                FROM campaign
                WHERE campaign.advertising_channel_type = "VIDEO"
                AND segments.date DURING LAST_30_DAYS
            '''
            
            response = ga_service.search(
                customer_id=self.customer_id,
                query=query
            )
            
            campaigns = []
            for row in response:
                campaign = row.campaign
                metrics = row.metrics
                
                campaigns.append({
                    'id': campaign.id,
                    'name': campaign.name,
                    'status': self.client.enums.CampaignStatusEnum(campaign.status).name,
                    'impressions': metrics.impressions,
                    'clicks': metrics.clicks,
                    'cost': metrics.cost_micros / 1_000_000,
                    'video_views': metrics.video_views,
                    'average_cpm': metrics.average_cpm / 1_000_000 if metrics.average_cpm else 0
                })
            
            return {
                'success': True,
                'campaigns': campaigns,
                'count': len(campaigns)
            }
            
        except GoogleAdsException as ex:
            return {
                'success': False,
                'error': str(ex)
            }
    
    def create_video_ad(self, campaign_id, video_id, **kwargs):
        """Create a video ad"""
        try:
            ad_group_service = self.client.get_service('AdGroupService')
            ad_group_ad_service = self.client.get_service('AdGroupAdService')
            
            # Create ad group
            ad_group_operation = self.client.get_type('AdGroupOperation')
            ad_group = ad_group_operation.create
            ad_group.name = f'Ad Group for {campaign_id}'
            ad_group.status = self.client.enums.AdGroupStatusEnum.ENABLED
            ad_group.campaign = campaign_id
            ad_group.type_ = self.client.enums.AdGroupTypeEnum.VIDEO_TRUE_VIEW_IN_STREAM
            
            ad_group_response = ad_group_service.mutate_ad_groups(
                customer_id=self.customer_id,
                operations=[ad_group_operation]
            )
            ad_group_id = ad_group_response.results[0].resource_name
            
            # Create video ad
            ad_group_ad_operation = self.client.get_type('AdGroupAdOperation')
            ad_group_ad = ad_group_ad_operation.create
            ad_group_ad.status = self.client.enums.AdGroupAdStatusEnum.ENABLED
            ad_group_ad.ad_group = ad_group_id
            
            # Set ad details
            video_ad = ad_group_ad.ad.video_ad
            video_ad.in_stream.action_button_label = 'LEARN_MORE'
            video_ad.in_stream.action_headline = 'Learn More'
            video_ad.in_stream.companion_banner.asset = 'INSERT_COMPANION_BANNER_ASSET_ID_HERE'
            video_ad.video.asset = f'INSERT_YOUTUBE_VIDEO_ASSET_ID_HERE'
            
            ad_response = ad_group_ad_service.mutate_ad_group_ads(
                customer_id=self.customer_id,
                operations=[ad_group_ad_operation]
            )
            
            return {
                'success': True,
                'ad_group_id': ad_group_id,
                'ad_id': ad_response.results[0].resource_name
            }
            
        except GoogleAdsException as ex:
            return {
                'success': False,
                'error': str(ex)
            }
    
    def get_insights(self, start_date, end_date):
        """Get campaign insights"""
        try:
            ga_service = self.client.get_service('GoogleAdsService')
            
            query = f'''
                SELECT
                    campaign.id,
                    campaign.name,
                    segments.date,
                    metrics.impressions,
                    metrics.clicks,
                    metrics.cost_micros,
                    metrics.video_views,
                    metrics.view_through_conversions,
                    metrics.average_cpm,
                    metrics.average_cpv,
                    metrics.ctr,
                    metrics.video_view_rate,
                    metrics.video_quartile_p100_rate
                FROM campaign
                WHERE campaign.advertising_channel_type = "VIDEO"
                AND segments.date BETWEEN "{start_date}" AND "{end_date}"
            '''
            
            response = ga_service.search(
                customer_id=self.customer_id,
                query=query
            )
            
            insights = []
            for row in response:
                campaign = row.campaign
                metrics = row.metrics
                segments = row.segments
                
                insights.append({
                    'campaign_id': campaign.id,
                    'campaign_name': campaign.name,
                    'date': segments.date,
                    'impressions': metrics.impressions,
                    'clicks': metrics.clicks,
                    'cost': metrics.cost_micros / 1_000_000,
                    'video_views': metrics.video_views,
                    'view_through_conversions': metrics.view_through_conversions,
                    'average_cpm': metrics.average_cpm / 1_000_000 if metrics.average_cpm else 0,
                    'average_cpv': metrics.average_cpv / 1_000_000 if metrics.average_cpv else 0,
                    'ctr': metrics.ctr,
                    'video_view_rate': metrics.video_view_rate,
                    'video_completion_rate': metrics.video_quartile_p100_rate
                })
            
            return {
                'success': True,
                'insights': insights,
                'period': f'{start_date} to {end_date}',
                'total_campaigns': len(set([i['campaign_id'] for i in insights]))
            }
            
        except GoogleAdsException as ex:
            return {
                'success': False,
                'error': str(ex)
            }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='YouTube Ads Manager')
    parser.add_argument('--action', required=True,
                       choices=['create_campaign', 'get_campaigns', 'create_video_ad', 'get_insights'],
                       help='Action to perform')
    parser.add_argument('--name', help='Campaign name')
    parser.add_argument('--campaign-type', choices=['VIDEO_ACTION', 'VIDEO_NON_SKIPPABLE_IN_STREAM'],
                       default='VIDEO_ACTION', help='Campaign type')
    parser.add_argument('--budget-amount', type=float, default=100.0, help='Daily budget amount')
    parser.add_argument('--campaign-id', help='Campaign ID for ad creation')
    parser.add_argument('--video-id', help='YouTube video ID')
    parser.add_argument('--start-date', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', help='End date (YYYY-MM-DD)')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    manager = YouTubeAdsManager()
    
    try:
        if args.action == 'create_campaign':
            result = manager.create_campaign(
                name=args.name or 'YouTube Campaign',
                campaign_type=args.campaign_type,
                budget_amount=args.budget_amount
            )
        elif args.action == 'get_campaigns':
            result = manager.get_campaigns()
        elif args.action == 'create_video_ad':
            if not args.campaign_id:
                print("Error: --campaign-id required for create_video_ad")
                exit(1)
            result = manager.create_video_ad(args.campaign_id, args.video_id)
        elif args.action == 'get_insights':
            start_date = args.start_date or (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            end_date = args.end_date or datetime.now().strftime('%Y-%m-%d')
            result = manager.get_insights(start_date, end_date)
        
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
cat > scripts/youtube_analytics.py << 'PYEOF'
#!/usr/bin/env python3
"""
YouTube Analytics - Performance reporting and insights
"""
import os
import json
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import argparse
import sys
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

load_dotenv()

class YouTubeAnalytics:
    def __init__(self):
        self.client_id = os.getenv('GOOGLE_CLIENT_ID')
        self.client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
        self.refresh_token = os.getenv('GOOGLE_REFRESH_TOKEN')
        
        # Initialize credentials
        self.creds = Credentials(
            token=None,
            refresh_token=self.refresh_token,
            token_uri='https://oauth2.googleapis.com/token',
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        
        # Refresh token if needed
        if self.creds.expired:
            self.creds.refresh(Request())
        
        # Build YouTube API service
        self.youtube = build('youtube', 'v3', credentials=self.creds)
    
    def get_channel_analytics(self, channel_id=None):
        """Get channel analytics"""
        try:
            # Get channel statistics
            if channel_id:
                request = self.youtube.channels().list(
                    part='statistics,snippet',
                    id=channel_id
                )
            else:
                request = self.youtube.channels().list(
                    part='statistics,snippet',
                    mine=True
                )
            
            response = request.execute()
            
            if not response.get('items'):
                return {'success': False, 'error': 'No channel found'}
            
            channel = response['items'][0]
            stats = channel['statistics']
            snippet = channel['snippet']
            
            return {
                'success': True,
                'channel_id': channel['id'],
                'channel_title': snippet['title'],
                'subscribers': int(stats.get('subscriberCount', 0)),
                'total_views': int(stats.get('viewCount', 0)),
                'total_videos': int(stats.get('videoCount', 0)),
                'created_at': snippet.get('publishedAt'),
                'country': snippet.get('country'),
                'description': snippet.get('description'),
                'custom_url': snippet.get('customUrl')
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_video_analytics(self, video_ids, start_date, end_date):
        """Get analytics for specific videos"""
        try:
            # This requires YouTube Analytics API which needs additional setup
            # For now, we'll use YouTube Data API for basic stats
            
            request = self.youtube.videos().list(
                part='statistics,contentDetails,snippet',
                id=','.join(video_ids)
            )
            
            response = request.execute()
            
            videos = []
            for item in response.get('items', []):
                stats = item['statistics']
                snippet = item['snippet']
                content = item['contentDetails']
                
                videos.append({
                    'video_id': item['id'],
                    'title': snippet['title'],
                    'published_at': snippet['publishedAt'],
                    'duration': content['duration'],
                    'views': int(stats.get('viewCount', 0)),
                    'likes': int(stats.get('likeCount', 0)),
                    'comments': int(stats.get('commentCount', 0)),
                    'favorites': int(stats.get('favoriteCount', 0)),
                    'description': snippet['description'],
                    'tags': snippet.get('tags', []),
                    'category_id': snippet['categoryId'],
                    'thumbnail_url': snippet['thumbnails']['high']['url']
                })
            
            return {
                'success': True,
                'videos': videos,
                'count': len(videos),
                'period': f'{start_date} to {end_date}'
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_top_videos(self, max_results=10):
        """Get top performing videos"""
        try:
            # Search for channel's videos
            channels_response = self.youtube.channels().list(
                part='contentDetails',
                mine=True
            ).execute()
            
            if not channels_response.get('items'):
                return {'success': False, 'error': 'No channel found'}
            
            uploads_playlist_id = channels_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
            
            # Get videos from uploads playlist
            playlist_items = []
            next_page_token = None
            
            while True:
                request = self.youtube.playlistItems().list(
                    part='snippet',
                    playlistId=uploads_playlist_id,
                    maxResults=50,
                    pageToken=next_page_token
                )
                response = request.execute()
                
                playlist_items.extend(response.get('items', []))
                next_page_token = response.get('nextPageToken')
                
                if not next_page_token or len(playlist_items) >= max_results:
                    break
            
            # Get video IDs
            video_ids = [item['snippet']['resourceId']['videoId'] for item in playlist_items[:max_results]]
            
            # Get video statistics
            videos_request = self.youtube.videos().list(
                part='statistics,snippet',
                id=','.join(video_ids)
            )
            videos_response = videos_request.execute()
            
            top_videos = []
            for item in videos_response.get('items', []):
                stats = item['statistics']
                snippet = item['snippet']
                
                top_videos.append({
                    'video_id': item['id'],
                    'title': snippet['title'],
                    'views': int(stats.get('viewCount', 0)),
                    'likes': int(stats.get('likeCount', 0)),
                    'comments': int(stats.get('commentCount', 0)),
                    'published_at': snippet['publishedAt'],
                    'thumbnail_url': snippet['thumbnails']['high']['url'],
                    'engagement_rate': (int(stats.get('likeCount', 0)) + int(stats.get('commentCount', 0))) / max(int(stats.get('viewCount', 1)), 1)
                })
            
            # Sort by views
            top_videos.sort(key=lambda x: x['views'], reverse=True)
            
            return {
                'success': True,
                'top_videos': top_videos,
                'total_videos_analyzed': len(top_videos)
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='YouTube Analytics')
    parser.add_argument('--action', required=True,
                       choices=['channel_analytics', 'video_analytics', 'top_videos'],
                       help='Action to perform')
    parser.add_argument('--channel-id', help='YouTube channel ID')
    parser.add_argument('--video-ids', help='Comma-separated video IDs')
    parser.add_argument('--start-date', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', help='End date (YYYY-MM-DD)')
    parser.add_argument('--max-results', type=int, default=10, help='Maximum results')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    analytics = YouTubeAnalytics()
    
    try:
        if args.action == 'channel_analytics':
            result = analytics.get_channel_analytics(args.channel_id)
        elif args.action == 'video_analytics':
            if not args.video_ids:
                print("Error: --video-ids required for video_analytics")
                exit(1)
            start_date = args.start_date or (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            end_date = args.end_date or datetime.now().strftime('%Y-%m-%d')
            video_ids = args.video_ids.split(',')
            result = analytics.get_video_analytics(video_ids, start_date, end_date)
        elif args.action == 'top_videos':
            result = analytics.get_top_videos(args.max_results)
        
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

# Create content optimizer script
cat > scripts/youtube_content_optimizer.py << 'PYEOF'
#!/usr/bin/env python3
"""
YouTube Content Optimizer - Video content analysis and optimization
"""
import os
import json
import re
from datetime import datetime
from dotenv import load_dotenv
import argparse
import sys
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

load_dotenv()

class YouTubeContentOptimizer:
    def __init__(self):
        self.client_id = os.getenv('GOOGLE_CLIENT_ID')
        self.client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
        self.refresh_token = os.getenv('GOOGLE_REFRESH_TOKEN')
        
        # Initialize credentials
        self.creds = Credentials(
            token=None,
            refresh_token=self.refresh_token,
            token_uri='https://oauth2.googleapis.com/token',
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        
        # Refresh token if needed
        if self.creds.expired:
            self.creds.refresh(Request())
        
        # Build YouTube API service
        self.youtube = build('youtube', 'v3', credentials=self.creds)
    
    def analyze_video_metadata(self, title, description, tags, category_id):
        """Analyze and optimize video metadata"""
        recommendations = []
        score = 100
        
        # Title analysis
        title_length = len(title)
        if title_length < 30:
            recommendations.append("Title is too short. Aim for 30-70 characters for better SEO.")
            score -= 10
        elif title_length > 100:
            recommendations.append("Title is too long. Keep under 100 characters for mobile display.")
            score -= 5
        
        # Check for keywords in title
        if not any(keyword in title.lower() for keyword in ['how to', 'tutorial', 'review', 'best', 'top']):
            recommendations.append("Consider adding action words like 'How to', 'Tutorial', or 'Review' to title.")
        
        # Description analysis
        desc_length = len(description)
        if desc_length < 200:
            recommendations.append("Description is too short. Add more context and keywords (aim for 200-5000 characters).")
            score -= 15
        elif desc_length > 5000:
            recommendations.append("Description is very long. Consider breaking into sections with timestamps.")
        
        # Check for timestamps in description
        if '0:00' in description or '00:00' in description:
            recommendations.append("Good: Timestamps found in description (improves user experience).")
            score += 5
        else:
            recommendations.append("Consider adding timestamps to description for longer videos.")
        
        # Tags analysis
        tag_count = len(tags)
        if tag_count < 5:
            recommendations.append(f"Add more tags (currently {tag_count}, aim for 10-15 relevant tags).")
            score -= 10
        elif tag_count > 30:
            recommendations.append(f"Too many tags ({tag_count}). YouTube recommends 10-15 most relevant tags.")
            score -= 5
        
        # Check for branded tags
        branded_tags = [tag for tag in tags if 'brand' in tag.lower() or 'channel' in tag.lower()]
        if not branded_tags:
            recommendations.append("Add branded tags with your channel name or brand.")
        
        # Category analysis
        category_names = {
            '1': 'Film & Animation',
            '2': 'Autos & Vehicles',
            '10': 'Music',
            '15': 'Pets & Animals',
            '17': 'Sports',
            '19': 'Travel & Events',
            '20': 'Gaming',
            '22': 'People & Blogs',
            '23': 'Comedy',
            '24': 'Entertainment',
            '25': 'News & Politics',
            '26': 'How-to & Style',
            '27': 'Education',
            '28': 'Science & Technology',
            '29': 'Non-profits & Activism'
        }
        
        category_name = category_names.get(str(category_id), f'Category {category_id}')
        
        return {
            'title': title,
            'title_length': title_length,
            'description': description,
            'description_length': desc_length,
            'tags': tags,
            'tag_count': tag_count,
            'category_id': category_id,
            'category_name': category_name,
            'recommendations': recommendations,
            'optimization_score': min(max(score, 0), 100),
            'grade': self._get_grade(score)
        }
    
    def _get_grade(self, score):
        """Convert score to letter grade"""
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    def get_trending_keywords(self, region_code='US', max_results=20):
        """Get trending keywords for a region"""
        try:
            # Get trending videos
            request = self.youtube.videos().list(
                part='snippet',
                chart='mostPopular',
                regionCode=region_code,
                maxResults=max_results
            )
            response = request.execute()
            
            trending_keywords = []
            for item in response.get('items', []):
                snippet = item['snippet']
                title = snippet['title']
                
                # Extract keywords from title
                words = re.findall(r'\b[A-Za-z]{3,}\b', title)
                for word in words:
                    word_lower = word.lower()
                    if word_lower not in ['the', 'and', 'for', 'with', 'this', 'that', 'what', 'how', 'why', 'when']:
                        trending_keywords.append(word_lower)
            
            # Count frequency
            from collections import Counter
            keyword_counts = Counter(trending_keywords)
            
            trending = [
                {'keyword': keyword, 'count': count}
                for keyword, count in keyword_counts.most_common(20)
            ]
            
            return {
                'success': True,
                'region': region_code,
                'trending_keywords': trending,
                'total_videos_analyzed': len(response.get('items', [])),
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def generate_thumbnail_ideas(self, title, category):
        """Generate thumbnail design ideas"""
        ideas = []
        
        # Based on category and title
        if 'tutorial' in title.lower() or 'how to' in title.lower():
            ideas.extend([
                'Before/After comparison',
                'Step-by-step numbered graphics',
                'Close-up of the result',
                'Person demonstrating the process'
            ])
        
        if 'review' in title.lower():
            ideas.extend([
                'Product close-up with rating',
                'Comparison of multiple products',
                'Person using the product',
                'Pros and cons list visually'
            ])
        
        if 'gaming' in category.lower():
            ideas.extend([
                'Game character close-up',
                'Action scene screenshot',
                'Game logo with exciting text',
                'Player reaction face'
            ])
        
        # General thumbnail best practices
        general_ideas = [
            'Bright, high-contrast colors',
            'Clear, readable text overlay',
            'Human face showing emotion',
            'Arrow or circle highlighting key element',
            'Minimal text (3-5 words max)',
            'Consistent branding (colors, logo)',
            'Mystery or curiosity element',
            'Number or percentage prominently displayed'
        ]
        
        ideas.extend(general_ideas)
        
        return {
            'title': title,
            'category': category,
            'thumbnail_ideas': list(set(ideas)),  # Remove duplicates
            'total_ideas': len(set(ideas))
        }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='YouTube Content Optimizer')
    parser.add_argument('--action', choices=['analyze_metadata', 'trending_keywords', 'thumbnail_ideas'],
                       help='Action to perform')
    parser.add_argument('--title', help='Video title for analysis')
    parser.add_argument('--description', help='Video description for analysis')
    parser.add_argument('--tags', help='Comma-separated tags for analysis')
    parser.add_argument('--category-id', default='27', help='YouTube category ID')
    parser.add_argument('--region-code', default='US', help='Region code for trending keywords')
    parser.add_argument('--max-results', type=int, default=20, help='Maximum results for trending keywords')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    optimizer = YouTubeContentOptimizer()
    
    try:
        if args.action == 'analyze_metadata':
            if not args.title or not args.description or not args.tags:
                print("Error: --title, --description, and --tags required for analyze_metadata")
                exit(1)
            tags = args.tags.split(',')
            result = optimizer.analyze_video_metadata(args.title, args.description, tags, args.category_id)
        elif args.action == 'trending_keywords':
            result = optimizer.get_trending_keywords(args.region_code, args.max_results)
        elif args.action == 'thumbnail_ideas':
            if not args.title or not args.category_id:
                print("Error: --title and --category-id required for thumbnail_ideas")
                exit(1)
            result = optimizer.generate_thumbnail_ideas(args.title, args.category_id)
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
  "name": "youtube-ads-mcp",
  "version": "1.0.0",
  "description": "YouTube Ads MCP integration",
  "main": "youtube_ads_api.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "dependencies": {
    "axios": "^1.6.0",
    "dotenv": "^16.3.0",
    "googleapis": "^128.0.0",
    "google-auth-library": "^9.0.0"
  },
  "keywords": ["youtube", "ads", "mcp", "video", "marketing", "analytics", "google"],
  "author": "SkillBuilder",
  "license": "MIT"
}
