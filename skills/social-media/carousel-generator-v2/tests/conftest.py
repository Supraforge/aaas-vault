"""
Pytest Configuration for Carousel Generator v2 Tests
"""

import sys
from pathlib import Path

import pytest

# Add scripts directory to path for imports
scripts_dir = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))


@pytest.fixture
def sample_slide_data():
    """Sample slide data for testing."""
    return {
        "type": "hook",
        "data": {
            "slideNumber": 1,
            "totalSlides": 5,
            "headline": "5 Statin Myths Debunked",
            "subtitle": "What the science actually says",
            "icon": "Pill",
            "theme": "teal"
        }
    }


@pytest.fixture
def sample_carousel_data():
    """Sample carousel data for testing."""
    return [
        {
            "type": "hook",
            "data": {
                "slideNumber": 1,
                "totalSlides": 5,
                "headline": "5 Statin Myths Debunked",
                "subtitle": "What the science actually says",
                "icon": "Pill",
                "theme": "teal"
            }
        },
        {
            "type": "myth",
            "data": {
                "slideNumber": 2,
                "totalSlides": 5,
                "myth": "Statins cause muscle pain in everyone",
                "truth": "Only 5-10% experience any muscle symptoms",
                "source": "Lancet 2022"
            }
        },
        {
            "type": "stat",
            "data": {
                "slideNumber": 3,
                "totalSlides": 5,
                "stat": "25%",
                "label": "Reduction in Heart Attack Risk",
                "context": "For every 1 mmol/L reduction in LDL",
                "source": "CTT Meta-analysis",
                "icon": "Heart",
                "color": "green"
            }
        },
        {
            "type": "tips",
            "data": {
                "slideNumber": 4,
                "totalSlides": 5,
                "title": "3 Tips for Statin Success",
                "tips": [
                    {"text": "Take at the same time daily"},
                    {"text": "Report symptoms early"},
                    {"text": "Combine with lifestyle changes"}
                ]
            }
        },
        {
            "type": "cta",
            "data": {
                "slideNumber": 5,
                "totalSlides": 5,
                "name": "Dr Shailesh Singh",
                "credentials": "Cardiologist | Evidence-Based Medicine",
                "handle": "@dr.shailesh.singh",
                "valueProposition": "Follow for evidence-based cardiology"
            }
        }
    ]
