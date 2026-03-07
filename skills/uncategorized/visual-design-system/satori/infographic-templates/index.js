/**
 * Infographic Templates Index
 *
 * World-class infographic templates with carousel-level visual impact.
 * Following the same design principles as carousel templates:
 * - Mesh gradient backgrounds (layered radials, not flat)
 * - Extreme font weight contrasts (900 vs 300)
 * - 3x+ size jumps for visual hierarchy
 * - Icon containers with styled backgrounds
 * - Gradient stat badges with shadows
 * - Large decorative background elements
 *
 * Templates:
 * - infographic-hero: Single key stat with visual impact
 * - infographic-dense: Multi-section information layout
 * - infographic-comparison: Two-column comparison
 * - infographic-myth: Myth vs Truth split design
 * - infographic-process: Workflow/steps with visual flow
 * - infographic-checklist: Patient guide with styled checklist
 */

// Import individual templates
const infographicHero = require('./infographic-hero');
const infographicDense = require('./infographic-dense');
const infographicComparison = require('./infographic-comparison');
const infographicMyth = require('./infographic-myth');
const infographicProcess = require('./infographic-process');
const infographicChecklist = require('./infographic-checklist');
const infographicTimeline = require('./infographic-timeline');
const infographicQuote = require('./infographic-quote');
const infographicRiskFactors = require('./infographic-risk-factors');
const infographicMedicalStat = require('./infographic-medical-stat');

// ============================================
// BRAND CONSTANTS (from carousel tokens)
// ============================================

const BRAND = {
  // Primary palette
  primary: '#16697A',        // Deep Teal - titles, CTAs
  primaryLight: '#1E8A9F',   // Light Teal - gradients
  secondary: '#218380',      // Secondary Teal - panels
  accent: '#EF5350',         // Coral - callouts, energy
  accentDark: '#D32F2F',     // Dark Coral - gradients

  // Semantic colors
  success: '#27AE60',        // Green - positive, truth
  successLight: '#2ECC71',   // Light Green - gradients
  alert: '#E74C3C',          // Red - danger, alerts
  mythRed: '#FF6B6B',        // Soft Red - myths
  mythRedDark: '#E53E3E',    // Dark Red - myth gradients

  // Neutrals
  backgroundWash: '#E8F5F4', // Soft Aqua - backgrounds
  neutralLight: '#F9FAFB',   // Near White - cards
  neutralDark: '#2F3E46',    // Warm Dark - text
  white: '#FFFFFF',
  black: '#000000',

  // Text shades
  textPrimary: '#2F3E46',
  textSecondary: '#5A6B73',
  textMuted: '#6B7C85',
};

// ============================================
// DIMENSIONS (Instagram portrait optimized)
// ============================================

const DIMENSIONS = {
  portrait: { width: 1080, height: 1350 },  // 4:5 (10% higher engagement)
  square: { width: 1080, height: 1080 },    // 1:1 multi-platform
  story: { width: 1080, height: 1920 },     // 9:16 stories
  default: { width: 1080, height: 1350 },
};

// ============================================
// ICONS (Medical + General)
// ============================================

const ICONS = {
  // Medical
  pill: '\u{1F48A}',           // 💊
  heart: '\u{2764}\u{FE0F}',   // ❤️
  'heart-pulse': '\u{1F493}',  // 💓
  stethoscope: '\u{1FA7A}',    // 🩺
  syringe: '\u{1F489}',        // 💉
  'blood-drop': '\u{1FA78}',   // 🩸
  dna: '\u{1F9EC}',            // 🧬
  microscope: '\u{1F52C}',     // 🔬
  brain: '\u{1F9E0}',          // 🧠
  lungs: '\u{1FAC1}',          // 🫁
  bone: '\u{1F9B4}',           // 🦴
  hospital: '\u{1F3E5}',       // 🏥
  ambulance: '\u{1F691}',      // 🚑
  doctor: '\u{1F468}\u{200D}\u{2695}\u{FE0F}', // 👨‍⚕️

  // Charts & Data
  'chart-up': '\u{1F4C8}',     // 📈
  'chart-down': '\u{1F4C9}',   // 📉
  graph: '\u{1F4CA}',          // 📊

  // Status & Action
  check: '\u{2705}',           // ✅
  cross: '\u{274C}',           // ❌
  warning: '\u{26A0}\u{FE0F}', // ⚠️
  stop: '\u{1F6D1}',           // 🛑
  star: '\u{2B50}',            // ⭐
  fire: '\u{1F525}',           // 🔥
  lightning: '\u{26A1}',       // ⚡
  target: '\u{1F3AF}',         // 🎯
  bulb: '\u{1F4A1}',           // 💡
  trophy: '\u{1F3C6}',         // 🏆
  shield: '\u{1F6E1}\u{FE0F}', // 🛡️
  clock: '\u{23F0}',           // ⏰
  magnify: '\u{1F50D}',        // 🔍
  books: '\u{1F4DA}',          // 📚
  people: '\u{1F465}',         // 👥

  // Arrows
  'arrow-up': '\u{2B06}\u{FE0F}',   // ⬆️
  'arrow-down': '\u{2B07}\u{FE0F}', // ⬇️
  'arrow-right': '\u{27A1}\u{FE0F}', // ➡️
};

