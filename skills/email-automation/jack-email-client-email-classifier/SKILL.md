---
name: jack-email-client-email-classifier
description: >-
  Automatically classify incoming emails as client-related based on sender,
  subject, and body content, using data from Airtable.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - email
  - classification
  - client identification
  - automation
triggers:
  - When processing a new email
allowed-tools: []
compatibility: 'n8n, airtable'
metadata:
  source: jack-school
  lesson: 85
  lesson_title: What it does
  difficulty: medium
  category: email
  tools_required:
    - n8n
    - airtable
  estimated_setup_time: 30min
---

# Email Client Email Classifier

## When to Use

Use this skill when you need to:
- When processing a new email

## What This Does

Automatically classify incoming emails as client-related based on sender, subject, and body content, using data from Airtable.

## Workflow

// Get client list from Format Airtable Data node
const clients = $input.first().json.clients || [];

// Get email data from Gmail Trigger
const gmailData = $('Gmail Trigger').first().json || {};
const headers = gmailData.headers || {};

// Extract email fields, ensuring they're strings
const subject = String(headers.subject || "").toLowerCase();
const fromHeader = String(headers.from || "").toLowerCase();
const body = String(gmailData.text || "").toLowerCase();

// Debug logging
console.log("Processing email:");
console.log("- Subject:", subject);
console.log("- From:", fromHeader);
console.log("- Available clients:", JSON.stringify(clients));

// Initialize variables
let isMatch = false;
let matchedClient = null;
let matchReason = "No match found";

// Check each client for matches
for (const client of clients) {
  if (!client.clientName) continue;
  
  const clientName = client.clientName.toLowerCase();
  const domain = client.domain ? client.domain.toLowerCase() : "";
  const clientEmail = client.email ? client.email.toLowerCase() : "";
  
  console.log(`Checking client: ${clientName}, email: ${clientEmail}, domain: ${domain}`);
  
  // Check if sender email matches client email directly
  if (clientEmail && fromHeader.includes(clientEmail)) {
    isMatch = true;
    matchedClient = client.clientName;
    matchReason = `Email match: ${clientEmail}`;
    break;
  }
  
  // Check for client name in subject
  if (clientName && subject.includes(clientName)) {
    isMatch = true;
    matchedClient = client.clientName;
    matchReason = `Subject contains client name: ${client.clientName}`;
    break;
  }
  
  // Check for client name in body
  if (clientName && body.includes(clientName)) {
    isMatch = true;
    matchedClient = client.clientName;
    matchReason = `Body contains client name: ${client.clientName}`;
    break;
  }
  
  // Check for domain in sender
  if (domain && fromHeader.includes(domain)) {
    isMatch = true;
    matchedClient = client.clientName;
    matchReason = `Sender contains client domain: ${domain}`;
    break;
  }
  
  // Special case for "Grind" vs "Grind Coffee"
  if ((clientName === "grind coffee" && subject.includes("grind")) ||
      (clientName === "grind" && subject.includes("grind"))) {
    isMatch = true;
    matchedClient = client.clientName;
    matchReason = `Subject contains partial client name: ${client.clientName}`;
    break;
  }
}

// Final decision
const decision = isMatch ? "Save" : "Delete";

// Return result
return {
  json: {
    decision,
    isClientEmail: isMatch,
    matchReason,
    matchedClient,
    emailSubject: headers.subject || "",
    emailFrom: headers.from || "",
    emailId: gmailData.id || headers["message-id"] || "",
    emailBody: gmailData.text || ""
  }
};

## Configuration

**Required tools/platforms:**
- n8n
- airtable

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
