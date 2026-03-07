# addMonths

Add months to a datetime. Handles month-end dates correctly.

## Signature

```ts
function addMonths(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  months: number
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to add months to |
| `months` | `number` | Number of months to add (can be negative) |

## Returns

A `Temporal.ZonedDateTime` with the months added.

## Examples

### Basic usage

```ts
import { addMonths } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');
addMonths(instant, 3);
// 2025-04-20T12:00:00Z[UTC]
```

### Month-end handling

```ts
const endOfJan = Temporal.Instant.from('2025-01-31T12:00:00Z');
addMonths(endOfJan, 1);
// 2025-02-28T12:00:00Z[UTC] (Jan 31 → Feb 28)
```
