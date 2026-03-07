---
name: payment
description: >-
  Payment processing and management. Handle invoices, transactions, and payment
  gateway integrations.
metadata:
  clawdbot:
    emoji: "\U0001F4B3"
    always: true
    requires:
      bins:
        - curl
        - jq
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Payment 💳

Payment processing and transaction management.

## Features

- Create and send invoices
- Process payments
- Track payment status
- Refund management
- Payment history

## Supported Gateways

- Stripe
- PayPal
- Square
- Crypto payments

## Usage Examples

```
"Create an invoice for $100"
"Check payment status for order #123"
"Show recent transactions"
```

## Safety Rules

1. **ALWAYS** verify payment amounts before processing
2. **NEVER** store sensitive payment credentials in plain text
