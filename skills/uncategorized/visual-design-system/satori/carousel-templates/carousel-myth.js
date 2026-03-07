/**
 * Carousel Myth Template - Myth-busting slide with visual satisfaction
 *
 * Design Principles:
 * - Split layout: top half (myth) / bottom half (truth)
 * - Top: Soft red background, X icon, strikethrough text
 * - Bottom: Success green background, checkmark icon, bold text
 * - Smooth gradient transition between sections
 * - Slide number indicator (subtle)
 *
 * Data Structure:
 * {
 *   slideNumber: 2,
 *   totalSlides: 10,
 *   myth: "Statins cause muscle pain in everyone",
 *   truth: "Only 5-10% experience muscle symptoms, and it's usually mild",
 *   source: "Lancet 2022",
 *   showFooter: true,
 *   footerName: "Dr. Shailesh Singh",
 *   footerHandle: "@heartdocshailesh"
 * }
 */

// Brand colors
const BRAND = {
  primary: '#16697A',
  secondary: '#218380',
  accent: '#EF5350',
  success: '#27AE60',
  successDark: '#1E8449',
  mythRed: '#FF6B6B',
  mythRedDark: '#E74C3C',
  backgroundWash: '#E8F5F4',
  neutralDark: '#2F3E46',
  white: '#FFFFFF',
};

/**
 * Generate the carousel myth template
 *
 * @param {Object} data - Template data
 * @param {Object} helpers - Helper functions from renderer
 * @returns {Object} - Satori-compatible JSX object
 */
