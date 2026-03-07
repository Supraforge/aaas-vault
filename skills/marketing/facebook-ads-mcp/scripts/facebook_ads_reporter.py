#!/usr/bin/env python3
"""
Facebook Ads Reporter - Performance reporting and analytics
"""

import os
import sys
import json
import argparse
import pandas as pd
from datetime import datetime, timedelta
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights

def init_api():
    """Initialize Facebook Ads API"""
    access_token = os.getenv('FACEBOOK_ADS_ACCESS_TOKEN')
    app_id = os.getenv('FACEBOOK_ADS_APP_ID')
    app_secret = os.getenv('FACEBOOK_ADS_APP_SECRET')
    account_id = os.getenv('FACEBOOK_ADS_ACCOUNT_ID')
    api_version = os.getenv('FACEBOOK_ADS_API_VERSION', 'v19.0')
    
    FacebookAdsApi.init(access_token=access_token, 
                       app_id=app_id, 
                       app_secret=app_secret,
                       api_version=api_version)
    return AdAccount(f'act_{account_id}')

def get_performance_report(account, date_range='last_7_days', level='campaign'):
    """Get performance report for specified date range and level"""
    print(f"📊 Generating {level} performance report for {date_range}")
    
    # Define date range
    end_date = datetime.now()
    if date_range == 'today':
        start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    elif date_range == 'yesterday':
        start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
        end_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    elif date_range == 'last_7_days':
        start_date = datetime.now() - timedelta(days=7)
    elif date_range == 'last_30_days':
        start_date = datetime.now() - timedelta(days=30)
    else:
        # Custom date range in format 'YYYY-MM-DD_YYYY-MM-DD'
        dates = date_range.split('_')
        if len(dates) == 2:
            start_date = datetime.strptime(dates[0], '%Y-%m-%d')
            end_date = datetime.strptime(dates[1], '%Y-%m-%d')
        else:
            start_date = datetime.now() - timedelta(days=7)
    
    # Define fields to retrieve
    fields = [
        'campaign_name',
        'adset_name',
        'ad_name',
        'impressions',
        'clicks',
        'spend',
        'cpc',
        'cpm',
        'ctr',
        'conversions',
        'conversion_rate',
        'frequency',
        'reach',
        'date_start',
        'date_stop',
    ]
    
    # Define parameters
    params = {
        'time_range': {
            'since': start_date.strftime('%Y-%m-%d'),
            'until': end_date.strftime('%Y-%m-%d')
        },
        'level': level,
        'time_increment': 1,
    }
    
    # Get insights
    insights = account.get_insights(fields=fields, params=params)
    
    # Convert to list of dicts
    report_data = []
    for insight in insights:
        report_data.append(dict(insight))
    
    return report_data

def export_report_to_csv(report_data, filename='facebook_ads_report.csv'):
    """Export report data to CSV"""
    if not report_data:
        print("❌ No data to export")
        return None
    
    df = pd.DataFrame(report_data)
    df.to_csv(filename, index=False)
    print(f"✅ Report exported to {filename}")
    return filename

def calculate_roi(report_data):
    """Calculate ROI metrics from report data"""
    if not report_data:
        return {"error": "No data available"}
    
    total_spend = sum(float(item.get('spend', 0)) for item in report_data)
    total_conversions = sum(float(item.get('conversions', 0)) for item in report_data)
    total_clicks = sum(float(item.get('clicks', 0)) for item in report_data)
    total_impressions = sum(float(item.get('impressions', 0)) for item in report_data)
    
    # Calculate metrics
    cpc = total_spend / total_clicks if total_clicks > 0 else 0
    ctr = (total_clicks / total_impressions) * 100 if total_impressions > 0 else 0
    conversion_rate = (total_conversions / total_clicks) * 100 if total_clicks > 0 else 0
    
    return {
        'total_spend': round(total_spend, 2),
        'total_conversions': round(total_conversions, 0),
        'total_clicks': round(total_clicks, 0),
        'total_impressions': round(total_impressions, 0),
        'average_cpc': round(cpc, 2),
        'ctr_percentage': round(ctr, 2),
        'conversion_rate_percentage': round(conversion_rate, 2),
    }

def main():
    parser = argparse.ArgumentParser(description='Facebook Ads Performance Reporter')
    parser.add_argument('--date-range', default='last_7_days',
                       choices=['today', 'yesterday', 'last_7_days', 'last_30_days'],
                       help='Date range for report')
    parser.add_argument('--level', default='campaign',
                       choices=['campaign', 'adset', 'ad', 'account'],
                       help='Level of reporting')
    parser.add_argument('--export', choices=['csv', 'json', 'none'], default='csv',
                       help='Export format')
    parser.add_argument('--calculate-roi', action='store_true',
                       help='Calculate ROI metrics')
    parser.add_argument('--output-file', default='facebook_ads_report.csv',
                       help='Output filename for export')
    
    args = parser.parse_args()
    
    # Initialize API
    try:
        account = init_api()
    except Exception as e:
        print(f"❌ Failed to initialize Facebook Ads API: {e}")
        sys.exit(1)
    
    # Get report
    report_data = get_performance_report(account, args.date_range, args.level)
    
    if not report_data:
        print("⚠️  No data found for the specified criteria")
        sys.exit(0)
    
    print(f"📈 Found {len(report_data)} records")
    
    # Calculate ROI if requested
    if args.calculate_roi:
        roi_metrics = calculate_roi(report_data)
        print("\n📊 ROI Metrics:")
        for key, value in roi_metrics.items():
            print(f"  {key}: {value}")
    
    # Export data
    if args.export == 'csv':
        export_report_to_csv(report_data, args.output_file)
    elif args.export == 'json':
        with open(args.output_file.replace('.csv', '.json'), 'w') as f:
            json.dump(report_data, f, indent=2)
        print(f"✅ Report exported to {args.output_file.replace('.csv', '.json')}")
    
    # Print sample data
    print("\n📋 Sample data (first 3 records):")
    for i, record in enumerate(report_data[:3]):
        print(f"\nRecord {i+1}:")
        for key in ['campaign_name', 'impressions', 'clicks', 'spend', 'conversions']:
            if key in record:
                print(f"  {key}: {record[key]}")

if __name__ == '__main__':
    main()
