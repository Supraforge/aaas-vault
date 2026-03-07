/**
 * Infographic Quote Template
 *
 * Displays an impactful expert quote with attribution.
 * Perfect for thought leadership, guidelines, expert opinions.
 *
 * Data schema:
 * {
 *   quote: "The best time to start statin therapy is...",
 *   author: "Dr. John Smith",
 *   credentials: "ACC President, Harvard Medical School",
 *   source: "JACC 2024",
 *   icon: "stethoscope",
 *   showFooter: true,
 *   footerName: "Dr. Shailesh Singh",
 *   footerHandle: "@heartdocshailesh"
 * }
 */

const { BRAND, ICONS, createBlob, createFooter, createIconContainer } = require('./constants');

function infographicQuote(data = {}) {
  const {
    quote = 'Evidence-based medicine saves lives.',
    author = 'Expert Opinion',
    credentials = '',
    source = '',
    icon = 'stethoscope',
    showFooter = true,
  } = data;

  const resolvedIcon = ICONS[icon] || ICONS.stethoscope;

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        width: '100%',
        height: '100%',
        background: `linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.secondary} 100%)`,
        fontFamily: 'Helvetica, Arial, sans-serif',
        position: 'relative',
        overflow: 'hidden',
      },
      children: [
        // Decorative blobs
        createBlob({ top: '-150px', right: '-150px', size: '500px', color: 'rgba(255, 255, 255, 0.03)' }),
        createBlob({ bottom: '-100px', left: '-100px', size: '400px', color: 'rgba(255, 255, 255, 0.02)' }),

        // Main content container
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
              position: 'relative',
              zIndex: 1,
            },
            children: [
              // Tag
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    alignItems: 'center',
                    gap: '12px',
                  },
                  children: [
                    {
                      type: 'div',
                      props: {
                        style: {
                          width: '64px',
                          height: '6px',
                          backgroundColor: BRAND.white,
                          borderRadius: '999px',
                        },
                      },
                    },
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '14px',
                          letterSpacing: '2px',
                          fontWeight: 700,
                          color: BRAND.backgroundWash,
                          textTransform: 'uppercase',
                        },
                        children: 'EXPERT INSIGHT',
                      },
                    },
                  ],
                },
              },

              // Quote icon
              createIconContainer(icon, {
                size: 120,
                bgColor: 'rgba(255, 255, 255, 0.15)',
                borderRadius: 30,
                fontSize: 64,
              }),

              // Opening quote mark
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '100px',
                    fontWeight: 900,
                    color: 'rgba(255, 255, 255, 0.2)',
                    lineHeight: 1,
                    marginBottom: '-30px',
                  },
                  children: '"',
                },
              },

              // Quote text
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '38px',
                    fontWeight: 500,
                    color: BRAND.white,
                    textAlign: 'center',
                    lineHeight: 1.4,
                    maxWidth: '900px',
                    fontStyle: 'italic',
                  },
                  children: quote,
                },
              },

              // Closing quote mark
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '100px',
                    fontWeight: 900,
                    color: 'rgba(255, 255, 255, 0.2)',
                    lineHeight: 1,
                    marginTop: '-30px',
                  },
                  children: '"',
                },
              },

              // Author attribution
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    gap: '8px',
                    marginTop: '16px',
                  },
                  children: [
                    // Author name
                    {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '28px',
                          fontWeight: 700,
                          color: BRAND.white,
                        },
                        children: `— ${author}`,
                      },
                    },
                    // Credentials
                    credentials ? {
                      type: 'div',
                      props: {
                        style: {
                          fontSize: '20px',
                          fontWeight: 400,
                          color: BRAND.backgroundWash,
                        },
                        children: credentials,
                      },
                    } : null,
                    // Source
                    source ? {
                      type: 'div',
                      props: {
                        style: {
                          display: 'flex',
                          alignItems: 'center',
                          marginTop: '8px',
                          padding: '8px 20px',
                          backgroundColor: 'rgba(255, 255, 255, 0.1)',
                          borderRadius: '20px',
                        },
                        children: {
                          type: 'div',
                          props: {
                            style: {
                              fontSize: '16px',
                              fontWeight: 500,
                              color: BRAND.backgroundWash,
                            },
                            children: source,
                          },
                        },
                      },
                    } : null,
                  ].filter(Boolean),
                },
              },
            ].filter(Boolean),
          },
        },

        // Footer
        showFooter ? createFooter({
          name: data.footerName,
          handle: data.footerHandle,
          dark: true,
        }) : null,
      ].filter(Boolean),
    },
  };
}

module.exports = infographicQuote;
