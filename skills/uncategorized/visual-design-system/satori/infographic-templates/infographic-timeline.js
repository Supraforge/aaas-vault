/**
 * Infographic Timeline Template
 *
 * Displays a vertical timeline with events/milestones.
 * Perfect for patient journeys, treatment progressions, clinical trial phases.
 *
 * Data schema:
 * {
 *   title: "Treatment Timeline",
 *   subtitle: "Expected progression over 12 months",
 *   events: [
 *     { time: "Day 0", title: "Start Treatment", description: "Initial dose" },
 *     { time: "Week 2", title: "First Assessment", description: "Check tolerability" },
 *     { time: "Month 3", title: "Dose Adjustment", description: "Titrate to target" },
 *   ],
 *   showFooter: true,
 *   footerName: "Dr. Shailesh Singh",
 *   footerHandle: "@heartdocshailesh"
 * }
 */

const { BRAND, GRADIENTS, createBlob, createFooter, createTagBadge } = require('./constants');

function infographicTimeline(data = {}) {
  const {
    title = 'Timeline',
    subtitle = '',
    events = [],
    showFooter = true,
  } = data;

  // Limit to 5 events
  const displayEvents = events.slice(0, 5);

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
        createBlob({ top: '-100px', right: '-100px', size: '400px', color: 'rgba(22, 105, 122, 0.04)' }),
        createBlob({ bottom: '-150px', left: '-100px', size: '350px', color: 'rgba(39, 174, 96, 0.03)' }),

        // Header
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              padding: '60px 60px 40px',
              gap: '16px',
            },
            children: [
              // Tag
              createTagBadge('TIMELINE', { color: BRAND.secondary }),
              // Title
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '48px',
                    fontWeight: 900,
                    color: BRAND.textPrimary,
                    textAlign: 'center',
                    lineHeight: 1.1,
                    letterSpacing: '-2px',
                  },
                  children: title,
                },
              },
              // Subtitle
              subtitle ? {
                type: 'div',
                props: {
                  style: {
                    fontSize: '22px',
                    fontWeight: 400,
                    color: BRAND.textSecondary,
                    textAlign: 'center',
                  },
                  children: subtitle,
                },
              } : null,
            ].filter(Boolean),
          },
        },

        // Events container
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flexDirection: 'column',
              flex: 1,
              padding: '20px 60px',
              gap: '16px',
            },
            children: displayEvents.map((event, index) => {
              const isLast = index === displayEvents.length - 1;
              const stepNumber = index + 1;

              return {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    alignItems: 'center',
                    gap: '20px',
                  },
                  children: [
                    // Step number circle
                    {
                      type: 'div',
                      props: {
                        style: {
                          width: '48px',
                          height: '48px',
                          borderRadius: '50%',
                          backgroundColor: isLast ? BRAND.success : BRAND.primary,
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          flexShrink: 0,
                        },
                        children: {
                          type: 'div',
                          props: {
                            style: {
                              fontSize: '20px',
                              fontWeight: 700,
                              color: BRAND.white,
                            },
                            children: String(stepNumber),
                          },
                        },
                      },
                    },
                    // Time label
                    {
                      type: 'div',
                      props: {
                        style: {
                          width: '100px',
                          fontSize: '16px',
                          fontWeight: 700,
                          color: BRAND.primary,
                          flexShrink: 0,
                        },
                        children: event.time || `Step ${stepNumber}`,
                      },
                    },
                    // Event card
                    {
                      type: 'div',
                      props: {
                        style: {
                          flex: 1,
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '4px',
                          backgroundColor: BRAND.white,
                          padding: '20px 24px',
                          borderRadius: '16px',
                          boxShadow: '0 8px 32px rgba(22, 105, 122, 0.08)',
                          border: `1px solid ${BRAND.backgroundWash}`,
                        },
                        children: [
                          {
                            type: 'div',
                            props: {
                              style: {
                                fontSize: '22px',
                                fontWeight: 700,
                                color: BRAND.textPrimary,
                              },
                              children: event.title || 'Event',
                            },
                          },
                          event.description ? {
                            type: 'div',
                            props: {
                              style: {
                                fontSize: '16px',
                                fontWeight: 400,
                                color: BRAND.textSecondary,
                              },
                              children: event.description,
                            },
                          } : null,
                        ].filter(Boolean),
                      },
                    },
                  ],
                },
              };
            }),
          },
        },

        // Footer
        showFooter ? createFooter({
          name: data.footerName,
          handle: data.footerHandle,
          dark: false,
        }) : null,
      ].filter(Boolean),
    },
  };
}

module.exports = infographicTimeline;
