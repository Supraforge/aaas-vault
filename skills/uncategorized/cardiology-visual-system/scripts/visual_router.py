#!/usr/bin/env python3
"""
Unified Visual Content Router

Intelligently routes visual content requests to the optimal tool:
- AntV Infographic: Template-driven infographics (200+ templates)
- Gemini: AI-generated infographics and medical illustrations
- Fal.ai: Stock/human imagery, lifestyle photos
- Mermaid: Flowcharts, treatment algorithms, clinical pathways
- Plotly: Data visualization, charts, trial results
- Marp: Slide decks and presentations
"""

import re
import sys
from pathlib import Path
from typing import Dict, Optional, Tuple


class VisualRouter:
    """
    Intelligent router for visual content generation.

    Analyzes request text and routes to the optimal tool based on content type,
    keywords, and complexity.
    """

    def __init__(self):
        """Initialize router with keyword patterns for each tool."""

        # AntV Infographic - Template-driven infographics
        self.antv_keywords = [
            'template infographic', 'structured infographic', 'step-by-step infographic',
            'trial timeline', 'mechanism steps', 'treatment pathway infographic',
            'dosing schedule', 'guideline summary', 'risk stratification infographic',
            'template-based', 'declarative infographic'
        ]

        # Gemini - AI-generated infographics
        self.gemini_keywords = [
            'infographic', 'explainer', 'illustration', 'visual summary',
            'concept diagram', 'icons', 'steps', 'process visual',
            'simplified', 'educational graphic', 'medical illustration'
        ]

        # Fal.ai - Stock/human imagery
        self.fal_keywords = [
            'blog image', 'header', 'hero image', 'lifestyle', 'patient photo',
            'stock', 'person', 'family', 'emotional', 'scenario', 'recovery',
            'hope imagery', 'human-centered'
        ]

        # Mermaid - Diagrams and flowcharts
        self.mermaid_keywords = [
            'flowchart', 'algorithm', 'pathway', 'decision tree', 'sequence',
            'timeline', 'process flow', 'treatment algorithm', 'diagnostic pathway',
            'workflow', 'clinical pathway', 'gantt'
        ]

        # Plotly - Data visualization (static)
        self.plotly_keywords = [
            'chart', 'graph', 'plot', 'data', 'statistics', 'trial results',
            'forest plot', 'trends', 'comparison', 'survival curve',
            'kaplan-meier', 'bar chart', 'line graph', 'scatter'
        ]

        # Vizzu - Animated data visualizations (NEW)
        self.vizzu_keywords = [
            'animated data', 'animated chart', 'animated graph', 'animated plot',
            'animated forest plot', 'animated survival curve', 'animated kaplan-meier',
            'chart transition', 'morphing chart', 'animated bar', 'animated line',
            'animated enrollment', 'animated trial', 'data animation', 'animated trend',
            'animated comparison', 'animated meta-analysis'
        ]

        # Marp - Presentations
        self.marp_keywords = [
            'slides', 'presentation', 'deck', 'powerpoint', 'lecture',
            'talk', 'keynote', 'conference', 'educational slides'
        ]

    def analyze_request(self, request: str) -> Tuple[str, float, Dict]:
        """
        Analyze request and determine best tool.

        Args:
            request: User request text

        Returns:
            Tuple of (tool_name, confidence, metadata)
        """
        request_lower = request.lower()

        # Calculate scores for each tool
        scores = {
            'antv': self._score_keywords(request_lower, self.antv_keywords),
            'gemini': self._score_keywords(request_lower, self.gemini_keywords),
            'fal': self._score_keywords(request_lower, self.fal_keywords),
            'mermaid': self._score_keywords(request_lower, self.mermaid_keywords),
            'plotly': self._score_keywords(request_lower, self.plotly_keywords),
            'vizzu': self._score_keywords(request_lower, self.vizzu_keywords),
            'marp': self._score_keywords(request_lower, self.marp_keywords),
        }

        # Apply priority rules

        # If specifically requests animation, STRONGLY favor Vizzu
        if any(kw in request_lower for kw in ['animated', 'animation', 'transition', 'morphing']):
            scores['vizzu'] *= 3.0

        # If specifically requests template/structured infographic, strongly favor AntV
        if any(kw in request_lower for kw in ['template', 'structured', 'declarative']):
            scores['antv'] *= 2.0

        # If requests data/numbers/statistics WITHOUT animation, favor Plotly
        if any(kw in request_lower for kw in ['data', 'chart', 'statistics', 'trial results']):
            if 'animated' not in request_lower and 'animation' not in request_lower:
                scores['plotly'] *= 1.5

        # If requests flowchart/algorithm, favor Mermaid
        if any(kw in request_lower for kw in ['flowchart', 'algorithm', 'decision tree']):
            scores['mermaid'] *= 1.5

        # If requests human/lifestyle imagery, favor Fal
        if any(kw in request_lower for kw in ['patient', 'person', 'lifestyle', 'photo']):
            scores['fal'] *= 1.5

        # Find best match
        best_tool = max(scores, key=scores.get)
        best_score = scores[best_tool]

        # If score is too low, default to Gemini (most versatile)
        if best_score < 1.0:
            best_tool = 'gemini'
            best_score = 1.0

        # Normalize confidence to 0-1 scale
        confidence = min(best_score / 3.0, 1.0)

        # Build metadata
        metadata = {
            'all_scores': scores,
            'keywords_found': self._find_keywords(request_lower),
            'reasoning': self._explain_choice(best_tool, request_lower)
        }

        return best_tool, confidence, metadata

    def _score_keywords(self, text: str, keywords: list) -> float:
        """Score text based on keyword matches."""
        score = 0.0
        for keyword in keywords:
            if keyword in text:
                score += 1.0
        return score

    def _find_keywords(self, text: str) -> Dict[str, list]:
        """Find which keywords matched for each tool."""
        found = {}

        for tool_name, keywords in [
            ('antv', self.antv_keywords),
            ('gemini', self.gemini_keywords),
            ('fal', self.fal_keywords),
            ('mermaid', self.mermaid_keywords),
            ('plotly', self.plotly_keywords),
            ('vizzu', self.vizzu_keywords),
            ('marp', self.marp_keywords),
        ]:
            found[tool_name] = [kw for kw in keywords if kw in text]

        return found

    def _explain_choice(self, tool: str, text: str) -> str:
        """Explain why this tool was chosen."""
        explanations = {
            'antv': 'Template-driven infographic with structured data layout',
            'gemini': 'AI-generated custom infographic or medical illustration',
            'fal': 'Human/lifestyle imagery for emotional storytelling',
            'mermaid': 'Structured diagram or flowchart for clinical pathways',
            'plotly': 'Data visualization for trial results and statistics',
            'vizzu': 'Animated data visualization with smooth transitions',
            'marp': 'Slide deck for presentations and lectures',
        }
        return explanations.get(tool, 'General purpose visual content')

    def route(self, request: str, verbose: bool = True) -> str:
        """
        Route request to optimal tool.

        Args:
            request: User request text
            verbose: Print routing decision

        Returns:
            Tool name
        """
        tool, confidence, metadata = self.analyze_request(request)

        if verbose:
            print(f"\n🎨 Visual Router Decision")
            print(f"=" * 50)
            print(f"Tool: {tool.upper()}")
            print(f"Confidence: {confidence:.1%}")
            print(f"Reasoning: {metadata['reasoning']}")
            print(f"\nAll Scores:")
            for t, s in sorted(metadata['all_scores'].items(), key=lambda x: x[1], reverse=True):
                print(f"  {t:10} {s:.1f}")
            print(f"\nKeywords Found:")
            for t, kws in metadata['keywords_found'].items():
                if kws:
                    print(f"  {t:10} {', '.join(kws[:3])}")

        return tool

    def get_tool_info(self, tool: str) -> Dict:
        """Get information about a specific tool."""
        tools = {
            'antv': {
                'name': 'AntV Infographic',
                'description': 'Template-driven infographics with 200+ built-in templates',
                'best_for': ['Trial timelines', 'Mechanism steps', 'Treatment pathways', 'Guideline summaries'],
                'output': 'SVG (via HTML preview)',
                'script': 'visual-design-system/antv_infographic/scripts/antv_renderer.py',
            },
            'gemini': {
                'name': 'Gemini Image Generation',
                'description': 'AI-generated custom infographics and medical illustrations',
                'best_for': ['Custom infographics', 'Medical illustrations', 'Visual summaries'],
                'output': 'PNG/JPG',
                'script': 'cardiology-visual-system/scripts/gemini_infographic.py',
            },
            'fal': {
                'name': 'Fal.ai Image Generation',
                'description': 'Stock imagery and lifestyle photos',
                'best_for': ['Blog headers', 'Patient scenarios', 'Lifestyle imagery'],
                'output': 'PNG',
                'script': 'cardiology-visual-system/scripts/fal_image.py',
            },
            'mermaid': {
                'name': 'Mermaid Diagrams',
                'description': 'Structured diagrams and flowcharts',
                'best_for': ['Clinical algorithms', 'Treatment pathways', 'Decision trees'],
                'output': 'SVG/PNG (via MCP)',
                'script': 'Use Mermaid MCP',
            },
            'plotly': {
                'name': 'Plotly Charts',
                'description': 'Data visualization and statistical charts',
                'best_for': ['Trial results', 'Forest plots', 'Trends over time'],
                'output': 'PNG/HTML',
                'script': 'cardiology-visual-system/scripts/plotly_charts.py',
            },
            'vizzu': {
                'name': 'Vizzu Animated Data Viz',
                'description': 'Animated data visualizations with smooth transitions',
                'best_for': ['Animated survival curves', 'Animated forest plots', 'Trial enrollment dashboards', 'Trend animations'],
                'output': 'HTML/MP4/GIF/WebM',
                'script': 'visual-design-system/vizzu_animations/vizzu_cli.py',
            },
            'marp': {
                'name': 'Marp Presentations',
                'description': 'Slide decks from Markdown',
                'best_for': ['Presentations', 'Lectures', 'Educational slides'],
                'output': 'PPTX/PDF/HTML',
                'script': 'Use Marp CLI',
            },
        }

        return tools.get(tool, {})


def main():
    """CLI interface for visual router."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Route visual content requests to optimal tool',
        epilog='Example: python visual_router.py "Create a trial timeline infographic"'
    )
    parser.add_argument('request', help='Visual content request')
    parser.add_argument('--quiet', action='store_true', help='Suppress verbose output')
    parser.add_argument('--info', action='store_true', help='Show tool information')

    args = parser.parse_args()

    router = VisualRouter()
    tool = router.route(args.request, verbose=not args.quiet)

    if args.info:
        print(f"\n📋 Tool Information")
        print(f"=" * 50)
        info = router.get_tool_info(tool)
        for key, value in info.items():
            if isinstance(value, list):
                print(f"{key.title()}: {', '.join(value)}")
            else:
                print(f"{key.title()}: {value}")

    return tool


if __name__ == '__main__':
    main()
