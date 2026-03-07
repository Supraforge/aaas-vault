#!/usr/bin/env node

/**
 * AntV Infographic Node.js Renderer
 *
 * Renders AntV Infographic specs to SVG using headless browser environment.
 * Supports both direct spec input and template-based generation.
 */

const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

/**
 * Setup JSDOM for server-side rendering
 */
function setupDOM() {
  const dom = new JSDOM('<!DOCTYPE html><html><body><div id="container"></div></body></html>', {
    url: 'http://localhost',
    pretendToBeVisual: true,
    resources: 'usable',
  });

  global.window = dom.window;
  global.document = dom.window.document;
  global.navigator = dom.window.navigator;
  global.HTMLElement = dom.window.HTMLElement;
  global.SVGElement = dom.window.SVGElement;

  return dom;
}

/**
 * Render infographic from spec to SVG
 */
async function render(spec, options = {}) {
  const { width = 800, height = 600 } = options;

  // Setup DOM environment
  const dom = setupDOM();
  const container = dom.window.document.getElementById('container');

  try {
    // Import AntV Infographic (must be after DOM setup)
    const { Infographic } = require('@antv/infographic');

    // Create infographic instance
    const infographic = new Infographic({
      container,
      width,
      height,
      editable: false,
    });

    // Render the spec
    await infographic.render(spec);

    // Extract SVG
    const svgElement = container.querySelector('svg');
    if (!svgElement) {
      throw new Error('No SVG element generated');
    }

    return svgElement.outerHTML;

  } catch (error) {
    throw new Error(`Render failed: ${error.message}`);
  } finally {
    dom.window.close();
  }
}

/**
 * Load template from templates directory
 */
function loadTemplate(templateName) {
  const templatePath = path.join(__dirname, '../templates', `${templateName}.txt`);
  if (!fs.existsSync(templatePath)) {
    throw new Error(`Template not found: ${templateName}`);
  }
  return fs.readFileSync(templatePath, 'utf-8');
}

/**
 * List available templates
 */
function listTemplates() {
  const templatesDir = path.join(__dirname, '../templates');
  if (!fs.existsSync(templatesDir)) {
    return [];
  }
  return fs.readdirSync(templatesDir)
    .filter(f => f.endsWith('.txt'))
    .map(f => f.replace('.txt', ''));
}

/**
 * CLI Interface
 */
async function main() {
  const args = process.argv.slice(2);

  if (args.includes('--help') || args.includes('-h')) {
    console.log(`
AntV Infographic Renderer

USAGE:
  node renderer.js [OPTIONS]

OPTIONS:
  --spec <spec>         Infographic spec (YAML-like syntax)
  --template <name>     Use a template from templates/ directory
  --output <file>       Output SVG file path
  --width <pixels>      Canvas width (default: 800)
  --height <pixels>     Canvas height (default: 600)
  --list                List available templates
  --help, -h            Show this help

EXAMPLES:
  # List templates
  node renderer.js --list

  # Render from template
  node renderer.js --template trial_result --output output.svg

  # Render from spec
  node renderer.js --spec "infographic list-row-simple..." --output output.svg
    `);
    process.exit(0);
  }

  if (args.includes('--list')) {
    const templates = listTemplates();
    console.log('Available templates:');
    templates.forEach(t => console.log(`  - ${t}`));
    process.exit(0);
  }

  // Parse arguments
  let spec = null;
  let outputPath = null;
  let width = 800;
  let height = 600;

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '--spec':
        spec = args[++i];
        break;
      case '--template':
        const templateName = args[++i];
        spec = loadTemplate(templateName);
        break;
      case '--output':
        outputPath = args[++i];
        break;
      case '--width':
        width = parseInt(args[++i]);
        break;
      case '--height':
        height = parseInt(args[++i]);
        break;
    }
  }

  if (!spec) {
    console.error('Error: Either --spec or --template is required');
    process.exit(1);
  }

  try {
    const svg = await render(spec, { width, height });

    if (outputPath) {
      fs.writeFileSync(outputPath, svg);
      console.log(`SVG saved to: ${outputPath}`);
    } else {
      console.log(svg);
    }

  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

// Run CLI if called directly
if (require.main === module) {
  main().catch(error => {
    console.error('Fatal error:', error);
    process.exit(1);
  });
}

// Export for use as module
module.exports = { render, loadTemplate, listTemplates };
