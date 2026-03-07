#!/usr/bin/env python3
"""
HubSpot CRM Operations Script
Handles contacts, companies, deals, and CRM data management
"""

import os
import sys
import json
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from hubspot import HubSpot

# Load environment variables
load_dotenv()

class HubSpotCRM:
    def __init__(self):
        self.access_token = os.getenv('HUBSPOT_ACCESS_TOKEN')
        self.portal_id = os.getenv('HUBSPOT_PORTAL_ID')
        
        if not self.access_token:
            raise ValueError("HUBSPOT_ACCESS_TOKEN not found in .env")
        
        # Initialize HubSpot client
        self.client = HubSpot(access_token=self.access_token)
    
    def get_contacts(self, limit=100, properties=None):
        """Retrieve contacts from HubSpot"""
        try:
            if properties is None:
                properties = ["email", "firstname", "lastname", "company", "phone"]
            
            response = self.client.crm.contacts.get_all(
                limit=limit,
                properties=properties
            )
            return response.results
        except Exception as e:
            print(f"Error fetching contacts: {e}")
            return []
    
    def create_contact(self, contact_data):
        """Create a new contact in HubSpot"""
        try:
            contact = self.client.crm.contacts.basic_api.create(
                simple_public_object_input=contact_data
            )
            print(f"Contact created: {contact.id}")
            return contact
        except Exception as e:
            print(f"Error creating contact: {e}")
            return None
    
    def get_companies(self, limit=100):
        """Retrieve companies from HubSpot"""
        try:
            response = self.client.crm.companies.get_all(limit=limit)
            return response.results
        except Exception as e:
            print(f"Error fetching companies: {e}")
            return []
    
    def get_deals(self, limit=100):
        """Retrieve deals from HubSpot"""
        try:
            response = self.client.crm.deals.get_all(limit=limit)
            return response.results
        except Exception as e:
            print(f"Error fetching deals: {e}")
            return []
    
    def export_contacts_to_csv(self, filename="hubspot_contacts_export.csv"):
        """Export contacts to CSV file"""
        try:
            contacts = self.get_contacts(limit=1000)
            
            if not contacts:
                print("No contacts found to export")
                return False
            
            # Convert to DataFrame
            data = []
            for contact in contacts:
                contact_dict = {
                    "id": contact.id,
                    "email": contact.properties.get("email", ""),
                    "first_name": contact.properties.get("firstname", ""),
                    "last_name": contact.properties.get("lastname", ""),
                    "company": contact.properties.get("company", ""),
                    "phone": contact.properties.get("phone", ""),
                    "created_at": contact.created_at,
                    "updated_at": contact.updated_at
                }
                data.append(contact_dict)
            
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)
            print(f"Exported {len(data)} contacts to {filename}")
            return True
            
        except Exception as e:
            print(f"Error exporting contacts: {e}")
            return False

if __name__ == "__main__":
    # Example usage
    crm = HubSpotCRM()
    
    # Get and display contacts
    contacts = crm.get_contacts(limit=10)
    print(f"Found {len(contacts)} contacts")
    
    # Export to CSV
    crm.export_contacts_to_csv()
