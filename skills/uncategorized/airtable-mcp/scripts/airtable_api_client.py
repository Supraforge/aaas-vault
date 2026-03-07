#!/usr/bin/env python3
"""
Airtable API Client for Python
"""
import os
import json
import requests
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime

@dataclass
class AirtableConfig:
    """Airtable configuration"""
    api_key: str
    base_id: str
    
class AirtableClient:
    """Airtable API client"""
    
    def __init__(self, config: AirtableConfig):
        self.config = config
        self.base_url = f"https://api.airtable.com/v0/{config.base_id}"
        self.headers = {
            "Authorization": f"Bearer {config.api_key}",
            "Content-Type": "application/json"
        }
    
    def list_tables(self) -> List[Dict[str, Any]]:
        """List all tables in the base"""
        # Note: Airtable API doesn't have a direct endpoint to list tables
        # This is a placeholder - in practice you need to know table names
        return [
            {"name": "Customers", "id": "tblCustomers"},
            {"name": "Products", "id": "tblProducts"},
            {"name": "Orders", "id": "tblOrders"},
            {"name": "Leads", "id": "tblLeads"},
        ]
    
    def get_records(self, table_name: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Get records from a table"""
        url = f"{self.base_url}/{table_name}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def create_record(self, table_name: str, fields: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new record"""
        url = f"{self.base_url}/{table_name}"
        data = {"fields": fields}
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()
    
    def update_record(self, table_name: str, record_id: str, fields: Dict[str, Any]) -> Dict[str, Any]:
        """Update an existing record"""
        url = f"{self.base_url}/{table_name}/{record_id}"
        data = {"fields": fields}
        response = requests.patch(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()
    
    def delete_record(self, table_name: str, record_id: str) -> bool:
        """Delete a record"""
        url = f"{self.base_url}/{table_name}/{record_id}"
        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()
        return True
    
    def search_records(self, table_name: str, formula: str) -> Dict[str, Any]:
        """Search records using Airtable formula"""
        url = f"{self.base_url}/{table_name}"
        params = {"filterByFormula": formula}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def export_to_csv(self, table_name: str, output_path: str) -> str:
        """Export table data to CSV"""
        records = self.get_records(table_name)
        
        if not records.get("records"):
            return "No records found"
        
        # Get field names from first record
        first_record = records["records"][0]
        field_names = list(first_record["fields"].keys())
        
        # Create CSV content
        csv_lines = [",".join(["ID"] + field_names)]
        
        for record in records["records"]:
            row = [record["id"]]
            for field in field_names:
                value = record["fields"].get(field, "")
                # Handle special characters
                if isinstance(value, str):
                    value = value.replace("\"", "\"\"")
                    if "," in value or "\"" in value:
                        value = f'"{value}"'
                row.append(str(value))
            csv_lines.append(",".join(row))
        
        csv_content = "\n".join(csv_lines)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(csv_content)
        
        return f"Exported {len(records['records'])} records to {output_path}"

def main():
    """Main function for command line usage"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Airtable API Client")
    parser.add_argument("--table", required=True, help="Table name")
    parser.add_argument("--action", required=True, 
                       choices=["list", "get", "create", "update", "delete", "search", "export"],
                       help="Action to perform")
    parser.add_argument("--record-id", help="Record ID for update/delete")
    parser.add_argument("--fields", help="Fields as JSON string")
    parser.add_argument("--formula", help="Airtable formula for search")
    parser.add_argument("--output", help="Output file for export")
    
    args = parser.parse_args()
    
    # Load config from environment
    api_key = os.getenv("AIRTABLE_TOKEN")
    base_id = os.getenv("AIRTABLE_BASE_ID")
    
    if not api_key or not base_id:
        print("Error: AIRTABLE_TOKEN and AIRTABLE_BASE_ID must be set in environment")
        return
    
    config = AirtableConfig(api_key=api_key, base_id=base_id)
    client = AirtableClient(config)
    
    try:
        if args.action == "list":
            tables = client.list_tables()
            print(json.dumps(tables, indent=2))
            
        elif args.action == "get":
            records = client.get_records(args.table)
            print(json.dumps(records, indent=2))
            
        elif args.action == "create":
            if not args.fields:
                print("Error: --fields required for create action")
                return
            fields = json.loads(args.fields)
            result = client.create_record(args.table, fields)
            print(json.dumps(result, indent=2))
            
        elif args.action == "update":
            if not args.record_id or not args.fields:
                print("Error: --record-id and --fields required for update action")
                return
            fields = json.loads(args.fields)
            result = client.update_record(args.table, args.record_id, fields)
            print(json.dumps(result, indent=2))
            
        elif args.action == "delete":
            if not args.record_id:
                print("Error: --record-id required for delete action")
                return
            success = client.delete_record(args.table, args.record_id)
            print(json.dumps({"success": success}, indent=2))
            
        elif args.action == "search":
            if not args.formula:
                print("Error: --formula required for search action")
                return
            result = client.search_records(args.table, args.formula)
            print(json.dumps(result, indent=2))
            
        elif args.action == "export":
            if not args.output:
                print("Error: --output required for export action")
                return
            result = client.export_to_csv(args.table, args.output)
            print(result)
            
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
