#!/usr/bin/env python3
"""
CE Research - Framework Synthesis Script
Combines validated research into SQUR-pattern contextual framework document
"""

import argparse
import json
import re
from pathlib import Path
from datetime import datetime


def get_skill_dir() -> Path:
    """Get the skill root directory"""
    return Path(__file__).parent.parent


def load_section_map() -> dict:
    """Load section mapping configuration"""
    map_file = get_skill_dir() / "resources" / "section_map.json"
    with open(map_file) as f:
        return json.load(f)


def load_squr_template() -> str:
    """Load SQUR template for reference"""
    template_file = get_skill_dir() / "resources" / "squr_template.md"
    return template_file.read_text()


def extract_blocks(content: str) -> dict:
    """Extract named blocks from research content"""
    blocks = {}
    pattern = r'===== ce\.[^.]+\.([^\s=]+) =====\n(.*?)(?====== |$)'
    matches = re.findall(pattern, content, re.DOTALL)

    for key, value in matches:
        blocks[key] = value.strip()

    return blocks


def load_all_research(research_dir: Path) -> dict:
    """Load all research files and extract blocks"""
    all_blocks = {}
    dimensions = ['company', 'competitors', 'market', 'audience', 'brand', 'strategy']

    for dim in dimensions:
        file_path = research_dir / f"{dim}.md"
        if file_path.exists():
            content = file_path.read_text()
            blocks = extract_blocks(content)
            all_blocks[dim] = blocks

    return all_blocks


def format_bullet(label: str, content: str) -> str:
    """Format a bullet point with bold label"""
    # Clean up content
    content = content.strip()
    if not content:
        return ""
    # Ensure proper formatting
    return f"- **{label}:** {content}"


def synthesize_section(section_key: str, section_config: dict, research: dict) -> list:
    """Synthesize a single SQUR section from research"""
    bullets = []

    for source in section_config['sources']:
        file_name = source['file'].replace('.md', '')

        if file_name == 'all':
            # Aggregate sources from all dimensions
            for dim, blocks in research.items():
                if 'sources_used' in blocks or 'reliability-report' in blocks:
                    content = blocks.get('sources_used', blocks.get('reliability-report', ''))
                    if content:
                        bullets.append(format_bullet(dim.title(), content[:200]))
        elif file_name in research:
            dim_blocks = research[file_name]
            for block_key in source['blocks']:
                if block_key in dim_blocks:
                    content = dim_blocks[block_key]
                    # Parse content into individual bullets
                    lines = content.split('\n')
                    for line in lines:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            # Check if already formatted as bullet
                            if line.startswith('-'):
                                line = line[1:].strip()
                            if line.startswith('*'):
                                line = line[1:].strip()
                            # Extract label if present
                            if ':' in line:
                                parts = line.split(':', 1)
                                label = parts[0].strip().replace('**', '').replace('*', '')
                                value = parts[1].strip()
                                bullets.append(format_bullet(label, value))
                            else:
                                bullets.append(f"- {line}")

    return bullets[:8]  # Limit to 8 bullets per section


def generate_framework(company: str, research: dict, section_map: dict) -> str:
    """Generate the full SQUR framework document"""

    # Emoji mapping
    emoji_map = {
        "brain": "brain",
        "lock": "lock",
        "busts_in_silhouette": "busts_in_silhouette",
        "globe_with_meridians": "globe_with_meridians",
        "crossed_swords": "crossed_swords",
        "chart_with_upwards_trend": "chart_with_upwards_trend",
        "fire": "fire",
        "dart": "dart",
        "books": "books"
    }

    lines = [
        f"# {company} Contextual Framework Document",
        "",
        f"This document serves as a high-context reference framework for {company}, "
        "summarizing key research insights and providing strategic context to guide "
        "product development, marketing, AI prompting, and lead generation initiatives.",
        ""
    ]

    # Generate each section
    for section_key in section_map['section_order']:
        section_config = section_map['squr_sections'][section_key]
        emoji = section_config['emoji']
        title = section_config['title']

        lines.append(f"## {title}")
        lines.append("")

        # Synthesize bullets for this section
        bullets = synthesize_section(section_key, section_config, research)

        if bullets:
            for bullet in bullets:
                if bullet:
                    lines.append(bullet)
            lines.append("")
        else:
            lines.append(f"- [No data available - research this dimension]")
            lines.append("")

    # Add footer
    lines.extend([
        "---",
        "",
        f"*Generated: {datetime.now().strftime('%Y-%m-%d')}*",
        "",
        "This framework should be updated continuously with new customer insights, "
        "competitive shifts, and feature evolution. It is the primary contextual base "
        f"to inform AI prompting, content generation, positioning, and product/UX decisions "
        f"for {company}.",
        ""
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Synthesize SQUR framework from research")
    parser.add_argument('--company', '-c', required=True, help='Company name')
    parser.add_argument('--force', '-f', action='store_true', help='Force synthesis even with gaps')
    parser.add_argument('--output', '-o', help='Custom output path')
    args = parser.parse_args()

    skill_dir = get_skill_dir()
    safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in args.company)
    output_dir = skill_dir / "output" / safe_name
    research_dir = output_dir / "research"

    if not research_dir.exists():
        print(f"No research found for: {args.company}")
        print(f"Expected directory: {research_dir}")
        print("\nRun research scripts first, e.g.:")
        print(f"  python run.py research_company.py --company '{args.company}' --generate-prompt")
        return 1

    # Check validation report
    validation_report = output_dir / "validation_report.md"
    if validation_report.exists() and not args.force:
        content = validation_report.read_text()
        if "Ready for Synthesis:** No" in content:
            print("Warning: Validation report indicates gaps in research.")
            print("Use --force to synthesize anyway, or address gaps first.")
            print(f"\nSee: {validation_report}")
            return 1

    print(f"Synthesizing framework for: {args.company}")
    print("="*50)

    # Load resources
    section_map = load_section_map()

    # Load all research
    research = load_all_research(research_dir)

    if not research:
        print("No research data found!")
        return 1

    print(f"Loaded research from {len(research)} dimensions:")
    for dim in research:
        block_count = len(research[dim])
        print(f"  - {dim}: {block_count} blocks")

    # Generate framework
    framework = generate_framework(args.company, research, section_map)

    # Count lines
    line_count = len(framework.split('\n'))
    print(f"\nGenerated framework: {line_count} lines")

    # Save framework
    framework_path = args.output if args.output else output_dir / "context_framework.md"
    Path(framework_path).write_text(framework)
    print(f"Framework saved to: {framework_path}")

    return 0


if __name__ == "__main__":
    exit(main())
