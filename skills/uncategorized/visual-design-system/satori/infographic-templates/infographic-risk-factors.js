/**
 * Infographic Risk Factors Template
 *
 * Displays risk factors with visual bars showing relative impact.
 * Perfect for cardiovascular risk, diabetes risk, lifestyle factors.
 *
 * Data schema:
 * {
 *   title: "Cardiovascular Risk Factors",
 *   subtitle: "Modifiable and non-modifiable factors",
 *   factors: [
 *     { name: "Smoking", risk: 85, color: "danger" },
 *     { name: "Hypertension", risk: 75, color: "danger" },
 *     { name: "Diabetes", risk: 65, color: "warning" },
 *     { name: "Obesity", risk: 55, color: "warning" },
 *     { name: "Sedentary lifestyle", risk: 45, color: "accent" },
 *   ],
 *   showFooter: true,
 *   footerName: "Dr. Shailesh Singh",
 *   footerHandle: "@heartdocshailesh"
 * }
 */

const { BRAND, GRADIENTS, createBlob, createFooter, createTagBadge, hexToRgba } = require('./constants');

// Extended color map for risk visualization
const COLOR_MAP = {
  danger: { bg: '#DC2626', light: '#EF4444' },
  warning: { bg: '#F59E0B', light: '#FBBF24' },
  accent: { bg: BRAND.accent, light: '#FF8A80' },
  primary: { bg: BRAND.primary, light: BRAND.primaryLight },
  success: { bg: BRAND.success, light: BRAND.successLight },
};

function infographicRiskFactors(data = {}) {
  const {
    title = 'Risk Factors',
    subtitle = '',
    factors = [],
    showFooter = true,
  } = data;

  // Limit to 6 factors
  const displayFactors = factors.slice(0, 6);

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
        createBlob({ bottom: '-100px', left: '-100px', size: '300px', color: 'rgba(220, 38, 38, 0.03)' }),

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
              createTagBadge('RISK ASSESSMENT', { color: BRAND.secondary }),
              // Title
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '46px',
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

        // Risk factors list
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
            children: displayFactors.map((factor) => {
              const colorScheme = COLOR_MAP[factor.color] || COLOR_MAP.primary;
              const riskValue = Math.min(100, Math.max(0, factor.risk || 50));

              return {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '8px',
                    backgroundColor: BRAND.white,
                    padding: '20px 24px',
                    borderRadius: '16px',
                    boxShadow: '0 8px 32px rgba(22, 105, 122, 0.08)',
                    border: `1px solid ${BRAND.backgroundWash}`,
                  },
                  children: [
                    // Name and percentage row
                    {
                      type: 'div',
                      props: {
                        style: {
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center',
                        },
                        children: [
                          {
                            type: 'div',
                            props: {
                              style: {
                                fontSize: '22px',
                                fontWeight: 600,
                                color: BRAND.textPrimary,
                              },
                              children: factor.name || 'Risk Factor',
                            },
                          },
                          {
                            type: 'div',
                            props: {
                              style: {
                                fontSize: '24px',
                                fontWeight: 800,
                                color: colorScheme.bg,
                              },
                              children: `${riskValue}%`,
                            },
                          },
                        ],
                      },
                    },
                    // Progress bar track
                    {
                      type: 'div',
                      props: {
                        style: {
                          display: 'flex',
                          width: '100%',
                          height: '14px',
                          backgroundColor: hexToRgba(colorScheme.bg, 0.15),
                          borderRadius: '7px',
                          overflow: 'hidden',
                        },
                        children: {
                          type: 'div',
                          props: {
                            style: {
                              width: `${riskValue}%`,
                              height: '100%',
                              background: `linear-gradient(90deg, ${colorScheme.bg} 0%, ${colorScheme.light} 100%)`,
                              borderRadius: '7px',
                            },
                          },
                        },
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

module.exports = infographicRiskFactors;
