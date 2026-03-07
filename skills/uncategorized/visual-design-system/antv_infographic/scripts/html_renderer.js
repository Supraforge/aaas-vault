#!/usr/bin/env node

/**
 * AntV Infographic HTML-based Renderer
 *
 * Creates standalone HTML files with embedded AntV Infographic specs.
 * Can be opened in browser to view/download SVG, or used with playwright-core.
 */

const fs = require('fs');
const path = require('path');

/**
 * Generate standalone HTML file with infographic
 */
function generateHTML(spec, options = {}) {
  const { width = 800, height = 600, title = 'AntV Infographic' } = options;

  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title}</title>
  <script src="https://unpkg.com/@antv/infographic@latest/dist/infographic.umd.min.js"></script>
  <style>
    body {
      margin: 0;
      padding: 20px;
      font-family: Arial, sans-serif;
      background: #f5f5f5;
    }
    #container {
      width: ${width}px;
      height: ${height}px;
      background: white;
      margin: 0 auto;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    #controls {
      text-align: center;
      margin: 20px auto;
      max-width: ${width}px;
    }
    button {
      background: #1e3a5f;
      color: white;
      border: none;
      padding: 10px 20px;
      font-size: 14px;
      cursor: pointer;
      border-radius: 4px;
      margin: 0 5px;
    }
    button:hover {
      background: #2d6a9f;
    }
    #spec-view {
      max-width: ${width}px;
      margin: 20px auto;
      padding: 15px;
      background: #f9f9f9;
      border: 1px solid #ddd;
      border-radius: 4px;
      font-family: 'Courier New', monospace;
      font-size: 12px;
      white-space: pre-wrap;
    }
  </style>
</head>
<body>
  <div id="controls">
    <button onclick="downloadSVG()">Download SVG</button>
    <button onclick="downloadPNG()">Download PNG</button>
    <button onclick="toggleSpec()">Toggle Spec</button>
  </div>

  <div id="container"></div>

  <div id="spec-view" style="display: none;"></div>

  <script>
    const spec = \`${spec.replace(/`/g, '\\`')}\`;

    // Display spec
    document.getElementById('spec-view').textContent = spec;

    // Initialize infographic
    const infographic = new Infographic.Infographic({
      container: '#container',
      width: ${width},
      height: ${height},
      editable: true,
    });

    // Render
    infographic.render(spec);

    // Download SVG
    function downloadSVG() {
      const svgElement = document.querySelector('#container svg');
      if (!svgElement) {
        alert('No SVG found');
        return;
      }

      const svgData = svgElement.outerHTML;
      const blob = new Blob([svgData], { type: 'image/svg+xml' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'infographic.svg';
      a.click();
      URL.revokeObjectURL(url);
    }

    // Download PNG
    function downloadPNG() {
      const svgElement = document.querySelector('#container svg');
      if (!svgElement) {
        alert('No SVG found');
        return;
      }

      const svgData = new XMLSerializer().serializeToString(svgElement);
      const canvas = document.createElement('canvas');
      canvas.width = ${width} * 2;  // 2x for better quality
      canvas.height = ${height} * 2;
      const ctx = canvas.getContext('2d');

      const img = new Image();
      img.onload = function() {
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
        canvas.toBlob(function(blob) {
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = 'infographic.png';
          a.click();
          URL.revokeObjectURL(url);
        });
      };

      const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
      const url = URL.createObjectURL(svgBlob);
      img.src = url;
    }

    // Toggle spec view
    function toggleSpec() {
      const specView = document.getElementById('spec-view');
      specView.style.display = specView.style.display === 'none' ? 'block' : 'none';
    }

    // Auto-extract SVG to console for programmatic access
    setTimeout(() => {
      const svgElement = document.querySelector('#container svg');
      if (svgElement) {
        console.log('=== SVG OUTPUT START ===');
        console.log(svgElement.outerHTML);
        console.log('=== SVG OUTPUT END ===');
      }
    }, 1000);
  </script>
</body>
</html>`;

  return html;
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
function main() {
  const args = process.argv.slice(2);

  if (args.includes('--help') || args.includes('-h')) {
    console.log(`
AntV Infographic HTML Renderer

USAGE:
  node html_renderer.js [OPTIONS]

OPTIONS:
  --spec <spec>         Infographic spec (YAML-like syntax)
  --template <name>     Use a template from templates/ directory
  --output <file>       Output HTML file path
  --width <pixels>      Canvas width (default: 800)
  --height <pixels>     Canvas height (default: 600)
  --title <string>      HTML page title
  --list                List available templates
  --help, -h            Show this help

EXAMPLES:
  # List templates
  node html_renderer.js --list

  # Generate HTML from template
  node html_renderer.js --template trial_result_simple --output preview.html

  # Generate HTML from spec
  node html_renderer.js --spec "infographic list-row-simple..." --output preview.html

  # Then open the HTML file in browser to view/download SVG
  open preview.html
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
  let outputPath = 'preview.html';
  let width = 800;
  let height = 600;
  let title = 'AntV Infographic';

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
      case '--title':
        title = args[++i];
        break;
    }
  }

  if (!spec) {
    console.error('Error: Either --spec or --template is required');
    process.exit(1);
  }

  try {
    const html = generateHTML(spec, { width, height, title });
    fs.writeFileSync(outputPath, html);
    console.log(`HTML file saved to: ${outputPath}`);
    console.log(`\nOpen this file in a browser to:`);
    console.log(`  - View the infographic`);
    console.log(`  - Download as SVG`);
    console.log(`  - Download as PNG`);
    console.log(`\nOr use with playwright-core for automated SVG extraction.`);
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

// Run CLI if called directly
if (require.main === module) {
  main();
}

// Export for use as module
module.exports = { generateHTML, loadTemplate, listTemplates };
