/**
 * Trial Summary Template - Clinical Trial Results Summary
 *
 * One-page summary of landmark clinical trial results.
 * Features: Key endpoints, forest plot placeholder, patient flow, conclusions.
 */

const React = require('react');
const { Document, Page, Text, View, StyleSheet, Image } = require('@react-pdf/renderer');

function TrialSummary({ data, styles, getColor }) {
  const {
    trialName = 'TRIAL-NAME',
    fullTitle = 'Full Trial Title Here',
    registry = 'NCT00000000',
    publication = '',
    population = {},
    intervention = {},
    comparator = {},
    primaryEndpoint = {},
    secondaryEndpoints = [],
    safetyFindings = [],
    conclusions = [],
    limitations = [],
    clinicalImplications = '',
  } = data;

  const localStyles = StyleSheet.create({
    trialHeader: {
      backgroundColor: getColor('primary.navy'),
      color: 'white',
      padding: 16,
      marginBottom: 16,
      marginLeft: -72,
      marginRight: -72,
      marginTop: -72,
      paddingLeft: 72,
      paddingRight: 72,
    },
    trialName: {
      fontSize: 24,
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      marginBottom: 4,
    },
    trialTitle: {
      fontSize: 11,
      marginBottom: 8,
      lineHeight: 1.3,
    },
    registryLine: {
      fontSize: 9,
      opacity: 0.8,
    },
    picoBox: {
      flexDirection: 'row',
      marginBottom: 16,
      gap: 12,
    },
    picoItem: {
      flex: 1,
      backgroundColor: '#f8f9fa',
      padding: 12,
      borderRadius: 4,
    },
    picoLabel: {
      fontSize: 9,
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      color: getColor('primary.teal'),
      marginBottom: 4,
      textTransform: 'uppercase',
    },
    picoValue: {
      fontSize: 10,
      lineHeight: 1.4,
    },
    endpointBox: {
      backgroundColor: '#f0f9ff',
      padding: 16,
      marginBottom: 16,
      borderRadius: 4,
      borderWidth: 2,
      borderColor: getColor('primary.blue'),
    },
    endpointLabel: {
      fontSize: 10,
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      color: getColor('primary.blue'),
      marginBottom: 8,
    },
    endpointResult: {
      flexDirection: 'row',
      justifyContent: 'space-between',
      alignItems: 'center',
    },
    hrValue: {
      fontSize: 28,
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      color: getColor('primary.navy'),
    },
    ciValue: {
      fontSize: 12,
      color: getColor('semantic.neutral'),
    },
    pValue: {
      fontSize: 14,
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      color: getColor('semantic.success'),
    },
    secondaryRow: {
      flexDirection: 'row',
      borderBottomWidth: 1,
      borderBottomColor: '#e5e7eb',
      paddingVertical: 8,
    },
    secondaryEndpoint: {
      flex: 2,
      fontSize: 9,
    },
    secondaryResult: {
      flex: 1,
      fontSize: 9,
      textAlign: 'right',
    },
    twoColumn: {
      flexDirection: 'row',
      gap: 16,
      marginTop: 16,
    },
    halfColumn: {
      flex: 1,
    },
    bulletList: {
      marginTop: 8,
    },
    bulletItem: {
      flexDirection: 'row',
      marginBottom: 4,
      fontSize: 9,
    },
    bullet: {
      width: 12,
    },
    conclusionBox: {
      backgroundColor: '#f0fdf4',
      padding: 12,
      borderRadius: 4,
      marginTop: 16,
      borderLeftWidth: 4,
      borderLeftColor: getColor('semantic.success'),
    },
    conclusionText: {
      fontSize: 10,
      lineHeight: 1.5,
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
    },
  });

  return (
    <Document>
      <Page size="LETTER" style={[styles.page, { paddingTop: 0 }]}>
        {/* Trial Header */}
        <View style={localStyles.trialHeader}>
          <Text style={localStyles.trialName}>{trialName}</Text>
          <Text style={localStyles.trialTitle}>{fullTitle}</Text>
          <Text style={localStyles.registryLine}>
            {registry} | {publication}
          </Text>
        </View>

        {/* PICO Summary */}
        <View style={localStyles.picoBox}>
          <View style={localStyles.picoItem}>
            <Text style={localStyles.picoLabel}>Population</Text>
            <Text style={localStyles.picoValue}>
              N = {population.n?.toLocaleString() || '?'}{'\n'}
              {population.description || 'Patients with...'}
            </Text>
          </View>
          <View style={localStyles.picoItem}>
            <Text style={localStyles.picoLabel}>Intervention</Text>
            <Text style={localStyles.picoValue}>
              {intervention.name || 'Treatment'}{'\n'}
              {intervention.dose || ''}
            </Text>
          </View>
          <View style={localStyles.picoItem}>
            <Text style={localStyles.picoLabel}>Comparator</Text>
            <Text style={localStyles.picoValue}>
              {comparator.name || 'Control'}{'\n'}
              {comparator.dose || ''}
            </Text>
          </View>
        </View>

        {/* Primary Endpoint */}
        <View style={localStyles.endpointBox}>
          <Text style={localStyles.endpointLabel}>PRIMARY ENDPOINT: {primaryEndpoint.name || 'Composite outcome'}</Text>
          <View style={localStyles.endpointResult}>
            <View>
              <Text style={localStyles.hrValue}>
                {primaryEndpoint.metric || 'HR'} {primaryEndpoint.value || '0.80'}
              </Text>
              <Text style={localStyles.ciValue}>
                95% CI: {primaryEndpoint.ci || '0.70-0.92'}
              </Text>
            </View>
            <Text style={localStyles.pValue}>
              p {primaryEndpoint.pValue || '< 0.001'}
            </Text>
          </View>
        </View>

        {/* Secondary Endpoints */}
        {secondaryEndpoints.length > 0 && (
          <View>
            <Text style={styles.subsectionHeader}>Secondary Endpoints</Text>
            {secondaryEndpoints.map((ep, index) => (
              <View key={index} style={localStyles.secondaryRow}>
                <Text style={localStyles.secondaryEndpoint}>{ep.name}</Text>
                <Text style={localStyles.secondaryResult}>
                  {ep.metric || 'HR'} {ep.value} ({ep.ci}) p={ep.pValue}
                </Text>
              </View>
            ))}
          </View>
        )}

        {/* Two Column: Safety and Limitations */}
        <View style={localStyles.twoColumn}>
          <View style={localStyles.halfColumn}>
            <Text style={styles.subsectionHeader}>Safety Findings</Text>
            <View style={localStyles.bulletList}>
              {safetyFindings.map((finding, index) => (
                <View key={index} style={localStyles.bulletItem}>
                  <Text style={localStyles.bullet}>•</Text>
                  <Text>{finding}</Text>
                </View>
              ))}
            </View>
          </View>
          <View style={localStyles.halfColumn}>
            <Text style={styles.subsectionHeader}>Limitations</Text>
            <View style={localStyles.bulletList}>
              {limitations.map((limitation, index) => (
                <View key={index} style={localStyles.bulletItem}>
                  <Text style={localStyles.bullet}>•</Text>
                  <Text>{limitation}</Text>
                </View>
              ))}
            </View>
          </View>
        </View>

        {/* Clinical Implications */}
        {clinicalImplications && (
          <View style={localStyles.conclusionBox}>
            <Text style={localStyles.conclusionText}>
              Clinical Implications: {clinicalImplications}
            </Text>
          </View>
        )}

        {/* Footer */}
        <View style={styles.footer} fixed>
          <Text>Trial Summary</Text>
          <Text style={styles.pageNumber} render={({ pageNumber, totalPages }) =>
            `${pageNumber} / ${totalPages}`
          } />
          <Text>Generated by Visual System</Text>
        </View>
      </Page>
    </Document>
  );
}

module.exports = TrialSummary;