function carouselMyth(data, helpers = {}) {
  const slideNumber = data.slideNumber || '';
  const totalSlides = data.totalSlides || '';
  const showSource = data.source && data.source.length > 0;
  const showFooter = data.showFooter !== false;

  // Calculate heights based on whether footer is shown
  const contentHeight = showFooter ? 'calc(100% - 140px)' : '100%';
  const footerHeight = '140px';

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        width: '100%',
        height: '100%',
        fontFamily: 'Helvetica, Arial, sans-serif',
        position: 'relative',
        overflow: 'hidden',
        backgroundColor: BRAND.backgroundWash,
      },
      children: [
        // Main content area
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flexDirection: 'column',
              flex: 1,
            },
            children: [
              // Slide number indicator (top right)
              slideNumber ? {
                type: 'div',
                props: {
                  style: {
                    position: 'absolute',
                    top: '32px',
                    right: '32px',
                    fontSize: '20px',
                    fontWeight: 600,
                    color: BRAND.white,
                    backgroundColor: 'rgba(0, 0, 0, 0.2)',
                    padding: '8px 16px',
                    borderRadius: '20px',
                    zIndex: 10,
                  },
                  children: totalSlides ? `${slideNumber}/${totalSlides}` : String(slideNumber),
                },
              } : null,

              // MYTH Section (Top Half)
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    flex: 1,
                    padding: '60px 60px 40px 60px',
                    background: `linear-gradient(180deg, ${BRAND.mythRed} 0%, ${BRAND.mythRedDark} 100%)`,
                    position: 'relative',
                  },
                  children: [
                    // MYTH label with X icon
                    {
                      type: 'div',
                      props: {
                        style: {
                          display: 'flex',
                          alignItems: 'center',
                          gap: '16px',
                          marginBottom: '24px',
                        },
                        children: [
                          // X icon in circle
                          {
                            type: 'div',
                            props: {
                              style: {
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                width: '56px',
                                height: '56px',
                                borderRadius: '50%',
                                backgroundColor: 'rgba(255, 255, 255, 0.25)',
                              },
                              children: {
                                type: 'div',
                                props: {
                                  style: {
                                    fontSize: '32px',
                                    lineHeight: 1,
                                  },
                                  children: '\u{274C}', // ❌
                                },
                              },
                            },
                          },
                          // MYTH text
                          {
                            type: 'div',
                            props: {
                              style: {
                                fontSize: '24px',
                                fontWeight: 700,
                                color: BRAND.white,
                                letterSpacing: '4px',
                                textTransform: 'uppercase',
                              },
                              children: 'MYTH',
                            },
                          },
                        ],
                      },
                    },

                    // Myth text with strikethrough effect
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '36px',
                          fontWeight: 500,
                          color: BRAND.white,
                          textAlign: 'center',
                          lineHeight: 1.3,
                          maxWidth: '900px',
                          textDecoration: 'line-through',
                          textDecorationColor: 'rgba(255, 255, 255, 0.6)',
                          textDecorationThickness: '3px',
                          opacity: 0.95,
                        },
                        children: `"${data.myth || 'Common myth goes here'}"`,
                      },
                    },
                  ],
                },
              },

              // Gradient transition line
              {
                type: 'div',
                props: {
                  style: {
                    height: '8px',
                    background: `linear-gradient(90deg, ${BRAND.mythRedDark} 0%, ${BRAND.successDark} 100%)`,
                  },
                },
              },

              // TRUTH Section (Bottom Half)
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    flex: 1,
                    padding: '40px 60px 60px 60px',
                    background: `linear-gradient(180deg, ${BRAND.successDark} 0%, ${BRAND.success} 100%)`,
                    position: 'relative',
                  },
                  children: [
                    // TRUTH label with check icon
                    {
                      type: 'div',
                      props: {
                        style: {
                          display: 'flex',
                          alignItems: 'center',
                          gap: '16px',
                          marginBottom: '24px',
                        },
                        children: [
                          // Check icon in circle
                          {
                            type: 'div',
                            props: {
                              style: {
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                width: '56px',
                                height: '56px',
                                borderRadius: '50%',
                                backgroundColor: 'rgba(255, 255, 255, 0.25)',
                              },
                              children: {
                                type: 'div',
                                props: {
                                  style: {
                                    fontSize: '32px',
                                    lineHeight: 1,
                                  },
                                  children: '\u{2705}', // ✅
                                },
                              },
                            },
                          },
                          // TRUTH text
                          {
                            type: 'div',
                            props: {
                              style: {
                                fontSize: '24px',
                                fontWeight: 700,
                                color: BRAND.white,
                                letterSpacing: '4px',
                                textTransform: 'uppercase',
                              },
                              children: 'TRUTH',
                            },
                          },
                        ],
                      },
                    },

                    // Truth text - bold and clear
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '36px',
                          fontWeight: 700,
                          color: BRAND.white,
                          textAlign: 'center',
                          lineHeight: 1.3,
                          maxWidth: '900px',
                        },
                        children: data.truth || 'The actual truth goes here',
                      },
                    },

                    // Source citation
                    showSource ? {
                      type: 'div',
                      props: {
                        style: {
                          position: 'absolute',
                          bottom: '20px',
                          right: '30px',
                          fontSize: '16px',
                          fontWeight: 500,
                          color: 'rgba(255, 255, 255, 0.7)',
                          fontStyle: 'italic',
                        },
                        children: `Source: ${data.source}`,
                      },
                    } : null,
                  ].filter(Boolean),
                },
              },
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
              height: footerHeight,
              backgroundColor: BRAND.white,
              borderTop: `3px solid ${BRAND.primary}`,
              padding: '0 60px',
            },
            children: [
              // Profile placeholder (circle)
              {
                type: 'div',
                props: {
                  style: {
                    width: '80px',
                    height: '80px',
                    borderRadius: '50%',
                    backgroundColor: BRAND.primary,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                  },
                  children: {
                    type: 'div',
                    props: {
                      style: {
                        fontSize: '36px',
                        color: BRAND.white,
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
                          color: BRAND.neutralDark,
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
                          color: BRAND.primary,
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

module.exports = carouselMyth;
module.exports.BRAND = BRAND;
