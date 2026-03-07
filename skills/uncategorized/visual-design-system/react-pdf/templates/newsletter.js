/**
 * Newsletter Template - B2C Patient Newsletter
 *
 * Eric Topol / Ground Truths style newsletter for patients.
 * Features: Clear headlines, stat boxes, key takeaways, citations.
 */

const React = require('react');
const { Document, Page, Text, View, StyleSheet, Image, Link } = require('@react-pdf/renderer');

function Newsletter({ data, styles, getColor }) {
  const {
    title = 'Heart Health Update',
    subtitle = 'Evidence-based insights for better cardiovascular health',
    date = new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }),
    author = 'Dr. Shailesh Singh',
    authorCredentials = 'Cardiologist',
    sections = [],
    keyTakeaways = [],
    stats = [],
    footer = {},
  } = data;

  const localStyles = StyleSheet.create({
    header: {
      marginBottom: 24,
      borderBottomWidth: 2,
      borderBottomColor: getColor('primary.teal'),
      paddingBottom: 16,
    },
    authorLine: {
      fontSize: 10,
      color: getColor('semantic.neutral'),
      marginTop: 8,
    },
    statsContainer: {
      flexDirection: 'row',
      gap: 16,
      marginBottom: 24,
    },
    statBox: {
      flex: 1,
      backgroundColor: '#f8f9fa',
      padding: 16,
      borderRadius: 4,
      borderLeftWidth: 4,
      borderLeftColor: getColor('primary.teal'),
    },
    takeawayBox: {
      backgroundColor: '#f0fdf4',
      padding: 16,
      borderRadius: 4,
      marginBottom: 16,
      borderLeftWidth: 4,
      borderLeftColor: getColor('semantic.success'),
    },
    takeawayTitle: {
      fontSize: 12,
      fontWeight: 'bold',
      color: getColor('semantic.success'),
      marginBottom: 8,
      fontFamily: 'Helvetica-Bold',
    },
    takeawayItem: {
      fontSize: 10,
      marginBottom: 4,
      paddingLeft: 12,
    },
    bullet: {
      position: 'absolute',
      left: 0,
    },
    sectionContent: {
      fontSize: 10,
      lineHeight: 1.6,
      textAlign: 'justify',
      marginBottom: 12,
    },
    citation: {
      fontSize: 8,
      color: getColor('semantic.neutral'),
      fontStyle: 'italic',
      marginTop: 4,
    },
  });

  return (
    <Document>
      <Page size="LETTER" style={styles.page}>
        {/* Header */}
        <View style={localStyles.header}>
          <Text style={styles.title}>{title}</Text>
          <Text style={styles.subtitle}>{subtitle}</Text>
          <Text style={localStyles.authorLine}>
            {author}, {authorCredentials} | {date}
          </Text>
        </View>

        {/* Stats Row */}
        {stats.length > 0 && (
          <View style={localStyles.statsContainer}>
            {stats.slice(0, 3).map((stat, index) => (
              <View key={index} style={localStyles.statBox}>
                <Text style={styles.statValue}>{stat.value}</Text>
                <Text style={styles.statLabel}>{stat.label}</Text>
                {stat.context && (
                  <Text style={localStyles.citation}>{stat.context}</Text>
                )}
              </View>
            ))}
          </View>
        )}

        {/* Key Takeaways */}
        {keyTakeaways.length > 0 && (
          <View style={localStyles.takeawayBox}>
            <Text style={localStyles.takeawayTitle}>Key Takeaways</Text>
            {keyTakeaways.map((takeaway, index) => (
              <View key={index} style={{ flexDirection: 'row', marginBottom: 6 }}>
                <Text style={localStyles.bullet}>•</Text>
                <Text style={localStyles.takeawayItem}>{takeaway}</Text>
              </View>
            ))}
          </View>
        )}

        {/* Sections */}
        {sections.map((section, index) => (
          <View key={index} wrap={false}>
            <Text style={styles.sectionHeader}>{section.title}</Text>
            {section.content && (
              <Text style={localStyles.sectionContent}>{section.content}</Text>
            )}
            {section.subsections && section.subsections.map((sub, subIndex) => (
              <View key={subIndex}>
                <Text style={styles.subsectionHeader}>{sub.title}</Text>
                <Text style={localStyles.sectionContent}>{sub.content}</Text>
              </View>
            ))}
            {section.citation && (
              <Text style={localStyles.citation}>Source: {section.citation}</Text>
            )}
          </View>
        ))}

        {/* Footer */}
        <View style={styles.footer} fixed>
          <Text>{footer.left || `© ${new Date().getFullYear()} ${author}`}</Text>
          <Text style={styles.pageNumber} render={({ pageNumber, totalPages }) =>
            `Page ${pageNumber} of ${totalPages}`
          } />
          <Text>{footer.right || 'For educational purposes only'}</Text>
        </View>
      </Page>
    </Document>
  );
}

module.exports = Newsletter;
