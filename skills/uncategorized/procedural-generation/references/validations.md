# Procedural Generation - Validations

## Unseeded Math.random() Usage

### **Id**
unseeded-math-random
### **Description**
  Math.random() is not seedable. For reproducible procedural generation,
  you need a seedable PRNG. Without seeds, you can't debug, share worlds,
  or synchronize multiplayer.
  
### **Pattern**
Math\.random\(\)
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
absent
### **Context Pattern**
generate|procedural|noise|spawn|level|dungeon|terrain|random
### **Message**
  Math.random() detected in procedural generation code. Use a seedable PRNG instead:
  - SplitMix64/Xoshiro for high quality
  - Mulberry32 for simple use cases
  - Custom LCG if you need to match legacy systems
  
### **Severity**
error
### **Autofix**


## Seed Storage/Logging

### **Id**
seed-storage
### **Description**
  Generated content seeds should be stored and/or logged for debugging
  and reproducibility. Without the seed, you can't reproduce bugs.
  
### **Pattern**
seed|worldSeed|levelSeed
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
generate|create|build|spawn
### **Message**
  Ensure seeds are:
  1. Logged on generation (console.log, analytics)
  2. Stored with save data
  3. Displayed to players for sharing
  
### **Severity**
warning
### **Autofix**


## Deterministic Operation Order

### **Id**
deterministic-order
### **Description**
  Random number consumption order must be deterministic. Set/Map iteration,
  Promise.all, and object key order can cause non-determinism.
  
### **Pattern**
new Set|new Map|Object\.keys|Object\.entries|Promise\.all
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
rng|random|seed|generate
### **Message**
  Potential non-determinism detected. Ensure:
  1. Sort arrays before iteration with random
  2. Use arrays instead of Sets/Maps when order matters
  3. Avoid Promise.all when results affect random sequence
  
### **Severity**
warning
### **Autofix**


## Generated Content Validation

### **Id**
generation-validation
### **Description**
  All procedurally generated content that affects gameplay must be validated
  before being shown to players. Unvalidated content can softlock games.
  
