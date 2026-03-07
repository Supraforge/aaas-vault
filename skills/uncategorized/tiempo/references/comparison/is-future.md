# isFuture

Returns true if the given datetime is in the future (after the current instant).

## Signature

```ts
function isFuture(
  date: Temporal.Instant | Temporal.ZonedDateTime
): boolean
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `date` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to check |

## Returns

`true` if the datetime is in the future, `false` otherwise.

## Examples

```ts
import { isFuture } from '@gobrand/tiempo';

const tomorrow = Temporal.Now.zonedDateTimeISO().add({ days: 1 });
const yesterday = Temporal.Now.zonedDateTimeISO().subtract({ days: 1 });

isFuture(tomorrow);  // true
isFuture(yesterday); // false
```

### With Instant

```ts
const futureInstant = Temporal.Now.instant().add({ hours: 1 });
isFuture(futureInstant); // true
```

### Works with any timezone

```ts
const futureInTokyo = Temporal.ZonedDateTime.from('2100-01-01T00:00:00+09:00[Asia/Tokyo]');
isFuture(futureInTokyo); // true
```

## Common Patterns

### Validate event dates

```ts
import { isFuture } from '@gobrand/tiempo';

function validateEventStart(start: Temporal.ZonedDateTime) {
  if (!isFuture(start)) {
    throw new Error('Event start date must be in the future');
  }
}
```
