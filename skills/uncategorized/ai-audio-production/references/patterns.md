# AI Audio Production

## Patterns


---
  #### **Name**
Music Model Selection
  #### **Description**
Choose the right AI music tool for the task
  #### **When**
Starting any AI music generation project
  #### **Example**
    SUNO AI:
    - Best for: Songs with vocals, lyrics, full arrangements
    - Strength: Vocal quality, song structure, emotional range
    - Weakness: Sometimes unpredictable, harder to control precisely
    - Use when: You need a "song" with vocals and lyrics
    
    UDIO:
    - Best for: Production quality, genre accuracy, instrumentals
    - Strength: Clean production, genre-specific details
    - Weakness: Vocals less natural than Suno
    - Use when: Production polish matters most
    
    SOUNDRAW:
    - Best for: Background music, customizable loops, commercial use
    - Strength: Predictable, customizable length/intensity
    - Weakness: Less creative range
    - Use when: You need reliable, licensable background music
    
    ELEVENLABS SFX:
    - Best for: Sound effects, foley, ambient audio
    - Strength: Text-to-sound for any described effect
    - Use when: Custom sound effects needed quickly
    

---
  #### **Name**
Genre-Accurate Prompting
  #### **Description**
Prompt for specific musical genres with technical accuracy
  #### **When**
Generating music that must fit a specific genre
  #### **Example**
    Generic prompt (weak):
    "happy upbeat music"
    
    Genre-specific prompt (strong):
    "Upbeat indie pop, 120 BPM, acoustic guitar strumming,
    handclaps, tambourine, warm analog synth bass, breathy
    female vocals, summer festival vibes, Vampire Weekend
    meets HAIM production style"
    
    Key elements to specify:
    - BPM (tempo)
    - Key instruments
    - Production era/style
    - Reference artists (for vibe, not copying)
    - Mood and use case
    - Specific sonic characteristics
    
    The more specific, the more control.
    

---
  #### **Name**
The Reference Track Method
  #### **Description**
Use existing music as a launching point for AI generation
  #### **When**
You know the vibe you want but can't describe it
  #### **Example**
    Step 1: Find reference track that has the vibe you want
    Step 2: Analyze it:
      - Genre and subgenre
      - BPM (use tap tempo tool)
      - Key instruments
      - Production style (vintage, modern, lo-fi, polished)
      - Mood and energy curve
      - Vocal style (if applicable)
    
    Step 3: Translate to prompt:
    "Create a track inspired by [analysis], with [your modifications]"
    
    Step 4: Generate and compare to reference
    Step 5: Iterate on prompt to get closer
    
    Never use reference for copying—use for understanding vibe.
    

---
  #### **Name**
Sound Effect Generation
  #### **Description**
Create custom sound effects with AI
  #### **When**
Need specific SFX that don't exist in libraries
  #### **Example**
    Using ElevenLabs Sound Effects or similar:
    
    Describe the sound, not the action:
    Bad: "door closing"
    Good: "Heavy wooden door slamming shut with metallic latch
    click, slight reverb indicating large stone room"
    
    Include:
    - Material (wood, metal, glass, fabric)
    - Scale (small, large, massive)
    - Environment (reverb, echo, room tone)
    - Quality (clean, distorted, lo-fi)
    - Duration (short impact, sustained)
    
    Generate multiple variations. Layer in DAW for complexity.
    

---
  #### **Name**
Audio Branding Package
  #### **Description**
Create consistent audio identity for a brand
  #### **When**
Developing audio logo, hold music, notification sounds
  #### **Example**
    Audio brand elements:
    
    1. AUDIO LOGO (sonic logo): 3-5 second signature sound
       - Generate variations, select most memorable
       - Must work at all volumes, on all speakers
       - Often melodic, sometimes just textural
    
    2. HOLD MUSIC: Background for calls, loading screens
       - Generate in brand mood
       - Loop seamlessly (specify in prompt)
       - Low-key enough to not annoy
    
    3. NOTIFICATION SOUNDS: Alerts, confirmations, errors
       - Short (< 1 second)
       - Distinct but not jarring
       - Consistent sonic palette
    
    4. BACKGROUND MUSIC: Videos, content, spaces
       - Various energy levels (calm, medium, energetic)
       - Same sonic palette as audio logo
       - Generate stems for flexibility
    
    Create brand sound guide like visual brand guide.
    

---
  #### **Name**
Stem Separation and Remix
  #### **Description**
Deconstruct and reconstruct audio using AI
  #### **When**
Need to isolate or modify elements of existing audio
  #### **Example**
    Using LALAL.AI, Descript, or similar:
    
    1. SEPARATE: Upload audio → Extract stems
       - Vocals
       - Drums
       - Bass
       - Other instruments
       - Background noise
    
    2. MANIPULATE: Adjust individual elements
       - Remove vocals for instrumental
       - Isolate vocals for remix
       - Remove background noise from recordings
       - Extract dialogue from noisy source
    
    3. RECONSTRUCT: Combine with new elements
       - AI-generated music bed + extracted vocals
       - Original bass + AI-generated drums
       - Clean dialogue + AI-generated ambience
    
    Workflow: Traditional recording → AI separation →
    AI enhancement → Professional result
    

---
  #### **Name**
Suno v4 Advanced Prompting
  #### **Description**
Professional-grade music generation with Suno's latest model
  #### **When**
