#!/usr/bin/env node
/**
 * Satori Renderer - React to SVG to PNG Pipeline
 *
 * Converts React-like JSX objects to publication-grade PNG images.
 * Uses Vercel's Satori for SVG generation and resvg for PNG conversion.
 *
 * Usage:
 *   node renderer.js --template stat-card --data '{"value": "42%", "label": "Reduction"}' --output chart.png
 *   echo '{"template": "stat-card", "data": {...}}' | node renderer.js --stdin
 */

const satori = require('satori').default;
const { Resvg } = require('@resvg/resvg-js');
const fs = require('fs');
const path = require('path');

// Load design tokens
const tokensPath = path.join(__dirname, '..', 'tokens');
const colors = JSON.parse(fs.readFileSync(path.join(tokensPath, 'colors.json'), 'utf8'));
const typography = JSON.parse(fs.readFileSync(path.join(tokensPath, 'typography.json'), 'utf8'));
const spacing = JSON.parse(fs.readFileSync(path.join(tokensPath, 'spacing.json'), 'utf8'));
const carouselBrandTokens = JSON.parse(
  fs.readFileSync(
    path.join(__dirname, '..', '..', 'carousel-generator-v2', 'tokens', 'brand-tokens.json'),
    'utf8'
  )
);

// Load carousel templates
const carouselTemplates = require('./carousel-templates');

// Load infographic templates (world-class visual system)
const infographicTemplates = require('./infographic-templates');

// Template registry
const templates = {};

/**
 * Register a template function
 */
function registerTemplate(name, templateFn) {
  templates[name] = templateFn;
}

// Register carousel templates
carouselTemplates.registerAll(registerTemplate);

// Register infographic templates
infographicTemplates.registerAll(registerTemplate);

/**
 * Get a color from tokens
 */
function getColor(path) {
  const parts = path.split('.');
  let current = colors;
  for (const part of parts) {
    current = current[part];
  }
  return current?.value || current;
}

function getBrandColor(name) {
  return carouselBrandTokens?.colors?.[name]?.value || name;
}

/**
 * Get font size in pixels
 */
function getFontSize(context, element) {
  return typography.sizes?.[context]?.[element]?.pixels || 16;
}

/**
 * Load font files for Satori
 */
async function loadFonts() {
  const fontsDir = path.join(__dirname, 'fonts');
  const fonts = [];

  // Font priority: Helvetica/Arial (publication standard) > Roboto (bundled fallback)
  const fontFiles = [
    { name: 'Helvetica', file: 'Helvetica.ttf', weight: 400 },
    { name: 'Helvetica', file: 'Helvetica-Bold.ttf', weight: 700 },
    { name: 'Arial', file: 'Arial.ttf', weight: 400 },
    { name: 'Arial', file: 'Arial-Bold.ttf', weight: 700 },
    { name: 'Roboto', file: 'Roboto-Regular.ttf', weight: 400 },
    { name: 'Roboto', file: 'Roboto-Bold.ttf', weight: 700 },
  ];

  for (const font of fontFiles) {
    const fontPath = path.join(fontsDir, font.file);
    if (fs.existsSync(fontPath)) {
      try {
        fonts.push({
          name: font.name,
          data: fs.readFileSync(fontPath),
          weight: font.weight,
          style: 'normal',
        });
      } catch (e) {
        console.error(`Warning: Could not load font ${font.file}:`, e.message);
      }
    }
  }

  if (fonts.length === 0) {
    throw new Error('No fonts found. Please add font files to the fonts/ directory.');
  }

  return fonts;
}

/**
 * Render a template to SVG
 */
async function renderToSvg(templateName, data, options = {}) {
  const width = options.width || 1200;
  const height = options.height || 630;

  const template = templates[templateName];
  if (!template) {
    throw new Error(`Template '${templateName}' not found. Available: ${Object.keys(templates).join(', ')}`);
  }

  const element = template(data, { getColor, getFontSize, colors, typography, spacing });
  const fonts = await loadFonts();

  const svg = await satori(element, {
    width,
    height,
    fonts: fonts.length > 0 ? fonts : undefined,
  });

  return svg;
}

/**
 * Convert SVG to PNG
 */
function svgToPng(svg, options = {}) {
  const scale = options.scale || 2; // 2x for retina/print quality

  const resvg = new Resvg(svg, {
    fitTo: {
      mode: 'zoom',
      value: scale,
    },
    font: {
      loadSystemFonts: true,
    },
  });

  const pngData = resvg.render();
  return pngData.asPng();
}

