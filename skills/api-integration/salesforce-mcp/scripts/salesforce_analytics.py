#!/usr/bin/env python3
"""
Salesforce Analytics Script
Generates business intelligence reports and dashboards
"""

import json
import pandas as pd
from datetime import datetime, timedelta
from salesforce_operations import SalesforceOperations

class SalesforceAnalytics:
    def __init__(self):
        self.sf_ops = SalesforceOperations()
    
    def calculate_conversion_rate(self, days=90):
        """Calculate lead to opportunity conversion rate"""
        # Get leads created in specified period
        soql = f"""
        SELECT Id, ConvertedDate, ConvertedOpportunityId
        FROM Lead
        WHERE CreatedDate = LAST_N_DAYS:{days}
        """
        leads = self.sf_ops.query(soql)
        
        converted = [lead for lead in leads if lead.get('ConvertedDate')]
        conversion_rate = (len(converted) / len(leads)) * 100 if leads else 0
        
        return {
            "total_leads": len(leads),
            "converted_leads": len(converted),
            "conversion_rate": round(conversion_rate, 2),
            "period_days": days
        }
    
    def sales_velocity(self):
        """Calculate sales velocity: (Pipeline × Win Rate × Deal Size) / Sales Cycle Length"""
        # Get won opportunities in last 90 days
        soql = """
        SELECT Id, Amount, CreatedDate, CloseDate
        FROM Opportunity
        WHERE StageName = 'Closed Won'
        AND CloseDate = LAST_N_DAYS:90
        """
        won_opps = self.sf_ops.query(soql)
        
        if not won_opps:
            return {"error": "No won opportunities in last 90 days"}
        
        # Calculate metrics
        total_won = sum(float(opp.get('Amount', 0)) for opp in won_opps)
        avg_deal_size = total_won / len(won_opps)
        
        # Calculate average sales cycle (in days)
        cycles = []
        for opp in won_opps:
            if opp.get('CreatedDate') and opp.get('CloseDate'):
                created = datetime.strptime(opp['CreatedDate'][:10], '%Y-%m-%d')
                closed = datetime.strptime(opp['CloseDate'][:10], '%Y-%m-%d')
                cycles.append((closed - created).days)
        
        avg_cycle = sum(cycles) / len(cycles) if cycles else 30
        
        # Get total pipeline
        pipeline = self.sf_ops.get_sales_pipeline()
        total_pipeline = sum(float(opp.get('Amount', 0)) for opp in pipeline) if pipeline else 0
        
        # Estimate win rate (simplified)
        win_rate = 0.25  # Default 25%, should be calculated from historical data
        
        # Sales velocity formula
        velocity = (total_pipeline * win_rate * avg_deal_size) / avg_cycle
        
        return {
            "sales_velocity": round(velocity, 2),
            "avg_deal_size": round(avg_deal_size, 2),
            "avg_sales_cycle_days": round(avg_cycle, 2),
            "estimated_win_rate": win_rate,
            "total_pipeline": round(total_pipeline, 2),
            "won_opportunities_last_90_days": len(won_opps)
        }
    
    def forecast_accuracy(self):
        """Analyze forecast accuracy"""
        # Get opportunities closed in last quarter
        soql = """
        SELECT Id, Name, Amount, ForecastCategory, StageName,
               CloseDate, Probability, CreatedDate
        FROM Opportunity
        WHERE CloseDate = LAST_QUARTER
        """
        opps = self.sf_ops.query(soql)
        
        if not opps:
            return {"error": "No opportunities in last quarter"}
        
        df = pd.DataFrame(opps)
        
        # Calculate forecast accuracy
        forecasted = df[df['ForecastCategory'].isin(['Pipeline', 'Best Case', 'Commit', 'Omitted'])]
        actual_won = df[df['StageName'] == 'Closed Won']
        
        accuracy = len(actual_won) / len(forecasted) * 100 if len(forecasted) > 0 else 0
        
        return {
            "total_opportunities": len(opps),
            "forecasted_opportunities": len(forecasted),
            "actual_won_opportunities": len(actual_won),
            "forecast_accuracy_percentage": round(accuracy, 2),
            "total_forecasted_amount": forecasted['Amount'].sum() if 'Amount' in forecasted.columns else 0,
            "actual_won_amount": actual_won['Amount'].sum() if 'Amount' in actual_won.columns else 0
        }
    
    def generate_executive_dashboard(self):
        """Generate comprehensive executive dashboard"""
        dashboard = {
            "timestamp": datetime.now().isoformat(),
            "pipeline_report": self.sf_ops.generate_pipeline_report(),
            "conversion_metrics": self.calculate_conversion_rate(),
            "sales_velocity": self.sales_velocity(),
            "forecast_accuracy": self.forecast_accuracy(),
            "key_performance_indicators": {
                "quarterly_target": 1000000,  # Example
                "ytd_revenue": 750000,  # Example
                "customer_acquisition_cost": 500,  # Example
                "customer_lifetime_value": 5000  # Example
            }
        }
        
        return dashboard

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Salesforce Analytics")
    parser.add_argument("--conversion", action="store_true", help="Calculate conversion rate")
    parser.add_argument("--velocity", action="store_true", help="Calculate sales velocity")
    parser.add_argument("--forecast", action="store_true", help="Analyze forecast accuracy")
    parser.add_argument("--dashboard", action="store_true", help="Generate executive dashboard")
    parser.add_argument("--export", type=str, help="Export dashboard to JSON file")
    
    args = parser.parse_args()
    
    try:
        analytics = SalesforceAnalytics()
        
        if args.conversion:
            result = analytics.calculate_conversion_rate()
            print("📊 Conversion Metrics:")
            print(json.dumps(result, indent=2))
        
        if args.velocity:
            result = analytics.sales_velocity()
            print("🚀 Sales Velocity:")
            print(json.dumps(result, indent=2))
        
        if args.forecast:
            result = analytics.forecast_accuracy()
            print("🎯 Forecast Accuracy:")
            print(json.dumps(result, indent=2))
        
        if args.dashboard:
            dashboard = analytics.generate_executive_dashboard()
            print("📈 Executive Dashboard:")
            print(json.dumps(dashboard, indent=2))
            
            if args.export:
                with open(args.export, 'w') as f:
                    json.dump(dashboard, f, indent=2)
                print(f"✅ Dashboard exported to {args.export}")
                
    except Exception as e:
        print(f"❌ Error: {e}")
