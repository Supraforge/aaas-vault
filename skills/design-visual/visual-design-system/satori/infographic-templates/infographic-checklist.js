/**
 * Infographic Checklist Template - Patient guide with styled checklist
 *
 * Design Principles:
 * - Clean checklist format
 * - Checkbox icons (filled/empty)
 * - Category grouping
 * - Subtle visual hierarchy
 * - Patient-friendly design
 *
 * Data Structure:
 * {
 *   tag: "PATIENT CHECKLIST",
 *   title: "Before Your Stress Test",
 *   subtitle: "Complete preparation guide",
 *   icon: "heart",
 *   categories: [
 *     {
 *       title: "24 Hours Before",
 *       items: [
 *         { text: "Avoid caffeine (coffee, tea, chocolate)", checked: false },
 *         { text: "Continue medications unless told otherwise", checked: false }
 *       ]
 *     },
 *     {
 *       title: "Day of Test",
 *       items: [
 *         { text: "Wear comfortable walking shoes", checked: false },
 *         { text: "Bring medication list", checked: false }
 *       ]
 *     }
 *   ],
 *   callout: { icon: "warning", text: "Tell staff if you have chest pain" },
 *   showFooter: true
 * }
 */

const { BRAND, ICONS, GRADIENTS, createBlob, createTagBadge, createFooter } = require('./constants');

/**
 * Create a checklist item
 */
function createChecklistItem(item) {
  const isChecked = item.checked === true;

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        alignItems: 'flex-start',
        gap: '14px',
        padding: '10px 0',
      },
      children: [
        // Checkbox
        {
          type: 'div',
          props: {
            style: {
              width: '28px',
              height: '28px',
              borderRadius: '8px',
              border: isChecked ? 'none' : `3px solid ${BRAND.primary}`,
              backgroundColor: isChecked ? BRAND.success : 'transparent',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              flexShrink: 0,
              marginTop: '2px',
            },
            children: isChecked ? {
              type: 'div',
              props: {
                style: {
                  fontSize: '18px',
                  color: BRAND.white,
                  lineHeight: 1,
                },
                children: '\u{2713}', // ✓
              },
            } : null,
          },
        },
        // Text
        {
          type: 'div',
          props: {
            style: {
              fontSize: '20px',
              color: BRAND.textPrimary,
              lineHeight: 1.4,
              textDecoration: isChecked ? 'line-through' : 'none',
              opacity: isChecked ? 0.7 : 1,
            },
            children: item.text || '',
          },
        },
      ],
    },
  };
}

/**
 * Create a category section
 */
function createCategory(category, index) {
  return {
    type: 'div',
    props: {
      style: {
        backgroundColor: BRAND.white,
        borderRadius: '20px',
        padding: '24px 28px',
        boxShadow: '0 6px 24px rgba(22, 105, 122, 0.08)',
        border: `1px solid ${BRAND.backgroundWash}`,
        display: 'flex',
        flexDirection: 'column',
      },
      children: [
        // Category title
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              alignItems: 'center',
              gap: '12px',
              marginBottom: '12px',
              paddingBottom: '12px',
              borderBottom: `2px solid ${BRAND.backgroundWash}`,
            },
            children: [
              // Number badge
              {
                type: 'div',
                props: {
                  style: {
                    width: '32px',
                    height: '32px',
                    borderRadius: '10px',
                    background: `linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.secondary} 100%)`,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                  },
                  children: {
                    type: 'div',
                    props: {
                      style: {
                        fontSize: '16px',
                        fontWeight: 700,
                        color: BRAND.white,
                      },
                      children: String(index + 1),
                    },
                  },
                },
              },
              // Title
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '22px',
                    fontWeight: 700,
                    color: BRAND.primary,
                  },
                  children: category.title || `Section ${index + 1}`,
                },
              },
            ],
          },
        },
        // Items
        ...(category.items || []).map(item => createChecklistItem(item)),
      ],
    },
  };
}

/**
 * Generate the infographic checklist template
 */
function infographicChecklist(data, helpers = {}) {
  const categories = data.categories || [];
  const showFooter = data.showFooter !== false;
  const headerIcon = ICONS[data.icon] || data.icon || ICONS.check;

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
        createBlob({ top: '-100px', right: '-100px', size: '350px', color: 'rgba(22, 105, 122, 0.05)' }),
        createBlob({ bottom: '-150px', left: '-150px', size: '400px', color: 'rgba(39, 174, 96, 0.04)' }),

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
                    marginBottom: '28px',
                  },
                  children: [
                    data.tag ? createTagBadge(data.tag) : null,

                    // Title row with icon
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
                          // Icon
                          {
                            type: 'div',
                            props: {
                              style: {
                                width: '72px',
                                height: '72px',
                                borderRadius: '20px',
                                background: `linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.secondary} 100%)`,
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                boxShadow: '0 8px 24px rgba(22, 105, 122, 0.2)',
                              },
                              children: {
                                type: 'div',
                                props: {
                                  style: { fontSize: '40px', lineHeight: 1 },
                                  children: headerIcon,
                                },
                              },
                            },
                          },
                          // Title
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
                                      fontSize: '44px',
                                      fontWeight: 900,
                                      color: BRAND.primary,
                                      lineHeight: 1.1,
                                      letterSpacing: '-1px',
                                    },
                                    children: data.title || 'Checklist',
                                  },
                                },
                                data.subtitle ? {
                                  type: 'div',
                                  props: {
                                    style: {
                                      fontSize: '20px',
                                      fontWeight: 300,
                                      color: BRAND.textSecondary,
                                    },
                                    children: data.subtitle,
                                  },
                                } : null,
                              ].filter(Boolean),
                            },
                          },
                        ],
                      },
                    },
                  ].filter(Boolean),
                },
              },

              // Categories
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '20px',
                    flex: 1,
                  },
                  children: categories.slice(0, 3).map((cat, i) => createCategory(cat, i)),
                },
              },

              // Callout
              data.callout ? {
                type: 'div',
                props: {
                  style: {
                    marginTop: '24px',
                    padding: '20px 28px',
                    background: `linear-gradient(135deg, ${BRAND.accent} 0%, ${BRAND.accentDark} 100%)`,
                    borderRadius: '16px',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '16px',
                    boxShadow: '0 8px 24px rgba(239, 83, 80, 0.2)',
                  },
                  children: [
                    // Icon
                    {
                      type: 'div',
                      props: {
                        style: {
                          width: '48px',
                          height: '48px',
                          borderRadius: '12px',
                          backgroundColor: 'rgba(255, 255, 255, 0.2)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                        },
                        children: {
                          type: 'div',
                          props: {
                            style: { fontSize: '28px', lineHeight: 1 },
                            children: ICONS[data.callout.icon] || ICONS.warning,
                          },
                        },
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
                        },
                        children: data.callout.text || '',
                      },
                    },
                  ],
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

module.exports = infographicChecklist;
