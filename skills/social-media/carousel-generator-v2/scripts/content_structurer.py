"""
Content Structurer for Carousel Generator v2

AI-powered content intelligence that transforms topics into structured carousel slides.

Features:
- Topic research via PubMed MCP
- 4A Framework classification
- Smart slide structure generation
- Hook generation with patterns (via HooksGenerator)
"""

import os
import json
import re
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

from .models import (
    SlideContent, SlideType, ColorMode, ContentCategory,
    Carousel, CarouselConfig, TEMPLATE_PRESETS
)
from .hooks_generator import HooksGenerator, GeneratedHook

# Import content database for curated cardiology content
try:
    from .content_database import (
        get_content, get_myths_for_topic, get_statistics_for_topic,
        get_tips_for_topic, normalize_topic, TopicContent
    )
    CONTENT_DB_AVAILABLE = True
except ImportError:
    CONTENT_DB_AVAILABLE = False
    get_content = None
    get_myths_for_topic = lambda x, c=3: []
    get_statistics_for_topic = lambda x, c=3: []
    get_tips_for_topic = lambda x, c=5: []
    normalize_topic = lambda x: x


class ContentFramework(str, Enum):
    """4A Content Framework for categorization."""
    ACTIONABLE = "actionable"       # Practical tips, how-to
    ANALYTICAL = "analytical"       # Data-driven, research
    ASPIRATIONAL = "aspirational"   # Motivational, outcomes
    ANTHROPOLOGICAL = "anthropological"  # Stories, human experience


@dataclass
class ResearchResult:
    """Result from research phase."""
    topic: str
    key_points: List[str]
    statistics: List[Dict[str, str]]
    myths: List[Dict[str, str]]
    quotes: List[Dict[str, str]]
    steps: List[str]
    sources: List[str]
    pmids: List[str]


@dataclass
class ContentStructure:
    """Structured content ready for slide generation."""
    topic: str
    framework: ContentFramework
    template: str
    slides: List[SlideContent]
    research: Optional[ResearchResult] = None


