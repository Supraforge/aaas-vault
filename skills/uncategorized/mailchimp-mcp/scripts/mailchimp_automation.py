#!/usr/bin/env python3
"""
Mailchimp Automation Script
Handles audience management, campaign creation, and automation workflows
"""
import os
import json
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

class MailchimpAutomation:
    def __init__(self):
        self.api_key = os.getenv('MAILCHIMP_API_KEY')
        self.server_prefix = os.getenv('MAILCHIMP_SERVER_PREFIX', 'us1')
        self.base_url = f"https://{self.server_prefix}.api.mailchimp.com/3.0/"
        self.headers = {
            'Authorization': f'apikey {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def list_audiences(self):
        """List all audiences/lists"""
        try:
            response = requests.get(f"{self.base_url}lists", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error listing audiences: {e}")
            return None
    
    def create_campaign(self, campaign_data):
        """Create a new email campaign"""
        try:
            response = requests.post(
                f"{self.base_url}campaigns", 
                headers=self.headers, 
                data=json.dumps(campaign_data)
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error creating campaign: {e}")
            return None
    
    def add_subscriber(self, list_id, subscriber_data):
        """Add subscriber to audience"""
        try:
            email = subscriber_data.get('email_address')
            email_hash = self._create_email_hash(email)
            
            response = requests.put(
                f"{self.base_url}lists/{list_id}/members/{email_hash}",
                headers=self.headers,
                data=json.dumps(subscriber_data)
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error adding subscriber: {e}")
            return None
    
    def get_campaign_analytics(self, campaign_id):
        """Get campaign performance analytics"""
        try:
            response = requests.get(
                f"{self.base_url}reports/{campaign_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error getting analytics: {e}")
            return None
    
    def create_automation(self, automation_data):
        """Create automation workflow"""
        try:
            response = requests.post(
                f"{self.base_url}automations",
                headers=self.headers,
                data=json.dumps(automation_data)
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error creating automation: {e}")
            return None
    
    def _create_email_hash(self, email):
        """Create MD5 hash for email (Mailchimp requirement)"""
        import hashlib
        return hashlib.md5(email.lower().encode()).hexdigest()

if __name__ == "__main__":
    # Example usage
    automation = MailchimpAutomation()
    
    # List audiences
    audiences = automation.list_audiences()
    if audiences:
        print(f"Found {audiences.get('total_items', 0)} audiences")
        for audience in audiences.get('lists', [])[:5]:
            print(f"- {audience['name']}: {audience['stats']['member_count']} members")
