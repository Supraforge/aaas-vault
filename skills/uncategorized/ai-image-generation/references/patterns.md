# AI Image Generation

## Patterns


---
  #### **Name**
Model Selection Guide
  #### **Description**
Choose the right model for each visual task
  #### **When**
Starting any AI image project
  #### **Example**
    MIDJOURNEY:
    - Best for: Aesthetic beauty, artistic styles, mood, texture
    - Weakness: Less prompt-literal, adds its own interpretation
    - Use when: You want beautiful and trust MJ's taste
    
    FLUX PRO:
    - Best for: Prompt adherence, text in images, specific details
    - Weakness: Can be too literal, less artistic interpretation
    - Use when: You need exactly what you described
    
    DALL-E 3:
    - Best for: Concepts, ideas, clear communication
    - Weakness: Distinctive "DALL-E look", less photorealistic
    - Use when: Concept clarity matters more than aesthetics
    
    STABLE DIFFUSION 3:
    - Best for: Control (ControlNet, LoRA), customization, iteration
    - Weakness: Requires more technical setup
    - Use when: You need specific control or custom training
    
    IMAGEN 3:
    - Best for: Photorealism, natural images
    - Weakness: Less stylization options
    - Use when: Photos of real-looking things
    
    IDEOGRAM:
    - Best for: Text in images, logos, signage
    - Weakness: Less artistic range
    - Use when: Text rendering is critical
    

---
  #### **Name**
The Prompt Architecture
  #### **Description**
Structure prompts for consistent, controllable results
  #### **When**
Writing prompts for any AI image model
  #### **Example**
    Prompt structure (in order of importance):
    
    1. SUBJECT: What is the main focus?
       "A golden retriever puppy"
    
    2. ACTION/STATE: What is it doing?
       "running through autumn leaves"
    
    3. ENVIRONMENT: Where is it?
       "in a sunlit forest clearing"
    
    4. STYLE: How should it look?
       "professional pet photography, Canon EOS R5"
    
    5. LIGHTING: What's the light quality?
       "golden hour backlight, lens flare"
    
    6. MOOD: What feeling?
       "joyful, energetic, warm"
    
    7. TECHNICAL: Camera/format details
       "shallow depth of field, 85mm f/1.4"
    
    Full prompt: "A golden retriever puppy running through
    autumn leaves in a sunlit forest clearing, professional
    pet photography style, golden hour backlight with subtle
    lens flare, joyful and energetic mood, Canon EOS R5,
    85mm f/1.4, shallow depth of field"
    

---
  #### **Name**
Consistent Character Framework
  #### **Description**
Generate the same character across multiple images
  #### **When**
Creating character-based content, mascots, or campaigns
  #### **Example**
    Technique 1: DETAILED DESCRIPTION
    Create exhaustive character description, use in every prompt:
    "[Character X: A 30-year-old woman with shoulder-length
    auburn hair, green eyes, light freckles, wearing a blue
    denim jacket and white t-shirt] walking through city streets"
    
    Technique 2: REFERENCE IMAGES
    Generate hero character image, use as reference (IP-Adapter,
    Midjourney /describe, DALL-E reference)
    
    Technique 3: SEED LOCKING
    Lock seed number for consistent randomness (where supported)
    
    Technique 4: STYLE SHEET
    Generate character turnaround sheet first:
    "Character sheet of [character], multiple angles,
    front view, side view, back view, expressions"
    
    Combine techniques for maximum consistency.
    

---
  #### **Name**
Brand-Aligned Generation
  #### **Description**
Generate images that match brand guidelines
  #### **When**
Creating marketing content that must feel on-brand
  #### **Example**
    Build a brand prompt prefix:
    
    Brand analysis → Prompt elements:
    - Colors: "using [hex colors] color palette"
    - Typography feel: "clean minimalist" or "playful bold"
    - Photography style: "bright and airy" or "moody and dramatic"
    - Subject treatment: "product hero shot" or "lifestyle context"
    
    Create brand prefix:
    "In [Brand] style: clean minimalist aesthetic, bright
    natural lighting, white and soft blue color palette,
    premium product photography feel, "
    
    Use prefix for every generation:
    "[Brand prefix] + [specific image description]"
    
    Store prefix in brand asset library. Update as style evolves.
    

---
  #### **Name**
The Generation Funnel
  #### **Description**
Systematic process from concept to final image
  #### **When**
Any production image generation task
  #### **Example**
    Stage 1: EXPLORE (quantity)
    - Generate 20+ variations with loose prompts
    - Different angles, styles, compositions
    - Goal: Find promising directions
    
    Stage 2: REFINE (quality)
    - Select top 3-5 directions
    - Tighten prompts based on what worked
    - Generate 10 variations of each winner
    - Goal: Nail the concept
    
    Stage 3: POLISH (perfection)
    - Select final winner
    - Inpaint any artifacts
    - Upscale with Magnific or Topaz
    - Color grade if needed
    - Goal: Production-ready asset
    
    Time: 30 minutes for production image vs. hours/days traditional
    

---
  #### **Name**
Batch Consistency System
  #### **Description**
Generate multiple images that feel like a cohesive set
  #### **When**
