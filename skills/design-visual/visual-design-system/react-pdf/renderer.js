#!/usr/bin/env node
/**
 * React-PDF Renderer - Publication-Grade Article PDFs
 *
 * Generates Nature/JACC/NEJM-quality PDFs for medical content.
 * Supports newsletters, editorials, reports, and clinical summaries.
 *
 * Usage:
 *   node -r @babel/register renderer.js --template newsletter --data '{"title": "..."}' --output article.pdf
 *   node -r @babel/register renderer.js --list
 *   echo '{"template": "newsletter", "data": {...}}' | node -r @babel/register renderer.js --stdin
 */

const React = require('react');
const { renderToBuffer } = require('@react-pdf/renderer');
const fs = require('fs');
const path = require('path');

// Resolve paths relative to visual-design-system (handles running from dist/)
// __dirname is react-pdf/dist when running built code
const visualSystemRoot = path.resolve(__dirname, '..', '..');
const tokensPath = path.join(visualSystemRoot, 'tokens');

// Load design tokens
const colors = JSON.parse(fs.readFileSync(path.join(tokensPath, 'colors.json'), 'utf8'));
const typography = JSON.parse(fs.readFileSync(path.join(tokensPath, 'typography.json'), 'utf8'));
const spacing = JSON.parse(fs.readFileSync(path.join(tokensPath, 'spacing.json'), 'utf8'));

// Load templates
const templates = require('./templates/index.js');

/**
 * Get color from tokens
 */
function getColor(colorPath) {
  const parts = colorPath.split('.');
  let current = colors;
  for (const part of parts) {
    current = current[part];
  }
  return current?.value || current || colorPath;
}

/**
 * Publication-grade PDF styles matching Nature/JACC standards
 */
const styles = {
  // Page settings
  page: {
    paddingTop: 72,      // 1 inch
    paddingBottom: 72,
    paddingLeft: 72,
    paddingRight: 72,
    fontSize: 10,
    fontFamily: 'Helvetica',
    lineHeight: 1.4,
    color: '#1a1a2e',
  },

  // Typography
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 12,
    color: getColor('primary.navy'),
    fontFamily: 'Helvetica-Bold',
  },
  subtitle: {
    fontSize: 14,
    marginBottom: 24,
    color: getColor('semantic.neutral'),
    fontFamily: 'Helvetica',
  },
  sectionHeader: {
    fontSize: 14,
    fontWeight: 'bold',
    marginTop: 24,
    marginBottom: 12,
    color: getColor('primary.navy'),
    fontFamily: 'Helvetica-Bold',
    borderBottomWidth: 1,
    borderBottomColor: getColor('primary.teal'),
    paddingBottom: 4,
  },
  subsectionHeader: {
    fontSize: 12,
    fontWeight: 'bold',
    marginTop: 16,
    marginBottom: 8,
    color: getColor('primary.blue'),
    fontFamily: 'Helvetica-Bold',
  },
  bodyText: {
    fontSize: 10,
    marginBottom: 8,
    textAlign: 'justify',
    lineHeight: 1.5,
  },
  caption: {
    fontSize: 8,
    fontStyle: 'italic',
    color: getColor('semantic.neutral'),
    marginTop: 4,
  },

  // Layout
  row: {
    flexDirection: 'row',
    marginBottom: 12,
  },
  column: {
    flexDirection: 'column',
  },
  twoColumn: {
    flexDirection: 'row',
    gap: 24,
  },

  // Components
  statBox: {
    backgroundColor: getColor('backgrounds.light'),
    padding: 16,
    borderRadius: 4,
    marginBottom: 12,
    borderLeftWidth: 4,
    borderLeftColor: getColor('primary.teal'),
  },
  statValue: {
    fontSize: 28,
    fontWeight: 'bold',
    color: getColor('primary.navy'),
    fontFamily: 'Helvetica-Bold',
  },
  statLabel: {
    fontSize: 10,
    color: getColor('semantic.neutral'),
    marginTop: 4,
  },
  keyFinding: {
    backgroundColor: '#f0f9ff',
    padding: 12,
    borderRadius: 4,
    marginBottom: 12,
    borderLeftWidth: 3,
    borderLeftColor: getColor('primary.blue'),
  },
  citation: {
    fontSize: 8,
    color: getColor('semantic.neutral'),
    marginTop: 2,
  },

  // Tables
  table: {
    display: 'table',
    width: '100%',
    marginBottom: 16,
  },
  tableRow: {
    flexDirection: 'row',
    borderBottomWidth: 1,
    borderBottomColor: '#e5e7eb',
  },
  tableHeader: {
    backgroundColor: getColor('primary.navy'),
    color: 'white',
    fontWeight: 'bold',
    padding: 8,
    fontSize: 9,
  },
  tableCell: {
    padding: 8,
    fontSize: 9,
    flex: 1,
  },

  // Footer
  footer: {
    position: 'absolute',
    bottom: 36,
    left: 72,
    right: 72,
    fontSize: 8,
    color: getColor('semantic.neutral'),
    borderTopWidth: 1,
    borderTopColor: '#e5e7eb',
    paddingTop: 8,
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  pageNumber: {
    fontSize: 8,
    color: getColor('semantic.neutral'),
  },
};

/**
 * Render a PDF document
 */
async function renderPDF(templateName, data, outputPath) {
  const TemplateComponent = templates[templateName];

  if (!TemplateComponent) {
    throw new Error(`Unknown template: ${templateName}. Available: ${Object.keys(templates).join(', ')}`);
  }

  const document = React.createElement(TemplateComponent, {
    data,
    styles,
    getColor,
  });

  const buffer = await renderToBuffer(document);

  // Ensure output directory exists
  const outputDir = path.dirname(outputPath);
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  fs.writeFileSync(outputPath, buffer);

  return {
    success: true,
    output: outputPath,
    size: buffer.length,
    template: templateName,
  };
}

/**
 * CLI interface
 */
async function main() {
  const args = process.argv.slice(2);

  // List templates
  if (args.includes('--list')) {
    console.log('Available templates:', Object.keys(templates).join(', '));
    return;
  }

  // Parse arguments
  let templateName = 'newsletter';
  let data = {};
  let outputPath = 'output.pdf';
  let useStdin = false;

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '--template':
      case '-t':
        templateName = args[++i];
        break;
      case '--data':
      case '-d':
        data = JSON.parse(args[++i]);
        break;
      case '--output':
      case '-o':
        outputPath = args[++i];
        break;
      case '--stdin':
        useStdin = true;
        break;
    }
  }

  // Read from stdin if requested
  if (useStdin) {
    const chunks = [];
    for await (const chunk of process.stdin) {
      chunks.push(chunk);
    }
    const input = JSON.parse(Buffer.concat(chunks).toString());
    templateName = input.template || templateName;
    data = input.data || data;
    outputPath = input.output || outputPath;
  }

  try {
    const result = await renderPDF(templateName, data, outputPath);
    console.log(JSON.stringify(result));
  } catch (error) {
    console.error(JSON.stringify({ success: false, error: error.message }));
    process.exit(1);
  }
}

main();
