/**
 * Infographic Comparison Template - Two-column comparison
 *
 * Design Principles:
 * - Split layout with contrasting colors
 * - Large stat badges on each side
 * - Clear visual distinction between options
 * - Supporting details below each stat
 * - Mesh gradient backgrounds
 *
 * Data Structure:
 * {
 *   tag: "TREATMENT COMPARISON",
 *   title: "ACE-I vs ARB in HFrEF",
 *   left: {
 *     label: "ACE Inhibitors",
 *     stat: "22%",
 *     statLabel: "Mortality Reduction",
 *     icon: "pill",
 *     bullets: ["First-line therapy", "More cough (10-15%)", "Lower cost"],
 *     theme: "primary"
 *   },
 *   right: {
 *     label: "ARBs",
 *     stat: "18%",
 *     statLabel: "Mortality Reduction",
 *     icon: "shield",
 *     bullets: ["ACE-I intolerant", "Better tolerated", "Higher cost"],
 *     theme: "accent"
 *   },
 *   source: "Meta-analysis, Circulation 2022",
 *   showFooter: true
 * }
 */

const { BRAND, ICONS, GRADIENTS, createBlob, createTagBadge, createFooter } = require('./constants');

// Theme colors for each side
const SIDE_THEMES = {
  primary: {
    headerBg: `linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.primaryLight} 100%)`,
    statBg: `linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.secondary} 100%)`,
    bulletColor: BRAND.primary,
    bgTint: 'rgba(22, 105, 122, 0.03)',
  },
  success: {
    headerBg: `linear-gradient(135deg, ${BRAND.success} 0%, ${BRAND.successLight} 100%)`,
    statBg: `linear-gradient(135deg, ${BRAND.success} 0%, #2ECC71 100%)`,
    bulletColor: BRAND.success,
    bgTint: 'rgba(39, 174, 96, 0.03)',
  },
  accent: {
    headerBg: `linear-gradient(135deg, ${BRAND.accent} 0%, ${BRAND.accentDark} 100%)`,
    statBg: `linear-gradient(135deg, ${BRAND.accent} 0%, #D32F2F 100%)`,
    bulletColor: BRAND.accent,
    bgTint: 'rgba(239, 83, 80, 0.03)',
  },
  danger: {
    headerBg: `linear-gradient(135deg, ${BRAND.alert} 0%, ${BRAND.mythRedDark} 100%)`,
    statBg: `linear-gradient(135deg, ${BRAND.alert} 0%, #C0392B 100%)`,
    bulletColor: BRAND.alert,
    bgTint: 'rgba(231, 76, 60, 0.03)',
  },
};

/**
 * Create one side of the comparison
 */
function createSide(side, position) {
  const theme = SIDE_THEMES[side.theme] || SIDE_THEMES.primary;
  const icon = ICONS[side.icon] || side.icon || ICONS.pill;
  const isLeft = position === 'left';

  return {
    type: 'div',
    props: {
      style: {
        flex: 1,
        display: 'flex',
        flexDirection: 'column',
        backgroundColor: BRAND.white,
        borderRadius: isLeft ? '24px 0 0 24px' : '0 24px 24px 0',
        overflow: 'hidden',
        boxShadow: '0 8px 32px rgba(22, 105, 122, 0.08)',
      },
      children: [
        // Header with gradient
        {
          type: 'div',
          props: {
            style: {
              background: theme.headerBg,
              padding: '24px 28px',
              display: 'flex',
              alignItems: 'center',
              gap: '14px',
            },
            children: [
              // Icon
              {
                type: 'div',
                props: {
                  style: {
                    width: '52px',
                    height: '52px',
                    borderRadius: '14px',
                    backgroundColor: 'rgba(255, 255, 255, 0.2)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                  },
                  children: {
                    type: 'div',
                    props: {
                      style: { fontSize: '28px', lineHeight: 1 },
                      children: icon,
                    },
                  },
                },
              },
              // Label
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '26px',
                    fontWeight: 700,
                    color: BRAND.white,
                  },
                  children: side.label || 'Option',
                },
              },
            ],
          },
        },

        // Stat section
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              padding: '32px 24px',
              backgroundColor: theme.bgTint,
            },
            children: [
              // Stat badge
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    background: theme.statBg,
                    padding: '24px 48px',
                    borderRadius: '20px',
                    boxShadow: '0 12px 32px rgba(0, 0, 0, 0.1)',
                  },
                  children: {
                    type: 'div',
                    props: {
                      style: {
                        fontSize: '64px',
                        fontWeight: 900,
                        color: BRAND.white,
                        lineHeight: 1,
                        letterSpacing: '-2px',
                      },
                      children: side.stat || '—',
                    },
                  },
                },
              },
              // Stat label
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '18px',
                    fontWeight: 600,
                    color: BRAND.neutralDark,
                    marginTop: '14px',
                    textAlign: 'center',
                  },
                  children: side.statLabel || '',
                },
              },
            ],
          },
        },

        // Bullets section
        {
          type: 'div',
          props: {
            style: {
              flex: 1,
              padding: '20px 28px 28px',
              display: 'flex',
              flexDirection: 'column',
              gap: '12px',
            },
            children: (side.bullets || []).map(text => ({
              type: 'div',
              props: {
                style: {
                  display: 'flex',
                  gap: '12px',
                  alignItems: 'flex-start',
                },
                children: [
                  {
                    type: 'div',
                    props: {
                      style: {
                        width: '8px',
                        height: '8px',
                        borderRadius: '50%',
                        backgroundColor: theme.bulletColor,
                        marginTop: '7px',
                        flexShrink: 0,
                      },
                    },
                  },
                  {
                    type: 'div',
                    props: {
                      style: {
                        fontSize: '17px',
                        lineHeight: 1.4,
                        color: BRAND.textPrimary,
                      },
                      children: text,
                    },
                  },
                ],
              },
            })),
          },
        },
      ],
    },
  };
}

