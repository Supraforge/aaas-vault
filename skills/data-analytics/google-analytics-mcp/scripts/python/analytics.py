#!/usr/bin/env python3
"""
Google Analytics MCP - Python Implementation
"""

import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pandas as pd

# Load environment variables
load_dotenv()

class GoogleAnalyticsMCP:
    """Main class for Google Analytics integration"""
    
    def __init__(self):
        self.client_id = os.getenv('GOOGLE_CLIENT_ID')
        self.client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
        self.property_id = os.getenv('GOOGLE_ANALYTICS_PROPERTY_ID')
        self.view_id = os.getenv('GOOGLE_ANALYTICS_VIEW_ID')
        self.credentials = None
        self.service = None
        
    def authenticate(self):
        """Authenticate with Google Analytics API"""
        SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
        
        # Try to load existing credentials
        creds_file = 'token.json'
        if os.path.exists(creds_file):
            self.credentials = Credentials.from_authorized_user_file(creds_file, SCOPES)
        
        # If credentials don't exist or are invalid, get new ones
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_config(
                    {
                        "installed": {
                            "client_id": self.client_id,
                            "client_secret": self.client_secret,
                            "redirect_uris": ["http://localhost:8080/"]
                        }
                    },
                    SCOPES
                )
                self.credentials = flow.run_local_server(port=8080)
            
            # Save credentials for next run
            with open(creds_file, 'w') as token:
                token.write(self.credentials.to_json())
        
        # Build service
        self.service = build('analyticsreporting', 'v4', credentials=self.credentials)
        return self.service
    
    def get_ga4_report(self, metrics: List[str], dimensions: List[str] = None, 
                      date_range: str = '30daysAgo:today') -> Dict:
        """Get GA4 report"""
        if not self.service:
            self.authenticate()
        
        # Prepare request body
        request_body = {
            'property': f'properties/{self.property_id.replace("GA4-", "")}',
            'dateRanges': [{'startDate': date_range.split(':')[0], 
                           'endDate': date_range.split(':')[1]}],
            'metrics': [{'name': metric} for metric in metrics]
        }
        
        if dimensions:
            request_body['dimensions'] = [{'name': dim} for dim in dimensions]
        
        # Make API call
        response = self.service.properties().batchRunReports(
            property=request_body['property'],
            body={'requests': [request_body]}
        ).execute()
        
        return self._parse_ga4_response(response)
    
    def get_ua_report(self, metrics: List[str], dimensions: List[str] = None,
                     date_range: str = '30daysAgo:today') -> Dict:
        """Get Universal Analytics report"""
        if not self.service:
            self.authenticate()
        
        # Prepare request
        request = {
            'viewId': self.view_id,
            'dateRanges': [{'startDate': date_range.split(':')[0], 
                           'endDate': date_range.split(':')[1]}],
            'metrics': [{'expression': f'ga:{metric}'} for metric in metrics]
        }
        
        if dimensions:
            request['dimensions'] = [{'name': f'ga:{dim}'} for dim in dimensions]
        
        # Make API call
        response = self.service.reports().batchGet(body={'reportRequests': [request]}).execute()
        
        return self._parse_ua_response(response)
    
    def _parse_ga4_response(self, response: Dict) -> Dict:
        """Parse GA4 API response"""
        results = []
        for report in response.get('reports', []):
            for row in report.get('rows', []):
                row_data = {}
                # Parse dimensions
                for i, dim in enumerate(row.get('dimensionValues', [])):
                    row_data[f'dimension_{i}'] = dim.get('value')
                # Parse metrics
                for i, metric in enumerate(row.get('metricValues', [])):
                    row_data[f'metric_{i}'] = metric.get('value')
                results.append(row_data)
        
        return {
            'total_rows': len(results),
            'data': results,
            'timestamp': datetime.now().isoformat()
        }
    
    def _parse_ua_response(self, response: Dict) -> Dict:
        """Parse Universal Analytics response"""
        results = []
        for report in response.get('reports', []):
            column_header = report.get('columnHeader', {})
            dimension_headers = column_header.get('dimensions', [])
            metric_headers = [h['name'] for h in column_header.get('metricHeader', {}).get('metricHeaderEntries', [])]
            
            for row in report.get('data', {}).get('rows', []):
                row_data = {}
                # Add dimensions
                for i, dim in enumerate(row.get('dimensions', [])):
                    header = dimension_headers[i] if i < len(dimension_headers) else f'dimension_{i}'
                    row_data[header.replace('ga:', '')] = dim
                # Add metrics
                for i, metric in enumerate(row.get('metrics', [{}])[0].get('values', [])):
                    header = metric_headers[i] if i < len(metric_headers) else f'metric_{i}'
                    row_data[header.replace('ga:', '')] = metric
                results.append(row_data)
        
        return {
            'total_rows': len(results),
            'data': results,
            'timestamp': datetime.now().isoformat()
        }
    
    def export_to_csv(self, data: Dict, filename: str = 'analytics_report.csv'):
        """Export analytics data to CSV"""
        df = pd.DataFrame(data['data'])
        df.to_csv(filename, index=False)
        print(f"✅ Report exported to {filename}")
        return filename
    
    def generate_insights(self, data: Dict) -> Dict:
        """Generate business insights from analytics data"""
        insights = {
            'summary': {
                'total_records': data['total_rows'],
                'generated_at': data['timestamp'],
                'data_points_analyzed': len(data['data'])
            },
            'recommendations': [],
            'key_metrics': {},
            'trends': []
        }
        
        # Example insights (customize based on actual data)
        if data['data']:
            insights['recommendations'].append(
                "Optimize landing pages for better conversion rates"
            )
            insights['recommendations'].append(
                "Increase content marketing efforts for organic traffic"
            )
            
            # Calculate average metrics if available
            metrics_data = [float(row.get('metric_0', 0)) for row in data['data'] 
                          if row.get('metric_0') and str(row.get('metric_0')).replace('.', '').isdigit()]
            if metrics_data:
                insights['key_metrics']['average_value'] = sum(metrics_data) / len(metrics_data)
        
        return insights

# Example usage
if __name__ == "__main__":
    print("🔍 Google Analytics MCP - Python Example")
    
    # Initialize client
    ga = GoogleAnalyticsMCP()
    
    # Example 1: Get basic traffic metrics (GA4)
    print("\n1. Getting basic traffic metrics...")
    if ga.property_id:
        traffic_data = ga.get_ga4_report(
            metrics=['activeUsers', 'sessions', 'screenPageViews'],
            dimensions=['date', 'country', 'deviceCategory'],
            date_range='7daysAgo:today'
        )
        print(f"   Retrieved {traffic_data['total_rows']} rows of traffic data")
        
        # Export to CSV
        csv_file = ga.export_to_csv(traffic_data, 'traffic_report.csv')
        
        # Generate insights
        insights = ga.generate_insights(traffic_data)
        print(f"   Generated {len(insights['recommendations'])} recommendations")
    else:
        print("   ⚠️ GA4 property ID not configured")
    
    # Example 2: Get conversion data (Universal Analytics)
    print("\n2. Getting conversion data...")
    if ga.view_id:
        conversion_data = ga.get_ua_report(
            metrics=['transactions', 'transactionRevenue', 'conversionRate'],
            dimensions=['source', 'medium', 'campaign'],
            date_range='30daysAgo:today'
        )
        print(f"   Retrieved {conversion_data['total_rows']} rows of conversion data")
    else:
        print("   ⚠️ Universal Analytics view ID not configured")
    
    print("\n✅ Examples completed (requires actual Google Analytics credentials)")
