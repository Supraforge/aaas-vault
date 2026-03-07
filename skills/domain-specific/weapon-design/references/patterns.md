# Weapon Design for Games

## Patterns


---
  #### **Name**
Silhouette-First Design
  #### **Description**
Design weapons as recognizable shapes before adding any detail
  #### **When**
Beginning any weapon concept, especially for games with large arsenals
  #### **Example**
    SILHOUETTE TEST PROTOCOL:
    
    1. Black-out test: Fill weapon solid black
       - Is it recognizable at 100px? 50px? 20px?
       - Can you tell melee from ranged?
       - Can you distinguish weapon class?
    
    2. Thumb test: Hold thumb over screen
       - Would you recognize this weapon behind your thumb?
       - Does the shape tell you the attack type?
    
    3. Silhouette differentiation:
       Common sword:    |=====>
       Greatsword:      |===============>
       Curved blade:    |~~~~~>
       Axe:             |===[]
       Hammer:          |===[===]
       Staff:           |==================|
       Dagger:          |=>
    
    FromSoftware's Moonlight Greatsword works because:
    - Distinctive curved blade (not straight like others)
    - Glowing element creates secondary silhouette
    - Width-to-length ratio unique in arsenal
    
    BAD SILHOUETTE: Detailed but generic longsword shape
    GOOD SILHOUETTE: Asymmetric blade with distinct pommel
    

---
  #### **Name**
Material Language System
  #### **Description**
Use consistent material associations to communicate weapon properties
  #### **When**
Establishing visual language for damage types and weapon origins
  #### **Example**
    MATERIAL → DAMAGE TYPE ASSOCIATIONS:
    
    Physical:
    - Steel/Iron → Slash/Pierce (gray, metallic sheen)
    - Bronze → Ancient/Blessed (warm metal, patina)
    - Bone/Ivory → Primal/Necrotic (off-white, organic curves)
    - Stone → Blunt/Earthen (rough texture, heavy)
    - Obsidian → Piercing (black, glass-sharp edges)
    
    Elemental:
    - Fire: Red-orange glow, ember particles, heat distortion
    - Ice: Blue crystalline, frost accumulation, cold mist
    - Lightning: Yellow-white arcs, crackling, metal conductors
    - Poison: Green liquid, dripping, organic growths
    - Holy: White-gold radiance, clean lines, angelic motifs
    - Dark: Purple-black void, absorbing light, corrupted forms
    
    Sci-Fi Energy:
    - Plasma: Blue-white core, contained energy field
    - Laser: Red beam, heat marks on housing
    - Particle: Green glow, accelerator rings
    - Void: Dark energy, gravitational distortion
    
    WETA PRINCIPLE: Even fantasy materials should feel manufacturable.
    Ask: "What would a smith do with this material?"
    

---
  #### **Name**
Weapon Weight Communication
  #### **Description**
Use proportions and grip placement to communicate weapon weight
  #### **When**
Designing any weapon that needs to "feel" heavy or light
  #### **Example**
    WEIGHT THROUGH PROPORTION:
    
    Heavy weapons (slow, powerful):
    - Thick, wide blade relative to handle
    - Handle positioned close to heavy end (short lever arm)
    - Chunky grip suggests two-handed use
    - Wide crossguard for counterbalance
    - Example: Greatsword, War hammer, Greataxe
    
    Light weapons (fast, precise):
    - Thin, narrow blade relative to handle
    - Long handle relative to blade (long lever arm)
    - Thin grip suggests one-handed/finesse
    - Minimal crossguard or hand protection
    - Example: Rapier, Dagger, Wand
    
    Balanced weapons (versatile):
    - Proportional blade-to-handle ratio
    - Balance point near crossguard
    - Moderate grip thickness
    - Example: Longsword, Spear, Katana
    
    FromSoftware's Berserk-inspired Greatsword:
    - Handle is 1/5 of total length (short lever = heavy)
    - Blade widens toward tip (top-heavy)
    - No detailed crossguard (weight is THE feature)
    - Rough texture suggests crude iron (heavy material)
    
    ANTI-PATTERN: Thin handle on massive blade = looks fragile
    PATTERN: Scale handle thickness with blade mass
    

---
  #### **Name**
Rarity Tier Visual Escalation
  #### **Description**
Create clear visual hierarchy that communicates rarity at a glance
  #### **When**
