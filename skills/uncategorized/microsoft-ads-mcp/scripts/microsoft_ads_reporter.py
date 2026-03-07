#!/usr/bin/env python3
"""
Microsoft Ads Reporter - Performance reporting and analytics
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from microsoft_ads_manager import MicrosoftAdsManager


def generate_performance_report(campaign_id: str, days: int = 30, output_format: str = 'json') -> dict:
    """Generate comprehensive performance report"""
    manager = MicrosoftAdsManager()
    
    # Get performance data
    performance = manager.get_campaign_performance(campaign_id, days)
    
    # Generate insights
    insights = {
        'performance_summary': {
            'ctr_status': 'Good' if performance['metrics']['ctr'] >= 2.0 else 'Needs Improvement',
            'conversion_status': 'Good' if performance['metrics']['conversion_rate'] >= 3.0 else 'Needs Improvement',
            'roas_status': 'Good' if performance['metrics']['roas'] >= 300 else 'Needs Improvement',
            'overall_score': 85  # Example score
        },
        'key_metrics': performance['metrics'],
        'trends': performance['trends'],
        'recommendations': performance['recommendations'],
        'comparison_benchmarks': {
            'industry_average_ctr': 1.8,
            'industry_average_cpc': 5.25,
            'industry_average_conversion_rate': 3.5
        }
    }
    
    # Add comparison to benchmarks
    insights['vs_benchmarks'] = {
        'ctr_vs_industry': f"{((performance['metrics']['ctr'] / insights['comparison_benchmarks']['industry_average_ctr']) - 1) * 100:.1f}%",
        'cpc_vs_industry': f"{((performance['metrics']['average_cpc'] / insights['comparison_benchmarks']['industry_average_cpc']) - 1) * 100:.1f}%",
        'conversion_vs_industry': f"{((performance['metrics']['conversion_rate'] / insights['comparison_benchmarks']['industry_average_conversion_rate']) - 1) * 100:.1f}%"
    }
    
    return insights


def create_visualization(performance_data: dict, output_path: str):
    """Create visualization of performance data"""
    metrics = performance_data['metrics']
    
    # Create bar chart for key metrics
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # CTR and Conversion Rate
    axes[0, 0].bar(['CTR', 'Conversion Rate'], 
                   [metrics['ctr'], metrics['conversion_rate']], 
                   color=['blue', 'green'])
    axes[0, 0].set_title('Engagement Metrics')
    axes[0, 0].set_ylabel('Percentage (%)')
    
    # Cost and Revenue
    axes[0, 1].bar(['Cost', 'Revenue'], 
                   [metrics['cost'], metrics['revenue']], 
                   color=['red', 'green'])
    axes[0, 1].set_title('Financial Metrics')
    axes[0, 1].set_ylabel('Amount ($)')
    
    # Impressions and Clicks
    axes[1, 0].bar(['Impressions', 'Clicks'], 
                   [metrics['impressions'] / 1000, metrics['clicks']], 
                   color=['gray', 'orange'])
    axes[1, 0].set_title('Volume Metrics')
    axes[1, 0].set_ylabel('Count (impressions in thousands)')
    
    # ROAS
    axes[1, 1].bar(['ROAS'], [metrics['roas']], color='purple')
    axes[1, 1].set_title('Return on Ad Spend')
    axes[1, 1].set_ylabel('Percentage (%)')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return output_path


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Microsoft Ads Performance Reporter')
    parser.add_argument('--campaign-id', required=True, help='Campaign ID')
    parser.add_argument('--days', type=int, default=30, help='Number of days to analyze')
    parser.add_argument('--output-format', choices=['json', 'csv', 'html', 'visual'], default='json',
                       help='Output format')
    parser.add_argument('--output-file', help='Output file path')
    
    args = parser.parse_args()
    
    try:
        # Generate report
        report = generate_performance_report(args.campaign_id, args.days)
        
        # Output based on format
        if args.output_format == 'json':
            output = json.dumps(report, indent=2)
            output_file = args.output_file or f'reports/performance_{args.campaign_id}_{datetime.now().strftime("%Y%m%d")}.json'
            
        elif args.output_format == 'csv':
            # Convert metrics to CSV
            df = pd.DataFrame([report['key_metrics']])
            output = df.to_csv(index=False)
            output_file = args.output_file or f'reports/performance_{args.campaign_id}_{datetime.now().strftime("%Y%m%d")}.csv'
            
        elif args.output_format == 'html':
            # Create HTML report
            html_template = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Microsoft Ads Performance Report</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    .metric {{ margin: 20px 0; padding: 15px; border-left: 4px solid #0078d4; }}
                    .good {{ border-color: #107c10; }}
                    .warning {{ border-color: #ffb900; }}
                    .critical {{ border-color: #d13438; }}
                </style>
            </head>
            <body>
                <h1>Microsoft Ads Performance Report</h1>
                <p>Campaign: {args.campaign_id}</p>
                <p>Date Range: Last {args.days} days</p>
                
                <h2>Key Metrics</h2>
                <div class="metric">
                    <h3>CTR: {report['key_metrics']['ctr']}%</h3>
                    <p>Status: {report['performance_summary']['ctr_status']}</p>
                </div>
                
                <div class="metric">
                    <h3>Conversion Rate: {report['key_metrics']['conversion_rate']}%</h3>
                    <p>Status: {report['performance_summary']['conversion_status']}</p>
                </div>
                
                <div class="metric">
                    <h3>ROAS: {report['key_metrics']['roas']}%</h3>
                    <p>Status: {report['performance_summary']['roas_status']}</p>
                </div>
                
                <h2>Recommendations</h2>
                <ul>
            """
            
            for rec in report['recommendations']:
                html_template += f'<li>{rec}</li>\n'
            
            html_template += """
                </ul>
                
                <h2>vs Industry Benchmarks</h2>
                <p>CTR: {report['vs_benchmarks']['ctr_vs_industry']} vs industry average</p>
                <p>CPC: {report['vs_benchmarks']['cpc_vs_industry']} vs industry average</p>
                <p>Conversion Rate: {report['vs_benchmarks']['conversion_vs_industry']} vs industry average</p>
                
                <p><em>Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</em></p>
            </body>
            </html>
            """
            
            output = html_template
            output_file = args.output_file or f'reports/performance_{args.campaign_id}_{datetime.now().strftime("%Y%m%d")}.html'
            
        elif args.output_format == 'visual':
            # Create visualization
            output_file = args.output_file or f'reports/performance_{args.campaign_id}_{datetime.now().strftime("%Y%m%d")}.png'
            Path('reports').mkdir(exist_ok=True)
            
            visualization_path = create_visualization(report, output_file)
            print(f"Visualization saved to: {visualization_path}")
            return
        
        # Ensure reports directory exists
        Path('reports').mkdir(exist_ok=True)
        
        # Write output
        with open(output_file, 'w') as f:
            f.write(output)
        
        print(f"Report saved to: {output_file}")
        
        # Also print summary to console
        print(f"\n📊 Performance Summary for Campaign {args.campaign_id}:")
        print(f"   CTR: {report['key_metrics']['ctr']}% ({report['performance_summary']['ctr_status']})")
        print(f"   Conversion Rate: {report['key_metrics']['conversion_rate']}% ({report['performance_summary']['conversion_status']})")
        print(f"   ROAS: {report['key_metrics']['roas']}% ({report['performance_summary']['roas_status']})")
        print(f"   Overall Score: {report['performance_summary']['overall_score']}/100")
        
    except Exception as e:
        print(f"Error generating report: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