// ============================================
// MESH GRADIENT PRESETS
// ============================================

const GRADIENTS = {
  // Primary theme - teal mesh
  primaryMesh: `
    radial-gradient(ellipse at 27% 37%, rgba(33, 131, 128, 0.4) 0%, transparent 50%),
    radial-gradient(ellipse at 97% 21%, rgba(22, 105, 122, 0.3) 0%, transparent 50%),
    radial-gradient(ellipse at 52% 99%, rgba(39, 174, 96, 0.2) 0%, transparent 50%),
    linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.secondary} 100%)
  `,

  // Light theme - soft aqua mesh
  lightMesh: `
    radial-gradient(ellipse at 27% 37%, rgba(22, 105, 122, 0.08) 0%, transparent 50%),
    radial-gradient(ellipse at 97% 21%, rgba(33, 131, 128, 0.06) 0%, transparent 50%),
    radial-gradient(ellipse at 10% 90%, rgba(39, 174, 96, 0.05) 0%, transparent 50%),
    linear-gradient(180deg, ${BRAND.backgroundWash} 0%, ${BRAND.white} 60%, ${BRAND.backgroundWash} 100%)
  `,

  // Accent theme - coral mesh
  accentMesh: `
    radial-gradient(ellipse at 27% 37%, rgba(239, 83, 80, 0.3) 0%, transparent 50%),
    radial-gradient(ellipse at 97% 21%, rgba(255, 107, 107, 0.25) 0%, transparent 50%),
    linear-gradient(135deg, ${BRAND.accent} 0%, ${BRAND.accentDark} 100%)
  `,

  // Success theme - green mesh
  successMesh: `
    radial-gradient(ellipse at 27% 37%, rgba(39, 174, 96, 0.3) 0%, transparent 50%),
    radial-gradient(ellipse at 97% 21%, rgba(46, 204, 113, 0.25) 0%, transparent 50%),
    linear-gradient(135deg, ${BRAND.success} 0%, ${BRAND.successLight} 100%)
  `,

  // Danger/Myth theme - red mesh
  dangerMesh: `
    radial-gradient(ellipse at 27% 37%, rgba(231, 76, 60, 0.3) 0%, transparent 50%),
    radial-gradient(ellipse at 97% 21%, rgba(255, 107, 107, 0.25) 0%, transparent 50%),
    linear-gradient(135deg, ${BRAND.mythRed} 0%, ${BRAND.alert} 100%)
  `,

  // Stat badge gradients
  statPrimary: `linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.primaryLight} 100%)`,
  statSuccess: `linear-gradient(135deg, ${BRAND.success} 0%, ${BRAND.successLight} 100%)`,
  statAccent: `linear-gradient(135deg, ${BRAND.accent} 0%, ${BRAND.accentDark} 100%)`,
  statDanger: `linear-gradient(135deg, ${BRAND.alert} 0%, ${BRAND.mythRedDark} 100%)`,
};

// ============================================
// UTILITY FUNCTIONS
// ============================================

/**
 * Convert hex color to rgba with opacity
 * Satori doesn't support hex+opacity suffix (e.g., #EF535088)
 * This converts hex to proper rgba() syntax
 *
 * @param {string} hex - Hex color (e.g., "#EF5350" or "EF5350")
 * @param {number} alpha - Opacity from 0 to 1 (default: 1)
 * @returns {string} rgba() color string
 */
