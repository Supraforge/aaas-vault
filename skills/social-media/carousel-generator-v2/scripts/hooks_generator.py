"""
Hooks Generator for Carousel Generator v2

Generates high-converting hook slides using:
- Patterns from hook-patterns.md
- PubMed integration for topic-specific statistics
- A/B test variations
- Quality scoring
- Topic normalization to avoid awkward phrasing

Usage:
    from scripts.hooks_generator import HooksGenerator, generate_hooks

    generator = HooksGenerator()
    hooks = generator.generate(topic="statins", template="myth_busting", count=3)
"""

import os
import re
import random
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

# Import content database for topic normalization and curated hooks
try:
    from .content_database import get_content, normalize_topic, get_hooks_for_topic
except ImportError:
    # Fallback if imported directly
    get_content = None
    normalize_topic = lambda x: x
    get_hooks_for_topic = lambda x: []


class HookCategory(str, Enum):
    """Categories of hook patterns."""
    NUMBER = "number"
    QUESTION = "question"
    MYTH = "myth"
    FEAR = "fear"
    AUTHORITY = "authority"
    CONTRARIAN = "contrarian"


@dataclass
class HookPattern:
    """A single hook pattern template."""
    category: HookCategory
    template: str
    requires_number: bool = False
    requires_stat: bool = False

    def format(self, topic: str, n: int = 5, stat: str = None, normalized_topic: str = None) -> str:
        """Format the pattern with topic and optional number/stat.

        Args:
            topic: Original topic string
            n: Number for numbered lists
            stat: Optional statistic value
            normalized_topic: Pre-normalized topic (to avoid redundancy like "statin myths myths")
        """
        result = self.template

        # Use normalized topic if provided, otherwise use original
        topic_to_use = normalized_topic if normalized_topic else topic

        # Smart substitution - avoid redundancy
        # If pattern contains "myths" and topic contains "myths", remove from topic
        pattern_lower = self.template.lower()
        topic_lower = topic_to_use.lower()

        if "myths" in pattern_lower and "myth" in topic_lower:
            # Remove "myths" or "myth" from topic
            topic_to_use = re.sub(r'\s*myths?\s*', ' ', topic_to_use, flags=re.IGNORECASE).strip()
        if "tips" in pattern_lower and "tip" in topic_lower:
            topic_to_use = re.sub(r'\s*tips?\s*', ' ', topic_to_use, flags=re.IGNORECASE).strip()
        if "facts" in pattern_lower and "fact" in topic_lower:
            topic_to_use = re.sub(r'\s*facts?\s*', ' ', topic_to_use, flags=re.IGNORECASE).strip()

        result = result.replace("{topic}", topic_to_use)
        result = result.replace("{n}", str(n))
        if stat and "{stat}" in result:
            result = result.replace("{stat}", stat)

        # Clean up any double spaces
        result = re.sub(r'\s+', ' ', result).strip()

        return result


@dataclass
class GeneratedHook:
    """A generated hook with metadata."""
    title: str
    subtitle: str
    category: HookCategory
    quality_score: float  # 0-1
    has_number: bool
    has_question: bool
    has_authority: bool
    variation_id: str  # For A/B tracking


@dataclass
class TopicStats:
    """Statistics fetched for a topic."""
    topic: str
    stats: List[Dict[str, str]] = field(default_factory=list)
    pmids: List[str] = field(default_factory=list)
    source: str = "pubmed"


