#!/usr/bin/env python3
"""
CRM Integration Script

Handles import/export of leads to various CRM systems.
"""

import os
import json
import csv
import argparse
from typing import List, Dict, Any

try:
    from simple_salesforce import Salesforce
    HAS_SALESFORCE = True
except ImportError:
    HAS_SALESFORCE = False

try:
    from hubspot import HubSpot
    HAS_HUBSPOT = True
except ImportError:
    HAS_HUBSPOT = False

class CRMIntegrator:
    """Integrate with various CRM systems"""

    def __init__(self, crm_type: str = "salesforce"):
        self.crm_type = crm_type
        self.client = None

        if crm_type == "salesforce" and HAS_SALESFORCE:
            self._init_salesforce()
        elif crm_type == "hubspot" and HAS_HUBSPOT:
            self._init_hubspot()

    def _init_salesforce(self):
        """Initialize Salesforce connection"""
        client_id = os.getenv("SALESFORCE_CLIENT_ID")
        client_secret = os.getenv("SALESFORCE_CLIENT_SECRET")
        username = os.getenv("SALESFORCE_USERNAME")
        password = os.getenv("SALESFORCE_PASSWORD")

        if all([client_id, client_secret, username, password]):
            self.client = Salesforce(
                client_id=client_id,
                client_secret=client_secret,
                username=username,
                password=password
            )
            print("Salesforce connection initialized")
        else:
            print("Salesforce credentials not fully configured")

    def _init_hubspot(self):
        """Initialize HubSpot connection"""
        api_key = os.getenv("HUBSPOT_API_KEY")
        if api_key:
            self.client = HubSpot(api_key=api_key)
            print("HubSpot connection initialized")
        else:
            print("HubSpot API key not configured")

    def import_leads(self, filepath: str) -> List[Dict]:
        """Import leads from file"""
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            return []

        leads = []
        if filepath.endswith(".csv"):
            with open(filepath, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                leads = list(reader)
        elif filepath.endswith(".json"):
            with open(filepath, "r", encoding="utf-8") as f:
                leads = json.load(f)
        else:
            print(f"Unsupported file format: {filepath}")
            return []

        print(f"Imported {len(leads)} leads from {filepath}")
        return leads

    def export_to_crm(self, leads: List[Dict]) -> Dict[str, Any]:
        """Export leads to CRM"""
        if not self.client:
            return {"success": False, "message": "CRM client not initialized"}

        results = {
            "total": len(leads),
            "successful": 0,
            "failed": 0,
            "errors": []
        }

        # This is a simplified example
        # In reality, you would make API calls to the CRM
        for lead in leads:
            try:
                # Mock CRM export
                print(f"Exporting lead: {lead.get('name', 'Unknown')}")
                results["successful"] += 1
            except Exception as e:
                results["failed"] += 1
                results["errors"].append(str(e))

        return results

    def map_fields(self, lead: Dict, mapping: Dict) -> Dict:
        """Map lead fields to CRM fields"""
        mapped = {}
        for crm_field, lead_field in mapping.items():
            if lead_field in lead:
                mapped[crm_field] = lead[lead_field]
            elif lead_field == "full_name" and "first_name" in lead and "last_name" in lead:
                mapped[crm_field] = f"{lead['first_name']} {lead['last_name']}"
            elif lead_field == "email" and "email" in lead:
                mapped[crm_field] = lead["email"]

        return mapped

def main():
    parser = argparse.ArgumentParser(description="CRM Integration")
    parser.add_argument("--import", dest="import_file", help="File to import leads from")
    parser.add_argument("--crm", choices=["salesforce", "hubspot"], default="salesforce",
                       help="CRM system to use")
    parser.add_argument("--export", action="store_true", help="Export to CRM")
    parser.add_argument("--map", help="Field mapping JSON file")

    args = parser.parse_args()

    integrator = CRMIntegrator(args.crm)

    if args.import_file:
        leads = integrator.import_leads(args.import_file)

        if args.export and leads:
            results = integrator.export_to_crm(leads)
            print(f"
Export Results:")
            print(f"  Total: {results['total']}")
            print(f"  Successful: {results['successful']}")
            print(f"  Failed: {results['failed']}")

            if results["errors"]:
                print(f"  Errors: {results['errors'][:5]}")  # Show first 5 errors
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
