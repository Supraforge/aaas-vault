#!/usr/bin/env python3
"""
Report Generator - Creates analytics reports from CRM data
"""

import json
from datetime import datetime, timedelta
from typing import Dict, Any, List


class ReportGenerator:
    """Generates various CRM reports"""

    def generate_sync_report(self, sync_results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate report for contact sync operation"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'operation': 'contact_sync',
            'summary': {
                'total_processed': sync_results.get('total', 0),
                'successful': sync_results.get('successful', 0),
                'failed': sync_results.get('failed', 0),
                'skipped': sync_results.get('skipped', 0)
            },
            'errors': sync_results.get('errors', []),
            'warnings': sync_results.get('warnings', []),
            'duration_seconds': sync_results.get('duration', 0)
        }

        # Calculate success rate
        total = report['summary']['total_processed']
        if total > 0:
            report['summary']['success_rate'] = round(
                report['summary']['successful'] / total * 100, 2
            )
        else:
            report['summary']['success_rate'] = 0

        return report

    def generate_report(self, data: Dict[str, Any], report_type: str) -> Dict[str, Any]:
        """Generate various types of reports"""
        if report_type == 'daily_sales':
            return self._generate_daily_sales_report(data)
        elif report_type == 'weekly_pipeline':
            return self._generate_weekly_pipeline_report(data)
        elif report_type == 'monthly_performance':
            return self._generate_monthly_performance_report(data)
        else:
            return self._generate_generic_report(data, report_type)

    def _generate_daily_sales_report(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate daily sales report"""
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)

        report = {
            'report_type': 'daily_sales',
            'date': today.isoformat(),
            'period': {
                'start': yesterday.isoformat(),
                'end': today.isoformat()
            },
            'metrics': {
                'new_leads': data.get('new_leads', 0),
                'converted_leads': data.get('converted_leads', 0),
                'new_deals': data.get('new_deals', 0),
                'closed_deals': data.get('closed_deals', 0),
                'deal_value': data.get('deal_value', 0),
                'activities_completed': data.get('activities', 0)
            },
            'top_performers': data.get('top_performers', []),
            'notable_events': data.get('notable_events', [])
        }

        # Calculate conversion rate
        new_leads = report['metrics']['new_leads']
        converted = report['metrics']['converted_leads']
        if new_leads > 0:
            report['metrics']['conversion_rate'] = round(converted / new_leads * 100, 2)
        else:
            report['metrics']['conversion_rate'] = 0

        return report

    def _generate_weekly_pipeline_report(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate weekly pipeline report"""
        today = datetime.now()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)

        report = {
            'report_type': 'weekly_pipeline',
            'week_number': today.isocalendar()[1],
            'period': {
                'start': week_start.date().isoformat(),
                'end': week_end.date().isoformat()
            },
            'pipeline_summary': {
                'total_deals': data.get('total_deals', 0),
                'total_value': data.get('total_value', 0),
                'deals_by_stage': data.get('deals_by_stage', {}),
                'average_deal_size': data.get('average_deal_size', 0),
                'pipeline_velocity': data.get('pipeline_velocity', 0)
            },
            'stage_analysis': data.get('stage_analysis', {}),
            'forecast': data.get('forecast', {}),
            'bottlenecks': data.get('bottlenecks', []),
            'recommendations': data.get('recommendations', [])
        }

        return report

    def _generate_monthly_performance_report(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate monthly performance report"""
        today = datetime.now()
        month_start = today.replace(day=1)
        if today.month == 12:
            month_end = today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1)
        else:
            month_end = today.replace(month=today.month + 1, day=1) - timedelta(days=1)

        report = {
            'report_type': 'monthly_performance',
            'month': today.strftime('%B %Y'),
            'period': {
                'start': month_start.date().isoformat(),
                'end': month_end.date().isoformat()
            },
            'team_performance': {
                'individual_metrics': data.get('individual_metrics', []),
                'team_averages': data.get('team_averages', {}),
                'goal_achievement': data.get('goal_achievement', {})
            },
            'financial_metrics': {
                'revenue': data.get('revenue', 0),
                'cac': data.get('cac', 0),
                'lifetime_value': data.get('lifetime_value', 0),
                'roi': data.get('roi', 0)
            },
            'trend_analysis': data.get('trend_analysis', {}),
            'key_achievements': data.get('key_achievements', []),
            'areas_for_improvement': data.get('improvement_areas', []),
            'next_month_goals': data.get('next_month_goals', [])
        }

        return report

    def _generate_generic_report(self, data: Dict[str, Any], report_type: str) -> Dict[str, Any]:
        """Generate generic report"""
        return {
            'report_type': report_type,
            'timestamp': datetime.now().isoformat(),
            'data': data,
            'summary': 'Custom report generated'
        }


if __name__ == "__main__":
    # Test the report generator
    generator = ReportGenerator()

    test_sync_results = {
        'total': 100,
        'successful': 95,
        'failed': 3,
        'skipped': 2,
        'errors': ['Invalid email: test@', 'Duplicate contact: john@example.com'],
        'duration': 45.2
    }

    sync_report = generator.generate_sync_report(test_sync_results)
    print(f"Sync report: {json.dumps(sync_report, indent=2)}")

    test_sales_data = {
        'new_leads': 25,
        'converted_leads': 5,
        'new_deals': 3,
        'closed_deals': 2,
        'deal_value': 15000,
        'activities': 47,
        'top_performers': ['John Doe', 'Jane Smith'],
        'notable_events': ['Large enterprise deal closed', 'New partnership signed']
    }

    daily_report = generator._generate_daily_sales_report(test_sales_data)
    print(f"
Daily sales report: {json.dumps(daily_report, indent=2)}")
