# startOfMonth

Returns a `ZonedDateTime` at the first moment of the month (1st day at midnight).

## Signature

```ts
function startOfMonth(
  input: Temporal.Instant | Temporal.ZonedDateTime
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to get the start of month for |

## Returns

A `Temporal.ZonedDateTime` at midnight on the 1st day of the month.

## Examples

```ts
import { startOfMonth } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-15T12:00:00Z');
startOfMonth(instant);
// 2025-01-01T00:00:00Z[UTC]

const zoned = Temporal.ZonedDateTime.from('2025-01-15T15:30:00-05:00[America/New_York]');
startOfMonth(zoned);
// 2025-01-01T00:00:00-05:00[America/New_York]
```

## Common Patterns

### Month-to-date

```ts
import { startOfMonth, now } from '@gobrand/tiempo';

const current = now('America/New_York');
const monthStart = startOfMonth(current);

// Month-to-date range: [monthStart, current]
```
