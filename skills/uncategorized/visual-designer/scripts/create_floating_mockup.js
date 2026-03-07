#!/usr/bin/env node
/**
 * Floating Device Mockup with Decorative Elements
 * Creates premium mockups with shadows, gradients, and floating effect
 */

const sharp = require('sharp');
const path = require('path');
const fs = require('fs');

const screenshotPath = process.argv[2];
const outputPath = process.argv[3];
const theme = process.argv[4] || 'dark'; // dark or light
const style = process.argv[5] || 'floating'; // floating, angled, minimal

if (!screenshotPath || !outputPath) {
    console.error('Usage: node create_floating_mockup.js <screenshot> <output> [dark|light] [floating|angled|minimal]');
    process.exit(1);
}

async function createMockup() {
    try {
        const canvasSize = 1200;
        const isDark = theme === 'dark';

        // Colors based on theme
        const bgColor = isDark ? '#0F172A' : '#F8FAFC';
        const accentColor = '#d4a853';
        const blueAccent = '#0369A1';

        // Screen dimensions
        const screenWidth = Math.round(canvasSize * 0.7);
        const screenHeight = Math.round(screenWidth * 0.5625);
        const bezelSize = 12;
        const frameRadius = 16;

        // Calculate position based on style
        let screenX, screenY, rotation;
        if (style === 'angled') {
            screenX = Math.round((canvasSize - screenWidth) / 2) + 50;
            screenY = Math.round((canvasSize - screenHeight) / 2) - 30;
        } else {
            screenX = Math.round((canvasSize - screenWidth) / 2);
            screenY = Math.round((canvasSize - screenHeight) / 2) - 40;
        }

        // Resize screenshot
        const resizedScreenshot = await sharp(screenshotPath)
            .resize(screenWidth - bezelSize * 2, screenHeight - bezelSize * 2, {
                fit: 'cover',
                position: 'top'
            })
            .toBuffer();

        // Create decorative SVG background
        const decorSvg = `
        <svg width="${canvasSize}" height="${canvasSize}" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:${accentColor};stop-opacity:0.15" />
                    <stop offset="100%" style="stop-color:${blueAccent};stop-opacity:0.1" />
                </linearGradient>
                <filter id="blur" x="-50%" y="-50%" width="200%" height="200%">
                    <feGaussianBlur in="SourceGraphic" stdDeviation="60" />
                </filter>
            </defs>
            <!-- Background -->
            <rect width="100%" height="100%" fill="${bgColor}"/>
            <!-- Decorative blobs -->
            <ellipse cx="${canvasSize * 0.15}" cy="${canvasSize * 0.3}" rx="200" ry="200" fill="${accentColor}" opacity="0.08" filter="url(#blur)"/>
            <ellipse cx="${canvasSize * 0.85}" cy="${canvasSize * 0.7}" rx="250" ry="250" fill="${blueAccent}" opacity="0.06" filter="url(#blur)"/>
            ${style === 'floating' ? `
            <!-- Floating dots/particles -->
            <circle cx="${canvasSize * 0.1}" cy="${canvasSize * 0.2}" r="4" fill="${accentColor}" opacity="0.4"/>
            <circle cx="${canvasSize * 0.08}" cy="${canvasSize * 0.6}" r="3" fill="${blueAccent}" opacity="0.3"/>
            <circle cx="${canvasSize * 0.92}" cy="${canvasSize * 0.25}" r="5" fill="${accentColor}" opacity="0.35"/>
            <circle cx="${canvasSize * 0.88}" cy="${canvasSize * 0.8}" r="4" fill="${blueAccent}" opacity="0.4"/>
            <circle cx="${canvasSize * 0.15}" cy="${canvasSize * 0.85}" r="3" fill="${accentColor}" opacity="0.3"/>
            ` : ''}
        </svg>`;

        // Device frame with shadow
        const frameSvg = `
        <svg width="${screenWidth + 40}" height="${screenHeight + 80}" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
                    <feDropShadow dx="0" dy="20" stdDeviation="25" flood-color="${isDark ? '#000' : '#64748b'}" flood-opacity="${isDark ? '0.5' : '0.2'}"/>
                </filter>
            </defs>
            <!-- Shadow layer -->
            <rect x="20" y="20" width="${screenWidth}" height="${screenHeight}"
                  rx="${frameRadius}" ry="${frameRadius}"
                  fill="#1a1a1a" filter="url(#shadow)"/>
        </svg>`;

        const frameBezelSvg = `
        <svg width="${screenWidth}" height="${screenHeight + 40}" xmlns="http://www.w3.org/2000/svg">
            <!-- Screen bezel -->
            <rect x="0" y="0" width="${screenWidth}" height="${screenHeight}"
                  rx="${frameRadius}" ry="${frameRadius}"
                  fill="${isDark ? '#1E293B' : '#374151'}"/>
            <!-- Screen area -->
            <rect x="${bezelSize}" y="${bezelSize}"
                  width="${screenWidth - bezelSize * 2}" height="${screenHeight - bezelSize * 2}"
                  rx="${frameRadius/2}" ry="${frameRadius/2}"
                  fill="#000"/>
            <!-- Base/stand -->
            <path d="M ${screenWidth * 0.35} ${screenHeight}
                     L ${screenWidth * 0.32} ${screenHeight + 35}
                     L ${screenWidth * 0.68} ${screenHeight + 35}
                     L ${screenWidth * 0.65} ${screenHeight} Z"
                  fill="${isDark ? '#1E293B' : '#4B5563'}"/>
            <ellipse cx="${screenWidth/2}" cy="${screenHeight + 38}" rx="${screenWidth * 0.22}" ry="4"
                     fill="${isDark ? '#1E293B' : '#4B5563'}"/>
        </svg>`;

        // Ensure output directory exists
        const outputDir = path.dirname(outputPath);
        if (outputDir && outputDir !== '.' && !fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        // Create final composite
        await sharp(Buffer.from(decorSvg))
            .composite([
                // Shadow
                {
                    input: Buffer.from(frameSvg),
                    left: screenX - 20,
                    top: screenY - 10
                },
                // Device frame
                {
                    input: Buffer.from(frameBezelSvg),
                    left: screenX,
                    top: screenY
                },
                // Screenshot
                {
                    input: resizedScreenshot,
                    left: screenX + bezelSize,
                    top: screenY + bezelSize
                }
            ])
            .png()
            .toFile(outputPath);

        console.log(`Premium mockup created: ${outputPath}`);
    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    }
}

createMockup();
