# AI Video Generation

## Patterns


---
  #### **Name**
Model Selection Matrix
  #### **Description**
Choose the right AI video model for each use case
  #### **When**
Starting any AI video project
  #### **Example**
    Model strengths (as of 2025):
    
    VEO3 (Google):
    - Best for: Photorealistic humans, natural motion, long clips
    - Weakness: Slower generation, less stylization control
    - Use when: Realism matters most, corporate/commercial
    
    RUNWAY GEN-3:
    - Best for: Artistic styles, motion control, consistent characters
    - Weakness: Shorter clips, sometimes uncanny faces
    - Use when: Creative/artistic projects, style transfer
    
    SORA (OpenAI):
    - Best for: Complex scenes, physics simulation, long coherence
    - Weakness: Queue times, less control
    - Use when: Ambitious scenes, world simulation
    
    KLING:
    - Best for: Speed, iteration, good motion
    - Weakness: Less photorealistic than Veo3
    - Use when: Fast prototyping, animation-style content
    
    PIKA:
    - Best for: Quick iterations, image-to-video, lip sync
    - Weakness: Shorter duration, less complex scenes
    - Use when: Social content, quick turnarounds
    
    LUMA DREAM MACHINE:
    - Best for: Camera motion, 3D consistency
    - Weakness: Character consistency
    - Use when: Product shots, architectural visualization
    

---
  #### **Name**
The Seed Frame Technique
  #### **Description**
Generate starting image with AI, then animate for consistency
  #### **When**
You need consistent style or character across video
  #### **Example**
    Problem: AI video models struggle with consistency across shots.
    
    Solution: Control the starting point.
    
    Workflow:
    1. Generate hero image in Midjourney/Flux with exact style
    2. Create character/object reference sheet
    3. Use image-to-video feature with seed image
    4. Generate multiple variations, select best motion
    5. Upscale final selection
    
    This gives you: Style consistency + AI motion generation
    
    Pro tip: Generate same character from multiple angles as
    reference images, then animate each for multi-shot sequence.
    

---
  #### **Name**
The Impossible Camera
  #### **Description**
Design shots that couldn't exist in physical production
  #### **When**
Leveraging AI video's unique strengths over traditional
  #### **Example**
    AI video advantage: No physical camera, no physics constraints.
    
    Impossible shots to try:
    - Continuous zoom from space to molecular level
    - Camera moving through solid objects
    - Time manipulation (freeze, reverse, loop) mid-shot
    - Perspective shifts (first person to god view seamlessly)
    - Scale transitions (human to insect to cosmic)
    
    Prompt pattern: "Camera [impossible movement] through [subject],
    continuous shot, no cuts, [style]"
    
    Example: "Camera flies through computer screen, enters digital
    world, zooms through data visualization, emerges from another
    screen in a different room, continuous shot, photorealistic"
    

---
  #### **Name**
Multi-Model Pipeline
  #### **Description**
Combine models to get best of each
  #### **When**
No single model satisfies all requirements
  #### **Example**
    Example pipeline for product commercial:
    
    1. MIDJOURNEY: Generate product in hero environment (style control)
    2. RUNWAY: Image-to-video for hero shot (motion quality)
    3. VEO3: Generate lifestyle B-roll (realism)
    4. PIKA: Quick variations for social cuts (speed)
    5. TOPAZ: Upscale all final selections (quality)
    6. PREMIERE: Edit together with traditional footage
    
    Each model does what it's best at.
    Final output: Better than any single model could produce.
    

---
  #### **Name**
Temporal Coherence Hacking
  #### **Description**
Maintain consistency across longer AI video sequences
  #### **When**
Generating content longer than a single clip allows
  #### **Example**
    Problem: AI models generate 5-10 second clips. You need 60 seconds.
    
    Techniques:
    1. OVERLAP METHOD: Generate clips with 1-2 second overlap,
       crossfade in editing
    
    2. KEYFRAME ANCHOR: Generate keyframes as images first,
       then video-to-video between keyframes
    
    3. LOOP AND EXTEND: Generate loopable middle section,
       unique intro and outro
    
    4. SCENE BREAKS: Instead of fighting coherence, embrace cuts.
       Each AI clip = one shot. Edit like traditional footage.
    
    5. CONSISTENT ELEMENTS: Use same prompt prefix for style.
       "In the style of [description], cinematic lighting,
       [your scene description]"
    

---
  #### **Name**
The Hybrid Production Model
  #### **Description**
Combine AI generation with traditional production
  #### **When**
Maximum quality with AI efficiency
  #### **Example**
    AI replaces: B-roll, establishing shots, impossible shots,
    visualizations, product renders
    
    Human creates: Talking heads, testimonials, interviews,
    performances requiring nuance
    
    Workflow:
    1. Shoot human elements traditionally (controlled, efficient)
    2. Generate AI elements to match (style match, extend scenes)
    3. Use AI for pickup shots (no reshoots needed)
    4. Composite AI backgrounds behind human footage
    5. Edit together seamlessly
    
    Cost model: 80% reduction in production costs, 90% of quality.
    

---
  #### **Name**
Platform Selection Matrix 2025
  #### **Description**
