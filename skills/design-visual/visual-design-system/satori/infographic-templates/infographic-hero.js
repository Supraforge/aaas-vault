/**
 * Infographic Hero Template - Single key stat with maximum visual impact
 *
 * Design Principles:
 * - Mesh gradient background for depth
 * - Huge stat in gradient badge (120px, 900 weight)
 * - Icon container with styled background
 * - Extreme font weight contrast (900 vs 300)
 * - Supporting context and source
 * - Branded footer
 *
 * Data Structure:
 * {
 *   stat: "26%",
 *   label: "Mortality Reduction",
 *   context: "HR 0.74, 95% CI 0.65-0.85",
 *   source: "PARADIGM-HF Trial",
 *   icon: "chart-down" | "heart" | "pill" | emoji,
 *   theme: "primary" | "success" | "accent" | "dark",
 *   tag: "CLINICAL TRIAL",
 *   showFooter: true,
 *   footerName: "Dr. Shailesh Singh",
 *   footerHandle: "@heartdocshailesh"
 * }
 */

const { BRAND, ICONS, GRADIENTS, createBlob, createFooter, createTagBadge } = require('./constants');

// Theme configurations
const THEMES = {
  primary: {
    background: GRADIENTS.lightMesh,
    statGradient: GRADIENTS.statPrimary,
    labelColor: BRAND.neutralDark,
    contextColor: BRAND.secondary,
    tagColor: BRAND.secondary,
    blobColor: 'rgba(22, 105, 122, 0.04)',
    iconBg: 'rgba(22, 105, 122, 0.1)',
    dark: false,
  },
  success: {
    background: `
      radial-gradient(ellipse at 27% 37%, rgba(39, 174, 96, 0.08) 0%, transparent 50%),
      radial-gradient(ellipse at 97% 21%, rgba(46, 204, 113, 0.06) 0%, transparent 50%),
      linear-gradient(180deg, #E8F8F0 0%, ${BRAND.white} 60%, #E8F8F0 100%)
    `,
    statGradient: GRADIENTS.statSuccess,
    labelColor: BRAND.neutralDark,
    contextColor: BRAND.success,
    tagColor: BRAND.success,
    blobColor: 'rgba(39, 174, 96, 0.04)',
    iconBg: 'rgba(39, 174, 96, 0.12)',
    dark: false,
  },
  accent: {
    background: `
      radial-gradient(ellipse at 27% 37%, rgba(239, 83, 80, 0.08) 0%, transparent 50%),
      radial-gradient(ellipse at 97% 21%, rgba(255, 107, 107, 0.06) 0%, transparent 50%),
      linear-gradient(180deg, #FFF3F2 0%, ${BRAND.white} 60%, #FFF3F2 100%)
    `,
    statGradient: GRADIENTS.statAccent,
    labelColor: BRAND.neutralDark,
    contextColor: BRAND.accent,
    tagColor: BRAND.accent,
    blobColor: 'rgba(239, 83, 80, 0.04)',
    iconBg: 'rgba(239, 83, 80, 0.12)',
    dark: false,
  },
  dark: {
    background: GRADIENTS.primaryMesh,
    statGradient: 'rgba(255, 255, 255, 0.15)',
    labelColor: 'rgba(255, 255, 255, 0.95)',
    contextColor: 'rgba(255, 255, 255, 0.8)',
    tagColor: BRAND.backgroundWash,
    blobColor: 'rgba(255, 255, 255, 0.03)',
    iconBg: 'rgba(255, 255, 255, 0.15)',
    dark: true,
  },
};

/**
 * Generate the infographic hero template
 */
function infographicHero(data, helpers = {}) {
  const theme = THEMES[data.theme] || THEMES.primary;
  const icon = ICONS[data.icon] || data.icon || ICONS['chart-up'];
  const showFooter = data.showFooter !== false;

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
        // Decorative blobs for depth
        createBlob({ top: '-150px', right: '-150px', size: '500px', color: theme.blobColor }),
        createBlob({ bottom: '-200px', left: '-200px', size: '600px', color: theme.blobColor }),
        createBlob({ top: '40%', right: '-100px', size: '300px', color: theme.blobColor }),

        // Main content area
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
              // Tag badge
              data.tag ? createTagBadge(data.tag, { color: theme.tagColor }) : null,

              // Icon container
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    width: '120px',
                    height: '120px',
                    borderRadius: '30px',
                    backgroundColor: theme.iconBg,
                    marginTop: data.tag ? '16px' : '0',
                  },
                  children: {
                    type: 'div',
                    props: {
                      style: {
                        fontSize: '64px',
                        lineHeight: 1,
                      },
                      children: icon,
                    },
                  },
                },
              },

              // Stat badge (the hero element)
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    background: theme.statGradient,
                    padding: '48px 80px',
                    borderRadius: '32px',
                    boxShadow: theme.dark ? 'none' : '0 24px 64px rgba(22, 105, 122, 0.18)',
                    marginTop: '16px',
                  },
                  children: {
                    type: 'div',
                    props: {
                      style: {
                        fontSize: '120px',
                        fontWeight: 900,
                        color: BRAND.white,
                        lineHeight: 1,
                        letterSpacing: '-4px',
                      },
                      children: data.stat || '—',
                    },
                  },
                },
              },

              // Label (bold, 40px)
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '44px',
                    fontWeight: 700,
                    color: theme.labelColor,
                    textAlign: 'center',
                    lineHeight: 1.2,
                    maxWidth: '800px',
                    marginTop: '8px',
                  },
                  children: data.label || 'Key Metric',
                },
              },

              // Context (HR, CI, etc.)
              data.context ? {
                type: 'div',
                props: {
                  style: {
                    fontSize: '26px',
                    fontWeight: 500,
                    color: theme.contextColor,
                    textAlign: 'center',
                    fontStyle: 'italic',
                    padding: '14px 28px',
                    backgroundColor: theme.dark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(22, 105, 122, 0.08)',
                    borderRadius: '14px',
                    marginTop: '4px',
                  },
                  children: data.context,
                },
              } : null,

              // Source
              data.source ? {
                type: 'div',
                props: {
                  style: {
                    fontSize: '20px',
                    fontWeight: 400,
                    color: theme.dark ? 'rgba(255, 255, 255, 0.6)' : BRAND.textMuted,
                    marginTop: '12px',
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
          dark: theme.dark,
        }) : null,
      ].filter(Boolean),
    },
  };
}

module.exports = infographicHero;
module.exports.THEMES = THEMES;
