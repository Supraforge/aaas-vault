#!/usr/bin/env python3
"""
Lead Generation Automation Script

This script automates lead generation from various sources including:
- LinkedIn profiles
- Company websites
- Email lists
- Public directories
"""

import os
import sys
import json
import csv
import argparse
from datetime import datetime
from typing import List, Dict, Any
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Try to import optional dependencies
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    HAS_SELENIUM = True
except ImportError:
    HAS_SELENIUM = False
    print("Warning: Selenium not installed. Browser automation disabled.")

try:
    from email_validator import validate_email, EmailNotValidError
    HAS_EMAIL_VALIDATOR = True
except ImportError:
    HAS_EMAIL_VALIDATOR = False

class LeadGenerator:
    """Main class for lead generation automation"""

    def __init__(self, config_path: str = None):
        """Initialize lead generator with configuration"""
        self.config = self._load_config(config_path)
        self.leads = []

    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from file or environment"""
        config = {
            "user_agent": os.getenv("USER_AGENT", "Mozilla/5.0 (compatible; LeadGenerator/1.0)"),
            "request_delay": float(os.getenv("REQUEST_DELAY", "2")),
            "max_retries": int(os.getenv("MAX_RETRIES", "3")),
            "output_format": os.getenv("DEFAULT_OUTPUT_FORMAT", "csv"),
            "enable_enrichment": os.getenv("ENABLE_DATA_ENRICHMENT", "true").lower() == "true",
            "validate_emails": os.getenv("VALIDATE_EMAILS", "true").lower() == "true",
        }

        # Load API keys
        api_keys = [
            "HUNTER_API_KEY", "CLEARBIT_API_KEY",
            "LINKEDIN_CLIENT_ID", "LINKEDIN_CLIENT_SECRET",
            "SALESFORCE_CLIENT_ID", "HUBSPOT_API_KEY"
        ]

        for key in api_keys:
            config[key.lower()] = os.getenv(key)

        return config

    def generate_from_keywords(self, keywords: List[str], limit: int = 100) -> List[Dict]:
        """Generate leads based on keywords"""
        print(f"Generating leads for keywords: {keywords}")

        # This is a simplified example - in reality, you would:
        # 1. Search LinkedIn/Sales Navigator
        # 2. Search company directories
        # 3. Use email finding APIs
        # 4. Enrich with additional data

        # Mock data for demonstration
        mock_leads = [
            {
                "name": "John Doe",
                "title": "Marketing Director",
                "company": "Tech Corp Inc.",
                "email": "john.doe@techcorp.com",
                "linkedin": "https://linkedin.com/in/johndoe",
                "phone": "+1-555-0123",
                "source": "keyword_search",
                "score": 85,
                "timestamp": datetime.now().isoformat()
            },
            {
                "name": "Jane Smith",
                "title": "Sales Manager",
                "company": "Business Solutions LLC",
                "email": "jane.smith@businesssolutions.com",
                "linkedin": "https://linkedin.com/in/janesmith",
                "phone": "+1-555-0456",
                "source": "keyword_search",
                "score": 78,
                "timestamp": datetime.now().isoformat()
            }
        ]

        self.leads.extend(mock_leads[:limit])
        return mock_leads[:limit]

    def find_emails(self, domain: str, full_name: str = None) -> List[str]:
        """Find email addresses for a domain"""
        if not self.config.get("hunter_api_key"):
            print("Hunter.io API key not configured")
            return []

        # This would call Hunter.io API
        # For now, return mock data
        return [f"contact@{domain}", f"info@{domain}"]

    def validate_lead(self, lead: Dict) -> Dict:
        """Validate and enrich lead data"""
        validated = lead.copy()

        # Email validation
        if "email" in lead and lead["email"] and self.config["validate_emails"]:
            if HAS_EMAIL_VALIDATOR:
                try:
                    validate_email(lead["email"])
                    validated["email_valid"] = True
                except EmailNotValidError:
                    validated["email_valid"] = False
            else:
                # Simple regex check
                if "@" in lead["email"] and "." in lead["email"]:
                    validated["email_valid"] = True
                else:
                    validated["email_valid"] = False

        # Calculate lead score
        score = 0
        if validated.get("email_valid", False):
            score += 30
        if "linkedin" in lead and lead["linkedin"]:
            score += 25
        if "title" in lead and lead["title"]:
            # Higher score for decision-maker titles
            decision_titles = ["director", "manager", "vp", "cfo", "ceo", "cto", "founder"]
            if any(title in lead["title"].lower() for title in decision_titles):
                score += 35
            else:
                score += 15

        validated["score"] = min(100, score)

        return validated

    def export_leads(self, format: str = None, filename: str = None) -> str:
        """Export leads to file"""
        if not self.leads:
            print("No leads to export")
            return ""

        export_format = format or self.config["output_format"]
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"leads_{timestamp}.{export_format}"

        # Validate all leads before export
        validated_leads = [self.validate_lead(lead) for lead in self.leads]

        if export_format == "csv":
            with open(filename, "w", newline="", encoding="utf-8") as f:
                if validated_leads:
                    writer = csv.DictWriter(f, fieldnames=validated_leads[0].keys())
                    writer.writeheader()
                    writer.writerows(validated_leads)
        elif export_format == "json":
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(validated_leads, f, indent=2)
        else:
            print(f"Unsupported format: {export_format}")
            return ""

        print(f"Exported {len(validated_leads)} leads to {filename}")
        return filename

    def generate_report(self) -> Dict:
        """Generate summary report of leads"""
        if not self.leads:
            return {"total_leads": 0, "message": "No leads generated"}

        validated_leads = [self.validate_lead(lead) for lead in self.leads]

        report = {
            "total_leads": len(validated_leads),
            "valid_emails": sum(1 for lead in validated_leads if lead.get("email_valid", False)),
            "average_score": sum(lead.get("score", 0) for lead in validated_leads) / len(validated_leads),
            "top_titles": {},
            "top_companies": {},
            "generated_at": datetime.now().isoformat()
        }

        # Count titles and companies
        for lead in validated_leads:
            title = lead.get("title", "Unknown")
            company = lead.get("company", "Unknown")

            report["top_titles"][title] = report["top_titles"].get(title, 0) + 1
            report["top_companies"][company] = report["top_companies"].get(company, 0) + 1

        # Sort and get top 5
        report["top_titles"] = dict(sorted(report["top_titles"].items(), 
                                         key=lambda x: x[1], reverse=True)[:5])
        report["top_companies"] = dict(sorted(report["top_companies"].items(), 
                                            key=lambda x: x[1], reverse=True)[:5])

        return report

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Lead Generation Automation")
    parser.add_argument("--keywords", nargs="+", help="Keywords for lead generation")
    parser.add_argument("--domain", help="Domain for email finding")
    parser.add_argument("--limit", type=int, default=100, help="Maximum leads to generate")
    parser.add_argument("--format", choices=["csv", "json"], default="csv", 
                       help="Output format")
    parser.add_argument("--output", help="Output filename")
    parser.add_argument("--report", action="store_true", help="Generate summary report")

    args = parser.parse_args()

    generator = LeadGenerator()

    if args.keywords:
        leads = generator.generate_from_keywords(args.keywords, args.limit)
        print(f"Generated {len(leads)} leads")

    if args.domain:
        emails = generator.find_emails(args.domain)
        print(f"Found emails for {args.domain}: {emails}")

    if args.report or generator.leads:
        report = generator.generate_report()
        print("
=== Lead Generation Report ===")
        print(f"Total Leads: {report['total_leads']}")
        print(f"Valid Emails: {report['valid_emails']}")
        print(f"Average Score: {report['average_score']:.1f}")

        if generator.leads:
            output_file = generator.export_leads(args.format, args.output)
            if output_file:
                print(f"Leads exported to: {output_file}")

    if not any([args.keywords, args.domain, args.report]):
        parser.print_help()

if __name__ == "__main__":
    main()
