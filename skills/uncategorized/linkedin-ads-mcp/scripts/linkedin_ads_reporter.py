#!/usr/bin/env python3
"""
LinkedIn Ads Reporter - Analytics and reporting
"""

import json
import csv
from datetime import datetime, timedelta
from typing import Dict, List
import pandas as pd
from linkedin_ads_manager import LinkedInAdsManager

class LinkedInAdsReporter:
    """Reporter for LinkedIn Ads analytics"""
    
    def __init__(self):
        self.manager = LinkedInAdsManager()
    
    def generate_performance_report(self, date_range: str = 'LAST_30_DAYS', format: str = 'json') -> str:
        """Generate performance report"""
        analytics = self.manager.get_account_analytics(date_range)
        
        if format == 'json':
            return json.dumps(analytics, indent=2)
        elif format == 'csv':
            # Convert to DataFrame
            df = pd.DataFrame(analytics.get('elements', []))
            
            # Add calculated metrics
            if 'impressions' in df.columns and 'clicks' in df.columns:
                df['CTR'] = (df['clicks'] / df['impressions']) * 100
            if 'costInUsd' in df.columns and 'clicks' in df.columns:
                df['CPC'] = df['costInUsd'] / df['clicks'].replace(0, 1)
            if 'costInUsd' in df.columns and 'conversions' in df.columns:
                df['CPA'] = df['costInUsd'] / df['conversions'].replace(0, 1)
            
            return df.to_csv(index=False)
        else:
            return str(analytics)
    
    def generate_campaign_comparison(self, campaign_ids: List[str]) -> Dict:
        """Generate comparison report for multiple campaigns"""
        comparison = {
            'generated_at': datetime.now().isoformat(),
            'campaigns_compared': len(campaign_ids),
            'metrics': {},
            'rankings': {},
            'recommendations': []
        }
        
        campaign_data = []
        for campaign_id in campaign_ids:
            analytics = self.manager.get_campaign_analytics(campaign_id)
            if analytics.get('elements'):
                campaign_data.append({
                    'campaign_id': campaign_id,
                    'data': analytics['elements'][0]
                })
        
        # Calculate rankings
        metrics = ['clicks', 'impressions', 'costInUsd', 'conversions']
        for metric in metrics:
            if all(metric in camp['data'] for camp in campaign_data):
                sorted_campaigns = sorted(campaign_data, key=lambda x: x['data'].get(metric, 0), reverse=True)
                comparison['rankings'][metric] = [
                    {'campaign_id': camp['campaign_id'], 'value': camp['data'].get(metric, 0)}
                    for camp in sorted_campaigns
                ]
        
        # Generate recommendations
        if len(campaign_data) >= 2:
            # Find best performing campaign
            best_campaign = max(campaign_data, key=lambda x: x['data'].get('conversions', 0))
            worst_campaign = min(campaign_data, key=lambda x: x['data'].get('conversions', 0))
            
            comparison['recommendations'].append({
                'type': 'PERFORMANCE_GAP',
                'message': f'Campaign {best_campaign["campaign_id"]} has {best_campaign["data"].get("conversions", 0)} conversions vs {worst_campaign["data"].get("conversions", 0)} for campaign {worst_campaign["campaign_id"]}. Consider applying successful strategies from best performer.',
                'priority': 'HIGH'
            })
        
        return comparison
    
    def generate_executive_summary(self) -> Dict:
        """Generate executive summary report"""
        campaigns = self.manager.get_campaigns()
        
        summary = {
            'report_date': datetime.now().strftime('%Y-%m-%d'),
            'total_campaigns': len(campaigns),
            'active_campaigns': len([c for c in campaigns if c.get('status') == 'ACTIVE']),
            'paused_campaigns': len([c for c in campaigns if c.get('status') == 'PAUSED']),
            'performance_overview': {},
            'key_insights': [],
            'action_items': []
        }
        
        # Get overall analytics
        analytics = self.manager.get_account_analytics()
        if analytics.get('elements'):
            total_data = analytics['elements'][0]
            summary['performance_overview'] = {
                'total_spend': total_data.get('costInUsd', 0),
                'total_clicks': total_data.get('clicks', 0),
                'total_impressions': total_data.get('impressions', 0),
                'total_conversions': total_data.get('conversions', 0)
            }
            
            # Calculate metrics
            if total_data.get('impressions', 0) > 0:
                summary['performance_overview']['avg_ctr'] = (total_data.get('clicks', 0) / total_data.get('impressions', 0)) * 100
            if total_data.get('clicks', 0) > 0:
                summary['performance_overview']['avg_cpc'] = total_data.get('costInUsd', 0) / total_data.get('clicks', 0)
            if total_data.get('conversions', 0) > 0:
                summary['performance_overview']['avg_cpa'] = total_data.get('costInUsd', 0) / total_data.get('conversions', 0)
        
        return summary

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='LinkedIn Ads Reporter')
    parser.add_argument('--performance-report', action='store_true', help='Generate performance report')
    parser.add_argument('--format', type=str, default='json', choices=['json', 'csv'], help='Report format')
    parser.add_argument('--compare-campaigns', nargs='+', help='Compare multiple campaigns')
    parser.add_argument('--executive-summary', action='store_true', help='Generate executive summary')
    
    args = parser.parse_args()
    reporter = LinkedInAdsReporter()
    
    if args.performance_report:
        report = reporter.generate_performance_report(format=args.format)
        if args.format == 'csv':
            filename = f"linkedin_performance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            with open(filename, 'w') as f:
                f.write(report)
            print(f"✅ Report saved to: {filename}")
        else:
            print(report)
    elif args.compare_campaigns:
        comparison = reporter.generate_campaign_comparison(args.compare_campaigns)
        print(json.dumps(comparison, indent=2))
    elif args.executive_summary:
        summary = reporter.generate_executive_summary()
        print(json.dumps(summary, indent=2))
    else:
        parser.print_help()
