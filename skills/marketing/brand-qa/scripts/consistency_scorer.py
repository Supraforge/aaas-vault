#!/usr/bin/env python3
"""
Consistency Scorer - Comprehensive brand consistency scoring combining voice and terminology.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict

# Import sibling modules
SKILL_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(SKILL_DIR / "scripts"))

from voice_checker import BrandVoiceChecker, load_brand_config, load_brand_lexicon
from terminology_validator import TerminologyValidator, load_lexicon, load_anti_patterns


class ConsistencyScorer:
    """Generate comprehensive brand consistency scores."""

    def __init__(self, brand_slug: str):
        self.brand_slug = brand_slug
        self.brand_config = load_brand_config(brand_slug)
        self.lexicon = load_lexicon(brand_slug)
        self.anti_patterns = load_anti_patterns()

        # Initialize checkers
        self.voice_checker = BrandVoiceChecker(self.brand_config, self.lexicon)
        self.term_validator = TerminologyValidator(self.brand_config, self.lexicon, self.anti_patterns)

    def score(self, text: str, threshold: int = 80) -> Dict:
        """Generate comprehensive consistency score."""

        # Run individual checks
        voice_results = self.voice_checker.check_voice(text)
        term_results = self.term_validator.validate(text)

        # Calculate weighted overall score
        # Voice: 40%, Terminology: 35%, Readability: 25%
        voice_score = voice_results.get("voice_score", 0)
        term_score = term_results.get("terminology_score", 0)
        readability_score = voice_results.get("readability", {}).get("score", 50)

        overall_score = (
            voice_score * 0.40 +
            term_score * 0.35 +
            readability_score * 0.25
        )

        # Determine grade
        if overall_score >= 90:
            grade = "A"
            grade_label = "Excellent"
        elif overall_score >= 80:
            grade = "B"
            grade_label = "Good"
        elif overall_score >= 70:
            grade = "C"
            grade_label = "Acceptable"
        elif overall_score >= 60:
            grade = "D"
            grade_label = "Needs Work"
        else:
            grade = "F"
            grade_label = "Significant Revision Needed"

        # Compile results
        results = {
            "brand": self.brand_config.get("brand_name", "Unknown"),
            "overall_score": round(overall_score, 1),
            "grade": grade,
            "grade_label": grade_label,
            "threshold": threshold,
            "passed": overall_score >= threshold,
            "components": {
                "voice": {
                    "score": voice_score,
                    "weight": "40%",
                    "weighted_contribution": round(voice_score * 0.40, 1)
                },
                "terminology": {
                    "score": term_score,
                    "weight": "35%",
                    "weighted_contribution": round(term_score * 0.35, 1)
                },
                "readability": {
                    "score": readability_score,
                    "weight": "25%",
                    "weighted_contribution": round(readability_score * 0.25, 1)
                }
            },
            "details": {
                "voice": {
                    "tone_analysis": voice_results.get("tone_analysis", {}),
                    "formality": voice_results.get("formality", {}),
                    "style": voice_results.get("style_assessment", {})
                },
                "terminology": {
                    "required_found": term_results.get("required_terms", {}).get("count", 0),
                    "required_minimum": term_results.get("required_terms", {}).get("minimum", 2),
                    "violations": term_results.get("anti_patterns", {}).get("count", 0)
                },
                "readability": voice_results.get("readability", {})
            },
            "recommendations": self._compile_recommendations(voice_results, term_results),
            "word_count": voice_results.get("word_count", 0)
        }

        return results

    def _compile_recommendations(self, voice_results: Dict, term_results: Dict) -> list:
        """Compile and prioritize recommendations from both checks."""
        all_recs = []

        # High priority: Anti-pattern violations
        for violation in term_results.get("anti_patterns", {}).get("violations", []):
            all_recs.append({
                "priority": "high",
                "category": "terminology",
                "message": f"Replace \"{violation['found']}\" with \"{violation['use_instead']}\""
            })

        # High priority: Missing required terms
        term_count = term_results.get("required_terms", {}).get("count", 0)
        term_min = term_results.get("required_terms", {}).get("minimum", 2)
        if term_count < term_min:
            missing = term_results.get("required_terms", {}).get("missing", [])[:3]
            all_recs.append({
                "priority": "high",
                "category": "terminology",
                "message": f"Add {term_min - term_count} more required term(s): {', '.join(missing)}"
            })

        # Medium priority: Voice recommendations
        for rec in voice_results.get("recommendations", []):
            all_recs.append({
                "priority": "medium",
                "category": "voice",
                "message": rec
            })

        # Medium priority: Term suggestions
        for sug in term_results.get("suggestions", []):
            if "Replace" not in sug and "Add at least" not in sug:  # Avoid duplicates
                all_recs.append({
                    "priority": "low",
                    "category": "terminology",
                    "message": sug
                })

        # Sort by priority
        priority_order = {"high": 0, "medium": 1, "low": 2}
        all_recs.sort(key=lambda x: priority_order.get(x["priority"], 3))

        return all_recs


def main():
    parser = argparse.ArgumentParser(description="Generate comprehensive brand consistency score")
    parser.add_argument("file", help="Path to content file")
    parser.add_argument("--brand", "-b", default="[PROJECT_NAME]", help="Brand slug (default: [PROJECT_NAME])")
    parser.add_argument("--output", "-o", choices=["json", "text"], default="text", help="Output format")
    parser.add_argument("--threshold", "-t", type=int, default=80, help="Pass/fail threshold (default: 80)")

    args = parser.parse_args()

    # Load content
    try:
        with open(args.file) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    # Score content
    try:
        scorer = ConsistencyScorer(args.brand)
        results = scorer.score(content, args.threshold)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Output
    if args.output == "json":
        print(json.dumps(results, indent=2))
    else:
        passed_str = "PASS" if results["passed"] else "FAIL"

        print(f"\n{'='*60}")
        print(f"BRAND CONSISTENCY REPORT: {results['brand']}")
        print(f"{'='*60}")
        print(f"\nFile: {args.file}")
        print(f"Words: {results['word_count']}")

        print(f"\n{'='*60}")
        print(f"  OVERALL SCORE: {results['overall_score']}/100  [{results['grade']}] {results['grade_label']}")
        print(f"  Threshold: {results['threshold']}  Status: {passed_str}")
        print(f"{'='*60}")

        print(f"\n--- Score Components ---")
        for component, data in results["components"].items():
            bar_len = int(data["score"] / 5)
            bar = "#" * bar_len + "-" * (20 - bar_len)
            print(f"  {component.title():12} [{bar}] {data['score']:5.1f}/100 ({data['weight']})")

        print(f"\n--- Details ---")
        details = results["details"]

        # Terminology details
        term_d = details["terminology"]
        print(f"  Terminology: {term_d['required_found']}/{term_d['required_minimum']} required terms, {term_d['violations']} violations")

        # Readability
        read_d = details["readability"]
        print(f"  Readability: {read_d.get('score', 0):.1f}/100 ({read_d.get('level', 'unknown')})")

        # Recommendations
        recs = results["recommendations"]
        if recs:
            print(f"\n--- Recommendations ({len(recs)}) ---")
            for rec in recs[:7]:  # Show top 7
                priority_icon = {"high": "!", "medium": "*", "low": "-"}.get(rec["priority"], "-")
                print(f"  {priority_icon} [{rec['category']}] {rec['message']}")

        print()

    # Exit with error if not passing
    if not results["passed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
