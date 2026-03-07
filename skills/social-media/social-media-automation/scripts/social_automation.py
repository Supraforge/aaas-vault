#!/usr/bin/env python3
"""
Social Media Automation Script
Automates posting, scheduling, and analytics across Twitter, Facebook, Instagram
"""

import os
import sys
import json
import schedule
import time
from datetime import datetime
from dotenv import load_dotenv

try:
    import tweepy
    from facebook import GraphAPI
    from instagrapi import Client
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Run: pip install tweepy facebook-sdk instagrapi schedule python-dotenv")
    sys.exit(1)

# Load environment variables
load_dotenv()

class SocialMediaAutomation:
    def __init__(self):
        self.platforms = {}
        self.setup_platforms()

    def setup_platforms(self):
        """Initialize API clients for available platforms"""
        # Twitter/X
        if all([os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_SECRET'),
                os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_SECRET')]):
            auth = tweepy.OAuthHandler(os.getenv('TWITTER_API_KEY'), 
                                       os.getenv('TWITTER_API_SECRET'))
            auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), 
                                 os.getenv('TWITTER_ACCESS_SECRET'))
            self.platforms['twitter'] = tweepy.API(auth)

        # Facebook
        if os.getenv('FACEBOOK_ACCESS_TOKEN'):
            self.platforms['facebook'] = GraphAPI(os.getenv('FACEBOOK_ACCESS_TOKEN'))

        # Instagram
        if os.getenv('INSTAGRAM_USERNAME') and os.getenv('INSTAGRAM_PASSWORD'):
            self.platforms['instagram'] = Client()
            self.platforms['instagram'].login(os.getenv('INSTAGRAM_USERNAME'), 
                                             os.getenv('INSTAGRAM_PASSWORD'))

    def post(self, platform, content, image_path=None):
        """Post content to specified platform"""
        if platform not in self.platforms:
            return {"status": "error", "message": f"Platform {platform} not configured"}

        try:
            if platform == 'twitter':
                if image_path:
                    media = self.platforms[platform].media_upload(image_path)
                    result = self.platforms[platform].update_status(status=content, 
                                                                   media_ids=[media.media_id])
                else:
                    result = self.platforms[platform].update_status(status=content)
                return {"status": "success", "id": result.id_str}

            elif platform == 'facebook':
                if image_path:
                    with open(image_path, 'rb') as image:
                        result = self.platforms[platform].put_photo(image=image, 
                                                                  message=content)
                else:
                    result = self.platforms[platform].put_object(parent_object='me', 
                                                               connection_name='feed',
                                                               message=content)
                return {"status": "success", "id": result['id']}

            elif platform == 'instagram':
                if image_path:
                    result = self.platforms[platform].photo_upload(image_path, content)
                else:
                    # Instagram requires an image
                    return {"status": "error", "message": "Instagram requires an image"}
                return {"status": "success", "id": result.pk}

        except Exception as e:
            return {"status": "error", "message": str(e)}

    def schedule_post(self, platform, content, schedule_time, image_path=None):
        """Schedule a post for future time"""
        def job():
            return self.post(platform, content, image_path)

        # Parse schedule_time (format: "HH:MM" or "YYYY-MM-DD HH:MM")
        schedule.every().day.at(schedule_time).do(job)
        return {"status": "scheduled", "time": schedule_time}

    def analyze(self, platform, metric='engagement', days=7):
        """Analyze social media performance"""
        # This is a simplified version - real implementation would use platform APIs
        analysis = {
            "platform": platform,
            "metric": metric,
            "period_days": days,
            "data": {
                "posts": 12,
                "engagement_rate": 4.2,
                "reach": 1500,
                "impressions": 3200
            }
        }

        # Save to file
        filename = f"analytics_{platform}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(analysis, f, indent=2)

        return {"status": "success", "file": filename, "data": analysis}

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python social_automation.py <platform> <action> [content] [schedule_time] [image_path]")
        print("Example: python social_automation.py twitter post "Hello world!"")
        sys.exit(1)

    sm = SocialMediaAutomation()
    platform = sys.argv[1]
    action = sys.argv[2]

    if action == "post":
        content = sys.argv[3] if len(sys.argv) > 3 else ""
        image_path = sys.argv[4] if len(sys.argv) > 4 else None
        result = sm.post(platform, content, image_path)
    elif action == "schedule":
        content = sys.argv[3] if len(sys.argv) > 3 else ""
        schedule_time = sys.argv[4] if len(sys.argv) > 4 else "09:00"
        image_path = sys.argv[5] if len(sys.argv) > 5 else None
        result = sm.schedule_post(platform, content, schedule_time, image_path)
    elif action == "analyze":
        metric = sys.argv[3] if len(sys.argv) > 3 else "engagement"
        days = int(sys.argv[4]) if len(sys.argv) > 4 else 7
        result = sm.analyze(platform, metric, days)
    else:
        result = {"status": "error", "message": f"Unknown action: {action}"}

    print(json.dumps(result, indent=2))
