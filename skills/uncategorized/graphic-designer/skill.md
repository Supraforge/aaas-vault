# Graphic Designer Skill

Image editing capabilities for quick design tasks directly from Claude Code.

## Trigger Keywords

- `edit image`, `image edit`, `photo edit`
- `remove background`, `background removal`, `cut out`, `no bg`
- `resize image`, `scale image`, `make smaller`, `make larger`
- `crop image`, `trim image`
- `adjust colors`, `brightness`, `contrast`, `saturation`
- `convert to png`, `convert to jpg`, `change format`

## Commands

- `/graphic-designer` — Interactive image editing session
- `/remove-bg <path>` — Quick background removal
- `/resize <path> --width <n>` — Quick resize
- `/image-info <path>` — Get image details

## Tool Location

```
~/.claude/skills/graphic-designer/tools/edit_image.py
```

## Operations

### 1. Remove Background

Remove background from any image using AI (rembg).

```bash
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py remove-bg <input> [-o output.png]
```

**Examples:**
```bash
# Basic removal - creates photo_nobg.png
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py remove-bg photo.jpg

# Custom output path
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py remove-bg product.jpg -o product-clean.png
```

### 2. Resize Image

Resize by width, height, or scale factor. Maintains aspect ratio by default.

```bash
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py resize <input> [options]
```

**Options:**
- `--width <px>` — Target width
- `--height <px>` — Target height
- `--scale <factor>` — Scale factor (0.5 = half, 2.0 = double)
- `--no-aspect` — Don't maintain aspect ratio
- `-o <path>` — Output path

**Examples:**
```bash
# Resize to 800px wide (maintains aspect)
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py resize banner.png --width 800

# Scale down to 50%
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py resize photo.jpg --scale 0.5

# Exact dimensions (no aspect)
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py resize thumb.jpg --width 200 --height 200 --no-aspect
```

### 3. Crop Image

Crop by coordinates or dimensions.

```bash
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py crop <input> [options]
```

**Options:**
- `--left <px>` — Left coordinate (default: 0)
- `--top <px>` — Top coordinate (default: 0)
- `--right <px>` — Right coordinate
- `--bottom <px>` — Bottom coordinate
- `--width <px>` — Crop width (alternative to right)
- `--height <px>` — Crop height (alternative to bottom)
- `-o <path>` — Output path

**Examples:**
```bash
# Crop 400x300 from top-left corner
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py crop photo.jpg --width 400 --height 300

# Crop from specific position
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py crop photo.jpg --left 100 --top 50 --width 600 --height 400
```

### 4. Adjust Colors

Adjust brightness, contrast, saturation, and sharpness.

```bash
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py colors <input> [options]
```

**Options:**
- `--brightness <float>` — 1.0 = no change, >1 = brighter, <1 = darker
- `--contrast <float>` — 1.0 = no change, >1 = more contrast
- `--saturation <float>` — 1.0 = no change, 0 = grayscale, >1 = more vivid
- `--sharpness <float>` — 1.0 = no change, >1 = sharper
- `-o <path>` — Output path

**Examples:**
```bash
# Brighten and increase contrast
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py colors dark-photo.jpg --brightness 1.3 --contrast 1.1

# Desaturate (make less colorful)
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py colors vivid.jpg --saturation 0.5

# Make grayscale
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py colors photo.jpg --saturation 0 -o photo-bw.jpg
```

### 5. Convert Format

Convert between PNG and JPG formats.

```bash
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py convert <input> --format <fmt> [options]
```

**Options:**
- `--format <fmt>` — Target format: `png` or `jpg`
- `--quality <1-100>` — JPEG quality (default: 95)
- `-o <path>` — Output path

**Examples:**
```bash
# PNG to JPG
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py convert screenshot.png --format jpg

# JPG to PNG (for transparency support)
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py convert photo.jpg --format png

# Lower quality for smaller file
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py convert large.png --format jpg --quality 70
```

### 6. Get Image Info

Display image metadata and dimensions.

```bash
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py info <input>
```

## Batch Operations

For multiple images, use shell loops:

```bash
# Remove background from all JPGs in folder
for f in *.jpg; do python3 ~/.claude/skills/graphic-designer/tools/edit_image.py remove-bg "$f"; done

# Resize all images to max 1200px wide
for f in *.{jpg,png}; do python3 ~/.claude/skills/graphic-designer/tools/edit_image.py resize "$f" --width 1200; done
```

## Common Workflows

### Product Photo Cleanup
```bash
# 1. Remove background
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py remove-bg product.jpg -o product-clean.png

# 2. Resize to standard size
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py resize product-clean.png --width 1000 -o product-final.png
```

### Social Media Post
```bash
# 1. Resize to Instagram square
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py resize photo.jpg --width 1080 --height 1080 --no-aspect

# 2. Boost colors for engagement
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py colors photo_resized.jpg --saturation 1.2 --contrast 1.1
```

### Web Optimization
```bash
# Convert PNG to compressed JPG
python3 ~/.claude/skills/graphic-designer/tools/edit_image.py convert hero.png --format jpg --quality 80 -o hero-web.jpg
```

## Usage Patterns

When user asks for image editing:

1. **First, get image info** to understand what we're working with
2. **Confirm the operation** and output location
3. **Execute the edit** using the appropriate command
4. **Verify the result** by checking the output file exists

When multiple operations are needed, chain them in sequence, using the output of one as input to the next.

## Dependencies

- Python 3.8+
- Pillow (`pip install Pillow`)
- rembg (`pip install rembg`) — for background removal

All dependencies should already be installed on this system.
