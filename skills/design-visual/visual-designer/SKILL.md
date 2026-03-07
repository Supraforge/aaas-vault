---
name: visual-designer
description: >-
  Generate UI mockups, icons, and placeholder images using multiple backends:
  Puter.js (free) or Google Vertex AI Imagen (high quality). Use when user needs
  visual assets, mockups, or AI-generated images.
triggers:
  - generate an icon
  - create a placeholder image
  - mockup a UI
  - generate image
  - visual asset
  - free image generation
  - puter
  - flux
  - imagen
  - vertex ai
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Visual Designer

AI image generation with multiple backends:

- **Puter.js** (Flux.1 Schnell) - Free, fast, no API key required
- **Google Vertex AI** (Imagen 3) - High quality, requires GCP project

## Capabilities

- Generate icons and UI elements
- Create placeholder images for mockups
- Generate visual assets for presentations
- Produce concept art and illustrations
- Create social media graphics
- Generate product mockups

## Quick Start

### Option A: Puter.js (Free)

```bash
# Ensure Node.js is installed
node --version

# Install dependencies (from project root)
npm install @heyputer/puter.js dotenv

# Set PUTER_AUTH_TOKEN in .env (get from puter.com)
echo "PUTER_AUTH_TOKEN=your_token_here" >> .env

# Generate an image
node skills/visual-designer/scripts/generate_image.js "a minimalist rocket icon, flat design" "rocket_icon.png"
```

### Option B: Google Vertex AI (High Quality)

```bash
# Ensure gcloud CLI is authenticated
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com

# Generate an image
node skills/visual-designer/scripts/generate_image_vertex.js "premium product mockup, professional photography" "mockup.png"
```

## Core Workflows

### 1. Generate UI Icon
```bash
node skills/visual-designer/scripts/generate_image.js \
  "minimalist [object] icon, flat design, [color] gradient, suitable for app UI" \
  "icons/[name].png"
```

### 2. Generate Mockup
```bash
node skills/visual-designer/scripts/generate_image.js \
  "professional UI mockup of [description], modern design, clean layout" \
  "mockups/[name].png"
```

### 3. Generate Placeholder
```bash
node skills/visual-designer/scripts/generate_image.js \
  "[description], professional photography style" \
  "placeholders/[name].png"
```

## Script Reference

### generate_image.js (Puter.js)

**Usage:**
```bash
node scripts/generate_image.js "<prompt>" [output_filename]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| prompt | Yes | Text description of the image to generate |
| output_filename | No | Output path (default: `generated_asset.png`) |

**Requirements:**
- `PUTER_AUTH_TOKEN` in `.env` file
- `@heyputer/puter.js` and `dotenv` packages installed

---

### generate_image_vertex.js (Google Vertex AI)

**Usage:**
```bash
node scripts/generate_image_vertex.js "<prompt>" [output_filename]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| prompt | Yes | Text description of the image to generate |
| output_filename | No | Output path (default: `generated_asset.png`) |

**Requirements:**
- `gcloud` CLI authenticated
- Vertex AI API enabled on project
- Project configured: `gcloud config set project PROJECT_ID`

**Output:**
- Saves PNG image to specified path
- Logs generation status to console

## Prompt Tips

### For Icons
- Include: "minimalist", "flat design", "vector style"
- Specify colors: "blue gradient", "monochrome", "brand colors"
- Add context: "suitable for app UI", "web icon"

### For Mockups
- Include: "professional", "modern design", "clean layout"
- Specify type: "dashboard", "mobile app", "landing page"
- Add details: "with navigation", "showing data charts"

### For Placeholders
- Include: "professional photography", "high quality"
- Specify subject: "business meeting", "product shot", "team photo"
- Add mood: "bright and optimistic", "corporate", "casual"

## Model Information

### Puter.js Backend

| Property | Value |
| -------- | ----- |
| Model | Flux.1 Schnell (black-forest-labs/FLUX.1-schnell) |
| Provider | Puter.js |
| Speed | Fast (~5-15 seconds) |
| Quality | Good for mockups and prototypes |
| Cost | Free (requires Puter account) |

### Vertex AI Backend

| Property | Value |
| -------- | ----- |
| Model | Imagen 3 (imagen-3.0-generate-001) |
| Provider | Google Cloud Vertex AI |
| Speed | Medium (~10-30 seconds) |
| Quality | High - production ready |
| Cost | Pay-per-use (GCP billing) |
| Aspect Ratios | 1:1 (default), configurable |

## Limitations

**Puter.js:**

- Image resolution may be limited by free tier
- No fine-tuning or LoRA support
- Rate limits may apply on heavy usage
- Requires Puter.com account and auth token

**Vertex AI:**

- Requires GCP project with billing enabled
- Quota limits (default ~10 images/minute)
- Pay-per-use pricing applies

