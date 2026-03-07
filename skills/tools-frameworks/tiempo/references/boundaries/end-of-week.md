# endOfWeek

Returns a `ZonedDateTime` at the last moment of the week (Sunday at 23:59:59.999999999). Uses ISO 8601 week definition: weeks end on Sunday.

## Signature

```ts
function endOfWeek(
  input: Temporal.Instant | Temporal.ZonedDateTime
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to get the end of week for |

## Returns

A `Temporal.ZonedDateTime` at Sunday 23:59:59.999999999 of the same week.

## Examples

### From Instant (Monday)

```ts
import { endOfWeek } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');
endOfWeek(instant);
// 2025-01-26T23:59:59.999999999Z[UTC] (next Sunday)
```

### From ZonedDateTime (Wednesday)

```ts
const zoned = Temporal.ZonedDateTime.from('2025-01-22T15:30:00-05:00[America/New_York]');
endOfWeek(zoned);
// 2025-01-26T23:59:59.999999999-05:00[America/New_York]
```
