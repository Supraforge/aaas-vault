#!/usr/bin/env python3
"""
Facebook Ads Optimizer - Bid and budget optimization
"""

import os
import sys
import json
import argparse
import statistics
from datetime import datetime, timedelta
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet

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

def analyze_campaign_performance(account, campaign_id, days_back=7):
    """Analyze campaign performance for optimization"""
    print(f"🔍 Analyzing campaign {campaign_id} performance for last {days_back} days")
    
    # Get campaign insights
    campaign = Campaign(campaign_id)
    
    # Define date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_back)
    
    params = {
        'time_range': {
            'since': start_date.strftime('%Y-%m-%d'),
            'until': end_date.strftime('%Y-%m-%d')
        },
        'level': 'adset',
    }
    
    fields = [
        'adset_name',
        'impressions',
        'clicks',
        'spend',
        'cpc',
        'ctr',
        'conversions',
        'conversion_rate',
        'frequency',
        'reach',
    ]
    
    insights = campaign.get_insights(fields=fields, params=params)
    
    if not insights:
        return {"error": "No performance data found"}
    
    # Analyze performance
    performance_data = []
    for insight in insights:
        data = dict(insight)
        
        # Calculate efficiency score
        spend = float(data.get('spend', 0))
        conversions = float(data.get('conversions', 0))
        clicks = float(data.get('clicks', 0))
        
        if spend > 0 and conversions > 0:
            cpa = spend / conversions
            efficiency_score = 100 / cpa if cpa > 0 else 0
        elif clicks > 0:
            cpc = spend / clicks if clicks > 0 else 0
            efficiency_score = 100 / cpc if cpc > 0 else 0
        else:
            efficiency_score = 0
        
        data['efficiency_score'] = round(efficiency_score, 2)
        data['roas'] = conversions * 100 / spend if spend > 0 else 0
        performance_data.append(data)
    
    return performance_data

def generate_optimization_recommendations(performance_data):
    """Generate optimization recommendations based on performance"""
    if not performance_data:
        return {"error": "No performance data available"}
    
    recommendations = []
    
    for adset in performance_data:
        adset_name = adset.get('adset_name', 'Unknown')
        efficiency = adset.get('efficiency_score', 0)
        cpc = float(adset.get('cpc', 0))
        ctr = float(adset.get('ctr', 0))
        conversions = float(adset.get('conversions', 0))
        spend = float(adset.get('spend', 0))
        
        rec = {
            'adset_name': adset_name,
            'current_efficiency': efficiency,
            'recommendations': []
        }
        
        # Generate recommendations based on metrics
        if efficiency < 50:
            rec['recommendations'].append({
                'action': 'DECREASE_BID',
                'reason': 'Low efficiency score',
                'suggested_change': '-20%',
                'priority': 'HIGH'
            })
        
        if cpc > 5.0:  # High CPC
            rec['recommendations'].append({
                'action': 'DECREASE_BID',
                'reason': 'High cost per click',
                'suggested_change': '-15%',
                'priority': 'MEDIUM'
            })
        
        if ctr < 1.0:  # Low CTR
            rec['recommendations'].append({
                'action': 'UPDATE_CREATIVE',
                'reason': 'Low click-through rate',
                'suggested_change': 'Test new ad creative',
                'priority': 'HIGH'
            })
        
        if conversions == 0 and spend > 10:
            rec['recommendations'].append({
                'action': 'PAUSE',
                'reason': 'No conversions despite spend',
                'suggested_change': 'Pause ad set for review',
                'priority': 'HIGH'
            })
        
        if efficiency > 80:
            rec['recommendations'].append({
                'action': 'INCREASE_BUDGET',
                'reason': 'High efficiency score',
                'suggested_change': '+30%',
                'priority': 'MEDIUM'
            })
        
        if rec['recommendations']:
            recommendations.append(rec)
    
    return recommendations

