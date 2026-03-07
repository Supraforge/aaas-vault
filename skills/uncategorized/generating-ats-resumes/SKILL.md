---
name: generating-ats-resumes
description: >-
  Generates and optimizes resumes for Applicant Tracking Systems (ATS). Use when
  the user needs to create a professional resume, align their experience with a
  job description, or ensure for document compatibility with automated screening
  tools.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Generating ATS-Friendly Resumes

This skill specializes in creating resumes that pass through Applicant Tracking Systems (ATS) by focusing on keyword alignment, standard formatting, and quantified achievements.

## When to use this skill
- When a user provides a job description (JD) and wants their resume tailored to it.
- When a resume needs to be converted from a "fancy" layout to an ATS-safe format.
- When the user wants to identify missing keywords or skills based on a target role.

## Workflow

1. **Input Analysis**:
   - Request the **Job Description (JD)** and the user's **Current Resume/Profile**.
   - Extract primary keywords (Skills, Tools, Job Titles) from the JD.

2. **Optimization Phase**:
   - **Keyword Mapping**: Align the user's skills with the exact terminology used in the JD.
   - **Job Title Alignment**: Suggest adjustments to current titles if they are non-standard but functionally equivalent to the target role.
   - **Bullet Point Refinement**: Transform generic tasks into "Action Verb + Metric" statements.

3. **Formatting & Generation**:
   - Use the [ATS-Safe Template](resources/ats-resume-template.md).
   - Ensure a single-column layout with no tables, headers, or complex graphics.
   - Provide the final version in Markdown or clear text for easy conversion to .docx/PDF.

4. **Validation**:
   - Verify the output against the [ATS Quick Checklist](resources/ats-checklist.md).

## Instructions

### 1. Keyword Extraction Rules
- Focus on **Hard Skills** first (e.g., Python, Salesforce, Project Management).
- Use exact phrasing: if JD says "Data Analysis," do not use "Analyzing Data."
- Include certifications and education explicitly mentioned as "Preferred" or "Required."

### 2. The "Action + Result" Formula
Refactor every experience bullet point to follow this structure:
> **[Strong Action Verb]** + **[Task/Project]** + **[Quantifiable Metric/Outcome]**
*Example: "Managed team" -> "Led a team of 10 developers to deliver 3 high-priority modules, reducing technical debt by 25%."*

### 3. Formatting Restrictions
- **No Tables**: ATS often breaks text inside tables.
- **No Columns**: Use a flat, single-column top-to-bottom flow.
- **Standard Headings**: Use only "Experience," "Skills," "Education," and "Summary."

## Resources
- [ATS-Safe Resume Template](resources/ats-resume-template.md)
- [ATS Quick Checklist](resources/ats-checklist.md)
