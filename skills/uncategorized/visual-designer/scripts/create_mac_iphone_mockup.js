#!/usr/bin/env node
/**
 * Mac + iPhone Combined Mockup Creator
 * Creates premium mockups with MacBook and iPhone side by side
 */

const sharp = require('sharp');
const path = require('path');
const fs = require('fs');

const desktopScreenshot = process.argv[2];
const mobileScreenshot = process.argv[3];
const outputPath = process.argv[4];
const theme = process.argv[5] || 'dark';

if (!desktopScreenshot || !mobileScreenshot || !outputPath) {
    console.error('Usage: node create_mac_iphone_mockup.js <desktop_screenshot> <mobile_screenshot> <output> [dark|light]');
    process.exit(1);
}

async function createMockup() {
    try {
        const canvasWidth = 1200;
        const canvasHeight = 1200;
        const isDark = theme === 'dark';

        // Colors
        const bgColor = isDark ? '#0F172A' : '#F8FAFC';
        const deviceColor = isDark ? '#1E293B' : '#374151';
        const screenBorder = isDark ? '#334155' : '#9CA3AF';
        const accentGold = '#d4a853';
        const accentBlue = '#0369A1';

        // MacBook dimensions
        const macWidth = 750;
        const macHeight = Math.round(macWidth * 0.625);
        const macScreenWidth = macWidth - 40;
        const macScreenHeight = macHeight - 60;
        const macX = 50;
        const macY = 280;

        // iPhone dimensions
        const iphoneWidth = 180;
        const iphoneHeight = 390;
        const iphoneScreenWidth = iphoneWidth - 16;
        const iphoneScreenHeight = iphoneHeight - 32;
        const iphoneX = 920;
        const iphoneY = 380;

        // Resize screenshots
        const desktopResized = await sharp(desktopScreenshot)
            .resize(macScreenWidth, macScreenHeight, { fit: 'cover', position: 'top' })
            .toBuffer();

        const mobileResized = await sharp(mobileScreenshot)
            .resize(iphoneScreenWidth, iphoneScreenHeight, { fit: 'cover', position: 'top' })
            .toBuffer();

        // Create SVG background with devices
        const svgContent = `
        <svg width="${canvasWidth}" height="${canvasHeight}" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <!-- Shadows -->
                <filter id="macShadow" x="-20%" y="-20%" width="140%" height="140%">
                    <feDropShadow dx="0" dy="20" stdDeviation="30" flood-color="${isDark ? '#000' : '#64748b'}" flood-opacity="${isDark ? '0.5' : '0.2'}"/>
                </filter>
                <filter id="iphoneShadow" x="-30%" y="-20%" width="160%" height="140%">
                    <feDropShadow dx="0" dy="15" stdDeviation="20" flood-color="${isDark ? '#000' : '#64748b'}" flood-opacity="${isDark ? '0.4' : '0.15'}"/>
                </filter>
                <!-- Gradients for background -->
                <radialGradient id="goldGlow" cx="20%" cy="30%" r="40%">
                    <stop offset="0%" stop-color="${accentGold}" stop-opacity="0.08"/>
                    <stop offset="100%" stop-color="${accentGold}" stop-opacity="0"/>
                </radialGradient>
                <radialGradient id="blueGlow" cx="80%" cy="70%" r="40%">
                    <stop offset="0%" stop-color="${accentBlue}" stop-opacity="0.06"/>
                    <stop offset="100%" stop-color="${accentBlue}" stop-opacity="0"/>
                </radialGradient>
            </defs>

            <!-- Background -->
            <rect width="100%" height="100%" fill="${bgColor}"/>
            <rect width="100%" height="100%" fill="url(#goldGlow)"/>
            <rect width="100%" height="100%" fill="url(#blueGlow)"/>

            <!-- MacBook Pro -->
            <g filter="url(#macShadow)">
                <!-- Screen bezel -->
                <rect x="${macX}" y="${macY}" width="${macWidth}" height="${macHeight - 20}"
                      rx="12" ry="12" fill="${deviceColor}"/>
                <!-- Screen -->
                <rect x="${macX + 20}" y="${macY + 12}" width="${macScreenWidth}" height="${macScreenHeight}"
                      rx="4" ry="4" fill="#000"/>
                <!-- Webcam -->
                <circle cx="${macX + macWidth/2}" cy="${macY + 8}" r="3" fill="#1a1a1a"/>
                <!-- Base/Keyboard -->
                <path d="M ${macX - 30} ${macY + macHeight - 20}
                         Q ${macX - 30} ${macY + macHeight + 5} ${macX} ${macY + macHeight + 5}
                         L ${macX + macWidth} ${macY + macHeight + 5}
                         Q ${macX + macWidth + 30} ${macY + macHeight + 5} ${macX + macWidth + 30} ${macY + macHeight - 20}
                         Z"
                      fill="${isDark ? '#0F172A' : '#4B5563'}"/>
                <!-- Trackpad notch -->
                <rect x="${macX + macWidth/2 - 40}" y="${macY + macHeight - 18}"
                      width="80" height="4" rx="2" fill="${isDark ? '#334155' : '#6B7280'}"/>
            </g>

            <!-- iPhone -->
            <g filter="url(#iphoneShadow)">
                <!-- Body -->
                <rect x="${iphoneX}" y="${iphoneY}" width="${iphoneWidth}" height="${iphoneHeight}"
                      rx="24" ry="24" fill="${deviceColor}" stroke="${screenBorder}" stroke-width="2"/>
                <!-- Screen -->
                <rect x="${iphoneX + 8}" y="${iphoneY + 8}" width="${iphoneScreenWidth}" height="${iphoneScreenHeight}"
                      rx="16" ry="16" fill="#000"/>
                <!-- Dynamic Island -->
                <rect x="${iphoneX + iphoneWidth/2 - 35}" y="${iphoneY + 16}"
                      width="70" height="20" rx="10" fill="#000"/>
                <!-- Home indicator -->
                <rect x="${iphoneX + iphoneWidth/2 - 40}" y="${iphoneY + iphoneHeight - 16}"
                      width="80" height="4" rx="2" fill="${isDark ? '#475569' : '#9CA3AF'}"/>
            </g>
        </svg>`;

        // Ensure output directory exists
        const outputDir = path.dirname(outputPath);
        if (outputDir && outputDir !== '.' && !fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        // Create final composite
        await sharp(Buffer.from(svgContent))
            .composite([
                // Desktop screenshot in MacBook
                {
                    input: desktopResized,
                    left: macX + 20,
                    top: macY + 12
                },
                // Mobile screenshot in iPhone
                {
                    input: mobileResized,
                    left: iphoneX + 8,
                    top: iphoneY + 8
                }
            ])
            .png()
            .toFile(outputPath);

        console.log(`Mac + iPhone mockup created: ${outputPath}`);
    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    }
}

createMockup();
