# Weapon Design - Sharp Edges

## Unusable Grip Ratio

### **Id**
unusable-grip-ratio
### **Summary**
Weapon grips that couldn't physically be held or controlled
### **Severity**
critical
### **Situation**
  Designing massive blade weapons with tiny handles, or grip placements
  that make no mechanical sense. The "cool art" that fails the WETA test.
  
### **Why**
  Players have intuitive understanding of leverage and balance. A 6-foot
  blade with a 4-inch handle looks wrong even to non-experts. It undermines
  the believability of your entire visual language.
  
### **Solution**
  GRIP-TO-BLADE RATIO GUIDELINES:
  
  One-handed weapons:
  - Handle: 1.5-2x palm widths (6-8 inches)
  - Blade weight must be controllable
  
  Two-handed weapons:
  - Handle: 3-4x palm widths (12-16 inches)
  - Or single long grip with pommel counterweight
  
  Massive/fantasy weapons:
  - Handle length: Minimum 1/4 of blade length
  - Add counterweight features (heavy pommel, tang)
  - Show wear patterns suggesting use
  
  FromSoftware test: Even their absurd weapons have
  proper lever arm ratios.
  
### **Symptoms**
  - This looks awkward to hold
  - Combat animations look floaty
  - Players question physics
  - Weapon feels toy-like despite size
### **Detection Pattern**


## Silhouette Collapse

### **Id**
silhouette-collapse
### **Summary**
Multiple weapons with nearly identical silhouettes
### **Severity**
critical
### **Situation**
  Arsenal of 20 swords that all look the same at gameplay distance.
  Different stats, same visual shape. "Just a different skin."
  
### **Why**
  Players can't identify weapons at a glance. In combat, they can't tell
  what enemies are wielding. Inventory feels like identical clones.
  Loot drops lose excitement because "they all look the same."
  
### **Solution**
  SILHOUETTE DIFFERENTIATION CHECKLIST:
  
  For each weapon pair:
  [ ] Different primary shape (straight vs curved, wide vs narrow)
  [ ] Different overall length category
  [ ] Different distinctive feature (guard, pommel, blade shape)
  [ ] Recognizable at 50px height
  
  Differentiation levers:
  - Blade curvature (straight, slight, deep)
  - Blade width (thin, medium, wide)
  - Guard type (none, disc, cross, curved, complex)
  - Pommel (none, round, pointed, decorative)
  - Blade terminus (pointed, flat, angled, forked)
  
  TEST: Print all weapon silhouettes at 1 inch. Hand to stranger.
  Can they sort by type? If no, differentiate more.
  
### **Symptoms**
  - Players confuse weapons in inventory
  - Enemy weapon identification fails
  - "They all look the same" feedback
  - Loot drops feel unrewarding
### **Detection Pattern**


## Fantasy Physics Break

### **Id**
fantasy-physics-break
### **Summary**
Fantasy weapons that violate their own established physics
### **Severity**
high
### **Situation**
  Magic sword with floating blade - but inconsistent float distance.
  Energy weapon with visible power source - but power runs out without
  visual change. Internal rules established then broken.
  
### **Why**
  Once you establish fantasy physics, breaking them destroys immersion
  worse than never having them. Players accept "magic makes it float"
  but not "magic makes it inconsistently float."
  
### **Solution**
  FANTASY PHYSICS CONSISTENCY:
  
  Document your fantasy rules:
  - "Floating elements hover 2-4 inches from core"
  - "Energy weapons dim when low on charge"
  - "Crystalline blades refract light consistently"
  
  Apply consistently:
  - Same rule for all weapons with that feature
  - Visual state matches game state
  - No exceptions for "cool factor"
  
  Example: Destiny's hard-light weapons
  - ALL have orange glow
  - ALL have similar geometric construction
  - Consistent "Forerunner technology" language
  
### **Symptoms**
  - Wait, why doesn't this one float too?
  - Visual/mechanical state mismatch
  - Players question if features are bugs
  - Fantasy feels arbitrary not magical
### **Detection Pattern**


## Rarity Inversion

### **Id**
rarity-inversion
### **Summary**
Lower-tier weapons looking more impressive than higher-tier ones
### **Severity**
high
### **Situation**
  That one "really cool" uncommon weapon that has particles. The rare
  weapon that's more ornate than the legendary. Visual hierarchy broken.
  
