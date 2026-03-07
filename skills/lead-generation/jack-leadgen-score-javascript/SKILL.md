---
name: jack-leadgen-score-javascript
description: >-
  Scores leads based on company size and turnover, assigning a tier (Hot, Warm,
  Cold, Dead) and action based on score.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - lead scoring
  - javascript
  - sales automation
triggers:
  - when a lead submits a form with company size and turnover information
  - to automatically prioritize leads based on potential value
allowed-tools: []
compatibility: javascript runtime environment
metadata:
  source: jack-school
  lesson: 110
  lesson_title: How to Automate UNSTOPPABLE Lead Magnets
  difficulty: medium
  category: leadgen
  tools_required:
    - javascript runtime environment
  estimated_setup_time: 30min
---

# Leadgen Score Javascript

## When to Use

Use this skill when you need to:
- when a lead submits a form with company size and turnover information
- to automatically prioritize leads based on potential value

## What This Does

Scores leads based on company size and turnover, assigning a tier (Hot, Warm, Cold, Dead) and action based on score.

## Workflow

// Get inputs (case-insensitive matching)
const companySizeRaw = input.companySize || "";
const turnoverRaw = input.turnover || "";

// Normalize to lowercase for matching
const companySize = companySizeRaw.toLowerCase();
const turnover = turnoverRaw.toLowerCase();

let score = 0;
let breakdown = [];

// 1. COMPANY SIZE SCORING (0-30 points)
const companySizeScores = {
  "1-10 employees": 6,
  "11-50 employees": 12,
  "51-250 employees": 18,
  "251-500 employees": 24,
  "500+ employees": 30
};

const companySizeScore = companySizeScores[companySize] || 0;
score += companySizeScore;
breakdown.push(`Employees: +${companySizeScore}`);

// 2. TURNOVER SCORING (0-70 points)
const turnoverScores = {
  "$100k - $500k": 14,
  "$500k - $1m": 28,
  "$1m - $2.5m": 42,
  "$2.5m - $5m": 56,
  "$5m+": 70
};

const turnoverScore = turnoverScores[turnover] || 0;
score += turnoverScore;
breakdown.push(`Turnover: +${turnoverScore}`);

// DETERMINE TIER WITH EMOJIS
let tier = "";
let action = "";
let priority = "";

if (score >= 70) {
  tier = "🔥 HOT";
  action = "Call today - High value target";
  priority = "High";
} else if (score >= 50) {
  tier = "🟡 WARM";
  action = "Contact this week";
  priority = "Medium";
} else if (score >= 30) {
  tier = "🔵 COLD";
  action = "Nurture sequence";
  priority = "Low";
} else {
  tier = "❌ DEAD";
  action = "Archive - Too small";
  priority = "None";
}

// Override: $5M+ companies are never DEAD
if (turnover.includes("$5m") && tier === "❌ DEAD") {
  tier = "🟡 WARM";
  action = "Contact this week - High revenue despite small team";
  priority = "Medium";
}

// Build result object
const result = {
  companySize: companySizeRaw,
  turnover: turnoverRaw,
  totalScore: score,
  maxScore: 100,
  scorePercent: score,
  tier: tier,
  priority: priority,
  action: action,
  employeePoints: companySizeScore,
  turnoverPoints: turnoverScore,
  breakdown: breakdown.join(" | ")
};

// Return it
return result;

## Configuration

**Required tools/platforms:**
- javascript runtime environment

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
