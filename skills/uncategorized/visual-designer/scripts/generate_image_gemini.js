#!/usr/bin/env node
/**
 * Visual Designer - AI Image Generation via Google Generative Language API (Imagen)
 *
 * Uses the Generative Language API endpoint which has higher/unlimited quotas
 * compared to the Vertex AI endpoint.
 *
 * Usage: node generate_image_gemini.js "Prompt text" [output_filename.png]
 *
 * Requires: GOOGLE_API_KEY in .env (get from AI Studio: aistudio.google.com)
 */

require('dotenv').config();
const fs = require('fs');
const path = require('path');
const https = require('https');

// Parse command line arguments
const prompt = process.argv[2];
const filename = process.argv[3] || 'generated_asset.png';

// Get API key from environment
const apiKey = process.env.GOOGLE_API_KEY;

// Validate input
if (!prompt) {
    console.error('Error: Prompt is required');
    console.error('Usage: node generate_image_gemini.js "Prompt text" [output_filename.png]');
    process.exit(1);
}

if (!apiKey) {
    console.error('Error: GOOGLE_API_KEY not found in environment');
    console.error('Get your API key from: https://aistudio.google.com/apikey');
    console.error('Then add to .env: GOOGLE_API_KEY=your_key_here');
    process.exit(1);
}

async function generateImage() {
    console.log(`Generating image for: "${prompt}"...`);
    console.log(`Output file: ${filename}`);

    try {
        // Generative Language API endpoint for Imagen 3
        const endpoint = `https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:generateImages?key=${apiKey}`;

        const requestBody = JSON.stringify({
            prompt: prompt,
            config: {
                numberOfImages: 1,
                aspectRatio: "1:1",
                safetyFilterLevel: "BLOCK_LOW_AND_ABOVE",
                personGeneration: "ALLOW_ADULT"
            }
        });

        const url = new URL(endpoint);
        const options = {
            hostname: url.hostname,
            path: url.pathname + url.search,
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Content-Length': Buffer.byteLength(requestBody)
            }
        };

        const response = await new Promise((resolve, reject) => {
            const req = https.request(options, (res) => {
                let data = '';
                res.on('data', chunk => data += chunk);
                res.on('end', () => {
                    if (res.statusCode >= 200 && res.statusCode < 300) {
                        resolve(JSON.parse(data));
                    } else {
                        reject(new Error(`API error (${res.statusCode}): ${data}`));
                    }
                });
            });
            req.on('error', reject);
            req.write(requestBody);
            req.end();
        });

        // Extract base64 image from response (handle both response formats)
        let imageData;
        if (response.generatedImages && response.generatedImages[0]) {
            imageData = response.generatedImages[0].image?.imageBytes || response.generatedImages[0].imageBytes;
        } else if (response.predictions && response.predictions[0]) {
            imageData = response.predictions[0].bytesBase64Encoded;
        }

        if (imageData) {
            const buffer = Buffer.from(imageData, 'base64');

            // Ensure output directory exists
            const outputDir = path.dirname(filename);
            if (outputDir && outputDir !== '.' && !fs.existsSync(outputDir)) {
                fs.mkdirSync(outputDir, { recursive: true });
            }

            fs.writeFileSync(filename, buffer);
            console.log(`Image saved to: ${filename}`);
        } else {
            console.error('Unexpected response format:', JSON.stringify(response, null, 2));
            process.exit(1);
        }

    } catch (error) {
        console.error('Error generating image:', error.message);
        process.exit(1);
    }
}

generateImage();
