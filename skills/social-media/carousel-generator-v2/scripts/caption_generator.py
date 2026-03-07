"""
Caption and Hashtag Generator for Carousel Generator v2

Generates Instagram-optimized captions and hashtags for carousel posts.
Uses AI to create engaging captions based on slide content.

Usage:
    from caption_generator import CaptionGenerator

    generator = CaptionGenerator()
    caption = generator.generate_caption(slides, topic)
    hashtags = generator.generate_hashtags(topic)
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

# Import models
try:
    from .models import SlideContent, SlideType
except ImportError:
    from models import SlideContent, SlideType


@dataclass
class CaptionResult:
    """Result of caption generation."""
    caption: str
    hook: str
    body: str
    cta: str
    alt_texts: List[str]
    hashtags: List[str]


class CaptionGenerator:
    """Generates captions and hashtags for Instagram carousels."""

    # Cardiology-specific hashtags
    CARDIOLOGY_HASHTAGS = [
        "#cardiology", "#heartdoctor", "#hearthealth", "#cardiologist",
        "#heartdisease", "#cardiovascularhealth", "#cardio", "#heartcare"
    ]

    # Topic-specific hashtags
    TOPIC_HASHTAGS = {
        "statins": ["#statins", "#cholesterol", "#LDL", "#lipids", "#heartattackprevention"],
        "cholesterol": ["#cholesterol", "#LDL", "#HDL", "#lipidprofile", "#dyslipidemia"],
        "blood pressure": ["#bloodpressure", "#hypertension", "#bpcontrol", "#highbloodpressure"],
        "hypertension": ["#hypertension", "#bloodpressure", "#bpmanagement", "#htn"],
        "heart failure": ["#heartfailure", "#HFrEF", "#HFpEF", "#cardiomyopathy", "#CHF"],
        "afib": ["#afib", "#atrialfibrillation", "#arrhythmia", "#strokeprevention"],
        "diabetes": ["#diabetes", "#diabetesawareness", "#type2diabetes", "#glucosecontrol"],
        "sglt2": ["#SGLT2", "#SGLT2inhibitors", "#dapagliflozin", "#empagliflozin"],
        "glp1": ["#GLP1", "#semaglutide", "#tirzepatide", "#weightloss", "#obesity"],
        "cac": ["#CAC", "#coronarycalcium", "#calciumscore", "#heartscreening"],
    }

    # General medical education hashtags
    EDUCATION_HASHTAGS = [
        "#medicaleducation", "#medicalfacts", "#healthtips", "#healthawareness",
        "#doctorlife", "#medicalmyths", "#evidencebasedmedicine"
    ]

    # Engagement hashtags
    ENGAGEMENT_HASHTAGS = [
        "#medtwitter", "#medicalcommunity", "#healthcommunity",
        "#learnmedicine", "#medstudent"
    ]

    def __init__(self, use_ai: bool = True):
        """
        Initialize caption generator.

        Args:
            use_ai: Whether to use AI for caption generation (requires API key)
        """
        self.use_ai = use_ai
        self._init_client()

    def _init_client(self):
        """Initialize AI client if available."""
        self.client = None
        if self.use_ai:
            try:
                import anthropic
                api_key = os.getenv("ANTHROPIC_API_KEY")
                if api_key:
                    self.client = anthropic.Anthropic(api_key=api_key)
            except ImportError:
                pass

    def generate_caption(self, slides: List[SlideContent], topic: str,
                        style: str = "educational") -> CaptionResult:
        """
        Generate Instagram caption for carousel.

        Args:
            slides: List of slide content
            topic: Main topic of the carousel
            style: Caption style (educational, myth_busting, tips, story)

        Returns:
            CaptionResult with caption, alt_texts, and hashtags
        """
        # Extract content from slides
        content_summary = self._extract_content_summary(slides)

        # Generate caption
        if self.client and self.use_ai:
            caption_parts = self._generate_ai_caption(slides, topic, style, content_summary)
        else:
            caption_parts = self._generate_template_caption(slides, topic, style, content_summary)

        # Generate alt texts
        alt_texts = self._generate_alt_texts(slides)

        # Generate hashtags
        hashtags = self.generate_hashtags(topic, len(slides))

        # Combine caption parts
        full_caption = f"{caption_parts['hook']}\n\n{caption_parts['body']}\n\n{caption_parts['cta']}"

        return CaptionResult(
            caption=full_caption,
            hook=caption_parts['hook'],
            body=caption_parts['body'],
            cta=caption_parts['cta'],
            alt_texts=alt_texts,
            hashtags=hashtags
        )

    def _extract_content_summary(self, slides: List[SlideContent]) -> Dict[str, Any]:
        """Extract key content from slides for caption generation."""
        summary = {
            "slide_count": len(slides),
            "slide_types": [],
            "key_points": [],
            "myths": [],
            "statistics": [],
            "tips": []
        }

        for slide in slides:
            summary["slide_types"].append(slide.slide_type.value if hasattr(slide.slide_type, 'value') else str(slide.slide_type))

            if slide.slide_type == SlideType.MYTH:
                if hasattr(slide, 'myth') and slide.myth:
                    summary["myths"].append({
                        "myth": slide.myth,
                        "truth": getattr(slide, 'truth', '')
                    })
            elif slide.slide_type == SlideType.STATS:
                if hasattr(slide, 'stat_value') and slide.stat_value:
                    summary["statistics"].append({
                        "value": slide.stat_value,
                        "label": getattr(slide, 'stat_label', '')
                    })
            elif slide.slide_type == SlideType.TIPS:
                if hasattr(slide, 'bullet_points') and slide.bullet_points:
                    summary["tips"].extend(slide.bullet_points[:3])

            if slide.title:
                summary["key_points"].append(slide.title)

        return summary

    def _generate_ai_caption(self, slides: List[SlideContent], topic: str,
                            style: str, content: Dict[str, Any]) -> Dict[str, str]:
        """Generate caption using AI."""

        prompt = f"""Generate an Instagram carousel caption for a cardiology educational post.

