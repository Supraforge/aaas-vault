#!/usr/bin/env python3
"""
CE Research - Validation Script
Scores research completeness and quality, identifies gaps
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


def extract_blocks(content: str) -> dict:
    """Extract named blocks from research content"""
    blocks = {}
    pattern = r'===== ce\.[^.]+\.([^\s=]+) =====\n(.*?)(?====== |$)'
    matches = re.findall(pattern, content, re.DOTALL)

    for key, value in matches:
        blocks[key] = value.strip()

    return blocks


def score_block(content: str) -> dict:
    """Score a single block for quality"""
    if not content:
        return {"score": 0, "issues": ["Empty block"]}

    issues = []
    score = 100

    # Check for placeholder text
    if '[' in content and ']' in content and len(content) < 50:
        issues.append("Contains placeholder text")
        score -= 50

    # Check for minimum content length
    word_count = len(content.split())
    if word_count < 10:
        issues.append(f"Too short ({word_count} words)")
        score -= 30
    elif word_count < 25:
        issues.append(f"Brief content ({word_count} words)")
        score -= 15

    # Check for specificity (numbers, proper nouns)
    has_numbers = bool(re.search(r'\d+', content))
    has_proper_nouns = bool(re.search(r'[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*', content))

    if not has_numbers and not has_proper_nouns:
        issues.append("Lacks specific details (no numbers or names)")
        score -= 20

    # Check for low confidence markers
    if '[LOW CONFIDENCE]' in content or '[UNVERIFIED]' in content:
        issues.append("Contains low confidence data")
        score -= 10

    return {
        "score": max(0, score),
        "word_count": word_count,
        "issues": issues
    }


def validate_dimension(research_dir: Path, dimension: str) -> dict:
    """Validate a single research dimension"""
    file_path = research_dir / f"{dimension}.md"

    if not file_path.exists():
        return {
            "exists": False,
            "score": 0,
            "blocks": {},
            "issues": [f"Research file not found: {dimension}.md"]
        }

    content = file_path.read_text()
    blocks = extract_blocks(content)

    block_scores = {}
    total_score = 0
    all_issues = []

    for key, value in blocks.items():
        result = score_block(value)
        block_scores[key] = result
        total_score += result["score"]
        all_issues.extend([f"{key}: {issue}" for issue in result["issues"]])

    avg_score = total_score / len(blocks) if blocks else 0

    return {
        "exists": True,
        "score": round(avg_score, 1),
        "block_count": len(blocks),
        "blocks": block_scores,
        "issues": all_issues
    }


def map_to_squr_sections(validation_results: dict, section_map: dict) -> dict:
    """Map validation results to SQUR sections"""
    squr_scores = {}

    for section_key, section_config in section_map['squr_sections'].items():
        source_scores = []

        for source in section_config['sources']:
            file_name = source['file'].replace('.md', '')
            if file_name == 'all':
                # Aggregate all dimensions
                for dim, result in validation_results.items():
                    if result['exists']:
                        source_scores.append(result['score'])
            elif file_name in validation_results:
                result = validation_results[file_name]
                if result['exists']:
                    # Check if specific blocks are present
                    for block_key in source['blocks']:
                        if block_key in result['blocks']:
                            source_scores.append(result['blocks'][block_key]['score'])

        avg_score = sum(source_scores) / len(source_scores) if source_scores else 0
        squr_scores[section_key] = {
            "title": section_config['title'],
            "score": round(avg_score, 1),
            "source_count": len(source_scores),
            "status": "good" if avg_score >= 60 else "needs_work" if avg_score >= 30 else "missing"
        }

    return squr_scores


def generate_report(company: str, validation_results: dict, squr_scores: dict) -> str:
    """Generate validation report markdown"""
    lines = [
        f"# CE Research Validation Report",
        f"**Company:** {company}",
        f"**Generated:** {datetime.now().isoformat()}",
        "",
        "---",
        "",
        "## Research Dimension Scores",
        ""
    ]

    dimensions = ['company', 'competitors', 'market', 'audience', 'brand', 'strategy']

    for dim in dimensions:
        result = validation_results.get(dim, {"exists": False, "score": 0})
        status = "OK" if result.get('score', 0) >= 60 else "NEEDS WORK" if result.get('exists') else "MISSING"
        score = result.get('score', 0)
        lines.append(f"| {dim.title():15} | {score:5.1f}% | {status:10} |")

    lines.extend([
        "",
        "## SQUR Section Coverage",
        "",
        "| Section | Score | Status |",
        "|---------|-------|--------|"
    ])

    for section_key, section_data in squr_scores.items():
        status_emoji = "" if section_data['status'] == 'good' else "" if section_data['status'] == 'needs_work' else ""
        lines.append(f"| {section_data['title']} | {section_data['score']:.1f}% | {status_emoji} {section_data['status']} |")

    # Identify gaps
    gaps = [s for s, d in squr_scores.items() if d['status'] != 'good']
    if gaps:
        lines.extend([
            "",
            "## Gaps Requiring Additional Research",
            ""
        ])
        for gap in gaps:
            section = squr_scores[gap]
            lines.append(f"- **{section['title']}**: Score {section['score']:.1f}% - needs more data")

    # Issues summary
    all_issues = []
    for dim, result in validation_results.items():
        all_issues.extend(result.get('issues', []))

    if all_issues:
        lines.extend([
            "",
            "## Issues Found",
            ""
        ])
        for issue in all_issues[:20]:  # Limit to top 20
            lines.append(f"- {issue}")

    # Overall assessment
    overall_score = sum(d['score'] for d in squr_scores.values()) / len(squr_scores)
    lines.extend([
        "",
        "---",
        "",
        f"## Overall Assessment",
        f"**Aggregate Score:** {overall_score:.1f}%",
        f"**Ready for Synthesis:** {'Yes' if overall_score >= 60 else 'No - address gaps first'}",
        ""
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Validate CE research quality")
    parser.add_argument('--company', '-c', required=True, help='Company name')
    parser.add_argument('--output', '-o', help='Custom output path')
    args = parser.parse_args()

    skill_dir = get_skill_dir()
    safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in args.company)
    output_dir = skill_dir / "output" / safe_name
    research_dir = output_dir / "research"

    if not research_dir.exists():
        print(f"No research found for: {args.company}")
        print(f"Expected directory: {research_dir}")
        return 1

    # Load section mapping
    section_map = load_section_map()

    # Validate each dimension
    dimensions = ['company', 'competitors', 'market', 'audience', 'brand', 'strategy']
    validation_results = {}

    print(f"Validating research for: {args.company}")
    print("="*50)

    for dim in dimensions:
        result = validate_dimension(research_dir, dim)
        validation_results[dim] = result
        status = "OK" if result['score'] >= 60 else "NEEDS WORK" if result['exists'] else "MISSING"
        print(f"  {dim:15} | Score: {result['score']:5.1f}% | {status}")

    # Map to SQUR sections
    squr_scores = map_to_squr_sections(validation_results, section_map)

    # Generate report
    report = generate_report(args.company, validation_results, squr_scores)

    # Save report
    report_path = output_dir / "validation_report.md"
    report_path.write_text(report)
    print(f"\nValidation report saved to: {report_path}")

    # Return exit code based on overall score
    overall = sum(d['score'] for d in squr_scores.values()) / len(squr_scores)
    print(f"\nOverall Score: {overall:.1f}%")

    if overall >= 60:
        print("Ready for synthesis!")
        return 0
    else:
        print("Address gaps before synthesis.")
        return 1


if __name__ == "__main__":
    exit(main())
