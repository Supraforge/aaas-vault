"""
Quality Checker for Carousel Generator v2

Automated quality assurance for carousel slides:
- WCAG AA contrast checking
- Text density validation
- Anti-AI voice detection
- Brand consistency verification
"""

from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional
from dataclasses import dataclass
import re

from .models import SlideContent, Carousel
from .tokens import (
    get_quality_gates, get_color_rgb, calculate_contrast_ratio,
    check_wcag_aa, hex_to_rgb
)


@dataclass
class QualityCheckResult:
    """Result of a quality check."""
    passed: bool
    check_name: str
    message: str
    details: Optional[Dict[str, Any]] = None


class QualityChecker:
    """Run quality checks on carousel content and design."""

    def __init__(self):
        self.quality_gates = get_quality_gates()

        # Anti-AI detection patterns
        # Only flag clearly AI-generated phrases, not common educational language
        self.ai_phrases = [
            r"it's important to note",
            r"in conclusion",
            r"stands as a testament",
            r"plays a vital role",
            r"nestled in",  # Only flag "nestled in", not just "nestled"
            r"vibrant tapestry",
            r"delve into",
            r"embark on a journey",
            r"in the realm of",
            r"a testament to",
            r"at the end of the day",
            # Note: Removed "groundbreaking", "game-changing", "revolutionary"
            # as these are sometimes legitimate in medical content
            # Note: Removed "So," and "Well," as they're common in conversational content
        ]

        # Em dash overuse pattern - only flag excessive use
        self.em_dash_pattern = re.compile(r'—')

    def check_text_density(self, slide: SlideContent) -> QualityCheckResult:
        """Check if slide text density is within limits."""
        max_words = self.quality_gates['maxWordsPerSlide']
        word_count = slide.word_count

        passed = word_count <= max_words

        return QualityCheckResult(
            passed=passed,
            check_name="text_density",
            message=f"Word count: {word_count}/{max_words}",
            details={"word_count": word_count, "max_allowed": max_words}
        )

    def check_contrast(self, foreground_hex: str, background_hex: str,
                       is_large_text: bool = False) -> QualityCheckResult:
        """Check WCAG AA contrast compliance."""
        fg_rgb = hex_to_rgb(foreground_hex)
        bg_rgb = hex_to_rgb(background_hex)

        ratio = calculate_contrast_ratio(fg_rgb, bg_rgb)
        min_ratio = 3.0 if is_large_text else 4.5
        passed = ratio >= min_ratio

        return QualityCheckResult(
            passed=passed,
            check_name="contrast_ratio",
            message=f"Contrast: {ratio:.2f}:1 (min {min_ratio}:1)",
            details={
                "ratio": ratio,
                "min_required": min_ratio,
                "is_large_text": is_large_text
            }
        )

    def check_anti_ai(self, text: str) -> QualityCheckResult:
        """Check for AI-generated content patterns."""
        text_lower = text.lower()
        found_patterns = []

        for pattern in self.ai_phrases:
            if re.search(pattern, text_lower):
                found_patterns.append(pattern)

        # Check em dash usage - only flag excessive use
        # For carousel slides (short text), allow up to 2 em-dashes
        # For longer text (>200 chars), allow up to 3
        em_dashes = len(self.em_dash_pattern.findall(text))
        max_em_dashes = 3 if len(text) > 200 else 2
        if em_dashes > max_em_dashes:
            found_patterns.append(f"em_dash_overuse ({em_dashes} in {len(text)} chars)")

        passed = len(found_patterns) == 0

        return QualityCheckResult(
            passed=passed,
            check_name="anti_ai",
            message="No AI patterns" if passed else f"Found {len(found_patterns)} AI patterns",
            details={"patterns_found": found_patterns}
        )

    def check_slide_count(self, carousel: Carousel) -> QualityCheckResult:
        """Check if slide count is optimal."""
        min_slides = self.quality_gates['optimalSlideCount']['min']
        max_slides = self.quality_gates['optimalSlideCount']['max']
        count = len(carousel.slides)

        passed = min_slides <= count <= max_slides

        return QualityCheckResult(
            passed=passed,
            check_name="slide_count",
            message=f"Slide count: {count} (optimal: {min_slides}-{max_slides})",
            details={"count": count, "optimal_range": [min_slides, max_slides]}
        )

    def check_hook_quality(self, hook_slide: SlideContent) -> QualityCheckResult:
        """Check hook slide effectiveness."""
        issues = []

        # Check title exists and is compelling
        if not hook_slide.title:
            issues.append("Missing hook title")
        elif len(hook_slide.title) < 10:
            issues.append("Hook title too short")
        elif len(hook_slide.title) > 100:
            issues.append("Hook title too long")

        # Check for question or number (engaging hooks)
        title = hook_slide.title or ""
        has_question = "?" in title
        has_number = bool(re.search(r'\d', title))

        if not has_question and not has_number:
            issues.append("Consider adding a question or number for engagement")

        passed = len(issues) == 0

        return QualityCheckResult(
            passed=passed,
            check_name="hook_quality",
            message="Hook is effective" if passed else f"Issues: {', '.join(issues)}",
            details={"issues": issues, "has_question": has_question, "has_number": has_number}
        )

    def check_cta_presence(self, carousel: Carousel) -> QualityCheckResult:
        """Check if carousel ends with a CTA."""
        from .models import SlideType

        if not carousel.slides:
            return QualityCheckResult(
                passed=False,
                check_name="cta_presence",
                message="No slides in carousel"
            )

        last_slide = carousel.slides[-1]
        has_cta = last_slide.slide_type == SlideType.CTA

        return QualityCheckResult(
            passed=has_cta,
            check_name="cta_presence",
            message="Ends with CTA" if has_cta else "Missing CTA slide",
            details={"last_slide_type": last_slide.slide_type.value}
        )

    def check_source_citation(self, slide: SlideContent) -> QualityCheckResult:
        """Check if statistical slides have source citations."""
        from .models import SlideType

        # Only check stat slides - they MUST have sources
        if slide.slide_type != SlideType.STAT:
            return QualityCheckResult(
                passed=True,
                check_name="source_citation",
                message="N/A (not a stat slide)"
            )

        has_source = bool(slide.source_text and slide.source_text.strip())

        return QualityCheckResult(
            passed=has_source,
            check_name="source_citation",
            message="Has source" if has_source else "Missing source citation",
            details={"source": slide.source_text if has_source else None}
        )

    def check_slide_variety(self, carousel: Carousel) -> QualityCheckResult:
        """Check that carousel has variety in slide types."""
        from .models import SlideType

        if len(carousel.slides) < 3:
            return QualityCheckResult(
                passed=True,
                check_name="slide_variety",
                message="Too few slides to check variety"
            )

        slide_types = [s.slide_type for s in carousel.slides]
        unique_types = set(slide_types)

        # Should have at least 2-3 different types for good variety
        min_types = min(3, len(carousel.slides) // 2)
        has_variety = len(unique_types) >= min_types

        return QualityCheckResult(
            passed=has_variety,
            check_name="slide_variety",
            message=f"{len(unique_types)} slide types used",
            details={
                "types_used": [t.value for t in unique_types],
                "type_counts": {t.value: slide_types.count(t) for t in unique_types}
            }
        )

    def check_readability(self, text: str) -> QualityCheckResult:
        """Check text readability using simple metrics."""
        if not text or len(text) < 20:
            return QualityCheckResult(
                passed=True,
                check_name="readability",
                message="Text too short to analyze"
            )

        words = text.split()
        sentences = len(re.findall(r'[.!?]+', text)) or 1

        # Average words per sentence
        avg_sentence_length = len(words) / sentences

        # For carousel slides, sentences should be punchy (under 20 words avg)
        is_readable = avg_sentence_length <= 20

        # Check for overly complex words (3+ syllables rough estimate)
        complex_words = sum(1 for w in words if len(w) > 10)
        complex_ratio = complex_words / len(words) if words else 0

        passed = is_readable and complex_ratio < 0.15

        return QualityCheckResult(
            passed=passed,
            check_name="readability",
            message=f"Avg {avg_sentence_length:.1f} words/sentence",
            details={
                "avg_sentence_length": avg_sentence_length,
                "complex_word_ratio": complex_ratio,
                "total_words": len(words)
            }
        )

    def run_all_checks(self, carousel: Carousel) -> Dict[str, List[QualityCheckResult]]:
        """Run all quality checks on a carousel."""
        results = {
            "carousel": [],
            "slides": {}
        }

        # Carousel-level checks
        results["carousel"].append(self.check_slide_count(carousel))
        results["carousel"].append(self.check_cta_presence(carousel))
        results["carousel"].append(self.check_slide_variety(carousel))

        # Slide-level checks
        for slide in carousel.slides:
            slide_results = []

            # Text density
            slide_results.append(self.check_text_density(slide))

            # Anti-AI for text content
            all_text = " ".join(filter(None, [
                slide.title, slide.subtitle, slide.body,
                slide.quote_text, slide.myth_text, slide.truth_text
            ]))
            if all_text:
                slide_results.append(self.check_anti_ai(all_text))
                slide_results.append(self.check_readability(all_text))

            # Source citation for stat slides
            slide_results.append(self.check_source_citation(slide))

            # Hook quality for first slide
            from .models import SlideType
            if slide.slide_type == SlideType.HOOK:
                slide_results.append(self.check_hook_quality(slide))

            results["slides"][slide.slide_number] = slide_results

        return results

    def generate_report(self, results: Dict[str, List[QualityCheckResult]]) -> str:
        """Generate a human-readable quality report."""
        lines = ["=" * 50, "CAROUSEL QUALITY REPORT", "=" * 50, ""]

        # Carousel checks
        lines.append("CAROUSEL CHECKS:")
        for check in results["carousel"]:
            status = "[PASS]" if check.passed else "[FAIL]"
            lines.append(f"  {status} {check.check_name}: {check.message}")
        lines.append("")

        # Slide checks
        lines.append("SLIDE CHECKS:")
        for slide_num, checks in results["slides"].items():
            lines.append(f"\n  Slide {slide_num}:")
            for check in checks:
                status = "[PASS]" if check.passed else "[FAIL]"
                lines.append(f"    {status} {check.check_name}: {check.message}")

        # Summary
        all_checks = results["carousel"] + [c for checks in results["slides"].values() for c in checks]
        passed = sum(1 for c in all_checks if c.passed)
        total = len(all_checks)

        lines.extend([
            "", "=" * 50,
            f"SUMMARY: {passed}/{total} checks passed",
            "=" * 50
        ])

        return "\n".join(lines)