/**
 * Full render pipeline: template → SVG → PNG
 */
async function render(templateName, data, options = {}) {
  const svg = await renderToSvg(templateName, data, options);
  const png = svgToPng(svg, options);
  return { svg, png };
}

/**
 * Save rendered output to files
 */
async function renderToFile(templateName, data, outputPath, options = {}) {
  const { svg, png } = await render(templateName, data, options);

  // Save PNG
  fs.writeFileSync(outputPath, png);

  // Optionally save SVG
  if (options.saveSvg) {
    const svgPath = outputPath.replace(/\.png$/, '.svg');
    fs.writeFileSync(svgPath, svg);
  }

  return { outputPath, size: png.length };
}

// ============================================
// TEMPLATES
// ============================================

/**
 * Stat Card - Big number with context
 *
 * Data: { value: "42%", label: "Risk Reduction", sublabel: "HR 0.58, 95% CI 0.45-0.75", source: "DAPA-HF Trial" }
 */
registerTemplate('stat-card', (data, { getColor }) => {
  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        width: '100%',
        height: '100%',
        backgroundColor: getColor('backgrounds.light_gray'),
        padding: '60px',
        fontFamily: 'Helvetica, Arial, sans-serif',
      },
      children: [
        {
          type: 'div',
          props: {
            style: {
              fontSize: '120px',
              fontWeight: 'bold',
              color: getColor('primary.navy'),
              lineHeight: 1.1,
            },
            children: data.value || '—',
          },
        },
        {
          type: 'div',
          props: {
            style: {
              fontSize: '32px',
              fontWeight: '600',
              color: getColor('text.primary'),
              marginTop: '20px',
              textAlign: 'center',
            },
            children: data.label || '',
          },
        },
        data.sublabel ? {
          type: 'div',
          props: {
            style: {
              fontSize: '20px',
              color: getColor('text.secondary'),
              marginTop: '12px',
              fontStyle: 'italic',
            },
            children: data.sublabel,
          },
        } : null,
        data.source ? {
          type: 'div',
          props: {
            style: {
              fontSize: '14px',
              color: getColor('text.muted'),
              marginTop: '40px',
              borderTop: `1px solid ${getColor('backgrounds.medium_gray')}`,
              paddingTop: '20px',
            },
            children: `Source: ${data.source}`,
          },
        } : null,
      ].filter(Boolean),
    },
  };
});

/**
 * Comparison - Side by side comparison
 *
 * Data: {
 *   title: "Treatment vs Control",
 *   left: { value: "12%", label: "Treatment", color: "treatment" },
 *   right: { value: "18%", label: "Control", color: "control" },
 *   metric: "Event Rate",
 *   source: "Trial Name"
 * }
 */
registerTemplate('comparison', (data, { getColor }) => {
  const leftColor = data.left?.color === 'treatment' ? '#0077bb' : getColor('primary.blue');
  const rightColor = data.right?.color === 'control' ? '#ee7733' : getColor('semantic.neutral');

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        width: '100%',
        height: '100%',
        backgroundColor: getColor('backgrounds.white'),
        padding: '50px',
        fontFamily: 'Helvetica, Arial, sans-serif',
      },
      children: [
        // Title
        {
          type: 'div',
          props: {
            style: {
              fontSize: '28px',
              fontWeight: 'bold',
              color: getColor('text.primary'),
              marginBottom: '40px',
              textAlign: 'center',
            },
            children: data.title || 'Comparison',
          },
        },
        // Comparison boxes
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flex: 1,
              gap: '40px',
              justifyContent: 'center',
              alignItems: 'center',
            },
            children: [
              // Left box
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    backgroundColor: getColor('backgrounds.light_gray'),
                    borderLeft: `6px solid ${leftColor}`,
                    padding: '40px 60px',
                    borderRadius: '8px',
                  },
                  children: [
                    {
                      type: 'div',
                      props: {
                        style: { fontSize: '72px', fontWeight: 'bold', color: leftColor },
                        children: data.left?.value || '—',
                      },
                    },
                    {
                      type: 'div',
                      props: {
                        style: { fontSize: '20px', color: getColor('text.secondary'), marginTop: '12px' },
                        children: data.left?.label || 'Left',
                      },
                    },
                  ],
                },
              },
              // VS
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '24px',
                    fontWeight: 'bold',
                    color: getColor('text.muted'),
                  },
                  children: 'vs',
                },
              },
              // Right box
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    backgroundColor: getColor('backgrounds.light_gray'),
                    borderLeft: `6px solid ${rightColor}`,
                    padding: '40px 60px',
                    borderRadius: '8px',
                  },
                  children: [
                    {
                      type: 'div',
                      props: {
                        style: { fontSize: '72px', fontWeight: 'bold', color: rightColor },
                        children: data.right?.value || '—',
                      },
                    },
                    {
                      type: 'div',
                      props: {
                        style: { fontSize: '20px', color: getColor('text.secondary'), marginTop: '12px' },
                        children: data.right?.label || 'Right',
                      },
                    },
                  ],
                },
              },
            ],
          },
        },
        // Metric and source
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              justifyContent: 'space-between',
              marginTop: '30px',
              paddingTop: '20px',
              borderTop: `1px solid ${getColor('backgrounds.medium_gray')}`,
            },
            children: [
              {
                type: 'div',
                props: {
                  style: { fontSize: '16px', color: getColor('text.secondary') },
                  children: data.metric || '',
                },
              },
              {
                type: 'div',
                props: {
                  style: { fontSize: '14px', color: getColor('text.muted') },
                  children: data.source ? `Source: ${data.source}` : '',
                },
              },
            ],
          },
        },
      ],
    },
  };
});

