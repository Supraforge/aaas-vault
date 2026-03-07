#!/usr/bin/env node
/**
 * Logo Compositing Script
 * Overlays SVG logos onto generated images
 *
 * Usage: node composite_logo.js <base_image> <logo_svg> <output_path> [position] [scale]
 *
 * Positions: bottom-left (default), bottom-right, top-left, top-right, center
 * Scale: 0.1 to 1.0 (default 0.15 = 15% of image width)
 */

const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const baseImagePath = process.argv[2];
const logoSvgPath = process.argv[3];
const outputPath = process.argv[4];
const position = process.argv[5] || 'bottom-left';
const scale = parseFloat(process.argv[6]) || 0.15;

if (!baseImagePath || !logoSvgPath || !outputPath) {
    console.error('Usage: node composite_logo.js <base_image> <logo_svg> <output_path> [position] [scale]');
    console.error('Positions: bottom-left, bottom-right, top-left, top-right, center');
    process.exit(1);
}

async function compositeImage() {
    try {
        // Get base image dimensions
        const baseMetadata = await sharp(baseImagePath).metadata();
        const baseWidth = baseMetadata.width;
        const baseHeight = baseMetadata.height;

        // Calculate logo size (scale relative to image width)
        const logoWidth = Math.round(baseWidth * scale);

        // Read and resize SVG logo
        const svgBuffer = fs.readFileSync(logoSvgPath);
        const logoBuffer = await sharp(svgBuffer)
            .resize({ width: logoWidth })
            .png()
            .toBuffer();

        // Get resized logo dimensions
        const logoMetadata = await sharp(logoBuffer).metadata();
        const logoHeight = logoMetadata.height;

        // Calculate position with padding (5% of image size)
        const padding = Math.round(baseWidth * 0.03);
        let left, top;

        switch (position) {
            case 'top-left':
                left = padding;
                top = padding;
                break;
            case 'top-right':
                left = baseWidth - logoWidth - padding;
                top = padding;
                break;
            case 'bottom-right':
                left = baseWidth - logoWidth - padding;
                top = baseHeight - logoHeight - padding;
                break;
            case 'center':
                left = Math.round((baseWidth - logoWidth) / 2);
                top = Math.round((baseHeight - logoHeight) / 2);
                break;
            case 'bottom-left':
            default:
                left = padding;
                top = baseHeight - logoHeight - padding;
                break;
        }

        // Ensure output directory exists
        const outputDir = path.dirname(outputPath);
        if (outputDir && outputDir !== '.' && !fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        // Composite the images
        await sharp(baseImagePath)
            .composite([{
                input: logoBuffer,
                left: left,
                top: top
            }])
            .toFile(outputPath);

        console.log(`Composited: ${outputPath}`);
    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    }
}

compositeImage();
