# addSeconds

Add seconds to a datetime.

## Signature

```ts
function addSeconds(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  seconds: number
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to add seconds to |
| `seconds` | `number` | Number of seconds to add (can be negative) |

## Returns

A `Temporal.ZonedDateTime` with the seconds added.

## Examples

```ts
import { addSeconds } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');
addSeconds(instant, 90);
// 2025-01-20T12:01:30Z[UTC]
```
