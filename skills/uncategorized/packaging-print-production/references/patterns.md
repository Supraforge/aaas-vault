# Packaging & Print Production

## Patterns


---
  #### **Name**
Print-Ready File Preparation
  #### **Description**
Complete workflow for preparing game files for manufacturing
  #### **When**
Preparing files for any print manufacturer
  #### **How**
    ## File Preparation Checklist
    
    ### Color Mode
    - [ ] All files in CMYK color mode (not RGB)
    - [ ] Rich black for large areas: C60-M40-Y40-K100
    - [ ] Pure black (K100) for small text only
    - [ ] Pantone spot colors specified separately if needed
    - [ ] ICC profile matches manufacturer spec (usually FOGRA39 or US Web Coated SWOP)
    
    ### Dimensions & Bleed
    - [ ] Document size matches dieline exactly
    - [ ] 3mm bleed on all edges (0.125" for US manufacturers)
    - [ ] Safe zone: 4-5mm from cut line for critical elements
    - [ ] Game boards: 10mm bleed for fold-over edges
    
    ### Typography
    - [ ] All fonts converted to outlines/paths
    - [ ] Minimum 8pt for body text
    - [ ] Minimum 6pt for footnotes/fine print
    - [ ] 7pt+ for reversed text (light on dark)
    - [ ] Sans-serif fonts preferred at small sizes
    
    ### Images
    - [ ] Resolution: 300 DPI minimum at final print size
    - [ ] All images embedded (not linked)
    - [ ] No upscaling of low-res images
    
    ### File Format
    - [ ] PDF/X-4 or PDF/X-1a
    - [ ] Layers flattened
    - [ ] Transparency flattened if required
    - [ ] Crop marks and bleed marks included
    
  #### **Example**
    # Adobe Illustrator Export Settings for Print
    
    File > Save As > PDF
    - Preset: [PDF/X-4:2008]
    - Marks and Bleeds:
      - Trim Marks: ON
      - Bleed: 3mm all sides
    - Output:
      - Color Conversion: Convert to Destination
      - Destination: Coated FOGRA39 (ISO 12647-2:2004)
    

---
  #### **Name**
Dieline Creation Standards
  #### **Description**
Industry-standard dieline conventions for packaging
  #### **When**
Creating or reviewing die-cut templates
  #### **How**
    ## Dieline Color Coding (Universal Standard)
    
    | Line Type | Color | Illustrator Spec | Purpose |
    |-----------|-------|------------------|---------|
    | Cut/Die Line | Red | 100% Magenta | Where material is cut |
    | Fold/Score | Blue | 100% Cyan | Where material folds |
    | Perforation | Green | 100% Yellow | Tear-away perforations |
    | Bleed Boundary | Orange | 50M 100Y | Artwork extension limit |
    | Safe Zone | Pink | 30M | Keep critical content inside |
    
    ## Dieline Layer Structure
    ```
    Layer: "DIELINE" (locked, non-printing)
    └── Cut lines (0.25pt stroke, red)
    └── Score lines (0.25pt stroke, blue, dashed)
    └── Bleed boundary (0.25pt stroke, orange)
    └── Safe zone (0.25pt stroke, pink)
    
    Layer: "ARTWORK"
    └── All printable content
    └── Must extend to bleed boundary
    └── Critical elements inside safe zone
    ```
    
    ## Standard Tolerances
    - Die-cut drift: ±1mm (Panda GM standard)
    - Score line accuracy: ±0.5mm
    - Registration: ±0.3mm between colors
    - Corner radius: 3mm standard for cards
    

---
  #### **Name**
Card Stock Selection Guide
  #### **Description**
Choosing appropriate card stock for game components
  #### **When**
Specifying card stock for cards, tiles, or tokens
  #### **How**
    ## Card Stock Decision Matrix
    
    ### By Use Case
    
    | Component | Recommended Stock | GSM | Core | Finish |
    |-----------|-------------------|-----|------|--------|
    | Standard cards | Blue core | 280-300 | Blue | Linen |
    | Hidden info cards | Black core | 310-330 | Black | Linen |
    | Premium/Casino | Black core | 320-350 | Black | Air-cushion |
    | Prototype cards | Art paper | 300 | White | Gloss |
    | Tarot-size cards | Blue/Black | 300-320 | Blue/Black | Linen |
    | Mini cards | Blue core | 280-300 | Blue | Smooth |
    | Tokens/Tiles | Greyboard | 1.5-2mm | N/A | Matte |
    
    ### Core Type Comparison
    
    **Blue Core (280-300 gsm)**
    - Standard for most board games
    - Good opacity, some light bleed-through possible
    - Cost-effective for large print runs
    - Use when: Budget-conscious, no hidden information
    
    **Black Core (310-330 gsm)**
    - Premium casino-grade opacity
    - Zero light bleed-through
    - Stiffer, more substantial feel
    - Use when: Hidden hands, competitive games, premium products
    
    ### Finish Types
    
    **Linen (Air-Cushion)**
    - Embossed cross-hatch texture
    - Reduces friction, easier shuffling
    - Hides fingerprints and wear
    - Best for: Frequently shuffled decks
    
    **Smooth (Ivory)**
    - No embossing, slick surface
    - Shows artwork more clearly
    - Marks and wear more visible
    - Best for: Display cards, minimal handling
    
    **Soft-Touch (Velvet)**
    - Polyurethane coating, suede-like feel
    - Premium tactile experience
    - Higher cost, less shuffle-friendly
    - Best for: Premium editions, special cards
    

---
  #### **Name**
Box Construction Guide
  #### **Description**
Selecting appropriate box styles for game packaging
  #### **When**
Designing game packaging or choosing box type
  #### **How**
    ## Box Type Selection
    
    ### Tuck Box (Card Games)
    **Best for:** Card-only games, <100 cards
    **Construction:** Single piece, folded and glued
    **Material:** 16-18pt card stock
    **Cost:** $ (lowest)
    **Specs:**
    - Add 3mm to card stack height for easy removal
    - Thumb notch: 25mm wide, 15mm deep
    - Lock tab: Full tuck or half-tuck
    
    ### Two-Piece Box (Standard Board Games)
    **Best for:** Medium games, mixed components
    **Construction:** Separate lid and base
    **Material:** 1.5-2mm greyboard, wrapped
    **Cost:** $$ (standard)
    **Specs:**
    - Lid overlap: 15-20mm on sides
    - Wall height: component stack + 15mm
    - Internal clearance: 15mm per dimension from largest component
    
    ### Magnetic Closure Box
    **Best for:** Premium/deluxe editions
    **Construction:** Rigid board with embedded magnets
    **Material:** 800-1500gsm greyboard
    **Cost:** $$$$ (premium)
    **Specs:**
    - 4 magnets: 2 in lid, 2 in base
    - Magnet strength: N35 minimum for secure closure
    - Lid lift: Slow, satisfying open
    - Often collapsible for shipping savings
    
    ### Lift-Lid Box (Big Box)
    **Best for:** Large games, heavy components
    **Construction:** Deep base, shallow lid
    **Material:** 2-2.5mm greyboard
    **Cost:** $$$
    **Specs:**
    - Reinforced corners for weight
    - Finger notch cutouts for lid removal
    
    ## Box Sizing Formula
    ```
    Internal Dimensions:
    Width  = largest component width + 15mm
    Length = largest component length + 15mm
    Height = total component stack + insert + 15mm
    
    External (for two-piece):
    Add 3mm for each wrapped wall (6mm total per dimension)
    Add lid overlap to height (15-20mm)
    ```
    

---
  #### **Name**
Insert Design Principles
  #### **Description**
Creating functional component storage inserts
  #### **When**
Designing game box inserts
  #### **How**
    ## Insert Types Comparison
    
    ### Thermoform (Vacuum-Formed Plastic)
    **Cost:** $$$ (tooling: $1,000-3,000)
    **MOQ:** 1,000+ units for cost-effectiveness
    **Pros:**
    - Custom shapes for each component
    - Professional appearance
    - Components locked in place
    **Cons:**
    - High tooling cost
    - Not eco-friendly
    - Changes require new molds
    **Best for:** Mass market, components with irregular shapes
    
    ### Cardboard Insert
    **Cost:** $
    **MOQ:** No minimum
    **Pros:**
    - Low cost, no tooling
    - Printable surfaces
    - Eco-friendly
    - Easy to modify
    **Cons:**
    - Limited to rectangular compartments
    - Less premium feel
    **Best for:** Budget-conscious, simple component sets
    
    ### EVA Foam Insert
    **Cost:** $$
    **MOQ:** Usually 500+
    **Pros:**
    - Custom die-cut shapes
    - Premium feel
    - Protects delicate components
    **Cons:**
    - Cannot be printed
    - Takes up more space
    **Best for:** Premium editions, delicate miniatures
    
    ## Insert Design Rules
    
    1. **Vertical Storage**: Design so components don't shift when box is stored on side
    2. **Easy Removal**: Finger cutouts or lift ribbons for all compartments
    3. **Sleeved Cards**: Add 5mm height for sleeved card stacks
    4. **Component Grouping**: Organize by setup order or player
    5. **Expansion Space**: Leave room for future content
    6. **Weight Distribution**: Heavy items at bottom
    
    ## Dimensions Guide
    ```
    Compartment = component + clearance
    
    Cards (unsleeved): +2mm width, +3mm height
    Cards (sleeved): +5mm width, +5mm height
    Tokens: +3mm per dimension
    Dice: +2mm per dimension
    Meeples: +3mm per dimension
    Miniatures: +5mm all around
    ```
    

---
  #### **Name**
Finishing Techniques Guide
  #### **Description**
Premium print finishing options and specifications
  #### **When**
Adding special finishes to packaging or components
  #### **How**
    ## Finishing Options Matrix
    
    | Finish | Cost | Setup | Effect | Best On |
    |--------|------|-------|--------|---------|
    | Gloss Lamination | $ | None | Shiny, protected | Mass market boxes |
    | Matte Lamination | $ | None | Soft, sophisticated | Premium boxes |
    | Soft-Touch | $$ | None | Velvet feel | Deluxe editions |
    | Spot UV | $$ | Mask file | Shiny accents | Logos, titles |
    | Foil Stamping | $$$ | Die | Metallic shine | Logos, premium |
    | Embossing | $$$ | Die | Raised texture | Logos, borders |
    | Debossing | $$$ | Die | Recessed texture | Leather-look |
    
    ## Spot UV Specifications
    
    **File Preparation:**
    - Create separate mask file (black = UV area)
    - Minimum line width: 0.5mm
    - Minimum text: 8pt
    - Works best over matte lamination (contrast)
    
    **Common Applications:**
    - Title text on box
    - Logo highlights
    - Card title bars
    - Select artwork elements
    
    ## Foil Stamping Specifications
    
    **Colors Available:**
    - Gold, Silver, Copper (standard)
    - Holographic (premium)
    - Colored metallics (custom)
    
    **Technical Limits:**
    - Minimum detail: 0.25-0.5mm
    - Maximum coverage: Usually <30% of surface
    - No gradients (solid areas only)
    
    **File Preparation:**
    - Vector artwork required
    - Separate layer/file for foil areas
    - 100% black indicates foil placement
    
    ## Embossing/Debossing Specifications
    
    **Depth Options:**
    - Light: 0.3-0.5mm (subtle texture)
    - Medium: 0.5-1.0mm (clear definition)
    - Deep: 1.0-1.5mm (dramatic effect)
    
    **Design Considerations:**
    - Works best with simple shapes
    - Fine detail may be lost
    - Combine with foil for "foil + emboss" (premium)
    - Blind emboss (no ink) for subtle elegance
    
    ## Combination Strategies
    
    **Best Value Premium:**
    Matte lamination + Spot UV on logo
    
    **High-End Look:**
    Soft-touch + Foil stamp + Emboss (on logo)
    
    **Budget Premium:**
    Gloss lamination + Spot UV (limited areas)
    

---
  #### **Name**
Unboxing Experience Design
  #### **Description**
Creating memorable first impressions through packaging
  #### **When**
Designing premium packaging or improving user experience
  #### **How**
    ## The Science of Unboxing
    
    Unboxing triggers dopamine release through anticipation. Design your packaging
    to maximize this effect through deliberate reveal sequences.
    
    ## Reveal Sequence Framework
    
    ### Layer 1: External (Anticipation)
    - First visual impression
    - Shrink wrap or belly band removal
    - Box texture and weight
    - **Goal:** Build anticipation
    
    ### Layer 2: Lid Opening (Reveal)
    - Lid resistance (slow, satisfying lift)
    - First glimpse of contents
    - Hidden message under lid (optional)
    - **Goal:** Dopamine spike
    
    ### Layer 3: Component Discovery (Satisfaction)
    - Organized, inviting layout
    - Each component in its place
    - Progressive revelation of depth
    - **Goal:** Perceived value
    
    ### Layer 4: Hidden Delights (Surprise)
    - Secret compartments
    - Messages under insert
    - Thank you card or bonus content
    - **Goal:** Emotional connection
    
    ## Practical Techniques
    
    **Vacuum Effect (Apple-style)**
    - Precise lid fit creates air resistance
    - Lid lifts slowly, dramatically
    - Requires tight tolerances (±0.5mm)
    
    **Tissue Paper Wrap**
    - Adds tactile layer
    - Covers components on first open
    - Creates unwrapping moment
    
    **Ribbon Pulls**
    - For heavy or snug inserts
    - Adds color accent
    - Premium feel at low cost
    
    **Printed Insert Underside**
    - Hidden art or message
    - Revealed when components removed
    - Easter egg for engaged customers
    
    ## Multi-Sensory Design
    
    | Sense | Element | Example |
    |-------|---------|---------|
    | Sight | Color, composition | Premium matte black with gold foil |
    | Touch | Texture, weight | Soft-touch coating, substantial box |
    | Sound | Opening sounds | Magnetic click, paper rustle |
    | Smell | Material scent | Fresh cardboard, wood components |
    

---
  #### **Name**
Manufacturing Vendor Selection
  #### **Description**
Choosing the right manufacturer for your game
  #### **When**
Deciding where to manufacture game components
  #### **How**
    ## Vendor Comparison Matrix
    
    ### China (Panda GM, LongPack, WinGo)
    **Best for:** Large runs (1,000+), complex components
    **MOQ:** Usually 1,000-1,500 units
    **Lead time:** 8-14 weeks production + 4-6 weeks shipping
    **Cost:** $ (lowest per unit)
    **Strengths:**
    - Widest component options
    - Most experienced with complex games
    - Custom molds affordable
    - Competitive pricing at scale
    **Challenges:**
    - Communication/timezone differences
    - Long shipping times
    - Import duties and tariffs
    - Quality control distance
    
    ### USA (The Game Crafter, Cartamundi USA)
    **Best for:** Small runs, prototypes, fast turnaround
    **MOQ:** 1 unit (TGC), 500+ (Cartamundi)
    **Lead time:** 1-4 weeks
    **Cost:** $$$ (highest per unit)
    **Strengths:**
    - Fast turnaround
    - No import hassles
    - Easy communication
    - Good for Kickstarter fulfillment
    **Challenges:**
    - Higher cost
    - Fewer custom component options
    - Limited finishing options
    
    ### Europe (LudoFact, Cartamundi EU)
    **Best for:** EU fulfillment, premium production
    **MOQ:** 1,000+ typically
    **Lead time:** 6-10 weeks
    **Cost:** $$ (moderate)
    **Strengths:**
    - Quality reputation
    - EU fulfillment convenience
    - Strong sustainability options
    **Challenges:**
    - Higher than China pricing
    - Limited exotic components
    - Some materials sourced from China
    
    ## Decision Framework
    
    ```
    IF quantity < 500:
      → The Game Crafter (USA POD)
    
    IF quantity 500-1000:
      → Compare USA bulk vs China minimum
      → Consider: urgency, component complexity
    
    IF quantity 1000-3000:
      → China likely most cost-effective
      → Get quotes from 2-3 manufacturers
    
    IF quantity 3000+:
      → Definitely China
      → Negotiate pricing, consider multiple vendors
    ```
    
    ## Shipping Cost Reality
    
    From China to USA:
    - 1 pallet (500 units): ~$1,500-2,000 ($3-4/unit)
    - 5 pallets (2,500 units): ~$2,500-3,000 ($1/unit)
    - Full container (5,000+ units): ~$3,000-4,500 ($0.60-0.90/unit)
    
    **Key insight:** Shipping cost per unit drops dramatically with volume.
    Often better to order more units at once.
    

---
  #### **Name**
Cost Optimization Strategies
  #### **Description**
Reducing manufacturing costs without sacrificing quality
  #### **When**
Trying to hit a target price point or improve margins
  #### **How**
    ## Component Nesting Optimization
    
    The single biggest cost saver most designers miss.
    
    ### Card Nesting
    - Standard press sheet: Fits 54-64 poker cards
    - Optimal deck sizes: 54, 108, 162 (multiples of sheet)
    - 55 cards = same cost as 54 (one sheet)
    - 70 cards = same cost as 108 (two sheets)
    
    ### Punchboard Nesting
    - Design tokens to share die-cut patterns
    - Rectangular tokens much cheaper than custom shapes
    - Example: Two 4"x5.5" sheets cheaper than one 8"x11"
      (Same paper, but simpler die)
    
    ### Box Sizing
    - Standard sizes have existing dies
    - Custom sizes = new die ($200-500)
    - Match box to existing manufacturer templates when possible
    
    ## Material Substitutions
    
    | Premium | Budget Alternative | Savings |
    |---------|-------------------|---------|
    | Black core cards | Blue core | 15-20% |
    | Thermoform insert | Cardboard insert | 50-70% |
    | Foil stamping | Spot UV | 40-50% |
    | Linen finish | Standard coating | 5-10% |
    | Custom dice | Standard dice + stickers | 60-80% |
    | Custom meeples | Cubes/standard shapes | 70-90% |
    
    ## Print Run Economics
    
    ```
    Per-unit cost breakdown (typical game):
    
    500 units:  $12-15/unit
    1000 units: $8-10/unit
    2000 units: $6-8/unit
    5000 units: $4-6/unit
    10000 units: $3-5/unit
    
    The jump from 500→1000 often gives 25-35% savings
    ```
    
    ## Hidden Costs to Account For
    
    1. **Freight forwarding:** $0.50-2/unit depending on volume
    2. **Import duties:** 0-25% depending on country
    3. **Warehousing:** $0.50-2/unit/month
    4. **Fulfillment:** $2-5/unit
    5. **Damaged/defect allowance:** 2-5% of units
    
    ## Negotiation Levers
    
    - **Payment terms:** 30% deposit / 70% before shipping (standard)
    - **Repeat orders:** 5-15% discount on reorders
    - **Combined shipping:** Share container with other publishers
    - **Off-peak timing:** Better rates during slow seasons (Jan-Feb)
    

---
  #### **Name**
Sustainable Packaging Options
  #### **Description**
Eco-friendly materials and certifications for game production
  #### **When**
Designing for sustainability or seeking certifications
  #### **How**
    ## Sustainability Certifications
    
    ### FSC (Forest Stewardship Council)
    - Verifies sustainable forestry practices
    - Chain of custody from forest to consumer
    - Adds ~$0.10-0.15/unit to paper costs
    - Strong consumer recognition
    - Required by some retailers
    
    ### Recycled Content
    - Post-consumer recycled (PCR) preferred
    - 30-100% recycled content available
    - May affect paper brightness/quality
    - Often cost-neutral or slight premium
    
    ## Sustainable Material Options
    
    ### Box & Paper
    - FSC-certified greyboard and wrap paper
    - 100% recycled cardboard (Monopoly Go Green approach)
    - Soy-based inks (standard at quality printers)
    - Water-based varnishes
    
    ### Inserts
    - Cardboard instead of plastic thermoform
    - Sugarcane bagasse trays (biodegradable)
    - Molded pulp (egg-carton material)
    
    ### Components
    - FSC-certified wooden pieces
    - "Re-wood" (80% wood waste + 20% binder)
    - Bamboo (fast-growing, renewable)
    - Recycled plastic (for necessary plastic parts)
    
    ### Wrapping
    - Paper belly bands instead of shrink wrap
    - Biodegradable shrink (if wrapping needed)
    - No individual component plastic bags
    
    ## Sustainability Leaders to Emulate
    
    **Stonemaier Games:**
    - FSC wood and paper
    - Soy inks, water-based varnish
    - Cardboard inserts (replaced plastic)
    - Paper belly bands (replaced shrink)
    
    **Lookout Spiele (Greenline):**
    - 100% FSC materials
    - Right-sized boxes (no wasted space)
    - Designed for recycling
    
    ## Cost Impact
    
    | Change | Cost Impact | Difficulty |
    |--------|-------------|------------|
    | FSC certification | +5-10% | Easy |
    | Recycled cardboard | +0-5% | Easy |
    | Soy inks | +0% | Standard |
    | Paper wrap vs shrink | -5% | Easy |
    | Cardboard vs plastic insert | -20-40% | Moderate |
    | Remove component bags | -2-5% | Easy |
    

## Anti-Patterns


---
  #### **Name**
RGB Design Workflow
  #### **Description**
Designing in RGB and converting to CMYK at the end
  #### **Why Bad**
    RGB has a much larger color gamut than CMYK. Neon greens, electric blues, and
    saturated oranges that look vibrant on screen become muddy when converted.
    You won't know how your colors actually look until it's too late.
    
  #### **Instead**
    Start every project in CMYK. Set your color mode before creating the first shape.
    If you must use RGB assets, convert early and adjust colors while you still
    have time to iterate.
    
  #### **Severity**
critical

---
  #### **Name**
Ignoring Bleed
  #### **Description**
Artwork that stops exactly at the trim line
  #### **Why Bad**
    Die-cutting has ±1mm tolerance. Without bleed, you'll get random white edges
    on finished products. This screams "amateur" and cannot be fixed post-production.
    
  #### **Instead**
    Extend all edge-touching artwork 3mm beyond the trim line. Verify bleed on every
    file before submission. Use manufacturer templates that include bleed guides.
    
  #### **Severity**
critical

---
  #### **Name**
Pure Black (K100) for Large Areas
  #### **Description**
Using 100% black (K only) for backgrounds or large solid areas
  #### **Why Bad**
    K100 appears dark gray in print, not black. The single-ink coverage is insufficient
    for rich, deep blacks. Your "black" box will look washed out next to competitors.
    
  #### **Instead**
    Use rich black: C60-M40-Y40-K100 for large areas. Keep pure K100 only for small
    text where registration matters. Some prefer C50-M50-Y50-K100 for warmer black.
    
  #### **Severity**
high

---
  #### **Name**
Tiny Fonts for Game Text
  #### **Description**
Using 5pt or smaller fonts for text players need to read
  #### **Why Bad**
    Below 6pt, most fonts become illegible blobs. Players shouldn't need magnifying
    glasses. Accessibility matters - not everyone has perfect vision.
    
  #### **Instead**
    Minimum 8pt for body text, 6pt absolute minimum for legal text/footnotes.
    Use 7pt+ for reversed text (light on dark). Test print at actual size before
    finalizing. Sans-serif fonts maintain legibility better at small sizes.
    
  #### **Severity**
high

---
  #### **Name**
Screen-Based Color Proofing
  #### **Description**
Approving colors based only on monitor display
  #### **Why Bad**
    Monitors vary wildly in color accuracy. Even calibrated screens don't perfectly
    represent CMYK output. What looks perfect on screen may disappoint in print.
    
  #### **Instead**
    Always request physical proofs from manufacturer. Use calibrated monitors as
    approximation only. For critical brand colors, specify Pantone spot colors.
    Build proof costs into project budget.
    
  #### **Severity**
high

---
  #### **Name**
Unoptimized Component Nesting
  #### **Description**
Designing tokens and cards without considering print sheet layout
  #### **Why Bad**
    A deck of 70 cards costs the same as 108 cards (both require 2 sheets).
    Random token shapes waste expensive punchboard material. You're literally
    throwing money away with inefficient designs.
    
  #### **Instead**
    Design to sheet multiples: 54, 108, 162 cards. Keep tokens rectangular when
    possible. Group similar components on shared sheets. Ask manufacturer for
    sheet sizes early in design process.
    
  #### **Severity**
medium

---
  #### **Name**
Ignoring Component Tolerances
  #### **Description**
Designing insert compartments exactly to component dimensions
  #### **Why Bad**
    Components vary ±1mm. Cards expand when sleeved (+5mm). Tight compartments
    make setup frustrating and cause component damage. Nobody enjoys prying cards
    from too-tight slots.
    
  #### **Instead**
    Add clearance: +2mm for unsleeved cards, +5mm for sleeved. +3mm for tokens.
    Design for easy retrieval with finger cutouts. Test with actual components
    plus sleeves during prototyping.
    
  #### **Severity**
medium

---
  #### **Name**
Last-Minute Manufacturer Selection
  #### **Description**
Choosing manufacturer after design is complete
  #### **Why Bad**
    Each manufacturer has different templates, capabilities, and constraints.
    A design optimized for Panda GM may not work at Game Crafter. You may need
    to redo significant work or accept compromises.
    
  #### **Instead**
    Select manufacturer early. Get their templates and design guidelines before
    starting. Verify component availability. Build relationship through quote
    process before committing to design direction.
    
  #### **Severity**
medium

---
  #### **Name**
Single Proof Review
  #### **Description**
Approving production after seeing only one proof
  #### **Why Bad**
    First proofs often have issues. Color may need adjustment. Text errors hide.
    Structural problems only appear when physically assembled. One round of proofs
    catches maybe 70% of issues.
    
  #### **Instead**
    Budget for 2-3 proof rounds. Have multiple people review. Test-assemble
    physical proofs. Check colors in different lighting. Verify text with fresh
    eyes. Review takes time - build it into timeline.
    
  #### **Severity**
medium