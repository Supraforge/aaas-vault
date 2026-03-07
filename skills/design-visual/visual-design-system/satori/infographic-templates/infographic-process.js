/**
 * Infographic Process Template - Workflow/steps with visual flow
 *
 * Design Principles:
 * - Numbered steps with gradient badges
 * - Visual flow with connectors
 * - Icon support for each step
 * - Progress indication
 * - Clear hierarchy
 *
 * Data Structure:
 * {
 *   tag: "TREATMENT ALGORITHM",
 *   title: "Starting SGLT2 Inhibitors",
 *   subtitle: "Step-by-step guide for clinicians",
 *   steps: [
 *     { title: "Screen", description: "Confirm HFrEF diagnosis, check eGFR", icon: "magnify" },
 *     { title: "Initiate", description: "Start at recommended dose", icon: "pill" },
 *     { title: "Monitor", description: "Check creatinine at 1-2 weeks", icon: "chart-up" },
 *     { title: "Optimize", description: "Titrate based on response", icon: "target" }
 *   ],
 *   note: "eGFR ≥20 mL/min/1.73m² for most agents",
 *   showFooter: true
 * }
 */

const { BRAND, ICONS, GRADIENTS, createBlob, createTagBadge, createFooter } = require('./constants');

/**
 * Create a step card
 */
function createStep(step, index, total) {
  const icon = ICONS[step.icon] || step.icon || ICONS.target;
  const stepNumber = step.number || index + 1;
  const isLast = index === total - 1;

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        alignItems: 'flex-start',
        gap: '20px',
        position: 'relative',
      },
      children: [
        // Step number and connector
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
            },
            children: [
              // Number badge with gradient
              {
                type: 'div',
                props: {
                  style: {
                    width: '56px',
                    height: '56px',
                    borderRadius: '16px',
                    background: `linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.secondary} 100%)`,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    boxShadow: '0 8px 24px rgba(22, 105, 122, 0.2)',
                  },
                  children: {
                    type: 'div',
                    props: {
                      style: {
                        fontSize: '26px',
                        fontWeight: 900,
                        color: BRAND.white,
                      },
                      children: String(stepNumber),
                    },
                  },
                },
              },
              // Connector line
              !isLast ? {
                type: 'div',
                props: {
                  style: {
                    width: '4px',
                    height: '80px',
                    background: `linear-gradient(180deg, ${BRAND.primary} 0%, ${BRAND.backgroundWash} 100%)`,
                    borderRadius: '2px',
                    marginTop: '8px',
                  },
                },
              } : null,
            ].filter(Boolean),
          },
        },

        // Step content card
        {
          type: 'div',
          props: {
            style: {
              flex: 1,
              backgroundColor: BRAND.white,
              borderRadius: '20px',
              padding: '24px 28px',
              boxShadow: '0 6px 24px rgba(22, 105, 122, 0.08)',
              border: `1px solid ${BRAND.backgroundWash}`,
              display: 'flex',
              gap: '18px',
              alignItems: 'flex-start',
            },
            children: [
              // Icon container
              {
                type: 'div',
                props: {
                  style: {
                    width: '52px',
                    height: '52px',
                    borderRadius: '14px',
                    backgroundColor: 'rgba(22, 105, 122, 0.08)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    flexShrink: 0,
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

              // Text content
              {
                type: 'div',
                props: {
                  style: {
                    flex: 1,
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '6px',
                  },
                  children: [
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '24px',
                          fontWeight: 700,
                          color: BRAND.primary,
                        },
                        children: step.title || `Step ${stepNumber}`,
                      },
                    },
                    step.description ? {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '18px',
                          color: BRAND.textSecondary,
                          lineHeight: 1.4,
                        },
                        children: step.description,
                      },
                    } : null,
                  ].filter(Boolean),
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
 * Generate the infographic process template
 */
function infographicProcess(data, helpers = {}) {
  const steps = data.steps || [];
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
              padding: '48px 60px 32px',
              position: 'relative',
            },
            children: [
              // Header
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    marginBottom: '36px',
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
                          lineHeight: 1.1,
                          marginTop: data.tag ? '16px' : '0',
                          letterSpacing: '-1px',
                        },
                        children: data.title || 'Process Flow',
                      },
                    },
                    data.subtitle ? {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '22px',
                          fontWeight: 300,
                          color: BRAND.textSecondary,
                          marginTop: '8px',
                        },
                        children: data.subtitle,
                      },
                    } : null,
                  ].filter(Boolean),
                },
              },

              // Steps
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '8px',
                    flex: 1,
                  },
                  children: steps.slice(0, 5).map((step, i) => createStep(step, i, Math.min(steps.length, 5))),
                },
              },

              // Note
              data.note ? {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    marginTop: '24px',
                    padding: '16px 24px',
                    backgroundColor: 'rgba(22, 105, 122, 0.06)',
                    borderRadius: '14px',
                    borderLeft: `4px solid ${BRAND.secondary}`,
                  },
                  children: {
                    type: 'div',
                    props: {
                      style: {
                        fontSize: '17px',
                        color: BRAND.textSecondary,
                        fontStyle: 'italic',
                      },
                      children: data.note,
                    },
                  },
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

module.exports = infographicProcess;
