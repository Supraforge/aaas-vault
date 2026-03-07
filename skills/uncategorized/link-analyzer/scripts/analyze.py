#!/usr/bin/env python3
"""
Link Analyzer - Main Orchestrator
Runs all link analysis components and generates comprehensive report
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# Add shared modules to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "shared"))
from config_loader import load_json_config
from utils import save_json, ensure_dir, timestamp

# Import analysis modules
from outbound_links import OutboundLinksAnalyzer
from internal_links import InternalLinksChecker
from link_graph import LinkGraphAnalyzer, generate_markdown_report as generate_graph_report


def run_full_analysis(
    dist_path: Path,
    config: dict,
    output_dir: Path,
    skip_http: bool = False
) -> dict:
    """Run all analysis components"""

    results = {
        "metadata": {
            "analyzed_at": timestamp(),
            "dist_path": str(dist_path)
        },
        "outbound": None,
        "internal": None,
        "link_graph": None,
        "http_check": None
    }

    # Get config values
    internal_domains = config.get("internal_domains", [])
    site_domain = config.get("site_domain", "")
    if site_domain and not internal_domains:
        internal_domains = [site_domain, f"www.{site_domain}"]

    excluded_paths = config.get("excluded_paths", [])
    thresholds = config.get("thresholds", {})

    ensure_dir(output_dir)

    # 1. Outbound Links Analysis
    print("\n" + "=" * 60)
    print("PHASE 1: Outbound Links Analysis")
    print("=" * 60)

    outbound_analyzer = OutboundLinksAnalyzer(dist_path, internal_domains)
    outbound_results = outbound_analyzer.analyze()
    results["outbound"] = outbound_results["metadata"]

    outbound_file = output_dir / "outbound_links.json"
    save_json(outbound_results, outbound_file)
    print(f"Saved to: {outbound_file}")

    # 2. Internal Links Check
    print("\n" + "=" * 60)
    print("PHASE 2: Internal Links Check")
    print("=" * 60)

    internal_checker = InternalLinksChecker(dist_path, excluded_paths=excluded_paths)
    internal_results = internal_checker.analyze()
    results["internal"] = internal_results["metadata"]

    internal_file = output_dir / "internal_links.json"
    save_json(internal_results, internal_file)
    print(f"Saved to: {internal_file}")

    # 3. Link Graph Analysis
    print("\n" + "=" * 60)
    print("PHASE 3: Link Graph Analysis")
    print("=" * 60)

    graph_analyzer = LinkGraphAnalyzer(dist_path, excluded_paths=excluded_paths)
    graph_results = graph_analyzer.analyze(
        underlinked_threshold=thresholds.get("underlinked_min_inbound", 3),
        overlinked_threshold=thresholds.get("overlinked_max_outbound", 50),
        sink_min_inbound=thresholds.get("link_sink_min_inbound", 5),
        sink_max_outbound=thresholds.get("link_sink_max_outbound", 2)
    )
    results["link_graph"] = {
        "metadata": graph_results["metadata"],
        "summary": graph_results["summary"]
    }

    graph_file = output_dir / "link_graph.json"
    save_json(graph_results, graph_file)
    print(f"Saved to: {graph_file}")

    # Generate markdown report
    report = generate_graph_report(graph_results)
    report_file = output_dir / "link_graph_report.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Report saved to: {report_file}")

    # 4. HTTP Check (optional, skip by default for speed)
    if not skip_http:
        print("\n" + "=" * 60)
        print("PHASE 4: HTTP Link Validation")
        print("=" * 60)
        print("Skipped. Run http_checker.py separately with --input outbound_links.json")
        results["http_check"] = {"status": "skipped"}
    else:
        results["http_check"] = {"status": "skipped"}

    return results


def generate_summary_report(results: dict, output_path: Path) -> None:
    """Generate overall summary report"""

    lines = [
        "# Link Analysis Summary Report",
        "",
        f"**Generated:** {results['metadata']['analyzed_at']}",
        f"**Site Path:** `{results['metadata']['dist_path']}`",
        "",
        "## Overview",
        "",
    ]

    # Outbound summary
    if results.get("outbound"):
        ob = results["outbound"]
        lines.extend([
            "### Outbound Links",
            f"- Files analyzed: {ob['files_analyzed']}",
            f"- Unique external links: {ob['unique_links']}",
            f"- Unique domains: {ob['unique_domains']}",
            f"- Total occurrences: {ob['total_link_occurrences']}",
            "",
        ])

    # Internal summary
    if results.get("internal"):
        il = results["internal"]
        lines.extend([
            "### Internal Links",
            f"- Files analyzed: {il['files_analyzed']}",
            f"- Links checked: {il['total_links_checked']}",
            f"- Valid links: {il['valid_links']}",
            f"- **Broken links: {il['broken_links']}**",
            "",
        ])

    # Link graph summary
    if results.get("link_graph"):
        lg = results["link_graph"]
        meta = lg["metadata"]
        summary = lg["summary"]
        lines.extend([
            "### Link Graph",
            f"- Total pages: {meta['total_pages']}",
            f"- Total internal links: {meta['total_links']}",
            "",
            "#### Issues Found",
            f"- **Orphan pages (critical):** {summary['orphan_pages']}",
            f"- Under-linked pages: {summary['underlinked_pages']}",
            f"- Over-linked pages: {summary['overlinked_pages']}",
            f"- Link sinks: {summary['link_sinks']}",
            "",
        ])

    # Recommendations
    lines.extend([
        "## Recommendations",
        "",
    ])

    if results.get("link_graph"):
        summary = results["link_graph"]["summary"]
        if summary["orphan_pages"] > 0:
            lines.append(f"1. **Critical:** Fix {summary['orphan_pages']} orphan pages - these may not be indexed by search engines")
        if summary["underlinked_pages"] > 0:
            lines.append(f"2. Add internal links to {summary['underlinked_pages']} under-linked pages")
        if summary["link_sinks"] > 0:
            lines.append(f"3. Add outbound links to {summary['link_sinks']} link sink pages to distribute link equity")

    if results.get("internal") and results["internal"]["broken_links"] > 0:
        lines.append(f"4. Fix {results['internal']['broken_links']} broken internal links")

    lines.extend([
        "",
        "## Next Steps",
        "",
        "1. Review detailed reports in the output directory",
        "2. Run HTTP validation: `python http_checker.py --input outbound_links.json`",
        "3. Prioritize fixes based on SEO impact",
    ])

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(description="Link Analyzer - Full Analysis")
    parser.add_argument("--dist", "-d", required=True, help="Path to dist directory")
    parser.add_argument("--config", help="Path to config.json")
    parser.add_argument("--output-dir", "-o", default="./link_analysis_results",
                        help="Output directory for results")
    parser.add_argument("--full", action="store_true", help="Run full analysis")
    parser.add_argument("--skip-http", action="store_true", default=True,
                        help="Skip HTTP validation (default, run separately)")

    args = parser.parse_args()

    # Load config
    config = {}
    if args.config:
        config_path = Path(args.config)
        if config_path.exists():
            config = load_json_config(config_path)
    else:
        # Try default config
        default_config = Path(__file__).parent.parent / "config.json"
        if default_config.exists():
            config = load_json_config(default_config)

    dist_path = Path(args.dist)
    if not dist_path.exists():
        print(f"Error: Directory not found: {dist_path}", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output_dir)

    print("=" * 60)
    print("LINK ANALYZER - FULL ANALYSIS")
    print("=" * 60)
    print(f"Source: {dist_path}")
    print(f"Output: {output_dir}")

    # Run analysis
    results = run_full_analysis(
        dist_path=dist_path,
        config=config,
        output_dir=output_dir,
        skip_http=args.skip_http
    )

    # Save overall results
    results_file = output_dir / "analysis_summary.json"
    save_json(results, results_file)

    # Generate summary report
    report_file = output_dir / "SUMMARY_REPORT.md"
    generate_summary_report(results, report_file)

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print(f"Results saved to: {output_dir}")
    print(f"Summary report: {report_file}")

    # Quick stats
    if results.get("link_graph"):
        summary = results["link_graph"]["summary"]
        print(f"\nKey Issues:")
        print(f"  - Orphan pages: {summary['orphan_pages']}")
        print(f"  - Under-linked: {summary['underlinked_pages']}")
        print(f"  - Link sinks: {summary['link_sinks']}")

    if results.get("internal"):
        print(f"  - Broken internal links: {results['internal']['broken_links']}")


if __name__ == "__main__":
    main()
