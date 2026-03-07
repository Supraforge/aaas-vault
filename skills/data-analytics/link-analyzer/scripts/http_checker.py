#!/usr/bin/env python3
"""
HTTP Link Checker
Validates external links via HTTP requests with parallel processing
"""

import sys
import json
import time
import argparse
from pathlib import Path
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict

import requests

# Add shared modules to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "shared"))
from config_loader import load_json_config
from utils import save_json, load_json, timestamp


class HTTPLinkChecker:
    """Check external links via HTTP requests"""

    def __init__(
        self,
        timeout: int = 5,
        max_workers: int = 20,
        retry_count: int = 1,
        user_agent: str = "Mozilla/5.0 (compatible; LinkChecker/1.0)"
    ):
        self.timeout = timeout
        self.max_workers = max_workers
        self.retry_count = retry_count
        self.user_agent = user_agent
        self.results: list[dict] = []

    def check_url(self, url: str) -> tuple[int | None, str, bool]:
        """Check if URL is accessible"""
        headers = {'User-Agent': self.user_agent}

        for attempt in range(self.retry_count):
            try:
                # Try HEAD first (faster)
                response = requests.head(
                    url,
                    timeout=self.timeout,
                    headers=headers,
                    allow_redirects=True
                )

                # Some sites block HEAD, fallback to GET
                if response.status_code in [405, 403]:
                    response = requests.get(
                        url,
                        timeout=self.timeout,
                        headers=headers,
                        allow_redirects=True,
                        stream=True
                    )
                    # Only read first 1KB
                    next(response.iter_content(1024), None)
                    response.close()

                is_broken = response.status_code >= 400
                return response.status_code, response.reason, is_broken

            except requests.exceptions.Timeout:
                if attempt == self.retry_count - 1:
                    return None, "Timeout", True
                time.sleep(1)

            except requests.exceptions.ConnectionError:
                return None, "Connection Error (Domain may not exist)", True

            except requests.exceptions.TooManyRedirects:
                return None, "Too Many Redirects", True

            except requests.exceptions.SSLError:
                return None, "SSL Certificate Error", True

            except Exception as e:
                return None, f"Error: {str(e)}", True

        return None, "Unknown Error", True

    def check_urls(self, urls_with_info: dict[str, dict]) -> list[dict]:
        """Check multiple URLs in parallel"""
        total = len(urls_with_info)
        completed = 0

        def check_single(url: str, info: dict) -> dict:
            status_code, status_msg, is_broken = self.check_url(url)
            return {
                'url': url,
                'status_code': status_code,
                'status_message': status_msg,
                'is_broken': is_broken,
                'occurrences': info.get('count', 1),
                'sample_pages': info.get('pages', [])[:5]
            }

        print(f"Checking {total} URLs in parallel (max {self.max_workers} workers)...")

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_url = {
                executor.submit(check_single, url, info): url
                for url, info in urls_with_info.items()
            }

            for future in as_completed(future_to_url):
                completed += 1
                result = future.result()
                self.results.append(result)

                status = "OK" if not result['is_broken'] else "BROKEN"
                url_display = result['url'][:60] + "..." if len(result['url']) > 60 else result['url']
                print(f"[{completed}/{total}] [{status}] {url_display}")

        return self.results


def filter_false_positives(
    results: list[dict],
    bot_blocker_domains: list[str] = None,
    ignore_status_codes: list[int] = None
) -> tuple[list[dict], list[dict]]:
    """Filter out known false positives"""
    bot_blockers = bot_blocker_domains or [
        'linkedin.com', 'stackoverflow.com', 'twitter.com', 'x.com',
        'facebook.com', 'instagram.com', 'pixabay.com', 'unsplash.com'
    ]
    ignore_codes = ignore_status_codes or [403, 503, 520, 999]

    real_broken = []
    false_positives = []

    for result in results:
        if not result['is_broken']:
            continue

        url = result['url'].lower()
        status_code = result['status_code']

        # Check if it's a known bot blocker
        is_false_positive = False
        for domain in bot_blockers:
            if domain in url:
                is_false_positive = True
                break

        # Check if status code should be ignored
        if status_code in ignore_codes:
            is_false_positive = True

        # Skip mailto/tel links
        if url.startswith('mailto:') or url.startswith('tel:'):
            is_false_positive = True

        if is_false_positive:
            false_positives.append(result)
        else:
            real_broken.append(result)

    return real_broken, false_positives


def main():
    parser = argparse.ArgumentParser(description="HTTP Link Checker")
    parser.add_argument("--input", "-i", required=True, help="Path to outbound links JSON")
    parser.add_argument("--config", help="Path to config.json")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--timeout", type=int, default=5, help="Request timeout")
    parser.add_argument("--workers", type=int, default=20, help="Max parallel workers")
    parser.add_argument("--filter", action="store_true", help="Filter false positives")

    args = parser.parse_args()

    # Load config
    config = {}
    if args.config:
        config = load_json_config(Path(args.config))

    http_config = config.get("http", {})
    timeout = args.timeout or http_config.get("timeout", 5)
    max_workers = args.workers or http_config.get("max_workers", 20)
    retry_count = http_config.get("retry_count", 1)
    user_agent = http_config.get("user_agent", "Mozilla/5.0 (compatible; LinkChecker/1.0)")

    # Load outbound links data
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    outbound_data = load_json(input_path)
    outbound_links = outbound_data.get("outbound_links", {})

    # Prepare URLs with metadata
    urls_with_info = {}
    for url, pages in outbound_links.items():
        urls_with_info[url] = {
            'count': len(pages),
            'pages': pages
        }

    # Run checker
    checker = HTTPLinkChecker(
        timeout=timeout,
        max_workers=max_workers,
        retry_count=retry_count,
        user_agent=user_agent
    )
    results = checker.check_urls(urls_with_info)

    # Separate broken and working
    broken = [r for r in results if r['is_broken']]
    working = [r for r in results if not r['is_broken']]

    # Filter false positives if requested
    if args.filter:
        fp_config = config.get("false_positives", {})
        real_broken, false_positives = filter_false_positives(
            broken,
            bot_blocker_domains=fp_config.get("bot_blocker_domains"),
            ignore_status_codes=fp_config.get("ignore_status_codes")
        )
    else:
        real_broken = broken
        false_positives = []

    # Build output
    output_data = {
        "metadata": {
            "checked_at": timestamp(),
            "total_checked": len(results),
            "working": len(working),
            "broken": len(broken),
            "real_broken": len(real_broken),
            "false_positives": len(false_positives)
        },
        "broken_links": sorted(real_broken, key=lambda x: x['occurrences'], reverse=True),
        "false_positives": false_positives,
        "working_links": working
    }

    # Output
    if args.output:
        output_path = Path(args.output)
        save_json(output_data, output_path)
        print(f"\nResults saved to: {output_path}")
    else:
        # Just print summary, not full JSON
        pass

    # Print summary
    meta = output_data["metadata"]
    print(f"\n{'=' * 60}")
    print("HTTP CHECK SUMMARY")
    print(f"{'=' * 60}")
    print(f"Total checked: {meta['total_checked']}")
    print(f"Working: {meta['working']}")
    print(f"Broken: {meta['broken']}")
    if args.filter:
        print(f"Real broken: {meta['real_broken']}")
        print(f"False positives filtered: {meta['false_positives']}")

    if real_broken:
        print(f"\nTOP BROKEN LINKS:")
        print("-" * 60)
        for link in real_broken[:10]:
            print(f"  [{link['status_code']}] {link['url'][:50]}... ({link['occurrences']} occurrences)")


if __name__ == "__main__":
    main()
