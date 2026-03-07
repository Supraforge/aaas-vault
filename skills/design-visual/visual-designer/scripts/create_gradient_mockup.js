#!/usr/bin/env node
/**
 * Gradient Background Mockup Creator
 * Creates mockups with premium gradient backgrounds and the real website
 */

const sharp = require('sharp');
const path = require('path');
const fs = require('fs');

const screenshotPath = process.argv[2];
const outputPath = process.argv[3];
const style = process.argv[4] || 'gold'; // gold, blue, mixed

if (!screenshotPath || !outputPath) {
    console.error('Usage: node create_gradient_mockup.js <screenshot> <output> [gold|blue|mixed]');
    process.exit(1);
}

async function createMockup() {
    try {
        const canvasSize = 1200;

        // Gradient colors based on style
        let gradientSvg;
        const accentGold = '#d4a853';
        const accentBlue = '#0369A1';
        const darkNavy = '#0F172A';
        const darkerNavy = '#020617';

        if (style === 'gold') {
            gradientSvg = `
            <svg width="${canvasSize}" height="${canvasSize}" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <radialGradient id="bg" cx="30%" cy="30%" r="70%">
                        <stop offset="0%" stop-color="#1E293B"/>
                        <stop offset="100%" stop-color="${darkerNavy}"/>
                    </radialGradient>
                    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
                        <stop offset="0%" stop-color="${accentGold}" stop-opacity="0.15"/>
                        <stop offset="100%" stop-color="${accentGold}" stop-opacity="0"/>
                    </radialGradient>
                </defs>
                <rect width="100%" height="100%" fill="url(#bg)"/>
                <ellipse cx="${canvasSize * 0.7}" cy="${canvasSize * 0.3}" rx="400" ry="400" fill="url(#glow)"/>
            </svg>`;
        } else if (style === 'blue') {
            gradientSvg = `
            <svg width="${canvasSize}" height="${canvasSize}" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <radialGradient id="bg" cx="70%" cy="70%" r="70%">
                        <stop offset="0%" stop-color="#1E293B"/>
                        <stop offset="100%" stop-color="${darkerNavy}"/>
                    </radialGradient>
                    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
                        <stop offset="0%" stop-color="${accentBlue}" stop-opacity="0.2"/>
                        <stop offset="100%" stop-color="${accentBlue}" stop-opacity="0"/>
                    </radialGradient>
                </defs>
                <rect width="100%" height="100%" fill="url(#bg)"/>
                <ellipse cx="${canvasSize * 0.2}" cy="${canvasSize * 0.8}" rx="450" ry="450" fill="url(#glow)"/>
            </svg>`;
        } else {
            gradientSvg = `
            <svg width="${canvasSize}" height="${canvasSize}" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stop-color="${darkerNavy}"/>
                        <stop offset="50%" stop-color="#0F172A"/>
                        <stop offset="100%" stop-color="#1E293B"/>
                    </linearGradient>
                    <radialGradient id="goldGlow" cx="50%" cy="50%" r="50%">
                        <stop offset="0%" stop-color="${accentGold}" stop-opacity="0.12"/>
                        <stop offset="100%" stop-color="${accentGold}" stop-opacity="0"/>
                    </radialGradient>
                    <radialGradient id="blueGlow" cx="50%" cy="50%" r="50%">
                        <stop offset="0%" stop-color="${accentBlue}" stop-opacity="0.1"/>
                        <stop offset="100%" stop-color="${accentBlue}" stop-opacity="0"/>
                    </radialGradient>
                </defs>
                <rect width="100%" height="100%" fill="url(#bg)"/>
                <ellipse cx="${canvasSize * 0.15}" cy="${canvasSize * 0.25}" rx="350" ry="350" fill="url(#goldGlow)"/>
                <ellipse cx="${canvasSize * 0.85}" cy="${canvasSize * 0.75}" rx="400" ry="400" fill="url(#blueGlow)"/>
            </svg>`;
        }

        // Screen dimensions
        const screenWidth = Math.round(canvasSize * 0.75);
        const screenHeight = Math.round(screenWidth * 0.5625);
        const screenX = Math.round((canvasSize - screenWidth) / 2);
        const screenY = Math.round((canvasSize - screenHeight) / 2) - 30;
        const borderRadius = 12;
        const shadowBlur = 30;

        // Resize screenshot
        const resizedScreenshot = await sharp(screenshotPath)
            .resize(screenWidth - 8, screenHeight - 8, {
                fit: 'cover',
                position: 'top'
            })
            .toBuffer();

        // Create frame with shadow
        const frameSvg = `
        <svg width="${screenWidth + 60}" height="${screenHeight + 60}" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
                    <feDropShadow dx="0" dy="15" stdDeviation="${shadowBlur}" flood-color="#000" flood-opacity="0.5"/>
                </filter>
            </defs>
            <rect x="30" y="20" width="${screenWidth}" height="${screenHeight}"
                  rx="${borderRadius}" ry="${borderRadius}"
                  fill="#1a1a1a" filter="url(#shadow)"/>
        </svg>`;

        const bezelSvg = `
        <svg width="${screenWidth}" height="${screenHeight}" xmlns="http://www.w3.org/2000/svg">
            <rect x="0" y="0" width="${screenWidth}" height="${screenHeight}"
                  rx="${borderRadius}" ry="${borderRadius}"
                  fill="#1E293B" stroke="#334155" stroke-width="1"/>
            <rect x="4" y="4" width="${screenWidth - 8}" height="${screenHeight - 8}"
                  rx="${borderRadius - 2}" ry="${borderRadius - 2}"
                  fill="#000"/>
        </svg>`;

        // Ensure output directory exists
        const outputDir = path.dirname(outputPath);
        if (outputDir && outputDir !== '.' && !fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        // Create background
        const bgBuffer = await sharp(Buffer.from(gradientSvg)).png().toBuffer();

        // Create final composite
        await sharp(bgBuffer)
            .composite([
                {
                    input: Buffer.from(frameSvg),
                    left: screenX - 30,
                    top: screenY - 20
                },
                {
                    input: Buffer.from(bezelSvg),
                    left: screenX,
                    top: screenY
                },
                {
                    input: resizedScreenshot,
                    left: screenX + 4,
                    top: screenY + 4
                }
            ])
            .png()
            .toFile(outputPath);

        console.log(`Gradient mockup created: ${outputPath}`);
    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    }
}

createMockup();