Designing weapons across multiple rarity tiers (common to legendary)
  #### **Example**
    RARITY VISUAL LANGUAGE (Destiny-inspired):
    
    Common (White):
    - Single material (all steel, all wood)
    - No special effects
    - Simple geometry
    - Functional, utilitarian appearance
    - "A soldier's weapon"
    
    Uncommon (Green):
    - Secondary material accent (leather wrap, metal inlay)
    - Subtle color variation
    - Slightly refined geometry
    - "A skilled craftsman's weapon"
    
    Rare (Blue):
    - Two distinct materials (steel + gold trim)
    - One unique silhouette element
    - Minor glow or particle effect
    - "A noble's weapon"
    
    Epic (Purple):
    - Three+ materials
    - Complex geometry with unique features
    - Active particle effects
    - Glowing elements
    - "A hero's weapon"
    
    Legendary (Orange/Gold):
    - Exotic materials (void crystals, dragon bone)
    - Impossible geometry (floating parts, energy cores)
    - Intense particle systems
    - Transforms or has alternate states
    - Unique audio signature
    - "A god's weapon"
    
    Exotic/Mythic (Yellow/Cyan):
    - Defies physics entirely
    - Multiple visual states
    - Ambient world effect (distorts nearby visuals)
    - Has "personality" - feels alive
    - "A legend made manifest"
    
    CRITICAL: Escalation must be consistent across entire arsenal.
    If your rare weapons have floating parts, legendary needs MORE.
    

---
  #### **Name**
First-Person vs Third-Person Optimization
  #### **Description**
Design weapons differently based on primary camera perspective
  #### **When**
Starting weapon design for any game project
  #### **Example**
    FIRST-PERSON PRIORITIES (Destiny, Halo, DOOM):
    
    1. Right-side silhouette matters most
       - Weapon held on right, detail visible on right
       - Left side can be simpler (rarely seen)
    
    2. Bottom 1/3 of screen real estate
       - Don't obstruct view with wide weapons
       - Scope/sight placement critical for aiming feel
    
    3. Animation support:
       - Clear reload animation surfaces
       - Visible moving parts (bolts, chambers)
       - Muzzle flash anchor point visible
    
    4. Hand visibility:
       - Gloves/hands frame the weapon
       - Grip ergonomics must read clearly
    
    THIRD-PERSON PRIORITIES (Dark Souls, Monster Hunter):
    
    1. Full 360-degree silhouette
       - Every angle must read
       - Back of weapon matters (sheathed view)
    
    2. Scale relative to character
       - Weapon defines character silhouette
       - Oversized weapons = power fantasy
       - Proportions relative to body, not screen
    
    3. Animation telegraphs:
       - Weapon shape indicates attack arc
       - Length communicates reach
       - Width suggests attack area
    
    4. Idle pose weapon placement:
       - Weapon visible in default stance
       - Contributes to character identity
    
    Bungie GDC Insight: "First-person weapons are 30% of the
    player's visual experience. They must be perfect."
    

---
  #### **Name**
Cultural Weapon Integration
  #### **Description**
Draw from real weapon history to inform fantasy designs
  #### **When**
Creating weapons that feel "authentic" even in fantasy settings
  #### **Example**
    CULTURAL WEAPON VOCABULARY:
    
    Japanese:
    - Katana: Single-edged curve, long handle, circular tsuba
    - Emphasize: Elegant curves, clean geometry, subtle decoration
    - Avoid: Excessive ornamentation, symmetrical guards
    
    European Medieval:
    - Longsword: Straight double-edge, cruciform crossguard
    - Emphasize: Functional beauty, balanced proportions
    - Avoid: Oversized gems, impractical spikes
    
    Norse/Viking:
    - Axe: Bearded blade, long ash handle, minimal guard
    - Emphasize: Brutal efficiency, carved wood, iron work
    - Avoid: Clean chrome finish, symmetrical designs
    
    Middle Eastern:
    - Scimitar: Deep curve, single edge, ornate pommel
    - Emphasize: Flowing curves, geometric patterns, gold inlay
    - Avoid: Straight blades, European crossguards
    
    Chinese:
    - Jian: Straight double-edge, disc guard, tassel
    - Dao: Single-edge curve, ring pommel
    - Emphasize: Elegant simplicity, jade accents, symmetry
    
    FANTASY SYNTHESIS EXAMPLE:
    "Elven Longsword" = European length/balance + Japanese curves +
                        Art Nouveau organic decoration
    
    Result feels "elven" because it combines recognizable elements
    into something new but internally consistent.
    

---
  #### **Name**
Sci-Fi Weapon Plausibility
  #### **Description**
Ground futuristic weapons in understandable technology
  #### **When**
