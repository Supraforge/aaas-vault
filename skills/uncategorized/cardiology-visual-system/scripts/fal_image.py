#!/usr/bin/env python3
"""
Fal.ai Image Generation for Medical Blogs

Generates contextually appropriate images for cardiology content.
Focuses on human experiences, not medical devices.

Usage:
    python fal_image.py "Patient experiencing chest pain" --output hero.png
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Optional, Tuple

# ============================================================================
# CONTENT GUIDELINES
# ============================================================================

BLOCKED_TERMS = [
    # Devices
    "pacemaker", "icd", "defibrillator", "stent", "balloon", "catheter",
    "valve", "lvad", "heart pump", "holter", "monitor device", "implant",
    "lead", "generator", "watchman", "occluder", "clip", "mitraclip",
    # Clinical imagery
    "ecg", "ekg", "electrocardiogram", "angiogram", "fluoroscopy", 
    "ct scan", "mri", "echo", "echocardiogram", "x-ray", "xray",
    "ultrasound", "doppler", "cardiac catheterization", "cath lab",
    # Procedures
    "surgery", "operation", "incision", "operating room", "surgical",
    "ablation", "cardioversion", "bypass", "cabg", "tavr", "tavi",
    "pci", "angioplasty", "thrombectomy",
    # Anatomical
    "cross-section", "cross section", "diagram", "schematic", "anatomy",
    "artery illustration", "heart diagram", "blood vessel diagram",
    # Medications
    "pill", "tablet", "medication bottle", "syringe", "injection",
    "iv drip", "infusion"
]

STYLE_PRESETS = {
    "photo": "realistic photography, natural lighting, editorial quality, professional photo",
    "illustration": "clean digital illustration, modern medical communication style, warm colors",
    "editorial": "editorial photography style, magazine quality, storytelling composition"
}

MEDICAL_CONTEXT_ENHANCERS = {
    "chest pain": "concerned expression, hand on chest, realistic indoor or office setting",
    "shortness of breath": "person catching breath, slight fatigue visible, empathetic portrayal",
    "palpitations": "hand on heart, worried but composed expression, home environment",
    "fatigue": "tired but resilient expression, natural lighting, relatable setting",
    "dizziness": "person steadying themselves, concerned expression, indoor setting",
    "swelling": "person noticing discomfort, seated position, caring atmosphere",
    "heart attack": "sudden distress, clutching chest, urgent but dignified portrayal",
    "anxiety": "worried expression, tense posture, empathetic lighting",
    "recovery": "hopeful expression, signs of improvement, warm lighting",
    "exercise": "active movement, healthy lifestyle, outdoor or gym setting",
    "diet": "healthy food, family or individual meal setting, warm atmosphere",
    "doctor": "compassionate healthcare provider, reassuring conversation, professional setting",
    "family": "supportive loved ones, caring expressions, home or hospital waiting area",
    "elderly": "dignified older adult, wise expression, respectful portrayal",
    "caregiver": "supportive person, gentle interaction, caring atmosphere"
}


def check_blocked_content(prompt: str) -> Tuple[bool, Optional[str]]:
    """Check if prompt requests blocked medical content."""
    prompt_lower = prompt.lower()
    for term in BLOCKED_TERMS:
        if term in prompt_lower:
            return True, term
    return False, None


def enhance_prompt(prompt: str, style: str = "photo") -> str:
    """Enhance prompt for medical blog appropriateness."""
    enhanced = prompt
    
    # Add context-specific enhancements
    prompt_lower = prompt.lower()
    for context, enhancement in MEDICAL_CONTEXT_ENHANCERS.items():
        if context in prompt_lower:
            if enhancement not in enhanced.lower():
                enhanced = f"{enhanced}, {enhancement}"
            break
    
    # Add style preset
    style_suffix = STYLE_PRESETS.get(style, STYLE_PRESETS["photo"])
    enhanced = f"{enhanced}, {style_suffix}"
    
    # Add general quality modifiers
    if "high quality" not in enhanced.lower():
        enhanced = f"{enhanced}, high quality, detailed, professional"
    
    return enhanced


def suggest_alternative(blocked_term: str) -> str:
    """Suggest a human-centered alternative."""
    alternatives = {
        "pacemaker": "a patient discussing heart rhythm treatment with their doctor, hopeful expression",
        "stent": "a patient learning about their treatment options, engaged conversation with cardiologist",
        "ecg": "a person being reassured by a healthcare provider, calm medical setting",
        "ekg": "a patient receiving good news about their heart health, relieved expression",
        "angiogram": "a patient preparing for a procedure, supported by caring medical staff",
        "surgery": "a family supporting a loved one before a medical procedure, hospital waiting area",
        "catheter": "a patient in recovery, peaceful expression, supportive environment",
        "bypass": "a patient discussing treatment options with surgeon, thoughtful conversation",
        "defibrillator": "a person learning about heart health, educational setting",
        "valve": "a patient and doctor reviewing treatment plan together",
    }
    
    for key, alt in alternatives.items():
        if key in blocked_term.lower():
            return alt
    
    return "a patient having a supportive conversation with their healthcare provider, warm lighting, professional medical setting"


def get_api_key() -> Optional[str]:
    """Check for Fal.ai API key."""
    api_key = os.environ.get("FAL_KEY")
    if api_key:
        return api_key
    
    # Check .env files
    for parent in [Path.cwd()] + list(Path.cwd().parents):
        env_file = parent / ".env"
        if env_file.exists():
            with open(env_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('FAL_KEY='):
                        return line.split('=', 1)[1].strip().strip('"').strip("'")
    return None


def generate_image(
    prompt: str,
    model: str = "fal-ai/recraft-v3",
    output_path: str = "medical_blog_image.png",
    style: str = "photo",
    aspect_ratio: str = "16:9"
) -> dict:
    """Generate image using Fal.ai API."""
    try:
        import requests
    except ImportError:
        print("❌ Install requests: pip install requests --break-system-packages")
        sys.exit(1)
    
    api_key = get_api_key()
    if not api_key:
        print("❌ FAL_KEY not found!")
        print("Set with: export FAL_KEY=your-api-key")
        print("Get key from: https://fal.ai/dashboard/keys")
        sys.exit(1)
    
    # Check for blocked content
    is_blocked, blocked_term = check_blocked_content(prompt)
    if is_blocked:
        print(f"⚠️  Medical device/procedure detected: '{blocked_term}'")
        alternative = suggest_alternative(blocked_term)
        print(f"   Using alternative: {alternative}")
        prompt = alternative
    
    # Enhance prompt
    enhanced_prompt = enhance_prompt(prompt, style)
    print(f"📝 Prompt: {enhanced_prompt[:100]}...")
    
    # API endpoints
    model_endpoints = {
        "fal-ai/recraft-v3": "https://fal.run/fal-ai/recraft-v3",
        "fal-ai/flux-pro/v1.1": "https://fal.run/fal-ai/flux-pro/v1.1",
        "fal-ai/flux-pro": "https://fal.run/fal-ai/flux-pro",
        "fal-ai/flux/schnell": "https://fal.run/fal-ai/flux/schnell",
        "fal-ai/ideogram/v3": "https://fal.run/fal-ai/ideogram/v3",
    }
    
    endpoint = model_endpoints.get(model, f"https://fal.run/{model}")
    
    # Prepare payload
    payload = {"prompt": enhanced_prompt}
    
    if "recraft" in model.lower():
        size_map = {
            "16:9": {"width": 1920, "height": 1080},
            "4:3": {"width": 1440, "height": 1080},
            "1:1": {"width": 1024, "height": 1024},
            "3:4": {"width": 1080, "height": 1440},
            "9:16": {"width": 1080, "height": 1920},
        }
        payload["image_size"] = size_map.get(aspect_ratio, size_map["16:9"])
        payload["style"] = "realistic_image" if style == "photo" else "digital_illustration"
    elif "flux" in model.lower():
        payload["image_size"] = aspect_ratio
    elif "ideogram" in model.lower():
        payload["aspect_ratio"] = aspect_ratio
    
    print(f"🚀 Generating with {model}...")
    
    headers = {
        "Authorization": f"Key {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=120)
        
        if response.status_code != 200:
            print(f"❌ API Error ({response.status_code})")
            print(f"   {response.text[:500]}")
            sys.exit(1)
        
        result = response.json()
        
        # Extract image URL
        image_url = None
        if "images" in result and result["images"]:
            img = result["images"][0]
            image_url = img.get("url") if isinstance(img, dict) else img
        elif "image" in result:
            img = result["image"]
            image_url = img.get("url") if isinstance(img, dict) else img
        elif "output" in result:
            out = result["output"]
            image_url = out[0] if isinstance(out, list) else out
        
        if not image_url:
            print(f"⚠️  No image URL in response: {list(result.keys())}")
            sys.exit(1)
        
        # Download and save
        print(f"📥 Downloading...")
        img_response = requests.get(image_url, timeout=60)
        
        with open(output_path, 'wb') as f:
            f.write(img_response.content)
        
        print(f"✅ Saved: {output_path}")
        
        # Cost estimate
        costs = {"recraft": 0.04, "flux-pro": 0.04, "flux/schnell": 0.003, "ideogram": 0.08}
        for key, cost in costs.items():
            if key in model.lower():
                print(f"💰 Cost: ~${cost:.3f}")
                break
        
        return {"success": True, "output_path": output_path, "prompt_used": enhanced_prompt}
        
    except requests.exceptions.Timeout:
        print("❌ Timeout. Try fal-ai/flux/schnell for faster generation.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate medical blog images via Fal.ai")
    parser.add_argument("prompt", help="Image description")
    parser.add_argument("--output", "-o", default="medical_blog_image.png", help="Output path")
    parser.add_argument("--model", "-m", default="fal-ai/recraft-v3", help="Fal.ai model")
    parser.add_argument("--style", "-s", choices=["photo", "illustration", "editorial"], default="photo")
    parser.add_argument("--aspect", "-a", default="16:9", help="Aspect ratio")
    
    args = parser.parse_args()
    
    generate_image(
        prompt=args.prompt,
        model=args.model,
        output_path=args.output,
        style=args.style,
        aspect_ratio=args.aspect
    )


if __name__ == "__main__":
    main()
