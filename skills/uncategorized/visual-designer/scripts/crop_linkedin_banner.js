#!/usr/bin/env node
/**
 * Crop images to LinkedIn banner dimensions
 * LinkedIn Company Banner: 1584 x 396 pixels (4:1 ratio)
 *
 * Usage: node crop_linkedin_banner.js <input_image> <output_image>
 */

const sharp = require('sharp');
const path = require('path');
const fs = require('fs');

const inputPath = process.argv[2];
const outputPath = process.argv[3];

if (!inputPath || !outputPath) {
    console.error('Usage: node crop_linkedin_banner.js <input_image> <output_image>');
    process.exit(1);
}

const LINKEDIN_WIDTH = 1584;
const LINKEDIN_HEIGHT = 396;

async function cropToLinkedIn() {
    try {
        // Ensure output directory exists
        const outputDir = path.dirname(outputPath);
        if (outputDir && outputDir !== '.' && !fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        await sharp(inputPath)
            .resize(LINKEDIN_WIDTH, LINKEDIN_HEIGHT, {
                fit: 'cover',
                position: 'center'
            })
            .toFile(outputPath);

        console.log(`Cropped to LinkedIn banner: ${outputPath}`);
    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    }
}

cropToLinkedIn();