/**
 * Process Flow - Step by step diagram
 *
 * Data: {
 *   title: "Treatment Algorithm",
 *   steps: [
 *     { number: 1, title: "Screen", description: "HFrEF diagnosis" },
 *     { number: 2, title: "Initiate", description: "Start GDMT" },
 *     { number: 3, title: "Optimize", description: "Titrate to target" },
 *   ]
 * }
 */
registerTemplate('process-flow', (data, { getColor }) => {
  const steps = data.steps || [];

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        width: '100%',
        height: '100%',
        backgroundColor: getColor('backgrounds.white'),
        padding: '50px',
        fontFamily: 'Helvetica, Arial, sans-serif',
      },
      children: [
        // Title
        {
          type: 'div',
          props: {
            style: {
              fontSize: '28px',
              fontWeight: 'bold',
              color: getColor('text.primary'),
              marginBottom: '50px',
              textAlign: 'center',
            },
            children: data.title || 'Process Flow',
          },
        },
        // Steps
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flex: 1,
              alignItems: 'center',
              justifyContent: 'center',
              gap: '20px',
            },
            children: steps.flatMap((step, i) => {
              const stepEl = {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    padding: '30px',
                    backgroundColor: getColor('backgrounds.light_gray'),
                    borderRadius: '12px',
                    minWidth: '180px',
                  },
                  children: [
                    {
                      type: 'div',
                      props: {
                        style: {
                          width: '50px',
                          height: '50px',
                          borderRadius: '50%',
                          backgroundColor: getColor('primary.navy'),
                          color: 'white',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          fontSize: '24px',
                          fontWeight: 'bold',
                        },
                        children: String(step.number || i + 1),
                      },
                    },
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '20px',
                          fontWeight: '600',
                          color: getColor('text.primary'),
                          marginTop: '16px',
                        },
                        children: step.title || '',
                      },
                    },
                    step.description ? {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '14px',
                          color: getColor('text.secondary'),
                          marginTop: '8px',
                          textAlign: 'center',
                        },
                        children: step.description,
                      },
                    } : null,
                  ].filter(Boolean),
                },
              };

              // Add arrow between steps
              if (i < steps.length - 1) {
                return [
                  stepEl,
                  {
                    type: 'div',
                    props: {
                      style: {
                        fontSize: '32px',
                        color: getColor('text.muted'),
                      },
                      children: '→',
                    },
                  },
                ];
              }
              return [stepEl];
            }),
          },
        },
      ],
    },
  };
});

/**
 * Trial Summary - Clinical trial results card
 *
 * Data: {
 *   trialName: "DAPA-HF",
 *   population: "HFrEF patients",
 *   intervention: "Dapagliflozin 10mg",
 *   primaryEndpoint: "CV death or HF hospitalization",
 *   result: { hr: 0.74, ci: "0.65-0.85", pValue: "<0.001" },
 *   nnt: 21,
 * }
 */
