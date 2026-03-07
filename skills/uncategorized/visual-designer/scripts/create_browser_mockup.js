#!/usr/bin/env node
/**
 * Browser Window Mockup Creator
 * Creates clean browser window mockups with website screenshots
 */

const sharp = require('sharp');
const path = require('path');
const fs = require('fs');

const screenshotPath = process.argv[2];
const outputPath = process.argv[3];
const theme = process.argv[4] || 'dark';

if (!screenshotPath || !outputPath) {
    console.error('Usage: node create_browser_mockup.js <screenshot> <output> [dark|light]');
    process.exit(1);
}

async function createMockup() {
    try {
        const canvasSize = 1200;
        const isDark = theme === 'dark';

        // Colors
        const bgColor = isDark ? '#0F172A' : '#F8FAFC';
        const browserBg = isDark ? '#1E293B' : '#FFFFFF';
        const browserBorder = isDark ? '#334155' : '#E2E8F0';
        const dotRed = '#EF4444';
        const dotYellow = '#F59E0B';
        const dotGreen = '#22C55E';
        const urlBarBg = isDark ? '#0F172A' : '#F1F5F9';

        // Browser dimensions
        const browserWidth = Math.round(canvasSize * 0.85);
        const browserHeight = Math.round(canvasSize * 0.75);
        const toolbarHeight = 44;
        const borderRadius = 12;

        // Position
        const browserX = Math.round((canvasSize - browserWidth) / 2);
        const browserY = Math.round((canvasSize - browserHeight) / 2) - 20;

        // Resize screenshot to fit browser content area
        const contentWidth = browserWidth - 4;
        const contentHeight = browserHeight - toolbarHeight - 4;

        const resizedScreenshot = await sharp(screenshotPath)
            .resize(contentWidth, contentHeight, {
                fit: 'cover',
                position: 'top'
            })
            .toBuffer();

        // Create browser frame SVG
        const browserSvg = `
        <svg width="${canvasSize}" height="${canvasSize}" xmlns="http://www.w3.org/2000/svg">
            <!-- Background -->
            <rect width="100%" height="100%" fill="${bgColor}"/>

            <!-- Browser shadow -->
            <defs>
                <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
                    <feDropShadow dx="0" dy="8" stdDeviation="20" flood-color="${isDark ? '#000' : '#64748b'}" flood-opacity="${isDark ? '0.4' : '0.15'}"/>
                </filter>
            </defs>

            <!-- Browser window -->
            <rect x="${browserX}" y="${browserY}" width="${browserWidth}" height="${browserHeight}"
                  rx="${borderRadius}" ry="${borderRadius}"
                  fill="${browserBg}" stroke="${browserBorder}" stroke-width="1"
                  filter="url(#shadow)"/>

            <!-- Toolbar -->
            <rect x="${browserX}" y="${browserY}" width="${browserWidth}" height="${toolbarHeight}"
                  rx="${borderRadius}" ry="${borderRadius}"
                  fill="${browserBg}"/>
            <rect x="${browserX}" y="${browserY + toolbarHeight - borderRadius}" width="${browserWidth}" height="${borderRadius}"
                  fill="${browserBg}"/>

            <!-- Traffic lights -->
            <circle cx="${browserX + 20}" cy="${browserY + toolbarHeight/2}" r="6" fill="${dotRed}"/>
            <circle cx="${browserX + 40}" cy="${browserY + toolbarHeight/2}" r="6" fill="${dotYellow}"/>
            <circle cx="${browserX + 60}" cy="${browserY + toolbarHeight/2}" r="6" fill="${dotGreen}"/>

            <!-- URL bar -->
            <rect x="${browserX + 80}" y="${browserY + 10}" width="${browserWidth - 100}" height="${toolbarHeight - 20}"
                  rx="6" ry="6" fill="${urlBarBg}"/>

            <!-- Toolbar bottom border -->
            <line x1="${browserX}" y1="${browserY + toolbarHeight}" x2="${browserX + browserWidth}" y2="${browserY + toolbarHeight}"
                  stroke="${browserBorder}" stroke-width="1"/>
        </svg>`;

        // Ensure output directory exists
        const outputDir = path.dirname(outputPath);
        if (outputDir && outputDir !== '.' && !fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        // Create final composite
        await sharp(Buffer.from(browserSvg))
            .composite([
                {
                    input: resizedScreenshot,
                    left: browserX + 2,
                    top: browserY + toolbarHeight + 2
                }
            ])
            .png()
            .toFile(outputPath);

        console.log(`Browser mockup created: ${outputPath}`);
    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    }
}

createMockup();
