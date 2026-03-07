#!/usr/bin/env python3
"""
Graphic Designer Tool - Image editing operations for Claude Code
Supports: background removal, resize, crop, color adjustment, format conversion
"""

import argparse
import sys
from pathlib import Path
from typing import Optional, Tuple

try:
    from PIL import Image, ImageEnhance, ImageOps
except ImportError:
    print("Error: Pillow not installed. Run: pip install Pillow")
    sys.exit(1)

try:
    from rembg import remove
    REMBG_AVAILABLE = True
except ImportError:
    REMBG_AVAILABLE = False


def remove_background(input_path: str, output_path: Optional[str] = None) -> str:
    """Remove background from image using rembg AI."""
    if not REMBG_AVAILABLE:
        raise RuntimeError("rembg not installed. Run: pip install rembg[gpu]")

    input_file = Path(input_path)
    if output_path is None:
        output_path = input_file.stem + "_nobg.png"

    with open(input_path, "rb") as f:
        input_data = f.read()

    output_data = remove(input_data)

    with open(output_path, "wb") as f:
        f.write(output_data)

    print(f"✓ Background removed: {output_path}")
    return output_path


def resize_image(
    input_path: str,
    output_path: Optional[str] = None,
    width: Optional[int] = None,
    height: Optional[int] = None,
    scale: Optional[float] = None,
    maintain_aspect: bool = True
) -> str:
    """Resize image by dimensions or scale factor."""
    img = Image.open(input_path)
    original_size = img.size

    if scale:
        new_width = int(original_size[0] * scale)
        new_height = int(original_size[1] * scale)
    elif width and height:
        if maintain_aspect:
            img.thumbnail((width, height), Image.Resampling.LANCZOS)
            new_width, new_height = img.size
        else:
            new_width, new_height = width, height
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    elif width:
        ratio = width / original_size[0]
        new_width = width
        new_height = int(original_size[1] * ratio)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    elif height:
        ratio = height / original_size[1]
        new_height = height
        new_width = int(original_size[0] * ratio)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    else:
        raise ValueError("Must specify width, height, or scale")

    if output_path is None:
        input_file = Path(input_path)
        output_path = f"{input_file.stem}_resized{input_file.suffix}"

    # Handle transparency for JPEG
    if output_path.lower().endswith(('.jpg', '.jpeg')) and img.mode == 'RGBA':
        img = img.convert('RGB')

    img.save(output_path, quality=95)
    print(f"✓ Resized {original_size} → ({new_width}, {new_height}): {output_path}")
    return output_path


def crop_image(
    input_path: str,
    output_path: Optional[str] = None,
    left: int = 0,
    top: int = 0,
    right: Optional[int] = None,
    bottom: Optional[int] = None,
    width: Optional[int] = None,
    height: Optional[int] = None
) -> str:
    """Crop image by coordinates or dimensions."""
    img = Image.open(input_path)

    if right is None:
        right = left + width if width else img.size[0]
    if bottom is None:
        bottom = top + height if height else img.size[1]

    cropped = img.crop((left, top, right, bottom))

    if output_path is None:
        input_file = Path(input_path)
        output_path = f"{input_file.stem}_cropped{input_file.suffix}"

    cropped.save(output_path, quality=95)
    print(f"✓ Cropped to ({right-left}x{bottom-top}): {output_path}")
    return output_path


def adjust_colors(
    input_path: str,
    output_path: Optional[str] = None,
    brightness: float = 1.0,
    contrast: float = 1.0,
    saturation: float = 1.0,
    sharpness: float = 1.0
) -> str:
    """Adjust image colors and appearance."""
    img = Image.open(input_path)

    if brightness != 1.0:
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness)

    if contrast != 1.0:
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast)

    if saturation != 1.0:
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(saturation)

    if sharpness != 1.0:
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(sharpness)

    if output_path is None:
        input_file = Path(input_path)
        output_path = f"{input_file.stem}_adjusted{input_file.suffix}"

    # Handle transparency for JPEG
    if output_path.lower().endswith(('.jpg', '.jpeg')) and img.mode == 'RGBA':
        img = img.convert('RGB')

    img.save(output_path, quality=95)
    print(f"✓ Colors adjusted: {output_path}")
    return output_path


def convert_format(
    input_path: str,
    output_format: str,
    output_path: Optional[str] = None,
    quality: int = 95
) -> str:
    """Convert image to different format."""
    img = Image.open(input_path)
    input_file = Path(input_path)

    # Normalize format
    fmt = output_format.lower().strip('.')
    if fmt == 'jpg':
        fmt = 'jpeg'

    if output_path is None:
        output_path = f"{input_file.stem}.{fmt if fmt != 'jpeg' else 'jpg'}"

    # Handle transparency for JPEG
    if fmt == 'jpeg' and img.mode == 'RGBA':
        # Create white background
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        img = background
    elif fmt == 'jpeg' and img.mode != 'RGB':
        img = img.convert('RGB')

    img.save(output_path, format=fmt.upper(), quality=quality)
    print(f"✓ Converted to {fmt.upper()}: {output_path}")
    return output_path


