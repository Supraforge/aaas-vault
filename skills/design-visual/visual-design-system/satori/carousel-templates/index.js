/**
 * Carousel Templates Index
 *
 * Exports all carousel-specific Satori templates for Instagram carousels.
 * These templates are designed following Anthropic aesthetic principles:
 * - Mesh gradient backgrounds (not flat colors)
 * - Extreme font weight contrasts (900 vs 300)
 * - 3x+ size jumps for visual hierarchy
 * - Distinctive, non-generic styling
 *
 * Templates:
 * - carousel-hook: Scroll-stopping first slide
 * - carousel-myth: Myth vs Truth split design
 * - carousel-stat: Big number with visual impact
 * - carousel-tips: Actionable tips in card layout
 * - carousel-cta: Call-to-action with personality
 */

const carouselHook = require('./carousel-hook');
const carouselMyth = require('./carousel-myth');
const carouselStat = require('./carousel-stat');
const carouselTips = require('./carousel-tips');
const carouselCta = require('./carousel-cta');

// Template registry for carousel slides
const CAROUSEL_TEMPLATES = {
  'carousel-hook': carouselHook,
  'carousel-myth': carouselMyth,
  'carousel-stat': carouselStat,
  'carousel-tips': carouselTips,
  'carousel-cta': carouselCta,
  // Aliases for convenience
  'hook': carouselHook,
  'myth': carouselMyth,
  'stat': carouselStat,
  'tips': carouselTips,
  'cta': carouselCta,
};

// Shared brand colors across all templates
const BRAND = {
  primary: '#16697A',
  primaryLight: '#1E8A9F',
  secondary: '#218380',
  accent: '#EF5350',
  accentDark: '#D32F2F',
  success: '#27AE60',
  successDark: '#1E8449',
  mythRed: '#FF6B6B',
  mythRedDark: '#E74C3C',
  backgroundWash: '#E8F5F4',
  neutralLight: '#F9FAFB',
  neutralDark: '#2F3E46',
  white: '#FFFFFF',
  black: '#000000',
};

// Instagram carousel dimensions
const DIMENSIONS = {
  instagram4x5: { width: 1080, height: 1350 },
  instagram1x1: { width: 1080, height: 1080 },
  // Default for carousels
  default: { width: 1080, height: 1350 },
};

/**
 * Get a template by name
 * @param {string} name - Template name
 * @returns {Function|null} - Template function or null if not found
 */
function getTemplate(name) {
  return CAROUSEL_TEMPLATES[name] || null;
}

/**
 * List all available template names
 * @returns {string[]} - Array of template names
 */
function listTemplates() {
  return Object.keys(CAROUSEL_TEMPLATES).filter(key => key.startsWith('carousel-'));
}

/**
 * Register all carousel templates with a renderer
 * @param {Function} registerFn - Function to call for each template (name, fn)
 */
function registerAll(registerFn) {
  // Only register the full names (not aliases)
  registerFn('carousel-hook', carouselHook);
  registerFn('carousel-myth', carouselMyth);
  registerFn('carousel-stat', carouselStat);
  registerFn('carousel-tips', carouselTips);
  registerFn('carousel-cta', carouselCta);
}

module.exports = {
  // Individual templates
  carouselHook,
  carouselMyth,
  carouselStat,
  carouselTips,
  carouselCta,

  // Template registry
  CAROUSEL_TEMPLATES,

  // Utilities
  getTemplate,
  listTemplates,
  registerAll,

  // Shared constants
  BRAND,
  DIMENSIONS,
};
