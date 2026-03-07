/**
 * Infographic Myth Template - Myth vs Truth split design
 *
 * Design Principles:
 * - Split layout: red (myth) vs green (truth)
 * - Large myth/truth labels
 * - Clear visual distinction
 * - Icon indicators (X for myth, check for truth)
 * - Evidence/source citation
 *
 * Data Structure:
 * {
 *   tag: "MYTH BUSTED",
 *   title: "Statins cause muscle damage in everyone",
 *   myth: {
 *     text: "Taking statins will definitely give you muscle pain",
 *     icon: "cross"
 *   },
 *   truth: {
 *     text: "Only 5-10% experience muscle symptoms, and most can continue therapy with adjustment",
 *     icon: "check"
 *   },
 *   evidence: "Meta-analysis of 19 RCTs (n=71,000)",
 *   source: "Lancet 2022",
 *   showFooter: true
 * }
 */

const { BRAND, ICONS, createBlob, createTagBadge, createFooter } = require('./constants');

/**
 * Generate the infographic myth template
 */
function infographicMyth(data, helpers = {}) {
  const showFooter = data.showFooter !== false;
  const mythIcon = ICONS[data.myth?.icon] || ICONS.cross;
  const truthIcon = ICONS[data.truth?.icon] || ICONS.check;

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        width: '100%',
        height: '100%',
        backgroundColor: BRAND.neutralLight,
        fontFamily: 'Helvetica, Arial, sans-serif',
        position: 'relative',
        overflow: 'hidden',
      },
      children: [
        // Header section
        {
          type: 'div',
          props: {
            style: {
              padding: '48px 50px 32px',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              backgroundColor: BRAND.backgroundWash,
            },
            children: [
              data.tag ? createTagBadge(data.tag, { color: BRAND.accent }) : null,
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '40px',
                    fontWeight: 900,
                    color: BRAND.primary,
                    textAlign: 'center',
                    lineHeight: 1.15,
                    marginTop: data.tag ? '16px' : '0',
                    maxWidth: '900px',
                    letterSpacing: '-0.5px',
                  },
                  children: data.title || 'Myth vs Truth',
                },
              },
            ].filter(Boolean),
          },
        },

        // Split panels
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flex: 1,
              gap: '4px',
            },
            children: [
              // MYTH side (red)
              {
                type: 'div',
                props: {
                  style: {
                    flex: 1,
                    background: `linear-gradient(180deg, ${BRAND.mythRed} 0%, ${BRAND.alert} 100%)`,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    padding: '40px 36px',
                    position: 'relative',
                    overflow: 'hidden',
                  },
                  children: [
                    // Decorative blob
                    {
                      type: 'div',
                      props: {
                        style: {
                          position: 'absolute',
                          top: '-100px',
                          left: '-100px',
                          width: '300px',
                          height: '300px',
                          borderRadius: '50%',
                          background: 'rgba(255, 255, 255, 0.08)',
                        },
                      },
                    },

                    // Icon badge
                    {
                      type: 'div',
                      props: {
                        style: {
                          width: '80px',
                          height: '80px',
                          borderRadius: '50%',
                          backgroundColor: 'rgba(255, 255, 255, 0.2)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          marginBottom: '20px',
                        },
                        children: {
                          type: 'div',
                          props: {
                            style: { fontSize: '44px', lineHeight: 1 },
                            children: mythIcon,
                          },
                        },
                      },
                    },

                    // Label
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '28px',
                          fontWeight: 900,
                          color: BRAND.white,
                          letterSpacing: '4px',
                          textTransform: 'uppercase',
                          marginBottom: '24px',
                        },
                        children: 'MYTH',
                      },
                    },

                    // Text
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '24px',
                          fontWeight: 500,
                          color: BRAND.white,
                          textAlign: 'center',
                          lineHeight: 1.4,
                          maxWidth: '400px',
                          position: 'relative',
                          zIndex: 1,
                        },
                        children: `"${data.myth?.text || 'Common misconception'}"`,
                      },
                    },
                  ],
                },
              },

              // TRUTH side (green)
              {
                type: 'div',
                props: {
                  style: {
                    flex: 1,
                    background: `linear-gradient(180deg, ${BRAND.success} 0%, #1E8449 100%)`,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    padding: '40px 36px',
                    position: 'relative',
                    overflow: 'hidden',
                  },
                  children: [
                    // Decorative blob
                    {
                      type: 'div',
                      props: {
                        style: {
                          position: 'absolute',
                          bottom: '-100px',
                          right: '-100px',
                          width: '300px',
                          height: '300px',
                          borderRadius: '50%',
                          background: 'rgba(255, 255, 255, 0.08)',
                        },
                      },
                    },

                    // Icon badge
                    {
                      type: 'div',
                      props: {
                        style: {
                          width: '80px',
                          height: '80px',
                          borderRadius: '50%',
                          backgroundColor: 'rgba(255, 255, 255, 0.2)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          marginBottom: '20px',
                        },
                        children: {
                          type: 'div',
                          props: {
                            style: { fontSize: '44px', lineHeight: 1 },
                            children: truthIcon,
                          },
                        },
                      },
                    },

                    // Label
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '28px',
                          fontWeight: 900,
                          color: BRAND.white,
                          letterSpacing: '4px',
                          textTransform: 'uppercase',
                          marginBottom: '24px',
                        },
                        children: 'TRUTH',
                      },
                    },

                    // Text
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '24px',
                          fontWeight: 500,
                          color: BRAND.white,
                          textAlign: 'center',
                          lineHeight: 1.4,
                          maxWidth: '400px',
                          position: 'relative',
                          zIndex: 1,
                        },
                        children: data.truth?.text || 'Evidence-based fact',
                      },
                    },
                  ],
                },
              },
            ],
          },
        },

        // Evidence bar
        (data.evidence || data.source) ? {
          type: 'div',
          props: {
            style: {
              backgroundColor: BRAND.primary,
              padding: '20px 50px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '20px',
            },
            children: [
              data.evidence ? {
                type: 'div',
                props: {
                  style: {
                    fontSize: '17px',
                    fontWeight: 600,
                    color: BRAND.white,
                  },
                  children: data.evidence,
                },
              } : null,
              data.source ? {
                type: 'div',
                props: {
                  style: {
                    fontSize: '15px',
                    color: 'rgba(255, 255, 255, 0.8)',
                    fontStyle: 'italic',
                  },
                  children: `— ${data.source}`,
                },
              } : null,
            ].filter(Boolean),
          },
        } : null,

        // Footer
        showFooter ? createFooter({
          name: data.footerName,
          handle: data.footerHandle,
          dark: false,
          height: 120,
        }) : null,
      ].filter(Boolean),
    },
  };
}

module.exports = infographicMyth;
