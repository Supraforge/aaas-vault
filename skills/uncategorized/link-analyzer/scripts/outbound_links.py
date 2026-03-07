#!/usr/bin/env python3
"""
Outbound Links Analyzer
Extracts and categorizes all external links from static site
"""

import sys
import json
import argparse
from pathlib import Path
from urllib.parse import urlparse
from collections import defaultdict, Counter
from glob import glob

from bs4 import BeautifulSoup

# Add shared modules to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "shared"))
from config_loader import load_json_config
from utils import save_json, timestamp


class OutboundLinksAnalyzer:
    """Analyze outbound links in static site"""

    def __init__(self, dist_path: Path, internal_domains: list[str]):
        self.dist_path = dist_path
        self.internal_domains = [d.lower() for d in internal_domains]
        self.outbound_links: dict[str, list[str]] = defaultdict(list)
        self.link_counts: Counter = Counter()
        self.domains: dict[str, list[str]] = defaultdict(list)
        self.link_types: dict[str, str] = {}

    def is_outbound_link(self, href: str) -> bool:
        """Determine if a link is outbound"""
        if not href or href.strip() == '':
            return False

        href = href.strip().lower()

        # Skip anchors, javascript, and relative links
        if href.startswith('#') or href.startswith('javascript:') or href.startswith('/'):
            return False

        # Skip internal domains
        for domain in self.internal_domains:
            if domain in href:
                return False

        return True

    def classify_link_type(self, url: str) -> str:
        """Classify the type of outbound link"""
        url_lower = url.lower()

        try:
            domain = urlparse(url).netloc.lower()
        except:
            domain = ""

        if url.startswith('mailto:'):
            return 'Email'
        elif url.startswith('tel:'):
            return 'Phone'
        elif 'twitter.com' in domain or 'x.com' in domain:
            return 'Social Media - Twitter/X'
        elif 'facebook.com' in domain:
            return 'Social Media - Facebook'
        elif 'linkedin.com' in domain:
            return 'Social Media - LinkedIn'
        elif 'instagram.com' in domain:
            return 'Social Media - Instagram'
        elif 'youtube.com' in domain or 'youtu.be' in domain:
            return 'Social Media - YouTube'
        elif 'amazon.com' in domain or 'amazon.' in domain or 'a.co' in domain:
            return 'Amazon'
        elif 'apps.apple.com' in domain or 'apple.com' in domain:
            return 'App Store'
        elif 'play.google.com' in domain:
            return 'Google Play Store'
        elif 'github.com' in domain:
            return 'GitHub'
        elif 'medium.com' in domain:
            return 'Medium'
        elif 'gumroad.com' in domain:
            return 'Gumroad'
        elif 'substack.com' in domain:
            return 'Substack'
        elif 'wikipedia.org' in domain:
            return 'Wikipedia'
        else:
            return 'External Website'

    def extract_links_from_file(self, file_path: Path) -> list[str]:
        """Extract all outbound links from HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            soup = BeautifulSoup(content, 'html.parser')
            links = []

            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                if self.is_outbound_link(href):
                    links.append(href)

            return links

        except Exception as e:
            print(f"Error processing {file_path}: {e}", file=sys.stderr)
            return []

    def get_relative_path(self, file_path: Path) -> str:
        """Get relative path from dist folder"""
        return str(file_path.relative_to(self.dist_path))

    def analyze(self) -> dict:
        """Analyze all HTML files"""
        html_files = list(self.dist_path.glob('**/*.html'))
        print(f"Found {len(html_files)} HTML files to analyze...")

        for i, file_path in enumerate(html_files, 1):
            links = self.extract_links_from_file(file_path)
            relative_path = self.get_relative_path(file_path)

            for link in links:
                self.outbound_links[link].append(relative_path)
                self.link_counts[link] += 1

                if link not in self.link_types:
                    self.link_types[link] = self.classify_link_type(link)

                try:
                    domain = urlparse(link).netloc
                    if domain:
                        if link not in self.domains[domain]:
                            self.domains[domain].append(link)
                except:
                    if ':' in link:
                        protocol = link.split(':')[0]
                        if link not in self.domains[f"{protocol}:"]:
                            self.domains[f"{protocol}:"].append(link)

            if i % 100 == 0:
                print(f"Processed {i}/{len(html_files)} files...")

        print(f"Analysis complete. Found {len(self.link_counts)} unique outbound links.")

        return {
            "metadata": {
                "analyzed_at": timestamp(),
                "files_analyzed": len(html_files),
                "unique_links": len(self.link_counts),
                "unique_domains": len(self.domains),
                "total_link_occurrences": sum(self.link_counts.values())
            },
            "outbound_links": dict(self.outbound_links),
            "link_counts": dict(self.link_counts),
            "domains": {k: list(set(v)) for k, v in self.domains.items()},
            "link_types": self.link_types
        }


def main():
    parser = argparse.ArgumentParser(description="Outbound Links Analyzer")
    parser.add_argument("--dist", "-d", required=True, help="Path to dist directory")
    parser.add_argument("--config", help="Path to config.json")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--domains", nargs="+", help="Internal domains to exclude")

    args = parser.parse_args()

    # Load config
    config = {}
    if args.config:
        config = load_json_config(Path(args.config))

    # Get internal domains
    if args.domains:
        internal_domains = args.domains
    else:
        internal_domains = config.get("internal_domains", [])
        if not internal_domains:
            site_domain = config.get("site_domain", "")
            if site_domain:
                internal_domains = [site_domain, f"www.{site_domain}"]

    dist_path = Path(args.dist)
    if not dist_path.exists():
        print(f"Error: Directory not found: {dist_path}", file=sys.stderr)
        sys.exit(1)

    # Run analysis
    analyzer = OutboundLinksAnalyzer(dist_path, internal_domains)
    results = analyzer.analyze()

    # Output
    if args.output:
        output_path = Path(args.output)
        save_json(results, output_path)
        print(f"\nResults saved to: {output_path}")
    else:
        print(json.dumps(results, indent=2))

    # Print summary
    meta = results["metadata"]
    print(f"\n{'=' * 60}")
    print("OUTBOUND LINKS SUMMARY")
    print(f"{'=' * 60}")
    print(f"Files analyzed: {meta['files_analyzed']}")
    print(f"Unique links: {meta['unique_links']}")
    print(f"Unique domains: {meta['unique_domains']}")
    print(f"Total occurrences: {meta['total_link_occurrences']}")

    # Type breakdown
    type_counts = Counter(results["link_types"].values())
    print(f"\nBy type:")
    for link_type, count in type_counts.most_common(10):
        print(f"  {link_type}: {count}")


if __name__ == "__main__":
    main()
