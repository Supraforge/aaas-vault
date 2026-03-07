#!/usr/bin/env python3
"""
Tracking Implementation Verifier
Verifies analytics tracking implementation on a website
"""

import requests
from bs4 import BeautifulSoup
import re
import json

def check_google_analytics(html_content):
    """Check for Google Analytics implementation"""
    checks = {
        'gtag.js': 'gtag.js' in html_content,
        'GA4 Measurement ID': 'G-' in html_content,
        'dataLayer': 'dataLayer' in html_content,
        'gtag config': 'gtag(\'config\'' in html_content
    }
    return checks

def check_google_tag_manager(html_content):
    """Check for Google Tag Manager implementation"""
    checks = {
        'GTM script': 'googletagmanager.com/gtm.js' in html_content,
        'GTM iframe': 'googletagmanager.com/ns.html' in html_content,
        'dataLayer': 'dataLayer' in html_content
    }
    return checks

def check_analytics_providers(url):
    """Check website for analytics implementations"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html_content = response.text
        
        results = {
            'url': url,
            'status_code': response.status_code,
            'google_analytics': check_google_analytics(html_content),
            'google_tag_manager': check_google_tag_manager(html_content),
            'has_amplitude': 'amplitude' in html_content.lower(),
            'has_mixpanel': 'mixpanel' in html_content.lower(),
            'has_segment': 'segment' in html_content.lower()
        }
        
        return results
        
    except Exception as e:
        return {'error': str(e), 'url': url}

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Verify analytics tracking implementation')
    parser.add_argument('url', help='Website URL to check')
    parser.add_argument('--format', choices=['text', 'json'], default='text', help='Output format')
    
    args = parser.parse_args()
    
    results = check_analytics_providers(args.url)
    
    if args.format == 'json':
        print(json.dumps(results, indent=2))
    else:
        print(f"Analytics Verification for: {args.url}")
        print("=" * 50)
        
        if 'error' in results:
            print(f"Error: {results['error']}")
            return 1
        
        print(f"Status Code: {results['status_code']}")
        print()
        
        print("Google Analytics:")
        for check, found in results['google_analytics'].items():
            status = "✅ Found" if found else "❌ Missing"
            print(f"  {check}: {status}")
        
        print()
        print("Google Tag Manager:")
        for check, found in results['google_tag_manager'].items():
            status = "✅ Found" if found else "❌ Missing"
            print(f"  {check}: {status}")
        
        print()
        print("Other Analytics Providers:")
        print(f"  Amplitude: {'✅ Found' if results['has_amplitude'] else '❌ Not detected'}")
        print(f"  Mixpanel: {'✅ Found' if results['has_mixpanel'] else '❌ Not detected'}")
        print(f"  Segment: {'✅ Found' if results['has_segment'] else '❌ Not detected'}")
    
    return 0

if __name__ == '__main__':
    exit(main())
