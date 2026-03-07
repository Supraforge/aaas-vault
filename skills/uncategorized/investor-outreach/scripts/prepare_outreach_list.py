#!/usr/bin/env python3
import json
import pandas as pd
import argparse
from pathlib import Path

def convert_to_outreach_csv(json_path, output_csv):
    """
    Converts Apify/Discovery JSON to a clean CSV for the mailing bridge.
    """
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    rows = []
    for item in data:
        # Apify 'startup-investor-scraper' often returns firm names and generic info
        # You will likely need to manually add the 'email' and 'contact_name' 
        # unless enriched by another tool.
        rows.append({
            "firm_name": item.get('name'),
            "name": "[Add Partner Name]", # Placeholder for manual entry
            "email": "[Add Email]",        # Placeholder for manual entry
            "hq": item.get('hq'),
            "focus": item.get('focus')
        })
    
    df = pd.DataFrame(rows)
    df.to_csv(output_csv, index=False)
    print(f"✅ Created outreach template at {output_csv}")
    print("👉 Action Required: Open the CSV and fill in the 'name' and 'email' columns for the partners you want to hit.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="investor_outreach_list.csv")
    args = parser.parse_args()
    convert_to_outreach_csv(args.input, args.output)
