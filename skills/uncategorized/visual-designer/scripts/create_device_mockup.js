#!/usr/bin/env node
/**
 * Device Mockup Creator
 * Creates laptop/monitor mockups with website screenshots
 *
 * Usage: node create_device_mockup.js <screenshot> <output> <background_color> [size]
 */

const sharp = require('sharp');
const path = require('path');
const fs = require('fs');

const screenshotPath = process.argv[2];
const outputPath = process.argv[3];
const bgColor = process.argv[4] || '#0F172A';
const outputSize = parseInt(process.argv[5]) || 1200;

if (!screenshotPath || !outputPath) {
    console.error('Usage: node create_device_mockup.js <screenshot> <output> <background_color> [size]');
    process.exit(1);
}

async function createMockup() {
    try {
        // Output dimensions (square for LinkedIn)
        const canvasSize = outputSize;

        // Device frame dimensions (laptop style)
        const screenWidth = Math.round(canvasSize * 0.75);
        const screenHeight = Math.round(screenWidth * 0.5625); // 16:9 ratio
        const bezelSize = Math.round(screenWidth * 0.02);
        const frameRadius = Math.round(screenWidth * 0.02);

        // Position (centered, slightly above middle)
        const screenX = Math.round((canvasSize - screenWidth) / 2);
        const screenY = Math.round((canvasSize - screenHeight) / 2) - Math.round(canvasSize * 0.05);

        // Resize screenshot to fit screen area
        const resizedScreenshot = await sharp(screenshotPath)
            .resize(screenWidth - bezelSize * 2, screenHeight - bezelSize * 2, {
                fit: 'cover',
                position: 'top'
            })
            .toBuffer();

        // Create the device frame SVG
        const frameWidth = screenWidth;
        const frameHeight = screenHeight + Math.round(screenHeight * 0.08); // Add base

        const frameSvg = `
        <svg width="${frameWidth}" height="${frameHeight}" xmlns="http://www.w3.org/2000/svg">
            <!-- Laptop screen bezel -->
            <rect x="0" y="0" width="${frameWidth}" height="${screenHeight}"
                  rx="${frameRadius}" ry="${frameRadius}"
                  fill="#1a1a1a"/>
            <!-- Screen inner (darker) -->
            <rect x="${bezelSize}" y="${bezelSize}"
                  width="${frameWidth - bezelSize * 2}" height="${screenHeight - bezelSize * 2}"
                  rx="${frameRadius/2}" ry="${frameRadius/2}"
                  fill="#000"/>
            <!-- Laptop base -->
            <path d="M ${frameWidth * 0.1} ${screenHeight}
                     L ${frameWidth * 0.05} ${frameHeight - 5}
                     Q ${frameWidth * 0.05} ${frameHeight} ${frameWidth * 0.1} ${frameHeight}
                     L ${frameWidth * 0.9} ${frameHeight}
                     Q ${frameWidth * 0.95} ${frameHeight} ${frameWidth * 0.95} ${frameHeight - 5}
                     L ${frameWidth * 0.9} ${screenHeight} Z"
                  fill="#2a2a2a"/>
            <!-- Trackpad hint -->
            <rect x="${frameWidth * 0.35}" y="${screenHeight + 8}"
                  width="${frameWidth * 0.3}" height="${frameHeight - screenHeight - 16}"
                  rx="3" ry="3"
                  fill="#222" opacity="0.5"/>
        </svg>`;

        const frameBuffer = Buffer.from(frameSvg);

        // Ensure output directory exists
        const outputDir = path.dirname(outputPath);
        if (outputDir && outputDir !== '.' && !fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        // Create final composite
        await sharp({
            create: {
                width: canvasSize,
                height: canvasSize,
                channels: 4,
                background: bgColor
            }
        })
        .composite([
            // Device frame
            {
                input: frameBuffer,
                left: screenX,
                top: screenY
            },
            // Screenshot inside frame
            {
                input: resizedScreenshot,
                left: screenX + bezelSize,
                top: screenY + bezelSize
            }
        ])
        .png()
        .toFile(outputPath);

        console.log(`Mockup created: ${outputPath}`);
    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    }
}

createMockup();
