#!/usr/bin/env python3
"""
Example usage of Google Analytics MCP
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../scripts/python'))

# Import would be: from analytics import GoogleAnalyticsMCP

print("📊 Google Analytics MCP Usage Examples")
print("=" * 50)

print("\n1. Basic Traffic Analysis:")
print("""
from analytics import GoogleAnalyticsMCP

ga = GoogleAnalyticsMCP()

# Get traffic data
traffic = ga.get_ga4_report(
    metrics=['activeUsers', 'sessions', 'screenPageViews'],
    dimensions=['date', 'country'],
    date_range='7daysAgo:today'
)

print(f"Total users: {sum(float(r.get('metric_0', 0)) for r in traffic['data'])}")
""")

print("\n2. Conversion Tracking:")
print("""
# Get conversion data
conversions = ga.get_ua_report(
    metrics=['transactions', 'transactionRevenue'],
    dimensions=['source', 'medium'],
    date_range='30daysAgo:today'
)

# Export to CSV
ga.export_to_csv(conversions, 'conversions_report.csv')
""")

print("\n3. Generate Insights:")
print("""
# Generate business insights
insights = ga.generate_insights(traffic)

print("Key Recommendations:")
for rec in insights['recommendations']:
    print(f"- {rec}")
""")

print("\n4. Real-time Monitoring:")
print("""
# Get real-time data
realtime = ga.get_ga4_report(
    metrics=['activeUsers'],
    date_range='today:today'
)

active_users = realtime['data'][0]['metric_0'] if realtime['data'] else 0
print(f"Active users right now: {active_users}")
""")

print("\n📋 Setup Instructions:")
print("1. Enable Google Analytics API in Google Cloud Console")
print("2. Create OAuth 2.0 credentials")
print("3. Add credentials to .env file")
print("4. Run authentication flow once")
print("5. Start querying your analytics data!")

print("\n✅ Examples ready for implementation")