### **Pattern**
generate.*\(|create.*Level|build.*Dungeon|spawn.*Room
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
validate|isValid|check|verify|connected|reachable|solvable
### **Message**
  Generated content should be validated for:
  1. Connectivity (all areas reachable)
  2. Completability (can reach exit from spawn)
  3. Required elements present (keys, items)
  4. No softlock conditions
  Have a fallback for when validation fails.
  
### **Severity**
error
### **Autofix**


## Fallback Content Exists

### **Id**
fallback-content
### **Description**
  When procedural generation fails repeatedly, hand-crafted fallback content
  should be used instead of showing broken content.
  
### **Pattern**
fallback|default.*level|backup|predefined
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
generate|failed|invalid|retry
### **Message**
  No fallback content detected. Add:
  1. Hand-crafted backup levels
  2. Known-good seed database
  3. Simplified generation mode
  
### **Severity**
warning
### **Autofix**


## Flood Fill Connectivity Check

### **Id**
connectivity-check
### **Description**
  Generated maps should use flood fill or equivalent to verify all
  floor/walkable tiles are connected.
  
### **Pattern**
flood.*fill|is.*connected|check.*connectivity|bfs|dfs
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
dungeon|level|cave|map|grid
### **Message**
  No connectivity check found. Generated maps may have isolated areas.
  Implement flood fill from spawn to verify all areas are reachable.
  
### **Severity**
warning
### **Autofix**


## Async/Background Generation

### **Id**
async-generation
### **Description**
  Heavy procedural generation should not block the main thread.
  Use Web Workers, requestIdleCallback, or chunked generation.
  
### **Pattern**
for\s*\([^)]*noise|while.*generate|new Array\(\d{4,}
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
async|worker|setTimeout|requestIdleCallback|requestAnimationFrame
### **Message**
  Large generation loop may block main thread. Consider:
  1. Web Workers for heavy computation
  2. requestIdleCallback for time-slicing
  3. Chunked generation across frames
  4. Show loading indicator during generation
  
### **Severity**
warning
### **Autofix**


## Chunk-Based Infinite World

### **Id**
chunk-based-infinite
### **Description**
  Infinite/large worlds should use chunk-based generation to enable
  on-demand loading and memory management.
  
### **Pattern**
infinite|endless|large.*world|open.*world
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
chunk|tile|sector|region|segment|partition
### **Message**
  Large world detected without chunking. Implement:
  1. Coordinate to chunk mapping
  2. Chunk loading/unloading by distance
  3. Chunk caching with LRU eviction
  4. Pre-generation of nearby chunks
  
### **Severity**
warning
### **Autofix**


## Noise Function Caching

### **Id**
noise-caching
### **Description**
  Expensive noise functions called repeatedly with same coordinates should
  be cached or memoized.
  
### **Pattern**
noise\(|fbm\(|perlin\(|simplex\(
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
cache|memo|store|map.*get
### **Message**
  Consider caching noise values for repeated lookups:
  1. Memoize by coordinate hash
  2. Pre-compute heightmaps
  3. Use LOD for distant samples
  
### **Severity**
info
### **Autofix**


## Domain Warping for Natural Terrain

### **Id**
noise-domain-warp
### **Description**
  Raw noise often has visible grid artifacts. Domain warping breaks up
  regularity and creates more organic-looking results.
  
### **Pattern**
noise.*terrain|heightmap|landscape
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
warp|distort|offset|transform
### **Message**
  Consider adding domain warping to break up noise grid artifacts:
  warpedNoise(x, y) = noise(x + noise(x,y), y + noise(x+c,y+c))
  
### **Severity**
info
### **Autofix**


## WFC Backtracking Support

### **Id**
wfc-backtracking
### **Description**
  Wave Function Collapse can reach contradiction states where no valid
  tiles remain. Backtracking or restart logic is needed.
  
### **Pattern**
wfc|wave.*function.*collapse|entropy
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
backtrack|retry|history|undo|restore|restart
### **Message**
  WFC detected without visible backtracking. Implement:
  1. History stack for backtracking
  2. Max backtrack limit
  3. Restart on contradiction
  4. Fallback pattern for repeated failures
  
### **Severity**
warning
### **Autofix**


## L-System Growth Limits

### **Id**
l-system-limits
### **Description**
  L-systems grow exponentially. Without limits, they can crash the browser.
  
### **Pattern**
l-system|axiom|rewrite|production
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
max.*iteration|max.*length|limit|cap
### **Message**
  L-system detected without visible limits. Add:
  1. Maximum iteration count
  2. Maximum string length
  3. Early termination on overflow
  
### **Severity**
warning
### **Autofix**


## Markov Chain Training Size

### **Id**
markov-training-data
### **Description**
  Markov chains need sufficient training data. Order-2 chains need 50+
  examples; order-3 needs 200+.
  
### **Pattern**
markov|chain|train|ngram
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
train|example|corpus|data
### **Message**
  Ensure Markov chain has sufficient training data:
  - Order 1: 20+ examples
  - Order 2: 50+ examples
  - Order 3: 200+ examples
  - Higher orders need exponentially more
  
### **Severity**
info
### **Autofix**


## Large Coordinate Handling

### **Id**
coordinate-overflow
### **Description**
  Large world coordinates can overflow integers or lose float precision.
  Use chunk-local coordinates for rendering.
  
### **Pattern**
worldX|worldY|globalPos|absolutePos
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
chunk|local|relative|origin|BigInt
### **Message**
  Large coordinates detected. Ensure:
  1. Rendering uses camera-relative coords
  2. Chunk coordinates are integers
  3. Local positions within chunks
  4. Origin recentering for far positions
  
### **Severity**
warning
### **Autofix**


## Float Accumulation Errors

### **Id**
float-accumulation
### **Description**
  Accumulated floating-point operations diverge across platforms.
  Calculate positions from integers where possible.
  
### **Pattern**
\+=.*0\.\d|position.*\+=
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
generate|procedural|world
### **Message**
  Float accumulation may cause platform divergence. Calculate from integers:
  BAD: pos += 0.001
  GOOD: pos = step * stepSize
  
### **Severity**
info
### **Autofix**


## Content Variety System

### **Id**
content-variety
### **Description**
  Procedural content can feel samey without explicit variety mechanisms.
  Use stratified sampling and rare content injection.
  
### **Pattern**
generate|spawn|create.*room|place
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
rare|common|weight|tier|variety|unique|special
### **Message**
  Consider adding variety mechanisms:
  1. Weighted rarity tiers (common/uncommon/rare)
  2. Bad luck protection (increasing rare chance)
  3. Guaranteed unique elements per level
  4. Level "moods" or themes
  
### **Severity**
info
### **Autofix**


## Biome Transition Smoothing

### **Id**
biome-blending
### **Description**
  Hard biome boundaries are immersion-breaking. Blend biomes at transitions.
  
### **Pattern**
biome|climate|zone
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
blend|transition|gradient|smooth|interpolate
### **Message**
  Biome system detected. Consider smooth transitions:
  1. Sample biomes at low frequency
  2. Blend properties in transition zones
  3. Define valid transition pairs
  4. Avoid impossible adjacencies (snow next to desert)
  
### **Severity**
info
### **Autofix**


## Player-Visible Seed

### **Id**
seed-display
### **Description**
  Players should be able to see and share world seeds. Display on
  pause menu or world select.
  
### **Pattern**
seed|worldSeed
### **File Glob**
**/*.{js,ts,jsx,tsx,svelte,vue}
### **Match**
present
### **Context Pattern**
display|show|render|UI|text
### **Message**
  Consider displaying seed to players for sharing.
  Human-friendly format: "dragon-castle-42" > "847293847"
  
### **Severity**
info
### **Autofix**


## Generation Quality Metrics

### **Id**
generation-metrics
### **Description**
  Track generation metrics to identify problems and improve quality.
  
### **Pattern**
generate|create.*level
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
metrics|analytics|telemetry|track|log
### **Message**
  Consider tracking generation metrics:
  - First-attempt success rate
  - Average retry count
  - Fallback usage rate
  - Failed seed patterns
  
### **Severity**
info
### **Autofix**


## Generation Debug Visualization

### **Id**
debug-visualization
### **Description**
  Debug visualization helps tune and debug procedural systems.
  
### **Pattern**
generate|noise|dungeon
### **File Glob**
**/*.{js,ts,jsx,tsx}
### **Match**
present
### **Context Pattern**
debug|visualize|preview|canvas
### **Message**
  Consider adding debug visualization:
  1. Noise value heatmaps
  2. Room/corridor overlays
  3. Validation step display
  4. Parameter sliders (dat.GUI)
  
### **Severity**
info
### **Autofix**
