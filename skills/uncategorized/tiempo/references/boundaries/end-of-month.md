# endOfMonth

Returns a `ZonedDateTime` at the last moment of the month.

## Signature

```ts
function endOfMonth(
  input: Temporal.Instant | Temporal.ZonedDateTime
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to get the end of month for |

## Returns

A `Temporal.ZonedDateTime` at the last nanosecond of the last day of the month.

## Examples

```ts
import { endOfMonth } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-15T12:00:00Z');
endOfMonth(instant);
// 2025-01-31T23:59:59.999999999Z[UTC]

// February in a non-leap year
const feb = Temporal.ZonedDateTime.from('2025-02-15T15:30:00-05:00[America/New_York]');
endOfMonth(feb);
// 2025-02-28T23:59:59.999999999-05:00[America/New_York]
```