Designing weapons for sci-fi or technology-heavy settings
  #### **Example**
    SCI-FI WEAPON DESIGN PRINCIPLES:
    
    Mass Effect Approach (Hard Sci-Fi):
    - All weapons use same base technology (mass effect fields)
    - Visual language consistent: heat sinks, eezo cores, modular parts
    - Ammunition is block of metal shaved into projectiles
    - Players understand the "why" of the design
    
    Halo Approach (Military Sci-Fi):
    - Human weapons: Recognizable firearm evolution
      - Magazine placement, barrel, stock, grip
      - Green/tan military colors, tactical rails
    - Covenant weapons: Alien but functional
      - Organic curves, purple/blue energy
      - No obvious ammunition (plasma-based)
    - Forerunner weapons: Transcendent technology
      - Geometric, orange hardlight
      - Floats, assembles, defies physics
    
    PLAUSIBILITY CHECKLIST:
    [ ] Energy source visible (glowing core, heat vents)
    [ ] Grip accommodates hands (even alien ones)
    [ ] Barrel/emission point clear
    [ ] Firing direction obvious
    [ ] Moving parts suggest mechanical operation
    [ ] Material suggests technology level
    
    Mass Effect Rail Gun Example:
    - Electromagnetic rails visible along barrel
    - Capacitor bank near grip (power source)
    - Heat sinks with cooling fins
    - Scope has electronics, not glass
    - Military modular construction
    
    "The best sci-fi weapons feel like they could be built."
    

---
  #### **Name**
Elemental Damage Visualization
  #### **Description**
Create consistent visual language for elemental/damage types
  #### **When**
Designing weapons with multiple damage types in the same game
  #### **Example**
    ELEMENTAL VISUAL CONSISTENCY:
    
    Fire Weapons:
    - Colors: Red, orange, yellow gradient
    - Materials: Blackened metal, ember glow, heat distortion
    - Particles: Sparks, smoke wisps, floating embers
    - Shape language: Aggressive, angular, flame-like protrusions
    - Example: Blade edge glows orange, darkens toward spine
    
    Ice Weapons:
    - Colors: White, light blue, cyan gradient
    - Materials: Crystalline, frosted metal, ice formations
    - Particles: Snowflakes, cold mist, breath vapor
    - Shape language: Sharp, crystalline, faceted
    - Example: Blade has ice crystal growths along edge
    
    Lightning Weapons:
    - Colors: Yellow, white, electric blue
    - Materials: Conductive metals, copper coils, capacitors
    - Particles: Arcing electricity, static sparks
    - Shape language: Angular, circuit-like patterns
    - Example: Metal blade with visible arc points
    
    Poison/Acid Weapons:
    - Colors: Green, purple, sickly yellow
    - Materials: Corroded metal, organic growths, dripping liquid
    - Particles: Bubbles, drips, toxic vapor
    - Shape language: Organic, corrupted, asymmetric
    - Example: Blade with etched channels holding green liquid
    
    Holy/Light Weapons:
    - Colors: White, gold, soft blue
    - Materials: Pristine metal, angelic imagery, inscriptions
    - Particles: Soft radiance, floating motes, lens flares
    - Shape language: Symmetrical, elegant, flowing
    
    CRITICAL: Same element = same visual language across ALL weapons.
    Fire sword and fire gun should share color palette and particle style.
    

## Anti-Patterns


---
  #### **Name**
The Unusable Fantasy Weapon
  #### **Description**
Designing weapons that couldn't physically be used
  #### **Why**
    Players have intuitive physics understanding. Weapons that defy basic
    physics break immersion and feel "wrong" even when players can't
    articulate why. WETA Workshop made functional Lord of the Rings weapons
    specifically to avoid this - and it shows in the films.
    
  #### **Instead**
    Even fantasy weapons should pass the "could I hold this?" test:
    
    BAD: 8-foot sword with grip in the middle
       - Where's the balance point?
       - How do you swing it?
    
    GOOD: 8-foot sword with long handle (1/3 of length)
       - Leverage makes swinging plausible
       - Historical zweihander reference
    
    BAD: Axe blade wider than the handle is long
       - Top-heavy to the point of unusable
       - Would rotate in your grip
    
    GOOD: Wide axe blade with extended counterweight pommel
       - Shows designer considered balance
       - Still reads as "massive" but feels real
    
    "If WETA couldn't forge it, redesign it."
    

---
  #### **Name**
Silhouette Homogeneity
  #### **Description**
Making all weapons in a class look too similar
  #### **Why**
    Players need to quickly identify weapons in gameplay. When your arsenal
    has 50 swords that all have the same basic shape, players struggle to
    identify their loadout, enemies' weapons, and loot drops.
    
  #### **Instead**
    Silhouette differentiation strategies:
    
    For 10 swords in one game:
    1. Vary blade curvature (straight, slight curve, deep curve)
    2. Vary blade width (thin rapier, medium arming sword, wide cleaver)
    3. Vary crossguard shape (cruciform, curved, disc, none)
    4. Vary pommel (round, pointed, animal head, none)
    5. Vary blade count (single, double, serrated)
    
    Test: Print silhouettes at 1 inch. Can you name each sword?
    If no, differentiate more.
    
    FromSoftware Arsenal Test:
    - Claymore: Wide, simple crossguard, straight
    - Zweihander: Narrower, longer, curved quillons
    - Bastard Sword: Medium, fuller visible
    - Moonlight: Curved, no guard, glowing blade
    
    Each immediately recognizable.
    

