#!/usr/bin/env python3
"""
Zapier API integration for workflow automation
"""
import os
import json
import requests
from typing import Dict, List, Optional
from dotenv import load_dotenv

load_dotenv()

class ZapierAPI:
    """Zapier API client for workflow automation"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('ZAPIER_API_KEY')
        self.base_url = 'https://api.zapier.com/v2'
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def list_zaps(self) -> List[Dict]:
        """List all zaps in the account"""
        response = requests.get(
            f'{self.base_url}/zaps',
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
    
    def get_zap(self, zap_id: str) -> Dict:
        """Get details of a specific zap"""
        response = requests.get(
            f'{self.base_url}/zaps/{zap_id}',
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
    
    def trigger_zap(self, zap_id: str, data: Dict) -> Dict:
        """Trigger a zap with provided data"""
        response = requests.post(
            f'{self.base_url}/zaps/{zap_id}/trigger',
            headers=self.headers,
            json=data
        )
        response.raise_for_status()
        return response.json()
    
    def get_executions(self, zap_id: str, limit: int = 10) -> List[Dict]:
        """Get recent executions for a zap"""
        response = requests.get(
            f'{self.base_url}/zaps/{zap_id}/executions',
            headers=self.headers,
            params={'limit': limit}
        )
        response.raise_for_status()
        return response.json()
    
    def create_webhook_zap(self, name: str, trigger_app: str, action_app: str) -> Dict:
        """Create a new webhook-based zap"""
        zap_data = {
            'name': name,
            'trigger': {
                'type': 'webhook',
                'app': trigger_app
            },
            'action': {
                'type': 'action',
                'app': action_app
            }
        }
        response = requests.post(
            f'{self.base_url}/zaps',
            headers=self.headers,
            json=zap_data
        )
        response.raise_for_status()
        return response.json()
    
    def test_connection(self) -> bool:
        """Test API connection"""
        try:
            response = requests.get(
                f'{self.base_url}/zaps',
                headers=self.headers,
                params={'limit': 1}
            )
            return response.status_code == 200
        except:
            return False

if __name__ == '__main__':
    # Example usage
    api = ZapierAPI()
    
    if api.test_connection():
        print("✅ Connected to Zapier API")
        
        # List zaps
        zaps = api.list_zaps()
        print(f"📊 Found {len(zaps)} zaps")
        
        for zap in zaps[:3]:  # Show first 3
            print(f"  • {zap.get('title', 'Untitled')} (ID: {zap.get('id')})")
    else:
        print("❌ Failed to connect to Zapier API")
        print("Check your ZAPIER_API_KEY in .env file")
