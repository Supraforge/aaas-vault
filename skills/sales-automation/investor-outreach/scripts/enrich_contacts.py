#!/usr/bin/env python3
"""
Investor Contact Enrichment Script
Takes firm names from discovery output and uses Tavily to find specific Partner names and emails.
"""

import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv
import time

# Load env from root
# Robust .env loading
def load_env():
    env_paths = [
        Path.cwd() / ".env",
        Path(__file__).parent.parent.parent.parent / ".env",
        Path("/tmp/sh_env")
    ]
    for env_path in env_paths:
        try:
            with open(env_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if '=' in line and not line.startswith('#'):
                        key, value = line.split('=', 1)
                        os.environ[key] = value.strip("'").strip('"')
            return True
        except Exception:
            continue
    return False

load_env()


TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def search_partner_info(firm_name, industry):
    """
    Search for partner names and potential emails for a venture firm.
    """
    if not TAVILY_API_KEY:
        return None
        
    query = f"Partner names at {firm_name} venture capital investing in {industry} contact email"
    print(f"🔎 Searching for contacts at {firm_name}...")
    
    try:
        response = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY_API_KEY,
                "query": query,
                "search_depth": "advanced",
                "max_results": 3
            },
            timeout=15
        )
        if response.status_code == 200:
            return response.json().get('results', [])
        return []
    except Exception as e:
        print(f"❌ Search error for {firm_name}: {e}")
        return []

def enrich_json_file(file_path):
    """
    Reads a discovery JSON, enriches it, and saves back.
    """
    path = Path(file_path)
    if not path.exists():
        print(f"❌ File not found: {file_path}")
        return

    with open(path, 'r') as f:
        data = json.load(f)

    enriched_data = []
    print(f"🚀 Enriching {len(data)} firms in {path.name}...")

    for item in data:
        firm_name = item.get('name')
        if not firm_name:
            continue
            
        industry = item.get('focus', ['AI'])[0] if isinstance(item.get('focus'), list) else 'AI'
        
        # Don't hammer the API too fast
        results = search_partner_info(firm_name, industry)
        
        # Extract snippets for manual/automated review
        snippets = " | ".join([r.get('content', '')[:200] for r in results])
        
        item['contact_enrichment_raw'] = snippets
        # Future: Use LLM here to extract exact email/name from snippets
        item['potential_leads'] = [r.get('url') for r in results]
        
        enriched_data.append(item)
        time.sleep(1) # Simple rate limiting

    output_path = path.parent / f"enriched_{path.name}"
    with open(output_path, 'w') as f:
        json.dump(enriched_data, f, indent=2)
    
    print(f"✅ Enrichment complete. Saved to {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        enrich_json_file(sys.argv[1])
    else:
        print("Usage: python3 enrich_contacts.py <path_to_discovery_json>")
