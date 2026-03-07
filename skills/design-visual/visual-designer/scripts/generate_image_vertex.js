#!/usr/bin/env node
/**
 * Visual Designer - AI Image Generation via Google Vertex AI (Imagen)
 *
 * Uses Google Cloud Vertex AI Imagen for image generation.
 *
 * Usage: node generate_image_vertex.js "Prompt text" [output_filename.png]
 *
 * Requires: gcloud CLI authenticated with Vertex AI enabled project
 */

const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');
const https = require('https');

// Parse command line arguments
const prompt = process.argv[2];
const filename = process.argv[3] || 'generated_asset.png';
const aspectRatio = process.argv[4] || '1:1'; // Supported: 1:1, 16:9, 9:16, 4:3, 3:4

// Validate input
if (!prompt) {
    console.error('Error: Prompt is required');
    console.error('Usage: node generate_image_vertex.js "Prompt text" [output_filename.png]');
    process.exit(1);
}

async function getAccessToken() {
    return new Promise((resolve, reject) => {
        exec('gcloud auth print-access-token', (error, stdout, stderr) => {
            if (error) {
                reject(new Error(`Failed to get access token: ${stderr}`));
                return;
            }
            resolve(stdout.trim());
        });
    });
}

async function getProjectId() {
    return new Promise((resolve, reject) => {
        exec('gcloud config get-value project', (error, stdout, stderr) => {
            if (error) {
                reject(new Error(`Failed to get project ID: ${stderr}`));
                return;
            }
            resolve(stdout.trim());
        });
    });
}

async function generateImage() {
    console.log(`Generating image for: "${prompt}"...`);
    console.log(`Output file: ${filename}`);

    try {
        const accessToken = await getAccessToken();
        const projectId = await getProjectId();
        const location = 'us-central1';

        // Imagen 3 Fast model endpoint (higher quota)
        const model = process.env.IMAGEN_MODEL || 'imagen-3.0-fast-generate-001';
        const endpoint = `https://${location}-aiplatform.googleapis.com/v1/projects/${projectId}/locations/${location}/publishers/google/models/${model}:predict`;

        // ============================================================
        // HARD-CODED RULE: NEVER PRODUCE TEXT IN ANY IMAGE
        // All AI-generated text is unusable - this applies to ALL models
        // ============================================================
        const NO_TEXT_SUFFIX = ', absolutely no text, no letters, no words, no numbers, no typography, no writing, no characters, no labels, no captions, no watermarks, no logos with text, no signs, no UI text, completely text-free image only';
        let finalPrompt = prompt + NO_TEXT_SUFFIX;
        console.log('*** HARD RULE ENFORCED: No text will be generated in this image ***');

        const requestBody = JSON.stringify({
            instances: [
                {
                    prompt: finalPrompt
                }
            ],
            parameters: {
                sampleCount: 1,
                aspectRatio: aspectRatio,
                safetyFilterLevel: "block_few",
                personGeneration: "allow_adult"
            }
        });

        const url = new URL(endpoint);
        const options = {
            hostname: url.hostname,
            path: url.pathname,
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${accessToken}`,
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

        // Extract base64 image from response
        if (response.predictions && response.predictions[0] && response.predictions[0].bytesBase64Encoded) {
            const imageData = response.predictions[0].bytesBase64Encoded;
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
