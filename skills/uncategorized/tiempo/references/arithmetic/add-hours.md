# addHours

Add hours to a datetime.

## Signature

```ts
function addHours(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  hours: number
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to add hours to |
| `hours` | `number` | Number of hours to add (can be negative) |

## Returns

A `Temporal.ZonedDateTime` with the hours added.

## Examples

```ts
import { addHours } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');
addHours(instant, 3);
// 2025-01-20T15:00:00Z[UTC]

addHours(instant, -5);
// 2025-01-20T07:00:00Z[UTC]
```
