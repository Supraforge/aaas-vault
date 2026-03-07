# Always Use Explicit Timezones

Never rely on implicit timezone behavior. Always specify the timezone explicitly.

## The Problem

JavaScript's Date object and many datetime libraries use the system's local timezone by default. This causes bugs when:
- Code runs on servers in different regions
- Code runs in browsers with different user settings
- Tests pass locally but fail in CI (different timezone)

## The Solution

Always pass the timezone explicitly to tiempo functions:

```ts
// ❌ Bad - implicit timezone (uses system default)
const date = new Date("2025-03-09");
const now = new Date();

// ✅ Good - explicit timezone
import { toZonedTime, now, today } from '@gobrand/tiempo';

const nyTime = toZonedTime(utcDate, 'America/New_York');
const currentTime = now('America/New_York');
const todayInTokyo = today('Asia/Tokyo');
```

## Server-side Patterns

```ts
// Get timezone from user preferences (stored in DB)
const userTime = toZonedTime(utcDate, user.timezone);

// Get timezone from request header (sent by client)
const userTime = toZonedTime(utcDate, req.headers['x-timezone']);

// For UTC operations
const utcTime = toZonedTime(utcDate, "UTC");
```

## Client-side Patterns

```ts
import { toZonedTime, browserTimezone } from '@gobrand/tiempo';

// Auto-detect browser timezone
const localTime = toZonedTime(utcDate, browserTimezone());
```

## Benefits

- **Predictable**: Same behavior regardless of where code runs
- **Testable**: Tests work the same in any environment
- **Debuggable**: Clear what timezone is being used
- **Explicit**: No hidden assumptions in code