class HooksGenerator:
    """
    Generate high-converting hooks for carousels.

    Features:
    - Pattern-based generation from hook-patterns.md
    - PubMed integration for real statistics
    - A/B test variations
    - Quality scoring based on best practices
    """

    # Cardiology-specific topic shortcuts with stats
    TOPIC_STATS = {
        "statins": [
            {"value": "25%", "context": "reduction in major cardiovascular events"},
            {"value": "50%", "context": "of patients discontinue within 1 year"},
            {"value": "5-10%", "context": "experience muscle symptoms"},
        ],
        "ldl": [
            {"value": "22%", "context": "lower MACE per 1 mmol/L reduction"},
            {"value": "<70", "context": "mg/dL target for high-risk patients"},
            {"value": "50%", "context": "reduction target from baseline"},
        ],
        "glp-1": [
            {"value": "15%", "context": "average weight loss at 1 year"},
            {"value": "20%", "context": "reduction in cardiovascular events"},
            {"value": "14.9%", "context": "weight loss with semaglutide 2.4mg"},
        ],
        "blood pressure": [
            {"value": "120/80", "context": "new optimal target mmHg"},
            {"value": "47%", "context": "of adults have hypertension"},
            {"value": "25%", "context": "have resistant hypertension"},
        ],
        "heart attack": [
            {"value": "805,000", "context": "Americans have MI yearly"},
            {"value": "1 in 5", "context": "MIs are silent"},
            {"value": "50%", "context": "occur without prior symptoms"},
        ],
        "cac": [
            {"value": "0", "context": "score means <1% 10-year risk"},
            {"value": "10x", "context": "risk increase with score >400"},
            {"value": "50%", "context": "of heart attacks have zero CAC"},
        ],
    }

    # Best performing numbers (odd numbers outperform)
    BEST_NUMBERS = [3, 5, 7]

    def __init__(self, patterns_path: str = None):
        """
        Initialize the hooks generator.

        Args:
            patterns_path: Path to hook-patterns.md (auto-detected if not provided)
        """
        self.patterns_path = patterns_path or self._find_patterns_path()
        self.patterns = self._load_patterns()

    def _find_patterns_path(self) -> Path:
        """Find the hook-patterns.md file."""
        possible_paths = [
            Path(__file__).parent.parent / "references" / "hook-patterns.md",
            Path("references/hook-patterns.md"),
            Path("skills/cardiology/carousel-generator-v2/references/hook-patterns.md"),
        ]

        for path in possible_paths:
            if path.exists():
                return path

        return possible_paths[0]  # Default, may not exist

    def _load_patterns(self) -> Dict[HookCategory, List[HookPattern]]:
        """Load patterns from the patterns file and hardcoded defaults."""
        patterns = {cat: [] for cat in HookCategory}

        # Hardcoded patterns (always available)
        patterns[HookCategory.NUMBER] = [
            HookPattern(HookCategory.NUMBER, "{n} things about {topic} you didn't know", requires_number=True),
            HookPattern(HookCategory.NUMBER, "{n} {topic} myths that could hurt you", requires_number=True),
            HookPattern(HookCategory.NUMBER, "{n} signs your {topic} needs attention", requires_number=True),
            HookPattern(HookCategory.NUMBER, "{n} ways to improve your {topic}", requires_number=True),
            HookPattern(HookCategory.NUMBER, "{n} mistakes people make with {topic}", requires_number=True),
            HookPattern(HookCategory.NUMBER, "{n} {topic} facts that will surprise you", requires_number=True),
            HookPattern(HookCategory.NUMBER, "{n} reasons why {topic} matter more than you think", requires_number=True),
        ]

        patterns[HookCategory.QUESTION] = [
            HookPattern(HookCategory.QUESTION, "Is your {topic} putting you at risk?"),
            HookPattern(HookCategory.QUESTION, "What if everything you know about {topic} is wrong?"),
            HookPattern(HookCategory.QUESTION, "Are you making this {topic} mistake?"),
            HookPattern(HookCategory.QUESTION, "Why does {topic} matter more than you think?"),
            HookPattern(HookCategory.QUESTION, "Is your doctor wrong about {topic}?"),
            HookPattern(HookCategory.QUESTION, "Could your {topic} be a warning sign?"),
        ]

        patterns[HookCategory.MYTH] = [
            HookPattern(HookCategory.MYTH, "The truth about {topic}"),
            HookPattern(HookCategory.MYTH, "Stop believing this {topic} myth"),
            HookPattern(HookCategory.MYTH, "{topic} myths debunked"),
            HookPattern(HookCategory.MYTH, "What doctors won't tell you about {topic}"),
            HookPattern(HookCategory.MYTH, "The {topic} lie you've been told"),
            HookPattern(HookCategory.MYTH, "This {topic} myth could hurt you"),
        ]

        patterns[HookCategory.FEAR] = [
            HookPattern(HookCategory.FEAR, "Your {topic} could be killing you"),
            HookPattern(HookCategory.FEAR, "The silent {topic} danger you're ignoring"),
            HookPattern(HookCategory.FEAR, "Warning signs of {topic} problems"),
            HookPattern(HookCategory.FEAR, "Don't ignore these {topic} symptoms"),
            HookPattern(HookCategory.FEAR, "This {topic} mistake is dangerous"),
        ]

        patterns[HookCategory.AUTHORITY] = [
            HookPattern(HookCategory.AUTHORITY, "What cardiologists wish you knew about {topic}"),
            HookPattern(HookCategory.AUTHORITY, "As a cardiologist, I must warn you about {topic}"),
            HookPattern(HookCategory.AUTHORITY, "New research reveals surprising {topic} facts"),
            HookPattern(HookCategory.AUTHORITY, "The latest study on {topic} changes everything"),
            HookPattern(HookCategory.AUTHORITY, "What 20 years of cardiology taught me about {topic}"),
        ]

        patterns[HookCategory.CONTRARIAN] = [
            HookPattern(HookCategory.CONTRARIAN, "Why mainstream {topic} advice is wrong"),
            HookPattern(HookCategory.CONTRARIAN, "Everything you know about {topic} is outdated"),
            HookPattern(HookCategory.CONTRARIAN, "The {topic} advice you should ignore"),
            HookPattern(HookCategory.CONTRARIAN, "Why I disagree with {topic} guidelines"),
            HookPattern(HookCategory.CONTRARIAN, "The unpopular truth about {topic}"),
        ]

        return patterns

    def get_topic_stats(self, topic: str, use_pubmed: bool = False) -> TopicStats:
        """
        Get statistics for a topic.

        Args:
            topic: The topic to look up
            use_pubmed: Whether to fetch from PubMed (requires MCP)

        Returns:
            TopicStats with available statistics
        """
        topic_lower = topic.lower()

        # Check for exact or partial match in our stats database
        for key, stats in self.TOPIC_STATS.items():
            if key in topic_lower or topic_lower in key:
                return TopicStats(
                    topic=topic,
                    stats=[{"value": s["value"], "label": s["context"]} for s in stats],
                    source="built-in"
                )

        # PubMed integration - fetch real statistics
        if use_pubmed:
            try:
                # Import shared PubMed client
                import sys
                from pathlib import Path
                scripts_dir = Path(__file__).resolve().parents[4] / "scripts"
                if str(scripts_dir) not in sys.path:
                    sys.path.insert(0, str(scripts_dir))

                from pubmed_client import PubMedClient

                client = PubMedClient()
                # Search for recent articles on the topic
                articles = client.search_and_fetch(
                    f"{topic} cardiology clinical trial",
                    max_results=3,
                    sort="relevance"
                )

                if articles:
                    # Extract key statistics from abstracts
                    extracted_stats = []
                    for article in articles:
                        # Look for percentages and HR values
                        import re
                        abstract = article.abstract or ""

                        # Find percentage reductions
                        pct_matches = re.findall(r'(\d+(?:\.\d+)?%?\s*reduction)', abstract, re.I)
                        for match in pct_matches[:1]:
                            extracted_stats.append({
                                "value": match,
                                "label": f"From {article.journal}"
                            })

                        # Find hazard ratios
                        hr_matches = re.findall(r'HR\s*[=:]?\s*([\d.]+)', abstract, re.I)
                        for match in hr_matches[:1]:
                            extracted_stats.append({
                                "value": f"HR {match}",
                                "label": f"From {article.journal}"
                            })

                    if extracted_stats:
                        return TopicStats(
                            topic=topic,
                            stats=extracted_stats[:3],
                            source="pubmed"
                        )

            except Exception as e:
                # Fall through to return empty stats
                pass

        return TopicStats(topic=topic, stats=[], source="none")

    def _select_category_for_template(self, template: str) -> HookCategory:
        """Select the best hook category for a template."""
        category_map = {
            "myth_busting": HookCategory.MYTH,
            "data_driven": HookCategory.AUTHORITY,
            "tips_5": HookCategory.NUMBER,
            "how_to": HookCategory.NUMBER,
            "patient_story": HookCategory.AUTHORITY,
        }
        return category_map.get(template, HookCategory.NUMBER)

    def _calculate_quality_score(self, hook: str) -> Tuple[float, Dict[str, bool]]:
        """
        Calculate quality score for a hook.

        Based on hook-patterns.md quality checklist:
        - Has number (3, 5, 7, 10)
        - Has question mark
        - Has specific topic
        - Has curiosity gap
        - Has authority marker

        Returns:
            Tuple of (score 0-1, feature dict)
        """
        features = {
            "has_number": bool(re.search(r'\b[3571]\d?\b', hook)),
            "has_question": "?" in hook,
            "has_specific": not any(weak in hook.lower() for weak in [
                "things to know", "some advice", "check this out", "important information"
            ]),
            "has_curiosity_gap": any(gap in hook.lower() for gap in [
                "you didn't know", "won't tell", "is wrong", "could", "really",
                "surprise", "truth", "myth", "mistake", "secret"
            ]),
            "has_authority": any(auth in hook.lower() for auth in [
                "cardiologist", "doctor", "research", "study", "trial", "data"
            ]),
            "no_ai_patterns": not any(ai in hook.lower() for ai in [
                "in today's", "it's no secret", "more and more", "groundbreaking"
            ]),
        }

        # Score: each feature is worth points
        score = sum([
            0.2 if features["has_number"] else 0,
            0.15 if features["has_question"] else 0,
            0.2 if features["has_specific"] else 0,
            0.25 if features["has_curiosity_gap"] else 0,
            0.1 if features["has_authority"] else 0,
            0.1 if features["no_ai_patterns"] else 0,
        ])

        return score, features

    def _generate_subtitle(self, template: str, topic: str, stats: TopicStats = None) -> str:
        """Generate an appropriate subtitle for the hook."""
        # Template-specific subtitles
        subtitles = {
            "tips_5": [
                "Evidence-based insights",
                "What the research shows",
                "Based on clinical evidence",
                "From a cardiologist's perspective",
            ],
            "myth_busting": [
                "What the research really shows",
                "Debunked by science",
                "The evidence is clear",
                "Time to set the record straight",
            ],
            "data_driven": [
                "Based on clinical trials",
                "What the data reveals",
                "Evidence that matters",
                "Numbers don't lie",
            ],
            "patient_story": [
                "A real story of transformation",
                "Lessons from the clinic",
                "What I've seen in practice",
                "Real patients, real outcomes",
            ],
            "how_to": [
                "A step-by-step guide",
                "Your action plan",
                "How to get started",
                "The practical approach",
            ],
        }

        # If we have stats, consider incorporating them
        if stats and stats.stats:
            stat = stats.stats[0]
            stat_subtitle = f"{stat['value']} {stat['label']}"
            if len(stat_subtitle) < 40:
                return stat_subtitle

        return random.choice(subtitles.get(template, subtitles["tips_5"]))

    def generate(self, topic: str, template: str = "tips_5",
                 count: int = 3, use_pubmed: bool = False) -> List[GeneratedHook]:
        """
        Generate hook variations for a topic.

        Args:
            topic: The carousel topic
            template: Template name (affects hook style)
            count: Number of variations to generate
            use_pubmed: Whether to fetch PubMed stats

        Returns:
            List of GeneratedHook objects, sorted by quality score
        """
        hooks = []

        # Normalize the topic to avoid redundancy like "statin myths myths"
        normalized = normalize_topic(topic) if normalize_topic else topic

        # First, try to get curated hooks from content database
        curated_hooks = get_hooks_for_topic(topic) if get_hooks_for_topic else []
        if curated_hooks:
            # Use curated hooks - they're pre-written and high quality
            for i, curated_title in enumerate(curated_hooks[:count]):
                score, features = self._calculate_quality_score(curated_title)
                stats = self.get_topic_stats(topic, use_pubmed)
                hook = GeneratedHook(
                    title=curated_title,
                    subtitle=self._generate_subtitle(template, topic, stats),
                    category=HookCategory.AUTHORITY,  # Curated hooks are authoritative
                    quality_score=min(score + 0.15, 1.0),  # Boost for being curated
                    has_number=features["has_number"],
                    has_question=features["has_question"],
                    has_authority=features["has_authority"],
                    variation_id=f"{template}_curated_{i}"
                )
                hooks.append(hook)

            if len(hooks) >= count:
                return hooks[:count]

        # Get topic stats
        stats = self.get_topic_stats(topic, use_pubmed)

        # Select primary category based on template
        primary_category = self._select_category_for_template(template)

        # Get patterns from primary category + one alternate
        primary_patterns = self.patterns[primary_category]

        # Add some variety from other categories
        alternate_categories = [c for c in HookCategory if c != primary_category]
        alternate_category = random.choice(alternate_categories)
        alternate_patterns = self.patterns[alternate_category][:2]

        all_patterns = primary_patterns + alternate_patterns

        # Generate hooks
        used_patterns = set()

        while len(hooks) < count * 2:  # Generate extras to pick best ones
            pattern = random.choice(all_patterns)

            # Avoid duplicates
            if pattern.template in used_patterns and len(hooks) < count:
                continue
            used_patterns.add(pattern.template)

            # Generate the hook with normalized topic
            n = random.choice(self.BEST_NUMBERS)
            stat_value = stats.stats[0]["value"] if stats.stats else None

            title = pattern.format(topic=topic, n=n, stat=stat_value, normalized_topic=normalized)
            title = title.strip()

            # Capitalize first letter properly
            if title:
                title = title[0].upper() + title[1:]

            # Generate subtitle
            subtitle = self._generate_subtitle(template, topic, stats)

            # Calculate quality
            score, features = self._calculate_quality_score(title)

            # Create hook object
            hook = GeneratedHook(
                title=title,
                subtitle=subtitle,
                category=pattern.category,
                quality_score=score,
                has_number=features["has_number"],
                has_question=features["has_question"],
                has_authority=features["has_authority"],
                variation_id=f"{template}_{pattern.category.value}_{len(hooks)}"
            )

            hooks.append(hook)

            if len(hooks) >= count * 2:
                break

        # Sort by quality and return top ones
        hooks.sort(key=lambda h: h.quality_score, reverse=True)
        return hooks[:count]

    def generate_ab_variations(self, topic: str, template: str = "tips_5") -> Dict[str, GeneratedHook]:
        """
        Generate A/B test variations for a topic.

        Returns exactly 2 hooks optimized for different engagement styles:
        - Variation A: Number-based (proven performer)
        - Variation B: Question or authority-based (engagement driver)

        Args:
            topic: The carousel topic
            template: Template name

        Returns:
            Dict with 'A' and 'B' variations
        """
        # Generate A: Number-based hook
        number_patterns = self.patterns[HookCategory.NUMBER]
        pattern_a = random.choice(number_patterns)
        n = random.choice(self.BEST_NUMBERS)

        stats = self.get_topic_stats(topic)

        title_a = pattern_a.format(topic=topic, n=n)
        title_a = title_a.strip().capitalize()
        score_a, features_a = self._calculate_quality_score(title_a)

        hook_a = GeneratedHook(
            title=title_a,
            subtitle=self._generate_subtitle(template, topic, stats),
            category=HookCategory.NUMBER,
            quality_score=score_a,
            has_number=features_a["has_number"],
            has_question=features_a["has_question"],
            has_authority=features_a["has_authority"],
            variation_id=f"{template}_A_number"
        )

        # Generate B: Question or authority-based
        alt_category = random.choice([HookCategory.QUESTION, HookCategory.AUTHORITY])
        alt_patterns = self.patterns[alt_category]
        pattern_b = random.choice(alt_patterns)

        title_b = pattern_b.format(topic=topic, n=n)
        title_b = title_b.strip().capitalize()
        score_b, features_b = self._calculate_quality_score(title_b)

        hook_b = GeneratedHook(
            title=title_b,
            subtitle=self._generate_subtitle(template, topic, stats),
            category=alt_category,
            quality_score=score_b,
            has_number=features_b["has_number"],
            has_question=features_b["has_question"],
            has_authority=features_b["has_authority"],
            variation_id=f"{template}_B_{alt_category.value}"
        )

        return {"A": hook_a, "B": hook_b}

    def get_best_hook(self, topic: str, template: str = "tips_5") -> GeneratedHook:
        """
        Get the single best hook for a topic.

        Args:
            topic: The carousel topic
            template: Template name

        Returns:
            The highest-scoring GeneratedHook
        """
        hooks = self.generate(topic, template, count=5)
        return hooks[0] if hooks else None


