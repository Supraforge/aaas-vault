#!/usr/bin/env node
/**
 * Visual Designer - AI Image Generation via Puter.js
 *
 * Uses Flux.1 Schnell (free) through Puter.js for image generation.
 *
 * Usage: node generate_image.js "Prompt text" [output_filename.png]
 * 
 * Note: Requires PUTER_AUTH_TOKEN environment variable for Node.js usage.
 * Get your token from https://puter.com/app/settings/api-keys
 */

const { init } = require('@heyputer/puter.js/src/init.cjs');
const fs = require('fs');
const path = require('path');
require('dotenv').config();

// Initialize Puter with auth token
const puter = init(process.env.PUTER_AUTH_TOKEN);

// Parse command line arguments
const prompt = process.argv[2];
const filename = process.argv[3] || 'generated_asset.png';

// Validate auth token
if (!process.env.PUTER_AUTH_TOKEN) {
    console.error('Error: PUTER_AUTH_TOKEN environment variable is required');
    console.error('');
    console.error('To get your token:');
    console.error('1. Visit https://puter.com');
    console.error('2. Sign in or create an account');
    console.error('3. Go to Settings → API Keys');
    console.error('4. Create a new API key');
    console.error('5. Add it to your .env file: PUTER_AUTH_TOKEN=your_token_here');
    console.error('');
    process.exit(1);
}

// Validate input
if (!prompt) {
    console.error('Error: Prompt is required');
    console.error('Usage: node generate_image.js "Prompt text" [output_filename.png]');
    process.exit(1);
}

async function generateImage() {
    console.log(`Generating image for: "${prompt}"...`);
    console.log(`Output file: ${filename}`);

    try {
        // Generate image using Flux.1 Schnell via Puter
        const image = await puter.ai.txt2img(prompt, {
            model: 'black-forest-labs/FLUX.1-schnell'
        });

        // Ensure output directory exists
        const outputDir = path.dirname(filename);
        if (outputDir && outputDir !== '.' && !fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        // Handle the response - Puter returns image data
        if (image && image.data) {
            // If image.data is a base64 string
            const buffer = Buffer.from(image.data, 'base64');
            fs.writeFileSync(filename, buffer);
            console.log(`Image saved to: ${filename}`);
        } else if (image && image.url) {
            // If Puter returns a URL, fetch and save it
            const response = await fetch(image.url);
            const arrayBuffer = await response.arrayBuffer();
            const buffer = Buffer.from(arrayBuffer);
            fs.writeFileSync(filename, buffer);
            console.log(`Image saved to: ${filename}`);
        } else if (Buffer.isBuffer(image)) {
            // Direct buffer response
            fs.writeFileSync(filename, image);
            console.log(`Image saved to: ${filename}`);
        } else {
            // Log the response for debugging
            console.log('Puter response:', JSON.stringify(image, null, 2));
            console.log('Image generated successfully via Puter.');
        }

    } catch (error) {
        console.error('Error generating image:', error.message);
        if (error.code === 'MODULE_NOT_FOUND') {
            console.error('\nTip: Run "npm install @heyputer/puter.js" in the project root');
        }
        process.exit(1);
    }
}

generateImage();
