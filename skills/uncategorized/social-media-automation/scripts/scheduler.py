#!/usr/bin/env python3
"""
Scheduler for social media posts
"""

import schedule
import time
from social_automation import SocialMediaAutomation

def run_scheduler():
    sm = SocialMediaAutomation()

    # Example scheduled posts (would be loaded from a database or file in real use)
    schedule.every().day.at("09:00").do(sm.post, "twitter", "Good morning! #motivation")
    schedule.every().day.at("12:00").do(sm.post, "facebook", "Lunch time thoughts...")
    schedule.every().day.at("18:00").do(sm.post, "instagram", "Evening vibes", "sunset.jpg")

    print("Scheduler started. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    run_scheduler()
