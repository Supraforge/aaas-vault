# Weapon Design - Validations

## Silhouette Test Documentation

### **Id**
silhouette-test-documented
### **Severity**
error
### **Type**
checklist
### **Description**
  Every weapon design must include silhouette test results
  
### **Checklist**
  - Black silhouette version created
  - Readable at 100px height
  - Readable at 50px height
  - Readable at 20px height (for gameplay distance)
  - Distinguishable from other weapons in same class
### **Applies To**
  - concept-art
  - weapon-design-doc

## Arsenal Silhouette Differentiation

### **Id**
silhouette-differentiation
### **Severity**
error
### **Type**
checklist
### **Description**
  All weapons in the same category must have distinct silhouettes
  
### **Checklist**
  - Each weapon has unique primary shape
  - No two weapons share identical guard type
  - No two weapons share identical blade width category
  - 1-inch silhouette test passed by external reviewer
  - Weapon can be named by silhouette alone
### **Applies To**
  - weapon-arsenal
  - weapon-catalog

## Character Scale Reference

### **Id**
scale-reference-included
### **Severity**
error
### **Type**
checklist
### **Description**
  Weapon designs must include character scale reference
  
### **Checklist**
  - Character silhouette included in design
  - Grip-to-hand proportion verified
  - Overall length relative to character documented
  - Size category assigned (small/medium/large/massive)
  - Tested in T-pose, idle, and attack pose
### **Applies To**
  - concept-art
  - weapon-design-doc

## Grip to Blade Ratio Check

### **Id**
grip-to-blade-ratio
### **Severity**
warning
### **Type**
checklist
### **Description**
  Weapon proportions must be physically plausible
  
### **Checklist**
  - One-handed: grip 6-8 inches OR justified exception
  - Two-handed: grip 12+ inches OR counterweight present
  - Massive weapons: grip minimum 1/4 blade length
  - Balance point considered in design
  - Lever arm mechanically logical
### **Applies To**
  - concept-art
  - weapon-design-doc

## Rarity Tier Assignment

### **Id**
rarity-tier-documented
### **Severity**
error
### **Type**
checklist
### **Description**
  Every weapon must have documented rarity tier
  
### **Checklist**
  - Rarity tier explicitly assigned
  - Visual features match tier allowance
  - No forbidden features for tier present
  - Compared against tier ceiling document
  - Escalation from lower tier visible
### **Applies To**
  - weapon-design-doc

## Rarity Feature Compliance

### **Id**
rarity-feature-compliance
### **Severity**
error
### **Type**
checklist
### **Description**
  Weapon visual features must comply with rarity tier limits
  
### **Checklist**
  - Common: Single material only
  - Uncommon: Maximum 2 materials
  - Rare: Maximum 3 materials, no particles
  - Epic: Particles allowed, no floating geometry
  - Legendary: Floating geometry allowed, max intensity
  - Exotic: Unique features reserved for tier
### **Applies To**
  - weapon-design-doc
  - weapon-catalog

## Material Language Consistency

### **Id**
material-language-consistency
### **Severity**
error
### **Type**
checklist
### **Description**
  Material usage must match established visual language
  
### **Checklist**
  - Colors match damage type documentation
  - Materials match origin/culture documentation
  - Glow colors match element assignments
  - No conflicting material meanings
  - Cross-referenced with material language doc
### **Applies To**
  - weapon-design-doc

## Damage Type Visual Communication

### **Id**
damage-type-visualization
### **Severity**
warning
### **Type**
checklist
### **Description**
  Elemental/damage types must be visually distinct
  
### **Checklist**
  - Fire: Red/orange glow, ember particles
  - Ice: Blue/white, crystalline, frost
  - Lightning: Yellow/white, arcs, conductive
  - Poison: Green, dripping, organic
  - Holy: White/gold, radiant, clean
  - Dark: Purple/black, void, corrupted
### **Applies To**
  - elemental-weapon
  - damage-type-weapon

## First-Person Camera Optimization

### **Id**
first-person-optimization
### **Severity**
error
### **Type**
checklist
### **Description**
  First-person weapons must not obstruct gameplay
  
### **Checklist**
  - Weapon body in lower 1/3 of screen
  - No elements crossing center reticle
  - Muzzle flash duration under 200ms
  - Reload animation visible without camera shift
  - Iron sights allow clear center view
  - 30-minute gameplay test passed (no eyestrain)
### **Applies To**
  - fps-weapon
  - first-person-weapon

## Third-Person Camera Optimization

