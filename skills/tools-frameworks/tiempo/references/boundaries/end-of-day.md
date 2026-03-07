# endOfDay

Returns a `ZonedDateTime` at the last nanosecond of the day (23:59:59.999999999).

## Signature

```ts
function endOfDay(
  input: Temporal.Instant | Temporal.ZonedDateTime
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to get the end of day for |

## Returns

A `Temporal.ZonedDateTime` at the last nanosecond of the same day.

## Examples

### From Instant (always UTC)

```ts
import { endOfDay } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');
endOfDay(instant);
// 2025-01-20T23:59:59.999999999Z[UTC]
```

### From ZonedDateTime (uses its timezone)

```ts
const zoned = Temporal.ZonedDateTime.from('2025-01-20T15:30:00-05:00[America/New_York]');
endOfDay(zoned);
// 2025-01-20T23:59:59.999999999-05:00[America/New_York]
```
