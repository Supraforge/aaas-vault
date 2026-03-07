/**
 * Clinical Report Template - Case Report / Clinical Summary
 *
 * Structured clinical documentation for case presentations.
 * Features: Patient info, timeline, findings, management, outcome.
 */

const React = require('react');
const { Document, Page, Text, View, StyleSheet } = require('@react-pdf/renderer');

function ClinicalReport({ data, styles, getColor }) {
  const {
    reportType = 'Case Report',
    title = 'Clinical Case Report',
    patient = {},
    chiefComplaint = '',
    historyOfPresentIllness = '',
    pastMedicalHistory = [],
    medications = [],
    physicalExam = {},
    investigations = [],
    diagnosis = {},
    management = [],
    outcome = '',
    discussion = '',
    learningPoints = [],
    references = [],
  } = data;

  const localStyles = StyleSheet.create({
    reportHeader: {
      borderBottomWidth: 2,
      borderBottomColor: getColor('primary.navy'),
      paddingBottom: 12,
      marginBottom: 16,
    },
    reportType: {
      fontSize: 10,
      color: getColor('primary.teal'),
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      textTransform: 'uppercase',
      letterSpacing: 1,
    },
    reportTitle: {
      fontSize: 18,
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      color: getColor('primary.navy'),
      marginTop: 8,
    },
    patientBox: {
      backgroundColor: '#f8f9fa',
      padding: 12,
      marginBottom: 16,
      flexDirection: 'row',
      justifyContent: 'space-between',
    },
    patientInfo: {
      fontSize: 10,
    },
    patientLabel: {
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      color: getColor('semantic.neutral'),
      marginRight: 4,
    },
    sectionContent: {
      fontSize: 10,
      lineHeight: 1.6,
      textAlign: 'justify',
      marginBottom: 8,
    },
    listItem: {
      flexDirection: 'row',
      marginBottom: 4,
      fontSize: 10,
    },
    bullet: {
      width: 16,
      color: getColor('primary.teal'),
    },
    investigationTable: {
      marginTop: 8,
      marginBottom: 12,
    },
    tableRow: {
      flexDirection: 'row',
      borderBottomWidth: 1,
      borderBottomColor: '#e5e7eb',
      paddingVertical: 6,
    },
    tableHeader: {
      flexDirection: 'row',
      backgroundColor: getColor('primary.navy'),
      paddingVertical: 8,
    },
    tableHeaderCell: {
      flex: 1,
      color: 'white',
      fontSize: 9,
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      paddingHorizontal: 8,
    },
    tableCell: {
      flex: 1,
      fontSize: 9,
      paddingHorizontal: 8,
    },
    abnormalValue: {
      color: getColor('semantic.danger'),
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
    },
    diagnosisBox: {
      backgroundColor: '#fef3c7',
      padding: 12,
      marginBottom: 16,
      borderLeftWidth: 4,
      borderLeftColor: getColor('semantic.warning'),
    },
    diagnosisLabel: {
      fontSize: 10,
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      color: getColor('semantic.warning'),
      marginBottom: 4,
    },
    diagnosisPrimary: {
      fontSize: 12,
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      color: getColor('primary.navy'),
    },
    diagnosisSecondary: {
      fontSize: 10,
      color: getColor('semantic.neutral'),
      marginTop: 4,
    },
    managementStep: {
      flexDirection: 'row',
      marginBottom: 8,
      alignItems: 'flex-start',
    },
    stepNumber: {
      width: 24,
      height: 24,
      borderRadius: 12,
      backgroundColor: getColor('primary.teal'),
      color: 'white',
      fontSize: 10,
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      textAlign: 'center',
      lineHeight: 24,
      marginRight: 12,
    },
    stepContent: {
      flex: 1,
      fontSize: 10,
      lineHeight: 1.5,
    },
    outcomeBox: {
      backgroundColor: '#f0fdf4',
      padding: 12,
      marginBottom: 16,
      borderLeftWidth: 4,
      borderLeftColor: getColor('semantic.success'),
    },
    learningBox: {
      backgroundColor: '#eff6ff',
      padding: 12,
      marginTop: 16,
      borderRadius: 4,
    },
    learningTitle: {
      fontSize: 11,
      fontWeight: 'bold',
      fontFamily: 'Helvetica-Bold',
      color: getColor('primary.blue'),
      marginBottom: 8,
    },
  });

  return (
    <Document>
      <Page size="LETTER" style={styles.page}>
        {/* Report Header */}
        <View style={localStyles.reportHeader}>
          <Text style={localStyles.reportType}>{reportType}</Text>
          <Text style={localStyles.reportTitle}>{title}</Text>
        </View>

        {/* Patient Demographics */}
        {patient.age && (
          <View style={localStyles.patientBox}>
            <View style={{ flexDirection: 'row' }}>
              <Text style={localStyles.patientLabel}>Age:</Text>
              <Text style={localStyles.patientInfo}>{patient.age}</Text>
            </View>
            <View style={{ flexDirection: 'row' }}>
              <Text style={localStyles.patientLabel}>Sex:</Text>
              <Text style={localStyles.patientInfo}>{patient.sex}</Text>
            </View>
            {patient.occupation && (
              <View style={{ flexDirection: 'row' }}>
                <Text style={localStyles.patientLabel}>Occupation:</Text>
                <Text style={localStyles.patientInfo}>{patient.occupation}</Text>
              </View>
            )}
          </View>
        )}

        {/* Chief Complaint */}
        {chiefComplaint && (
          <View wrap={false}>
            <Text style={styles.sectionHeader}>Chief Complaint</Text>
            <Text style={localStyles.sectionContent}>{chiefComplaint}</Text>
          </View>
        )}

        {/* History of Present Illness */}
        {historyOfPresentIllness && (
          <View wrap={false}>
            <Text style={styles.sectionHeader}>History of Present Illness</Text>
            <Text style={localStyles.sectionContent}>{historyOfPresentIllness}</Text>
          </View>
        )}

        {/* Past Medical History */}
        {pastMedicalHistory.length > 0 && (
          <View wrap={false}>
            <Text style={styles.sectionHeader}>Past Medical History</Text>
            {pastMedicalHistory.map((item, index) => (
              <View key={index} style={localStyles.listItem}>
                <Text style={localStyles.bullet}>•</Text>
                <Text>{item}</Text>
              </View>
            ))}
          </View>
        )}

        {/* Investigations */}
        {investigations.length > 0 && (
          <View wrap={false}>
            <Text style={styles.sectionHeader}>Investigations</Text>
            <View style={localStyles.investigationTable}>
              <View style={localStyles.tableHeader}>
                <Text style={localStyles.tableHeaderCell}>Test</Text>
                <Text style={localStyles.tableHeaderCell}>Result</Text>
                <Text style={localStyles.tableHeaderCell}>Reference</Text>
              </View>
              {investigations.map((inv, index) => (
                <View key={index} style={localStyles.tableRow}>
                  <Text style={localStyles.tableCell}>{inv.test}</Text>
                  <Text style={[
                    localStyles.tableCell,
                    inv.abnormal && localStyles.abnormalValue
                  ]}>
                    {inv.result}
                  </Text>
                  <Text style={localStyles.tableCell}>{inv.reference}</Text>
                </View>
              ))}
            </View>
          </View>
        )}

        {/* Diagnosis */}
        {diagnosis.primary && (
          <View style={localStyles.diagnosisBox}>
            <Text style={localStyles.diagnosisLabel}>DIAGNOSIS</Text>
            <Text style={localStyles.diagnosisPrimary}>{diagnosis.primary}</Text>
            {diagnosis.secondary && (
              <Text style={localStyles.diagnosisSecondary}>
                Secondary: {Array.isArray(diagnosis.secondary) ? diagnosis.secondary.join(', ') : diagnosis.secondary}
              </Text>
            )}
          </View>
        )}

        {/* Management */}
        {management.length > 0 && (
          <View wrap={false}>
            <Text style={styles.sectionHeader}>Management</Text>
            {management.map((step, index) => (
              <View key={index} style={localStyles.managementStep}>
                <Text style={localStyles.stepNumber}>{index + 1}</Text>
                <Text style={localStyles.stepContent}>{step}</Text>
              </View>
            ))}
          </View>
        )}

        {/* Outcome */}
        {outcome && (
          <View style={localStyles.outcomeBox}>
            <Text style={[localStyles.diagnosisLabel, { color: getColor('semantic.success') }]}>OUTCOME</Text>
            <Text style={localStyles.sectionContent}>{outcome}</Text>
          </View>
        )}

        {/* Learning Points */}
        {learningPoints.length > 0 && (
          <View style={localStyles.learningBox}>
            <Text style={localStyles.learningTitle}>Key Learning Points</Text>
            {learningPoints.map((point, index) => (
              <View key={index} style={localStyles.listItem}>
                <Text style={localStyles.bullet}>{index + 1}.</Text>
                <Text>{point}</Text>
              </View>
            ))}
          </View>
        )}

        {/* Footer */}
        <View style={styles.footer} fixed>
          <Text>{reportType}</Text>
          <Text style={styles.pageNumber} render={({ pageNumber, totalPages }) =>
            `${pageNumber} / ${totalPages}`
          } />
          <Text>Confidential</Text>
        </View>
      </Page>
    </Document>
  );
}

module.exports = ClinicalReport;
