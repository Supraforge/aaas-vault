---
name: stripe-mcp
description: >-
  Integrates with Stripe API for payment processing, subscription management,
  invoicing, and financial automation
version: 1.0.0
dependencies:
  - python3
  - node
  - npm
inputs:
  - name: stripe_api_key
    description: Stripe secret API key
  - name: stripe_webhook_secret
    description: Stripe webhook signing secret for verifying events
  - name: stripe_publishable_key
    description: Stripe publishable key for client-side operations
outputs:
  - type: file
    description: Payment records and transaction reports
  - type: stdout
    description: API responses and operation status
compatibility: 'agent-zero, claude-code, cursor'
---

# Stripe MCP

## 🎯 Triggers
- "Process a payment for a customer"
- "Create a subscription plan"
- "Generate an invoice"
- "Handle Stripe webhook events"
- "Retrieve payment analytics"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/stripe-mcp/test.sh`.
- [ ] Check `.env` contains required Stripe API keys.
- [ ] Ensure Python and Node.js dependencies are installed.

## 📋 Workflow
1. **Authentication Setup**: Configure Stripe API keys in `.env` file
2. **Payment Processing**: Handle credit card payments, Apple Pay, Google Pay
3. **Subscription Management**: Create and manage recurring billing
4. **Webhook Handling**: Process Stripe events (payment succeeded, failed, etc.)
5. **Reporting**: Generate financial reports and analytics

## 🛠️ Script Reference
- Use `scripts/stripe_payments.py` for payment processing
- Use `scripts/stripe_subscriptions.py` for subscription management
- Use `scripts/stripe_mcp_server.js` for MCP server implementation
- Use `scripts/stripe_webhooks.py` for webhook handling

## 🔐 Security Notes
- Never commit `.env` file with Stripe keys
- Use environment variables in production
- Validate webhook signatures to prevent fraud

## 📚 API Reference
- [Stpe API Documentation](https://stripe.com/docs/api)
- [Stripe Webhooks Guide](https://stripe.com/docs/webhooks)
- [Stripe Python Library](https://github.com/stripe/stripe-python)
