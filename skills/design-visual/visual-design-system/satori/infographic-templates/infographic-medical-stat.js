/**
 * Infographic Medical Stat Template
 *
 * Displays a key statistic with a medical SVG icon.
 * Uses the medical icon library for professional, scalable icons.
 *
 * Data schema:
 * {
 *   stat: "42%",
 *   label: "Risk Reduction",
 *   context: "HR 0.58, 95% CI 0.45-0.75",
 *   source: "DAPA-HF Trial",
 *   medicalIcon: "cardiology",  // From icon library: cardiology, diabetes, etc.
 *   tag: "CLINICAL TRIAL",
 *   theme: "primary" | "success" | "accent",
 *   showFooter: true,
 *   footerName: "Dr. Shailesh Singh",
 *   footerHandle: "@heartdocshailesh"
 * }
 */

const { BRAND, GRADIENTS, createBlob, createFooter, createTagBadge, createMedicalIcon } = require('./constants');

// Theme configurations
const THEMES = {
  primary: {
    background: GRADIENTS.lightMesh,
    statGradient: `linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.primaryLight} 100%)`,
    iconBg: 'rgba(22, 105, 122, 0.1)',
    iconColor: BRAND.primary,
    labelColor: BRAND.textPrimary,
    contextColor: BRAND.secondary,
    blobColor: 'rgba(22, 105, 122, 0.04)',
  },
  success: {
    background: `radial-gradient(ellipse at 27% 37%, rgba(39, 174, 96, 0.08) 0%, transparent 50%), linear-gradient(180deg, #E8F8F0 0%, ${BRAND.white} 60%, #E8F8F0 100%)`,
    statGradient: `linear-gradient(135deg, ${BRAND.success} 0%, ${BRAND.successLight} 100%)`,
    iconBg: 'rgba(39, 174, 96, 0.12)',
    iconColor: BRAND.success,
    labelColor: BRAND.textPrimary,
    contextColor: BRAND.success,
    blobColor: 'rgba(39, 174, 96, 0.04)',
  },
  accent: {
    background: `radial-gradient(ellipse at 27% 37%, rgba(239, 83, 80, 0.08) 0%, transparent 50%), linear-gradient(180deg, #FFF3F2 0%, ${BRAND.white} 60%, #FFF3F2 100%)`,
    statGradient: `linear-gradient(135deg, ${BRAND.accent} 0%, ${BRAND.accentDark} 100%)`,
    iconBg: 'rgba(239, 83, 80, 0.12)',
    iconColor: BRAND.accent,
    labelColor: BRAND.textPrimary,
    contextColor: BRAND.accent,
    blobColor: 'rgba(239, 83, 80, 0.04)',
  },
};

function infographicMedicalStat(data = {}) {
  const {
    stat = '—',
    label = 'Key Metric',
    context = '',
    source = '',
    medicalIcon = 'cardiology',
    tag = '',
    theme = 'primary',
    showFooter = true,
  } = data;

  const t = THEMES[theme] || THEMES.primary;

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        width: '100%',
        height: '100%',
        background: t.background,
        fontFamily: 'Helvetica, Arial, sans-serif',
        position: 'relative',
        overflow: 'hidden',
      },
      children: [
        // Decorative blobs
        createBlob({ top: '-150px', right: '-150px', size: '500px', color: t.blobColor }),
        createBlob({ bottom: '-200px', left: '-200px', size: '600px', color: t.blobColor }),

        // Main content
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
            },
            children: [
              // Tag
              tag ? createTagBadge(tag, { color: t.contextColor }) : null,

              // Medical SVG Icon
              createMedicalIcon(medicalIcon, {
                size: 120,
                backgroundColor: t.iconBg,
                borderRadius: 30,
                padding: 20,
                color: t.iconColor,
              }),

              // Stat badge
              {
                type: 'div',
                props: {
                  style: {
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    background: t.statGradient,
                    padding: '48px 80px',
                    borderRadius: '32px',
                    boxShadow: '0 24px 64px rgba(22, 105, 122, 0.18)',
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
                      children: stat,
                    },
                  },
                },
              },

              // Label
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '44px',
                    fontWeight: 700,
                    color: t.labelColor,
                    textAlign: 'center',
                    lineHeight: 1.2,
                    maxWidth: '800px',
                    marginTop: '8px',
                  },
                  children: label,
                },
              },

              // Context
              context ? {
                type: 'div',
                props: {
                  style: {
                    fontSize: '26px',
                    fontWeight: 500,
                    color: t.contextColor,
                    textAlign: 'center',
                    fontStyle: 'italic',
                    padding: '14px 28px',
                    backgroundColor: 'rgba(22, 105, 122, 0.08)',
                    borderRadius: '14px',
                    marginTop: '4px',
                  },
                  children: context,
                },
              } : null,

              // Source
              source ? {
                type: 'div',
                props: {
                  style: {
                    fontSize: '20px',
                    fontWeight: 400,
                    color: BRAND.textMuted,
                    marginTop: '12px',
                  },
                  children: `Source: ${source}`,
                },
              } : null,
            ].filter(Boolean),
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

module.exports = infographicMedicalStat;
