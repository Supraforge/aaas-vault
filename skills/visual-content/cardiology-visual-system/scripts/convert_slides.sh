#!/bin/bash
# Marp Slide Conversion Helper
# Converts Markdown slides to PPTX, PDF, or HTML

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INPUT="${1:-presentation.md}"
FORMAT="${2:-pptx}"
OUTPUT="${3:-}"

# Check if marp-cli is installed
if ! command -v marp &> /dev/null; then
    echo "❌ Marp CLI not found!"
    echo ""
    echo "Install with:"
    echo "  npm install -g @marp-team/marp-cli"
    echo ""
    echo "Or use npx:"
    echo "  npx @marp-team/marp-cli $INPUT --pptx"
    exit 1
fi

# Check if input file exists
if [ ! -f "$INPUT" ]; then
    echo "❌ Input file not found: $INPUT"
    echo ""
    echo "Usage: ./convert_slides.sh <input.md> [format] [output]"
    echo ""
    echo "Formats: pptx, pdf, html"
    exit 1
fi

# Set output filename if not provided
if [ -z "$OUTPUT" ]; then
    BASENAME="${INPUT%.*}"
    OUTPUT="${BASENAME}.${FORMAT}"
fi

echo "📄 Input:  $INPUT"
echo "📦 Format: $FORMAT"
echo "💾 Output: $OUTPUT"
echo ""

case $FORMAT in
    pptx)
        marp "$INPUT" --pptx -o "$OUTPUT"
        ;;
    pdf)
        marp "$INPUT" --pdf -o "$OUTPUT"
        ;;
    html)
        marp "$INPUT" -o "$OUTPUT"
        ;;
    *)
        echo "❌ Unknown format: $FORMAT"
        echo "   Use: pptx, pdf, or html"
        exit 1
        ;;
esac

echo ""
echo "✅ Created: $OUTPUT"

# Show file size
if [ -f "$OUTPUT" ]; then
    SIZE=$(ls -lh "$OUTPUT" | awk '{print $5}')
    echo "📊 Size: $SIZE"
fi
