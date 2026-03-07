# startOfYear

Returns a `ZonedDateTime` at the first moment of the year (January 1 at midnight).

## Signature

```ts
function startOfYear(
  input: Temporal.Instant | Temporal.ZonedDateTime
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to get the start of year for |

## Returns

A `Temporal.ZonedDateTime` at January 1, 00:00:00.000000000.

## Examples

```ts
import { startOfYear } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-06-15T12:00:00Z');
startOfYear(instant);
// 2025-01-01T00:00:00Z[UTC]

const zoned = Temporal.ZonedDateTime.from('2025-06-15T15:30:00-05:00[America/New_York]');
startOfYear(zoned);
// 2025-01-01T00:00:00-05:00[America/New_York]
```

## Common Patterns

### Year-to-date

```ts
import { startOfYear, now } from '@gobrand/tiempo';

const current = now('America/New_York');
const yearStart = startOfYear(current);

// Year-to-date range: [yearStart, current]
```
