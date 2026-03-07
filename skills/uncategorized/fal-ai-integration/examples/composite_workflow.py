#!/usr/bin/env python3
"""
Advanced Compositing Workflow Example

This script demonstrates:
1. Generating custom backgrounds with FLUX
2. Compositing your trained LoRA subject onto backgrounds
3. Fine-tuning integration with strength parameter
"""

import os
from dotenv import load_dotenv
import fal_client
import base64
from typing import Optional

# Load environment variables
load_dotenv()
fal_client.api_key = os.getenv("FAL_KEY")

# ============================================================================
# Configuration
# ============================================================================

TRIGGER_PHRASE = "MYNAME"  # Your unique trigger phrase
TRAINER_ID = "your-trainer-id-here"  # From fal.ai training job


# ============================================================================
# Core Functions
# ============================================================================

def get_trained_model_url(trainer_id: str) -> Optional[str]:
    """Retrieve trained LoRA model URL"""
    try:
        result = fal_client.result("fal-ai/flux-lora-portrait-trainer", trainer_id)
        if result and "diffusers_lora_file" in result:
            return result["diffusers_lora_file"]["url"]
        return None
    except Exception as e:
        print(f"⚠️  Could not fetch trained model: {e}")
        return None


def generate_background(prompt: str, image_size: str = "landscape_16_9") -> dict:
    """Generate a standalone background environment"""
    
    enhanced_prompt = (
        f"Professional 8k architectural photography, {prompt}. "
        f"Cinematic lighting, shallow depth of field, premium quality."
    )
    
    print(f"✨ Generating background: {prompt}")
    
    result = fal_client.subscribe(
        "fal-ai/flux/dev",
        arguments={
            "prompt": enhanced_prompt,
            "image_size": image_size,
            "num_inference_steps": 28,
            "guidance_scale": 3.5,
        },
        with_logs=True,
    )
    
    return result


def composite_subject_on_image(
    background_path: str,
    lora_url: str,
    trigger_phrase: str,
    prompt: Optional[str] = None,
    strength: float = 0.85,
    image_size: str = "landscape_16_9",
) -> dict:
    """Composite your trained subject onto a background image"""
    
    # Read and encode the background image
    with open(background_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")
    
    # Default prompt if none provided
    final_prompt = prompt or (
        f"A professional photograph of {trigger_phrase}, integrated into the scene. "
        f"The lighting on {trigger_phrase} perfectly matches the ambient light. "
        f"High resolution, architectural photography style."
    )
    
    print(f"🎨 Compositing {trigger_phrase} onto background")
    print(f"📝 Prompt: {final_prompt}")
    print(f"⚡ Strength: {strength}")
    
    arguments = {
        "prompt": final_prompt,
        "image_url": f"data:image/webp;base64,{image_data}",
        "strength": strength,
        "loras": [{"path": lora_url, "scale": 1.0}],
        "num_images": 1,
        "image_size": image_size,
        "guidance_scale": 3.5,
        "num_inference_steps": 28,
    }
    
    result = fal_client.subscribe(
        "fal-ai/flux-lora",
        arguments=arguments,
        with_logs=True,
    )
    
    return result


def save_images(result: dict, output_dir: str = "generated_images", prefix: str = "image"):
    """Save generated images from FAL.ai result to disk"""
    import requests
    from pathlib import Path
    import time
    
    Path(output_dir).mkdir(exist_ok=True)
    saved_paths = []
    
    images_to_save = []
    if "image" in result:
        images_to_save.append(result["image"])
    if "images" in result:
        images_to_save.extend(result["images"])
    
    for idx, image in enumerate(images_to_save):
        image_url = image["url"]
        response = requests.get(image_url)
        
        if response.status_code == 200:
            timestamp = int(time.time())
            filename = f"{prefix}_{timestamp}_{idx + 1}.png"
            filepath = Path(output_dir) / filename
            
            with open(filepath, "wb") as f:
                f.write(response.content)
            
            saved_paths.append(str(filepath))
            print(f"✅ Saved: {filepath}")
    
    return saved_paths


# ============================================================================
# Main Workflow
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("FAL.ai Advanced Compositing Workflow")
    print("=" * 60)
    
    # Check API key
    if not os.getenv("FAL_KEY"):
        print("⚠️  Please set your FAL_KEY in the .env file")
        exit(1)
    
    # Get trained model
    print(f"\n🔍 Fetching trained model from trainer ID: {TRAINER_ID}")
    lora_url = get_trained_model_url(TRAINER_ID)
    
    if not lora_url:
        print("\n❌ Could not retrieve LoRA model URL")
        exit(1)
    
    # Background generation prompts
    background_prompts = [
        "A modern tech conference booth with blue and gold branding, premium lighting",
        "A luxury automotive showroom with sports cars and dramatic lighting",
        "A minimalist office with floor-to-ceiling windows and city views",
        "A cozy library with leather chairs and warm ambient lighting",
    ]
    
    print("\n📋 Available background options:")
    for i, prompt in enumerate(background_prompts, 1):
        print(f"  {i}. {prompt}")
    
    print("\nSelect background (1-4) or enter custom prompt:")
    user_input = input("> ").strip()
    
    if user_input.isdigit() and 1 <= int(user_input) <= len(background_prompts):
        bg_prompt = background_prompts[int(user_input) - 1]
    else:
        bg_prompt = user_input if user_input else background_prompts[0]
    
    # Step 1: Generate background
    print("\n" + "=" * 60)
    print("STEP 1: Generating Background")
    print("=" * 60)
    
    bg_result = generate_background(bg_prompt)
    
    if not bg_result:
        print("\n❌ Background generation failed")
        exit(1)
    
    print("\n💾 Saving background...")
    bg_paths = save_images(bg_result, prefix="background")
    
    if not bg_paths:
        print("\n❌ Failed to save background")
        exit(1)
    
    background_path = bg_paths[0]
    print(f"\n✅ Background saved: {background_path}")
    
    # Step 2: Composite subject onto background
    print("\n" + "=" * 60)
    print("STEP 2: Compositing Subject")
    print("=" * 60)
    
    # Strength parameter (higher = more transformation)
    print("\nEnter strength (0.75-0.95, default 0.85):")
    strength_input = input("> ").strip()
    strength = float(strength_input) if strength_input else 0.85
    
    # Optional custom prompt
    print("\nEnter custom composite prompt (or press Enter for default):")
    custom_prompt = input("> ").strip()
    
    composite_result = composite_subject_on_image(
        background_path=background_path,
        lora_url=lora_url,
        trigger_phrase=TRIGGER_PHRASE,
        prompt=custom_prompt if custom_prompt else None,
        strength=strength,
    )
    
    if not composite_result:
        print("\n❌ Compositing failed")
        exit(1)
    
    print("\n💾 Saving composite...")
    composite_paths = save_images(composite_result, prefix="composite")
    
    if composite_paths:
        print(f"\n✅ Workflow complete!")
        print(f"📁 Background: {background_path}")
        print(f"📁 Composite: {composite_paths[0]}")
    else:
        print("\n❌ Failed to save composite")