TOPIC: {topic}
STYLE: {style}
SLIDES: {content['slide_count']} slides

CONTENT SUMMARY:
- Slide types: {', '.join(content['slide_types'][:5])}
- Key points: {'; '.join(content['key_points'][:5])}
- Myths addressed: {len(content['myths'])}
- Statistics shown: {len(content['statistics'])}
- Tips shared: {len(content['tips'])}

REQUIREMENTS:
1. HOOK (first line): Start with a scroll-stopping question or bold statement
2. BODY (2-4 short paragraphs): Summarize the key takeaways, use line breaks
3. CTA (call to action): End with "Save this 📌" or "Follow @heartdocshailesh for more"

STYLE GUIDELINES:
- Write like Dr. Eric Topol (authoritative but accessible)
- Use emojis sparingly (1-2 per paragraph max)
- Keep it educational, not promotional
- Mention specific data/statistics if available
- Avoid AI-sounding phrases ("It's important to note", "In conclusion")
- Max 2,200 characters total

Return as JSON:
{{
    "hook": "...",
    "body": "...",
    "cta": "..."
}}
"""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )

            text = response.content[0].text
            # Extract JSON
            start = text.find('{')
            end = text.rfind('}') + 1
            if start != -1 and end > start:
                return json.loads(text[start:end])
        except Exception as e:
            pass

        # Fallback to template
        return self._generate_template_caption(slides, topic, style, content)

    def _generate_template_caption(self, slides: List[SlideContent], topic: str,
                                  style: str, content: Dict[str, Any]) -> Dict[str, str]:
        """Generate caption using templates."""

        # Hook templates
        hook_templates = {
            "myth_busting": [
                f"🚨 {len(content['myths'])} {topic} myths that could be hurting your heart →",
                f"Stop believing these {topic} myths 🛑",
                f"What your doctor wishes you knew about {topic} 👇",
            ],
            "tips": [
                f"🫀 {len(content['tips'])} evidence-based {topic} tips →",
                f"Your cardiologist's guide to {topic} 📋",
                f"How to actually improve your {topic.replace('heart', 'heart health')} →",
            ],
            "educational": [
                f"🔬 The science of {topic} explained →",
                f"What the latest research says about {topic} 📊",
                f"Understanding {topic}: A cardiologist's perspective →",
            ],
            "story": [
                f"This changed how I think about {topic} 💭",
                f"A patient asked me about {topic}... here's what I said →",
                f"The truth about {topic} that nobody talks about 🎯",
            ]
        }

        hooks = hook_templates.get(style, hook_templates["educational"])
        hook = hooks[0]  # Use first template

        # Generate body
        body_parts = []

        if content['myths']:
            myth = content['myths'][0]
            body_parts.append(f"Myth: \"{myth.get('myth', '')}\"")
            body_parts.append(f"Truth: {myth.get('truth', '')}")

        if content['statistics']:
            stat = content['statistics'][0]
            body_parts.append(f"📊 Key stat: {stat.get('value', '')} - {stat.get('label', '')}")

        if content['tips']:
            body_parts.append("Key takeaways:")
            for tip in content['tips'][:3]:
                body_parts.append(f"• {tip}")

        if not body_parts:
            body_parts.append(f"Swipe through to learn the evidence-based facts about {topic}.")
            body_parts.append(f"This carousel covers {content['slide_count']} key points every patient should know.")

        body = "\n\n".join(body_parts)

        # CTA
        cta = "💾 Save this for later\n👉 Follow @heartdocshailesh for more evidence-based cardiology"

        return {
            "hook": hook,
            "body": body,
            "cta": cta
        }

    def _generate_alt_texts(self, slides: List[SlideContent]) -> List[str]:
        """Generate alt text for each slide for accessibility."""
        alt_texts = []

        for i, slide in enumerate(slides, 1):
            slide_type = slide.slide_type.value if hasattr(slide.slide_type, 'value') else str(slide.slide_type)

            if slide.slide_type == SlideType.HOOK:
                alt = f"Slide {i}: Hook slide with title '{slide.title or 'Topic introduction'}'"
            elif slide.slide_type == SlideType.MYTH:
                myth = getattr(slide, 'myth', slide.title or 'a common myth')
                alt = f"Slide {i}: Myth-busting slide addressing '{myth[:50]}'"
            elif slide.slide_type == SlideType.STATS:
                stat = getattr(slide, 'stat_value', '')
                label = getattr(slide, 'stat_label', '')
                alt = f"Slide {i}: Statistics slide showing {stat} {label}"
            elif slide.slide_type == SlideType.TIPS:
                tip_count = len(getattr(slide, 'bullet_points', [])) or "several"
                alt = f"Slide {i}: Tips slide with {tip_count} actionable recommendations"
            elif slide.slide_type == SlideType.CTA:
                alt = f"Slide {i}: Call to action - follow for more content"
            else:
                alt = f"Slide {i}: {slide_type} slide about {slide.title or 'the topic'}"

            alt_texts.append(alt)

        return alt_texts

    def generate_hashtags(self, topic: str, slide_count: int = 8) -> List[str]:
        """
        Generate optimized hashtags for the carousel.

        Args:
            topic: Main topic
            slide_count: Number of slides

        Returns:
            List of 15-20 hashtags
        """
        hashtags = []

        # Add core cardiology hashtags (3-4)
        hashtags.extend(self.CARDIOLOGY_HASHTAGS[:4])

        # Add topic-specific hashtags (3-5)
        topic_lower = topic.lower()
        for key, tags in self.TOPIC_HASHTAGS.items():
            if key in topic_lower:
                hashtags.extend(tags[:4])
                break

        # Add education hashtags (3-4)
        hashtags.extend(self.EDUCATION_HASHTAGS[:4])

        # Add engagement hashtags (2-3)
        hashtags.extend(self.ENGAGEMENT_HASHTAGS[:3])

        # Add branded hashtag
        hashtags.append("#heartdocshailesh")

        # Remove duplicates and limit to 20
        seen = set()
        unique_hashtags = []
        for tag in hashtags:
            if tag.lower() not in seen:
                seen.add(tag.lower())
                unique_hashtags.append(tag)

        return unique_hashtags[:20]

    def format_for_instagram(self, result: CaptionResult) -> str:
        """
        Format caption with hashtags for Instagram posting.

        Args:
            result: CaptionResult from generate_caption

        Returns:
            Ready-to-paste Instagram caption
        """
        # Main caption
        output = result.caption

        # Add spacing before hashtags
        output += "\n\n.\n.\n.\n"

        # Add hashtags
        output += " ".join(result.hashtags)

        return output


def generate_caption_for_carousel(slides: List[SlideContent], topic: str,
                                 style: str = "educational") -> CaptionResult:
    """
    Convenience function to generate caption.

    Args:
        slides: List of slide content
        topic: Main topic
        style: Caption style

    Returns:
        CaptionResult
    """
    generator = CaptionGenerator()
    return generator.generate_caption(slides, topic, style)


if __name__ == "__main__":
    # Test with sample data
    from models import SlideContent, SlideType

    slides = [
        SlideContent(slide_type=SlideType.HOOK, title="5 Statin Myths Exposed"),
        SlideContent(slide_type=SlideType.MYTH, title="Myth 1", myth="Statins cause muscle pain in everyone", truth="Only 5-10% experience muscle symptoms"),
        SlideContent(slide_type=SlideType.MYTH, title="Myth 2", myth="Statins damage your liver", truth="Serious liver problems are extremely rare"),
        SlideContent(slide_type=SlideType.STATS, title="The Evidence", stat_value="25%", stat_label="mortality reduction in high-risk patients"),
        SlideContent(slide_type=SlideType.CTA, title="Follow for more", cta_text="Follow @heartdocshailesh"),
    ]

    generator = CaptionGenerator(use_ai=False)
    result = generator.generate_caption(slides, "statins", "myth_busting")

    print("=" * 60)
    print("CAPTION:")
    print("=" * 60)
    print(result.caption)
    print("\n" + "=" * 60)
    print("HASHTAGS:")
    print("=" * 60)
    print(" ".join(result.hashtags))
    print("\n" + "=" * 60)
    print("ALT TEXTS:")
    print("=" * 60)
    for alt in result.alt_texts:
        print(f"  - {alt}")