class ContentStructurer:
    """
    Transform topics into structured carousel content.

    Uses AI to research topics, classify content, and generate
    optimal slide structures.
    """

    def __init__(self, use_ai: bool = True, api_key: str = None):
        """
        Initialize the content structurer.

        Args:
            use_ai: Whether to use AI for content generation
            api_key: OpenRouter/Anthropic API key (optional, uses env var)
        """
        self.use_ai = use_ai
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY") or os.getenv("ANTHROPIC_API_KEY")

        # Initialize hooks generator
        self.hooks_generator = HooksGenerator()

    def classify_content(self, topic: str, key_points: List[str] = None) -> ContentFramework:
        """
        Classify content into 4A Framework category.

        Args:
            topic: The content topic
            key_points: Optional list of key points to analyze

        Returns:
            ContentFramework category
        """
        # Keywords for classification
        actionable_keywords = ["how to", "tips", "ways to", "steps", "guide", "improve", "reduce", "increase"]
        analytical_keywords = ["data", "research", "study", "trial", "statistics", "evidence", "meta-analysis"]
        aspirational_keywords = ["success", "story", "journey", "achieved", "transformed", "possible"]
        anthropological_keywords = ["patient", "story", "experience", "case", "real", "learned"]

        topic_lower = topic.lower()
        points_text = " ".join(key_points or []).lower()
        full_text = f"{topic_lower} {points_text}"

        # Score each category
        scores = {
            ContentFramework.ACTIONABLE: sum(1 for kw in actionable_keywords if kw in full_text),
            ContentFramework.ANALYTICAL: sum(1 for kw in analytical_keywords if kw in full_text),
            ContentFramework.ASPIRATIONAL: sum(1 for kw in aspirational_keywords if kw in full_text),
            ContentFramework.ANTHROPOLOGICAL: sum(1 for kw in anthropological_keywords if kw in full_text),
        }

        # Return highest scoring category, default to actionable
        return max(scores, key=scores.get) if max(scores.values()) > 0 else ContentFramework.ACTIONABLE

    def select_template(self, framework: ContentFramework, topic: str) -> str:
        """
        Select optimal template based on content framework.

        Args:
            framework: The 4A category
            topic: The content topic

        Returns:
            Template name from TEMPLATE_PRESETS
        """
        topic_lower = topic.lower()

        # Check for specific patterns in topic
        if any(word in topic_lower for word in ["myth", "truth", "lie", "wrong"]):
            return "myth_busting"

        if any(word in topic_lower for word in ["story", "patient", "case", "journey"]):
            return "patient_story"

        if any(word in topic_lower for word in ["data", "trial", "study", "research", "statistics"]):
            return "data_driven"

        if any(word in topic_lower for word in ["how to", "steps", "guide", "process"]):
            return "how_to"

        # Default by framework
        framework_templates = {
            ContentFramework.ACTIONABLE: "tips_5",
            ContentFramework.ANALYTICAL: "data_driven",
            ContentFramework.ASPIRATIONAL: "patient_story",
            ContentFramework.ANTHROPOLOGICAL: "patient_story",
        }

        return framework_templates.get(framework, "tips_5")

    def generate_hook(self, topic: str, template: str) -> Tuple[str, str]:
        """
        Generate a compelling hook for the first slide.

        Uses the HooksGenerator for high-quality, scored hooks.

        Args:
            topic: The content topic
            template: The template being used

        Returns:
            Tuple of (title, subtitle)
        """
        # Use the hooks generator to get the best hook
        hook = self.hooks_generator.get_best_hook(topic, template)

        if hook:
            return hook.title, hook.subtitle

        # Fallback if generator fails
        return f"What you need to know about {topic}", "Evidence-based insights"

    def generate_hook_variations(self, topic: str, template: str, count: int = 3) -> List[GeneratedHook]:
        """
        Generate multiple hook variations for A/B testing.

        Args:
            topic: The content topic
            template: The template being used
            count: Number of variations to generate

        Returns:
            List of GeneratedHook objects with quality scores
        """
        return self.hooks_generator.generate(topic, template, count)

    def generate_ab_hooks(self, topic: str, template: str) -> Dict[str, GeneratedHook]:
        """
        Generate A/B test hook variations.

        Args:
            topic: The content topic
            template: The template being used

        Returns:
            Dict with 'A' (number-based) and 'B' (alternate) variations
        """
        return self.hooks_generator.generate_ab_variations(topic, template)

    def structure_from_topic(self, topic: str,
                            template: str = None,
                            research: ResearchResult = None) -> ContentStructure:
        """
        Structure a carousel from a topic.

        Args:
            topic: The content topic
            template: Optional template override
            research: Optional pre-fetched research

        Returns:
            ContentStructure ready for rendering
        """
        # Classify content
        framework = self.classify_content(topic)

        # Select template
        if not template:
            template = self.select_template(framework, topic)

        # Get template structure
        preset = TEMPLATE_PRESETS.get(template, TEMPLATE_PRESETS["tips_5"])
        slide_types = preset["slides"]

        # Generate hook
        hook_title, hook_subtitle = self.generate_hook(topic, template)

        # Get curated content from database if available
        db_content = get_content(topic) if CONTENT_DB_AVAILABLE else None
        db_myths = get_myths_for_topic(topic, count=10) if CONTENT_DB_AVAILABLE else []
        db_stats = get_statistics_for_topic(topic, count=10) if CONTENT_DB_AVAILABLE else []
        db_tips = get_tips_for_topic(topic, count=10) if CONTENT_DB_AVAILABLE else []

        # Normalize topic for cleaner text
        normalized_topic = normalize_topic(topic) if CONTENT_DB_AVAILABLE else topic

        # Track usage indices
        myth_index = 0
        stat_index = 0
        tip_index = 0

        # Build slides
        slides = []
        tip_counter = 1

        for i, slide_type in enumerate(slide_types, 1):
            slide = SlideContent(
                slide_type=slide_type,
                slide_number=i,
                color_mode=ColorMode.DARK if slide_type in [SlideType.HOOK, SlideType.QUOTE, SlideType.CTA] else ColorMode.LIGHT
            )

            if slide_type == SlideType.HOOK:
                slide.title = hook_title
                slide.subtitle = hook_subtitle

            elif slide_type == SlideType.TIPS:
                # Priority: research > database > placeholder
                if research and tip_counter <= len(research.key_points):
                    slide.title = f"Tip #{tip_counter}"
                    slide.bullet_points = [research.key_points[tip_counter - 1]]
                elif db_tips and tip_index < len(db_tips):
                    slide.title = f"Tip #{tip_counter}"
                    slide.bullet_points = [db_tips[tip_index]]
                    tip_index += 1
                else:
                    slide.title = f"Key Point #{tip_counter}"
                    slide.bullet_points = [f"Evidence-based insight about {normalized_topic}"]
                tip_counter += 1

            elif slide_type == SlideType.STATS:
                # Priority: research > database > placeholder
                if research and research.statistics:
                    stat = research.statistics[0]
                    slide.statistic = stat.get("value", "85%")
                    slide.stat_label = stat.get("label", "of patients benefit")
                    slide.stat_context = stat.get("context", "Based on clinical evidence")
                    slide.source = stat.get("source")
                elif db_stats and stat_index < len(db_stats):
                    stat = db_stats[stat_index]
                    slide.statistic = stat.get("value", "")
                    slide.stat_label = stat.get("label", "")
                    slide.stat_context = stat.get("context", "Based on clinical evidence")
                    slide.source = stat.get("source")
                    stat_index += 1
                else:
                    slide.statistic = "Evidence-based"
                    slide.stat_label = f"approach to {normalized_topic}"
                    slide.stat_context = "Clinical research supports this"

            elif slide_type == SlideType.MYTH:
                # Priority: research > database > placeholder
                if research and research.myths:
                    myth = research.myths[0]
                    slide.myth_text = myth.get("myth", f"Common misconception about {normalized_topic}")
                    slide.truth_text = myth.get("truth", "The evidence shows something different")
                    slide.source = myth.get("source")
                    research.myths.pop(0)  # Use next myth for next slide
                elif db_myths and myth_index < len(db_myths):
                    myth = db_myths[myth_index]
                    slide.myth_text = myth.get("myth", "")
                    slide.truth_text = myth.get("truth", "")
                    slide.source = myth.get("source")
                    myth_index += 1
                else:
                    slide.myth_text = f"Common misconception about {normalized_topic}"
                    slide.truth_text = "The scientific evidence tells a different story"

            elif slide_type == SlideType.QUOTE:
                # Priority: research > database > default
                if research and research.quotes:
                    quote = research.quotes[0]
                    slide.quote_text = quote.get("text", f"Important perspective on {normalized_topic}")
                    slide.quote_author = quote.get("author", "Expert Cardiologist")
                elif db_content and db_content.quotes:
                    quote = db_content.quotes[0]
                    slide.quote_text = quote.get("text", "")
                    slide.quote_author = quote.get("author", "Dr. Shailesh Singh, Cardiologist")
                else:
                    slide.quote_text = f"The evidence on {normalized_topic} is clear and compelling."
                    slide.quote_author = "Dr. Shailesh Singh, Cardiologist"

            elif slide_type == SlideType.STEPS:
                if research and research.steps:
                    slide.title = "How to Apply This"
                    slide.steps = research.steps[:3]  # Max 3 steps per slide
                elif db_tips and len(db_tips) >= 3:
                    slide.title = "Key Action Steps"
                    slide.steps = db_tips[:3]
                else:
                    slide.title = "How to Take Action"
                    slide.steps = [
                        f"Learn the facts about {normalized_topic}",
                        "Discuss with your cardiologist",
                        "Make evidence-based decisions"
                    ]

            elif slide_type == SlideType.COMPARISON:
                slide.title = "The Difference"
                slide.before_text = "Common approach that may not work"
                slide.after_text = "Evidence-based method that works"

            elif slide_type == SlideType.STORY:
                slide.title = "Real Impact"
                slide.body = f"Understanding {normalized_topic} has helped countless patients improve their heart health."

            elif slide_type == SlideType.DATA:
                # Priority: research > database > placeholder
                if research and research.statistics:
                    stat = research.statistics[0] if research.statistics else {}
                    slide.statistic = stat.get("value", "2.3x")
                    slide.stat_label = stat.get("label", "Risk reduction")
                    slide.stat_context = stat.get("context", "Based on meta-analysis")
                elif db_stats and stat_index < len(db_stats):
                    stat = db_stats[stat_index]
                    slide.statistic = stat.get("value", "")
                    slide.stat_label = stat.get("label", "")
                    slide.stat_context = stat.get("context", "Based on clinical evidence")
                    stat_index += 1
                else:
                    slide.statistic = "Significant"
                    slide.stat_label = f"improvement with {normalized_topic}"
                    slide.stat_context = "Based on clinical research"

            elif slide_type == SlideType.CTA:
                slide.cta_text = "Follow for more"
                slide.cta_handle = "@heartdocshailesh"

            slides.append(slide)

        return ContentStructure(
            topic=topic,
            framework=framework,
            template=template,
            slides=slides,
            research=research
        )

    def structure_from_longform(self, content: str,
                                content_type: str = "newsletter") -> ContentStructure:
        """
        Extract carousel structure from long-form content.

        Args:
            content: Long-form text (newsletter, blog, script)
            content_type: Type of content for appropriate parsing

        Returns:
            ContentStructure with extracted content
        """
        # Extract key points
        key_points = self._extract_key_points(content)

        # Extract statistics
        statistics = self._extract_statistics(content)

        # Determine topic from content
        topic = self._extract_topic(content)

        # Create research result
        research = ResearchResult(
            topic=topic,
            key_points=key_points,
            statistics=statistics,
            myths=[],
            quotes=[],
            steps=[],
            sources=[],
            pmids=[]
        )

        # Use tips template for extracted content
        return self.structure_from_topic(topic, template="tips_5", research=research)

    def _extract_key_points(self, content: str) -> List[str]:
        """Extract key points from content."""
        key_points = []

        # Look for bullet points
        bullet_pattern = r'[-•*]\s*(.+?)(?:\n|$)'
        bullets = re.findall(bullet_pattern, content)
        key_points.extend(bullets[:5])

        # Look for numbered lists
        number_pattern = r'\d+[.)]\s*(.+?)(?:\n|$)'
        numbered = re.findall(number_pattern, content)
        key_points.extend(numbered[:5])

        # If not enough, extract sentences with keywords
        if len(key_points) < 3:
            keywords = ["important", "key", "critical", "essential", "main", "primary"]
            sentences = content.split('.')
            for sentence in sentences:
                if any(kw in sentence.lower() for kw in keywords):
                    clean = sentence.strip()
                    if len(clean) > 20 and len(clean) < 200:
                        key_points.append(clean)

        return key_points[:5]

    def _extract_statistics(self, content: str) -> List[Dict[str, str]]:
        """Extract statistics from content."""
        statistics = []

        # Pattern for percentages
        pct_pattern = r'(\d+(?:\.\d+)?%)\s+(?:of\s+)?(.+?)(?:\.|,|;|\n)'
        for match in re.finditer(pct_pattern, content):
            statistics.append({
                "value": match.group(1),
                "label": match.group(2).strip()[:50],
                "context": "From clinical data"
            })

        # Pattern for ratios
        ratio_pattern = r'(\d+(?:\.\d+)?x)\s+(.+?)(?:\.|,|;|\n)'
        for match in re.finditer(ratio_pattern, content):
            statistics.append({
                "value": match.group(1),
                "label": match.group(2).strip()[:50],
                "context": "From research"
            })

        # Pattern for NNT/NNH
        nnt_pattern = r'NNT\s*(?:of\s*)?(\d+)'
        for match in re.finditer(nnt_pattern, content):
            statistics.append({
                "value": f"NNT {match.group(1)}",
                "label": "Number needed to treat",
                "context": "Clinical effectiveness"
            })

        return statistics[:3]

    def _extract_topic(self, content: str) -> str:
        """Extract main topic from content."""
        # Look for title patterns
        title_patterns = [
            r'^#\s+(.+?)$',  # Markdown H1
            r'^##\s+(.+?)$',  # Markdown H2
            r'<h1>(.+?)</h1>',  # HTML H1
            r'Title:\s*(.+?)(?:\n|$)',  # Explicit title
        ]

        for pattern in title_patterns:
            match = re.search(pattern, content, re.MULTILINE)
            if match:
                return match.group(1).strip()

        # Fall back to first line
        first_line = content.strip().split('\n')[0]
        return first_line[:100] if first_line else "Health Topic"


def structure_content(topic: str, template: str = None) -> ContentStructure:
    """
    Convenience function to structure content from a topic.

    Args:
        topic: The content topic
        template: Optional template override

    Returns:
        ContentStructure ready for rendering
    """
    structurer = ContentStructurer()
    return structurer.structure_from_topic(topic, template)


def structure_from_text(content: str, content_type: str = "newsletter") -> ContentStructure:
    """
    Convenience function to structure content from long-form text.

    Args:
        content: Long-form text
        content_type: Type of content

    Returns:
        ContentStructure ready for rendering
    """
    structurer = ContentStructurer()
    return structurer.structure_from_longform(content, content_type)
