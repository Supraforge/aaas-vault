#!/usr/bin/env python3
"""
Base module for CE Research scripts
Provides common utilities for all research dimensions
"""

import json
import argparse
from pathlib import Path
from datetime import datetime


def get_skill_dir() -> Path:
    """Get the skill root directory"""
    return Path(__file__).parent.parent


def get_output_dir(company: str) -> Path:
    """Get or create the output directory for a company"""
    skill_dir = get_skill_dir()
    # Sanitize company name for directory
    safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in company)
    output_dir = skill_dir / "output" / safe_name
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create research subdirectory
    research_dir = output_dir / "research"
    research_dir.mkdir(exist_ok=True)

    return output_dir


def load_prompts() -> dict:
    """Load CE prompts configuration"""
    prompts_file = get_skill_dir() / "resources" / "ce_prompts.json"
    with open(prompts_file) as f:
        return json.load(f)


def format_block(company: str, key: str, content: str) -> str:
    """Format a content block with the standard pattern"""
    return f"===== ce.{company}.{key} =====\n{content}\n"


def format_reliability_report(scores: dict) -> str:
    """Format a reliability report section"""
    lines = ["===== reliability-report ====="]
    for key, score in scores.items():
        lines.append(f"- {key}: {score}")
    return "\n".join(lines)


def save_research(company: str, dimension: str, content: str) -> Path:
    """Save research output to the appropriate file"""
    output_dir = get_output_dir(company)
    research_file = output_dir / "research" / f"{dimension}.md"

    # Add metadata header
    header = f"""# CE Research: {dimension.title()} - {company}
Generated: {datetime.now().isoformat()}

---

"""

    with open(research_file, 'w') as f:
        f.write(header + content)

    return research_file


def create_research_parser(dimension: str, description: str) -> argparse.ArgumentParser:
    """Create standard argument parser for research scripts"""
    parser = argparse.ArgumentParser(
        description=f"CE Research - {description}",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--company', '-c',
        required=True,
        help='Company name to research'
    )
    parser.add_argument(
        '--output', '-o',
        help='Custom output directory (optional)'
    )
    parser.add_argument(
        '--generate-prompt', '-g',
        action='store_true',
        help='Generate research prompt for Claude to execute'
    )
    return parser


def generate_research_prompt(company: str, dimension: str, config: dict) -> str:
    """Generate a research prompt for Claude to execute"""

    prompt_parts = [
        f"# CE Deep Research - {config['name']}",
        f"**Company:** {company}",
        "",
        f"## Role",
        f"You are my {config['role']}.",
        "",
        f"## Task",
        f"{config['description']}",
        "",
        f"## Sources to Check",
    ]

    for source in config['sources']:
        prompt_parts.append(f"- {source}")

    prompt_parts.extend([
        "",
        "## Search Queries to Execute",
        "Use WebSearch for these queries:",
        ""
    ])

    for query in config['search_queries']:
        formatted_query = query.replace('{company}', company).replace('{industry}', f'{company} industry')
        prompt_parts.append(f"- `{formatted_query}`")

    prompt_parts.extend([
        "",
        "## Required Output Format",
        f"Structure your findings using these blocks (replace {company} with actual name):",
        ""
    ])

    for block in config['output_blocks']:
        prompt_parts.append(f"```")
        prompt_parts.append(f"===== ce.{company}.{block['key']} =====")
        prompt_parts.append(f"[{block['description']}]")
        prompt_parts.append(f"```")
        prompt_parts.append("")

    if 'per_competitor_blocks' in config:
        prompt_parts.extend([
            "For each competitor found, also output:",
            ""
        ])
        for block in config['per_competitor_blocks']:
            prompt_parts.append(f"```")
            prompt_parts.append(f"===== ce.{company}.competitor.{{competitor_name}}.{block['key']} =====")
            prompt_parts.append(f"[{block['description']}]")
            prompt_parts.append(f"```")
            prompt_parts.append("")

    prompt_parts.extend([
        "## Quality Requirements",
        "- Every fact must be concrete and specific (names, numbers, features)",
        "- No generic fluff or filler statements",
        "- If information is uncertain, mark with [LOW CONFIDENCE]",
        "- Include source URLs where possible",
        "",
        "## End with Reliability Report",
        "```",
        "===== reliability-report =====",
        "- confidence: [HIGH/MEDIUM/LOW]",
        "- sources_checked: [count]",
        "- data_freshness: [date or estimate]",
        "- gaps: [list any missing information]",
        "```"
    ])

    return "\n".join(prompt_parts)