Choose the right AI video tool for each use case
  #### **When**
Starting any AI video project
  #### **Example**
    VEO3 (Google):
    - Best for: Cinematic realism, long-form, storytelling
    - Strength: Film-grade quality, consistent characters
    - Weakness: Limited availability, Google ecosystem
    - Use when: Maximum quality matters, enterprise projects
    
    RUNWAY GEN-3 ALPHA TURBO:
    - Best for: 4K output, advanced camera controls
    - Strength: Speed, professional features, API
    - Weakness: 10-second limit per generation
    - Use when: Commercial production, client work
    
    KLING AI:
    - Best for: Motion quality, longer clips (up to 2min)
    - Strength: Excellent motion, good at humans
    - Weakness: Slower generation
    - Use when: Human subjects, extended scenes
    
    PIKA 2.0:
    - Best for: Quick iterations, stylized content
    - Strength: Fast, creative effects
    - Weakness: Less realistic than competitors
    - Use when: Social content, rapid prototyping
    
    MINIMAX VIDEO:
    - Best for: Consistency, product demos
    - Strength: Stable outputs, good for objects
    - Use when: Product marketing, consistent style
    
    SORA:
    - Best for: Complex scenes, physics accuracy
    - Strength: Understands real-world physics
    - Weakness: Limited access
    - Use when: Available and physics matters
    

---
  #### **Name**
Enterprise Video Pipeline
  #### **Description**
Production-ready workflow with cost tracking and quality gates
  #### **When**
Scaling AI video for enterprise marketing
  #### **Example**
    ENTERPRISE WORKFLOW:
    
    1. BRIEF & BUDGET
    - Define output requirements (resolution, length, style)
    - Calculate cost ceiling: ~$0.05-0.50 per second
    - Set generation budget (e.g., 10 iterations per scene)
    
    2. GENERATION PHASE
    - Use API for batch processing
    - Implement rate limiting (respect 10-20 req/min limits)
    - Save all seeds and prompts to metadata JSON
    - Track costs per generation
    
    3. QUALITY GATES
    - Motion smoothness check
    - Brand consistency verification
    - Artifact detection (hands, faces, text)
    - Human review before final selection
    
    4. INTEGRATION
    - Export with metadata for asset management
    - Version control for prompt libraries
    - A/B test variations before scaling
    
    COST TRACKING:
    ```python
    generation_log = {
      "prompt": "...",
      "model": "runway-gen3",
      "duration": 10,
      "cost_estimate": 0.50,
      "seed": 12345,
      "selected": True
    }
    ```
    

---
  #### **Name**
Multi-Model Composition
  #### **Description**
Combine multiple AI video tools for optimal results
  #### **When**
Single model can't achieve desired output
  #### **Example**
    HYBRID WORKFLOW EXAMPLES:
    
    Product Hero Video:
    1. MINIMAX: Generate product rotation (consistency)
    2. RUNWAY: Add camera motion and style
    3. VEO3: Generate lifestyle B-roll
    4. COMBINE: Edit together in Premiere/DaVinci
    
    Brand Story Video:
    1. MIDJOURNEY: Create key visual frames
    2. RUNWAY: Animate Midjourney frames (image-to-video)
    3. KLING: Generate human presenter scenes
    4. COMBINE: Seamless edit with transitions
    
    Social Ad Package:
    1. Generate HERO version in VEO3/Runway (highest quality)
    2. Use PIKA for quick 9:16 variations
    3. Generate 5 hook variations with different openings
    4. A/B test with real audience
    
    KEY PRINCIPLE:
    No single model excels at everything.
    Use each model for its strengths.
    Combine outputs for final product.
    

## Anti-Patterns


---
  #### **Name**
Single-Prompt Dependency
  #### **Description**
Expecting perfect results from one prompt
  #### **Why**
AI video requires iteration; first generation is rarely final
  #### **Instead**
Generate 10+ variations. Select and refine. Iterate on prompt.

---
  #### **Name**
Ignoring Model Limitations
  #### **Description**
Fighting against what a model can't do well
  #### **Why**
Each model has weaknesses; forcing them creates uncanny results
  #### **Instead**
Match task to model strength. Use different model if needed.

---
  #### **Name**
Skipping Human Review
  #### **Description**
Publishing AI video without careful human evaluation
  #### **Why**
AI hallucinates confidently—weird hands, extra limbs, physics breaks
  #### **Instead**
Frame-by-frame review for hero content. Check hands, faces, text.

---
  #### **Name**
Over-Prompting
  #### **Description**
Adding too many instructions that conflict
  #### **Why**
AI models can't handle contradictory or too-complex prompts
  #### **Instead**
Simple, clear prompts. One style direction. Build complexity gradually.

---
  #### **Name**
Ignoring Resolution Hierarchy
  #### **Description**
Generating at final resolution immediately
  #### **Why**
Wastes compute and time on rejected generations
  #### **Instead**
Generate low-res first, select best, upscale winners only.

---
  #### **Name**
Fighting Temporal Limits
  #### **Description**
Trying to generate long videos in single pass
  #### **Why**
Models have clip length limits; longer = more artifacts
  #### **Instead**
Embrace short clips. Edit together like traditional footage.