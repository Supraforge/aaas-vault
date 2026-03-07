#!/usr/bin/env python3
"""
Mailchimp Analytics Script
Provides campaign performance insights and reporting
"""
import os
import json
from datetime import datetime, timedelta
from mailchimp_automation import MailchimpAutomation
from dotenv import load_dotenv

load_dotenv()

def generate_campaign_report(campaign_id):
    """Generate detailed campaign performance report"""
    automation = MailchimpAutomation()
    analytics = automation.get_campaign_analytics(campaign_id)
    
    if not analytics:
        return "Error: Could not retrieve campaign analytics"
    
    report = {
        "campaign_id": campaign_id,
        "campaign_title": analytics.get('campaign_title', 'Unknown'),
        "sent_time": analytics.get('send_time', 'Not sent'),
        "emails_sent": analytics.get('emails_sent', 0),
        "opens": {
            "total": analytics.get('opens', {}).get('opens_total', 0),
            "unique": analytics.get('opens', {}).get('unique_opens', 0),
            "rate": analytics.get('opens', {}).get('open_rate', 0)
        },
        "clicks": {
            "total": analytics.get('clicks', {}).get('clicks_total', 0),
            "unique": analytics.get('clicks', {}).get('unique_clicks', 0),
            "rate": analytics.get('clicks', {}).get('click_rate', 0)
        },
        "bounces": analytics.get('bounces', {}).get('hard_bounces', 0) + analytics.get('bounces', {}).get('soft_bounces', 0),
        "unsubscribes": analytics.get('unsubscribed', 0),
        "timestamp": datetime.now().isoformat()
    }
    
    return json.dumps(report, indent=2)

def calculate_roi(campaign_id, revenue):
    """Calculate ROI for campaign"""
    automation = MailchimpAutomation()
    analytics = automation.get_campaign_analytics(campaign_id)
    
    if not analytics:
        return "Error: Could not retrieve campaign data"
    
    emails_sent = analytics.get('emails_sent', 0)
    unique_clicks = analytics.get('clicks', {}).get('unique_clicks', 0)
    
    # Simple ROI calculation
    click_rate = (unique_clicks / emails_sent * 100) if emails_sent > 0 else 0
    roi_percentage = (revenue / emails_sent * 100) if emails_sent > 0 else 0
    
    return {
        "campaign_id": campaign_id,
        "emails_sent": emails_sent,
        "unique_clicks": unique_clicks,
        "click_rate": f"{click_rate:.2f}%",
        "revenue": revenue,
        "roi_per_email": f"${revenue/emails_sent:.2f}" if emails_sent > 0 else "N/A",
        "roi_percentage": f"{roi_percentage:.2f}%"
    }

if __name__ == "__main__":
    print("Mailchimp Analytics Script")
    print("=" * 50)
    print("\nExample functions available:")
    print("1. generate_campaign_report(campaign_id)")
    print("2. calculate_roi(campaign_id, revenue)")
