#!/usr/bin/env python3
"""
Email Finder Script

Finds email addresses using various services and techniques.
"""

import os
import re
import requests
import argparse
from typing import List, Optional

class EmailFinder:
    """Find email addresses for domains and people"""

    def __init__(self):
        self.hunter_api_key = os.getenv("HUNTER_API_KEY")
        self.clearbit_api_key = os.getenv("CLEARBIT_API_KEY")

    def find_by_domain(self, domain: str) -> List[str]:
        """Find email addresses for a domain"""
        emails = []

        # Common email patterns
        common_patterns = [
            f"contact@{domain}",
            f"info@{domain}",
            f"hello@{domain}",
            f"support@{domain}",
            f"sales@{domain}",
            f"admin@{domain}",
        ]

        # Try Hunter.io if API key is available
        if self.hunter_api_key:
            hunter_emails = self._query_hunter(domain)
            if hunter_emails:
                emails.extend(hunter_emails)

        # Add common patterns
        emails.extend(common_patterns)

        # Remove duplicates
        return list(set(emails))

    def find_by_person(self, first_name: str, last_name: str, domain: str) -> List[str]:
        """Find email for a specific person"""
        emails = []

        # Common email formats
        formats = [
            f"{first_name}.{last_name}@{domain}",
            f"{first_name}{last_name}@{domain}",
            f"{first_name[0]}{last_name}@{domain}",
            f"{first_name}@{domain}",
            f"{last_name}.{first_name}@{domain}",
            f"{first_name[0]}.{last_name}@{domain}",
        ]

        emails.extend(formats)

        # Try Clearbit if API key is available
        if self.clearbit_api_key:
            clearbit_email = self._query_clearbit(first_name, last_name, domain)
            if clearbit_email:
                emails.append(clearbit_email)

        return list(set(emails))

    def _query_hunter(self, domain: str) -> List[str]:
        """Query Hunter.io API"""
        try:
            url = f"https://api.hunter.io/v2/domain-search"
            params = {
                "domain": domain,
                "api_key": self.hunter_api_key,
                "limit": 10
            }

            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if "data" in data and "emails" in data["data"]:
                    return [email["value"] for email in data["data"]["emails"]]
        except Exception as e:
            print(f"Hunter.io query failed: {e}")

        return []

    def _query_clearbit(self, first_name: str, last_name: str, domain: str) -> Optional[str]:
        """Query Clearbit API"""
        try:
            url = f"https://person.clearbit.com/v2/people/find"
            params = {
                "email": f"{first_name}.{last_name}@{domain}",
            }
            headers = {
                "Authorization": f"Bearer {self.clearbit_api_key}"
            }

            response = requests.get(url, params=params, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if "email" in data:
                    return data["email"]
        except Exception as e:
            print(f"Clearbit query failed: {e}")

        return None

    def validate_email(self, email: str) -> bool:
        """Basic email validation"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

def main():
    parser = argparse.ArgumentParser(description="Email Finder")
    parser.add_argument("--domain", required=True, help="Domain to search")
    parser.add_argument("--name", help="Full name (format: First Last)")
    parser.add_argument("--validate", action="store_true", help="Validate found emails")

    args = parser.parse_args()

    finder = EmailFinder()

    if args.name:
        name_parts = args.name.split()
        if len(name_parts) >= 2:
            first_name, last_name = name_parts[0], name_parts[-1]
            emails = finder.find_by_person(first_name, last_name, args.domain)
            print(f"Found emails for {args.name} @ {args.domain}:")
        else:
            print("Please provide full name (First Last)")
            return
    else:
        emails = finder.find_by_domain(args.domain)
        print(f"Found emails for domain {args.domain}:")

    for email in emails:
        if args.validate:
            is_valid = finder.validate_email(email)
            status = "✅" if is_valid else "❌"
            print(f"  {status} {email}")
        else:
            print(f"  {email}")

if __name__ == "__main__":
    main()
