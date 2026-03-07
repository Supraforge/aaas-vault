/**
 * Carousel Stat Template - Big number with visual impact
 *
 * Design Principles:
 * - Number in large colored circle or rounded rectangle
 * - Supporting icon (chart, heart, pill)
 * - Label below the number
 * - Context/source at bottom
 * - Background: subtle gradient, not flat
 *
 * Data Structure:
 * {
 *   stat: "26%",
 *   label: "Mortality Reduction",
 *   context: "HR 0.74, 95% CI 0.65-0.85",
 *   source: "PARADIGM-HF Trial",
 *   icon: "chart-up" | "heart" | "pill" | "shield",
 *   theme: "primary" | "success" | "accent",
 *   slideNumber: 3,
 *   totalSlides: 10,
 *   showFooter: true,
 *   footerName: "Dr. Shailesh Singh",
 *   footerHandle: "@heartdocshailesh"
 * }
 */

// Brand colors
const BRAND = {
  primary: '#16697A',
  primaryLight: '#1E8A9F',
  secondary: '#218380',
  accent: '#EF5350',
  accentDark: '#D32F2F',
  success: '#27AE60',
  successLight: '#2ECC71',
  mythRed: '#FF6B6B',
  backgroundWash: '#E8F5F4',
  neutralLight: '#F9FAFB',
  neutralDark: '#2F3E46',
  white: '#FFFFFF',
};

// Icon map
const ICONS = {
  'chart-up': '\u{1F4C8}',    // 📈
  'chart-down': '\u{1F4C9}',  // 📉
  heart: '\u{2764}\u{FE0F}',  // ❤️
  'heart-pulse': '\u{1F493}', // 💓
  pill: '\u{1F48A}',          // 💊
  shield: '\u{1F6E1}\u{FE0F}',// 🛡️
  star: '\u{2B50}',           // ⭐
  target: '\u{1F3AF}',        // 🎯
  trophy: '\u{1F3C6}',        // 🏆
  lightning: '\u{26A1}',      // ⚡
  check: '\u{2705}',          // ✅
  fire: '\u{1F525}',          // 🔥
  brain: '\u{1F9E0}',         // 🧠
  stethoscope: '\u{1FA7A}',   // 🩺
  clock: '\u{23F0}',          // ⏰
  people: '\u{1F465}',        // 👥
  graph: '\u{1F4CA}',         // 📊
};

// Theme configurations
const THEMES = {
  primary: {
    background: `linear-gradient(135deg, ${BRAND.backgroundWash} 0%, ${BRAND.white} 100%)`,
    statBg: `linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.primaryLight} 100%)`,
    statColor: BRAND.white,
    labelColor: BRAND.neutralDark,
    contextColor: BRAND.secondary,
  },
  success: {
    background: `linear-gradient(135deg, #E8F8F0 0%, ${BRAND.white} 100%)`,
    statBg: `linear-gradient(135deg, ${BRAND.success} 0%, ${BRAND.successLight} 100%)`,
    statColor: BRAND.white,
    labelColor: BRAND.neutralDark,
    contextColor: BRAND.success,
  },
  accent: {
    background: `linear-gradient(135deg, #FFF3F2 0%, ${BRAND.white} 100%)`,
    statBg: `linear-gradient(135deg, ${BRAND.accent} 0%, ${BRAND.accentDark} 100%)`,
    statColor: BRAND.white,
    labelColor: BRAND.neutralDark,
    contextColor: BRAND.accent,
  },
  dark: {
    background: `linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.secondary} 100%)`,
    statBg: 'rgba(255, 255, 255, 0.15)',
    statColor: BRAND.white,
    labelColor: 'rgba(255, 255, 255, 0.95)',
    contextColor: 'rgba(255, 255, 255, 0.8)',
  },
};

/**
 * Generate the carousel stat template
 *
 * @param {Object} data - Template data
 * @param {Object} helpers - Helper functions from renderer
 * @returns {Object} - Satori-compatible JSX object
 */