### **Why**
  Rarity hierarchy is a promise to players. "Work harder, get cooler gear."
  When lower tiers look better, the grind feels unrewarding and players
  lose trust in visual signals.
  
### **Solution**
  RARITY VISUAL AUDIT:
  
  Create feature assignment table:
  | Feature             | Common | Uncommon | Rare | Epic | Legendary |
  |---------------------|--------|----------|------|------|-----------|
  | Single material     | Yes    | Yes      | Yes  | Yes  | Yes       |
  | Secondary accent    | No     | Yes      | Yes  | Yes  | Yes       |
  | Third material      | No     | No       | Yes  | Yes  | Yes       |
  | Glow effects        | No     | No       | No   | Yes  | Yes       |
  | Particles           | No     | No       | No   | Yes  | Yes       |
  | Animated parts      | No     | No       | No   | No   | Yes       |
  | Impossible geometry | No     | No       | No   | No   | Yes       |
  
  Review every weapon against table. No exceptions.
  
### **Symptoms**
  - Why does that green look cooler than my purple?
  - Legendary weapons feel underwhelming
  - Players keep lower-tier "cool" weapons
  - Gear progression feels arbitrary
### **Detection Pattern**


## Scale Reference Failure

### **Id**
scale-reference-failure
### **Summary**
Weapons that read wrong relative to character or environment
### **Severity**
high
### **Situation**
  Designing weapons in isolation without character scale reference.
  Sword looks great in concept art, then comically small or large in-game.
  
### **Why**
  Weapons are always seen with characters. A perfectly designed sword
  that's wrong for character proportions looks amateur in-game. The
  weapon-to-character relationship defines power fantasy.
  
### **Solution**
  SCALE REFERENCE PROTOCOL:
  
  1. Always design with character silhouette visible
  2. Establish weapon size categories:
     - Small: Handle to elbow
     - Medium: Handle to shoulder
     - Large: Handle to head height
     - Massive: Handle to above head
  
  3. Test in T-pose, idle pose, and attack pose
  4. Consider camera: FPS weapons seem larger
  
  Reference ratios (third-person):
  - Dagger: 1/3 forearm length
  - Short sword: Forearm length
  - Longsword: Arm length
  - Greatsword: Shoulder to ground
  - Staff: Character height + 20%
  
  Import rough model into engine EARLY.
  
### **Symptoms**
  - That looks huge in the concept art...
  - Weapon clips through character/environment
  - Animations look wrong
  - Power fantasy miscommunicated
### **Detection Pattern**


## Material Language Inconsistency

### **Id**
material-language-inconsistency
### **Summary**
Same materials meaning different things on different weapons
### **Severity**
high
### **Situation**
  Blue glow means ice on this sword but energy on that gun. Gold trim
  means legendary here but ancient origin there. No consistent vocabulary.
  
### **Why**
  Material language teaches players your world. When it's inconsistent,
  every weapon requires re-learning. Players can't make quick judgments
  about damage types, origins, or effects.
  
### **Solution**
  MATERIAL LANGUAGE DOCUMENT:
  
  Create and enforce:
  
  Colors:
  - Blue glow = Ice damage (always)
  - Red glow = Fire damage (always)
  - Purple = Void/Dark damage (always)
  - Gold = Legendary tier OR ancient origin (pick one)
  
  Materials:
  - Crystal = Magical origin
  - Bone = Primal/beast origin
  - Black metal = Corrupted/evil
  - White metal = Blessed/holy
  
  Textures:
  - Smooth metal = Refined, high-tier
  - Rough metal = Crude, low-tier
  - Organic pattern = Living weapon
  
  Document distributed to all weapon designers.
  Review new weapons against doc before approval.
  
### **Symptoms**
  - I thought blue meant ice?
  - Players mis-predict damage types
  - Elemental weapons feel arbitrary
  - No cohesive world-building
### **Detection Pattern**


## First Person Obstruction

### **Id**
first-person-obstruction
### **Summary**
Weapons designed for third-person that block first-person view
### **Severity**
high
### **Situation**
  Wide-blade weapons that obscure center of screen. Elaborate effects
  that blind during combat. Designed to look cool, not to be used.
  
### **Why**
  In first-person, weapons occupy 20-30% of screen real estate constantly.
  If they obstruct view or cause visual fatigue, gameplay suffers. Players
  won't use cool weapons that make them lose fights.
  
