# Frontend Skills

Wallet connection, transaction signing, on-chain state reading, and security.

## Skills in This Pillar

| Skill | Description | Difficulty |
|-------|-------------|------------|
| [wallet-connection-ux](wallet-connection-ux/) | Phantom/Solflare/Backpack UX, connect/disconnect, state | Beginner |
| [transaction-signing-and-feedback](transaction-signing-and-feedback/) | Pending/fail states, retries, confirmations | Intermediate |
| [reading-onchain-state](reading-onchain-state/) | Fetch patterns, caching, reactivity, indexing | Intermediate |
| [frontend-security-basics](frontend-security-basics/) | Phishing vectors, approval UX, safety prompts | Intermediate |

## Building a Solana dApp

1. **Connect**: `wallet-connection-ux` - let users connect wallets
2. **Read**: `reading-onchain-state` - display on-chain data
3. **Write**: `transaction-signing-and-feedback` - submit transactions
4. **Secure**: `frontend-security-basics` - protect users

## Quick Start

**Build wallet connection:**
```
Apply wallet-connection-ux to create a React connect button
with Phantom/Solflare support, proper error handling, and
mobile deep link support.
```

**Handle transaction UX:**
```
Use transaction-signing-and-feedback to design the UX flow
for a swap transaction: pending state, confirmation, error
handling, and retry logic.
```

## Framework Support

All skills work with:
- React / Next.js
- Vue / Nuxt
- Svelte / SvelteKit
- Vanilla JS

Using `@solana/wallet-adapter-*` packages for wallet integration.

## Related Skills

- [trading/jupiter-swap-integration](../trading/jupiter-swap-integration/) - Swap implementation
- [infra/rpc-selection-and-resilience](../infra/rpc-selection-and-resilience/) - RPC setup
- [core-dev/solana-account-model](../core-dev/solana-account-model/) - Understanding accounts
