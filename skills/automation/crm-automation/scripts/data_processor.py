#!/usr/bin/env python3
"""
Data Processor - Handles data validation and formatting for CRM operations
"""

import json
import csv
import re
from typing import Dict, Any, List
from datetime import datetime


class DataProcessor:
    """Processes and validates data for CRM operations"""

    def load_contacts(self, file_path: str) -> List[Dict[str, Any]]:
        """Load contacts from file (CSV or JSON)"""
        if file_path.endswith('.csv'):
            return self._load_csv(file_path)
        elif file_path.endswith('.json'):
            return self._load_json(file_path)
        else:
            raise ValueError("Unsupported file format. Use CSV or JSON")

    def _load_csv(self, file_path: str) -> List[Dict[str, Any]]:
        """Load contacts from CSV file"""
        contacts = []
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                contacts.append(row)
        return contacts

    def _load_json(self, file_path: str) -> List[Dict[str, Any]]:
        """Load contacts from JSON file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and 'contacts' in data:
            return data['contacts']
        else:
            raise ValueError("Invalid JSON structure")

    def validate_contacts(self, contacts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Validate contact data"""
        validated = []

        for contact in contacts:
            validated_contact = self._validate_contact(contact)
            if validated_contact:
                validated.append(validated_contact)

        return validated

    def _validate_contact(self, contact: Dict[str, Any]) -> Dict[str, Any]:
        """Validate individual contact"""
        # Check for required email
        email = contact.get('email', '').strip()
        if not email or not self._is_valid_email(email):
            print(f"Warning: Invalid email for contact: {contact.get('first_name', 'Unknown')}")
            return None

        # Clean and format data
        validated = {
            'email': email.lower(),
            'first_name': contact.get('first_name', '').strip().title(),
            'last_name': contact.get('last_name', '').strip().title(),
            'company': contact.get('company', '').strip(),
            'phone': self._format_phone(contact.get('phone', '')),
            'tags': self._parse_tags(contact.get('tags', '')),
            'custom_fields': contact.get('custom_fields', {})
        }

        # Remove empty values
        validated = {k: v for k, v in validated.items() if v}

        return validated

    def validate_lead(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate lead data"""
        validated = {
            'email': lead_data.get('email', '').strip().lower(),
            'first_name': lead_data.get('first_name', '').strip().title(),
            'last_name': lead_data.get('last_name', '').strip().title(),
            'company': lead_data.get('company', '').strip(),
            'job_title': lead_data.get('job_title', '').strip(),
            'source': lead_data.get('source', 'website'),
            'status': lead_data.get('status', 'new'),
            'notes': lead_data.get('notes', ''),
            'custom_fields': lead_data.get('custom_fields', {})
        }

        # Validate required fields
        if not validated['email'] or not self._is_valid_email(validated['email']):
            raise ValueError("Valid email is required for lead")

        return validated

    def calculate_lead_score(self, lead: Dict[str, Any]) -> int:
        """Calculate lead score based on various factors"""
        score = 0

        # Email domain quality
        email = lead.get('email', '')
        if email and self._is_company_email(email):
            score += 10

        # Job title
        job_title = lead.get('job_title', '').lower()
        title_keywords = ['director', 'manager', 'vp', 'chief', 'head', 'lead']
        if any(keyword in job_title for keyword in title_keywords):
            score += 20

        # Company information
        company = lead.get('company', '')
        if company and len(company) > 2:  # Not empty
            score += 5

        # Source quality
        source = lead.get('source', '').lower()
        high_quality_sources = ['referral', 'event', 'partnership', 'outbound']
        if source in high_quality_sources:
            score += 15

        # Cap score at 100
        return min(score, 100)

    def _is_valid_email(self, email: str) -> bool:
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def _is_company_email(self, email: str) -> bool:
        """Check if email is from a company domain (not gmail, yahoo, etc.)"""
        personal_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com']
        domain = email.split('@')[-1].lower()
        return domain not in personal_domains

    def _format_phone(self, phone: str) -> str:
        """Format phone number"""
        if not phone:
            return ''

        # Remove non-numeric characters
        digits = re.sub(r'\D', '', phone)

        if len(digits) == 10:
            return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        elif len(digits) == 11 and digits[0] == '1':
            return f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
        else:
            return phone  # Return as-is if can't format

    def _parse_tags(self, tags_input) -> List[str]:
        """Parse tags from string or list"""
        if isinstance(tags_input, list):
            return [str(tag).strip().lower() for tag in tags_input]
        elif isinstance(tags_input, str):
            return [tag.strip().lower() for tag in tags_input.split(',')]
        else:
            return []


if __name__ == "__main__":
    # Test the data processor
    processor = DataProcessor()

    test_contact = {
        'email': 'test@example.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'company': 'Test Corp',
        'phone': '555-123-4567',
        'tags': 'lead,test'
    }

    validated = processor._validate_contact(test_contact)
    print(f"Validated contact: {validated}")

    test_lead = {
        'email': 'jane@company.com',
        'first_name': 'Jane',
        'last_name': 'Smith',
        'job_title': 'Director of Marketing',
        'company': 'Big Company Inc',
        'source': 'referral'
    }

    validated_lead = processor.validate_lead(test_lead)
    score = processor.calculate_lead_score(validated_lead)
    print(f"Lead score: {score}")