function hexToRgba(hex, alpha = 1) {
  // Remove # if present
  const cleanHex = hex.replace('#', '');

  // Parse hex values
  const r = parseInt(cleanHex.slice(0, 2), 16);
  const g = parseInt(cleanHex.slice(2, 4), 16);
  const b = parseInt(cleanHex.slice(4, 6), 16);

  // Clamp alpha to valid range
  const clampedAlpha = Math.max(0, Math.min(1, alpha));

  return `rgba(${r}, ${g}, ${b}, ${clampedAlpha})`;
}

// ============================================
// COMPONENT BUILDERS
// ============================================

/**
 * Create decorative background blob
 */
function createBlob(options = {}) {
  const {
    top = '-100px',
    right = '-100px',
    left,
    bottom,
    size = '400px',
    color = 'rgba(255, 255, 255, 0.03)',
  } = options;

  const style = {
    position: 'absolute',
    width: size,
    height: size,
    borderRadius: '50%',
    background: color,
  };

  if (top) style.top = top;
  if (right) style.right = right;
  if (left) style.left = left;
  if (bottom) style.bottom = bottom;

  return {
    type: 'div',
    props: { style },
  };
}

/**
 * Create icon container with styled background
 */
function createIconContainer(icon, options = {}) {
  const {
    size = 120,
    bgColor = 'rgba(255, 255, 255, 0.15)',
    borderRadius = 30,
    fontSize = 64,
  } = options;

  const resolvedIcon = ICONS[icon] || icon || ICONS.heart;

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: `${size}px`,
        height: `${size}px`,
        borderRadius: `${borderRadius}px`,
        backgroundColor: bgColor,
      },
      children: {
        type: 'div',
        props: {
          style: {
            fontSize: `${fontSize}px`,
            lineHeight: 1,
          },
          children: resolvedIcon,
        },
      },
    },
  };
}

/**
 * Create gradient stat badge
 */
function createStatBadge(stat, options = {}) {
  const {
    gradient = GRADIENTS.statPrimary,
    fontSize = 96,
    padding = '40px 72px',
    shadow = true,
  } = options;

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        background: gradient,
        padding,
        borderRadius: '32px',
        boxShadow: shadow ? '0 20px 60px rgba(22, 105, 122, 0.2)' : 'none',
      },
      children: {
        type: 'div',
        props: {
          style: {
            fontSize: `${fontSize}px`,
            fontWeight: 900,
            color: BRAND.white,
            lineHeight: 1,
            letterSpacing: '-3px',
          },
          children: stat,
        },
      },
    },
  };
}

/**
 * Create branded footer
 */
function createFooter(options = {}) {
  const {
    name = 'Dr. Shailesh Singh',
    handle = '@heartdocshailesh',
    dark = false,
    height = 140,
  } = options;

  const bgColor = dark ? 'rgba(0, 0, 0, 0.2)' : BRAND.white;
  const textColor = dark ? BRAND.white : BRAND.neutralDark;
  const handleColor = dark ? BRAND.backgroundWash : BRAND.primary;
  const initialBg = dark ? BRAND.white : BRAND.primary;
  const initialColor = dark ? BRAND.primary : BRAND.white;

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '24px',
        height: `${height}px`,
        backgroundColor: bgColor,
        borderTop: dark ? 'none' : `3px solid ${BRAND.primary}`,
        padding: '0 60px',
      },
      children: [
        // Profile initial
        {
          type: 'div',
          props: {
            style: {
              width: '80px',
              height: '80px',
              borderRadius: '50%',
              backgroundColor: initialBg,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            },
            children: {
              type: 'div',
              props: {
                style: {
                  fontSize: '36px',
                  color: initialColor,
                  fontWeight: 700,
                },
                children: name.charAt(0).toUpperCase(),
              },
            },
          },
        },
        // Name and handle
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flexDirection: 'column',
              gap: '4px',
            },
            children: [
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '24px',
                    fontWeight: 600,
                    color: textColor,
                  },
                  children: name,
                },
              },
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '20px',
                    fontWeight: 500,
                    color: handleColor,
                  },
                  children: handle,
                },
              },
            ],
          },
        },
      ],
    },
  };
}

/**
 * Create section card with accent border
 */
