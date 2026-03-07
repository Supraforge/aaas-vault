#!/usr/bin/env python3
import pandas as pd
from pathlib import Path

def create_batch_2():
    final_contacts = []
    
    # 1. Porsche Ventures
    final_contacts.append({
        "Firm": "Porsche Ventures",
        "name": "Patrick Huke",
        "email": "patrick.huke@porsche.de",
        "blurb": "I've been following Porsche Ventures' focus on the future of mobility and digital transformation. As we build the AI-native compliance layer for SDVs, your perspective on the OEM-software stack would be invaluable.",
        "Reason": "Head of Porsche Ventures, focus on mobility & digital transformation"
    })
    
    # 2. HELLA Ventures
    final_contacts.append({
        "Firm": "HELLA Ventures",
        "name": "Joerg Weisgerber",
        "email": "joerg.weisgerber@hella.com",
        "blurb": "Given HELLA's leadership in automotive electronics and your investment in Apex.AI, I thought our work on 'Quality Gateways' for safety-critical software would be highly relevant to your portfolio.",
        "Reason": "Partner at HELLA Ventures, deep expertise in automotive electronics"
    })

    # 3. Eclipse Ventures
    final_contacts.append({
        "Firm": "Eclipse Ventures",
        "name": "Aidan Madigan-Curtis",
        "email": "aidan@eclipse.vc",
        "blurb": "Eclipse has an incredible track record in industrial transformation. We're applying a similar thesis to the 'Intelligence Layer' of automotive engineering to solve the compliance tax.",
        "Reason": "Partner at Eclipse, focused on industrial tech and robotics"
    })
    
    # 4. Viola Ventures
    final_contacts.append({
        "Firm": "Viola Ventures",
        "name": "Zvika Orron",
        "email": "zvika@viola.vc",
        "blurb": "I noted Viola's strength in deep tech and AI. We're tackling the specific bottleneck of automotive audit trails with an AI-first approach that I think resonates with your thesis.",
        "Reason": "General Partner, focus on deep tech and industrials"
    })

    # 5. Smart Infrastructure Ventures
    final_contacts.append({
        "Firm": "Smart Infrastructure Ventures",
        "name": "Björn Bauermeister",
        "email": "bjoern@smart-infrastructure.vc",
        "blurb": "As a Leipzig-based fund with a strong DACH industrial focus, your expertise in scaling regional tech champions is exactly what we're looking for as we validate with VW Group.",
        "Reason": "Founding Partner, DACH industrial tech focus"
    })
    
    # 6. Airbus Ventures
    final_contacts.append({
        "Firm": "Airbus Ventures",
        "name": "Thomas d'Halluin",
        "email": "thomas@airbusventures.vc",
        "blurb": "Safety-critical software is in Airbus's DNA. We are bringing that same level of rigor to automotive SDV compliance using autonomous AI proxies to automate the audit trail.",
        "Reason": "Managing Partner, focus on safety-critical systems and aerospace/auto crossover"
    })

    # 7. Haufe Group Ventures
    final_contacts.append({
        "Firm": "Haufe Group Ventures",
        "name": "Jasper Roll",
        "email": "jasper.roll@haufe-group.com",
        "blurb": "Haufe Group's focus on enterprise software and workflow automation aligns perfectly with our mission to automate the manual 'compliance tax' in automotive R&D.",
        "Reason": "Managing Director, focus on B2B SaaS and workflow automation"
    })

    # 8. Silent Ventures
    final_contacts.append({
        "Firm": "Silent Ventures",
        "name": "Jordan Noone",
        "email": "jordan@silent.vc",
        "blurb": "I saw Silent Ventures' interest in frontier industrial tech. We're building the infrastructure that allows safety-critical engineering to move at the speed of software development.",
        "Reason": "Co-founder, focus on high-stakes frontier technology"
    })

    # 9. BMW i Ventures
    final_contacts.append({
        "Firm": "BMW i Ventures",
        "name": "Kasper Sage",
        "email": "kasper@bmwivenc.com",
        "blurb": "With your deep involvement in the software-defined vehicle movement, I wanted to share how we are automating the compliance bottleneck that currently slows down OEM innovation cycles.",
        "Reason": "Managing Partner at BMW's fund, SDV and industrial tech focus"
    })

    # 10. Index Ventures (London/Europe)
    final_contacts.append({
        "Firm": "Index Ventures",
        "name": "Georgia Stevenson",
        "email": "georgia@indexventures.com",
        "blurb": "Index has backed some of the most iconic software platforms in Europe. We're building the foundational compliance layer for the future of regulated mobility software.",
        "Reason": "Partner in London/Europe, focus on B2B SaaS"
    })

    # Create the CSV
    df = pd.DataFrame(final_contacts)
    out_file = Path("/Users/user/.gemini/[PROJECT_NAME]/skills/investor-outreach/output/BATCH_2_PREP.csv")
    df.to_csv(out_file, index=False)
    print(f"✅ Generated Batch 2 Prep with {len(df)} high-conviction leads.")
    print(f"📍 File: {out_file}")

if __name__ == "__main__":
    create_batch_2()
