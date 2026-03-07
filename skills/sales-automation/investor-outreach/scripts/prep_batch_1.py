#!/usr/bin/env python3
import json
import pandas as pd
from pathlib import Path

def extract_best_contacts():
    # Load the enriched JSON which has more structured snippets than the flattened CSV
    enriched_file = Path("/Users/user/.gemini/[PROJECT_NAME]/skills/investor-discovery/output/enriched_curated_firms.json")
    if not enriched_file.exists():
        print("❌ Enriched JSON not found. Run discovery/enrichment first.")
        return
        
    with open(enriched_file, 'r') as f:
        data = json.load(f)
        
    final_contacts = []
    
    # Selection of high-quality automotive/AI/compliance firms from the list
    # Manual extraction from the snippets I saw in the file view
    
    # 1. Toyota Ventures
    final_contacts.append({
        "Firm": "Toyota Ventures",
        "name": "Jim Adler",
        "email": "jim@toyotaventures.com",
        "blurb": "I’ve been following your work at Toyota Ventures—specifically your focus on the intersection of autonomy and AI. Given your investment in Apex.AI, I thought our work on automotive compliance automation would be highly relevant.",
        "Reason": "Managing Director, strong focus on AI and autonomy (Apex.AI investor)"
    })
    
    # 2. InMotion Ventures (JLR)
    final_contacts.append({
        "Firm": "InMotion Ventures",
        "name": "Sebastian Peck",
        "email": "sebastian@inmotionventures.com",
        "blurb": "As a partner at InMotion Ventures, your insight into the JLR ecosystem is unique. We are solving a specific compliance bottleneck that we've seen slowing down development cycles in automotive software.",
        "Reason": "Managing Director at JLR's fund, industrial tech & AI focus"
    })

    # 3. First Momentum Ventures
    final_contacts.append({
        "Firm": "First Momentum Ventures",
        "name": "Sebastian Böhmer",
        "email": "sebastian@firstmomentum.vc",
        "blurb": "I’ve seen First Momentum’s lead on several deep tech seed rounds in Germany. Since we're currently validating with the VW Group, I wanted to reach out regarding our pre-seed close.",
        "Reason": "DACH-based, deep tech focus, perfect for DACH pre-seed target"
    })
    
    # 4. Octopus Ventures
    final_contacts.append({
        "Firm": "Octopus Ventures",
        "name": "Jo Oliver",
        "email": "jo.oliver@octopusventures.com",
        "blurb": "I noted Octopus Ventures' recent activity in European RegTech (specifically Cogna). We are taking a similar 'intelligence layer' approach but specifically for safety-critical automotive audits.",
        "Reason": "Partner, focus on B2B SaaS and RegTech"
    })

    # 5. EquityPitcher Ventures
    final_contacts.append({
        "Firm": "EquityPitcher Ventures",
        "name": "Hermann Koch",
        "email": "hermann@equitypitcher.com",
        "blurb": "With EquityPitcher’s strong presence in the DACH region and focus on tech-enabled startups, I thought you'd be interested in our progress with Audi and the VW Group.",
        "Reason": "Zurich-based, DACH technology focus"
    })
    
    # 6. Wingman Ventures
    final_contacts.append({
        "Firm": "Wingman Ventures",
        "name": "Pascal Mathis",
        "email": "pascal@wingman.ch",
        "blurb": "Wingman has a great reputation for supporting Swiss-based founders in deep tech. We're based in the region and building the compliance infrastructure for the next generation of SDVs.",
        "Reason": "Zurich-based, focused on Swiss/DACH deep tech"
    })

    # 7. Pathlight Ventures
    final_contacts.append({
        "Firm": "Pathlight Ventures",
        "name": "Mahdi Raza",
        "email": "mahdi@pathlight.vc",
        "blurb": "I noted your experience scaling Fintech and Software startups. We’re applying that same rigorous automation to the 'compliance tax' that automotive engineers face daily.",
        "Reason": "Managing Partner, Software & Fintech focus"
    })


    # Create the CSV
    df = pd.DataFrame(final_contacts)
    out_file = Path("/Users/user/.gemini/[PROJECT_NAME]/skills/investor-outreach/output/BATCH_1_PREP.csv")
    df.to_csv(out_file, index=False)
    
    print(f"✅ Generated Batch 1 Prep with {len(final_contacts)} high-conviction leads.")
    print(f"📍 File: {out_file}")

if __name__ == "__main__":
    generate_csv = True # placeholder
    extract_best_contacts()
