#!/usr/bin/env python3
"""
Example usage of Salesforce MCP Python scripts
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.salesforce_operations import SalesforceOperations
from scripts.salesforce_analytics import SalesforceAnalytics
from scripts.salesforce_sync import SalesforceSync

# Example 1: Basic operations
print("=== Example 1: Basic Salesforce Operations ===")
sf_ops = SalesforceOperations()

# Get sales pipeline
pipeline = sf_ops.get_sales_pipeline()
print(f"Open opportunities: {len(pipeline)}")

# Create a new lead
lead_data = {
    "FirstName": "John",
    "LastName": "Doe",
    "Company": "Example Corp",
    "Email": "john.doe@example.com",
    "Phone": "+1-555-0123",
    "LeadSource": "Web",
    "Status": "New",
    "Description": "From website contact form"
}
# result = sf_ops.create_lead(lead_data)
# print(f"Lead created: {result}")

# Example 2: Analytics
print("\n=== Example 2: Sales Analytics ===")
analytics = SalesforceAnalytics()

# Get conversion rate
conversion = analytics.calculate_conversion_rate()
print(f"Conversion rate (90 days): {conversion['conversion_rate']}%")

# Get sales velocity
velocity = analytics.sales_velocity()
print(f"Sales velocity: ${velocity['sales_velocity']:,.2f}")

# Example 3: Data sync
print("\n=== Example 3: Data Synchronization ===")
sync = SalesforceSync()

# Export contacts to CSV
# sync.export_contacts_to_csv("salesforce_contacts_export.csv")

# Sync with marketing platform
# sync.sync_with_marketing_platform("mailchimp")

print("\n✅ Examples completed (commented out actual API calls)")