**Both:**

- Requires internet connection
- Best results with detailed, specific prompts

## Troubleshooting

| Problem | Backend | Solution |
| ------- | ------- | -------- |
| "Module not found" | Puter | Run `npm install @heyputer/puter.js dotenv` |
| "PUTER_AUTH_TOKEN required" | Puter | Add token to `.env` file |
| "Network error" | Both | Check internet connection |
| "gcloud auth" error | Vertex | Run `gcloud auth login` |
| 429 quota exceeded | Vertex | Wait for quota reset or request increase |
| Low quality output | Both | Refine prompt with more specific descriptors |

---

## Guided Discovery Process (REQUIRED)

**Every new campaign must follow this discovery-first workflow.** Do NOT default to previous patterns.

### Why This Matters

The assistant tends to fall back into the same creative patterns:
- Same mockup styles (Mac + iPhone)
- Same color approaches (dark + gold gradient)
- Same carousel structures

This workflow forces fresh creative exploration for each campaign.

### Phase 1: Context Loading

Before asking ANY questions, read these documents:

```bash
# Load brand context
context/brand.md              # Core brand identity
context/brand_strategy.md     # Voice, messaging, positioning
context/sf_brand_strategy.md  # Visual identity system
context/goals.md              # Current business objectives
```

Extract:
- Brand voice characteristics
- Visual identity rules
- Current business priorities
- Target audience definitions

### Phase 2: Campaign Discovery Questions

**Ask the user (do NOT assume):**

1. What's the campaign goal? (awareness, conversion, engagement, thought leadership)
2. Who exactly is the audience for THIS campaign?
3. What's the key message? (one thing they should remember)
4. What emotion should it evoke? (trust, urgency, curiosity, excitement)
5. Any specific constraints? (platform, timeline, existing assets)

### Phase 3: Creative Exploration

**Research NEW directions based on context + goals:**

1. Search for current trends in the relevant space
2. Look at what competitors/peers are doing NOW
3. Find inspiration from adjacent industries
4. Propose 2-3 DIFFERENT creative directions:
   - Direction A: [describe approach, mood, visual style]
   - Direction B: [different approach, contrast to A]
   - Direction C: [experimental/bold option]

### Phase 4: User Selection & Brief Generation

1. Present options with reasoning
2. User selects or combines directions
3. Generate brief that explicitly states:
   - Why this direction was chosen
   - What makes it DIFFERENT from previous campaigns
   - Specific visual treatments (not defaults)

### Phase 5: Asset Generation

1. Use `--clean` flag (fresh start)
2. Follow brief specifications exactly
3. If brief says "browser mockup" don't default to "Mac + iPhone"
4. Verify outputs match the NEW direction

---

## Content Brief Workflow

A structured, research-first content creation process for producing brand-aligned visual assets.

### Overview

1. **Define** - Create a content brief with copy, audience, and visual specifications
2. **Capture** - Take screenshots of website sections
3. **Generate** - Create mockups with device frames and backgrounds
4. **Brand** - Composite logos onto all assets
5. **Publish** - Review and post to social media

### Quick Start: Batch Generation

```bash
# Generate all assets from a content brief
node skills/visual-designer/scripts/batch_from_brief.js "context/content_briefs/2025-02-15_website-launch.md"

# Dry run to see what would be generated
node skills/visual-designer/scripts/batch_from_brief.js "context/content_briefs/my-campaign.md" --dry-run
```

### Content Brief Template

Create briefs in `context/content_briefs/`:

```bash
# Copy template for new campaign
cp context/content_briefs/_template.md context/content_briefs/YYYY-MM-DD_campaign-name.md
```

See `_example_website_launch.md` for a complete example.

---

## Mockup Generation Scripts

### screenshot_sections.js

Captures multiple sections of a website with dark/light theme support.

```bash
node scripts/screenshot_sections.js "https://example.com" "./screenshots" "dark"
```

**Arguments:**
| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| url | No | supra-forge.com | Website URL to capture |
| outputDir | No | ./screenshots | Output directory |
| colorScheme | No | dark | Theme: `dark` or `light` |

**Outputs:**
- `hero_[theme].png` - Hero section (1920x1080 @2x)
- `step_section_[theme].png` - Scrolled step section
- `full_[theme].png` - Full page screenshot
- `mobile_[theme].png` - Mobile viewport (390x844 @3x)

**Requirements:** `puppeteer` package

---

### create_mac_iphone_mockup.js

Creates premium Mac + iPhone combined device mockups.