registerTemplate('trial-summary', (data, { getColor }) => {
  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        width: '100%',
        height: '100%',
        backgroundColor: getColor('backgrounds.white'),
        padding: '50px',
        fontFamily: 'Helvetica, Arial, sans-serif',
      },
      children: [
        // Header
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              marginBottom: '30px',
              paddingBottom: '20px',
              borderBottom: `2px solid ${getColor('primary.navy')}`,
            },
            children: [
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '36px',
                    fontWeight: 'bold',
                    color: getColor('primary.navy'),
                  },
                  children: data.trialName || 'Trial',
                },
              },
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '16px',
                    color: getColor('text.secondary'),
                    backgroundColor: getColor('backgrounds.light_gray'),
                    padding: '8px 16px',
                    borderRadius: '4px',
                  },
                  children: data.population || '',
                },
              },
            ],
          },
        },
        // Main content
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flex: 1,
              gap: '40px',
            },
            children: [
              // Left: Details
              {
                type: 'div',
                props: {
                  style: {
                    flex: 1,
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '20px',
                  },
                  children: [
                    {
                      type: 'div',
                      props: {
                        style: { display: 'flex', flexDirection: 'column' },
                        children: [
                          {
                            type: 'div',
                            props: {
                              style: { fontSize: '14px', color: getColor('text.muted'), marginBottom: '4px' },
                              children: 'INTERVENTION',
                            },
                          },
                          {
                            type: 'div',
                            props: {
                              style: { fontSize: '18px', color: getColor('text.primary') },
                              children: data.intervention || '—',
                            },
                          },
                        ],
                      },
                    },
                    {
                      type: 'div',
                      props: {
                        style: { display: 'flex', flexDirection: 'column' },
                        children: [
                          {
                            type: 'div',
                            props: {
                              style: { fontSize: '14px', color: getColor('text.muted'), marginBottom: '4px' },
                              children: 'PRIMARY ENDPOINT',
                            },
                          },
                          {
                            type: 'div',
                            props: {
                              style: { fontSize: '18px', color: getColor('text.primary') },
                              children: data.primaryEndpoint || '—',
                            },
                          },
                        ],
                      },
                    },
                  ],
                },
              },
              // Right: Results
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    backgroundColor: getColor('backgrounds.light_gray'),
                    padding: '40px',
                    borderRadius: '12px',
                    minWidth: '280px',
                  },
                  children: [
                    {
                      type: 'div',
                      props: {
                        style: { fontSize: '14px', color: getColor('text.muted'), marginBottom: '8px' },
                        children: 'HAZARD RATIO',
                      },
                    },
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '64px',
                          fontWeight: 'bold',
                          color: data.result?.hr < 1 ? getColor('semantic.success') : getColor('semantic.danger'),
                        },
                        children: data.result?.hr?.toString() || '—',
                      },
                    },
                    {
                      type: 'div',
                      props: {
                        style: { fontSize: '18px', color: getColor('text.secondary'), marginTop: '8px' },
                        children: `95% CI: ${data.result?.ci || '—'}`,
                      },
                    },
                    {
                      type: 'div',
                      props: {
                        style: { fontSize: '16px', color: getColor('text.muted'), marginTop: '4px', fontStyle: 'italic' },
                        children: `P ${data.result?.pValue || '—'}`,
                      },
                    },
                    data.nnt ? {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '14px',
                          color: getColor('primary.navy'),
                          marginTop: '20px',
                          padding: '8px 16px',
                          backgroundColor: 'white',
                          borderRadius: '4px',
                        },
                        children: `NNT: ${data.nnt}`,
                      },
                    } : null,
                  ].filter(Boolean),
                },
              },
            ],
          },
        },
      ],
    },
  };
});

/**
 * Key Finding - Highlight a key finding with icon
 *
 * Data: {
 *   icon: "heart" | "arrow-down" | "warning" | "check",
 *   finding: "SGLT2 inhibitors reduce HF hospitalization by 30%",
 *   context: "Meta-analysis of 5 major trials",
 *   evidence: "Class I, Level A"
 * }
 */
registerTemplate('key-finding', (data, { getColor }) => {
  const icons = {
    heart: '❤️',
    'arrow-down': '↓',
    'arrow-up': '↑',
    warning: '⚠️',
    check: '✓',
    star: '★',
  };

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        width: '100%',
        height: '100%',
        backgroundColor: getColor('primary.navy'),
        padding: '60px',
        fontFamily: 'Helvetica, Arial, sans-serif',
      },
      children: [
        // Icon
        {
          type: 'div',
          props: {
            style: {
              fontSize: '72px',
              marginBottom: '30px',
            },
            children: icons[data.icon] || icons.star,
          },
        },
        // Finding
        {
          type: 'div',
          props: {
            style: {
              fontSize: '36px',
              fontWeight: 'bold',
              color: 'white',
              lineHeight: 1.3,
              flex: 1,
            },
            children: data.finding || '',
          },
        },
        // Context and evidence
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              justifyContent: 'space-between',
              marginTop: '40px',
              paddingTop: '20px',
              borderTop: '1px solid rgba(255,255,255,0.3)',
            },
            children: [
              {
                type: 'div',
                props: {
                  style: { fontSize: '16px', color: 'rgba(255,255,255,0.8)' },
                  children: data.context || '',
                },
              },
              data.evidence ? {
                type: 'div',
                props: {
                  style: {
                    fontSize: '14px',
                    color: 'white',
                    backgroundColor: 'rgba(255,255,255,0.2)',
                    padding: '6px 12px',
                    borderRadius: '4px',
                  },
                  children: data.evidence,
                },
              } : null,
            ].filter(Boolean),
          },
        },
      ],
    },
  };
});

