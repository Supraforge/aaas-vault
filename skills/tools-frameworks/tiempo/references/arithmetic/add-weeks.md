# addWeeks

Add weeks to a datetime.

## Signature

```ts
function addWeeks(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  weeks: number
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to add weeks to |
| `weeks` | `number` | Number of weeks to add (can be negative) |

## Returns

A `Temporal.ZonedDateTime` with the weeks added.

## Examples

```ts
import { addWeeks } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');
addWeeks(instant, 2);
// 2025-02-03T12:00:00Z[UTC]
```
