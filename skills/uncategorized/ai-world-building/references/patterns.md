# AI World Building

## Patterns


---
  #### **Name**
The World Bible Structure
  #### **Description**
Document the rules that define a brand universe
  #### **When**
Creating a new brand world or systematizing an existing one
  #### **Example**
    WORLD BIBLE SECTIONS:
    
    1. VISUAL FOUNDATION
       - Core color palette (with usage rules)
       - Typography system
       - Texture and material language
       - Light quality (time of day, source, temperature)
       - Aspect ratios and composition rules
    
    2. CHARACTER SYSTEM
       - Main characters (detailed sheets)
       - Character archetypes (rules for creating new ones)
       - Wardrobe guidelines
       - Expression ranges
       - Forbidden elements (what characters NEVER do)
    
    3. ENVIRONMENT SYSTEM
       - Key locations (detailed references)
       - Architectural language
       - Natural elements
       - Props and objects
       - Forbidden elements
    
    4. INTERACTION RULES
       - How characters relate to environments
       - How elements combine
       - Composition patterns
       - Motion principles (if applicable)
    
    5. PROMPT LIBRARY
       - Base prompts for each asset type
       - Style suffixes
       - Negative prompts
       - Model-specific versions
    
    OUTPUT: Living document that enables anyone to generate
    consistent assets without art direction.
    

---
  #### **Name**
Character Model Sheet System
  #### **Description**
Define characters for consistent AI generation
  #### **When**
Creating characters that must appear consistently
  #### **Example**
    CHARACTER SHEET INCLUDES:
    
    1. VISUAL REFERENCE (AI-generated):
       - Front view (neutral)
       - 3/4 view
       - Side profile
       - Back view
       - Multiple expressions (happy, sad, surprised, angry)
       - Multiple poses (standing, sitting, walking, gesturing)
    
    2. TEXT DESCRIPTION (for prompts):
       "[Name] is a [age]-year-old [gender] with [hair description],
       [eye description], [skin tone], [body type]. They wear
       [signature outfit]. Distinguishing features: [list].
       They NEVER [restrictions]."
    
    3. PROMPT FORMULA:
       Base: "[Full description] [action], [environment], [style suffix]"
       Example: "Luna is a 28-year-old woman with shoulder-length
       pink hair, green eyes, fair skin, athletic build. She wears
       a vintage denim jacket and white t-shirt. Distinguishing
       features: small star tattoo on left wrist, silver hoop earrings.
       She NEVER wears hats or formal clothing."
    
    4. CONSISTENCY TECHNIQUES:
       - Use same seed base
       - Reference images (IP-Adapter)
       - LoRA training for important characters
       - Detailed negative prompts
    

---
  #### **Name**
Visual Language Extraction
  #### **Description**
Derive systematic rules from existing brand assets
  #### **When**
Systematizing an existing brand for AI generation
  #### **Example**
    EXTRACTION PROCESS:
    
    Step 1: GATHER (collect all existing brand assets)
    - Photography
    - Illustrations
    - UI elements
    - Marketing materials
    - Social content
    
    Step 2: ANALYZE (find patterns)
    - Color: Extract exact values, relationships
    - Composition: Common layouts, ratios
    - Light: Direction, quality, temperature
    - Texture: Surface qualities, materials
    - Subject treatment: How products/people are shown
    
    Step 3: CODIFY (write rules)
    "Colors: Primary #HEX (60%), Secondary #HEX (30%), Accent #HEX (10%)
    Light: Always soft, slightly warm (5500K), from upper left
    Composition: Rule of thirds, subject in left third, clean backgrounds
    Texture: Matte surfaces, no gloss, subtle grain"
    
    Step 4: TEST (generate with rules)
    - Generate 20 test images using rules
    - Compare to original assets
    - Adjust rules until match is close
    
    Step 5: DOCUMENT (create prompt library)
    - Base style prompt
    - Product shot prompt
    - Lifestyle prompt
    - Social content prompt
    

---
  #### **Name**
Environment as Character
  #### **Description**
Design consistent environments that feel like places
  #### **When**
Creating locations for a brand world
  #### **Example**
    ENVIRONMENT SHEET INCLUDES:
    
    1. OVERVIEW:
       - Name and description
       - Role in brand world
       - Mood and atmosphere
       - Reference images
    
    2. ARCHITECTURAL ELEMENTS:
       - Materials (wood, metal, concrete, glass)
       - Color palette
       - Texture language
       - Scale and proportion
       - Lighting conditions
    
    3. DETAILS:
       - Props that appear
       - Props that NEVER appear
       - Vegetation
       - Weather conditions
       - Time of day
    
    4. VARIATIONS:
       - Same space, different times
       - Same space, different uses
       - Close-up details
       - Wide establishing shots
    
    5. PROMPT FORMULA:
       "[Environment name]: [architectural style] [space type] with
       [material list], [lighting conditions], [mood descriptors],
       featuring [key props], [style suffix]"
    
    Environments should feel recognizable even with different content.
    

---
  #### **Name**
Scalable Universe Expansion
  #### **Description**
System for growing the world while maintaining consistency
  #### **When**
Expanding beyond initial world building
  #### **Example**
    EXPANSION FRAMEWORK:
    
    TIER 1: CORE (immutable)
    - Main characters
    - Key locations
    - Visual foundation
    - These never change
    
    TIER 2: EXTENDED (careful expansion)
    - Secondary characters (follow character archetype rules)
    - Additional locations (follow environment language)
    - New props (follow material/texture language)
    - Require review against world bible
    
    TIER 3: CAMPAIGN-SPECIFIC (temporary)
    - Campaign characters
    - Seasonal variations
    - Promotional elements
    - Must still feel like they belong
    
    EXPANSION PROCESS:
    1. Review world bible rules
    2. Design within constraints
    3. Generate test assets
    4. Compare to existing assets
    5. Refine until coherent
    6. Document new elements
    7. Update world bible if permanent
    
    RULE: It's easier to maintain a smaller, tighter world
    than a sprawling inconsistent one.
    

## Anti-Patterns


---
  #### **Name**
Asset-First Thinking
  #### **Description**
Creating individual assets without systematic rules
  #### **Why**
Each new asset becomes a consistency challenge
  #### **Instead**
Define rules first. Assets should be outputs of rules.

---
  #### **Name**
Over-Complexity
  #### **Description**
Creating worlds too complex to maintain consistency
  #### **Why**
More elements = more things to get wrong
  #### **Instead**
Start small. Expand carefully. Simplicity enables scale.

---
  #### **Name**
Verbal-Only Documentation
  #### **Description**
Describing world in words without visual references
  #### **Why**
Visual consistency requires visual documentation
  #### **Instead**
World bible must be visual-first. Images, not just text.

---
  #### **Name**
Ignoring Negatives
  #### **Description**
Not defining what's NOT in the world
  #### **Why**
Boundaries are as important as content for consistency
  #### **Instead**
Define what NEVER appears. Explicit exclusions.

---
  #### **Name**
One-Time World Building
  #### **Description**
Creating world bible and never updating
  #### **Why**
Worlds evolve; documentation must too
  #### **Instead**
Living document. Update as world expands and lessons learned.

---
  #### **Name**
Tool Lock-In
  #### **Description**
Building world around one AI tool's capabilities
  #### **Why**
Tools change; world should be tool-agnostic
  #### **Instead**
Describe world in universal terms. Adapt prompts per tool.