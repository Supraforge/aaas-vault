# Arithmetic Functions Overview

All arithmetic functions are DST-safe—they add/subtract calendar units, not fixed durations.

## Add Functions

| Function | Description |
|----------|-------------|
| `addYears(input, n)` | Add years |
| `addMonths(input, n)` | Add months (handles month boundaries) |
| `addWeeks(input, n)` | Add weeks |
| `addDays(input, n)` | Add calendar days |
| `addHours(input, n)` | Add hours |
| `addMinutes(input, n)` | Add minutes |
| `addSeconds(input, n)` | Add seconds |
| `addMilliseconds(input, n)` | Add milliseconds |
| `addMicroseconds(input, n)` | Add microseconds |
| `addNanoseconds(input, n)` | Add nanoseconds |

## Subtract Functions

| Function | Description |
|----------|-------------|
| `subYears(input, n)` | Subtract years |
| `subMonths(input, n)` | Subtract months |
| `subWeeks(input, n)` | Subtract weeks |
| `subDays(input, n)` | Subtract days |
| `subHours(input, n)` | Subtract hours |
| `subMinutes(input, n)` | Subtract minutes |
| `subSeconds(input, n)` | Subtract seconds |
| `subMilliseconds(input, n)` | Subtract milliseconds |
| `subMicroseconds(input, n)` | Subtract microseconds |
| `subNanoseconds(input, n)` | Subtract nanoseconds |

## Common Signature

All functions follow this pattern:

```ts
function addX(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  amount: number
): Temporal.ZonedDateTime
```

## DST-Safe vs Duration-Based

**Calendar units** (years, months, weeks, days) add calendar periods:
- `addDays(date, 1)` = same time tomorrow, even across DST

**Duration units** (hours, minutes, seconds) add exact elapsed time:
- `addHours(date, 24)` = exactly 24 hours later (may be different time due to DST)

## Examples

```ts
import { addMonths, addDays, addHours, subWeeks } from '@gobrand/tiempo';

// Add 3 months (handles month boundaries)
const future = addMonths(date, 3);

// Subtract 2 weeks
const past = subWeeks(date, 2);

// Add 5 days (calendar days)
const nextWeek = addDays(date, 5);

// Add 48 hours (exact duration)
const later = addHours(date, 48);
```

## Negative Values

All functions accept negative values (equivalent to subtracting):

```ts
addDays(date, -7);  // Same as subDays(date, 7)
addMonths(date, -1); // Same as subMonths(date, 1)
```
