/**
 * Editorial Template - JACC-Style Medical Editorial
 *
 * Publication-grade editorial format for medical professionals.
 * Features: Abstract, structured sections, references, author info.
 */

const React = require('react');
const { Document, Page, Text, View, StyleSheet, Link } = require('@react-pdf/renderer');

function Editorial({ data, styles, getColor }) {
  const {
    title = 'Untitled Editorial',
    authors = [{ name: 'Dr. Shailesh Singh', affiliation: 'Department of Cardiology' }],
    abstract = '',
    keywords = [],
    sections = [],
    references = [],
    correspondingAuthor = {},
    disclosures = 'The author has no conflicts of interest to disclose.',
    funding = 'No external funding was received for this work.',
  } = data;

  const localStyles = StyleSheet.create({
    titleBlock: {
      marginBottom: 24,
    },
    editorialTitle: {
      fontSize: 18,
      fontWeight: 'bold',
      color: getColor('primary.navy'),
      marginBottom: 16,
      fontFamily: 'Helvetica-Bold',
      lineHeight: 1.3,
    },
    authorList: {
      fontSize: 10,
      marginBottom: 8,
      color: '#333',
    },
    affiliations: {
      fontSize: 9,
      color: getColor('semantic.neutral'),
      marginBottom: 16,
      fontStyle: 'italic',
    },
    abstractBox: {
      backgroundColor: '#f8f9fa',
      padding: 16,
      marginBottom: 24,
      borderLeftWidth: 4,
      borderLeftColor: getColor('primary.navy'),
    },
    abstractLabel: {
      fontSize: 11,
      fontWeight: 'bold',
      marginBottom: 8,
      fontFamily: 'Helvetica-Bold',
      color: getColor('primary.navy'),
    },
    abstractText: {
      fontSize: 10,
      lineHeight: 1.5,
      textAlign: 'justify',
    },
    keywordsLine: {
      fontSize: 9,
      color: getColor('semantic.neutral'),
      marginTop: 12,
    },
    keywordLabel: {
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
    },
    sectionContent: {
      fontSize: 10,
      lineHeight: 1.6,
      textAlign: 'justify',
      marginBottom: 12,
    },
    referencesSection: {
      marginTop: 24,
      paddingTop: 16,
      borderTopWidth: 1,
      borderTopColor: '#e5e7eb',
    },
    reference: {
      fontSize: 8,
      marginBottom: 6,
      paddingLeft: 16,
      textIndent: -16,
    },
    refNumber: {
      fontWeight: 'bold',
    },
    disclosuresBox: {
      marginTop: 24,
      paddingTop: 16,
      borderTopWidth: 1,
      borderTopColor: '#e5e7eb',
      fontSize: 8,
      color: getColor('semantic.neutral'),
    },
    disclosureLabel: {
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      marginBottom: 4,
    },
    correspondenceBox: {
      marginTop: 16,
      fontSize: 8,
      color: getColor('semantic.neutral'),
    },
  });

  // Format authors with superscript affiliations
  const formatAuthors = () => {
    return authors.map((author, i) => {
      const suffix = i < authors.length - 1 ? ', ' : '';
      return `${author.name}${author.superscript ? `${author.superscript}` : ''}${suffix}`;
    }).join('');
  };

  // Format affiliations
  const formatAffiliations = () => {
    const uniqueAffiliations = [...new Set(authors.map(a => a.affiliation).filter(Boolean))];
    return uniqueAffiliations.map((aff, i) => `${i + 1}${aff}`).join('; ');
  };

  return (
    <Document>
      <Page size="LETTER" style={styles.page}>
        {/* Title Block */}
        <View style={localStyles.titleBlock}>
          <Text style={localStyles.editorialTitle}>{title}</Text>
          <Text style={localStyles.authorList}>{formatAuthors()}</Text>
          <Text style={localStyles.affiliations}>{formatAffiliations()}</Text>
        </View>

        {/* Abstract */}
        {abstract && (
          <View style={localStyles.abstractBox}>
            <Text style={localStyles.abstractLabel}>Abstract</Text>
            <Text style={localStyles.abstractText}>{abstract}</Text>
            {keywords.length > 0 && (
              <Text style={localStyles.keywordsLine}>
                <Text style={localStyles.keywordLabel}>Keywords: </Text>
                {keywords.join(', ')}
              </Text>
            )}
          </View>
        )}

        {/* Main Sections */}
        {sections.map((section, index) => (
          <View key={index} wrap={false}>
            <Text style={styles.sectionHeader}>{section.title}</Text>
            {Array.isArray(section.content) ? (
              section.content.map((para, pIndex) => (
                <Text key={pIndex} style={localStyles.sectionContent}>{para}</Text>
              ))
            ) : (
              <Text style={localStyles.sectionContent}>{section.content}</Text>
            )}
          </View>
        ))}

        {/* References */}
        {references.length > 0 && (
          <View style={localStyles.referencesSection}>
            <Text style={styles.sectionHeader}>References</Text>
            {references.map((ref, index) => (
              <Text key={index} style={localStyles.reference}>
                <Text style={localStyles.refNumber}>{index + 1}. </Text>
                {ref}
              </Text>
            ))}
          </View>
        )}

        {/* Disclosures */}
        <View style={localStyles.disclosuresBox}>
          <Text style={localStyles.disclosureLabel}>Disclosures</Text>
          <Text>{disclosures}</Text>
          {funding && (
            <>
              <Text style={[localStyles.disclosureLabel, { marginTop: 8 }]}>Funding</Text>
              <Text>{funding}</Text>
            </>
          )}
        </View>

        {/* Corresponding Author */}
        {correspondingAuthor.name && (
          <View style={localStyles.correspondenceBox}>
            <Text style={localStyles.disclosureLabel}>Corresponding Author</Text>
            <Text>{correspondingAuthor.name}</Text>
            {correspondingAuthor.email && <Text>Email: {correspondingAuthor.email}</Text>}
            {correspondingAuthor.address && <Text>{correspondingAuthor.address}</Text>}
          </View>
        )}

        {/* Footer */}
        <View style={styles.footer} fixed>
          <Text>Editorial</Text>
          <Text style={styles.pageNumber} render={({ pageNumber, totalPages }) =>
            `${pageNumber} / ${totalPages}`
          } />
          <Text>Preprint - Not Peer Reviewed</Text>
        </View>
      </Page>
    </Document>
  );
}

module.exports = Editorial;