```bash
node scripts/create_mac_iphone_mockup.js \
  "screenshots/hero_dark.png" \
  "screenshots/mobile_dark.png" \
  "output/mockup.png" \
  "dark"
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| desktopScreenshot | Yes | Desktop screenshot path |
| mobileScreenshot | Yes | Mobile screenshot path |
| outputPath | Yes | Output file path |
| theme | No | `dark` (default) or `light` |

**Output:** 1200x1200 PNG with:
- MacBook Pro frame with shadow
- iPhone with Dynamic Island
- Gradient background with gold/blue accent glows

**Requirements:** `sharp` package

---

### create_browser_mockup.js

Creates macOS-style browser window mockups.

```bash
node scripts/create_browser_mockup.js \
  "screenshots/hero_dark.png" \
  "output/browser_mockup.png" \
  "dark"
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| screenshot | Yes | Screenshot to embed |
| outputPath | Yes | Output file path |
| theme | No | `dark` (default) or `light` |

**Output:** Browser window with traffic light buttons and subtle shadow.

---

### create_gradient_mockup.js

Creates premium gradient background mockups.

```bash
node scripts/create_gradient_mockup.js \
  "screenshots/step_section_dark.png" \
  "output/gradient_mockup.png" \
  "gold"
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| screenshot | Yes | Screenshot to embed |
| outputPath | Yes | Output file path |
| gradientType | No | `gold`, `blue`, or `mixed` |

**Output:** 1200x1200 PNG with brand-aligned gradient background.

---

### composite_logo.js

Overlays SVG logos onto images with positioning and scaling.

```bash
node scripts/composite_logo.js \
  "input.png" \
  "website/assets/supra-forge-logo-dark.svg" \
  "output_branded.png" \
  "bottom-left" \
  "0.16"
```

**Arguments:**
| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| inputImage | Yes | - | Base image path |
| logoSvg | Yes | - | SVG logo path |
| outputPath | Yes | - | Output file path |
| position | No | bottom-left | Position: `bottom-left`, `bottom-right`, `top-left`, `top-right`, `center` |
| scale | No | 0.2 | Logo scale relative to image width |

**Logo Files:**
- Dark backgrounds: `supra-forge-logo-dark.svg`, `[PROJECT_NAME]-logo-dark.svg`
- Light backgrounds: `supra-forge-logo.svg`, `[PROJECT_NAME]-logo.svg`

---

### batch_from_brief.js

Reads a content brief and auto-generates all specified assets.

```bash
node scripts/batch_from_brief.js "context/content_briefs/campaign.md" [--dry-run]
```

**Process:**
1. Parses brief for campaign name, visual specs, carousel slides
2. Captures screenshots from landing page URL (if provided)
3. Generates mockups based on device/style specifications
4. Creates carousel slide variations
5. Composites brand logo onto all assets
6. Outputs to `assets/brand/campaigns/<campaign-name>/`

**Options:**
| Flag | Description |
|------|-------------|
| --dry-run | Preview what would be generated without executing |

---

## AI Image Generation: HARD RULES

⚠️ **CRITICAL: NO TEXT IN AI IMAGES**

All AI-generated text is unusable. The `generate_image_vertex.js` script enforces this automatically by appending a no-text suffix to ALL prompts:

```javascript
// HARD-CODED - Cannot be overridden
const NO_TEXT_SUFFIX = ', absolutely no text, no letters, no words...';
```

**Workaround for text in images:**
1. Generate text-free AI backgrounds
2. Use Sharp.js or design tools to composite text layers
3. Or use real screenshots with actual rendered text

---

## Complete Workflow Example

```bash
# 1. Create content brief
cp context/content_briefs/_template.md context/content_briefs/2025-02-15_product-launch.md
# Edit the brief with campaign details...

# 2. Capture website screenshots
node skills/visual-designer/scripts/screenshot_sections.js \
  "https://supra-forge.com" \
  "assets/brand/social/screenshots" \
  "dark"

# 3. Generate mockups
node skills/visual-designer/scripts/create_mac_iphone_mockup.js \
  "assets/brand/social/screenshots/hero_dark.png" \
  "assets/brand/social/screenshots/mobile_dark.png" \
  "assets/brand/campaigns/product-launch/cover.png" \
  "dark"

# 4. Add logo branding
node skills/visual-designer/scripts/composite_logo.js \
  "assets/brand/campaigns/product-launch/cover.png" \
  "website/assets/supra-forge-logo-dark.svg" \
  "assets/brand/campaigns/product-launch/cover_branded.png" \
  "bottom-left" \
  "0.16"

# OR: Run everything automatically from the brief
node skills/visual-designer/scripts/batch_from_brief.js \
  "context/content_briefs/2025-02-15_product-launch.md"
```

---

## Related Skills

Works well with: `brand-designer`, `ui-ux-designer`, `canvas-design`, `content-creator`

## Keywords

image generation, AI art, mockup, icon, placeholder, visual asset, puter, flux, vertex ai, imagen, google cloud, ui design, content brief, carousel, linkedin, social media, device mockup, screenshot, branding
