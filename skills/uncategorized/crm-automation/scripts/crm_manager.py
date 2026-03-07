#!/usr/bin/env python3
"""
CRM Manager - Main orchestration script for CRM automation
"""

import os
import sys
import json
import argparse
from datetime import datetime
from typing import Dict, Any, List, Optional

# Add scripts directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

try:
    from hubspot_integration import HubSpotIntegration
    from salesforce_integration import SalesforceIntegration
    from data_processor import DataProcessor
    from report_generator import ReportGenerator
    from auth_tester import AuthTester
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure all required dependencies are installed")
    sys.exit(1)


class CRMManager:
    """Main CRM manager class"""

    def __init__(self):
        self.crm_platforms = {
            'hubspot': HubSpotIntegration,
            'salesforce': SalesforceIntegration,
            'zoho': None,  # Placeholder for Zoho integration
            'freshworks': None,  # Placeholder for Freshworks integration
            'pipedrive': None,  # Placeholder for Pipedrive integration
        }
        self.data_processor = DataProcessor()
        self.report_generator = ReportGenerator()

    def select_platform(self, platform_name: str):
        """Select and initialize CRM platform"""
        platform_name = platform_name.lower()

        if platform_name not in self.crm_platforms:
            raise ValueError(f"Unsupported CRM platform: {platform_name}")

        platform_class = self.crm_platforms.get(platform_name)
        if platform_class is None:
            print(f"Note: {platform_name} integration not yet implemented")
            return None

        return platform_class()

    def sync_contacts(self, platform, data_file: str) -> Dict[str, Any]:
        """Sync contacts with CRM"""
        print(f"Syncing contacts from {data_file}...")

        # Load and process data
        contacts = self.data_processor.load_contacts(data_file)
        validated_contacts = self.data_processor.validate_contacts(contacts)

        # Sync with CRM
        results = platform.sync_contacts(validated_contacts)

        # Generate report
        report = self.report_generator.generate_sync_report(results)

        return {
            'status': 'success',
            'synced_count': len(validated_contacts),
            'results': results,
            'report': report
        }

    def create_lead(self, platform, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new lead in CRM"""
        print("Creating new lead...")

        # Validate lead data
        validated_lead = self.data_processor.validate_lead(lead_data)

        # Calculate lead score
        lead_score = self.data_processor.calculate_lead_score(validated_lead)
        validated_lead['score'] = lead_score

        # Create lead in CRM
        result = platform.create_lead(validated_lead)

        # Trigger follow-up if score is high
        if lead_score > 75:
            self._trigger_high_score_followup(validated_lead)

        return {
            'status': 'success',
            'lead_id': result.get('id'),
            'lead_score': lead_score,
            'result': result
        }

    def update_pipeline(self, platform, pipeline_data: Dict[str, Any]) -> Dict[str, Any]:
        """Update sales pipeline"""
        print("Updating sales pipeline...")

        result = platform.update_pipeline(pipeline_data)

        return {
            'status': 'success',
            'updated_deals': result.get('updated_count', 0),
            'result': result
        }

    def send_followup(self, platform, followup_data: Dict[str, Any]) -> Dict[str, Any]:
        """Send automated follow-up"""
        print("Sending follow-up...")

        result = platform.send_followup(followup_data)

        return {
            'status': 'success',
            'sent_count': result.get('sent_count', 0),
            'result': result
        }

    def generate_report(self, platform, report_type: str) -> Dict[str, Any]:
        """Generate CRM analytics report"""
        print(f"Generating {report_type} report...")

        data = platform.get_report_data(report_type)
        report = self.report_generator.generate_report(data, report_type)

        return {
            'status': 'success',
            'report_type': report_type,
            'report': report
        }

    def _trigger_high_score_followup(self, lead: Dict[str, Any]):
        """Trigger follow-up for high-score leads"""
        print(f"High-score lead detected ({lead['score']}/100). Triggering immediate follow-up...")
        # This would integrate with email automation
        pass

    def run_test(self):
        """Run self-test"""
        print("Running CRM manager self-test...")

        # Test platform selection
        try:
            platform = self.select_platform('hubspot')
            print("✅ Platform selection test passed")
        except Exception as e:
            print(f"❌ Platform selection test failed: {e}")

        # Test data processor
        test_data = {'email': 'test@example.com', 'first_name': 'Test'}
        try:
            validated = self.data_processor.validate_contacts([test_data])
            print("✅ Data processor test passed")
        except Exception as e:
            print(f"❌ Data processor test failed: {e}")

        print("Self-test complete!")


def main():
    parser = argparse.ArgumentParser(description='CRM Automation Manager')
    parser.add_argument('--platform', required=True, help='CRM platform (hubspot, salesforce, etc.)')
    parser.add_argument('--operation', required=True, help='Operation to perform')
    parser.add_argument('--data-file', help='Path to data file')
    parser.add_argument('--data-json', help='JSON data as string')
    parser.add_argument('--report-type', help='Type of report to generate')
    parser.add_argument('--test', action='store_true', help='Run self-test')

    args = parser.parse_args()

    manager = CRMManager()

    if args.test:
        manager.run_test()
        return

    # Select platform
    try:
        platform = manager.select_platform(args.platform)
        if platform is None:
            print(f"Platform {args.platform} not available")
            return
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Execute operation
    try:
        if args.operation == 'sync_contacts':
            if not args.data_file:
                print("Error: --data-file required for sync_contacts")
                return
            result = manager.sync_contacts(platform, args.data_file)

        elif args.operation == 'create_lead':
            if not args.data_json:
                print("Error: --data-json required for create_lead")
                return
            lead_data = json.loads(args.data_json)
            result = manager.create_lead(platform, lead_data)

        elif args.operation == 'update_pipeline':
            if not args.data_json:
                print("Error: --data-json required for update_pipeline")
                return
            pipeline_data = json.loads(args.data_json)
            result = manager.update_pipeline(platform, pipeline_data)

        elif args.operation == 'send_followup':
            if not args.data_json:
                print("Error: --data-json required for send_followup")
                return
            followup_data = json.loads(args.data_json)
            result = manager.send_followup(platform, followup_data)

        elif args.operation == 'generate_report':
            if not args.report_type:
                print("Error: --report-type required for generate_report")
                return
            result = manager.generate_report(platform, args.report_type)

        else:
            print(f"Unknown operation: {args.operation}")
            return

        # Output result
        print(json.dumps(result, indent=2))

    except Exception as e:
        print(f"Error during operation: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
