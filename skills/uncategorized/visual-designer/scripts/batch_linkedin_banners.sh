#!/bin/bash
# Batch process LinkedIn banners - crop and add logos

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="/Users/user/.gemini/[PROJECT_NAME]"
LINKEDIN_DIR="$PROJECT_ROOT/assets/brand/linkedin"

# Logo paths
SF_DARK="$PROJECT_ROOT/website/assets/supra-forge-logo-dark.svg"
SF_LIGHT="$PROJECT_ROOT/website/assets/supra-forge-logo.svg"
[PROJECT_NAME]_DARK="$PROJECT_ROOT/website/assets/[PROJECT_NAME]-logo-dark.svg"
[PROJECT_NAME]_LIGHT="$PROJECT_ROOT/website/assets/[PROJECT_NAME]-logo.svg"

# Create output directories
mkdir -p "$LINKEDIN_DIR/cropped"
mkdir -p "$LINKEDIN_DIR/supraforge"
mkdir -p "$LINKEDIN_DIR/[PROJECT_NAME]"

echo "=== Processing LinkedIn Banners ==="

# Process each base image
for base in "$LINKEDIN_DIR"/base_*.png; do
    if [ -f "$base" ]; then
        filename=$(basename "$base")
        name="${filename%.png}"

        echo ""
        echo "Processing: $filename"

        # Step 1: Crop to LinkedIn dimensions
        cropped="$LINKEDIN_DIR/cropped/${name}_cropped.png"
        node "$SCRIPT_DIR/crop_linkedin_banner.js" "$base" "$cropped"

        # Determine if dark or light based on filename
        if [[ "$filename" == *"_dark"* ]]; then
            sf_logo="$SF_DARK"
            [PROJECT_NAME]_logo="$[PROJECT_NAME]_DARK"
        else
            sf_logo="$SF_LIGHT"
            [PROJECT_NAME]_logo="$[PROJECT_NAME]_LIGHT"
        fi

        # Step 2: Add SUPRA FORGE logo
        sf_output="$LINKEDIN_DIR/supraforge/sf_linkedin_${name#base_}.png"
        node "$SCRIPT_DIR/composite_logo.js" "$cropped" "$sf_logo" "$sf_output" "bottom-left" "0.12"

        # Step 3: Add [PROJECT_NAME] logo
        [PROJECT_NAME]_output="$LINKEDIN_DIR/[PROJECT_NAME]/[PROJECT_NAME]_linkedin_${name#base_}.png"
        node "$SCRIPT_DIR/composite_logo.js" "$cropped" "$[PROJECT_NAME]_logo" "$[PROJECT_NAME]_output" "bottom-left" "0.12"
    fi
done

echo ""
echo "=== Done! ==="
echo ""
echo "SUPRA FORGE LinkedIn banners: $(ls -1 $LINKEDIN_DIR/supraforge/*.png 2>/dev/null | wc -l)"
echo "[PROJECT_NAME] LinkedIn banners: $(ls -1 $LINKEDIN_DIR/[PROJECT_NAME]/*.png 2>/dev/null | wc -l)"
