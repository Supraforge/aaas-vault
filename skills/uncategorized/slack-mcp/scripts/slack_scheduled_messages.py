#!/usr/bin/env python3
"""
Slack Scheduled Messages
Schedule and send messages to Slack channels at specific times
"""

import os
import schedule
import time
from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()

class SlackScheduler:
    def __init__(self):
        self.client = WebClient(token=os.getenv('SLACK_BOT_TOKEN'))
        self.jobs = []
    
    def send_message(self, channel, text, blocks=None):
        """Send a message to Slack"""
        try:
            response = self.client.chat_postMessage(
                channel=channel,
                text=text,
                blocks=blocks
            )
            print(f"Message sent to {channel}: {response['ts']}")
            return response
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")
            return None
    
    def schedule_daily_message(self, channel, text, time_str):
        """Schedule a daily message at specific time"""
        job = schedule.every().day.at(time_str).do(
            self.send_message, channel=channel, text=text
        )
        self.jobs.append(job)
        print(f"Scheduled daily message at {time_str} to {channel}")
        return job
    
    def schedule_weekly_message(self, channel, text, day, time_str):
        """Schedule a weekly message on specific day and time"""
        job = getattr(schedule.every(), day).at(time_str).do(
            self.send_message, channel=channel, text=text
        )
        self.jobs.append(job)
        print(f"Scheduled weekly message on {day} at {time_str} to {channel}")
        return job
    
    def run_pending(self):
        """Run all pending scheduled jobs"""
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    
    def clear_all_jobs(self):
        """Clear all scheduled jobs"""
        schedule.clear()
        self.jobs = []
        print("Cleared all scheduled jobs")

if __name__ == "__main__":
    scheduler = SlackScheduler()
    
    # Example: Schedule daily standup reminder
    scheduler.schedule_daily_message(
        channel="#general",
        text="🚀 Good morning team! Time for daily standup!",
        time_str="09:30"
    )
    
    # Example: Schedule weekly team meeting
    scheduler.schedule_weekly_message(
        channel="#team-meetings",
        text="📅 Weekly team meeting starting in 5 minutes!",
        day="monday",
        time_str="14:00"
    )
    
    print("Scheduler started. Press Ctrl+C to stop.")
    try:
        scheduler.run_pending()
    except KeyboardInterrupt:
        print("\nScheduler stopped.")
