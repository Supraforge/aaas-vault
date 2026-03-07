#!/usr/bin/env python3
"""
Link Graph Analyzer
Builds internal link graph and calculates link metrics:
- Orphan pages (zero inbound)
- Under-linked pages (below threshold)
- Over-linked pages (above threshold)
- Link sinks (receive but don't pass)
"""

import sys
import re
import json
import argparse
import urllib.parse
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, asdict

from bs4 import BeautifulSoup

# Add shared modules to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "shared"))
from config_loader import load_json_config
from utils import save_json, timestamp


@dataclass
class PageMetrics:
    """Metrics for a single page"""
    url: str
    inbound: int
    outbound: int
    ratio: float
    inbound_from: list[str]
    outbound_to: list[str]


class LinkGraphAnalyzer:
    """Build and analyze internal link graph"""

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
            '.ico', '.pdf', '.xml', '.txt', '.woff', '.woff2', '.json'
        ]

        # Link graph: source -> list of targets
        self.link_graph: dict[str, list[str]] = defaultdict(list)
        # All pages found
        self.all_pages: set[str] = set()
        # Metrics per page
        self.metrics: dict[str, PageMetrics] = {}

    def normalize_url(self, url: str) -> str:
        """Normalize URL to consistent format"""
        # Remove fragment
        if '#' in url:
            url = url.split('#')[0]

        # Remove query string
        if '?' in url:
            url = url.split('?')[0]

        # Decode URL encoding
        try:
            url = urllib.parse.unquote(url)
        except:
            pass

        # Ensure leading slash
        if not url.startswith('/'):
            url = '/' + url

        # Ensure trailing slash for directories
        if not url.endswith('/') and '.' not in url.split('/')[-1]:
            url = url + '/'

        return url

    def file_path_to_url(self, file_path: Path) -> str:
        """Convert file path to URL"""
        relative = file_path.relative_to(self.dist_path)

        # Convert to URL format
        url = '/' + str(relative).replace('\\', '/')

        # Remove index.html
        if url.endswith('/index.html'):
            url = url[:-10]
        elif url.endswith('.html'):
            url = url[:-5] + '/'

        return self.normalize_url(url)

    def is_excluded(self, url: str) -> bool:
        """Check if URL should be excluded"""
        for pattern in self.excluded_paths:
            if url.startswith(pattern):
                return True

        for ext in self.excluded_extensions:
            if url.lower().endswith(ext):
                return True

        return False

    def extract_internal_links(self, content: str) -> list[str]:
        """Extract internal links from HTML"""
        soup = BeautifulSoup(content, 'html.parser')
        links = []

        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']

            # Only internal links
            if href.startswith('/'):
                normalized = self.normalize_url(href)
                if not self.is_excluded(normalized):
                    links.append(normalized)

        return links

    def build_graph(self) -> None:
        """Build the complete link graph"""
        html_files = list(self.dist_path.glob('**/*.html'))
        print(f"Building link graph from {len(html_files)} HTML files...")

        for i, file_path in enumerate(html_files, 1):
            source_url = self.file_path_to_url(file_path)

            if self.is_excluded(source_url):
                continue

            self.all_pages.add(source_url)

            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                links = self.extract_internal_links(content)

                # Store unique links only
                unique_links = list(set(links))
                self.link_graph[source_url] = unique_links

                # Also track target pages
                for link in unique_links:
                    self.all_pages.add(link)

            except Exception as e:
                print(f"Error processing {file_path}: {e}", file=sys.stderr)

            if i % 100 == 0:
                print(f"Processed {i}/{len(html_files)} files...")

        print(f"Graph built. {len(self.all_pages)} pages, {sum(len(v) for v in self.link_graph.values())} links.")

    def calculate_metrics(self) -> None:
        """Calculate metrics for each page"""
        # Build reverse graph (inbound links)
        inbound_from: dict[str, list[str]] = defaultdict(list)

        for source, targets in self.link_graph.items():
            for target in targets:
                inbound_from[target].append(source)

        # Calculate metrics for each page
        for page in self.all_pages:
            inbound_list = inbound_from.get(page, [])
            outbound_list = self.link_graph.get(page, [])

            inbound_count = len(inbound_list)
            outbound_count = len(outbound_list)

            # Calculate ratio
            if outbound_count == 0:
                ratio = float('inf') if inbound_count > 0 else 0.0
            else:
                ratio = inbound_count / outbound_count

            self.metrics[page] = PageMetrics(
                url=page,
                inbound=inbound_count,
                outbound=outbound_count,
                ratio=round(ratio, 2) if ratio != float('inf') else -1,  # -1 represents infinity
                inbound_from=sorted(inbound_list)[:10],  # Limit for output size
                outbound_to=sorted(outbound_list)[:10]
            )

    def find_orphans(self) -> list[str]:
        """Find pages with zero inbound links"""
        orphans = []
        for page, metrics in self.metrics.items():
            if metrics.inbound == 0:
                # Exclude homepage
                if page != '/':
                    orphans.append(page)
        return sorted(orphans)

    def find_underlinked(self, threshold: int = 3) -> list[dict]:
        """Find pages with fewer than threshold inbound links"""
        underlinked = []
        for page, metrics in self.metrics.items():
            if 0 < metrics.inbound < threshold:
                underlinked.append({
                    'url': page,
                    'inbound': metrics.inbound,
                    'inbound_from': metrics.inbound_from
                })
        return sorted(underlinked, key=lambda x: x['inbound'])

    def find_overlinked(self, threshold: int = 50) -> list[dict]:
        """Find pages with more than threshold outbound links"""
        overlinked = []
        for page, metrics in self.metrics.items():
            if metrics.outbound > threshold:
                overlinked.append({
                    'url': page,
                    'outbound': metrics.outbound
                })
        return sorted(overlinked, key=lambda x: x['outbound'], reverse=True)

    def find_link_sinks(self, min_inbound: int = 5, max_outbound: int = 2) -> list[dict]:
        """Find pages that receive links but don't pass them"""
        sinks = []
        for page, metrics in self.metrics.items():
            if metrics.inbound >= min_inbound and metrics.outbound <= max_outbound:
                sinks.append({
                    'url': page,
                    'inbound': metrics.inbound,
                    'outbound': metrics.outbound
                })
        return sorted(sinks, key=lambda x: x['inbound'], reverse=True)

    def get_top_pages_by_inbound(self, limit: int = 20) -> list[dict]:
        """Get pages with most inbound links"""
        sorted_pages = sorted(
            self.metrics.values(),
            key=lambda x: x.inbound,
            reverse=True
        )
        return [
            {'url': p.url, 'inbound': p.inbound, 'outbound': p.outbound}
            for p in sorted_pages[:limit]
        ]

    def analyze(
        self,
        underlinked_threshold: int = 3,
        overlinked_threshold: int = 50,
        sink_min_inbound: int = 5,
        sink_max_outbound: int = 2
    ) -> dict:
        """Run full analysis"""
        self.build_graph()
        self.calculate_metrics()

        orphans = self.find_orphans()
        underlinked = self.find_underlinked(underlinked_threshold)
        overlinked = self.find_overlinked(overlinked_threshold)
        link_sinks = self.find_link_sinks(sink_min_inbound, sink_max_outbound)
        top_pages = self.get_top_pages_by_inbound()

        return {
            "metadata": {
                "analyzed_at": timestamp(),
                "total_pages": len(self.all_pages),
                "total_links": sum(len(v) for v in self.link_graph.values()),
                "thresholds": {
                    "underlinked": underlinked_threshold,
                    "overlinked": overlinked_threshold,
                    "sink_min_inbound": sink_min_inbound,
                    "sink_max_outbound": sink_max_outbound
                }
            },
            "summary": {
                "orphan_pages": len(orphans),
                "underlinked_pages": len(underlinked),
                "overlinked_pages": len(overlinked),
                "link_sinks": len(link_sinks)
            },
            "orphan_pages": orphans,
            "underlinked_pages": underlinked,
            "overlinked_pages": overlinked,
            "link_sinks": link_sinks,
            "top_pages_by_inbound": top_pages,
            "link_graph": {k: v for k, v in self.link_graph.items()},
            "page_metrics": {k: asdict(v) for k, v in self.metrics.items()}
        }


