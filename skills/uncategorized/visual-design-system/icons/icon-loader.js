/**
 * Medical Icon Loader
 *
 * Loads SVG icons from the icon library for use in visual content.
 * Supports loading as:
 * - Raw SVG string
 * - Data URI (for img src)
 * - Satori-compatible object (for direct rendering)
 *
 * Usage:
 *   const { loadIcon, loadIconAsDataUri, getIconPath, listIcons } = require('./icon-loader');
 *
 *   // Load icon by name
 *   const svg = loadIcon('cardiology');
 *   const dataUri = loadIconAsDataUri('cardiology');
 *
 *   // List available icons
 *   const allIcons = listIcons();
 *   const cardiologyIcons = listIcons('cardiology');
 */

const fs = require('fs');
const path = require('path');

// Load manifest
const MANIFEST_PATH = path.join(__dirname, 'icon-manifest.json');
let manifest = null;

function getManifest() {
  if (!manifest) {
    manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
  }
  return manifest;
}

/**
 * Find icon info by name across all categories
 */
function findIcon(name) {
  const m = getManifest();
  for (const [category, data] of Object.entries(m.categories)) {
    const icon = data.icons.find(i => i.name === name);
    if (icon) {
      return { ...icon, category };
    }
  }
  return null;
}

/**
 * Get the file path for an icon
 */
function getIconPath(name) {
  const icon = findIcon(name);
  if (!icon) {
    throw new Error(`Icon '${name}' not found. Use listIcons() to see available icons.`);
  }
  return path.join(__dirname, icon.file);
}

/**
 * Load icon as raw SVG string
 */
function loadIcon(name) {
  const iconPath = getIconPath(name);
  if (!fs.existsSync(iconPath)) {
    throw new Error(`Icon file not found: ${iconPath}`);
  }
  return fs.readFileSync(iconPath, 'utf8');
}

/**
 * Load icon as base64 data URI
 */
function loadIconAsDataUri(name, options = {}) {
  const svg = loadIcon(name);
  const { color } = options;

  let processedSvg = svg;

  // Optionally recolor the SVG
  if (color) {
    // Replace fill colors (but not fill="none")
    processedSvg = processedSvg.replace(/fill="(?!none)[^"]*"/g, `fill="${color}"`);
    // Add fill to paths without fill attribute
    processedSvg = processedSvg.replace(/<path(?![^>]*fill=)/g, `<path fill="${color}"`);
  }

  const base64 = Buffer.from(processedSvg).toString('base64');
  return `data:image/svg+xml;base64,${base64}`;
}

/**
 * Load icon and return SVG dimensions
 */
function loadIconWithDimensions(name) {
  const svg = loadIcon(name);

  // Extract viewBox or width/height
  const viewBoxMatch = svg.match(/viewBox="([^"]+)"/);
  const widthMatch = svg.match(/width="(\d+)"/);
  const heightMatch = svg.match(/height="(\d+)"/);

  let width = 64, height = 64;

  if (viewBoxMatch) {
    const [, , , w, h] = viewBoxMatch[1].split(/\s+/);
    width = parseFloat(w) || 64;
    height = parseFloat(h) || 64;
  } else if (widthMatch && heightMatch) {
    width = parseInt(widthMatch[1]);
    height = parseInt(heightMatch[1]);
  }

  return { svg, width, height };
}

/**
 * List available icons, optionally filtered by category
 */
function listIcons(category = null) {
  const m = getManifest();
  const result = [];

  for (const [cat, data] of Object.entries(m.categories)) {
    if (category && cat !== category) continue;

    for (const icon of data.icons) {
      result.push({
        name: icon.name,
        category: cat,
        file: icon.file,
      });
    }
  }

  return result;
}

/**
 * List available categories
 */
function listCategories() {
  const m = getManifest();
  return Object.entries(m.categories).map(([name, data]) => ({
    name,
    description: data.description,
    count: data.icons.length,
  }));
}

/**
 * Get icons by category
 */
function getIconsByCategory(category) {
  const m = getManifest();
  const cat = m.categories[category];
  if (!cat) {
    throw new Error(`Category '${category}' not found. Use listCategories() to see available.`);
  }
  return cat.icons.map(i => i.name);
}

/**
 * Create Satori-compatible image element for an icon
 * Returns a div with the icon as background image
 */
function createIconElement(name, options = {}) {
  const {
    size = 64,
    color = null,
    backgroundColor = 'transparent',
    borderRadius = 0,
  } = options;

  const dataUri = loadIconAsDataUri(name, { color });

  return {
    type: 'div',
    props: {
      style: {
        width: `${size}px`,
        height: `${size}px`,
        backgroundImage: `url("${dataUri}")`,
        backgroundSize: 'contain',
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        backgroundColor,
        borderRadius: `${borderRadius}px`,
        flexShrink: 0,
      },
    },
  };
}

/**
 * Batch load multiple icons
 */
function loadIcons(names) {
  return names.reduce((acc, name) => {
    try {
      acc[name] = loadIconAsDataUri(name);
    } catch (e) {
      console.warn(`Warning: Could not load icon '${name}': ${e.message}`);
    }
    return acc;
  }, {});
}

// Export all functions
module.exports = {
  loadIcon,
  loadIconAsDataUri,
  loadIconWithDimensions,
  getIconPath,
  findIcon,
  listIcons,
  listCategories,
  getIconsByCategory,
  createIconElement,
  loadIcons,
  getManifest,
};

// CLI support
if (require.main === module) {
  const args = process.argv.slice(2);
  const command = args[0];

  switch (command) {
    case 'list':
      const category = args[1];
      const icons = listIcons(category);
      console.log(JSON.stringify(icons, null, 2));
      break;

    case 'categories':
      const cats = listCategories();
      console.log(JSON.stringify(cats, null, 2));
      break;

    case 'path':
      const name = args[1];
      if (!name) {
        console.error('Usage: node icon-loader.js path <icon-name>');
        process.exit(1);
      }
      console.log(getIconPath(name));
      break;

    case 'datauri':
      const iconName = args[1];
      const color = args[2];
      if (!iconName) {
        console.error('Usage: node icon-loader.js datauri <icon-name> [color]');
        process.exit(1);
      }
      console.log(loadIconAsDataUri(iconName, { color }));
      break;

    default:
      console.log(`
Medical Icon Loader CLI

Commands:
  list [category]        List all icons or icons in a category
  categories             List all categories
  path <name>            Get file path for an icon
  datauri <name> [color] Get data URI for an icon (optionally recolored)

Examples:
  node icon-loader.js list
  node icon-loader.js list cardiology
  node icon-loader.js categories
  node icon-loader.js path cardiology
  node icon-loader.js datauri cardiology "#16697A"
      `);
  }
}