// ============================================
// CLI
// ============================================

async function main() {
  const args = process.argv.slice(2);

  // Parse arguments
  let template = 'stat-card';
  let data = {};
  let output = 'output.png';
  let width = 1200;
  let height = 630;
  let stdin = false;

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '--template':
      case '-t':
        template = args[++i];
        break;
      case '--data':
      case '-d':
        data = JSON.parse(args[++i]);
        break;
      case '--output':
      case '-o':
        output = args[++i];
        break;
      case '--width':
        width = parseInt(args[++i]);
        break;
      case '--height':
        height = parseInt(args[++i]);
        break;
      case '--stdin':
        stdin = true;
        break;
      case '--list':
        console.log('Available templates:', Object.keys(templates).join(', '));
        process.exit(0);
      case '--help':
      case '-h':
        console.log(`
Satori Renderer - React to PNG Pipeline

Usage:
  node renderer.js --template <name> --data '<json>' --output <file.png>
  echo '{"template": "...", "data": {...}}' | node renderer.js --stdin

Options:
  --template, -t   Template name (default: stat-card)
  --data, -d       JSON data for template
  --output, -o     Output file (default: output.png)
  --width          Image width (default: 1200)
  --height         Image height (default: 630)
  --stdin          Read JSON input from stdin
  --list           List available templates
  --help, -h       Show this help

Legacy Templates:
  stat-card        Big number with context
  comparison       Side-by-side comparison
  process-flow     Step-by-step diagram
  trial-summary    Clinical trial results
  key-finding      Highlighted finding with icon

World-Class Infographic Templates (1080x1350, carousel visual language):
  infographic-hero       Single key stat with maximum visual impact
  infographic-dense      Multi-section information layout
  infographic-comparison Two-column comparison (drug vs drug, etc.)
  infographic-myth       Myth vs Truth split design
  infographic-process    Workflow/steps with visual flow
  infographic-checklist  Patient guide with styled checklist

Carousel Templates (1080x1350 Instagram format):
  carousel-hook    Scroll-stopping first slide
  carousel-myth    Myth vs Truth split design
  carousel-stat    Big number with visual impact
  carousel-tips    Actionable tips in card layout
  carousel-cta     Call-to-action with personality
        `);
        process.exit(0);
    }
  }

  // Read from stdin if requested
  if (stdin) {
    const chunks = [];
    for await (const chunk of process.stdin) {
      chunks.push(chunk);
    }
    const input = JSON.parse(Buffer.concat(chunks).toString());
    template = input.template || template;
    data = input.data || data;
    output = input.output || output;
    width = input.width || width;
    height = input.height || height;
  }

  try {
    const result = await renderToFile(template, data, output, { width, height, saveSvg: true });
    console.log(JSON.stringify({
      success: true,
      output: result.outputPath,
      size: result.size,
    }));
  } catch (error) {
    console.error(JSON.stringify({
      success: false,
      error: error.message,
    }));
    process.exit(1);
  }
}

// Export for programmatic use
module.exports = {
  render,
  renderToSvg,
  renderToFile,
  registerTemplate,
  templates,
  getColor,
  getFontSize,
  // Carousel-specific exports
  carouselTemplates,
  CAROUSEL_DIMENSIONS: carouselTemplates.DIMENSIONS,
  CAROUSEL_BRAND: carouselTemplates.BRAND,
  // Infographic-specific exports
  infographicTemplates,
  INFOGRAPHIC_DIMENSIONS: infographicTemplates.DIMENSIONS,
  INFOGRAPHIC_BRAND: infographicTemplates.BRAND,
  INFOGRAPHIC_ICONS: infographicTemplates.ICONS,
  INFOGRAPHIC_GRADIENTS: infographicTemplates.GRADIENTS,
};

// Run CLI if executed directly
if (require.main === module) {
  main().catch(console.error);
}
