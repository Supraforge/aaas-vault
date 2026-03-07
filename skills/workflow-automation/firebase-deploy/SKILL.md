---
name: "deploy-landing-page"
description: "Deploys a landing page to Firebase Hosting without requiring confirmation prompts."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["firebase","hosting","deployment"]
triggers:
  - "deploy landing page"
  - "firebase deploy hosting"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "workflow"
  original_file: "firebase-deploy.md"
---

# Deploy Landing Page

## When to Use

Use when you want to quickly deploy your landing page updates to Firebase Hosting without interactive prompts.

## What This Does

Deploys a landing page to Firebase Hosting without requiring confirmation prompts.

## Workflow

1. Select the Firebase project using `npx firebase use --add`. 2. Deploy to Firebase Hosting using `npx firebase deploy --only hosting`.

## Prerequisites

Firebase CLI installed and project initialized with Firebase Hosting.
