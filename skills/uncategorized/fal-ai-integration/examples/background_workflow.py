#!/usr/bin/env python3
"""
Background Manipulation Workflow Example

This script demonstrates:
1. Background removal using Bria RMBG 2.0
2. Background replacement with AI-generated environments
3. Saving and managing results
"""

import os
from dotenv import load_dotenv
import fal_client
import base64

# Load environment variables
load_dotenv()
fal_client.api_key = os.getenv("FAL_KEY")


# ============================================================================
# Core Functions
# ============================================================================

def remove_background(image_path_or_url: str) -> dict:
    """Remove background from an image using Bria RMBG 2.0"""
    
    # Handle local file vs URL
    if os.path.exists(image_path_or_url):
        with open(image_path_or_url, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")
            image_url = f"data:image/webp;base64,{image_data}"
    else:
        image_url = image_path_or_url
    
    print(f"✂️  Removing background from: {image_path_or_url}")
    
    result = fal_client.subscribe(
        "fal-ai/bria/background/remove",
        arguments={"image_url": image_url},
        with_logs=True,
    )
    
    return result


def replace_background(image_path_or_url: str, prompt: str) -> dict:
    """Replace background with AI-generated environment"""
    
    # Handle local file vs URL
    if os.path.exists(image_path_or_url):
        with open(image_path_or_url, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")
            image_url = f"data:image/webp;base64,{image_data}"
    else:
        image_url = image_path_or_url
    
    print(f"🖼️  Replacing background with: {prompt}")
    
    result = fal_client.subscribe(
        "fal-ai/bria/background/replace",
        arguments={
            "image_url": image_url,
            "prompt": prompt,
        },
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
# Main Workflow
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("FAL.ai Background Manipulation Workflow")
    print("=" * 60)
    
    # Check API key
    if not os.getenv("FAL_KEY"):
        print("⚠️  Please set your FAL_KEY in the .env file")
        exit(1)
    
    # Configuration
    INPUT_IMAGE = "path/to/your/image.jpg"  # Replace with your image path
    
    # Example background prompts
    background_prompts = [
        "Standing in a modern tech office with glass walls and city views",
        "At a luxury automotive tradeshow booth with premium lighting",
        "In a cozy library with wooden shelves and warm lighting",
        "On a rooftop terrace at sunset with city skyline in background",
    ]
    
    print("\n📋 Available background options:")
    for i, prompt in enumerate(background_prompts, 1):
        print(f"  {i}. {prompt}")
    
    # Get user choice
    print("\nSelect a background (1-4) or enter custom prompt:")
    user_input = input("> ").strip()
    
    if user_input.isdigit() and 1 <= int(user_input) <= len(background_prompts):
        selected_prompt = background_prompts[int(user_input) - 1]
    else:
        selected_prompt = user_input if user_input else background_prompts[0]
    
    print(f"\n🎯 Using prompt: {selected_prompt}")
    
    # Workflow choice
    print("\nChoose workflow:")
    print("  1. Remove background only")
    print("  2. Replace background")
    workflow = input("> ").strip()
    
    try:
        if workflow == "1":
            # Remove background
            print("\n🚀 Starting background removal...")
            result = remove_background(INPUT_IMAGE)
            
            if result:
                print("\n💾 Saving result...")
                save_images(result, prefix="bg_removed")
                print("\n✅ Background removal complete!")
            else:
                print("\n❌ Background removal failed")
        
        elif workflow == "2":
            # Replace background
            print("\n🚀 Starting background replacement...")
            result = replace_background(INPUT_IMAGE, selected_prompt)
            
            if result:
                print("\n💾 Saving result...")
                save_images(result, prefix="bg_replaced")
                print("\n✅ Background replacement complete!")
            else:
                print("\n❌ Background replacement failed")
        
        else:
            print("Invalid workflow selection")
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
