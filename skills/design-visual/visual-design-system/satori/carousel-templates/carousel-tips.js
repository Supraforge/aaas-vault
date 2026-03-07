/**
 * Carousel Tips Template - Actionable tips in card layout
 *
 * Design Principles:
 * - Title at top
 * - Each tip in a card with numbered circle (brand-primary)
 * - Tip text with optional icon
 * - Cards have subtle shadow/border
 * - Stacked vertically with consistent gaps
 *
 * Data Structure:
 * {
 *   title: "3 Ways to Protect Your Heart",
 *   tips: [
 *     { number: 1, text: "Take statins as prescribed", icon: "pill" },
 *     { number: 2, text: "Monitor your cholesterol yearly", icon: "chart" },
 *     { number: 3, text: "Exercise 150 min/week", icon: "running" }
 *   ],
 *   theme: "light" | "dark",
 *   slideNumber: 5,
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
  success: '#27AE60',
  backgroundWash: '#E8F5F4',
  neutralLight: '#F9FAFB',
  neutralDark: '#2F3E46',
  white: '#FFFFFF',
};

// Icon map
const ICONS = {
  pill: '\u{1F48A}',           // 💊
  heart: '\u{2764}\u{FE0F}',   // ❤️
  chart: '\u{1F4C8}',          // 📈
  running: '\u{1F3C3}',        // 🏃
  food: '\u{1F957}',           // 🥗
  sleep: '\u{1F634}',          // 😴
  water: '\u{1F4A7}',          // 💧
  apple: '\u{1F34E}',          // 🍎
  clock: '\u{23F0}',           // ⏰
  calendar: '\u{1F4C5}',       // 📅
  check: '\u{2705}',           // ✅
  star: '\u{2B50}',            // ⭐
  target: '\u{1F3AF}',         // 🎯
  brain: '\u{1F9E0}',          // 🧠
  stethoscope: '\u{1FA7A}',    // 🩺
  doctor: '\u{1F468}\u{200D}\u{2695}\u{FE0F}', // 👨‍⚕️
  hospital: '\u{1F3E5}',       // 🏥
  muscle: '\u{1F4AA}',         // 💪
  meditation: '\u{1F9D8}',     // 🧘
  scales: '\u{2696}\u{FE0F}',  // ⚖️
  sun: '\u{2600}\u{FE0F}',     // ☀️
  moon: '\u{1F319}',           // 🌙
  smoking: '\u{1F6AD}',        // 🚭
  alcohol: '\u{1F377}',        // 🍷
  coffee: '\u{2615}',          // ☕
  walking: '\u{1F6B6}',        // 🚶
  cycling: '\u{1F6B4}',        // 🚴
  swimming: '\u{1F3CA}',       // 🏊
  yoga: '\u{1F9D8}',           // 🧘
  weights: '\u{1F3CB}\u{FE0F}',// 🏋️
};

// Theme configurations
const THEMES = {
  light: {
    background: `linear-gradient(180deg, ${BRAND.backgroundWash} 0%, ${BRAND.white} 100%)`,
    titleColor: BRAND.primary,
    cardBg: BRAND.white,
    cardBorder: 'rgba(22, 105, 122, 0.1)',
    cardShadow: '0 4px 20px rgba(22, 105, 122, 0.08)',
    numberBg: BRAND.primary,
    numberColor: BRAND.white,
    textColor: BRAND.neutralDark,
  },
  dark: {
    background: `linear-gradient(180deg, ${BRAND.primary} 0%, ${BRAND.secondary} 100%)`,
    titleColor: BRAND.white,
    cardBg: 'rgba(255, 255, 255, 0.1)',
    cardBorder: 'rgba(255, 255, 255, 0.15)',
    cardShadow: 'none',
    numberBg: BRAND.white,
    numberColor: BRAND.primary,
    textColor: BRAND.white,
  },
};

/**
 * Generate the carousel tips template
 *
 * @param {Object} data - Template data
 * @param {Object} helpers - Helper functions from renderer
 * @returns {Object} - Satori-compatible JSX object
 */
function carouselTips(data, helpers = {}) {
  const theme = THEMES[data.theme] || THEMES.light;
  const tips = data.tips || [];
  const slideNumber = data.slideNumber || '';
  const totalSlides = data.totalSlides || '';
  const showFooter = data.showFooter !== false;
  const isDarkTheme = data.theme === 'dark';

  // Calculate card sizing based on number of tips
  const maxTips = 5;
  const displayTips = tips.slice(0, maxTips);
  const cardGap = displayTips.length <= 3 ? 24 : 16;

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
        !isDarkTheme ? {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '-100px',
              right: '-100px',
              width: '400px',
              height: '400px',
              borderRadius: '50%',
              background: 'rgba(22, 105, 122, 0.03)',
            },
          },
        } : null,

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
              flex: 1,
              padding: '60px',
              gap: '32px',
            },
            children: [
              // Title
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '44px',
                    fontWeight: 700,
                    color: theme.titleColor,
                    textAlign: 'center',
                    lineHeight: 1.2,
                    marginBottom: '16px',
                  },
                  children: data.title || 'Tips',
                },
              },

              // Tips container
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    gap: `${cardGap}px`,
                    flex: 1,
                    justifyContent: displayTips.length <= 3 ? 'center' : 'flex-start',
                  },
                  children: displayTips.map((tip, index) => {
                    const tipIcon = ICONS[tip.icon] || tip.icon || '';

                    return {
                      type: 'div',
                      props: {
                        key: index,
                        style: {
                          display: 'flex',
                          alignItems: 'center',
                          gap: '24px',
                          backgroundColor: theme.cardBg,
                          border: `2px solid ${theme.cardBorder}`,
                          borderRadius: '20px',
                          padding: displayTips.length <= 3 ? '28px 32px' : '20px 28px',
                          boxShadow: theme.cardShadow,
                        },
                        children: [
                          // Number circle
                          {
                            type: 'div',
                            props: {
                              style: {
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                width: displayTips.length <= 3 ? '60px' : '50px',
                                height: displayTips.length <= 3 ? '60px' : '50px',
                                minWidth: displayTips.length <= 3 ? '60px' : '50px',
                                borderRadius: '50%',
                                backgroundColor: theme.numberBg,
                              },
                              children: {
                                type: 'div',
                                props: {
                                  style: {
                                    fontSize: displayTips.length <= 3 ? '28px' : '24px',
                                    fontWeight: 700,
                                    color: theme.numberColor,
                                    lineHeight: 1,
                                  },
                                  children: String(tip.number || index + 1),
                                },
                              },
                            },
                          },

                          // Text
                          {
                            type: 'div',
                            props: {
                              style: {
                                flex: 1,
                                fontSize: displayTips.length <= 3 ? '30px' : '26px',
                                fontWeight: 500,
                                color: theme.textColor,
                                lineHeight: 1.4,
                              },
                              children: tip.text || '',
                            },
                          },

                          // Icon (optional)
                          tipIcon ? {
                            type: 'div',
                            props: {
                              style: {
                                fontSize: displayTips.length <= 3 ? '40px' : '32px',
                                lineHeight: 1,
                              },
                              children: tipIcon,
                            },
                          } : null,
                        ].filter(Boolean),
                      },
                    };
                  }),
                },
              },
            ],
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

module.exports = carouselTips;
module.exports.BRAND = BRAND;
module.exports.ICONS = ICONS;
module.exports.THEMES = THEMES;
