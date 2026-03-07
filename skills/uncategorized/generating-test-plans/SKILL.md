---
name: generating-test-plans
description: >-
  Generates, verifies, and improves test plan documents. Use when the user needs
  to create a new test plan, evaluate an existing one, or transform a draft into
  a professional standard document.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Generating Test Plans

This skill provides a structured approach to creating, verifying, and refining test plan documents to ensure high-quality software testing.

## When to use this skill
- When the user uploads a test plan and wants it verified against industry standards.
- When the user needs to generate a new test plan from scratch or based on requirement documents.
- When an existing test plan needs to be improved, updated, or reformatted.

## Workflow

To process a test plan, follow this "Verify-Plan-Refine" pattern:

1. **Verify Phase** (If a document is uploaded):
   - Review the uploaded document using the [Verification Checklist](resources/verification-checklist.md).
   - Identify missing sections or weak descriptions (e.g., vague test objectives, missing exit criteria).
   - Provide feedback to the user on what is missing or needs improvement.

2. **Generation/Update Phase**:
   - Use the [Standard Test Plan Template](resources/test-plan-template.md) as a base.
   - If generating from an existing document, merge the existing content into the template, filling in gaps and enhancing details.
   - If generating from requirements, map requirements to test objectives and scope.

3. **Refinement Phase**:
   - Ensure the tone is professional and technical.
   - Verify that all specific user constraints are met.
   - Present the finalized test plan to the user.

## Instructions

### 1. Document Analysis
When a user uploads a document, check for these core components:
- **Test Items**: What is being tested?
- **Features to be Tested**: Specific functional/non-functional areas.
- **Features NOT to be Tested**: Explicit exclusions.
- **Pass/Fail Criteria**: How do we know it passed?
- **Suspension/Resume Criteria**: When to stop testing (e.g., blocking bugs).
- **Deliverables**: What reports will be generated?
- **Risks and Contingencies**: What could go wrong?

### 2. Improvement Rules
- **Specific**: Ensure steps and criteria are not ambiguous.
- **Actionable**: All test items should lead to a clear test activity.
- **Format**: Use Markdown headers and lists for readability.

## Resources
- [Standard Test Plan Template](resources/test-plan-template.md)
- [Verification Checklist](resources/verification-checklist.md)
