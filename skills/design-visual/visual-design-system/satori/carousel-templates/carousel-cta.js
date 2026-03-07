/**
 * Carousel CTA Template - Call-to-action with personality
 *
 * Design Principles:
 * - Profile photo (circular, prominent)
 * - Name and credentials
 * - Value proposition text
 * - Handle with accent color
 * - Social proof (follower count, optional)
 * - Background: brand gradient
 *
 * Data Structure:
 * {
 *   name: "Dr. Shailesh Singh",
 *   credentials: "Cardiologist | Evidence-Based Medicine",
 *   handle: "@heartdocshailesh",
 *   valueProposition: "Follow for myth-busting cardiology content",
 *   followerCount: "50K+",
 *   ctaText: "Follow for more",
 *   photoPath: "/path/to/photo.jpg",  // Optional - will show initial if not provided
 *   theme: "dark" | "light" | "accent"
 * }
 */

// Brand colors
const BRAND = {
  primary: '#16697A',
  primaryLight: '#1E8A9F',
  secondary: '#218380',
  accent: '#EF5350',
  accentDark: '#D32F2F',
  success: '#27AE60',
  backgroundWash: '#E8F5F4',
  neutralLight: '#F9FAFB',
  neutralDark: '#2F3E46',
  white: '#FFFFFF',
};

// Theme configurations with mesh gradients
const THEMES = {
  dark: {
    background: `radial-gradient(ellipse at 20% 30%, rgba(33, 131, 128, 0.4) 0%, transparent 50%),
                 radial-gradient(ellipse at 80% 70%, rgba(22, 105, 122, 0.3) 0%, transparent 50%),
                 linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.secondary} 100%)`,
    nameColor: BRAND.white,
    credentialsColor: 'rgba(255, 255, 255, 0.85)',
    handleColor: BRAND.backgroundWash,
    valueColor: BRAND.white,
    ctaBg: BRAND.white,
    ctaColor: BRAND.primary,
    photoBorder: BRAND.white,
    followerBg: 'rgba(255, 255, 255, 0.15)',
    followerColor: BRAND.white,
  },
  light: {
    background: `radial-gradient(ellipse at 20% 30%, rgba(22, 105, 122, 0.08) 0%, transparent 50%),
                 radial-gradient(ellipse at 80% 70%, rgba(33, 131, 128, 0.05) 0%, transparent 50%),
                 linear-gradient(180deg, ${BRAND.backgroundWash} 0%, ${BRAND.white} 100%)`,
    nameColor: BRAND.primary,
    credentialsColor: BRAND.neutralDark,
    handleColor: BRAND.secondary,
    valueColor: BRAND.neutralDark,
    ctaBg: BRAND.primary,
    ctaColor: BRAND.white,
    photoBorder: BRAND.primary,
    followerBg: 'rgba(22, 105, 122, 0.1)',
    followerColor: BRAND.primary,
  },
  accent: {
    background: `radial-gradient(ellipse at 20% 30%, rgba(239, 83, 80, 0.3) 0%, transparent 50%),
                 radial-gradient(ellipse at 80% 70%, rgba(211, 47, 47, 0.2) 0%, transparent 50%),
                 linear-gradient(135deg, ${BRAND.accent} 0%, ${BRAND.accentDark} 100%)`,
    nameColor: BRAND.white,
    credentialsColor: 'rgba(255, 255, 255, 0.9)',
    handleColor: BRAND.white,
    valueColor: BRAND.white,
    ctaBg: BRAND.white,
    ctaColor: BRAND.accent,
    photoBorder: BRAND.white,
    followerBg: 'rgba(255, 255, 255, 0.2)',
    followerColor: BRAND.white,
  },
};

/**
 * Generate the carousel CTA template
 *
 * @param {Object} data - Template data
 * @param {Object} helpers - Helper functions from renderer
 * @returns {Object} - Satori-compatible JSX object
 */
