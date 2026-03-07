#!/usr/bin/env python3
"""
Investor Discovery to Outreach Bridge
This script takes a list of investors (from discovery scripts or a CSV) 
and automates the mailing process.
"""

import os
import json
import pandas as pd
import argparse
from pathlib import Path
from investor_mailer import send_investor_email

def process_outreach_batch(csv_path, template_id, attachment=None, dry_run=True, cc=None):
    """
    Reads a CSV of investors and sends emails.
    CSV expects columns: 'name', 'email', 'blurb' (optional)
    """
    if not os.path.exists(csv_path):
        print(f"❌ Error: CSV file not found at {csv_path}")
        return

    df = pd.read_csv(csv_path)
    print(f"📂 Loaded {len(df)} contacts from {csv_path}")

    success_count = 0
    for index, row in df.iterrows():
        name = str(row.get('name', '')).strip()
        email = str(row.get('email', '')).strip()
        blurb = str(row.get('blurb', '')).strip() if 'blurb' in row else ""
        
        if not name or not email or '@' not in email:
            print(f"⚠️ Skipping row {index}: Missing name or valid email ({name}, {email})")
            continue

        if dry_run:
            print(f"🔍 [DRY RUN] Would send '{template_id}' to {name} <{email}>")
            if cc:
                print(f"   📎 CC: {cc}")
            if blurb:
                print(f"   ✍️ Custom Blurb: {blurb[:60]}...")
            success_count += 1
        else:
            success = send_investor_email(
                to_email=email,
                template_id=template_id,
                name_placeholder=name,
                attachment_path=attachment,
                blurb=blurb,
                cc=cc
            )
            if success:
                success_count += 1

    mode = "DRY RUN" if dry_run else "LIVE"
    print(f"\n✅ {mode} Complete. {success_count}/{len(df)} emails processed.")


def main():
    parser = argparse.ArgumentParser(description="Bridge Discovery to Outreach")
    parser.add_argument("--csv", required=True, help="Path to investor CSV (must have 'name' and 'email' columns)")
    parser.add_argument("--template", required=True, choices=["traction-first", "tech-forward", "problem-solution"], help="Template ID")
    parser.add_argument("--attach", help="Path to deck/attachment")
    parser.add_argument("--cc", help="Email address to CC")
    parser.add_argument("--live", action="store_true", help="Run live (actually send emails). Default is dry run.")

    args = parser.parse_args()

    process_outreach_batch(
        csv_path=args.csv,
        template_id=args.template,
        attachment=args.attach,
        dry_run=not args.live,
        cc=args.cc
    )


if __name__ == "__main__":
    main()