### **Solution**
  FIRST-PERSON DESIGN RULES:
  
  Screen obstruction:
  - Weapon body stays in lower 1/3 of screen
  - No element crosses center reticle
  - Scope/sight allows clear view down center
  
  Visual effects:
  - Muzzle flash < 200ms duration
  - No persistent glow crossing reticle
  - Particle effects spawn forward, not up
  
  Ergonomic feel:
  - Reload animations visible without camera move
  - Weapon swap smooth (no screen-covering spin)
  - Iron sights clear (not obstructive geometry)
  
  TEST: Play 30 minutes with weapon. Any eyestrain? Any deaths
  from obstruction? If yes, redesign.
  
### **Symptoms**
  - I can't see anything when I fire
  - Players avoid visually impressive weapons
  - Combat feels obstructed
  - Weapon "gets in the way"
### **Detection Pattern**


## Audio Visual Mismatch

### **Id**
audio-visual-mismatch
### **Summary**
Weapons that look heavy but sound light, or vice versa
### **Severity**
high
### **Situation**
  Massive war hammer that "pings" on impact. Sleek rapier with deep
  "thoom" sound. Visual and audio not aligned on weight/power.
  
### **Why**
  Audio completes the weapon experience. Mismatched audio makes weapons
  feel broken or fake. Players instinctively distrust the experience.
  "It LOOKS powerful but feels weak."
  
### **Solution**
  AUDIO-VISUAL ALIGNMENT:
  
  Heavy weapons (slow, powerful):
  - Deep frequency sounds (100-300Hz base)
  - Long decay/reverb
  - "Thoom", "boom", "crash"
  - Screen shake on impact
  
  Light weapons (fast, precise):
  - Higher frequency sounds (500Hz+ base)
  - Short, crisp decay
  - "Swish", "clink", "ping"
  - Minimal/no screen shake
  
  Energy weapons:
  - Synthesized components
  - Electronic harmonics
  - Match visual energy color with audio "brightness"
  
  DESIGN HANDOFF must include audio direction:
  - Weight class (light/medium/heavy)
  - Material (metal/wood/energy/bone)
  - Power level (weak/medium/powerful/devastating)
  
### **Symptoms**
  - Sounds don't match the weapon
  - Impacts feel unsatisfying
  - Weight feels wrong
  - Players mute combat audio
### **Detection Pattern**


## Impractical Edge Geometry

### **Id**
impractical-edge-geometry
### **Summary**
Blade edges and points that couldn't cut or pierce
### **Severity**
medium
### **Situation**
  Sword with blade edge on the wrong side of curve. Axe with cutting
  edge perpendicular to swing arc. Spear tip at 90-degree angle.
  
### **Why**
  Players intuitively understand how cutting/piercing works. Weapons
  with geometry that wouldn't work break immersion. "How is that
  supposed to cut anything?"
  
### **Solution**
  EDGE GEOMETRY RULES:
  
  Cutting weapons:
  - Edge faces direction of swing arc
  - Curved blades: Outer edge sharpened
  - Edge-to-spine ratio logical
  
  Piercing weapons:
  - Point aligned with thrust direction
  - Taper allows penetration
  - Cross-section supports penetration
  
  Blunt weapons:
  - Contact surface matches swing terminus
  - Weight concentrated at impact point
  - Handle opposite impact face
  
  Quick test: Draw swing arc. Does edge contact target
  at proper angle? If no, redesign.
  
### **Symptoms**
  - How would you even use that?
  - Combat animations look wrong
  - Damage type visually confused
  - Immersion breaks on inspection
### **Detection Pattern**


## Cultural Appropriation Without Research

### **Id**
cultural-appropriation-without-research
### **Summary**
Borrowing cultural weapon aesthetics superficially
### **Severity**
medium
### **Situation**
  "Japanese-inspired" sword with European crossguard. "Viking" axe with
  Chinese dragon motifs. Generic "tribal" weapons matching no culture.
  
### **Why**
  Superficial cultural borrowing appears lazy and can be offensive.
  Players familiar with source cultures notice immediately. It
  undermines the authenticity of your entire world.
  
