# startOfWeek

Returns a `ZonedDateTime` at the first moment of the week (Monday at midnight). Uses ISO 8601 week definition: weeks start on Monday.

## Signature

```ts
function startOfWeek(
  input: Temporal.Instant | Temporal.ZonedDateTime
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to get the start of week for |

## Returns

A `Temporal.ZonedDateTime` at Monday midnight of the same week.

## Examples

### From Instant (Monday)

```ts
import { startOfWeek } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z'); // Monday
startOfWeek(instant);
// 2025-01-20T00:00:00Z[UTC] (same day, already Monday)
```

### From ZonedDateTime (Wednesday)

```ts
const zoned = Temporal.ZonedDateTime.from('2025-01-22T15:30:00-05:00[America/New_York]');
startOfWeek(zoned);
// 2025-01-20T00:00:00-05:00[America/New_York] (previous Monday)
```

## Common Patterns

### This week's range

```ts
import { startOfWeek, endOfWeek } from '@gobrand/tiempo';

const now = Temporal.Now.zonedDateTimeISO('America/New_York');
const weekStart = startOfWeek(now);
const weekEnd = endOfWeek(now);
```
