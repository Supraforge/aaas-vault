"""
Export utilities for converting Vizzu HTML animations to video formats.

Supports MP4, GIF, and WebM using Playwright for browser automation.
"""

from __future__ import annotations

import asyncio
import subprocess
from pathlib import Path
from typing import Optional

try:
    from playwright.async_api import async_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False


async def _capture_animation_async(
    html_path: Path,
    output_path: Path,
    duration: int = 5000,
    width: int = 800,
    height: int = 600,
    fps: int = 30,
) -> None:
    """
    Capture animation frames using Playwright.

    Args:
        html_path: Path to HTML file with animation
        output_path: Output video file path
        duration: Animation duration in milliseconds
        width: Video width
        height: Video height
        fps: Frames per second
    """
    if not PLAYWRIGHT_AVAILABLE:
        raise RuntimeError(
            "Playwright not installed. Run: pip install playwright && playwright install chromium"
        )

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': width, 'height': height})

        # Load HTML
        await page.goto(f'file://{html_path.absolute()}')

        # Wait for animation to load
        await page.wait_for_timeout(500)

        # Record frames
        frames = []
        frame_interval = 1000 / fps  # ms per frame
        num_frames = int(duration / frame_interval)

        for i in range(num_frames):
            screenshot = await page.screenshot(type='png')
            frames.append(screenshot)
            await page.wait_for_timeout(frame_interval)

        await browser.close()

        # Save frames to temp directory
        frames_dir = output_path.parent / f'{output_path.stem}_frames'
        frames_dir.mkdir(exist_ok=True)

        for i, frame in enumerate(frames):
            frame_path = frames_dir / f'frame_{i:04d}.png'
            with open(frame_path, 'wb') as f:
                f.write(frame)

        return frames_dir


def export_to_mp4(
    html_path: Path | str,
    output_path: Optional[Path | str] = None,
    duration: int = 5000,
    fps: int = 30,
    width: int = 800,
    height: int = 600,
) -> Path:
    """
    Export Vizzu animation to MP4 video.

    Args:
        html_path: Path to HTML file with animation
        output_path: Output MP4 file path (auto-generated if None)
        duration: Animation duration in milliseconds
        fps: Frames per second
        width: Video width
        height: Video height

    Returns:
        Path to output MP4 file

    Examples:
        >>> export_to_mp4('animation.html', 'animation.mp4')
        PosixPath('animation.mp4')
    """
    html_path = Path(html_path)
    if output_path is None:
        output_path = html_path.with_suffix('.mp4')
    else:
        output_path = Path(output_path)

    # Capture frames
    frames_dir = asyncio.run(
        _capture_animation_async(html_path, output_path, duration, width, height, fps)
    )

    # Convert frames to MP4 using ffmpeg
    try:
        cmd = [
            'ffmpeg',
            '-y',  # Overwrite output
            '-framerate', str(fps),
            '-i', str(frames_dir / 'frame_%04d.png'),
            '-c:v', 'libx264',
            '-pix_fmt', 'yuv420p',
            '-crf', '23',
            str(output_path),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"ffmpeg failed: {result.stderr}")
    except FileNotFoundError:
        raise RuntimeError(
            "ffmpeg not found. Install with: apt-get install ffmpeg or brew install ffmpeg"
        )

    # Clean up frames
    import shutil
    shutil.rmtree(frames_dir)

    return output_path


def export_to_gif(
    html_path: Path | str,
    output_path: Optional[Path | str] = None,
    duration: int = 5000,
    fps: int = 15,
    width: int = 800,
    height: int = 600,
    optimize: bool = True,
) -> Path:
    """
    Export Vizzu animation to GIF.

    Args:
        html_path: Path to HTML file with animation
        output_path: Output GIF file path (auto-generated if None)
        duration: Animation duration in milliseconds
        fps: Frames per second (lower for smaller file size)
        width: Video width
        height: Video height
        optimize: Optimize GIF file size

    Returns:
        Path to output GIF file

    Examples:
        >>> export_to_gif('animation.html', 'animation.gif', fps=10)
        PosixPath('animation.gif')
    """
    html_path = Path(html_path)
    if output_path is None:
        output_path = html_path.with_suffix('.gif')
    else:
        output_path = Path(output_path)

    # Capture frames
    frames_dir = asyncio.run(
        _capture_animation_async(html_path, output_path, duration, width, height, fps)
    )

    # Convert frames to GIF using ffmpeg
    try:
        # Generate palette for better quality
        palette_path = frames_dir / 'palette.png'
        cmd_palette = [
            'ffmpeg',
            '-y',
            '-i', str(frames_dir / 'frame_%04d.png'),
            '-vf', 'palettegen',
            str(palette_path),
        ]
        subprocess.run(cmd_palette, capture_output=True, check=True)

        # Create GIF with palette
        cmd_gif = [
            'ffmpeg',
            '-y',
            '-framerate', str(fps),
            '-i', str(frames_dir / 'frame_%04d.png'),
            '-i', str(palette_path),
            '-filter_complex', 'paletteuse',
            str(output_path),
        ]
        result = subprocess.run(cmd_gif, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"ffmpeg failed: {result.stderr}")

        # Optimize GIF if requested
        if optimize:
            try:
                cmd_opt = ['gifsicle', '-O3', '--colors', '128', '-i', str(output_path), '-o', str(output_path)]
                subprocess.run(cmd_opt, capture_output=True, check=True)
            except FileNotFoundError:
                # gifsicle not available, skip optimization
                pass

    except FileNotFoundError:
        raise RuntimeError(
            "ffmpeg not found. Install with: apt-get install ffmpeg or brew install ffmpeg"
        )

    # Clean up frames
    import shutil
    shutil.rmtree(frames_dir)

    return output_path


def export_to_webm(
    html_path: Path | str,
    output_path: Optional[Path | str] = None,
    duration: int = 5000,
    fps: int = 30,
    width: int = 800,
    height: int = 600,
) -> Path:
    """
    Export Vizzu animation to WebM video (web-optimized).

    Args:
        html_path: Path to HTML file with animation
        output_path: Output WebM file path (auto-generated if None)
        duration: Animation duration in milliseconds
        fps: Frames per second
        width: Video width
        height: Video height

    Returns:
        Path to output WebM file

    Examples:
        >>> export_to_webm('animation.html', 'animation.webm')
        PosixPath('animation.webm')
    """
    html_path = Path(html_path)
    if output_path is None:
        output_path = html_path.with_suffix('.webm')
    else:
        output_path = Path(output_path)

    # Capture frames
    frames_dir = asyncio.run(
        _capture_animation_async(html_path, output_path, duration, width, height, fps)
    )

    # Convert frames to WebM using ffmpeg
    try:
        cmd = [
            'ffmpeg',
            '-y',  # Overwrite output
            '-framerate', str(fps),
            '-i', str(frames_dir / 'frame_%04d.png'),
            '-c:v', 'libvpx-vp9',
            '-pix_fmt', 'yuva420p',
            '-crf', '30',
            '-b:v', '0',
            str(output_path),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"ffmpeg failed: {result.stderr}")
    except FileNotFoundError:
        raise RuntimeError(
            "ffmpeg not found. Install with: apt-get install ffmpeg or brew install ffmpeg"
        )

    # Clean up frames
    import shutil
    shutil.rmtree(frames_dir)

    return output_path