function createSectionCard(options = {}) {
  const {
    title,
    bullets = [],
    accentColor = BRAND.secondary,
    width = '470px',
  } = options;

  return {
    type: 'div',
    props: {
      style: {
        width,
        backgroundColor: 'rgba(255, 255, 255, 0.96)',
        border: `1px solid ${BRAND.backgroundWash}`,
        borderRadius: '24px',
        padding: '24px 28px',
        display: 'flex',
        flexDirection: 'column',
        boxShadow: '0 8px 32px rgba(22, 105, 122, 0.08)',
      },
      children: [
        // Title
        {
          type: 'div',
          props: {
            style: {
              fontSize: '22px',
              fontWeight: 700,
              color: BRAND.primary,
              marginBottom: '12px',
              display: 'flex',
              alignItems: 'center',
              gap: '10px',
            },
            children: [
              // Accent bar
              {
                type: 'div',
                props: {
                  style: {
                    width: '4px',
                    height: '24px',
                    backgroundColor: accentColor,
                    borderRadius: '2px',
                  },
                },
              },
              title,
            ],
          },
        },
        // Bullets
        ...bullets.map(text => ({
          type: 'div',
          props: {
            style: {
              display: 'flex',
              gap: '12px',
              alignItems: 'flex-start',
              marginTop: '10px',
            },
            children: [
              {
                type: 'div',
                props: {
                  style: {
                    width: '8px',
                    height: '8px',
                    borderRadius: '50%',
                    backgroundColor: accentColor,
                    marginTop: '8px',
                    flexShrink: 0,
                  },
                },
              },
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '18px',
                    lineHeight: 1.4,
                    color: BRAND.textPrimary,
                  },
                  children: text,
                },
              },
            ],
          },
        })),
      ],
    },
  };
}

/**
 * Create tag/label badge
 */
function createTagBadge(text, options = {}) {
  const {
    color = BRAND.secondary,
    bgOpacity = 0.1,
  } = options;

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        alignItems: 'center',
        gap: '12px',
      },
      children: [
        {
          type: 'div',
          props: {
            style: {
              width: '64px',
              height: '6px',
              backgroundColor: BRAND.primary,
              borderRadius: '999px',
            },
          },
        },
        {
          type: 'div',
          props: {
            style: {
              fontSize: '14px',
              letterSpacing: '2px',
              fontWeight: 700,
              color,
              textTransform: 'uppercase',
            },
            children: text,
          },
        },
      ],
    },
  };
}

// ============================================
// TEMPLATE REGISTRY
// ============================================

const INFOGRAPHIC_TEMPLATES = {
  'infographic-hero': infographicHero,
  'infographic-dense': infographicDense,
  'infographic-comparison': infographicComparison,
  'infographic-myth': infographicMyth,
  'infographic-process': infographicProcess,
  'infographic-checklist': infographicChecklist,
  'infographic-timeline': infographicTimeline,
  'infographic-quote': infographicQuote,
  'infographic-risk-factors': infographicRiskFactors,
  'infographic-medical-stat': infographicMedicalStat,
};

/**
 * Get a template by name
 */
function getTemplate(name) {
  return INFOGRAPHIC_TEMPLATES[name] || null;
}

/**
 * List all available template names
 */
function listTemplates() {
  return Object.keys(INFOGRAPHIC_TEMPLATES);
}

/**
 * Register all infographic templates with a renderer
 */
function registerAll(registerFn) {
  Object.entries(INFOGRAPHIC_TEMPLATES).forEach(([name, template]) => {
    registerFn(name, template);
  });
}

// ============================================
// EXPORTS
// ============================================

module.exports = {
  // Individual templates
  infographicHero,
  infographicDense,
  infographicComparison,
  infographicMyth,
  infographicProcess,
  infographicChecklist,
  infographicTimeline,
  infographicQuote,
  infographicRiskFactors,
  infographicMedicalStat,

  // Template registry
  INFOGRAPHIC_TEMPLATES,

  // Utilities
  getTemplate,
  listTemplates,
  registerAll,

  // Shared constants
  BRAND,
  DIMENSIONS,
  ICONS,
  GRADIENTS,

  // Component builders
  createBlob,
  createIconContainer,
  createStatBadge,
  createFooter,
  createSectionCard,
  createTagBadge,

  // Utility functions
  hexToRgba,
};