/**
 * Generate the infographic comparison template
 */
function infographicComparison(data, helpers = {}) {
  const showFooter = data.showFooter !== false;

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        width: '100%',
        height: '100%',
        background: GRADIENTS.lightMesh,
        fontFamily: 'Helvetica, Arial, sans-serif',
        position: 'relative',
        overflow: 'hidden',
      },
      children: [
        // Decorative blobs
        createBlob({ top: '-100px', right: '-100px', size: '350px', color: 'rgba(22, 105, 122, 0.04)' }),
        createBlob({ bottom: '-150px', left: '-150px', size: '400px', color: 'rgba(239, 83, 80, 0.04)' }),

        // Content
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flexDirection: 'column',
              flex: 1,
              padding: '48px 50px 32px',
              position: 'relative',
              zIndex: 1,
            },
            children: [
              // Header
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    marginBottom: '28px',
                  },
                  children: [
                    data.tag ? createTagBadge(data.tag) : null,
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '44px',
                          fontWeight: 900,
                          color: BRAND.primary,
                          textAlign: 'center',
                          lineHeight: 1.1,
                          marginTop: data.tag ? '16px' : '0',
                          letterSpacing: '-1px',
                        },
                        children: data.title || 'Comparison',
                      },
                    },
                  ].filter(Boolean),
                },
              },

              // Comparison columns
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    gap: '24px',
                    flex: 1,
                  },
                  children: [
                    createSide(data.left || {}, 'left'),
                    // VS divider
                    {
                      type: 'div',
                      props: {
                        style: {
                          display: 'flex',
                          flexDirection: 'column',
                          alignItems: 'center',
                          justifyContent: 'center',
                          width: '60px',
                        },
                        children: [
                          {
                            type: 'div',
                            props: {
                              style: {
                                width: '56px',
                                height: '56px',
                                borderRadius: '50%',
                                backgroundColor: BRAND.neutralLight,
                                border: `3px solid ${BRAND.primary}`,
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                              },
                              children: {
                                type: 'div',
                                props: {
                                  style: {
                                    fontSize: '20px',
                                    fontWeight: 700,
                                    color: BRAND.primary,
                                  },
                                  children: 'VS',
                                },
                              },
                            },
                          },
                        ],
                      },
                    },
                    createSide(data.right || {}, 'right'),
                  ],
                },
              },

              // Source
              data.source ? {
                type: 'div',
                props: {
                  style: {
                    marginTop: '20px',
                    fontSize: '15px',
                    color: BRAND.textMuted,
                    textAlign: 'center',
                  },
                  children: `Source: ${data.source}`,
                },
              } : null,
            ].filter(Boolean),
          },
        },

        // Footer
        showFooter ? createFooter({
          name: data.footerName,
          handle: data.footerHandle,
          height: 110,
        }) : null,
      ].filter(Boolean),
    },
  };
}

module.exports = infographicComparison;
