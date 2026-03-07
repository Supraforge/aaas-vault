/**
 * Infographic Dense Template - Multi-section information layout
 *
 * COMPLETELY REBUILT with carousel visual language:
 * - Mesh gradient background
 * - Bold headline with 900 weight
 * - Styled section cards with accent borders
 * - Icon support for sections
 * - Gradient callout bar
 * - Branded footer
 *
 * Data Structure:
 * {
 *   tag: "PATIENT GUIDE",
 *   title: "GLP-1 Roll-Off in Heart Patients",
 *   subtitle: "A practical tapering infographic",
 *   icon: "pill",
 *   sections: [
 *     { title: "Who this is for", bullets: ["..."], icon: "people", accent: "teal" },
 *     { title: "Red flags", bullets: ["..."], icon: "warning", accent: "danger" }
 *   ],
 *   callout: { label: "Bottom line", text: "..." },
 *   footer: "Educational infographic. Not medical advice.",
 *   showBrandFooter: true
 * }
 */

const { BRAND, ICONS, GRADIENTS, createBlob, createTagBadge, createFooter, hexToRgba } = require('./constants');

/**
 * Create a styled section card with icon and accent
 */
function createSection(section, index) {
  const accentColor = section.accent === 'danger' ? BRAND.alert :
                     section.accent === 'success' ? BRAND.success :
                     section.accent === 'accent' ? BRAND.accent : BRAND.secondary;

  const icon = ICONS[section.icon] || section.icon || null;

  return {
    type: 'div',
    props: {
      style: {
        width: '470px',
        backgroundColor: 'rgba(255, 255, 255, 0.97)',
        border: `1px solid ${BRAND.backgroundWash}`,
        borderRadius: '24px',
        padding: '24px 28px',
        display: 'flex',
        flexDirection: 'column',
        boxShadow: '0 8px 32px rgba(22, 105, 122, 0.08)',
        position: 'relative',
        overflow: 'hidden',
      },
      children: [
        // Accent bar at top
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: 0,
              left: 0,
              right: 0,
              height: '4px',
              background: `linear-gradient(90deg, ${accentColor} 0%, ${hexToRgba(accentColor, 0.53)} 100%)`,
            },
          },
        },

        // Title row with icon
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              alignItems: 'center',
              gap: '12px',
              marginBottom: '14px',
              marginTop: '4px',
            },
            children: [
              // Icon (if provided)
              icon ? {
                type: 'div',
                props: {
                  style: {
                    fontSize: '28px',
                    lineHeight: 1,
                  },
                  children: icon,
                },
              } : null,
              // Title
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '22px',
                    fontWeight: 700,
                    color: BRAND.primary,
                  },
                  children: section.title || `Section ${index + 1}`,
                },
              },
            ].filter(Boolean),
          },
        },

        // Bullets
        ...(section.bullets || []).map(text => ({
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
                    lineHeight: 1.45,
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
 * Generate the infographic dense template
 */
function infographicDense(data, helpers = {}) {
  const sections = data.sections || [];
  const showBrandFooter = data.showBrandFooter !== false;
  const headerIcon = ICONS[data.icon] || data.icon || null;

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
        createBlob({ top: '-120px', right: '-120px', size: '400px', color: 'rgba(33, 131, 128, 0.06)' }),
        createBlob({ bottom: '-180px', left: '-180px', size: '500px', color: 'rgba(239, 83, 80, 0.05)' }),
        createBlob({ top: '50%', right: '-80px', size: '250px', color: 'rgba(22, 105, 122, 0.04)' }),

        // Content container
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flexDirection: 'column',
              flex: 1,
              padding: '48px 50px 24px',
              position: 'relative',
              zIndex: 1,
            },
            children: [
              // Header section
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    marginBottom: '28px',
                  },
                  children: [
                    // Tag
                    data.tag ? createTagBadge(data.tag) : null,

                    // Title row with optional icon
                    {
                      type: 'div',
                      props: {
                        style: {
                          display: 'flex',
                          alignItems: 'center',
                          gap: '20px',
                          marginTop: data.tag ? '16px' : '0',
                        },
                        children: [
                          // Header icon
                          headerIcon ? {
                            type: 'div',
                            props: {
                              style: {
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                width: '72px',
                                height: '72px',
                                borderRadius: '20px',
                                backgroundColor: 'rgba(22, 105, 122, 0.1)',
                              },
                              children: {
                                type: 'div',
                                props: {
                                  style: { fontSize: '40px', lineHeight: 1 },
                                  children: headerIcon,
                                },
                              },
                            },
                          } : null,

                          // Title
                          {
                            type: 'div',
                            props: {
                              style: {
                                fontSize: '48px',
                                fontWeight: 900,
                                color: BRAND.primary,
                                lineHeight: 1.1,
                                letterSpacing: '-1px',
                              },
                              children: data.title || 'Infographic Title',
                            },
                          },
                        ].filter(Boolean),
                      },
                    },

                    // Subtitle
                    data.subtitle ? {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '22px',
                          fontWeight: 300,
                          color: BRAND.textSecondary,
                          marginTop: '10px',
                          marginLeft: headerIcon ? '92px' : '0',
                        },
                        children: data.subtitle,
                      },
                    } : null,
                  ].filter(Boolean),
                },
              },

              // Cards grid
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexWrap: 'wrap',
                    gap: '20px',
                    justifyContent: 'space-between',
                    flex: 1,
                  },
                  children: sections.slice(0, 6).map((section, i) => createSection(section, i)),
                },
              },

              // Callout bar
              data.callout ? {
                type: 'div',
                props: {
                  style: {
                    marginTop: '24px',
                    background: `linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.secondary} 100%)`,
                    color: BRAND.white,
                    borderRadius: '20px',
                    padding: '20px 28px',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '20px',
                    boxShadow: '0 12px 40px rgba(22, 105, 122, 0.2)',
                  },
                  children: [
                    // Label badge
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '13px',
                          letterSpacing: '1.5px',
                          fontWeight: 700,
                          color: 'rgba(255, 255, 255, 0.85)',
                          backgroundColor: 'rgba(255, 255, 255, 0.15)',
                          padding: '8px 14px',
                          borderRadius: '8px',
                          textTransform: 'uppercase',
                          flexShrink: 0,
                        },
                        children: data.callout.label || 'BOTTOM LINE',
                      },
                    },
                    // Text
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '20px',
                          fontWeight: 600,
                          color: BRAND.white,
                          lineHeight: 1.4,
                        },
                        children: data.callout.text || '',
                      },
                    },
                  ],
                },
              } : null,

              // Disclaimer footer
              data.footer ? {
                type: 'div',
                props: {
                  style: {
                    marginTop: '16px',
                    fontSize: '13px',
                    color: BRAND.textMuted,
                    textAlign: 'center',
                  },
                  children: data.footer,
                },
              } : null,
            ].filter(Boolean),
          },
        },

        // Brand footer
        showBrandFooter ? createFooter({
          name: data.footerName,
          handle: data.footerHandle,
          height: 120,
        }) : null,
      ].filter(Boolean),
    },
  };
}

module.exports = infographicDense;
