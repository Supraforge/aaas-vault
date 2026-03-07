#!/usr/bin/env node
/**
 * Premium 3D-Style Mockup Creator
 * Composites real screenshots onto premium AI-generated backgrounds
 * with professional device frames
 */

const sharp = require('sharp');
const path = require('path');
const fs = require('fs');

const backgroundPath = process.argv[2];
const screenshotPath = process.argv[3];
const outputPath = process.argv[4];
const style = process.argv[5] || 'laptop'; // laptop, floating, angled

if (!backgroundPath || !screenshotPath || !outputPath) {
    console.error('Usage: node create_premium_3d_mockup.js <background> <screenshot> <output> [laptop|floating|angled]');
    process.exit(1);
}

async function createMockup() {
    try {
        // Get background dimensions
        const bgMeta = await sharp(backgroundPath).metadata();
        const canvasSize = bgMeta.width;

        // Device dimensions based on style
        let screenWidth, screenHeight, screenX, screenY;
        let frameColor = '#1a1a1a';
        let bezelSize = 8;

        if (style === 'angled') {
            // Smaller, angled position (like in inspiration)
            screenWidth = Math.round(canvasSize * 0.55);
            screenHeight = Math.round(screenWidth * 0.625);
            screenX = Math.round(canvasSize * 0.15);
            screenY = Math.round(canvasSize * 0.25);
        } else if (style === 'floating') {
            // Centered floating card
            screenWidth = Math.round(canvasSize * 0.6);
            screenHeight = Math.round(screenWidth * 0.6);
            screenX = Math.round((canvasSize - screenWidth) / 2);
            screenY = Math.round((canvasSize - screenHeight) / 2);
            bezelSize = 12;
        } else {
            // Standard laptop
            screenWidth = Math.round(canvasSize * 0.65);
            screenHeight = Math.round(screenWidth * 0.5625);
            screenX = Math.round((canvasSize - screenWidth) / 2);
            screenY = Math.round(canvasSize * 0.28);
        }

        // Resize screenshot
        const contentWidth = screenWidth - bezelSize * 2;
        const contentHeight = screenHeight - bezelSize * 2 - 20; // Leave room for toolbar

        const resizedScreenshot = await sharp(screenshotPath)
            .resize(contentWidth, contentHeight, { fit: 'cover', position: 'top' })
            .toBuffer();

        // Create device frame SVG with premium styling
        const frameSvg = `
        <svg width="${screenWidth + 40}" height="${screenHeight + 80}" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <!-- Premium shadow -->
                <filter id="deviceShadow" x="-30%" y="-30%" width="160%" height="160%">
                    <feGaussianBlur in="SourceAlpha" stdDeviation="15"/>
                    <feOffset dx="0" dy="10" result="offsetblur"/>
                    <feComponentTransfer>
                        <feFuncA type="linear" slope="0.4"/>
                    </feComponentTransfer>
                    <feMerge>
                        <feMergeNode/>
                        <feMergeNode in="SourceGraphic"/>
                    </feMerge>
                </filter>
                <!-- Screen glow -->
                <filter id="screenGlow" x="-10%" y="-10%" width="120%" height="120%">
                    <feGaussianBlur stdDeviation="3" result="glow"/>
                    <feMerge>
                        <feMergeNode in="glow"/>
                        <feMergeNode in="SourceGraphic"/>
                    </feMerge>
                </filter>
                <!-- Metallic gradient for bezel -->
                <linearGradient id="bezelGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stop-color="#3a3a3a"/>
                    <stop offset="50%" stop-color="#1a1a1a"/>
                    <stop offset="100%" stop-color="#2a2a2a"/>
                </linearGradient>
            </defs>

            <!-- Device body with shadow -->
            <g filter="url(#deviceShadow)">
                <!-- Main bezel -->
                <rect x="20" y="10" width="${screenWidth}" height="${screenHeight}"
                      rx="10" ry="10" fill="url(#bezelGrad)"/>
                <!-- Subtle highlight on top edge -->
                <rect x="20" y="10" width="${screenWidth}" height="2"
                      rx="1" fill="#4a4a4a" opacity="0.5"/>
            </g>

            <!-- Screen area -->
            <rect x="${20 + bezelSize}" y="${10 + bezelSize}"
                  width="${contentWidth}" height="${contentHeight + 20}"
                  rx="4" ry="4" fill="#000" filter="url(#screenGlow)"/>

            <!-- Webcam notch (for MacBook style) -->
            <circle cx="${20 + screenWidth/2}" cy="${10 + bezelSize/2 + 2}" r="2.5" fill="#2a2a2a"/>

            <!-- Laptop base -->
            <path d="M ${20 - 20} ${10 + screenHeight}
                     Q ${20 - 25} ${10 + screenHeight + 15} ${20 - 5} ${10 + screenHeight + 18}
                     L ${20 + screenWidth + 5} ${10 + screenHeight + 18}
                     Q ${20 + screenWidth + 25} ${10 + screenHeight + 15} ${20 + screenWidth + 20} ${10 + screenHeight}
                     Z"
                  fill="#1a1a1a"/>

            <!-- Trackpad indication -->
            <rect x="${20 + screenWidth/2 - 35}" y="${10 + screenHeight + 3}"
                  width="70" height="10" rx="3" fill="#252525"/>
        </svg>`;

        // Load background
        const background = await sharp(backgroundPath).toBuffer();

        // Ensure output directory exists
        const outputDir = path.dirname(outputPath);
        if (outputDir && outputDir !== '.' && !fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        // Create final composite
        await sharp(background)
            .composite([
                // Device frame
                {
                    input: Buffer.from(frameSvg),
                    left: screenX - 20,
                    top: screenY - 10
                },
                // Real screenshot
                {
                    input: resizedScreenshot,
                    left: screenX + bezelSize,
                    top: screenY + bezelSize
                }
            ])
            .png()
            .toFile(outputPath);

        console.log(`Premium 3D mockup created: ${outputPath}`);
    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    }
}

createMockup();
