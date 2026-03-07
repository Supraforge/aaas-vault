#!/usr/bin/env python3
"""
Internal Links Checker
Validates all internal links in static site point to existing pages
"""

import sys
import re
import json
import argparse
import urllib.parse
from pathlib import Path
from collections import defaultdict

from bs4 import BeautifulSoup

# Add shared modules to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "shared"))
from config_loader import load_json_config
from utils import save_json, timestamp


class InternalLinksChecker:
    """Check internal links for broken references"""

    def __init__(
        self,
        dist_path: Path,
        excluded_paths: list[str] = None,
        excluded_extensions: list[str] = None
    ):
        self.dist_path = dist_path
        self.excluded_paths = excluded_paths or []
        self.excluded_extensions = excluded_extensions or [
            '.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg',
            '.ico', '.pdf', '.xml', '.txt', '.woff', '.woff2'
        ]
        self.broken_links: list[dict] = []
        self.valid_links: int = 0

    def extract_internal_links(self, content: str) -> list[str]:
        """Extract all internal links from HTML content"""
        pattern = r'href=["\']([^"\']*)["\']'
        links = re.findall(pattern, content, re.IGNORECASE)

        internal_links = []
        for link in links:
            # Only internal links (starting with /)
            if link.startswith('/'):
                # Remove fragment
                if '#' in link:
                    link = link.split('#')[0]

                if not link or link == '/':
                    continue

                # Decode URL encoding
                try:
                    link = urllib.parse.unquote(link)
                except:
                    pass

                internal_links.append(link)

        return internal_links

    def is_excluded(self, link: str) -> bool:
        """Check if link should be excluded from analysis"""
        # Check excluded paths
        for pattern in self.excluded_paths:
            if link.startswith(pattern):
                return True

        # Check excluded extensions
        for ext in self.excluded_extensions:
            if link.lower().endswith(ext):
                return True

        return False

    def check_link_exists(self, link: str) -> tuple[bool, str | None]:
        """Check if a link target exists"""
        relative_path = link.lstrip('/')

        # Try different path variations
        possible_paths = [
            self.dist_path / relative_path,
            self.dist_path / relative_path / 'index.html',
            self.dist_path / (relative_path + '.html'),
            self.dist_path / relative_path.rstrip('/') / 'index.html',
        ]

        for path in possible_paths:
            if path.exists():
                return True, str(path)

        return False, None

    def analyze(self) -> dict:
        """Analyze all HTML files for broken internal links"""
        html_files = list(self.dist_path.glob('**/*.html'))
        print(f"Found {len(html_files)} HTML files to check...")

        total_links_checked = 0
        broken_by_source: dict[str, list[str]] = defaultdict(list)

        for i, file_path in enumerate(html_files, 1):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                relative_file = str(file_path.relative_to(self.dist_path))
                internal_links = self.extract_internal_links(content)

                for link in internal_links:
                    if self.is_excluded(link):
                        continue

                    total_links_checked += 1
                    exists, found_path = self.check_link_exists(link)

                    if not exists:
                        self.broken_links.append({
                            'source_file': relative_file,
                            'broken_link': link
                        })
                        broken_by_source[relative_file].append(link)
                    else:
                        self.valid_links += 1

            except Exception as e:
                print(f"Error processing {file_path}: {e}", file=sys.stderr)

            if i % 100 == 0:
                print(f"Checked {i}/{len(html_files)} files...")

        print(f"Analysis complete. Checked {total_links_checked} internal links.")

        return {
            "metadata": {
                "analyzed_at": timestamp(),
                "files_analyzed": len(html_files),
                "total_links_checked": total_links_checked,
                "valid_links": self.valid_links,
                "broken_links": len(self.broken_links)
            },
            "broken_links": self.broken_links,
            "broken_by_source": dict(broken_by_source)
        }


def main():
    parser = argparse.ArgumentParser(description="Internal Links Checker")
    parser.add_argument("--dist", "-d", required=True, help="Path to dist directory")
    parser.add_argument("--config", help="Path to config.json")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--exclude", nargs="+", help="Paths to exclude")

    args = parser.parse_args()

    # Load config
    config = {}
    if args.config:
        config = load_json_config(Path(args.config))

    # Get exclusions
    excluded_paths = args.exclude or config.get("excluded_paths", [])
    excluded_extensions = config.get("excluded_extensions", [])

    dist_path = Path(args.dist)
    if not dist_path.exists():
        print(f"Error: Directory not found: {dist_path}", file=sys.stderr)
        sys.exit(1)

    # Run analysis
    checker = InternalLinksChecker(
        dist_path,
        excluded_paths=excluded_paths,
        excluded_extensions=excluded_extensions
    )
    results = checker.analyze()

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
    print("INTERNAL LINKS CHECK SUMMARY")
    print(f"{'=' * 60}")
    print(f"Files analyzed: {meta['files_analyzed']}")
    print(f"Links checked: {meta['total_links_checked']}")
    print(f"Valid links: {meta['valid_links']}")
    print(f"Broken links: {meta['broken_links']}")

    if results["broken_links"]:
        print(f"\nBROKEN LINKS:")
        print("-" * 60)

        # Group by source and show first 20
        shown = 0
        for source, links in results["broken_by_source"].items():
            if shown >= 20:
                remaining = len(results["broken_by_source"]) - 20
                print(f"\n... and {remaining} more files with broken links")
                break

            print(f"\n{source}:")
            for link in links[:5]:
                print(f"  - {link}")
            if len(links) > 5:
                print(f"  ... and {len(links) - 5} more")
            shown += 1
    else:
        print("\nNo broken internal links found!")


if __name__ == "__main__":
    main()