---
  #### **Name**
Rarity Visual Inflation
  #### **Description**
Making common weapons too fancy or legendary weapons not fancy enough
  #### **Why**
    Visual rarity is a contract with the player. When common weapons have
    particle effects, legendary weapons lose impact. When legendary weapons
    look plain, the grind feels unrewarding. Consistent escalation is
    essential for player satisfaction.
    
  #### **Instead**
    AUDIT YOUR RARITY SCALE:
    
    1. List ALL visual features in your legendary weapons
    2. Check: Do ANY common/uncommon weapons have these features?
    3. If yes, remove from lower tiers OR add more to legendary
    
    Visual Feature Tier Assignment:
    - Single material: Common only
    - Secondary material accent: Uncommon+
    - Third material: Rare+
    - Particle effects: Epic+
    - Animated/moving parts: Epic+
    - Impossible geometry: Legendary+
    - Transforms/multiple states: Exotic only
    
    ANTI-PATTERN: "But this uncommon sword is REALLY cool so it gets particles"
    PATTERN: "Particles start at Epic. No exceptions. Cool uncommon = better proportions"
    
    Destiny's Gjallarhorn works because nothing below Exotic
    has tracking wolf-head missiles.
    

---
  #### **Name**
Ignoring Audio/VFX Integration
  #### **Description**
Designing weapons without considering sound and effects
  #### **Why**
    Weapons are audiovisual experiences. A weapon that looks powerful but
    sounds weak feels weak. Design and audio/VFX must align or the weapon
    feels "broken" to players.
    
  #### **Instead**
    Design with audio/VFX anchors:
    
    DESIGN DOCUMENT MUST INCLUDE:
    1. Sound profile
       - Attack: Whoosh, clang, bang, pew
       - Impact: Thud, slice, crunch, sizzle
       - Ambient: Hum, crackle, drip
    
    2. VFX anchors
       - Muzzle/emission point location
       - Trail origin and end points
       - Impact effect spawn point
       - Ambient effect attachment bones
    
    3. Screen feel
       - Camera shake intensity
       - Hitstop duration
       - Recoil pattern
    
    Example: Fire Greatsword
    - Visual: Glowing orange edge, ember particles
    - Audio: Low whoosh + crackle on swing, sizzle on impact
    - VFX: Fire trail from tip, ember burst on hit
    - Feel: Slow swing, heavy hitstop, screen shake
    
    All elements say "heavy fire weapon." Consistency is key.
    

---
  #### **Name**
Culture Cosplay Without Research
  #### **Description**
Superficially borrowing cultural weapon aesthetics without understanding them
  #### **Why**
    Katanas with cruciform crossguards, Viking swords with Chinese tassels,
    "tribal" weapons that match no actual culture - these feel disrespectful
    and amateurish. Players who know real weapons notice immediately.
    
  #### **Instead**
    CULTURAL RESEARCH PROTOCOL:
    
    1. Study 5+ real examples from the culture
    2. Identify functional AND decorative elements
    3. Understand WHY design choices exist
       - Katana curve = cutting draw-cuts
       - European crossguard = hand protection in armored combat
       - Chinese ring pommel = balance + lanyard attachment
    
    4. Keep functional elements accurate
    5. Apply fantasy to decorative elements
    
    GOOD: Elven katana
    - Curve maintained (functional)
    - Handle length maintained (functional)
    - Tsuba replaced with leaf-motif guard (decorative)
    - Mekugi replaced with crystal pins (decorative)
    
    BAD: "Asian-inspired" sword
    - Random curve direction
    - European proportions
    - Generic "oriental" pattern
    - No understanding of real sword anatomy
    

---
  #### **Name**
Power Creep in Visuals
  #### **Description**
Continually escalating visual flair until hierarchy breaks
  #### **Why**
    When each new content drop adds "cooler looking" weapons, eventually
    common weapons look like old legendaries, and new legendaries have
    to be absurdly over-designed. Players lose trust in visual rarity
    signaling. The World of Warcraft shoulder pad problem.
    
  #### **Instead**
    VISUAL CEILING DOCTRINE:
    
    1. Define maximum visual intensity at project start
       - "Legendary weapons have X particles max"
       - "No more than Y materials per weapon"
       - "Floating parts reserved for Exotic tier"
    
    2. New content fills gaps, doesn't raise ceiling
       - New legendary? Different look, same intensity
       - New exotic? Matches existing exotic intensity
    
    3. Audit each release
       - Does this weapon exceed its tier ceiling?
       - Does this make existing same-tier weapons look weak?
       - If yes: Redesign to fit ceiling
    
    PATTERN: "Different, not more."
    
    Destiny handles this by giving each expansion a visual theme,
    not escalating power-look across expansions.
    