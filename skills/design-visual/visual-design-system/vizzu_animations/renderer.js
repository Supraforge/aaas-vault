#!/usr/bin/env node

/**
 * Vizzu HTML renderer for animated data visualizations.
 *
 * This script renders Vizzu animations to HTML files that can be
 * converted to video using Playwright.
 */

const fs = require('fs');
const path = require('path');

// Read payload from command line argument
const payloadPath = process.argv[2];
if (!payloadPath) {
  console.error('Usage: node renderer.js <payload.json>');
  process.exit(1);
}

const payload = JSON.parse(fs.readFileSync(payloadPath, 'utf8'));
const { data, config, animation, output } = payload;

// Generate HTML with Vizzu animation
const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${config.title || 'Vizzu Animation'}</title>
  <script type="module">
    import Vizzu from 'https://cdn.jsdelivr.net/npm/vizzu@0.9/dist/vizzu.min.js';

    // Design tokens (from visual-design-system)
    const COLORS = {
      primary: '#2d6a9f',
      secondary: '#48a9a6',
      success: '#2e7d32',
      warning: '#e65100',
      danger: '#c62828',
      navy: '#1e3a5f',
      teal: '#2d7a77',
      blue: '#4477AA',
      orange: '#ee7733',
      treatment: '#0077bb',
      control: '#ee7733',
    };

    const data = ${JSON.stringify(data)};
    const config = ${JSON.stringify(config)};
    const animationConfig = ${JSON.stringify(animation)};

    // Initialize Vizzu
    const chart = new Vizzu('vizzuCanvas', { data });

    // Apply configuration and animate
    chart.initializing.then(chart => {
      const animateConfig = {
        x: config.x,
        y: config.y,
        title: config.title,
      };

      if (config.color) {
        animateConfig.color = config.color;
      }
      if (config.size) {
        animateConfig.size = config.size;
      }

      // Apply colors from design system
      const style = {
        plot: {
          marker: {
            colorPalette: [
              COLORS.blue,
              COLORS.orange,
              COLORS.success,
              COLORS.danger,
              COLORS.teal,
            ],
          },
        },
      };

      return chart.animate(
        {
          ...animateConfig,
          style,
        },
        {
          duration: animationConfig.duration || 2000,
          easing: animationConfig.easing || 'cubic-bezier(0.65,0,0.35,1)',
        }
      );
    });
  </script>
  <style>
    body {
      margin: 0;
      padding: 20px;
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
      background: #ffffff;
    }
    #vizzuCanvas {
      width: 800px;
      height: 600px;
      margin: 0 auto;
      display: block;
    }
  </style>
</head>
<body>
  <div id="vizzuCanvas"></div>
</body>
</html>`;

// Write HTML to output file
fs.writeFileSync(output, html, 'utf8');
console.log(`✅ Vizzu animation rendered to: ${output}`);
