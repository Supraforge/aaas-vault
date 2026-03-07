---
name: falai-integration
description: >-
  Comprehensive guide for integrating FAL.ai models including FLUX LoRA,
  background manipulation, and image generation
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# FAL.ai Integration Skill

This skill provides patterns and examples for integrating FAL.ai's powerful AI models into your projects. It covers FLUX LoRA custom model training, background removal/replacement, image-to-image compositing, and direct image generation.

## Prerequisites

1. **FAL.ai API Key**: Get your API key from [fal.ai/dashboard/keys](https://fal.ai/dashboard/keys)
2. **Python Environment**: Python 3.8+ with `fal-client` installed
3. **Environment Variables**: Store your API key in `.env` file

```bash
# Install fal-client
pip install fal-client

# Add to .env
FAL_KEY=your_api_key_here
```

## Core Capabilities

### 1. FLUX LoRA Custom Model Training

Train a custom LoRA model on your own images to generate personalized content.

**Key Concepts:**

- **Trigger Phrase**: A unique word/phrase that activates your trained model
- **LoRA URL**: The trained model weights URL returned after training
- **Trainer ID**: The training job ID used to retrieve the model

**Implementation Pattern:**

```python
import fal_client
import os
from dotenv import load_dotenv

load_dotenv()
fal_client.api_key = os.getenv("FAL_KEY")

def get_trained_model_url(trainer_id: str) -> Optional[str]:
    """Retrieve trained LoRA model URL from a completed training job"""
    try:
        result = fal_client.result("fal-ai/flux-lora-portrait-trainer", trainer_id)
        if result and "diffusers_lora_file" in result:
            return result["diffusers_lora_file"]["url"]
        return None
    except Exception as e:
        print(f"Could not fetch trained model: {e}")
        return None

def generate_with_lora(prompt: str, lora_url: str, **kwargs):
    """Generate images using your trained LoRA model"""
    arguments = {
        "prompt": prompt,
        "loras": [{"path": lora_url, "scale": 1.0}],
        "num_images": kwargs.get("num_images", 1),
        "image_size": kwargs.get("image_size", "square_hd"),
        "guidance_scale": kwargs.get("guidance_scale", 3.5),
        "num_inference_steps": kwargs.get("num_inference_steps", 28),
    }
    
    if "seed" in kwargs:
        arguments["seed"] = kwargs["seed"]
    
    return fal_client.subscribe(
        "fal-ai/flux-lora",
        arguments=arguments,
        with_logs=True,
    )
```

**Training Your Model:**

1. Visit [FLUX LoRA Portrait Trainer Playground](https://fal.ai/models/fal-ai/flux-lora-portrait-trainer/playground)
2. Upload 10-20 high-quality images of your subject
3. Choose a unique trigger phrase (e.g., "MYNAME", "MYBRAND")
4. Start training and save the `trainer_id`
5. Use `get_trained_model_url(trainer_id)` to retrieve the model

### 2. Background Removal

Remove backgrounds from images using Bria RMBG 2.0.

**Implementation Pattern:**

```python
import base64

def remove_background(image_path_or_url: str) -> dict:
    """Remove background from an image"""
    
    # Handle local file vs URL
    if os.path.exists(image_path_or_url):
        with open(image_path_or_url, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")
            image_url = f"data:image/webp;base64,{image_data}"
    else:
        image_url = image_path_or_url
    
    result = fal_client.subscribe(
        "fal-ai/bria/background/remove",
        arguments={"image_url": image_url},
        with_logs=True,
    )
    
    return result
```

**Model**: `fal-ai/bria/background/remove`  
**API Docs**: [Background Removal API](https://fal.ai/models/bria/background/remove/api)

### 3. Background Replacement

Replace image backgrounds with AI-generated environments.

**Implementation Pattern:**

```python
def replace_background(image_path_or_url: str, prompt: str) -> dict:
    """Replace background with AI-generated environment"""
    
    # Handle local file vs URL
    if os.path.exists(image_path_or_url):
        with open(image_path_or_url, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")
            image_url = f"data:image/webp;base64,{image_data}"
    else:
        image_url = image_path_or_url
    
    result = fal_client.subscribe(
        "fal-ai/bria/background/replace",
        arguments={
            "image_url": image_url,
            "prompt": prompt,
        },
        with_logs=True,
    )
    
    return result
```

**Example Prompts:**

- "Standing in a modern office with glass walls and city views"
- "At a luxury automotive tradeshow booth with premium lighting"
- "In a cozy library with wooden shelves and warm lighting"

**Model**: `fal-ai/bria/background/replace`  
**API Docs**: [Background Replace API](https://fal.ai/models/bria/replace-background/api)

### 4. Image-to-Image Compositing

Composite your trained subject into existing backgrounds with perfect lighting integration.

**Implementation Pattern:**

```python
def composite_subject_on_image(
    background_path: str,
    lora_url: str,
    trigger_phrase: str,
    prompt: Optional[str] = None,
    strength: float = 0.85,
    **kwargs
) -> dict:
    """Composite your trained subject onto a background image"""
    
    # Read and encode the background image
    with open(background_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")
    
    # Default prompt if none provided
    final_prompt = prompt or (
        f"A professional photograph of {trigger_phrase}, integrated into the scene. "
        f"The lighting on {trigger_phrase} perfectly matches the ambient light."
    )
    
    arguments = {
        "prompt": final_prompt,
        "image_url": f"data:image/webp;base64,{image_data}",
        "strength": strength,  # 0.0-1.0, higher = more transformation
        "loras": [{"path": lora_url, "scale": 1.0}],
        "num_images": kwargs.get("num_images", 1),
        "image_size": kwargs.get("image_size", "landscape_16_9"),
        "guidance_scale": kwargs.get("guidance_scale", 3.5),
        "num_inference_steps": kwargs.get("num_inference_steps", 28),
    }
    
    if "seed" in kwargs:
        arguments["seed"] = kwargs["seed"]
    
    return fal_client.subscribe(
        "fal-ai/flux-lora",
        arguments=arguments,
        with_logs=True,
    )
```

**Key Parameters:**

- `strength`: Controls how much the image changes (0.0 = no change, 1.0 = complete transformation)
- Typical range: 0.75-0.90 for good integration while preserving background

### 5. Direct Background Generation

Generate standalone backgrounds using FLUX models.

**Implementation Pattern:**

```python
def generate_background(prompt: str, image_size: str = "landscape_16_9") -> dict:
    """Generate a standalone background environment"""
    
    enhanced_prompt = (
        f"Professional 8k architectural photography, {prompt}. "
        f"Cinematic lighting, shallow depth of field, premium quality."
    )
    
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
```

## Utility Functions

### Save Images to Disk

```python
def save_images(result: dict, output_dir: str = "generated_images", prefix: str = "image") -> list:
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
```

## Configuration Options

### Image Sizes

- `square_hd` - High definition square
- `square` - Standard square
- `portrait_4_3` - Portrait 4:3 ratio
- `portrait_16_9` - Portrait 16:9 ratio
- `landscape_4_3` - Landscape 4:3 ratio
- `landscape_16_9` - Landscape 16:9 ratio

### Generation Parameters

| Parameter | Range | Default | Description |
|-----------|-------|---------|-------------|
| `guidance_scale` | 1.0-20.0 | 3.5 | How closely to follow the prompt |
| `num_inference_steps` | 1-50 | 28 | Quality vs speed tradeoff |
| `num_images` | 1-4 | 1 | Number of images to generate |
| `seed` | Any int | Random | For reproducible results |
| `strength` | 0.0-1.0 | 0.85 | Image-to-image transformation amount |

## Common Workflows

### Workflow 1: Custom Portrait with Branded Background

```python
# 1. Train your LoRA model (do this once)
trainer_id = "your-trainer-id-from-fal-ai"
lora_url = get_trained_model_url(trainer_id)

# 2. Generate a branded background
bg_result = generate_background(
    "A modern tech conference booth with blue and gold branding, "
    "premium lighting, professional atmosphere"
)
save_images(bg_result, prefix="background")

# 3. Composite your subject onto the background
composite_result = composite_subject_on_image(
    background_path="generated_images/background_*.png",
    lora_url=lora_url,
    trigger_phrase="YOURNAME",
    strength=0.88
)
save_images(composite_result, prefix="final_composite")
```

### Workflow 2: Background Replacement

```python
# 1. Remove existing background
remove_result = remove_background("original_photo.jpg")
save_images(remove_result, prefix="no_bg")

# 2. Replace with new environment
replace_result = replace_background(
    "original_photo.jpg",
    prompt="Standing in a luxury automotive showroom with sports cars"
)
save_images(replace_result, prefix="new_bg")
```

## Best Practices

1. **Trigger Phrases**: Use unique, uncommon words to avoid conflicts with common vocabulary
2. **Training Data**: Use 10-20 high-quality, diverse images for best LoRA results
3. **Prompt Engineering**: Be specific about lighting, atmosphere, and composition
4. **Strength Parameter**: Start with 0.85 for compositing, adjust based on results
5. **Error Handling**: Always wrap FAL.ai calls in try-except blocks
6. **API Response Formats**: Handle both `image` (single) and `images` (list) response formats

## Troubleshooting

### Issue: Generated images don't match training data

- **Solution**: Ensure you're using the trigger phrase in your prompt
- **Solution**: Verify the LoRA URL is correct and model training completed successfully

### Issue: Background integration looks unnatural

- **Solution**: Adjust the `strength` parameter (try 0.75-0.95 range)
- **Solution**: Improve your prompt to describe lighting and scale explicitly

### Issue: API returns empty results

- **Solution**: Check API key is set correctly in environment
- **Solution**: Verify the model name and arguments match API documentation
- **Solution**: Handle both `image` and `images` response keys

## Resources

- [FAL.ai Dashboard](https://fal.ai/dashboard)
- [FLUX LoRA Portrait Trainer](https://fal.ai/models/fal-ai/flux-lora-portrait-trainer)
- [Background Removal API](https://fal.ai/models/bria/background/remove/api)
- [Background Replace API](https://fal.ai/models/bria/replace-background/api)
- [FLUX Dev Model](https://fal.ai/models/fal-ai/flux/dev)

## Example Scripts

See the `examples/` directory for complete, runnable examples:

- `basic_lora_generation.py` - Simple LoRA model usage
- `background_workflow.py` - Complete background manipulation workflow
- `composite_workflow.py` - Advanced compositing with custom backgrounds
