import pandas as pd
import json
import argparse
import os
import sys
from datetime import datetime
from scoring import calculate_relevance_score

def main():
    parser = argparse.ArgumentParser(description="Search for investors in OpenVC database.")
    parser.add_argument("--project", required=True, help="Project name/description")
    parser.add_argument("--industry", required=True, help="Industry keywords, comma-separated")
    parser.add_argument("--stage", required=True, help="Target funding stage (e.g., Seed, Series A)")
    parser.add_argument("--geography", help="Target geographies, comma-separated")
    parser.add_argument("--check-size", help="Target check size range (e.g., 500K-2M)")
    parser.add_argument("--max-results", type=int, default=50, help="Max results to return")
    
    args = parser.parse_args()

    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file = os.path.join(base_dir, "resources", "openvc_investors.csv")
    synonyms_file = os.path.join(base_dir, "resources", "synonyms.json")
    geo_file = os.path.join(base_dir, "resources", "geography_mapping.json")
    output_dir = os.path.join(base_dir, "output")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Check if CSV exists
    if not os.path.exists(csv_file):
        print(f"Error: Database file not found at {csv_file}")
        print("Please run scripts/download_openvc.py first.")
        sys.exit(1)

    # Load data
    df = pd.read_csv(csv_file)
    
    with open(synonyms_file, 'r') as f:
        synonyms = json.load(f)
    
    with open(geo_file, 'r') as f:
        geo_mapping = json.load(f)

    # Prepare criteria
    criteria = {
        "industry": [i.strip() for i in args.industry.split(',')],
        "stage": args.stage,
        "geography": [g.strip() for g in args.geography.split(',')] if args.geography else [],
        "check_size": args.check_size
    }

    # Process and score
    scored_investors = []
    
    for _, row in df.iterrows():
        investor_data = row.to_dict()
        score, reasons = calculate_relevance_score(investor_data, criteria, synonyms, geo_mapping)
        
        if score > 0.1: # Threshold to filter non-relevant
            investor_data['relevance_score'] = score
            investor_data['match_reasons'] = reasons
            scored_investors.append(investor_data)

    # Sort and rank
    ranked_investors = sorted(scored_investors, key=lambda x: x['relevance_score'], reverse=True)[:args.max_results]

    # Generate metadata
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    metadata = {
        "search_metadata": {
            "timestamp": datetime.now().isoformat(),
            "project": args.project,
            "filters": criteria,
            "total_found": len(scored_investors),
            "returned": len(ranked_investors)
        },
        "investors": ranked_investors
    }

    # Save JSON
    json_output = os.path.join(output_dir, f"investors_{timestamp}.json")
    with open(json_output, 'w') as f:
        json.dump(metadata, f, indent=2)

    # Save CSV
    csv_output = os.path.join(output_dir, f"investors_{timestamp}.csv")
    pd.DataFrame(ranked_investors).to_csv(csv_output, index=False)

    # Save Markdown Report
    repo_output = os.path.join(output_dir, f"investors_{timestamp}_report.md")
    with open(repo_output, 'w') as f:
        f.write(f"# Investor Discovery Report: {args.project}\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("## Search Criteria\n")
        f.write(f"- **Industries:** {', '.join(criteria['industry'])}\n")
        f.write(f"- **Stage:** {criteria['stage']}\n")
        f.write(f"- **Geography:** {', '.join(criteria['geography']) if criteria['geography'] else 'N/A'}\n")
        f.write(f"- **Check Size:** {criteria['check_size'] if criteria['check_size'] else 'N/A'}\n\n")
        
        f.write("## Top Results\n\n")
        for i, inv in enumerate(ranked_investors, 1):
            f.write(f"### {i}. {inv.get('Name')} ({inv.get('relevance_score')*100}% Match)\n")
            f.write(f"- **Type:** {inv.get('Type')}\n")
            f.write(f"- **HQ:** {inv.get('Geography')}\n")
            f.write(f"- **Contact:** {inv.get('Contact Method')} / {inv.get('Link')}\n")
            f.write(f"- **Match Reasons:** {', '.join(inv.get('match_reasons'))}\n\n")

    print(f"Discovery complete! Found {len(scored_investors)} matches.")
    print(f"Results saved to {output_dir}")
    print(f"JSON: {json_output}")
    print(f"CSV: {csv_output}")
    print(f"Report: {repo_output}")

if __name__ == "__main__":
    main()