function carouselCta(data, helpers = {}) {
  const theme = THEMES[data.theme] || THEMES.dark;
  const showFollowerCount = data.followerCount && data.followerCount.length > 0;
  const ctaText = data.ctaText || 'Follow for more';
  const initial = (data.name || 'Dr. S').split(' ').map(n => n.charAt(0)).join('').toUpperCase().slice(0, 2);

  return {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        width: '100%',
        height: '100%',
        background: theme.background,
        padding: '80px',
        fontFamily: 'Helvetica, Arial, sans-serif',
        position: 'relative',
        overflow: 'hidden',
      },
      children: [
        // Background decorative elements
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '-150px',
              right: '-150px',
              width: '500px',
              height: '500px',
              borderRadius: '50%',
              background: 'rgba(255, 255, 255, 0.03)',
            },
          },
        },
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              bottom: '-200px',
              left: '-200px',
              width: '600px',
              height: '600px',
              borderRadius: '50%',
              background: 'rgba(255, 255, 255, 0.02)',
            },
          },
        },

        // Profile photo container
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              width: '200px',
              height: '200px',
              borderRadius: '50%',
              border: `6px solid ${theme.photoBorder}`,
              backgroundColor: theme.ctaBg,
              marginBottom: '40px',
              boxShadow: '0 20px 60px rgba(0, 0, 0, 0.15)',
            },
            children: {
              type: 'div',
              props: {
                style: {
                  fontSize: '72px',
                  fontWeight: 700,
                  color: theme.ctaColor,
                  lineHeight: 1,
                },
                children: initial,
              },
            },
          },
        },

        // Name
        {
          type: 'div',
          props: {
            style: {
              fontSize: '48px',
              fontWeight: 700,
              color: theme.nameColor,
              textAlign: 'center',
              lineHeight: 1.2,
              marginBottom: '12px',
            },
            children: data.name || 'Dr. Shailesh Singh',
          },
        },

        // Credentials
        {
          type: 'div',
          props: {
            style: {
              fontSize: '24px',
              fontWeight: 400,
              color: theme.credentialsColor,
              textAlign: 'center',
              lineHeight: 1.4,
              marginBottom: '24px',
              letterSpacing: '1px',
            },
            children: data.credentials || 'Cardiologist | Evidence-Based Medicine',
          },
        },

        // Handle
        {
          type: 'div',
          props: {
            style: {
              fontSize: '28px',
              fontWeight: 600,
              color: theme.handleColor,
              textAlign: 'center',
              marginBottom: '40px',
              padding: '12px 28px',
              backgroundColor: 'rgba(255, 255, 255, 0.1)',
              borderRadius: '30px',
            },
            children: data.handle || '@heartdocshailesh',
          },
        },

        // Value proposition
        {
          type: 'div',
          props: {
            style: {
              fontSize: '32px',
              fontWeight: 500,
              color: theme.valueColor,
              textAlign: 'center',
              lineHeight: 1.4,
              maxWidth: '800px',
              marginBottom: '48px',
            },
            children: data.valueProposition || 'Follow for myth-busting cardiology content',
          },
        },

        // CTA Button
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '16px',
              backgroundColor: theme.ctaBg,
              color: theme.ctaColor,
              fontSize: '28px',
              fontWeight: 700,
              padding: '24px 56px',
              borderRadius: '40px',
              boxShadow: '0 8px 30px rgba(0, 0, 0, 0.15)',
            },
            children: [
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '28px',
                  },
                  children: ctaText,
                },
              },
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '24px',
                  },
                  children: '\u{1F449}', // 👉
                },
              },
            ],
          },
        },

        // Follower count (optional)
        showFollowerCount ? {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              bottom: '60px',
              display: 'flex',
              alignItems: 'center',
              gap: '12px',
              backgroundColor: theme.followerBg,
              color: theme.followerColor,
              fontSize: '20px',
              fontWeight: 500,
              padding: '12px 24px',
              borderRadius: '25px',
            },
            children: [
              {
                type: 'div',
                props: {
                  style: {
                    fontSize: '20px',
                  },
                  children: '\u{1F465}', // 👥
                },
              },
              {
                type: 'div',
                props: {
                  children: `${data.followerCount} followers`,
                },
              },
            ],
          },
        } : null,
      ].filter(Boolean),
    },
  };
}

module.exports = carouselCta;
module.exports.BRAND = BRAND;
module.exports.THEMES = THEMES;
