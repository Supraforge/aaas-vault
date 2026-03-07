# addYears

Add years to a datetime. Handles leap years correctly.

## Signature

```ts
function addYears(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  years: number
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to add years to |
| `years` | `number` | Number of years to add (can be negative) |

## Returns

A `Temporal.ZonedDateTime` with the years added.

## Examples

### Basic usage

```ts
import { addYears } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');
addYears(instant, 2);
// 2027-01-20T12:00:00Z[UTC]
```

### Leap year handling

```ts
const leapDay = Temporal.Instant.from('2024-02-29T12:00:00Z');
addYears(leapDay, 1);
// 2025-02-28T12:00:00Z[UTC] (Feb 29 → Feb 28)
```

### Negative values subtract

```ts
addYears(instant, -5);
// 2020-01-20T12:00:00Z[UTC]
```
