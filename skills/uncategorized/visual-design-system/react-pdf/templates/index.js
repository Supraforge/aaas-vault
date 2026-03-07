/**
 * PDF Template Registry
 *
 * All templates export a React component that renders a PDF document.
 */

module.exports = {
  newsletter: require('./newsletter.js'),
  editorial: require('./editorial.js'),
  trialSummary: require('./trial-summary.js'),
  clinicalReport: require('./clinical-report.js'),
};
