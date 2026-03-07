#!/usr/bin/env node
/**
 * Website Section Screenshot Tool
 * Takes screenshots of specific sections of a website
 *
 * Usage: node screenshot_sections.js <url> [output_dir] [theme]
 *
 * Arguments:
 *   url        - REQUIRED: Website URL to capture
 *   output_dir - Output directory (default: ./screenshots)
 *   theme      - Color scheme: dark or light (default: dark)
 *
 * Example:
 *   node screenshot_sections.js "https://example.com" "./screenshots" "dark"
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

// URL is REQUIRED - no silent default to prevent using wrong website
const url = process.argv[2];

if (!url || url.startsWith('-')) {
    console.error('\n❌ ERROR: URL argument is required');
    console.error('\nUsage: node screenshot_sections.js <url> [output_dir] [theme]');
    console.error('\nArguments:');
    console.error('  url        - REQUIRED: Website URL to capture');
    console.error('  output_dir - Output directory (default: ./screenshots)');
    console.error('  theme      - Color scheme: dark or light (default: dark)');
    console.error('\nExample:');
    console.error('  node screenshot_sections.js "https://supra-forge.com" "./screenshots" "dark"');
    console.error('\n⚠️  No default URL to prevent using wrong website screenshots.\n');
    process.exit(1);
}

// Validate URL format
try {
    new URL(url);
} catch (e) {
    console.error(`\n❌ ERROR: Invalid URL format: ${url}`);
    console.error('   URL must start with http:// or https://\n');
    process.exit(1);
}

const outputDir = process.argv[3] || './screenshots';
const colorScheme = process.argv[4] || 'dark';

async function takeScreenshots() {
    console.log(`Taking section screenshots of: ${url}`);
    console.log(`Color scheme: ${colorScheme}`);

    // Ensure output directory exists
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }

    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    try {
        const page = await browser.newPage();

        // Set viewport for high-res screenshots
        await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 2 });

        // Set color scheme preference
        await page.emulateMediaFeatures([
            { name: 'prefers-color-scheme', value: colorScheme }
        ]);

        // Navigate to URL
        await page.goto(url, {
            waitUntil: 'networkidle2',
            timeout: 30000
        });

        // Wait for page to fully render
        await new Promise(r => setTimeout(r, 3000));

        // Screenshot 1: Hero section (top of page)
        await page.screenshot({
            path: path.join(outputDir, `hero_${colorScheme}.png`),
            type: 'png',
            clip: { x: 0, y: 0, width: 1920, height: 1080 }
        });
        console.log(`Saved: hero_${colorScheme}.png`);

        // Screenshot 2: Scroll down to Step section
        await page.evaluate(() => window.scrollBy(0, 600));
        await new Promise(r => setTimeout(r, 1000));
        await page.screenshot({
            path: path.join(outputDir, `step_section_${colorScheme}.png`),
            type: 'png',
            clip: { x: 0, y: 0, width: 1920, height: 1080 }
        });
        console.log(`Saved: step_section_${colorScheme}.png`);

        // Screenshot 3: Full page for variety
        await page.evaluate(() => window.scrollTo(0, 0));
        await new Promise(r => setTimeout(r, 500));
        await page.screenshot({
            path: path.join(outputDir, `full_${colorScheme}.png`),
            type: 'png'
        });
        console.log(`Saved: full_${colorScheme}.png`);

        // Mobile viewport screenshot
        await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 3 }); // iPhone 14 Pro
        await page.evaluate(() => window.scrollTo(0, 0));
        await new Promise(r => setTimeout(r, 1000));
        await page.screenshot({
            path: path.join(outputDir, `mobile_${colorScheme}.png`),
            type: 'png'
        });
        console.log(`Saved: mobile_${colorScheme}.png`);

    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    } finally {
        await browser.close();
    }

    console.log('Done!');
}

takeScreenshots();