def get_info(input_path: str) -> dict:
    """Get image information."""
    img = Image.open(input_path)
    info = {
        "path": input_path,
        "format": img.format,
        "mode": img.mode,
        "size": img.size,
        "width": img.size[0],
        "height": img.size[1],
    }

    # File size
    file_size = Path(input_path).stat().st_size
    if file_size > 1024 * 1024:
        info["file_size"] = f"{file_size / (1024*1024):.2f} MB"
    else:
        info["file_size"] = f"{file_size / 1024:.2f} KB"

    print(f"Image: {input_path}")
    print(f"  Format: {info['format']}")
    print(f"  Mode: {info['mode']}")
    print(f"  Size: {info['width']}x{info['height']}")
    print(f"  File size: {info['file_size']}")

    return info


def main():
    parser = argparse.ArgumentParser(
        description="Image editing tool for Claude Code",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Remove background:
    python edit_image.py remove-bg photo.jpg
    python edit_image.py remove-bg photo.jpg -o clean.png

  Resize image:
    python edit_image.py resize photo.jpg --width 800
    python edit_image.py resize photo.jpg --scale 0.5
    python edit_image.py resize photo.jpg --width 800 --height 600

  Crop image:
    python edit_image.py crop photo.jpg --left 100 --top 50 --width 400 --height 300

  Adjust colors:
    python edit_image.py colors photo.jpg --brightness 1.2 --contrast 1.1
    python edit_image.py colors photo.jpg --saturation 0.5  # desaturate

  Convert format:
    python edit_image.py convert photo.png --format jpg --quality 85

  Get image info:
    python edit_image.py info photo.jpg
"""
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Remove background
    bg_parser = subparsers.add_parser("remove-bg", help="Remove image background")
    bg_parser.add_argument("input", help="Input image path")
    bg_parser.add_argument("-o", "--output", help="Output path (default: input_nobg.png)")

    # Resize
    resize_parser = subparsers.add_parser("resize", help="Resize image")
    resize_parser.add_argument("input", help="Input image path")
    resize_parser.add_argument("-o", "--output", help="Output path")
    resize_parser.add_argument("--width", type=int, help="Target width")
    resize_parser.add_argument("--height", type=int, help="Target height")
    resize_parser.add_argument("--scale", type=float, help="Scale factor (e.g., 0.5 for half)")
    resize_parser.add_argument("--no-aspect", action="store_true", help="Don't maintain aspect ratio")

    # Crop
    crop_parser = subparsers.add_parser("crop", help="Crop image")
    crop_parser.add_argument("input", help="Input image path")
    crop_parser.add_argument("-o", "--output", help="Output path")
    crop_parser.add_argument("--left", type=int, default=0, help="Left coordinate")
    crop_parser.add_argument("--top", type=int, default=0, help="Top coordinate")
    crop_parser.add_argument("--right", type=int, help="Right coordinate")
    crop_parser.add_argument("--bottom", type=int, help="Bottom coordinate")
    crop_parser.add_argument("--width", type=int, help="Crop width (alternative to right)")
    crop_parser.add_argument("--height", type=int, help="Crop height (alternative to bottom)")

    # Color adjustment
    color_parser = subparsers.add_parser("colors", help="Adjust colors")
    color_parser.add_argument("input", help="Input image path")
    color_parser.add_argument("-o", "--output", help="Output path")
    color_parser.add_argument("--brightness", type=float, default=1.0, help="Brightness (1.0 = no change)")
    color_parser.add_argument("--contrast", type=float, default=1.0, help="Contrast (1.0 = no change)")
    color_parser.add_argument("--saturation", type=float, default=1.0, help="Saturation (1.0 = no change, 0 = grayscale)")
    color_parser.add_argument("--sharpness", type=float, default=1.0, help="Sharpness (1.0 = no change)")

    # Convert format
    convert_parser = subparsers.add_parser("convert", help="Convert format")
    convert_parser.add_argument("input", help="Input image path")
    convert_parser.add_argument("--format", "-f", required=True, help="Target format (png, jpg)")
    convert_parser.add_argument("-o", "--output", help="Output path")
    convert_parser.add_argument("--quality", type=int, default=95, help="JPEG quality (1-100)")

    # Info
    info_parser = subparsers.add_parser("info", help="Get image info")
    info_parser.add_argument("input", help="Input image path")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        if args.command == "remove-bg":
            remove_background(args.input, args.output)
        elif args.command == "resize":
            resize_image(
                args.input, args.output,
                width=args.width, height=args.height,
                scale=args.scale, maintain_aspect=not args.no_aspect
            )
        elif args.command == "crop":
            crop_image(
                args.input, args.output,
                left=args.left, top=args.top,
                right=args.right, bottom=args.bottom,
                width=args.width, height=args.height
            )
        elif args.command == "colors":
            adjust_colors(
                args.input, args.output,
                brightness=args.brightness, contrast=args.contrast,
                saturation=args.saturation, sharpness=args.sharpness
            )
        elif args.command == "convert":
            convert_format(args.input, args.format, args.output, args.quality)
        elif args.command == "info":
            get_info(args.input)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
