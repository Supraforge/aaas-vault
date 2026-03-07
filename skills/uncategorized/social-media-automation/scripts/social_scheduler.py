#!/usr/bin/env python3
"""
Social Media Scheduler
Main script for scheduling and posting social media content
"""

import os
import sys
import json
import schedule
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any
import logging
from dotenv import load_dotenv

# Add scripts directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.platform_integration import PlatformManager
from scripts.content_generator import ContentGenerator
from scripts.utils import setup_logging, load_config

class SocialScheduler:
    """Main scheduler for social media automation"""

    def __init__(self):
        """Initialize scheduler with configuration"""
        load_dotenv()
        self.logger = setup_logging(__name__)
        self.config = load_config()

        # Initialize managers
        self.platform_manager = PlatformManager()
        self.content_generator = ContentGenerator()

        # Load content strategy
        self.strategy = self._load_strategy()

        # Schedule storage
        self.schedule = []

    def _load_strategy(self) -> Dict[str, Any]:
        """Load content strategy from file"""
        strategy_path = os.path.join('templates', 'content_strategy.json')
        if os.path.exists(strategy_path):
            with open(strategy_path, 'r') as f:
                return json.load(f)
        else:
            self.logger.warning(f"Strategy file not found: {strategy_path}")
            return self._default_strategy()

    def _default_strategy(self) -> Dict[str, Any]:
        """Create default content strategy"""
        return {
            "brand_voice": "professional",
            "target_audience": "general",
            "content_themes": ["industry news", "tips", "company updates"],
            "posting_frequency": {
                "twitter": "2/day",
                "linkedin": "1/day",
                "facebook": "1/day"
            }
        }

    def create_schedule(self, days: int = 30) -> List[Dict[str, Any]]:
        """Create social media schedule for specified number of days"""
        self.logger.info(f"Creating schedule for {days} days")

        schedule = []
        start_date = datetime.now()

        for day_offset in range(days):
            current_date = start_date + timedelta(days=day_offset)
            day_schedule = self._create_daily_schedule(current_date)
            schedule.extend(day_schedule)

        self.schedule = schedule
        self._save_schedule(schedule)

        return schedule

    def _create_daily_schedule(self, date: datetime) -> List[Dict[str, Any]]:
        """Create schedule for a single day"""
        day_schedule = []

        # Get optimal posting times for each platform
        posting_times = self._get_optimal_posting_times(date)

        for platform, times in posting_times.items():
            for post_time in times:
                # Generate content for this time slot
                content = self.content_generator.generate_post(
                    platform=platform,
                    theme=self._get_daily_theme(date),
                    time_of_day=post_time.strftime('%H:%M')
                )

                schedule_item = {
                    "date": date.strftime('%Y-%m-%d'),
                    "time": post_time.strftime('%H:%M'),
                    "platform": platform,
                    "content": content,
                    "status": "scheduled",
                    "timezone": os.getenv('TIMEZONE', 'UTC')
                }

                day_schedule.append(schedule_item)

        return day_schedule

    def _get_optimal_posting_times(self, date: datetime) -> Dict[str, List[datetime]]:
        """Calculate optimal posting times for each platform"""
        # This would use historical data and AI to determine best times
        # For now, use default times

        default_times = {
            "twitter": [
                datetime.combine(date.date(), datetime.strptime('09:00', '%H:%M').time()),
                datetime.combine(date.date(), datetime.strptime('12:00', '%H:%M').time()),
                datetime.combine(date.date(), datetime.strptime('17:00', '%H:%M').time())
            ],
            "linkedin": [
                datetime.combine(date.date(), datetime.strptime('10:00', '%H:%M').time())
            ],
            "facebook": [
                datetime.combine(date.date(), datetime.strptime('13:00', '%H:%M').time())
            ],
            "instagram": [
                datetime.combine(date.date(), datetime.strptime('11:00', '%H:%M').time())
            ]
        }

        return default_times

    def _get_daily_theme(self, date: datetime) -> str:
        """Get content theme for the day"""
        themes = self.strategy.get('content_themes', ['general'])
        day_index = date.weekday()  # 0=Monday, 6=Sunday
        return themes[day_index % len(themes)]

    def _save_schedule(self, schedule: List[Dict[str, Any]]):
        """Save schedule to file"""
        os.makedirs('data', exist_ok=True)
        schedule_path = os.path.join('data', f'schedule_{datetime.now().strftime("%Y%m%d")}.json')

        with open(schedule_path, 'w') as f:
            json.dump(schedule, f, indent=2, default=str)

        self.logger.info(f"Schedule saved to {schedule_path}")

    def execute_schedule(self):
        """Execute the current schedule"""
        self.logger.info("Executing social media schedule")

        for item in self.schedule:
            if item['status'] == 'scheduled':
                try:
                    self._post_content(item)
                    item['status'] = 'posted'
                    item['posted_at'] = datetime.now().isoformat()
                    self.logger.info(f"Posted to {item['platform']}: {item['content'][:50]}...")
                except Exception as e:
                    item['status'] = 'failed'
                    item['error'] = str(e)
                    self.logger.error(f"Failed to post to {item['platform']}: {e}")

        # Update schedule file
        self._save_schedule(self.schedule)

    def _post_content(self, item: Dict[str, Any]):
        """Post content to specified platform"""
        platform = item['platform']
        content = item['content']

        # This would call the platform-specific posting function
        # For now, just log it
        self.logger.info(f"Would post to {platform}: {content}")

        # Actual implementation would be:
        # self.platform_manager.post(platform, content)

    def run_scheduler(self):
        """Run continuous scheduler"""
        self.logger.info("Starting social media scheduler")

        # Schedule daily schedule creation
        schedule.every().day.at("00:01").do(self.create_schedule, days=1)

        # Schedule posting every hour
        schedule.every().hour.do(self.execute_schedule)

        # Run scheduler
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute


def main():
    """Main function"""
    import argparse

    parser = argparse.ArgumentParser(description='Social Media Scheduler')
    parser.add_argument('--create-schedule', type=int, default=30,
                       help='Create schedule for N days (default: 30)')
    parser.add_argument('--execute', action='store_true',
                       help='Execute current schedule')
    parser.add_argument('--run', action='store_true',
                       help='Run continuous scheduler')

    args = parser.parse_args()

    scheduler = SocialScheduler()

    if args.create_schedule:
        schedule = scheduler.create_schedule(days=args.create_schedule)
        print(f"Created schedule with {len(schedule)} posts")

    if args.execute:
        scheduler.execute_schedule()
        print("Schedule executed")

    if args.run:
        scheduler.run_scheduler()

if __name__ == '__main__':
    main()
