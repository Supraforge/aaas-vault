/**
 * Carousel Hook Template - Scroll-stopping first slide
 *
 * Design Principles:
 * - Mesh gradient background (not flat color)
 * - Bold headline with extreme font weight contrast (900 vs 300)
 * - Topic icon or emoji for visual interest
 * - Clean, no footer (hooks are clean)
 *
 * Data Structure:
 * {
 *   headline: "5 Statin Myths Exposed",
 *   subtitle: "What every patient needs to know",
 *   icon: "pill" | "heart" | "chart" | "warning" | emoji,
 *   theme: "dark" | "light" | "accent"
 * }
 */

// Brand colors from tokens
const BRAND = {
  primary: '#16697A',
  secondary: '#218380',
  accent: '#EF5350',
  success: '#27AE60',
  mythRed: '#FF6B6B',
  backgroundWash: '#E8F5F4',
  neutralDark: '#2F3E46',
  white: '#FFFFFF',
};

// Icon map (emojis and unicode symbols)
const ICONS = {
  pill: '\u{1F48A}',           // 💊
  heart: '\u{2764}\u{FE0F}',   // ❤️
  'heart-pulse': '\u{1F493}',  // 💓
  chart: '\u{1F4C8}',          // 📈
  'chart-down': '\u{1F4C9}',   // 📉
  warning: '\u{26A0}\u{FE0F}', // ⚠️
  check: '\u{2705}',           // ✅
  cross: '\u{274C}',           // ❌
  star: '\u{2B50}',            // ⭐
  fire: '\u{1F525}',           // 🔥
  brain: '\u{1F9E0}',          // 🧠
  dna: '\u{1F9EC}',            // 🧬
  microscope: '\u{1F52C}',     // 🔬
  syringe: '\u{1F489}',        // 💉
  stethoscope: '\u{1FA7A}',    // 🩺
  'blood-drop': '\u{1FA78}',   // 🩸
  lungs: '\u{1FAC1}',          // 🫁
  bone: '\u{1F9B4}',           // 🦴
  doctor: '\u{1F468}\u{200D}\u{2695}\u{FE0F}', // 👨‍⚕️
  hospital: '\u{1F3E5}',       // 🏥
  ambulance: '\u{1F691}',      // 🚑
  shield: '\u{1F6E1}\u{FE0F}', // 🛡️
  lightning: '\u{26A1}',       // ⚡
  target: '\u{1F3AF}',         // 🎯
  bulb: '\u{1F4A1}',           // 💡
  stop: '\u{1F6D1}',           // 🛑
  clock: '\u{23F0}',           // ⏰
  trophy: '\u{1F3C6}',         // 🏆
  books: '\u{1F4DA}',          // 📚
  magnify: '\u{1F50D}',        // 🔍
};

// Theme configurations with mesh gradients
const THEMES = {
  dark: {
    // Mesh gradient: radial gradients layered for depth
    background: `radial-gradient(ellipse at 27% 37%, rgba(33, 131, 128, 0.4) 0%, transparent 50%),
                 radial-gradient(ellipse at 97% 21%, rgba(22, 105, 122, 0.3) 0%, transparent 50%),
                 radial-gradient(ellipse at 52% 99%, rgba(39, 174, 96, 0.2) 0%, transparent 50%),
                 linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.secondary} 100%)`,
    headlineColor: BRAND.white,
    subtitleColor: 'rgba(255, 255, 255, 0.85)',
    iconBgColor: 'rgba(255, 255, 255, 0.15)',
  },
  light: {
    background: `radial-gradient(ellipse at 27% 37%, rgba(22, 105, 122, 0.1) 0%, transparent 50%),
                 radial-gradient(ellipse at 97% 21%, rgba(33, 131, 128, 0.08) 0%, transparent 50%),
                 linear-gradient(180deg, ${BRAND.backgroundWash} 0%, ${BRAND.white} 100%)`,
    headlineColor: BRAND.primary,
    subtitleColor: BRAND.neutralDark,
    iconBgColor: 'rgba(22, 105, 122, 0.1)',
  },
  accent: {
    background: `radial-gradient(ellipse at 27% 37%, rgba(239, 83, 80, 0.3) 0%, transparent 50%),
                 radial-gradient(ellipse at 97% 21%, rgba(255, 107, 107, 0.25) 0%, transparent 50%),
                 linear-gradient(135deg, ${BRAND.accent} 0%, #D32F2F 100%)`,
    headlineColor: BRAND.white,
    subtitleColor: 'rgba(255, 255, 255, 0.9)',
    iconBgColor: 'rgba(255, 255, 255, 0.2)',
  },
};

/**
 * Generate the carousel hook template
 *
 * @param {Object} data - Template data
 * @param {Object} helpers - Helper functions from renderer
 * @returns {Object} - Satori-compatible JSX object
 */
function carouselHook(data, helpers = {}) {
  const theme = THEMES[data.theme] || THEMES.dark;
  const icon = ICONS[data.icon] || data.icon || ICONS.heart;

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
        background: theme.background,
        padding: '80px',
        fontFamily: 'Helvetica, Arial, sans-serif',
        position: 'relative',
        overflow: 'hidden',
      },
      children: [
        // Decorative background elements for visual interest
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '-100px',
              right: '-100px',
              width: '400px',
              height: '400px',
              borderRadius: '50%',
              background: 'rgba(255, 255, 255, 0.03)',
            },
          },
        },
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              bottom: '-150px',
              left: '-150px',
              width: '500px',
              height: '500px',
              borderRadius: '50%',
              background: 'rgba(255, 255, 255, 0.02)',
            },
          },
        },

        // Icon container
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              width: '120px',
              height: '120px',
              borderRadius: '30px',
              backgroundColor: theme.iconBgColor,
              marginBottom: '48px',
            },
            children: {
              type: 'div',
              props: {
                style: {
                  fontSize: '64px',
                  lineHeight: 1,
                },
                children: icon,
              },
            },
          },
        },

        // Headline - extreme weight (900) for drama
        {
          type: 'div',
          props: {
            style: {
              fontSize: '72px',
              fontWeight: 900,
              color: theme.headlineColor,
              textAlign: 'center',
              lineHeight: 1.1,
              letterSpacing: '-2px',
              maxWidth: '900px',
              marginBottom: '32px',
            },
            children: data.headline || 'Scroll-Stopping Hook',
          },
        },

        // Subtitle - contrasting light weight (300)
        data.subtitle ? {
          type: 'div',
          props: {
            style: {
              fontSize: '32px',
              fontWeight: 300,
              color: theme.subtitleColor,
              textAlign: 'center',
              lineHeight: 1.4,
              maxWidth: '800px',
              letterSpacing: '0.5px',
            },
            children: data.subtitle,
          },
        } : null,

        // Swipe indicator (subtle)
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              bottom: '60px',
              display: 'flex',
              alignItems: 'center',
              gap: '12px',
              color: theme.subtitleColor,
              opacity: 0.6,
            },
            children: [
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '18px',
                    fontWeight: 400,
                    letterSpacing: '2px',
                    textTransform: 'uppercase',
                  },
                  children: 'Swipe',
                },
              },
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '24px',
                  },
                  children: '\u{1F449}', // 👉
                },
              },
            ],
          },
        },
      ].filter(Boolean),
    },
  };
}

module.exports = carouselHook;
module.exports.BRAND = BRAND;
module.exports.ICONS = ICONS;
module.exports.THEMES = THEMES;
