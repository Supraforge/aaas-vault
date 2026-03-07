#!/bin/bash
# Batch composite script - adds logos to all themed images

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="/Users/user/.gemini/[PROJECT_NAME]"
THEMED_DIR="$PROJECT_ROOT/assets/brand/themed"
OUTPUT_DIR="$PROJECT_ROOT/assets/brand/branded"

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
    node "$SCRIPT_DIR/composite_logo.js" "$input" "$logo" "$output" "bottom-left" "0.18"
}

echo "Compositing with SUPRA FORGE logo..."

# Dark images use dark logo (white text)
for img in "$THEMED_DIR"/*_dark_*.png; do
    if [ -f "$img" ]; then
        filename=$(basename "$img")
        composite "$img" "$SF_DARK" "$OUTPUT_DIR/supraforge/sf_$filename"
    fi
done

# Light images use light logo (dark text)
for img in "$THEMED_DIR"/*_light_*.png; do
    if [ -f "$img" ]; then
        filename=$(basename "$img")
        composite "$img" "$SF_LIGHT" "$OUTPUT_DIR/supraforge/sf_$filename"
    fi
done

echo "Compositing with [PROJECT_NAME] logo..."

# Dark images use dark logo (white text)
for img in "$THEMED_DIR"/*_dark_*.png; do
    if [ -f "$img" ]; then
        filename=$(basename "$img")
        composite "$img" "$[PROJECT_NAME]_DARK" "$OUTPUT_DIR/[PROJECT_NAME]/[PROJECT_NAME]_$filename"
    fi
done

# Light images use light logo (dark text)
for img in "$THEMED_DIR"/*_light_*.png; do
    if [ -f "$img" ]; then
        filename=$(basename "$img")
        composite "$img" "$[PROJECT_NAME]_LIGHT" "$OUTPUT_DIR/[PROJECT_NAME]/[PROJECT_NAME]_$filename"
    fi
done

echo "Done! Branded images saved to $OUTPUT_DIR"