def generate_markdown_report(analysis: dict) -> str:
    """Generate markdown report from analysis"""
    lines = [
        "# Link Graph Analysis Report",
        "",
        f"**Generated:** {analysis['metadata']['analyzed_at']}",
        f"**Total Pages:** {analysis['metadata']['total_pages']}",
        f"**Total Internal Links:** {analysis['metadata']['total_links']}",
        "",
        "## Summary",
        "",
        f"| Issue | Count |",
        f"|-------|-------|",
        f"| Orphan Pages | {analysis['summary']['orphan_pages']} |",
        f"| Under-linked Pages | {analysis['summary']['underlinked_pages']} |",
        f"| Over-linked Pages | {analysis['summary']['overlinked_pages']} |",
        f"| Link Sinks | {analysis['summary']['link_sinks']} |",
        "",
    ]

    # Orphans
    if analysis['orphan_pages']:
        lines.extend([
            "## Orphan Pages (Critical)",
            "",
            "These pages have **zero inbound internal links**. Search engines may not discover them.",
            "",
        ])
        for page in analysis['orphan_pages'][:20]:
            lines.append(f"- `{page}`")
        if len(analysis['orphan_pages']) > 20:
            lines.append(f"\n*... and {len(analysis['orphan_pages']) - 20} more*")
        lines.append("")

    # Under-linked
    if analysis['underlinked_pages']:
        threshold = analysis['metadata']['thresholds']['underlinked']
        lines.extend([
            f"## Under-linked Pages (<{threshold} inbound)",
            "",
            "These pages have few inbound links and may lack authority.",
            "",
            "| Page | Inbound Links |",
            "|------|---------------|",
        ])
        for page in analysis['underlinked_pages'][:20]:
            lines.append(f"| `{page['url']}` | {page['inbound']} |")
        if len(analysis['underlinked_pages']) > 20:
            lines.append(f"\n*... and {len(analysis['underlinked_pages']) - 20} more*")
        lines.append("")

    # Over-linked
    if analysis['overlinked_pages']:
        threshold = analysis['metadata']['thresholds']['overlinked']
        lines.extend([
            f"## Over-linked Pages (>{threshold} outbound)",
            "",
            "These pages have many outbound links, diluting link equity.",
            "",
            "| Page | Outbound Links |",
            "|------|----------------|",
        ])
        for page in analysis['overlinked_pages']:
            lines.append(f"| `{page['url']}` | {page['outbound']} |")
        lines.append("")

    # Link Sinks
    if analysis['link_sinks']:
        lines.extend([
            "## Link Sinks",
            "",
            "These pages receive links but don't pass them to other pages.",
            "",
            "| Page | Inbound | Outbound |",
            "|------|---------|----------|",
        ])
        for page in analysis['link_sinks'][:20]:
            lines.append(f"| `{page['url']}` | {page['inbound']} | {page['outbound']} |")
        if len(analysis['link_sinks']) > 20:
            lines.append(f"\n*... and {len(analysis['link_sinks']) - 20} more*")
        lines.append("")

    # Top pages
    lines.extend([
        "## Top Pages by Inbound Links",
        "",
        "| Page | Inbound | Outbound |",
        "|------|---------|----------|",
    ])
    for page in analysis['top_pages_by_inbound']:
        lines.append(f"| `{page['url']}` | {page['inbound']} | {page['outbound']} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Link Graph Analyzer")
    parser.add_argument("--dist", "-d", required=True, help="Path to dist directory")
    parser.add_argument("--config", help="Path to config.json")
    parser.add_argument("--output", "-o", help="Output JSON file path")
    parser.add_argument("--report", "-r", help="Output markdown report path")
    parser.add_argument("--underlinked", type=int, default=3, help="Under-linked threshold")
    parser.add_argument("--overlinked", type=int, default=50, help="Over-linked threshold")
    parser.add_argument("--exclude", nargs="+", help="Paths to exclude")

    args = parser.parse_args()

    # Load config
    config = {}
    if args.config:
        config = load_json_config(Path(args.config))

    thresholds = config.get("thresholds", {})
    underlinked_threshold = args.underlinked or thresholds.get("underlinked_min_inbound", 3)
    overlinked_threshold = args.overlinked or thresholds.get("overlinked_max_outbound", 50)
    sink_min_inbound = thresholds.get("link_sink_min_inbound", 5)
    sink_max_outbound = thresholds.get("link_sink_max_outbound", 2)

    excluded_paths = args.exclude or config.get("excluded_paths", [])

    dist_path = Path(args.dist)
    if not dist_path.exists():
        print(f"Error: Directory not found: {dist_path}", file=sys.stderr)
        sys.exit(1)

    # Run analysis
    analyzer = LinkGraphAnalyzer(dist_path, excluded_paths=excluded_paths)
    analysis = analyzer.analyze(
        underlinked_threshold=underlinked_threshold,
        overlinked_threshold=overlinked_threshold,
        sink_min_inbound=sink_min_inbound,
        sink_max_outbound=sink_max_outbound
    )

    # Output JSON
    if args.output:
        output_path = Path(args.output)
        save_json(analysis, output_path)
        print(f"\nJSON results saved to: {output_path}")

    # Output markdown report
    if args.report:
        report = generate_markdown_report(analysis)
        report_path = Path(args.report)
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Markdown report saved to: {report_path}")

    # Print summary
    summary = analysis["summary"]
    print(f"\n{'=' * 60}")
    print("LINK GRAPH ANALYSIS SUMMARY")
    print(f"{'=' * 60}")
    print(f"Total pages: {analysis['metadata']['total_pages']}")
    print(f"Total links: {analysis['metadata']['total_links']}")
    print()
    print(f"Orphan pages (0 inbound): {summary['orphan_pages']}")
    print(f"Under-linked (<{underlinked_threshold} inbound): {summary['underlinked_pages']}")
    print(f"Over-linked (>{overlinked_threshold} outbound): {summary['overlinked_pages']}")
    print(f"Link sinks: {summary['link_sinks']}")

    if analysis['orphan_pages']:
        print(f"\nORPHAN PAGES (first 10):")
        for page in analysis['orphan_pages'][:10]:
            print(f"  - {page}")


if __name__ == "__main__":
    main()