def apply_optimization(account, adset_id, action, value=None):
    """Apply optimization to ad set"""
    print(f"⚡ Applying optimization: {action} to adset {adset_id}")
    
    adset = AdSet(adset_id)
    
    if action == 'DECREASE_BID':
        # Get current bid
        adset.remote_read(fields=['bid_amount'])
        current_bid = adset.get('bid_amount', 100)
        
        # Calculate new bid
        if value:
            percentage = float(value.strip('%')) / 100
            new_bid = current_bid * (1 - percentage)
        else:
            new_bid = current_bid * 0.8  # Default 20% decrease
        
        # Update bid
        adset.update({
            AdSet.Field.bid_amount: int(new_bid)
        })
        
        return {
            'adset_id': adset_id,
            'action': 'DECREASE_BID',
            'old_bid': current_bid,
            'new_bid': new_bid,
            'change_percentage': f'{((new_bid - current_bid) / current_bid * 100):.1f}%'
        }
    
    elif action == 'INCREASE_BUDGET':
        # Get current budget
        adset.remote_read(fields=['daily_budget'])
        current_budget = adset.get('daily_budget', 1000)
        
        # Calculate new budget
        if value:
            percentage = float(value.strip('%')) / 100
            new_budget = current_budget * (1 + percentage)
        else:
            new_budget = current_budget * 1.3  # Default 30% increase
        
        # Update budget
        adset.update({
            AdSet.Field.daily_budget: int(new_budget)
        })
        
        return {
            'adset_id': adset_id,
            'action': 'INCREASE_BUDGET',
            'old_budget': current_budget,
            'new_budget': new_budget,
            'change_percentage': f'{((new_budget - current_budget) / current_budget * 100):.1f}%'
        }
    
    elif action == 'PAUSE':
        # Pause ad set
        adset.update({
            AdSet.Field.status: 'PAUSED'
        })
        
        return {
            'adset_id': adset_id,
            'action': 'PAUSE',
            'status': 'PAUSED'
        }
    
    else:
        return {
            'adset_id': adset_id,
            'action': action,
            'error': 'Action not implemented'
        }

def main():
    parser = argparse.ArgumentParser(description='Facebook Ads Optimizer')
    parser.add_argument('--campaign-id', required=True,
                       help='Campaign ID to analyze')
    parser.add_argument('--days', type=int, default=7,
                       help='Days back to analyze (default: 7)')
    parser.add_argument('--analyze-only', action='store_true',
                       help='Only analyze, don\'t apply optimizations')
    parser.add_argument('--apply', action='store_true',
                       help='Apply optimization recommendations')
    parser.add_argument('--output', choices=['json', 'text'], default='text',
                       help='Output format')
    
    args = parser.parse_args()
    
    # Initialize API
    try:
        account = init_api()
    except Exception as e:
        print(f"❌ Failed to initialize Facebook Ads API: {e}")
        sys.exit(1)
    
    # Analyze performance
    performance_data = analyze_campaign_performance(account, args.campaign_id, args.days)
    
    if 'error' in performance_data:
        print(f"❌ {performance_data['error']}")
        sys.exit(1)
    
    # Generate recommendations
    recommendations = generate_optimization_recommendations(performance_data)
    
    if 'error' in recommendations:
        print(f"❌ {recommendations['error']}")
        sys.exit(1)
    
    # Output analysis
    if args.output == 'json':
        result = {
            'performance_data': performance_data,
            'recommendations': recommendations
        }
        print(json.dumps(result, indent=2))
    else:
        print(f"📊 Performance Analysis for Campaign {args.campaign_id}:")
        print(f"📅 Last {args.days} days")
        print(f"📈 {len(performance_data)} ad sets analyzed\n")
        
        for i, adset in enumerate(performance_data[:5]):  # Show top 5
            print(f"Ad Set: {adset.get('adset_name', 'Unknown')}")
            print(f"  Spend: ${adset.get('spend', 0):.2f}")
            print(f"  Conversions: {adset.get('conversions', 0)}")
            print(f"  CPC: ${adset.get('cpc', 0):.2f}")
            print(f"  CTR: {adset.get('ctr', 0):.2f}%")
            print(f"  Efficiency Score: {adset.get('efficiency_score', 0):.1f}")
            print()
        
        print("\n🎯 Optimization Recommendations:")
        for rec in recommendations:
            print(f"\nAd Set: {rec['adset_name']}")
            print(f"  Current Efficiency: {rec['current_efficiency']:.1f}")
            for r in rec['recommendations']:
                print(f"  • {r['action']}: {r['reason']} ({r['priority']} priority)")
                print(f"    Suggested: {r['suggested_change']}")
    
    # Apply optimizations if requested
    if args.apply and not args.analyze_only:
        print("\n⚡ Applying optimizations...")
        applied_results = []
        
        for rec in recommendations:
            adset_name = rec['adset_name']
            # Extract adset ID from name (simplified - in real scenario would map)
            # For demo purposes, we'll just show what would happen
            for r in rec['recommendations']:
                if r['priority'] == 'HIGH':
                    result = {
                        'adset': adset_name,
                        'action': r['action'],
                        'suggested_change': r['suggested_change'],
                        'status': 'SIMULATED (would apply in production)'
                    }
                    applied_results.append(result)
        
        print(f"✅ {len(applied_results)} optimizations would be applied")
        for result in applied_results:
            print(f"  • {result['adset']}: {result['action']} ({result['suggested_change']})")

if __name__ == '__main__':
    main()