### **Id**
third-person-optimization
### **Severity**
error
### **Type**
checklist
### **Description**
  Third-person weapons must read at distance
  
### **Checklist**
  - 360-degree silhouette readable
  - Sheathed/back view designed
  - Scale communicates power level
  - Attack arc suggested by shape
  - Idle pose weapon visible
### **Applies To**
  - tps-weapon
  - third-person-weapon

## Audio Direction Documentation

### **Id**
audio-direction-documented
### **Severity**
warning
### **Type**
checklist
### **Description**
  Weapon design must include audio direction for sound designer
  
### **Checklist**
  - Weight class specified (light/medium/heavy)
  - Material composition listed
  - Damage type documented
  - Power level indicated
  - Expected sound profile described
  - Reference sounds provided if available
### **Applies To**
  - weapon-design-doc

## VFX Anchor Point Documentation

### **Id**
vfx-anchor-points
### **Severity**
warning
### **Type**
checklist
### **Description**
  Weapon design must include VFX anchor points
  
### **Checklist**
  - Muzzle/emission point marked
  - Trail origin and end points marked
  - Impact effect spawn point identified
  - Ambient effect attachment locations
  - Particle intensity level specified
  - Color palette for effects documented
### **Applies To**
  - weapon-design-doc

## Cultural Reference Research

### **Id**
cultural-reference-research
### **Severity**
info
### **Type**
checklist
### **Description**
  Culturally-inspired weapons must show research
  
### **Checklist**
  - 5+ real-world reference examples documented
  - Functional elements identified and preserved
  - Decorative elements identified as changeable
  - Cultural significance understood
  - Fantasy modifications justified
### **Applies To**
  - cultural-weapon
  - historical-inspired

## Attack Type Visual Telegraph

### **Id**
attack-type-telegraph
### **Severity**
warning
### **Type**
checklist
### **Description**
  Weapon shape must communicate attack type
  
### **Checklist**
  - Slashing: Long edge visible, curved/wide blade
  - Thrusting: Prominent point, narrow profile
  - Blunt: Heavy head, thick profile
  - Area: Wide/multiple heads
  - External tester correctly predicted attack type
### **Applies To**
  - melee-weapon
  - action-game-weapon

## Legendary Weapon Requirements

### **Id**
legendary-weapon-requirements
### **Severity**
error
### **Type**
checklist
### **Description**
  Legendary weapons must meet enhanced standards
  
### **Checklist**
  - Unique silhouette (not variation of existing)
  - Lore/story significance documented
  - Signature visual feature identified
  - Audio signature specified
  - VFX exceed epic tier
  - Instantly recognizable in 1-second glance
### **Applies To**
  - legendary-weapon
  - exotic-weapon

## Exotic Weapon Uniqueness

### **Id**
exotic-uniqueness
### **Severity**
error
### **Type**
checklist
### **Description**
  Exotic weapons must have truly unique features
  
### **Checklist**
  - Feature reserved for exotic tier present
  - No similar feature on any lower-tier weapon
  - Transforms or has alternate visual state
  - Unique gameplay-affecting visual element
  - Would be recognizable from across the room
### **Applies To**
  - exotic-weapon
  - mythic-weapon

## Visual Ceiling Compliance

### **Id**
visual-ceiling-compliance
### **Severity**
error
### **Type**
checklist
### **Description**
  New weapons must not exceed established visual ceiling
  
### **Checklist**
  - Compared against visual ceiling document
  - Particle count within tier maximum
  - Material count within tier maximum
  - No reserved features used below tier
  - Does not make same-tier weapons look weak
  - Follows 'different, not more' principle
### **Applies To**
  - new-weapon
  - dlc-weapon
  - seasonal-weapon

## 3D Modeling Handoff Completeness

### **Id**
modeling-handoff-complete
### **Severity**
error
### **Type**
checklist
### **Description**
  Handoff to 3D modeling must include all required assets
  
### **Checklist**
  - Front view concept
  - Side view concept
  - Top view (if complex geometry)
  - 3/4 beauty angle
  - Material callouts with finish specs
  - Scale reference with character
  - Polygon budget assigned
  - LOD requirements documented
### **Applies To**
  - production-handoff

## Combat Design Handoff Completeness

### **Id**
combat-design-handoff-complete
### **Severity**
warning
### **Type**
checklist
### **Description**
  Handoff to combat design must include visual-feel guidance
  
### **Checklist**
  - Intended weight class
  - Expected swing speed visual
  - Damage type visual elements
  - Rarity tier and power level
  - Silhouette attack arc suggestion
  - Animation reference if available
### **Applies To**
  - combat-handoff