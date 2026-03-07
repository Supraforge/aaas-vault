#!/usr/bin/env python3
"""
Gemini Infographic Generation for Medical Content

Creates infographics, medical illustrations, and educational visuals
using Google's Gemini API.

Usage:
    python gemini_infographic.py --topic "Heart Failure Stages" --output hf_stages.jpg
    python gemini_infographic.py --prompt "Create an infographic showing..." --output output.jpg
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Optional


def get_api_key() -> Optional[str]:
    """Get Gemini API key from environment or .env file."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        return api_key
    
    for parent in [Path.cwd()] + list(Path.cwd().parents):
        env_file = parent / ".env"
        if env_file.exists():
            with open(env_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('GEMINI_API_KEY='):
                        return line.split('=', 1)[1].strip().strip('"').strip("'")
    return None


# Medical infographic prompt templates
INFOGRAPHIC_TEMPLATES = {
    "stages": """Create a clean, professional medical infographic showing the stages/progression of {topic}.

Requirements:
- Clear visual hierarchy with numbered or lettered stages
- Use icons or simple illustrations for each stage
- Brief, readable text descriptions
- Arrows or flow indicators showing progression
- Professional medical color scheme (blues, teals, whites)
- Modern, clean design suitable for patient education
- No cluttered elements
- Easy to read at a glance""",

    "comparison": """Create a professional medical infographic comparing {topic}.

Requirements:
- Side-by-side or column comparison layout
- Clear headers for each option
- Icons representing key points
- Pros/cons or key differences highlighted
- Professional medical color scheme
- Clean, modern design
- Easy to scan and understand""",

    "process": """Create a clear medical infographic showing the process/workflow for {topic}.

Requirements:
- Step-by-step visual flow
- Numbered steps with icons
- Brief text for each step
- Arrows connecting the steps
- Professional, clean design
- Medical color palette (blues, greens, teals)
- Suitable for patient or professional education""",

    "risk_factors": """Create an educational medical infographic about risk factors for {topic}.

Requirements:
- Visual icons for each risk factor
- Grid or radial layout
- Brief descriptions
- Color coding (modifiable vs non-modifiable if applicable)
- Professional medical styling
- Clear hierarchy and readability""",

    "statistics": """Create a data-focused medical infographic presenting statistics about {topic}.

Requirements:
- Key numbers prominently displayed
- Visual representations (icons, simple charts)
- Source attribution space
- Professional layout
- Medical color scheme
- Easy to understand at a glance""",

    "symptoms": """Create a patient-friendly infographic showing symptoms of {topic}.

Requirements:
- Body-related icons or human figure if appropriate
- Clear symptom labels
- Grouped by severity or type if applicable
- When to seek care highlighted
- Warm but professional colors
- Accessible, non-scary presentation""",

    "treatment": """Create a medical infographic summarizing treatment options for {topic}.

Requirements:
- Treatment categories clearly organized
- Icons for each treatment type
- Brief descriptions of each approach
- Professional medical design
- Clear visual hierarchy
- Suitable for patient education""",

    "custom": """{prompt}

Style requirements:
- Professional medical infographic style
- Clean, modern design
- Medical color palette (blues, teals, professional tones)
- Clear visual hierarchy
- Easy to read text
- Icons or illustrations where appropriate
- Suitable for medical education content"""
}


def build_infographic_prompt(
    topic: Optional[str] = None,
    template: str = "custom",
    custom_prompt: Optional[str] = None,
    style: str = "minimalist medical",
    additional_instructions: str = ""
) -> str:
    """Build a complete infographic prompt."""
    
    if custom_prompt:
        base = INFOGRAPHIC_TEMPLATES["custom"].format(prompt=custom_prompt)
    elif topic and template in INFOGRAPHIC_TEMPLATES:
        base = INFOGRAPHIC_TEMPLATES[template].format(topic=topic)
    else:
        raise ValueError("Provide either --topic with --template, or --prompt")
    
    # Add style modifier
    style_addition = f"\n\nVisual style: {style}, high quality, publication ready"
    
    # Add any additional instructions
    if additional_instructions:
        style_addition += f"\n\nAdditional requirements: {additional_instructions}"
    
    return base + style_addition


def generate_infographic(
    prompt: str,
    output_path: str = "infographic.jpg",
    aspect_ratio: str = "3:4",
    resolution: str = "2K"
) -> dict:
    """Generate infographic using Gemini API."""
    
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("❌ Install google-genai:")
        print("   pip install google-genai --break-system-packages")
        sys.exit(1)
    
    api_key = get_api_key()
    if not api_key:
        print("❌ GEMINI_API_KEY not found!")
        print("Set with: export GEMINI_API_KEY=your-key")
        sys.exit(1)
    
    client = genai.Client(api_key=api_key)
    
    print(f"📝 Prompt: {prompt[:150]}...")
    print(f"🚀 Generating infographic ({aspect_ratio}, {resolution})...")
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=[prompt],
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE', 'TEXT'],
                image_config=types.ImageConfig(
                    aspect_ratio=aspect_ratio,
                )
            )
        )
        
        # Process response
        for part in response.parts:
            if hasattr(part, 'inline_data') and part.inline_data:
                # Save image - Gemini returns JPEG by default
                image = part.as_image()
                
                # Ensure .jpg extension for JPEG data
                if not output_path.lower().endswith(('.jpg', '.jpeg')):
                    output_path = output_path.rsplit('.', 1)[0] + '.jpg'
                
                image.save(output_path)
                print(f"✅ Saved: {output_path}")
                
                return {
                    "success": True,
                    "output_path": output_path,
                    "prompt_used": prompt
                }
            elif hasattr(part, 'text') and part.text:
                print(f"📄 Model response: {part.text[:200]}...")
        
        print("⚠️  No image generated. The model may have declined.")
        return {"success": False, "error": "No image in response"}
        
    except Exception as e:
        print(f"❌ Generation error: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Generate medical infographics with Gemini",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Using a template
  python gemini_infographic.py --topic "Heart Failure" --template stages --output hf_stages.jpg
  
  # Custom prompt
  python gemini_infographic.py --prompt "Create an infographic showing 5 warning signs of stroke" --output stroke.jpg
  
  # With style options
  python gemini_infographic.py --topic "AFib Risk Factors" --template risk_factors --style "modern minimal" --aspect 1:1

Templates available: stages, comparison, process, risk_factors, statistics, symptoms, treatment
        """
    )
    
    parser.add_argument("--topic", "-t", help="Topic for template-based generation")
    parser.add_argument("--template", choices=list(INFOGRAPHIC_TEMPLATES.keys()), 
                        default="custom", help="Infographic template type")
    parser.add_argument("--prompt", "-p", help="Custom prompt (overrides template)")
    parser.add_argument("--output", "-o", default="infographic.jpg", help="Output path")
    parser.add_argument("--style", "-s", default="minimalist medical", 
                        help="Visual style description")
    parser.add_argument("--aspect", "-a", default="3:4", 
                        help="Aspect ratio: 1:1, 3:4, 4:3, 16:9, 9:16")
    parser.add_argument("--resolution", "-r", default="2K", 
                        choices=["1K", "2K", "4K"], help="Image resolution")
    parser.add_argument("--instructions", "-i", default="", 
                        help="Additional instructions")
    
    args = parser.parse_args()
    
    # Validate input
    if not args.prompt and not args.topic:
        parser.error("Provide either --prompt or --topic with --template")
    
    # Build prompt
    prompt = build_infographic_prompt(
        topic=args.topic,
        template=args.template,
        custom_prompt=args.prompt,
        style=args.style,
        additional_instructions=args.instructions
    )
    
    # Generate
    generate_infographic(
        prompt=prompt,
        output_path=args.output,
        aspect_ratio=args.aspect,
        resolution=args.resolution
    )


if __name__ == "__main__":
    main()
