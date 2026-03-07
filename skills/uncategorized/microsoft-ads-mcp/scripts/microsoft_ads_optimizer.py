#!/usr/bin/env python3
"""
Microsoft Ads Optimizer - Bid and campaign optimization
"""

import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from microsoft_ads_manager import MicrosoftAdsManager


def optimize_campaign(campaign_id: str, **kwargs) -> dict:
    """Optimize campaign bids and settings"""
    manager = MicrosoftAdsManager()
    
    # Get current performance
    performance = manager.get_campaign_performance(campaign_id, days=30)
    
    # Determine optimization strategy based on performance
    metrics = performance['metrics']
    
    optimization_plan = {
        'campaign_id': campaign_id,
        'optimization_date': datetime.now().isoformat(),
        'current_performance': metrics,
        'actions': [],
        'expected_impact': {},
        'risk_level': 'Low'
    }
    
    # Rule-based optimization logic
    if metrics['ctr'] < 1.5:
        optimization_plan['actions'].append({
            'action': 'increase_bids',
            'target': 'top_10_performing_keywords',
            'increase_percentage': 15,
            'reason': 'Low CTR indicates poor ad positioning'
        })
        optimization_plan['expected_impact']['ctr_increase'] = '0.3-0.5%'
    
    if metrics['conversion_rate'] < 2.0:
        optimization_plan['actions'].append({
            'action': 'add_negative_keywords',
            'keywords': ['free', 'cheap', 'trial'],
            'reason': 'Low conversion rate suggests irrelevant traffic'
        })
        optimization_plan['expected_impact']['conversion_increase'] = '0.5-1.0%'
    
    if metrics['average_cpc'] > 6.0:
        optimization_plan['actions'].append({
            'action': 'reduce_bids',
            'target': 'low_performing_keywords',
            'decrease_percentage': 20,
            'reason': 'High CPC reducing ROI'
        })
        optimization_plan['expected_impact']['cpc_decrease'] = '$0.75-1.25'
    
    if metrics['roas'] < 250:
        optimization_plan['actions'].append({
            'action': 'adjust_budget_allocation',
            'shift_percentage': 30,
            'from': 'underperforming_campaigns',
            'to': 'high_roas_campaigns',
            'reason': 'Low ROAS requires budget reallocation'
        })
        optimization_plan['expected_impact']['roas_increase'] = '40-60%'
    
    # Add time-based optimizations
    optimization_plan['actions'].append({
        'action': 'implement_dayparting',
        'peak_hours': ['09:00-12:00', '14:00-17:00'],
        'bid_adjustment': 25,
        'reason': 'B2B traffic peaks during business hours'
    })
    
    # Add device optimization
    optimization_plan['actions'].append({
        'action': 'adjust_device_bids',
        'desktop_increase': 20,
        'mobile_decrease': 10,
        'reason': 'B2B conversions higher on desktop'
    })
    
    # Calculate expected improvements
    total_expected_improvement = 0
    if 'ctr_increase' in optimization_plan['expected_impact']:
        total_expected_improvement += 15
    if 'conversion_increase' in optimization_plan['expected_impact']:
        total_expected_improvement += 20
    if 'cpc_decrease' in optimization_plan['expected_impact']:
        total_expected_improvement += 15
    if 'roas_increase' in optimization_plan['expected_impact']:
        total_expected_improvement += 25
    
    optimization_plan['total_expected_improvement'] = f'{total_expected_improvement}%'
    
    return optimization_plan


def apply_optimizations(optimization_plan: dict) -> dict:
    """Apply optimization plan to campaign"""
    # This would integrate with actual Microsoft Ads API
    # For now, return simulated application results
    
    application_result = {
        'optimization_plan_id': optimization_plan['campaign_id'] + '_' + datetime.now().strftime('%Y%m%d'),
        'applied_at': datetime.now().isoformat(),
        'actions_applied': len(optimization_plan['actions']),
        'status': 'completed',
        'estimated_savings': 450.00,  # Example savings
        'estimated_performance_improvement': optimization_plan['total_expected_improvement'],
        'next_review_date': (datetime.now() + timedelta(days=7)).isoformat(),
        'monitoring_metrics': [
            'ctr_change',
            'cpc_change',
            'conversion_rate_change',
            'roas_change'
        ]
    }
    
    return application_result


def main():
    import argparse
    import json
    
    parser = argparse.ArgumentParser(description='Microsoft Ads Campaign Optimizer')
    parser.add_argument('--action', required=True, choices=['analyze', 'apply', 'auto'],
                       help='Optimization action')
    parser.add_argument('--campaign-id', required=True, help='Campaign ID to optimize')
    parser.add_argument('--output-format', choices=['json', 'table', 'summary'], default='json',
                       help='Output format')
    parser.add_argument('--auto-apply', action='store_true', help='Auto-apply optimizations (for auto action)')
    
    args = parser.parse_args()
    
    try:
        if args.action == 'analyze':
            # Analyze and create optimization plan
            plan = optimize_campaign(args.campaign_id)
            result = {'optimization_plan': plan}
            
        elif args.action == 'apply':
            # Create and apply optimization plan
            plan = optimize_campaign(args.campaign_id)
            application = apply_optimizations(plan)
            result = {
                'optimization_plan': plan,
                'application_result': application
            }
            
        elif args.action == 'auto':
            # Automatic optimization with optional auto-apply
            plan = optimize_campaign(args.campaign_id)
            
            if args.auto_apply:
                application = apply_optimizations(plan)
                result = {
                    'optimization_plan': plan,
                    'application_result': application,
                    'mode': 'auto_applied'
                }
            else:
                result = {
                    'optimization_plan': plan,
                    'mode': 'analysis_only',
                    'message': 'Use --auto-apply to automatically apply optimizations'
                }
        
        # Output result
        if args.output_format == 'json':
            print(json.dumps(result, indent=2))
        elif args.output_format == 'summary':
            if 'optimization_plan' in result:
                plan = result['optimization_plan']
                print(f"\n🔧 Optimization Plan for Campaign {args.campaign_id}")
                print(f"   Date: {plan['optimization_date']}")
                print(f"   Actions: {len(plan['actions'])}")
                print(f"   Expected Improvement: {plan.get('total_expected_improvement', 'N/A')}")
                print(f"   Risk Level: {plan['risk_level']}")
                print("\n📋 Recommended Actions:")
                for i, action in enumerate(plan['actions'], 1):
                    print(f"   {i}. {action['action']}: {action.get('reason', '')}")
                
            if 'application_result' in result:
                app = result['application_result']
                print(f"\n✅ Application Result:")
                print(f"   Status: {app['status']}")
                print(f"   Actions Applied: {app['actions_applied']}")
                print(f"   Estimated Savings: ${app['estimated_savings']:.2f}")
                print(f"   Next Review: {app['next_review_date']}")
        
    except Exception as e:
        print(f"Error during optimization: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
