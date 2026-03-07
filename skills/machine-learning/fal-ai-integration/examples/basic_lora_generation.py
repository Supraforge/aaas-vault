#!/usr/bin/env python3
"""
Basic LoRA Model Generation Example

This script demonstrates how to:
1. Retrieve a trained LoRA model URL
2. Generate images using your custom LoRA model
3. Save the results to disk
"""

import os
from dotenv import load_dotenv
import fal_client
from typing import Optional

# Load environment variables
load_dotenv()
fal_client.api_key = os.getenv("FAL_KEY")

# ============================================================================
# Configuration
# ============================================================================

# Replace these with your actual values
TRIGGER_PHRASE = "MYNAME"  # Your unique trigger phrase
TRAINER_ID = "your-trainer-id-here"  # From fal.ai training job


# ============================================================================
# Core Functions
# ============================================================================

def get_trained_model_url(trainer_id: str) -> Optional[str]:
    """Retrieve trained LoRA model URL from a completed training job"""
    try:
        result = fal_client.result("fal-ai/flux-lora-portrait-trainer", trainer_id)
        if result and "diffusers_lora_file" in result:
            lora_url = result["diffusers_lora_file"]["url"]
            print(f"✅ Found trained model: {lora_url}")
            return lora_url
        else:
            print("⚠️  Training result found but no LoRA file in response")
            return None
    except Exception as e:
        print(f"⚠️  Could not fetch trained model: {e}")
        return None


def generate_with_lora(
    prompt: str,
    lora_url: str,
    num_images: int = 1,
    image_size: str = "square_hd",
    guidance_scale: float = 3.5,
    num_inference_steps: int = 28,
    seed: Optional[int] = None,
) -> dict:
    """Generate images using your trained LoRA model"""
    
    print(f"🎨 Generating with prompt: {prompt}")
    
    arguments = {
        "prompt": prompt,
        "loras": [{"path": lora_url, "scale": 1.0}],
        "num_images": num_images,
        "image_size": image_size,
        "guidance_scale": guidance_scale,
        "num_inference_steps": num_inference_steps,
    }
    
    if seed is not None:
        arguments["seed"] = seed
    
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
    
    # Handle both 'image' (single) and 'images' (list) formats
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
        else:
            print(f"❌ Failed to download image {idx + 1}")
    
    return saved_paths


# ============================================================================
# Main Script
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("FAL.ai LoRA Generation Example")
    print("=" * 60)
    
    # Check API key
    if not os.getenv("FAL_KEY"):
        print("⚠️  Please set your FAL_KEY in the .env file")
        print("Get your API key from: https://fal.ai/dashboard/keys")
        exit(1)
    
    # Get trained model URL
    print(f"\n🔍 Fetching trained model from trainer ID: {TRAINER_ID}")
    lora_url = get_trained_model_url(TRAINER_ID)
    
    if not lora_url:
        print("\n❌ Could not retrieve LoRA model URL")
        print("Please check your TRAINER_ID and ensure training completed successfully")
        exit(1)
    
    # Example prompts (remember to use your trigger phrase!)
    example_prompts = [
        f"A professional portrait of {TRIGGER_PHRASE}, studio lighting, high quality",
        f"{TRIGGER_PHRASE} in a business suit, confident expression, corporate headshot",
        f"{TRIGGER_PHRASE} smiling, casual outdoor setting, natural lighting",
    ]
    
    print(f"\n🎯 Trigger phrase: '{TRIGGER_PHRASE}'")
    print("\nExample prompts:")
    for i, prompt in enumerate(example_prompts, 1):
        print(f"  {i}. {prompt}")
    
    # Get user input
    print("\n" + "=" * 60)
    print("Enter your prompt (or press Enter for example #1):")
    user_prompt = input("> ").strip()
    
    if not user_prompt:
        user_prompt = example_prompts[0]
        print(f"Using: {user_prompt}")
    
    # Generate images
    print("\n🎨 Generating images...")
    result = generate_with_lora(
        prompt=user_prompt,
        lora_url=lora_url,
        num_images=2,  # Generate 2 variations
    )
    
    # Save results
    if result:
        print("\n💾 Saving images...")
        saved_paths = save_images(result, prefix="lora_gen")
        
        print(f"\n✅ Done! Generated {len(saved_paths)} image(s)")
        print(f"📁 Saved to: generated_images/")
    else:
        print("\n❌ Generation failed")
