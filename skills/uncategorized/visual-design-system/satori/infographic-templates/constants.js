/**
 * Infographic Constants
 *
 * Shared constants for all infographic templates.
 * Extracted to avoid circular dependencies.
 */

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

  if (top && !bottom) style.top = top;
  if (right && !left) style.right = right;
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

/**
 * Convert hex color to rgba with opacity
 * Satori doesn't support hex+opacity suffix (e.g., #EF535088)
 * This converts hex to proper rgba() syntax
 */
function hexToRgba(hex, alpha = 1) {
  const cleanHex = hex.replace('#', '');
  const r = parseInt(cleanHex.slice(0, 2), 16);
  const g = parseInt(cleanHex.slice(2, 4), 16);
  const b = parseInt(cleanHex.slice(4, 6), 16);
  const clampedAlpha = Math.max(0, Math.min(1, alpha));
  return `rgba(${r}, ${g}, ${b}, ${clampedAlpha})`;
}

// ============================================
// MEDICAL SVG ICONS
// ============================================

// Lazy-load icon loader to avoid circular deps
let iconLoader = null;
function getIconLoader() {
  if (!iconLoader) {
    try {
      iconLoader = require('../../icons/icon-loader');
    } catch (e) {
      console.warn('Medical icon loader not available:', e.message);
      return null;
    }
  }
  return iconLoader;
}

/**
 * Create a Satori element using a medical SVG icon
 *
 * @param {string} iconName - Name from icon manifest (e.g., 'cardiology', 'diabetes')
 * @param {object} options - Styling options
 * @param {number} options.size - Icon size in pixels (default: 64)
 * @param {string} options.color - SVG fill color (default: null = original colors)
 * @param {string} options.backgroundColor - Background color (default: transparent)
 * @param {number} options.borderRadius - Border radius (default: 0)
 * @param {number} options.padding - Padding inside container (default: 0)
 */
function createMedicalIcon(iconName, options = {}) {
  const loader = getIconLoader();
  if (!loader) {
    // Fallback to emoji if loader not available
    return createIconContainer(iconName, options);
  }

  const {
    size = 64,
    color = null,
    backgroundColor = 'transparent',
    borderRadius = 0,
    padding = 0,
  } = options;

  try {
    const dataUri = loader.loadIconAsDataUri(iconName, { color });

    return {
      type: 'div',
      props: {
        style: {
          width: `${size}px`,
          height: `${size}px`,
          padding: `${padding}px`,
          backgroundColor,
          borderRadius: `${borderRadius}px`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          flexShrink: 0,
        },
        children: {
          type: 'img',
          props: {
            src: dataUri,
            width: size - (padding * 2),
            height: size - (padding * 2),
          },
        },
      },
    };
  } catch (e) {
    // Fallback to emoji icon
    console.warn(`Medical icon '${iconName}' not found, using fallback`);
    return createIconContainer('heart', options);
  }
}

/**
 * List available medical icons
 */
function listMedicalIcons(category = null) {
  const loader = getIconLoader();
  if (!loader) return [];
  return loader.listIcons(category);
}

/**
 * List medical icon categories
 */
function listMedicalIconCategories() {
  const loader = getIconLoader();
  if (!loader) return [];
  return loader.listCategories();
}

module.exports = {
  BRAND,
  DIMENSIONS,
  ICONS,
  GRADIENTS,
  createBlob,
  createIconContainer,
  createStatBadge,
  createFooter,
  createSectionCard,
  createTagBadge,
  hexToRgba,
  // Medical icon support
  createMedicalIcon,
  listMedicalIcons,
  listMedicalIconCategories,
};
