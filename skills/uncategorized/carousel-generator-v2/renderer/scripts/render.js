#!/usr/bin/env node

/**
 * Carousel Slide Renderer using Puppeteer
 *
 * Usage:
 *   node render.js --input slides.json --output ./output
 *   node render.js --slide '{"type":"hook","data":{...}}' --output slide.png
 *
 * The script expects either:
 * - A JSON file with an array of slides
 * - A single slide JSON object via --slide argument
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');
const os = require('os');
const { spawn } = require('child_process');

const RENDERER_DIR = path.resolve(__dirname, '..');
const DEFAULT_OUTPUT_DIR = path.join(RENDERER_DIR, 'output');
const DEV_SERVER_PORT = 3001;
const STATIC_SERVER_PORT = 3002;
const DEV_SERVER_HOST = '127.0.0.1';
const BUILD_DIR = path.join(RENDERER_DIR, 'dist');

// Start Vite dev server
function startDevServer() {
  return new Promise((resolve, reject) => {
    console.log('Starting Vite dev server...');

    const vite = spawn('npm', ['run', 'dev', '--', '--host', DEV_SERVER_HOST, '--port', DEV_SERVER_PORT.toString()], {
      cwd: RENDERER_DIR,
      stdio: ['pipe', 'pipe', 'pipe'],
      shell: true
    });

    let serverReady = false;

    const handleOutput = async (data, source) => {
      const output = data.toString();
      if ((output.includes('Local:') || output.includes('http://') || output.includes('ready in')) && !serverReady) {
        serverReady = true;
        console.log('Vite dev server detected ready signal');
        // Wait a bit for server to fully initialize (fix race condition)
        await delay(1500);
        console.log('Vite dev server ready');
        resolve(vite);
      }
    };

    vite.stdout.on('data', (data) => handleOutput(data, 'stdout'));

    vite.stderr.on('data', (data) => {
      // Vite outputs to stderr sometimes
      handleOutput(data, 'stderr');
    });

    vite.on('error', (err) => {
      reject(new Error(`Failed to start Vite: ${err.message}`));
    });

    // Timeout after 60 seconds (increased from 30s)
    setTimeout(() => {
      if (!serverReady) {
        vite.kill();
        reject(new Error('Vite dev server startup timeout (60s)'));
      }
    }, 60000);
  });
}

function buildStaticSite() {
  return new Promise((resolve, reject) => {
    console.log('Building static renderer...');
    const build = spawn('npm', ['run', 'build'], {
      cwd: RENDERER_DIR,
      stdio: ['pipe', 'pipe', 'pipe'],
      shell: true
    });

    build.on('error', (err) => {
      reject(new Error(`Failed to run build: ${err.message}`));
    });

    build.on('close', (code) => {
      if (code === 0) {
        resolve();
      } else {
        reject(new Error(`Build failed with exit code ${code}`));
      }
    });
  });
}

// Start a simple static file server for the built files
function startStaticServer() {
  return new Promise((resolve, reject) => {
    console.log('Starting static file server...');

    // Use npx serve for a simple static server
    const server = spawn('npx', ['serve', BUILD_DIR, '-l', STATIC_SERVER_PORT.toString(), '-s'], {
      cwd: RENDERER_DIR,
      stdio: ['pipe', 'pipe', 'pipe'],
      shell: true
    });

    let serverReady = false;

    const handleOutput = async (data) => {
      const output = data.toString();
      if ((output.includes('Accepting connections') || output.includes('http://') || output.includes('Serving')) && !serverReady) {
        serverReady = true;
        await delay(500);
        console.log('Static server ready');
        resolve(server);
      }
    };

    server.stdout.on('data', handleOutput);
    server.stderr.on('data', handleOutput);

    server.on('error', (err) => {
      reject(new Error(`Failed to start static server: ${err.message}`));
    });

    // Timeout after 30 seconds
    setTimeout(() => {
      if (!serverReady) {
        server.kill();
        reject(new Error('Static server startup timeout'));
      }
    }, 30000);
  });
}

async function resolveRenderTarget() {
  try {
    const viteProcess = await startDevServer();
    return {
      renderUrl: `http://${DEV_SERVER_HOST}:${DEV_SERVER_PORT}?mode=render`,
      serverProcess: viteProcess
    };
  } catch (err) {
    console.warn(`Dev server failed (${err.message}). Falling back to static build...`);
    const indexPath = path.join(BUILD_DIR, 'index.html');
    if (!fs.existsSync(indexPath)) {
      await buildStaticSite();
    }

    // Start a proper HTTP server instead of using file:// protocol
    try {
      const staticServer = await startStaticServer();
      return {
        renderUrl: `http://${DEV_SERVER_HOST}:${STATIC_SERVER_PORT}?mode=render`,
        serverProcess: staticServer
      };
    } catch (serverErr) {
      // Ultimate fallback: use file:// but warn about limitations
      console.warn(`Static server failed (${serverErr.message}). Using file:// protocol (may have limitations)...`);
      return {
        renderUrl: `file://${indexPath}?mode=render`,
        serverProcess: null
      };
    }
  }
}

// Helper to wait
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// Render a single slide
async function renderSlide(page, renderUrl, slideData, outputPath) {
  console.log(`Rendering ${slideData.type} slide to ${outputPath}...`);

  // Set slide data in localStorage before navigating
  await page.evaluateOnNewDocument((data) => {
    localStorage.setItem('slideData', JSON.stringify(data));
  }, slideData);

  // Navigate to render mode
  await page.goto(renderUrl, {
    waitUntil: 'networkidle0'
  });

  // Also try setting via window function
  await page.evaluate((data) => {
    if (window.setSlideData) {
      window.setSlideData(data);
    }
  }, slideData);

  // Wait for the slide to render (increased timeout for complex slides)
  await page.waitForSelector('#slide-container', { timeout: 30000 });
  await delay(1000); // Extra time for React to re-render and images to load

  // Get the slide element
  const slideElement = await page.$('#slide-container');
  if (!slideElement) {
    throw new Error('Slide container not found');
  }

  // Take screenshot
  await slideElement.screenshot({
    path: outputPath,
    type: 'png'
  });

  console.log(`Saved: ${outputPath}`);
}

// Main function
async function main() {
  const args = process.argv.slice(2);

  // Parse arguments
  let inputFile = null;
  let singleSlide = null;
  let outputDir = DEFAULT_OUTPUT_DIR;
  let outputFile = null;
  let width = 1080;
  let height = 1080;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--input' && args[i + 1]) {
      inputFile = args[++i];
    } else if (args[i] === '--slide' && args[i + 1]) {
      singleSlide = JSON.parse(args[++i]);
    } else if (args[i] === '--output' && args[i + 1]) {
      const out = args[++i];
      if (out.endsWith('.png')) {
        outputFile = out;
      } else {
        outputDir = out;
      }
    } else if (args[i] === '--width' && args[i + 1]) {
      width = parseInt(args[++i], 10);
    } else if (args[i] === '--height' && args[i + 1]) {
      height = parseInt(args[++i], 10);
    } else if (args[i] === '--help') {
      console.log(`
Carousel Slide Renderer

Usage:
  node render.js --input slides.json --output ./output
  node render.js --slide '{"type":"hook","data":{...}}' --output slide.png

Options:
  --input    Path to JSON file with array of slides
  --slide    Single slide JSON object
  --output   Output directory (for multiple slides) or file path (for single slide)
  --width    Output width (default 1080)
  --height   Output height (default 1080)
  --help     Show this help message

Slide Types:
  hook   - Hook/intro slide
  myth   - Myth vs Truth slide
  stat   - Statistics slide
  tips   - Tips/list slide
  cta    - Call-to-action slide
`);
      process.exit(0);
    }
  }

  // Load slides
  let slides = [];
  if (singleSlide) {
    slides = [singleSlide];
  } else if (inputFile) {
    const content = fs.readFileSync(inputFile, 'utf-8');
    slides = JSON.parse(content);
    if (!Array.isArray(slides)) {
      slides = [slides];
    }
  } else {
    console.error('Error: Please provide --input or --slide argument');
    process.exit(1);
  }

  // Create output directory
  if (!outputFile) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  // Start dev server
  const { renderUrl, serverProcess } = await resolveRenderTarget();

  // Launch browser with temporary profile (auto-cleaned)
  const userDataDir = fs.mkdtempSync(path.join(os.tmpdir(), 'puppeteer-carousel-'));

  const browser = await puppeteer.launch({
    headless: 'new',
    userDataDir,
    ignoreDefaultArgs: ['--enable-crashpad'],
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-crashpad',
      '--disable-breakpad',
      '--disable-gpu',
      '--disable-dev-shm-usage'
    ]
  });

  try {
    const page = await browser.newPage();

    // Set viewport to match slide dimensions
    await page.setViewport({
      width,
      height,
      deviceScaleFactor: 2 // Retina quality
    });

    // Render each slide
    for (let i = 0; i < slides.length; i++) {
      const slide = slides[i];
      const filename = outputFile || path.join(outputDir, `slide_${String(i + 1).padStart(2, '0')}.png`);

      await renderSlide(page, renderUrl, slide, filename);
    }

    console.log(`\nRendered ${slides.length} slide(s) successfully!`);
  } finally {
    await browser.close();
    if (serverProcess) {
      serverProcess.kill();
    }
    // Clean up temp profile directory
    try {
      fs.rmSync(userDataDir, { recursive: true, force: true });
    } catch (cleanupErr) {
      // Ignore cleanup errors - OS will clean temp eventually
    }
  }
}

// Run if called directly
if (require.main === module) {
  main().catch((err) => {
    console.error('Error:', err.message);
    process.exit(1);
  });
}

module.exports = { renderSlide, startDevServer };
