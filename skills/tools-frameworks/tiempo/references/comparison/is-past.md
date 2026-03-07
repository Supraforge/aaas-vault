# isPast

Returns true if the given datetime is in the past (before the current instant).

## Signature

```ts
function isPast(
  date: Temporal.Instant | Temporal.ZonedDateTime
): boolean
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `date` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to check |

## Returns

`true` if the datetime is in the past, `false` otherwise.

## Examples

```ts
import { isPast } from '@gobrand/tiempo';

const yesterday = Temporal.Now.zonedDateTimeISO().subtract({ days: 1 });
const tomorrow = Temporal.Now.zonedDateTimeISO().add({ days: 1 });

isPast(yesterday); // true
isPast(tomorrow);  // false
```

### With Instant

```ts
const pastInstant = Temporal.Now.instant().subtract({ hours: 1 });
isPast(pastInstant); // true
```