### **Solution**
  CULTURAL WEAPON RESEARCH:
  
  Before borrowing cultural aesthetics:
  1. Research 5+ real examples from that culture
  2. Understand functional AND decorative elements
  3. Know why design choices exist
  4. Identify what CAN be changed (decoration)
  5. Identify what SHOULDN'T change (function)
  
  Example - Japanese sword integration:
  KEEP: Blade curve, handle length, two-handed grip
  CHANGE: Guard design, habaki, decoration, materials
  
  When creating new cultures:
  - Base on real weapon evolution
  - Internal consistency matters
  - Document your design decisions
  
### **Symptoms**
  - That's not how katanas work
  - Informed players call out mistakes
  - Cultural elements feel random
  - World-building undermined
### **Detection Pattern**


## Telegraph Readability Failure

### **Id**
telegraph-readability-failure
### **Summary**
Weapon shapes that don't communicate attack type
### **Severity**
medium
### **Situation**
  Axe that looks like it should slash but is a thrust weapon. Spear
  visually identical to staff but completely different moveset.
  Shape doesn't match function.
  
### **Why**
  In action games, players read enemy weapons to predict attacks.
  When visual shape doesn't match attack type, players feel cheated.
  "How was I supposed to know it does that?"
  
### **Solution**
  SHAPE-TO-ATTACK LANGUAGE:
  
  Slashing weapons:
  - Long edge visible
  - Curved or wide blade
  - Thin profile (cuts through)
  
  Thrusting weapons:
  - Prominent point
  - Narrow profile
  - Long, straight form
  
  Blunt weapons:
  - Heavy head visible
  - Thick profile
  - Concentrated mass at end
  
  Area/sweep weapons:
  - Wide head or multiple heads
  - Visible arc-creating shape
  - Heavy, momentum-focused
  
  TEST: Show weapon to tester. Ask "How does this attack?"
  If answer doesn't match mechanics, redesign.
  
### **Symptoms**
  - Players surprised by attack patterns
  - Enemy tells feel unfair
  - Weapon/moveset mismatch feedback
  - Combat readability low
### **Detection Pattern**


## Vfx Overdose

### **Id**
vfx-overdose
### **Summary**
Too many particle effects making weapons unreadable
### **Severity**
medium
### **Situation**
  Legendary weapon with so many particles you can't see the weapon.
  Every attack spawns 50 effects. Visual noise overwhelming actual design.
  
### **Why**
  VFX should enhance, not replace design. When particles obscure the
  weapon, players don't form attachment to the object itself. The cool
  factor is fleeting - they remember effects, not weapon.
  
### **Solution**
  VFX RESTRAINT RULES:
  
  Ambient effects (always on):
  - Maximum 3-5 particles visible at once
  - Should not obscure weapon silhouette
  - Lower intensity than attack effects
  
  Attack effects (momentary):
  - Trails: Maximum 2 trails per weapon
  - Impact: Maximum 20 particles, < 500ms
  - Screen effects: Subtle, < 200ms
  
  Escalation by rarity:
  - Epic: Introduce particle effects
  - Legendary: Increase particle count 2x
  - Exotic: Add unique effect type
  
  Never exceed: Weapon design readable at all times.
  
### **Symptoms**
  - What even is that weapon?
  - Silhouette lost in particles
  - Performance issues
  - Players remember effects, not weapons
### **Detection Pattern**


## Power Creep Visual Escalation

### **Id**
power-creep-visual-escalation
### **Summary**
Each content update making weapons visually more extreme
### **Severity**
high
### **Situation**
  Year 1 legendaries look plain next to Year 3 rares. Visual ceiling
  constantly raised. New content must out-flashy previous content.
  
### **Why**
  Unchecked visual escalation breaks rarity hierarchy and makes old
  content feel worthless. Eventually, common weapons look like old
  legendaries, and design space exhausts. The WoW shoulder pad problem.
  
### **Solution**
  VISUAL CEILING DOCTRINE:
  
  1. Define maximum at project start:
     - Max particles per weapon
     - Max materials per weapon
     - Reserved features (floating parts = Exotic only)
  
  2. New content fills gaps, doesn't raise ceiling:
     - New legendary: Different look, same intensity
     - New theme: Varies design, not power-look
  
  3. Audit every release:
     - Does this exceed tier ceiling?
     - Does this make same-tier weapons look weak?
     - If yes: Redesign to fit ceiling
  
  MANTRA: "Different, not more."
  
### **Symptoms**
  - Old legendaries look like new uncommons
  - Constant visual one-upmanship
  - Design space exhausting
  - Player complaint about transmog/cosmetics
### **Detection Pattern**
