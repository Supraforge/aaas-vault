import argparse
import os
import json
import requests
import sys

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

def tavily_search(query, depth="basic", max_results=5):
    load_env()
    """
    Executes a search using the Tavily API.
    """
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        print("Error: TAVILY_API_KEY not found in environment variables.")
        print("Please add 'TAVILY_API_KEY=tvly-...' to your .env file.")
        sys.exit(1)

    url = "https://api.tavily.com/search"
    
    payload = {
        "api_key": api_key,
        "query": query,
        "search_depth": depth,
        "include_answer": True,
        "max_results": max_results
    }

    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Tavily API: {e}")
        sys.exit(1)

def format_output(data):
    """
    Formats the JSON response into a readable Markdown summary.
    """
    answer = data.get("answer", "")
    results = data.get("results", [])

    print(f"# Research Results\n")
    if answer:
        print(f"## AI Answer\n{answer}\n")
    
    print(f"## Sources\n")
    for result in results:
        title = result.get("title", "No Title")
        url = result.get("url", "#")
        content = result.get("content", "")[:200] + "..."
        
        print(f"- **[{title}]({url})**")
        print(f"  > {content}\n")

    # Print raw JSON for the agent to parse if needed (hidden from user output usually, but useful for logs)
    # print("\n--- RAW JSON ---\n")
    # print(json.dumps(data, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tavily AI Search Tool")
    parser.add_argument("--query", type=str, required=True, help="The search query")
    parser.add_argument("--depth", type=str, default="basic", choices=["basic", "advanced"], help="Search depth: basic or advanced")
    parser.add_argument("--max_results", type=int, default=5, help="Max number of results")

    args = parser.parse_args()

    # Load .env manually if needed (for localized testing), but ideally the environment should provide it.
    # In this agent system, .env is usually auto-loaded. If checks fail, we might need python-dotenv.
    # We'll assume the environment is primed.

    data = tavily_search(args.query, args.depth, args.max_results)
    format_output(data)
