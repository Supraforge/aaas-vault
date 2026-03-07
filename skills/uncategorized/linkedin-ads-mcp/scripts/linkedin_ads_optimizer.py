#!/usr/bin/env python3
"""
LinkedIn Ads Optimizer - Budget and bid optimization
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List
from linkedin_ads_manager import LinkedInAdsManager

class LinkedInAdsOptimizer:
    """Optimizer for LinkedIn Ads campaigns"""
    
    def __init__(self):
        self.manager = LinkedInAdsManager()
    
    def analyze_campaign_performance(self, campaign_id: str) -> Dict:
        """Analyze campaign performance and provide optimization recommendations"""
        analytics = self.manager.get_campaign_analytics(campaign_id)
        
        recommendations = {
            'campaign_id': campaign_id,
            'analysis_date': datetime.now().isoformat(),
            'recommendations': [],
            'warnings': [],
            'optimization_opportunities': []
        }
        
        # Analyze performance metrics
        if analytics.get('elements'):
            for element in analytics['elements']:
                # Check CTR
                clicks = element.get('clicks', 0)
                impressions = element.get('impressions', 0)
                
                if impressions > 0:
                    ctr = (clicks / impressions) * 100
                    if ctr < 0.5:
                        recommendations['recommendations'].append({
                            'type': 'CTR_IMPROVEMENT',
                            'message': f'Low CTR ({ctr:.2f}%). Consider improving ad creative or targeting.',
                            'priority': 'HIGH'
                        })
                
                # Check cost per conversion
                cost = element.get('costInUsd', 0)
                conversions = element.get('conversions', 0)
                
                if conversions > 0:
                    cpc = cost / conversions
                    if cpc > 100:
                        recommendations['warnings'].append({
                            'type': 'HIGH_CPA',
                            'message': f'High cost per conversion (${cpc:.2f}). Consider adjusting bids or improving landing page.',
                            'priority': 'HIGH'
                        })
                
                # Check budget utilization
                if 'dailyBudget' in element:
                    budget = element['dailyBudget'].get('amount', 0)
                    if budget > 0 and cost < budget * 0.5:
                        recommendations['optimization_opportunities'].append({
                            'type': 'UNDERSPENT_BUDGET',
                            'message': f'Campaign is underspending (${cost:.2f} of ${budget:.2f} daily budget). Consider increasing bids or expanding targeting.',
                            'priority': 'MEDIUM'
                        })
        
        return recommendations
    
    def optimize_bids(self, campaign_id: str, strategy: str = 'MAXIMIZE_CONVERSIONS') -> Dict:
        """Optimize bids based on performance"""
        analysis = self.analyze_campaign_performance(campaign_id)
        
        optimization_plan = {
            'campaign_id': campaign_id,
            'strategy': strategy,
            'adjustments': [],
            'expected_impact': 'Varies based on campaign performance'
        }
        
        # Generate bid adjustments based on analysis
        for rec in analysis['recommendations']:
            if rec['type'] == 'CTR_IMPROVEMENT':
                optimization_plan['adjustments'].append({
                    'action': 'INCREASE_BID',
                    'reason': 'Low CTR - increase bid to improve ad placement',
                    'percentage': 10
                })
        
        for warning in analysis['warnings']:
            if warning['type'] == 'HIGH_CPA':
                optimization_plan['adjustments'].append({
                    'action': 'DECREASE_BID',
                    'reason': 'High cost per conversion - reduce bid to improve efficiency',
                    'percentage': 15
                })
        
        return optimization_plan
    
    def generate_optimization_report(self, campaign_ids: List[str]) -> str:
        """Generate comprehensive optimization report for multiple campaigns"""
        report = {
            'generated_at': datetime.now().isoformat(),
            'campaigns_analyzed': len(campaign_ids),
            'campaign_reports': [],
            'summary': {
                'total_recommendations': 0,
                'total_warnings': 0,
                'total_opportunities': 0
            }
        }
        
        for campaign_id in campaign_ids:
            analysis = self.analyze_campaign_performance(campaign_id)
            report['campaign_reports'].append(analysis)
            
            report['summary']['total_recommendations'] += len(analysis['recommendations'])
            report['summary']['total_warnings'] += len(analysis['warnings'])
            report['summary']['total_opportunities'] += len(analysis['optimization_opportunities'])
        
        return json.dumps(report, indent=2)

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='LinkedIn Ads Optimizer')
    parser.add_argument('--analyze', type=str, help='Analyze campaign performance for given campaign ID')
    parser.add_argument('--optimize-bids', type=str, help='Generate bid optimization plan for campaign ID')
    parser.add_argument('--generate-report', nargs='+', help='Generate optimization report for campaign IDs')
    
    args = parser.parse_args()
    optimizer = LinkedInAdsOptimizer()
    
    if args.analyze:
        result = optimizer.analyze_campaign_performance(args.analyze)
        print(json.dumps(result, indent=2))
    elif args.optimize_bids:
        result = optimizer.optimize_bids(args.optimize_bids)
        print(json.dumps(result, indent=2))
    elif args.generate_report:
        result = optimizer.generate_optimization_report(args.generate_report)
        print(result)
    else:
        parser.print_help()
