#!/usr/bin/env node
/**
 * AntV G2 Grammar-Based Chart Renderer
 *
 * Renders charts from declarative grammar specifications to PNG/SVG.
 * Supports medical chart types: forest plots, Kaplan-Meier curves,
 * multi-panel figures, and custom compositions.
 *
 * Usage:
 *   node renderer.js --spec forest_plot.json --output chart.png
 *   node renderer.js --grammar '{"type": "interval", ...}' --output chart.svg
 */

const { Chart } = require('@antv/g2');
const { createCanvas } = require('canvas');
const fs = require('fs');
const path = require('path');

// Design tokens from visual-design-system
const DESIGN_TOKENS = {
  colors: {
    primary: {
      navy: '#1e3a5f',
      blue: '#2d6a9f',
      teal: '#48a9a6'
    },
    semantic: {
      success: '#2e7d32',
      warning: '#e65100',
      danger: '#c62828',
      neutral: '#546e7a'
    },
    categorical: ['#4477AA', '#66CCEE', '#228833', '#CCBB44', '#EE6677', '#AA3377', '#BBBBBB'],
    treatment_control: ['#0077bb', '#ee7733'],
    benefit_risk: ['#009988', '#cc3311']
  },
  typography: {
    family: 'Helvetica, Arial, sans-serif',
    sizes: {
      title: 14,
      axis: 8,
      legend: 9,
      label: 7
    }
  },
  spacing: {
    padding: [40, 60, 40, 60] // top, right, bottom, left
  }
};

/**
 * Load grammar specification from file or string
 */
function loadGrammar(grammarInput) {
  if (fs.existsSync(grammarInput)) {
    const content = fs.readFileSync(grammarInput, 'utf-8');
    return JSON.parse(content);
  }
  return JSON.parse(grammarInput);
}

/**
 * Apply design tokens to grammar specification
 */
function applyDesignTokens(spec) {
  // Apply color palette if not specified
  if (spec.scale && !spec.scale.color) {
    spec.scale = spec.scale || {};
    spec.scale.color = { range: DESIGN_TOKENS.colors.categorical };
  }

  // Apply typography defaults
  if (!spec.theme) {
    spec.theme = {
      fontFamily: DESIGN_TOKENS.typography.family,
      fontSize: DESIGN_TOKENS.typography.sizes.axis
    };
  }

  return spec;
}

/**
 * Render chart from grammar specification
 */
async function renderChart(grammarSpec, options = {}) {
  const {
    width = 800,
    height = 600,
    format = 'png',
    output = 'chart.png'
  } = options;

  // Create canvas
  const canvas = createCanvas(width, height);

  // Initialize G2 chart
  const chart = new Chart({
    container: canvas,
    width,
    height,
    padding: DESIGN_TOKENS.spacing.padding,
    autoFit: false
  });

  // Apply grammar specification
  if (grammarSpec.data) {
    chart.data(grammarSpec.data);
  }

  // Apply marks (geometry layers)
  if (grammarSpec.marks) {
    grammarSpec.marks.forEach(mark => {
      const geom = chart[mark.type]();

      if (mark.encode) {
        Object.entries(mark.encode).forEach(([channel, field]) => {
          geom.encode(channel, field);
        });
      }

      if (mark.style) {
        geom.style(mark.style);
      }

      if (mark.transform) {
        mark.transform.forEach(t => {
          if (typeof t === 'string') {
            geom.transform(t);
          } else {
            geom.transform(t.type, t.options);
          }
        });
      }
    });
  }

  // Apply scales
  if (grammarSpec.scales) {
    Object.entries(grammarSpec.scales).forEach(([channel, scaleSpec]) => {
      chart.scale(channel, scaleSpec);
    });
  }

  // Apply coordinates
  if (grammarSpec.coordinate) {
    const coord = chart.coordinate();
    if (grammarSpec.coordinate.type) {
      coord.type(grammarSpec.coordinate.type);
    }
    if (grammarSpec.coordinate.transform) {
      grammarSpec.coordinate.transform.forEach(t => {
        coord.transform(t);
      });
    }
  }

  // Apply axes
  if (grammarSpec.axes !== false) {
    chart.axis('x', {
      title: grammarSpec.xAxis?.title || null,
      labelFontSize: DESIGN_TOKENS.typography.sizes.axis,
      ...grammarSpec.xAxis
    });
    chart.axis('y', {
      title: grammarSpec.yAxis?.title || null,
      labelFontSize: DESIGN_TOKENS.typography.sizes.axis,
      ...grammarSpec.yAxis
    });
  }

  // Apply legend
  if (grammarSpec.legend !== false) {
    chart.legend({
      position: 'bottom',
      fontSize: DESIGN_TOKENS.typography.sizes.legend,
      ...grammarSpec.legend
    });
  }

  // Apply interactions
  if (grammarSpec.interactions) {
    grammarSpec.interactions.forEach(interaction => {
      chart.interaction(interaction);
    });
  }

  // Render chart
  await chart.render();

  // Export to file
  const buffer = canvas.toBuffer(format === 'svg' ? 'image/svg+xml' : 'image/png');
  fs.writeFileSync(output, buffer);

  console.log(`✅ Chart rendered: ${output}`);
  console.log(`   Resolution: ${width}x${height}px`);
  console.log(`   Format: ${format.toUpperCase()}`);

  return output;
}

