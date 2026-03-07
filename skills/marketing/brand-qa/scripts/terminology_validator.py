#!/usr/bin/env python3
"""
Terminology Validator - Checks content for required brand terminology and anti-patterns.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

SKILL_DIR = Path(__file__).parent.parent
PROJECT_ROOT = SKILL_DIR.parent.parent


def load_brand_config(brand_slug: str) -> Dict:
    """Load brand configuration."""
    config_path = PROJECT_ROOT / "context" / "brand_configs" / f"{brand_slug}.json"
    if not config_path.exists():
        raise FileNotFoundError(f"Brand config not found: {config_path}")

    with open(config_path) as f:
        return json.load(f)


def load_lexicon(brand_slug: str) -> Dict:
    """Load brand lexicon (required terms)."""
    # Try brand-specific first
    lexicon_path = SKILL_DIR / "resources" / f"{brand_slug}_lexicon.json"
    if not lexicon_path.exists():
        lexicon_path = SKILL_DIR / "resources" / "[PROJECT_NAME]_lexicon.json"

    if not lexicon_path.exists():
        return {"required_terms": [], "preferred_phrases": [], "min_required": 2}

    with open(lexicon_path) as f:
        return json.load(f)


def load_anti_patterns() -> Dict:
    """Load anti-patterns to avoid."""
    anti_path = SKILL_DIR / "resources" / "anti_patterns.json"
    if not anti_path.exists():
        return {"patterns": []}

    with open(anti_path) as f:
        return json.load(f)


class TerminologyValidator:
    """Validate content terminology against brand guidelines."""

    def __init__(self, brand_config: Dict, lexicon: Dict, anti_patterns: Dict):
        self.brand_config = brand_config
        self.lexicon = lexicon
        self.anti_patterns = anti_patterns
        self.min_required = lexicon.get("min_required", 2)

    def validate(self, text: str) -> Dict:
        """Validate text for terminology compliance."""
        text_lower = text.lower()

        results = {
            "brand": self.brand_config.get("brand_name", "Unknown"),
            "terminology_score": 0,
            "required_terms": {
                "found": [],
                "missing": [],
                "count": 0,
                "minimum": self.min_required
            },
            "preferred_phrases": {
                "found": [],
                "count": 0
            },
            "anti_patterns": {
                "violations": [],
                "count": 0
            },
            "suggestions": [],
            "passed": False
        }

        # Check required terms
        required_terms = self.lexicon.get("required_terms", [])
        for term_info in required_terms:
            term = term_info if isinstance(term_info, str) else term_info.get("term", "")
            term_lower = term.lower()

            if term_lower in text_lower:
                results["required_terms"]["found"].append(term)
            else:
                results["required_terms"]["missing"].append(term)

        results["required_terms"]["count"] = len(results["required_terms"]["found"])

        # Check preferred phrases
        preferred = self.lexicon.get("preferred_phrases", [])
        for phrase_info in preferred:
            phrase = phrase_info if isinstance(phrase_info, str) else phrase_info.get("phrase", "")
            phrase_lower = phrase.lower()

            if phrase_lower in text_lower:
                results["preferred_phrases"]["found"].append(phrase)

        results["preferred_phrases"]["count"] = len(results["preferred_phrases"]["found"])

        # Check anti-patterns
        patterns = self.anti_patterns.get("patterns", [])
        for pattern_info in patterns:
            bad_term = pattern_info.get("avoid", "").lower()
            replacement = pattern_info.get("use_instead", "")
            context = pattern_info.get("context", "")

            if bad_term and bad_term in text_lower:
                results["anti_patterns"]["violations"].append({
                    "found": bad_term,
                    "use_instead": replacement,
                    "context": context
                })

        results["anti_patterns"]["count"] = len(results["anti_patterns"]["violations"])

        # Calculate score
        # Required terms: 50 points max (based on meeting minimum)
        req_score = min(50, (results["required_terms"]["count"] / max(1, self.min_required)) * 50)

        # Preferred phrases: 30 points max (10 per phrase, max 3)
        pref_score = min(30, results["preferred_phrases"]["count"] * 10)

        # Anti-pattern penalty: -15 per violation
        violation_penalty = results["anti_patterns"]["count"] * 15

        total_score = max(0, req_score + pref_score - violation_penalty)
        results["terminology_score"] = round(total_score, 1)

        # Determine pass/fail
        meets_minimum = results["required_terms"]["count"] >= self.min_required
        no_violations = results["anti_patterns"]["count"] == 0
        results["passed"] = meets_minimum and results["terminology_score"] >= 50

        # Generate suggestions
        results["suggestions"] = self._generate_suggestions(results)

        return results

    def _generate_suggestions(self, results: Dict) -> List[str]:
        """Generate improvement suggestions."""
        suggestions = []

        # Missing required terms
        missing = results["required_terms"]["missing"]
        if missing and results["required_terms"]["count"] < self.min_required:
            suggestions.append(f"Add at least {self.min_required - results['required_terms']['count']} more required term(s)")
            suggestions.append(f"Consider using: {', '.join(missing[:3])}")

        # Anti-pattern violations
        for violation in results["anti_patterns"]["violations"]:
            suggestions.append(
                f"Replace \"{violation['found']}\" with \"{violation['use_instead']}\""
            )

        # Encourage preferred phrases
        if results["preferred_phrases"]["count"] == 0:
            preferred = self.lexicon.get("preferred_phrases", [])[:3]
            if preferred:
                phrases = [p if isinstance(p, str) else p.get("phrase", "") for p in preferred]
                suggestions.append(f"Consider using key phrases: {', '.join(phrases)}")

        return suggestions


def main():
    parser = argparse.ArgumentParser(description="Validate content terminology against brand guidelines")
    parser.add_argument("file", help="Path to content file")
    parser.add_argument("--brand", "-b", default="[PROJECT_NAME]", help="Brand slug (default: [PROJECT_NAME])")
    parser.add_argument("--output", "-o", choices=["json", "text"], default="text", help="Output format")
    parser.add_argument("--strict", "-s", action="store_true", help="Exit 1 on any violation")

    args = parser.parse_args()

    # Load content
    try:
        with open(args.file) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    # Load configs
    try:
        brand_config = load_brand_config(args.brand)
        lexicon = load_lexicon(args.brand)
        anti_patterns = load_anti_patterns()
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Validate
    validator = TerminologyValidator(brand_config, lexicon, anti_patterns)
    results = validator.validate(content)

    # Output
    if args.output == "json":
        print(json.dumps(results, indent=2))
    else:
        print(f"\n{'='*50}")
        print(f"TERMINOLOGY CHECK: {results['brand']}")
        print(f"{'='*50}")
        print(f"\nFile: {args.file}")
        print(f"\nTERMINOLOGY SCORE: {results['terminology_score']}/100 {'PASS' if results['passed'] else 'NEEDS WORK'}")

        print(f"\n--- Required Terms ({results['required_terms']['count']}/{results['required_terms']['minimum']} minimum) ---")
        if results["required_terms"]["found"]:
            print(f"  Found: {', '.join(results['required_terms']['found'])}")
        if results["required_terms"]["missing"]:
            print(f"  Missing: {', '.join(results['required_terms']['missing'][:5])}")

        if results["preferred_phrases"]["found"]:
            print(f"\n--- Preferred Phrases Found ---")
            for phrase in results["preferred_phrases"]["found"]:
                print(f"  + {phrase}")

        if results["anti_patterns"]["violations"]:
            print(f"\n--- Anti-Pattern Violations ({results['anti_patterns']['count']}) ---")
            for v in results["anti_patterns"]["violations"]:
                print(f"  ! \"{v['found']}\" -> use \"{v['use_instead']}\"")

        if results["suggestions"]:
            print(f"\n--- Suggestions ---")
            for s in results["suggestions"]:
                print(f"  - {s}")

        print()

    # Strict mode exit
    if args.strict and (not results["passed"] or results["anti_patterns"]["count"] > 0):
        sys.exit(1)


if __name__ == "__main__":
    main()
