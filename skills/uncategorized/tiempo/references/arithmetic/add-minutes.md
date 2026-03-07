# addMinutes

Add minutes to a datetime.

## Signature

```ts
function addMinutes(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  minutes: number
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to add minutes to |
| `minutes` | `number` | Number of minutes to add (can be negative) |

## Returns

A `Temporal.ZonedDateTime` with the minutes added.

## Examples

```ts
import { addMinutes } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');
addMinutes(instant, 45);
// 2025-01-20T12:45:00Z[UTC]
```
