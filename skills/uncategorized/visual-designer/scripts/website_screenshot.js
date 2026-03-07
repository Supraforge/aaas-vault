#!/usr/bin/env node
/**
 * Website Screenshot Tool
 * Takes screenshots of websites for mockup compositing
 *
 * Usage: node website_screenshot.js <url> <output_path> [width] [height] [dark_mode]
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const url = process.argv[2];
const outputPath = process.argv[3];
const width = parseInt(process.argv[4]) || 1920;
const height = parseInt(process.argv[5]) || 1080;
const darkMode = process.argv[6] === 'dark';

if (!url || !outputPath) {
    console.error('Usage: node website_screenshot.js <url> <output_path> [width] [height] [dark|light]');
    process.exit(1);
}

async function takeScreenshot() {
    console.log(`Taking screenshot of: ${url}`);
    console.log(`Dimensions: ${width}x${height}`);
    console.log(`Mode: ${darkMode ? 'dark' : 'light'}`);

    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    try {
        const page = await browser.newPage();

        // Set viewport
        await page.setViewport({ width, height, deviceScaleFactor: 2 });

        // Set color scheme preference
        await page.emulateMediaFeatures([
            { name: 'prefers-color-scheme', value: darkMode ? 'dark' : 'light' }
        ]);

        // Navigate to URL
        await page.goto(url, {
            waitUntil: 'networkidle2',
            timeout: 30000
        });

        // Wait a bit for any animations
        await new Promise(r => setTimeout(r, 2000));

        // Ensure output directory exists
        const outputDir = path.dirname(outputPath);
        if (outputDir && outputDir !== '.' && !fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        // Take screenshot
        await page.screenshot({
            path: outputPath,
            type: 'png'
        });

        console.log(`Screenshot saved: ${outputPath}`);
    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    } finally {
        await browser.close();
    }
}

takeScreenshot();
