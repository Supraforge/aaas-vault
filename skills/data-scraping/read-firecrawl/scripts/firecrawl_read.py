import argparse
import os
import json
import requests
import sys
import time

def load_env():
    """
    Manually loads .env file if it exists.
    """
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, _, value = line.partition('=')
                    if key and value:
                        os.environ[key.strip()] = value.strip()

def firecrawl_read(url, mode="scrape", max_depth=2):
    load_env()
    """
    Executes a scrape or crawl using the Firecrawl API.
    """
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        print("Error: FIRECRAWL_API_KEY not found in environment variables.")
        print("Please add 'FIRECRAWL_API_KEY=fc-...' to your .env file.")
        sys.exit(1)

    base_url = "https://api.firecrawl.dev/v1"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    if mode == "scrape":
        endpoint = f"{base_url}/scrape"
        payload = {
            "url": url,
            "formats": ["markdown"]
        }
        
        try:
            response = requests.post(endpoint, json=payload, headers=headers, timeout=60)
            response.raise_for_status()
            data = response.json()
            
            # Output Markdown
            markdown = data.get("data", {}).get("markdown", "")
            if not markdown:
                 print("No markdown content returned.")
                 return

            print(f"# Scrape Results: {url}\n")
            print(markdown)

        except requests.exceptions.RequestException as e:
            print(f"Error connecting to Firecrawl API: {e}")
            if response is not None:
                print(response.text)
            sys.exit(1)

    elif mode == "crawl":
        endpoint = f"{base_url}/crawl"
        payload = {
            "url": url,
            "crawlerOptions": {
                "limit": 10, # Safety limit
                "maxDepth": max_depth,
                "returnOnlyUrls": False
            }
        }

        try:
            # 1. Start Crawl
            print(f"Starting crawl for {url}...")
            response = requests.post(endpoint, json=payload, headers=headers, timeout=30)
            response.raise_for_status()
            job_id = response.json().get("id")
            
            if not job_id:
                print("Error: No job ID returned for crawl.")
                sys.exit(1)

            # 2. Poll Status
            print(f"Job ID: {job_id}. Polling for results...")
            while True:
                status_url = f"{base_url}/crawl/{job_id}"
                status_res = requests.get(status_url, headers=headers)
                status_res.raise_for_status()
                status_data = status_res.json()
                
                status = status_data.get("status")
                if status == "completed":
                    print("\n--- Crawl Completed ---\n")
                    data = status_data.get("data", [])
                    for i, page in enumerate(data):
                         print(f"## Page {i+1}: {page.get('metadata', {}).get('title', 'Unknown')}")
                         print(f"URL: {page.get('metadata', {}).get('url', 'Unknown')}")
                         print(f"\n{page.get('markdown', '')[:500]}...\n[Content Truncated for Overview]\n")
                    break
                elif status == "failed":
                    print("Crawl failed.")
                    sys.exit(1)
                
                time.sleep(2)

        except requests.exceptions.RequestException as e:
            print(f"Error connecting to Firecrawl API: {e}")
            sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Firecrawl Reader Tool")
    parser.add_argument("--url", type=str, required=True, help="The URL to read")
    parser.add_argument("--mode", type=str, default="scrape", choices=["scrape", "crawl"], help="Mode: scrape (single) or crawl (site)")
    parser.add_argument("--max_depth", type=int, default=2, help="Max depth for crawl")

    args = parser.parse_args()
    firecrawl_read(args.url, args.mode, args.max_depth)
