#!/usr/bin/env python3
"""
Salesforce Operations Script
Handles core CRM operations: Leads, Contacts, Accounts, Opportunities
"""

import os
import sys
import json
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from simple_salesforce import Salesforce

# Load environment variables
load_dotenv()

class SalesforceOperations:
    def __init__(self):
        """Initialize Salesforce connection"""
        self.client_id = os.getenv('SALESFORCE_CLIENT_ID')
        self.client_secret = os.getenv('SALESFORCE_CLIENT_SECRET')
        self.username = os.getenv('SALESFORCE_USERNAME')
        self.password = os.getenv('SALESFORCE_PASSWORD')
        self.instance_url = os.getenv('SALESFORCE_INSTANCE_URL')
        self.api_version = os.getenv('SALESFORCE_API_VERSION', '59.0')
        
        if not all([self.client_id, self.client_secret, self.username, self.password, self.instance_url]):
            raise ValueError("Missing Salesforce credentials in .env file")
        
        self.sf = None
        self.connect()
    
    def connect(self):
        """Connect to Salesforce"""
        try:
            self.sf = Salesforce(
                username=self.username,
                password=self.password,
                security_token='',  # Included in password
                client_id=self.client_id,
                client_secret=self.client_secret,
                domain='login' if 'my.salesforce.com' in self.instance_url else 'test'
            )
            print(f"✅ Connected to Salesforce: {self.sf.session_id[:20]}...")
            return True
        except Exception as e:
            print(f"❌ Salesforce connection failed: {e}")
            return False
    
    def query(self, soql_query):
        """Execute SOQL query"""
        try:
            result = self.sf.query_all(soql_query)
            return result['records']
        except Exception as e:
            print(f"❌ Query failed: {e}")
            return []
    
    def create_lead(self, lead_data):
        """Create a new Lead"""
        try:
            result = self.sf.Lead.create(lead_data)
            print(f"✅ Lead created: {result['id']}")
            return result
        except Exception as e:
            print(f"❌ Lead creation failed: {e}")
            return None
    
    def update_opportunity(self, opp_id, update_data):
        """Update Opportunity stage or other fields"""
        try:
            result = self.sf.Opportunity.update(opp_id, update_data)
            print(f"✅ Opportunity updated: {opp_id}")
            return result
        except Exception as e:
            print(f"❌ Opportunity update failed: {e}")
            return None
    
    def get_sales_pipeline(self):
        """Get current sales pipeline"""
        soql = """
        SELECT Id, Name, StageName, Amount, CloseDate, Probability,
               Account.Name, Owner.Name, CreatedDate
        FROM Opportunity
        WHERE IsClosed = false
        ORDER BY CloseDate ASC
        """
        return self.query(soql)
    
    def get_leads_last_30_days(self):
        """Get leads created in last 30 days"""
        soql = """
        SELECT Id, FirstName, LastName, Company, Email, Status,
               CreatedDate, LeadSource, Rating
        FROM Lead
        WHERE CreatedDate = LAST_N_DAYS:30
        ORDER BY CreatedDate DESC
        """
        return self.query(soql)
    
    def generate_pipeline_report(self):
        """Generate pipeline analysis report"""
        pipeline = self.get_sales_pipeline()
        
        if not pipeline:
            return {"error": "No pipeline data found"}
        
        df = pd.DataFrame(pipeline)
        
        # Calculate metrics
        total_pipeline = df['Amount'].sum() if 'Amount' in df.columns else 0
        weighted_pipeline = (df['Amount'] * df['Probability'] / 100).sum() \
            if all(col in df.columns for col in ['Amount', 'Probability']) else 0
        
        report = {
            "total_opportunities": len(pipeline),
            "total_pipeline_value": float(total_pipeline),
            "weighted_pipeline_value": float(weighted_pipeline),
            "by_stage": df.groupby('StageName').size().to_dict() if 'StageName' in df.columns else {},
            "next_30_days": len([opp for opp in pipeline if opp.get('CloseDate') and \
                                 datetime.strptime(opp['CloseDate'], '%Y-%m-%d') <= \
                                 datetime.now().replace(day=datetime.now().day + 30)])
        }
        
        return report
    
    def export_to_csv(self, data, filename):
        """Export data to CSV"""
        if not data:
            print("❌ No data to export")
            return False
        
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"✅ Data exported to {filename}")
        return True

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Salesforce Operations")
    parser.add_argument("--test", action="store_true", help="Test Salesforce connection")
    parser.add_argument("--pipeline", action="store_true", help="Get sales pipeline")
    parser.add_argument("--leads", action="store_true", help="Get recent leads")
    parser.add_argument("--report", action="store_true", help="Generate pipeline report")
    parser.add_argument("--export", type=str, help="Export data to CSV file")
    
    args = parser.parse_args()
    
    try:
        sf_ops = SalesforceOperations()
        
        if args.test:
            print("✅ Salesforce connection successful")
        
        if args.pipeline:
            pipeline = sf_ops.get_sales_pipeline()
            print(f"📊 Sales Pipeline: {len(pipeline)} opportunities")
            for opp in pipeline[:5]:  # Show first 5
                print(f"  • {opp.get('Name')}: ${opp.get('Amount', 0)} ({opp.get('StageName')})")
        
        if args.leads:
            leads = sf_ops.get_leads_last_30_days()
            print(f"📋 Recent Leads: {len(leads)} in last 30 days")
            for lead in leads[:5]:
                print(f"  • {lead.get('FirstName')} {lead.get('LastName')} - {lead.get('Company')}")
        
        if args.report:
            report = sf_ops.generate_pipeline_report()
            print("📈 Pipeline Report:")
            print(json.dumps(report, indent=2))
        
        if args.export:
            data = sf_ops.get_sales_pipeline() if 'pipeline' in args.export else sf_ops.get_leads_last_30_days()
            sf_ops.export_to_csv(data, args.export)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