Need broadcast-quality AI-generated music
  #### **Example**
    SUNO V4 PROMPT STRUCTURE:
    
    [Genre/Style] + [Instruments] + [Mood] + [Reference] + [Technical]
    
    EXAMPLES:
    
    Corporate/Motivational:
    "Uplifting corporate pop, acoustic guitar strumming,
    warm piano chords, subtle strings, 100 BPM,
    inspiring Monday motivation vibes, clean production"
    
    Tech/Startup:
    "Modern electronic pop, synth arpeggios, four-on-the-floor beat,
    Daft Punk meets The Weeknd, 120 BPM, futuristic optimistic,
    perfect for product launch video"
    
    Emotional/Story:
    "Cinematic orchestral, solo piano intro building to full strings,
    Hans Zimmer inspired, emotional journey, minor key to major resolution,
    3-minute arc for brand story video"
    
    ADVANCED CONTROLS:
    - Specify BPM for precise timing
    - Reference artists for vibe (not copying)
    - Describe energy curve: "builds from quiet to triumphant"
    - Request instrumental: "no vocals, instrumental only"
    
    ITERATION STRATEGY:
    1. Generate 8 variations of initial prompt
    2. Select top 2, note what works
    3. Refine prompt based on winners
    4. Generate 8 more with refined prompt
    5. Select final from batch 2
    

---
  #### **Name**
Udio vs Suno Selection Guide
  #### **Description**
Choose the right AI music platform for each project
  #### **When**
Deciding between Udio and Suno for music generation
  #### **Example**
    SUNO V4:
    ✅ Best for: Songs with vocals, lyrics, emotional range
    ✅ Strength: Natural-sounding vocals, song structure
    ✅ Great at: Pop, rock, folk, singer-songwriter
    ❌ Weakness: Less control over production details
    → Use for: Brand anthem, campaign song, content with lyrics
    
    UDIO:
    ✅ Best for: Production quality, genre accuracy
    ✅ Strength: Clean mixes, professional sound design
    ✅ Great at: Electronic, hip-hop, EDM, instrumentals
    ❌ Weakness: Vocals less natural than Suno
    → Use for: Background music, instrumentals, production polish
    
    DECISION MATRIX:
    
    | Need               | Choose    |
    |--------------------|-----------|
    | Vocals critical    | Suno      |
    | Instrumental only  | Either    |
    | Electronic/EDM     | Udio      |
    | Organic/acoustic   | Suno      |
    | Precise BPM        | Udio      |
    | Emotional impact   | Suno      |
    | Production polish  | Udio      |
    
    PRO STRATEGY:
    Generate in both, select best. Different songs suit different tools.
    

---
  #### **Name**
Complete Audio Branding Package
  #### **Description**
Create consistent audio identity across all touchpoints
  #### **When**
Building comprehensive audio brand for a company
  #### **Example**
    AUDIO BRAND PACKAGE COMPONENTS:
    
    1. SONIC LOGO (3-5 seconds)
       Generate 20+ variations
       Criteria: Memorable, works at all volumes, distinctive
       Prompt: "[Brand personality] sonic signature,
       [key instrument], [emotional quality], 3 seconds,
       instantly recognizable like Intel bong or Netflix ta-dum"
    
    2. HOLD MUSIC (2-3 minutes, loopable)
       Prompt: "Calm [brand mood] background music,
       minimal, loopable, not annoying on repeat,
       [brand instruments], ambient, no vocals"
       Test: Play for 10 minutes, still pleasant?
    
    3. NOTIFICATION SOUNDS (under 1 second each)
       - Success: Bright, positive, confirms action
       - Error: Attention-getting, not jarring
       - Message: Friendly, inviting engagement
       Generate with ElevenLabs SFX for control
    
    4. VIDEO MUSIC LIBRARY (3-5 tracks)
       Variations in energy:
       - Low energy: Thoughtful, ambient
       - Medium energy: Upbeat, engaging
       - High energy: Exciting, dynamic
       All sharing same sonic palette as logo
    
    5. BRAND SOUND GUIDE (Document)
       - Core sonic attributes
       - Instrument palette
       - Tempo range (BPM)
       - Mood spectrum
       - What to avoid
    
    CONSISTENCY RULE:
    All audio shares same:
    - Key/mode (if musical)
    - Instrument family
    - Production style
    - Emotional range
    

## Anti-Patterns


---
  #### **Name**
Genre Vagueness
  #### **Description**
Using generic mood words instead of specific genre terms
  #### **Why**
AI models know genres; vague prompts get vague results
  #### **Instead**
Be specific. "90s trip-hop with vinyl crackle" not "chill music"

---
  #### **Name**
Ignoring Rights
  #### **Description**
Using AI music without understanding licensing
  #### **Why**
AI-generated music has varying license terms; some restrict commercial use
  #### **Instead**
Check platform license terms. Many require subscription for commercial use.

---
  #### **Name**
First Generation Shipping
  #### **Description**
Using the first generated track without iteration
  #### **Why**
AI music is probabilistic; first generation rarely optimal
  #### **Instead**
Generate 10+ versions. Select and refine. Extend/edit winners.

---
  #### **Name**
Ignoring Audio Quality
  #### **Description**
Not properly exporting or mastering AI audio
  #### **Why**
Raw AI output may need EQ, compression, limiting for broadcast
  #### **Instead**
Run through basic mastering chain. Match loudness standards.

---
  #### **Name**
Overcomplicating Prompts
  #### **Description**
Adding contradictory style elements
  #### **Why**
"Jazz rock electronic ambient classical" confuses models
  #### **Instead**
One or two complementary genres. Clear direction.

---
  #### **Name**
Skipping Human Review
  #### **Description**
Publishing AI audio without listening critically
  #### **Why**
AI audio can have artifacts, weird moments, quality issues
  #### **Instead**
Full playthrough before publishing. Edit out problem sections.