Creating image series, campaign assets, or galleries
  #### **Example**
    For 10 images that feel like one shoot:
    
    1. STYLE LOCK: Same style suffix on all prompts
       "--style [style code] --seed [base seed]"
    
    2. LIGHTING LOCK: Same lighting description
       "soft studio lighting with subtle shadows"
    
    3. COLOR LOCK: Same color direction
       "muted earth tones with teal accent"
    
    4. COMPOSITION RULES: Same framing approach
       "centered subject, clean background, 16:9"
    
    5. MODEL LOCK: Same model for entire batch
    
    Generate: Create all images, review as grid, regenerate outliers.
    
    Result: 10 images that clearly belong together.
    

---
  #### **Name**
Prompt Weight Control
  #### **Description**
Control relative importance of elements using double-colon syntax
  #### **When**
Need precise control over which elements dominate the image
  #### **Example**
    Midjourney weight syntax:
    cyberpunk city::3 flying cars::1 neon lights::2
    
    Numbers indicate relative weight (3x, 1x, 2x importance)
    Higher weight = more influence on output
    
    PRACTICAL EXAMPLES:
    # Hero product focus:
    product bottle::4 background::1 lighting::2
    
    # Style over subject:
    art nouveau style::3 woman portrait::1
    
    # Balanced composition:
    sunset::2 mountains::2 reflection::2
    
    DEFAULT: Elements without weights are treated as ::1
    RANGE: Typically 0.5 to 5, but can go higher
    

---
  #### **Name**
Advanced Parameter Mastery
  #### **Description**
Key Midjourney parameters for marketing-quality outputs
  #### **When**
Need precise control over aspect ratio, style, and quality
  #### **Example**
    ESSENTIAL PARAMETERS:
    
    --ar 16:9      # Widescreen (ads, YouTube thumbnails)
    --ar 9:16      # Vertical (Stories, Reels, TikTok)
    --ar 1:1       # Square (Instagram feed)
    --ar 4:5       # Instagram portrait
    --ar 2:3       # Pinterest optimal
    
    --s 100-250    # Low stylize: prompt-adherent, literal
    --s 500-750    # Medium: balanced creativity
    --s 750-1000   # High: maximum artistic interpretation
    
    --q 1          # Standard quality (default)
    --q 2          # Higher quality, longer render
    
    --v 6.1        # Latest version
    --style raw    # Less Midjourney aesthetic, more literal
    
    --no text      # Exclude text from image
    --no watermark # Exclude watermarks
    
    MARKETING PRESET:
    /imagine [prompt] --ar 16:9 --s 250 --q 2 --no text --no watermark
    

---
  #### **Name**
Midjourney to Runway Pipeline
  #### **Description**
Standard professional workflow for AI video from AI images
  #### **When**
Creating broadcast-quality video content from generated images
  #### **Example**
    THE PROFESSIONAL PIPELINE:
    
    STEP 1: MIDJOURNEY KEY FRAMES
    Generate 5-10 "key frames" that establish:
    - Visual style and color palette
    - Lighting and mood
    - Character/product consistency
    - Scene compositions
    
    Use same seed (--seed 12345) for consistency.
    Use --style raw for easier animation.
    
    STEP 2: RUNWAY GEN-3 ANIMATION
    Import Midjourney frames to Runway
    - Image-to-video for hero shots
    - Text-to-video for transitions
    - Motion brush for specific animations
    
    Prompt structure for Runway:
    "[Camera motion], [subject action], [atmosphere]"
    Example: "Slow push in, product rotating, soft lighting"
    
    STEP 3: POST-PRODUCTION
    - Color grade for consistency
    - Add transitions between segments
    - Audio sync with Suno/ElevenLabs
    - Export at 4K for future-proofing
    
    This workflow produces broadcast-quality content at 40-60%
    of traditional production time and cost.
    

## Anti-Patterns


---
  #### **Name**
Prompt Vomiting
  #### **Description**
Stuffing prompts with every possible descriptor
  #### **Why**
Overwhelming prompts confuse models; quality drops
  #### **Instead**
50 words maximum. Prioritize. Test what each word does.

---
  #### **Name**
Model Monogamy
  #### **Description**
Using only one model for everything
  #### **Why**
Each model has strengths; one model means missing capabilities
  #### **Instead**
Match model to task. Build multi-model workflow.

---
  #### **Name**
First Generation Shipping
  #### **Description**
Using the first generated image without iteration
  #### **Why**
AI generation is probabilistic; first try is rarely best
  #### **Instead**
Generate batches. Select best. Refine. Never ship v1.

---
  #### **Name**
Ignoring Negatives
  #### **Description**
Not specifying what you DON'T want
  #### **Why**
Models hallucinate defaults—watermarks, text, artifacts
  #### **Instead**
Use negative prompts. "no watermark, no text, no blur"

---
  #### **Name**
Resolution Rushing
  #### **Description**
Generating at maximum resolution immediately
  #### **Why**
Wastes time and compute on rejected concepts
  #### **Instead**
Low-res exploration → Select winners → Upscale finals only

---
  #### **Name**
Prompt Copying Without Understanding
  #### **Description**
Using prompts from others without knowing why they work
  #### **Why**
Context matters; prompts are model-specific, style-specific
  #### **Instead**
Deconstruct prompts. Test each element. Build your own library.