def generate_hooks(topic: str, template: str = "tips_5", count: int = 3) -> List[GeneratedHook]:
    """
    Convenience function to generate hooks.

    Args:
        topic: The carousel topic
        template: Template name
        count: Number of variations

    Returns:
        List of GeneratedHook objects
    """
    generator = HooksGenerator()
    return generator.generate(topic, template, count)


def generate_ab_hooks(topic: str, template: str = "tips_5") -> Dict[str, GeneratedHook]:
    """
    Convenience function for A/B variations.

    Args:
        topic: The carousel topic
        template: Template name

    Returns:
        Dict with 'A' and 'B' variations
    """
    generator = HooksGenerator()
    return generator.generate_ab_variations(topic, template)


# CLI for testing
if __name__ == "__main__":
    import sys

    topic = sys.argv[1] if len(sys.argv) > 1 else "statins"
    template = sys.argv[2] if len(sys.argv) > 2 else "myth_busting"

    print(f"\n🎣 Generating hooks for: {topic}")
    print(f"📋 Template: {template}\n")

    generator = HooksGenerator()

    # Generate multiple variations
    hooks = generator.generate(topic, template, count=5)

    print("=" * 60)
    print("TOP 5 HOOK VARIATIONS (sorted by quality)")
    print("=" * 60)

    for i, hook in enumerate(hooks, 1):
        print(f"\n{i}. [{hook.quality_score:.0%}] {hook.title}")
        print(f"   Subtitle: {hook.subtitle}")
        print(f"   Category: {hook.category.value}")
        features = []
        if hook.has_number:
            features.append("📊 number")
        if hook.has_question:
            features.append("❓ question")
        if hook.has_authority:
            features.append("🩺 authority")
        print(f"   Features: {', '.join(features) if features else 'none'}")

    print("\n" + "=" * 60)
    print("A/B TEST VARIATIONS")
    print("=" * 60)

    ab = generator.generate_ab_variations(topic, template)

    print(f"\n🅰️  Variation A (Number-based):")
    print(f"   {ab['A'].title}")
    print(f"   Quality: {ab['A'].quality_score:.0%}")

    print(f"\n🅱️  Variation B ({ab['B'].category.value}):")
    print(f"   {ab['B'].title}")
    print(f"   Quality: {ab['B'].quality_score:.0%}")

    print("\n✅ Hook generation complete!")