/**
 * Load medical grammar template
 */
function loadMedicalTemplate(templateName, data) {
  const templatePath = path.join(__dirname, 'templates', `${templateName}.json`);

  if (!fs.existsSync(templatePath)) {
    throw new Error(`Template not found: ${templateName}`);
  }

  const template = JSON.parse(fs.readFileSync(templatePath, 'utf-8'));

  // Inject data into template
  if (data) {
    template.data = data;
  }

  return template;
}

/**
 * List available templates
 */
function listTemplates() {
  const templatesDir = path.join(__dirname, 'templates');

  if (!fs.existsSync(templatesDir)) {
    console.log('No templates directory found.');
    return;
  }

  const templates = fs.readdirSync(templatesDir)
    .filter(f => f.endsWith('.json'))
    .map(f => f.replace('.json', ''));

  console.log('\n📊 Available G2 Medical Templates:\n');
  templates.forEach((t, i) => {
    console.log(`   ${i + 1}. ${t}`);
  });
  console.log('');
}

// CLI interface
if (require.main === module) {
  const args = process.argv.slice(2);

  const parseArgs = () => {
    const parsed = {
      spec: null,
      grammar: null,
      template: null,
      data: null,
      output: 'chart.png',
      width: 800,
      height: 600,
      format: 'png',
      list: false
    };

    for (let i = 0; i < args.length; i++) {
      const arg = args[i];
      const next = args[i + 1];

      switch (arg) {
        case '--spec':
        case '-s':
          parsed.spec = next;
          i++;
          break;
        case '--grammar':
        case '-g':
          parsed.grammar = next;
          i++;
          break;
        case '--template':
        case '-t':
          parsed.template = next;
          i++;
          break;
        case '--data':
        case '-d':
          parsed.data = next;
          i++;
          break;
        case '--output':
        case '-o':
          parsed.output = next;
          i++;
          break;
        case '--width':
        case '-w':
          parsed.width = parseInt(next);
          i++;
          break;
        case '--height':
        case '-h':
          parsed.height = parseInt(next);
          i++;
          break;
        case '--format':
        case '-f':
          parsed.format = next;
          i++;
          break;
        case '--list':
        case '-l':
          parsed.list = true;
          break;
      }
    }

    return parsed;
  };

  const options = parseArgs();

  if (options.list) {
    listTemplates();
    process.exit(0);
  }

  if (args.length === 0) {
    console.log(`
AntV G2 Grammar-Based Chart Renderer

Usage:
  node renderer.js --spec <grammar.json> --output <chart.png>
  node renderer.js --template <name> --data <data.json> --output <chart.png>
  node renderer.js --grammar '{"type": "interval", ...}' --output <chart.svg>
  node renderer.js --list

Options:
  --spec, -s       Grammar specification file (JSON)
  --grammar, -g    Inline grammar specification (JSON string)
  --template, -t   Medical template name
  --data, -d       Data file for template (JSON/CSV)
  --output, -o     Output file path (default: chart.png)
  --width, -w      Chart width in pixels (default: 800)
  --height, -h     Chart height in pixels (default: 600)
  --format, -f     Output format: png or svg (default: png)
  --list, -l       List available medical templates

Examples:
  node renderer.js --template forest_plot --data trials.json -o forest.png
  node renderer.js --spec custom_grammar.json -o chart.svg --format svg
  node renderer.js --list
    `);
    process.exit(0);
  }

  // Load grammar
  let grammar;

  if (options.template) {
    const data = options.data ? JSON.parse(fs.readFileSync(options.data, 'utf-8')) : null;
    grammar = loadMedicalTemplate(options.template, data);
  } else if (options.spec) {
    grammar = loadGrammar(options.spec);
  } else if (options.grammar) {
    grammar = JSON.parse(options.grammar);
  } else {
    console.error('❌ Provide --spec, --grammar, or --template');
    process.exit(1);
  }

  // Apply design tokens
  grammar = applyDesignTokens(grammar);

  // Render chart
  renderChart(grammar, {
    width: options.width,
    height: options.height,
    format: options.format,
    output: options.output
  }).catch(err => {
    console.error('❌ Rendering failed:', err.message);
    process.exit(1);
  });
}

module.exports = { renderChart, loadMedicalTemplate, applyDesignTokens };
