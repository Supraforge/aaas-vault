#!/bin/bash
# Batch composite script for inspiration assets - adds logos to all images

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="/Users/user/.gemini/[PROJECT_NAME]"
INSPIRATION_DIR="$PROJECT_ROOT/assets/brand/inspiration"
OUTPUT_DIR="$PROJECT_ROOT/assets/brand/final"

# Logo paths
SF_DARK="$PROJECT_ROOT/website/assets/supra-forge-logo-dark.svg"
SF_LIGHT="$PROJECT_ROOT/website/assets/supra-forge-logo.svg"
[PROJECT_NAME]_DARK="$PROJECT_ROOT/website/assets/[PROJECT_NAME]-logo-dark.svg"
[PROJECT_NAME]_LIGHT="$PROJECT_ROOT/website/assets/[PROJECT_NAME]-logo.svg"

# Create output directories
mkdir -p "$OUTPUT_DIR/supraforge"
mkdir -p "$OUTPUT_DIR/[PROJECT_NAME]"

# Function to composite
composite() {
    local input=$1
    local logo=$2
    local output=$3
    local scale=${4:-0.15}
    node "$SCRIPT_DIR/composite_logo.js" "$input" "$logo" "$output" "bottom-left" "$scale"
}

echo "=== Compositing Inspiration Assets with Logos ==="

# Process all subdirectories
for category in hmi factory compliance matrix safety; do
    echo ""
    echo "Processing $category assets..."

    # Dark images use dark logo (white text)
    for img in "$INSPIRATION_DIR/$category"/*_dark_*.png; do
        if [ -f "$img" ]; then
            filename=$(basename "$img")
            echo "  - $filename (dark)"
            composite "$img" "$SF_DARK" "$OUTPUT_DIR/supraforge/sf_${category}_$filename" 0.18
            composite "$img" "$[PROJECT_NAME]_DARK" "$OUTPUT_DIR/[PROJECT_NAME]/[PROJECT_NAME]_${category}_$filename" 0.18
        fi
    done

    # Light images use light logo (dark text)
    for img in "$INSPIRATION_DIR/$category"/*_light_*.png; do
        if [ -f "$img" ]; then
            filename=$(basename "$img")
            echo "  - $filename (light)"
            composite "$img" "$SF_LIGHT" "$OUTPUT_DIR/supraforge/sf_${category}_$filename" 0.18
            composite "$img" "$[PROJECT_NAME]_LIGHT" "$OUTPUT_DIR/[PROJECT_NAME]/[PROJECT_NAME]_${category}_$filename" 0.18
        fi
    done
done

echo ""
echo "=== Done! ==="
echo "Branded assets saved to: $OUTPUT_DIR"
echo ""
echo "SUPRA FORGE branded: $(ls -1 $OUTPUT_DIR/supraforge/*.png 2>/dev/null | wc -l) images"
echo "[PROJECT_NAME] branded: $(ls -1 $OUTPUT_DIR/[PROJECT_NAME]/*.png 2>/dev/null | wc -l) images"
