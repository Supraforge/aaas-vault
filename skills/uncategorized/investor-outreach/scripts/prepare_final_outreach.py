#!/usr/bin/env python3
import json
import pandas as pd
from pathlib import Path

def generate_csv():
    enriched_file = Path("/Users/user/.gemini/[PROJECT_NAME]/skills/investor-discovery/output/enriched_curated_firms.json")
    if not enriched_file.exists():
        print("❌ Enriched file not found")
        return
        
    with open(enriched_file, 'r') as f:
        data = json.load(f)
        
    final_rows = []
    
    for item in data:
        firm = item.get('name')
        snippets = item.get('contact_enrichment_raw', '')
        
        # Heuristic: Find things that look like names "Firstname Lastname"
        # Since we don't have an LLM call here, we'll provide the snippets 
        # in the CSV for the user to quickly copy-paste.
        
        final_rows.append({
            "Firm Name": firm,
            "Target Name": "[NAME]", # Placeholder for manual confirmation
            "Target Email": "[EMAIL]", # Placeholder for manual confirmation
            "Discovery Details": snippets[:500],
            "Source URLs": ", ".join(item.get('urls', []))[:500]
        })
        
    df = pd.DataFrame(final_rows)
    out_file = Path("/Users/user/.gemini/[PROJECT_NAME]/skills/investor-outreach/output/MASTER_OUTREACH_LIST.csv")
    out_file.parent.mkdir(exist_ok=True)
    df.to_csv(out_file, index=False)
    print(f"✅ Generated final outreach list: {out_file}")

if __name__ == "__main__":
    generate_csv()
