#!/usr/bin/env python3
"""
Google Ads Reporter - Advanced reporting and analytics
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.google_ads_manager import GoogleAdsManager
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def generate_detailed_report():
    """Generate detailed performance report with visualizations"""
    manager = GoogleAdsManager()
    campaigns = manager.get_campaigns()
    
    if not campaigns:
        print("No campaigns found")
        return
    
    # Create DataFrame for analysis
    df = pd.DataFrame([{
        'Campaign': c.name,
        'Status': c.status,
        'Clicks': c.clicks,
        'Impressions': c.impressions,
        'Cost': c.cost,
        'Conversions': c.conversions,
        'CTR': c.ctr,
        'CPC': c.cpc,
        'Conversion Rate': c.conversion_rate,
        'ROAS': c.roas
    } for c in campaigns])
    
    # Generate summary
    print("\n📊 Google Ads Performance Summary")
    print("=" * 50)
    print(f"Total Campaigns: {len(df)}")
    print(f"Active Campaigns: {len(df[df['Status'] == 'ENABLED'])}")
    print(f"Total Spend: ${df['Cost'].sum():.2f}")
    print(f"Total Clicks: {df['Clicks'].sum():,}")
    print(f"Total Conversions: {df['Conversions'].sum():.0f}")
    print(f"Average CTR: {df['CTR'].mean():.2%}")
    print(f"Average CPC: ${df['CPC'].mean():.2f}")
    print(f"Average ROAS: {df['ROAS'].mean():.2f}")
    
    # Identify top performers
    top_roas = df.nlargest(3, 'ROAS')
    print("\n🏆 Top 3 Campaigns by ROAS:")
    for _, row in top_roas.iterrows():
        print(f"  • {row['Campaign']}: ROAS = {row['ROAS']:.2f}, Cost = ${row['Cost']:.2f}")
    
    # Identify underperformers
    low_ctr = df[df['CTR'] < 0.01]
    if len(low_ctr) > 0:
        print("\n⚠️  Campaigns with Low CTR (<1%):")
        for _, row in low_ctr.iterrows():
            print(f"  • {row['Campaign']}: CTR = {row['CTR']:.2%}")
    
    # Save to CSV
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_file = f"google_ads_detailed_report_{timestamp}.csv"
    df.to_csv(csv_file, index=False)
    print(f"\n💾 Detailed report saved to: {csv_file}")
    
    return csv_file

def create_performance_charts():
    """Create performance visualization charts"""
    manager = GoogleAdsManager()
    campaigns = manager.get_campaigns()
    
    if len(campaigns) < 2:
        print("Need at least 2 campaigns for charts")
        return
    
    # Prepare data
    names = [c.name[:20] + '...' if len(c.name) > 20 else c.name for c in campaigns]
    costs = [c.cost for c in campaigns]
    roas_values = [c.roas for c in campaigns]
    ctr_values = [c.ctr * 100 for c in campaigns]  # Convert to percentage
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Google Ads Performance Dashboard', fontsize=16)
    
    # 1. Cost by Campaign
    axes[0, 0].bar(names, costs, color='skyblue')
    axes[0, 0].set_title('Cost by Campaign')
    axes[0, 0].set_ylabel('Cost ($)')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. ROAS by Campaign
    axes[0, 1].bar(names, roas_values, color='lightgreen')
    axes[0, 1].set_title('ROAS by Campaign')
    axes[0, 1].set_ylabel('ROAS')
    axes[0, 1].axhline(y=1.0, color='red', linestyle='--', alpha=0.5)
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # 3. CTR by Campaign
    axes[1, 0].bar(names, ctr_values, color='gold')
    axes[1, 0].set_title('CTR by Campaign')
    axes[1, 0].set_ylabel('CTR (%)')
    axes[1, 0].axhline(y=2.0, color='green', linestyle='--', alpha=0.5)
    axes[1, 0].tick_params(axis='x', rotation=45)
    
    # 4. Cost vs ROAS scatter
    axes[1, 1].scatter(costs, roas_values, s=100, alpha=0.6, edgecolors='black')
    axes[1, 1].set_title('Cost vs ROAS')
    axes[1, 1].set_xlabel('Cost ($)')
    axes[1, 1].set_ylabel('ROAS')
    axes[1, 1].axhline(y=1.0, color='red', linestyle='--', alpha=0.5)
    
    # Add campaign labels to scatter plot
    for i, name in enumerate(names):
        axes[1, 1].annotate(name, (costs[i], roas_values[i]), fontsize=8)
    
    plt.tight_layout()
    
    # Save chart
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    chart_file = f"google_ads_charts_{timestamp}.png"
    plt.savefig(chart_file, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"📊 Charts saved to: {chart_file}")
    return chart_file

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Google Ads Reporter")
    parser.add_argument("--report", action="store_true", help="Generate detailed report")
    parser.add_argument("--charts", action="store_true", help="Create performance charts")
    
    args = parser.parse_args()
    
    if args.report:
        generate_detailed_report()
    elif args.charts:
        create_performance_charts()
    else:
        parser.print_help()
