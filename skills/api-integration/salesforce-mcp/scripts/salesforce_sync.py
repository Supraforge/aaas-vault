#!/usr/bin/env python3
"""
Salesforce Sync Script
Synchronizes Salesforce data with other platforms
"""

import json
import csv
from datetime import datetime
from salesforce_operations import SalesforceOperations

class SalesforceSync:
    def __init__(self):
        self.sf_ops = SalesforceOperations()
    
    def export_contacts_to_csv(self, filename="salesforce_contacts.csv"):
        """Export Salesforce contacts to CSV"""
        soql = """
        SELECT Id, FirstName, LastName, Email, Phone, Title,
               Account.Name, MailingStreet, MailingCity, MailingState,
               MailingPostalCode, MailingCountry, CreatedDate
        FROM Contact
        ORDER BY LastName
        """
        contacts = self.sf_ops.query(soql)
        
        if not contacts:
            print("❌ No contacts found")
            return False
        
        # Flatten nested Account.Name
        for contact in contacts:
            if 'Account' in contact and contact['Account']:
                contact['AccountName'] = contact['Account'].get('Name', '')
            else:
                contact['AccountName'] = ''
            
        # Write to CSV
        fieldnames = ['Id', 'FirstName', 'LastName', 'Email', 'Phone', 'Title',
                     'AccountName', 'MailingStreet', 'MailingCity', 'MailingState',
                     'MailingPostalCode', 'MailingCountry', 'CreatedDate']
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for contact in contacts:
                row = {field: contact.get(field, '') for field in fieldnames}
                writer.writerow(row)
        
        print(f"✅ Exported {len(contacts)} contacts to {filename}")
        return True
    
    def sync_with_marketing_platform(self, platform="mailchimp"):
        """Sync contacts with marketing platform"""
        contacts = self.sf_ops.query("""
        SELECT Id, FirstName, LastName, Email, HasOptedOutOfEmail
        FROM Contact
        WHERE Email != null AND HasOptedOutOfEmail = false
        """)
        
        if not contacts:
            print("❌ No marketable contacts found")
            return False
        
        print(f"📧 Found {len(contacts)} marketable contacts")
        
        # Prepare data for marketing platform
        marketing_data = []
        for contact in contacts:
            marketing_data.append({
                "email": contact.get('Email'),
                "first_name": contact.get('FirstName', ''),
                "last_name": contact.get('LastName', ''),
                "salesforce_id": contact.get('Id'),
                "sync_date": datetime.now().isoformat()
            })
        
        # Export to JSON for integration
        with open(f"salesforce_to_{platform}_sync.json", 'w') as f:
            json.dump(marketing_data, f, indent=2)
        
        print(f"✅ Prepared sync data for {platform}")
        print(f"   Run integration script to upload to {platform}")
        return True
    
    def import_leads_from_csv(self, csv_file):
        """Import leads from CSV file to Salesforce"""
        import pandas as pd
        
        try:
            df = pd.read_csv(csv_file)
            print(f"📄 Reading {len(df)} leads from {csv_file}")
            
            imported = 0
            failed = 0
            
            for _, row in df.iterrows():
                lead_data = {
                    "FirstName": row.get('FirstName', ''),
                    "LastName": row.get('LastName', ''),
                    "Company": row.get('Company', 'Unknown Company'),
                    "Email": row.get('Email', ''),
                    "Phone": row.get('Phone', ''),
                    "LeadSource": row.get('LeadSource', 'Web'),
                    "Status": "New",
                    "Description": row.get('Description', '')
                }
                
                # Remove empty values
                lead_data = {k: v for k, v in lead_data.items() if pd.notna(v)}
                
                result = self.sf_ops.create_lead(lead_data)
                if result:
                    imported += 1
                else:
                    failed += 1
            
            print(f"✅ Imported {imported} leads, {failed} failed")
            return imported
            
        except Exception as e:
            print(f"❌ Import failed: {e}")
            return 0

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Salesforce Sync")
    parser.add_argument("--export-contacts", type=str, help="Export contacts to CSV file")
    parser.add_argument("--sync-marketing", type=str, help="Sync with marketing platform (mailchimp/hubspot)")
    parser.add_argument("--import-leads", type=str, help="Import leads from CSV file")
    
    args = parser.parse_args()
    
    try:
        sync = SalesforceSync()
        
        if args.export_contacts:
            sync.export_contacts_to_csv(args.export_contacts)
        
        if args.sync_marketing:
            sync.sync_with_marketing_platform(args.sync_marketing)
        
        if args.import_leads:
            sync.import_leads_from_csv(args.import_leads)
            
    except Exception as e:
        print(f"❌ Error: {e}")
