#!/usr/bin/env python3
"""
3D Stack Selector for Marketing Projects
Helps choose the right 3D technology for marketing and content creation projects.
"""

import sys
import json

def analyze_project(project_type, target_platform, complexity, timeline):
    """Analyze project requirements and recommend 3D stack."""

    recommendations = {
        "spline": {
            "score": 0,
            "reason": "",
            "best_for": ["quick-demos", "designer-led", "marketing-prototypes"],
            "limitations": ["complex-interactions", "custom-shaders", "large-scenes"]
        },
        "react_three_fiber": {
            "score": 0,
            "reason": "",
            "best_for": ["e-commerce", "react-sites", "interactive-configurators"],
            "limitations": ["non-react-projects", "simple-scenes"]
        },
        "threejs": {
            "score": 0,
            "reason": "",
            "best_for": ["custom-experiences", "max-control", "complex-animations"],
            "limitations": ["steep-learning", "longer-development"]
        },
        "babylonjs": {
            "score": 0,
            "reason": "",
            "best_for": ["game-like", "vr-ar", "physics-simulations"],
            "limitations": ["smaller-community", "enterprise-focus"]
        }
    }

    # Scoring logic
    if timeline == "urgent" or timeline == "short":
        recommendations["spline"]["score"] += 3
        recommendations["spline"]["reason"] += "Fastest to implement for quick marketing demos. "

    if project_type in ["product-configurator", "e-commerce"]:
        recommendations["react_three_fiber"]["score"] += 2
        recommendations["react_three_fiber"]["reason"] += "Ideal for interactive product experiences. "

    if complexity == "high" or project_type == "immersive-brand-experience":
        recommendations["threejs"]["score"] += 2
        recommendations["threejs"]["reason"] += "Maximum control for complex brand experiences. "

    if target_platform == "mobile-web":
        recommendations["spline"]["score"] += 1
        recommendations["spline"]["reason"] += "Good mobile performance with built-in optimizations. "

    # Find best recommendation
    best = max(recommendations.items(), key=lambda x: x[1]["score"])

    return {
        "recommendation": best[0],
        "score": best[1]["score"],
        "reason": best[1]["reason"],
        "all_options": recommendations
    }

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        result = analyze_project(
            project_type="product-configurator",
            target_platform="web",
            complexity="medium",
            timeline="medium"
        )
        print(json.dumps(result, indent=2))
    else:
        print("3D Stack Selector for Marketing Projects")
        print("Usage: python3 3d_stack_selector.py test")
        print("
This tool helps choose the right 3D technology for marketing projects.")
