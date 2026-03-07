#!/usr/bin/env python3
"""
Test script for Carousel Generator V2 new features:
1. DataSlide with Plotly chart embeds
2. Author profile configuration system

Usage:
    python scripts/test_new_features.py
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from puppeteer_renderer import PuppeteerRenderer


def test_data_slide():
    """Test DataSlide with Plotly forest plot."""
    print("\n" + "="*60)
    print("TEST 1: DataSlide with Plotly Forest Plot")
    print("="*60 + "\n")

    renderer = PuppeteerRenderer(dimensions="portrait", account=1)

    # Create a forest plot data slide
    forest_data = {
        "studies": ["PARADIGM-HF", "DAPA-HF", "EMPEROR-Reduced", "VICTORIA", "GALACTIC-HF"],
        "estimates": [0.80, 0.74, 0.75, 0.90, 0.92],
        "lower_ci": [0.73, 0.65, 0.65, 0.82, 0.86],
        "upper_ci": [0.87, 0.85, 0.86, 0.98, 0.99],
        "null_value": 1.0
    }

    slides = [
        renderer.create_hook_slide(
            slide_number=1,
            total_slides=3,
            headline="Heart Failure Trials Meta-Analysis",
            subtitle="Evidence-based review of major trials",
            icon="Heart",
            theme="teal"
        ),
        renderer.create_data_slide(
            slide_number=2,
            total_slides=3,
            title="Hazard Ratios Across Trials",
            chart_data=forest_data,
            chart_type="forest",
            caption="All trials showed significant mortality reduction",
            source="Meta-analysis 2024",
            icon="BarChart3"
        ),
        renderer.create_cta_slide(
            slide_number=3,
            total_slides=3
        )
    ]

    # Render
    output_dir = Path(__file__).parent.parent / "outputs" / "test_data_slide"
    output_files = renderer.render_carousel(slides, str(output_dir))

    print(f"✅ Rendered {len(output_files)} slides:")
    for f in output_files:
        print(f"   - {f}")


def test_bar_chart_slide():
    """Test DataSlide with bar chart."""
    print("\n" + "="*60)
    print("TEST 2: DataSlide with Bar Chart")
    print("="*60 + "\n")

    renderer = PuppeteerRenderer(dimensions="portrait", account=1)

    # Create a bar chart data slide
    bar_data = {
        "data": {
            "Outcome": ["Primary Endpoint", "Secondary Endpoint", "Safety Event"],
            "Treatment": [12.3, 8.5, 3.2],
            "Placebo": [18.7, 14.2, 2.8]
        },
        "x": "Outcome",
        "y": "Treatment"
    }

    slides = [
        renderer.create_hook_slide(
            slide_number=1,
            total_slides=3,
            headline="Clinical Trial Results",
            subtitle="Treatment vs Placebo outcomes",
            icon="TrendingUp",
            theme="teal"
        ),
        renderer.create_data_slide(
            slide_number=2,
            total_slides=3,
            title="Treatment Outcomes",
            chart_data=bar_data,
            chart_type="bar",
            caption="Treatment showed superior outcomes across all endpoints",
            source="RCT 2024",
            icon="BarChart3"
        ),
        renderer.create_cta_slide(
            slide_number=3,
            total_slides=3
        )
    ]

    # Render
    output_dir = Path(__file__).parent.parent / "outputs" / "test_bar_chart"
    output_files = renderer.render_carousel(slides, str(output_dir))

    print(f"✅ Rendered {len(output_files)} slides:")
    for f in output_files:
        print(f"   - {f}")


def test_author_config():
    """Test author configuration system with different accounts."""
    print("\n" + "="*60)
    print("TEST 3: Author Configuration System")
    print("="*60 + "\n")

    # Test Account 1
    print("Account 1: @heartdocshailesh")
    renderer1 = PuppeteerRenderer(dimensions="portrait", account=1)

    slides1 = [
        renderer1.create_hook_slide(
            slide_number=1,
            total_slides=2,
            headline="Test Account 1",
            subtitle="Primary cardiology account",
            icon="Heart"
        ),
        renderer1.create_cta_slide(
            slide_number=2,
            total_slides=2
        )
    ]

    output_dir1 = Path(__file__).parent.parent / "outputs" / "test_account_1"
    output_files1 = renderer1.render_carousel(slides1, str(output_dir1))
    print(f"   ✅ Rendered {len(output_files1)} slides")

    # Test Account 2
    print("\nAccount 2: @dr.shailesh.singh")
    renderer2 = PuppeteerRenderer(dimensions="portrait", account=2)

    slides2 = [
        renderer2.create_hook_slide(
            slide_number=1,
            total_slides=2,
            headline="Test Account 2",
            subtitle="Clinical cardiology account",
            icon="Heart"
        ),
        renderer2.create_cta_slide(
            slide_number=2,
            total_slides=2
        )
    ]

    output_dir2 = Path(__file__).parent.parent / "outputs" / "test_account_2"
    output_files2 = renderer2.render_carousel(slides2, str(output_dir2))
    print(f"   ✅ Rendered {len(output_files2)} slides")


def test_full_carousel():
    """Test full carousel with all features."""
    print("\n" + "="*60)
    print("TEST 4: Full Carousel with All Features")
    print("="*60 + "\n")

    renderer = PuppeteerRenderer(dimensions="portrait", account=1)

    # Forest plot data
    forest_data = {
        "studies": ["PARADIGM-HF", "DAPA-HF", "EMPEROR-Reduced"],
        "estimates": [0.80, 0.74, 0.75],
        "lower_ci": [0.73, 0.65, 0.65],
        "upper_ci": [0.87, 0.85, 0.86],
        "null_value": 1.0
    }

    slides = [
        renderer.create_hook_slide(
            slide_number=1,
            total_slides=6,
            headline="5 Heart Failure Facts You Should Know",
            subtitle="Evidence-based insights",
            icon="Heart",
            theme="teal"
        ),
        renderer.create_myth_slide(
            slide_number=2,
            total_slides=6,
            myth="Heart failure means your heart has stopped",
            truth="Heart failure means your heart isn't pumping efficiently, not that it has stopped",
            source="AHA 2024"
        ),
        renderer.create_data_slide(
            slide_number=3,
            total_slides=6,
            title="Major Trial Results",
            chart_data=forest_data,
            chart_type="forest",
            caption="All trials showed significant mortality reduction with SGLT2 inhibitors",
            source="Meta-analysis 2024",
            icon="BarChart3"
        ),
        renderer.create_stat_slide(
            slide_number=4,
            total_slides=6,
            stat="26%",
            label="Mortality Reduction",
            context="With sacubitril/valsartan in HFrEF",
            source="PARADIGM-HF",
            icon="TrendingUp",
            color="green"
        ),
        renderer.create_tips_slide(
            slide_number=5,
            total_slides=6,
            title="3 Ways to Manage Heart Failure",
            tips=[
                {"text": "Take medications as prescribed daily", "icon": "Pill"},
                {"text": "Monitor your weight and symptoms", "icon": "Activity"},
                {"text": "Reduce salt intake to <2g per day", "icon": "Salad"}
            ]
        ),
        renderer.create_cta_slide(
            slide_number=6,
            total_slides=6
        )
    ]

    # Render
    output_dir = Path(__file__).parent.parent / "outputs" / "test_full_carousel"
    output_files = renderer.render_carousel(slides, str(output_dir))

    print(f"✅ Rendered {len(output_files)} slides:")
    for f in output_files:
        print(f"   - {f}")


def main():
    """Run all tests."""
    print("\n" + "="*60)
    print("CAROUSEL GENERATOR V2 - NEW FEATURES TEST SUITE")
    print("="*60)

    try:
        test_data_slide()
        test_bar_chart_slide()
        test_author_config()
        test_full_carousel()

        print("\n" + "="*60)
        print("✅ ALL TESTS COMPLETED SUCCESSFULLY")
        print("="*60 + "\n")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
