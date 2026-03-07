#!/usr/bin/env python3
"""
Brand Voice Checker - Validates content against brand voice guidelines.
Extended from content-creator/brand_voice_analyzer.py with brand-specific validation.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Add parent directories to path for imports
SKILL_DIR = Path(__file__).parent.parent
PROJECT_ROOT = SKILL_DIR.parent.parent


def load_brand_config(brand_slug: str) -> Dict:
    """Load brand configuration by slug."""
    config_path = PROJECT_ROOT / "context" / "brand_configs" / f"{brand_slug}.json"
    if not config_path.exists():
        raise FileNotFoundError(f"Brand config not found: {config_path}")

    with open(config_path) as f:
        config = json.load(f)

    # Load context docs for additional voice guidance
    context = {}
    for doc_path in config.get("context_docs", []):
        full_path = PROJECT_ROOT / doc_path
        if full_path.exists():
            with open(full_path) as f:
                context[doc_path] = f.read()

    config["_context"] = context
    return config


def load_brand_lexicon(brand_slug: str) -> Dict:
    """Load brand-specific lexicon."""
    lexicon_path = SKILL_DIR / "resources" / f"{brand_slug}_lexicon.json"

    # Fall back to generic lexicon if brand-specific doesn't exist
    if not lexicon_path.exists():
        lexicon_path = SKILL_DIR / "resources" / "[PROJECT_NAME]_lexicon.json"

    if not lexicon_path.exists():
        return {"required_terms": [], "preferred_phrases": []}

    with open(lexicon_path) as f:
        return json.load(f)


class BrandVoiceChecker:
    """Check content against brand voice guidelines."""

    def __init__(self, brand_config: Dict, lexicon: Dict):
        self.brand_config = brand_config
        self.lexicon = lexicon
        self.voice_config = brand_config.get("voice", {})

        # Parse tone attributes
        tone_str = self.voice_config.get("tone", "")
        self.tone_attributes = [t.strip().lower() for t in tone_str.split(",")]

        # Define tone keyword mappings
        self.tone_keywords = {
            "innovative": ["cutting-edge", "breakthrough", "revolutionary", "pioneering", "next-generation", "transform", "reimagine", "disrupt"],
            "precise": ["exact", "specific", "measurable", "quantified", "data-driven", "evidence-based", "proven", "validated"],
            "empowering": ["enable", "empower", "unlock", "achieve", "succeed", "capability", "potential", "strength"],
            "authoritative": ["expertise", "proven", "research shows", "data indicates", "industry-leading", "established"],
            "vitreous": ["transparent", "clear", "visible", "obvious", "evident", "straightforward"],
            "calm": ["confident", "assured", "steady", "reliable", "consistent", "stable"],
            "professional": ["excellence", "quality", "standard", "best practice", "industry", "enterprise"],
            "friendly": ["together", "partnership", "collaborate", "support", "help", "guide"]
        }

        # Formality indicators
        self.formality_markers = {
            "formal": ["hereby", "therefore", "furthermore", "pursuant", "regarding", "accordingly", "subsequently"],
            "casual": ["hey", "cool", "awesome", "stuff", "yeah", "gonna", "wanna", "kinda"]
        }

    def check_voice(self, text: str) -> Dict:
        """Analyze text for brand voice alignment."""
        text_lower = text.lower()
        words = text.split()
        word_count = len(words)

        results = {
            "word_count": word_count,
            "brand": self.brand_config.get("brand_name", "Unknown"),
            "voice_score": 0,
            "tone_analysis": {},
            "formality": {},
            "style_assessment": {},
            "recommendations": [],
            "passed": False
        }

        # Analyze tone alignment
        tone_scores = {}
        for attr in self.tone_attributes:
            if attr in self.tone_keywords:
                keywords = self.tone_keywords[attr]
                matches = sum(1 for kw in keywords if kw in text_lower)
                tone_scores[attr] = {
                    "matches": matches,
                    "keywords_found": [kw for kw in keywords if kw in text_lower],
                    "score": min(100, matches * 20)  # Each match adds 20 points, max 100
                }
            else:
                tone_scores[attr] = {"matches": 0, "keywords_found": [], "score": 0}

        results["tone_analysis"] = tone_scores

        # Calculate overall tone score
        if tone_scores:
            avg_tone_score = sum(t["score"] for t in tone_scores.values()) / len(tone_scores)
        else:
            avg_tone_score = 50  # Neutral if no tone defined

        # Analyze formality
        formal_count = sum(1 for marker in self.formality_markers["formal"] if marker in text_lower)
        casual_count = sum(1 for marker in self.formality_markers["casual"] if marker in text_lower)

        if casual_count > formal_count:
            formality_level = "casual"
            formality_score = 60 if "friendly" in self.tone_attributes else 40
        elif formal_count > casual_count:
            formality_level = "formal"
            formality_score = 80 if "authoritative" in self.tone_attributes else 70
        else:
            formality_level = "balanced"
            formality_score = 80

        results["formality"] = {
            "level": formality_level,
            "formal_markers": formal_count,
            "casual_markers": casual_count,
            "score": formality_score
        }

        # Analyze style
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        if sentences:
            sentence_lengths = [len(s.split()) for s in sentences]
            avg_length = sum(sentence_lengths) / len(sentence_lengths)
            length_variance = max(sentence_lengths) - min(sentence_lengths) if len(sentence_lengths) > 1 else 0

            # Good variety = higher score
            variety_score = min(100, 60 + length_variance * 3)

            # Check for question usage (engagement indicator)
            question_count = text.count("?")
            engagement_bonus = min(20, question_count * 10)

            results["style_assessment"] = {
                "avg_sentence_length": round(avg_length, 1),
                "sentence_count": len(sentences),
                "variety_score": variety_score,
                "questions_used": question_count,
                "engagement_bonus": engagement_bonus
            }

            style_score = variety_score + engagement_bonus
        else:
            style_score = 50
            results["style_assessment"] = {"error": "No sentences detected"}

        # Calculate readability (Flesch Reading Ease)
        readability = self._calculate_readability(text)
        results["readability"] = {
            "score": round(readability, 1),
            "level": self._readability_level(readability)
        }

        # Calculate overall voice score
        # Weights: Tone 40%, Formality 20%, Style 25%, Readability 15%
        overall_score = (
            avg_tone_score * 0.40 +
            formality_score * 0.20 +
            min(100, style_score) * 0.25 +
            readability * 0.15
        )

        results["voice_score"] = round(overall_score, 1)
        results["passed"] = overall_score >= 70

        # Generate recommendations
        results["recommendations"] = self._generate_recommendations(results)

        return results

    def _calculate_readability(self, text: str) -> float:
        """Calculate Flesch Reading Ease score."""
        sentences = re.split(r'[.!?]+', text)
        words = text.split()

        if not sentences or not words:
            return 50.0

        syllables = sum(self._count_syllables(word) for word in words)

        avg_sentence_length = len(words) / max(1, len([s for s in sentences if s.strip()]))
        avg_syllables_per_word = syllables / max(1, len(words))

        # Flesch Reading Ease formula
        score = 206.835 - 1.015 * avg_sentence_length - 84.6 * avg_syllables_per_word
        return max(0, min(100, score))

    def _count_syllables(self, word: str) -> int:
        """Count syllables in a word."""
        word = word.lower().strip(".,!?;:'\"")
        vowels = 'aeiou'
        syllable_count = 0
        previous_was_vowel = False

        for char in word:
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                syllable_count += 1
            previous_was_vowel = is_vowel

        if word.endswith('e') and syllable_count > 1:
            syllable_count -= 1

        return max(1, syllable_count)

    def _readability_level(self, score: float) -> str:
        """Convert readability score to level description."""
        if score >= 80:
            return "Easy (general audience)"
        elif score >= 60:
            return "Standard (business audience)"
        elif score >= 40:
            return "Moderately difficult (technical)"
        else:
            return "Difficult (specialized)"

    def _generate_recommendations(self, results: Dict) -> List[str]:
        """Generate actionable recommendations."""
        recs = []

        # Tone recommendations
        for attr, data in results.get("tone_analysis", {}).items():
            if data.get("score", 0) < 40:
                recs.append(f"Add more {attr} language (consider: {', '.join(self.tone_keywords.get(attr, [])[:3])})")

        # Formality recommendations
        formality = results.get("formality", {})
        if formality.get("casual_markers", 0) > 2:
            recs.append("Reduce casual language for more professional tone")

        # Style recommendations
        style = results.get("style_assessment", {})
        if style.get("variety_score", 100) < 70:
            recs.append("Vary sentence length for better readability")
        if style.get("questions_used", 0) == 0:
            recs.append("Consider adding a question to increase engagement")

        # Readability recommendations
        readability = results.get("readability", {}).get("score", 50)
        if readability < 40:
            recs.append("Simplify language - use shorter sentences and common words")
        elif readability > 80 and "authoritative" in self.tone_attributes:
            recs.append("Consider slightly more technical language for authority")

        # Overall score recommendations
        if results.get("voice_score", 0) < 70:
            recs.append("Review brand voice guidelines in context/brand_strategy.md")

        return recs


def main():
    parser = argparse.ArgumentParser(description="Check content against brand voice guidelines")
    parser.add_argument("file", help="Path to content file to check")
    parser.add_argument("--brand", "-b", default="[PROJECT_NAME]", help="Brand slug (default: [PROJECT_NAME])")
    parser.add_argument("--output", "-o", choices=["json", "text"], default="text", help="Output format")
    parser.add_argument("--verify", "-v", action="store_true", help="Strict mode - exit 1 if not passing")

    args = parser.parse_args()

    # Load content
    try:
        with open(args.file) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    # Load brand config and lexicon
    try:
        brand_config = load_brand_config(args.brand)
        lexicon = load_brand_lexicon(args.brand)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Run voice check
    checker = BrandVoiceChecker(brand_config, lexicon)
    results = checker.check_voice(content)

    # Output results
    if args.output == "json":
        print(json.dumps(results, indent=2))
    else:
        print(f"\n{'='*50}")
        print(f"BRAND VOICE CHECK: {results['brand']}")
        print(f"{'='*50}")
        print(f"\nFile: {args.file}")
        print(f"Word Count: {results['word_count']}")
        print(f"\nVOICE SCORE: {results['voice_score']}/100 {'PASS' if results['passed'] else 'NEEDS WORK'}")

        print(f"\n--- Tone Analysis ---")
        for attr, data in results.get("tone_analysis", {}).items():
            keywords = ", ".join(data.get("keywords_found", [])[:3]) or "none"
            print(f"  {attr.title()}: {data.get('score', 0)}/100 (found: {keywords})")

        print(f"\n--- Formality ---")
        formality = results.get("formality", {})
        print(f"  Level: {formality.get('level', 'unknown')}")
        print(f"  Score: {formality.get('score', 0)}/100")

        print(f"\n--- Style ---")
        style = results.get("style_assessment", {})
        print(f"  Avg sentence length: {style.get('avg_sentence_length', 0)} words")
        print(f"  Variety score: {style.get('variety_score', 0)}/100")
        print(f"  Questions used: {style.get('questions_used', 0)}")

        print(f"\n--- Readability ---")
        readability = results.get("readability", {})
        print(f"  Score: {readability.get('score', 0)}/100")
        print(f"  Level: {readability.get('level', 'unknown')}")

        if results.get("recommendations"):
            print(f"\n--- Recommendations ---")
            for rec in results["recommendations"]:
                print(f"  - {rec}")

        print()

    # Exit with error if verify mode and not passing
    if args.verify and not results["passed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