function carouselStat(data, helpers = {}) {
  const theme = THEMES[data.theme] || THEMES.primary;
  const icon = ICONS[data.icon] || data.icon || ICONS['chart-up'];
  const slideNumber = data.slideNumber || '';
  const totalSlides = data.totalSlides || '';
  const showFooter = data.showFooter !== false;
  const isDarkTheme = data.theme === 'dark';

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        width: '100%',
        height: '100%',
        background: theme.background,
        fontFamily: 'Helvetica, Arial, sans-serif',
        position: 'relative',
        overflow: 'hidden',
      },
      children: [
        // Background decorative elements
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '-200px',
              right: '-200px',
              width: '600px',
              height: '600px',
              borderRadius: '50%',
              background: isDarkTheme
                ? 'rgba(255, 255, 255, 0.03)'
                : `rgba(22, 105, 122, 0.03)`,
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
              width: '400px',
              height: '400px',
              borderRadius: '50%',
              background: isDarkTheme
                ? 'rgba(255, 255, 255, 0.02)'
                : `rgba(22, 105, 122, 0.02)`,
            },
          },
        },

        // Slide number indicator
        slideNumber ? {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '32px',
              right: '32px',
              fontSize: '20px',
              fontWeight: 600,
              color: isDarkTheme ? BRAND.white : BRAND.neutralDark,
              backgroundColor: isDarkTheme ? 'rgba(255, 255, 255, 0.15)' : 'rgba(22, 105, 122, 0.1)',
              padding: '8px 16px',
              borderRadius: '20px',
              zIndex: 10,
            },
            children: totalSlides ? `${slideNumber}/${totalSlides}` : String(slideNumber),
          },
        } : null,

        // Main content
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              flex: 1,
              padding: '80px 60px',
              gap: '32px',
            },
            children: [
              // Icon
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '64px',
                    lineHeight: 1,
                    marginBottom: '16px',
                  },
                  children: icon,
                },
              },

              // Stat container (large rounded rectangle)
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    background: theme.statBg,
                    padding: '48px 80px',
                    borderRadius: '32px',
                    boxShadow: isDarkTheme
                      ? 'none'
                      : '0 20px 60px rgba(22, 105, 122, 0.15)',
                  },
                  children: {
                    type: 'div',
                    props: {
                      style: {
                        fontSize: '120px',
                        fontWeight: 900,
                        color: theme.statColor,
                        lineHeight: 1,
                        letterSpacing: '-4px',
                      },
                      children: data.stat || '—',
                    },
                  },
                },
              },

              // Label
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '40px',
                    fontWeight: 700,
                    color: theme.labelColor,
                    textAlign: 'center',
                    lineHeight: 1.3,
                    maxWidth: '800px',
                  },
                  children: data.label || 'Key Metric',
                },
              },

              // Context (HR, CI, etc.)
              data.context ? {
                type: 'div',
                props: {
                  style: {
                    fontSize: '24px',
                    fontWeight: 500,
                    color: theme.contextColor,
                    textAlign: 'center',
                    fontStyle: 'italic',
                    padding: '12px 24px',
                    backgroundColor: isDarkTheme
                      ? 'rgba(255, 255, 255, 0.1)'
                      : 'rgba(22, 105, 122, 0.08)',
                    borderRadius: '12px',
                  },
                  children: data.context,
                },
              } : null,

              // Source
              data.source ? {
                type: 'div',
                props: {
                  style: {
                    fontSize: '18px',
                    fontWeight: 400,
                    color: isDarkTheme ? 'rgba(255, 255, 255, 0.6)' : BRAND.neutralDark,
                    opacity: isDarkTheme ? 1 : 0.6,
                    marginTop: '8px',
                  },
                  children: `Source: ${data.source}`,
                },
              } : null,
            ].filter(Boolean),
          },
        },

        // Footer
        showFooter ? {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '24px',
              height: '140px',
              backgroundColor: isDarkTheme ? 'rgba(0, 0, 0, 0.2)' : BRAND.white,
              borderTop: isDarkTheme ? 'none' : `3px solid ${BRAND.primary}`,
              padding: '0 60px',
            },
            children: [
              // Profile placeholder
              {
                type: 'div',
                props: {
                  style: {
                    width: '80px',
                    height: '80px',
                    borderRadius: '50%',
                    backgroundColor: isDarkTheme ? BRAND.white : BRAND.primary,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                  },
                  children: {
                    type: 'div',
                    props: {
                      style: {
                        fontSize: '36px',
                        color: isDarkTheme ? BRAND.primary : BRAND.white,
                        fontWeight: 700,
                      },
                      children: (data.footerName || 'Dr. S').charAt(0).toUpperCase(),
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
                          color: isDarkTheme ? BRAND.white : BRAND.neutralDark,
                        },
                        children: data.footerName || 'Dr. Shailesh Singh',
                      },
                    },
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '20px',
                          fontWeight: 500,
                          color: isDarkTheme ? BRAND.backgroundWash : BRAND.primary,
                        },
                        children: data.footerHandle || '@heartdocshailesh',
                      },
                    },
                  ],
                },
              },
            ],
          },
        } : null,
      ].filter(Boolean),
    },
  };
}

module.exports = carouselStat;
module.exports.BRAND = BRAND;
module.exports.ICONS = ICONS;
module.exports.THEMES = THEMES;
