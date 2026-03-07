# endOfYear

Returns a `ZonedDateTime` at the last moment of the year (December 31 at 23:59:59.999999999).

## Signature

```ts
function endOfYear(
  input: Temporal.Instant | Temporal.ZonedDateTime
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to get the end of year for |

## Returns

A `Temporal.ZonedDateTime` at December 31, 23:59:59.999999999.

## Examples

```ts
import { endOfYear } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-06-15T12:00:00Z');
endOfYear(instant);
// 2025-12-31T23:59:59.999999999Z[UTC]

const zoned = Temporal.ZonedDateTime.from('2025-06-15T15:30:00-05:00[America/New_York]');
endOfYear(zoned);
// 2025-12-31T23:59:59.999999999-05:00[America/New_York]
```
