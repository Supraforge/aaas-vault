# toIso

Convert a `Temporal.Instant` or `ZonedDateTime` to an ISO 8601 string.

## Signature

```ts
function toIso(input: Temporal.Instant): string

function toIso(
  input: Temporal.ZonedDateTime,
  options?: ToIsoOptions
): string

interface ToIsoOptions {
  mode?: 'utc' | 'offset';
}
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | A Temporal.Instant or Temporal.ZonedDateTime |
| `options.mode` | `'utc' \| 'offset'` | `'utc'` (default) outputs UTC time with Z suffix, `'offset'` outputs local time with offset suffix |

## Returns

An ISO 8601 string representation.

- **UTC mode** (default): `"2025-01-20T20:00:00Z"`
- **Offset mode**: `"2025-01-20T15:00:00-05:00"`

## Examples

### From ZonedDateTime (UTC mode)

```ts
import { toIso } from '@gobrand/tiempo';

const zoned = Temporal.ZonedDateTime.from("2025-01-20T15:00:00-05:00[America/New_York]");

toIso(zoned);
// => "2025-01-20T20:00:00Z"

toIso(zoned, { mode: 'utc' });
// => "2025-01-20T20:00:00Z"
```

### From ZonedDateTime (Offset mode)

```ts
const zoned = Temporal.ZonedDateTime.from("2025-01-20T15:00:00-05:00[America/New_York]");

toIso(zoned, { mode: 'offset' });
// => "2025-01-20T15:00:00-05:00"
```

### From Instant

```ts
const instant = Temporal.Instant.from("2025-01-20T20:00:00Z");
toIso(instant);
// => "2025-01-20T20:00:00Z"
```

### Preserves Precision

Sub-millisecond precision is preserved:

```ts
const zoned = toZonedTime("2025-01-20T20:00:00.123456789Z", "America/New_York");
toIso(zoned);
// => "2025-01-20T20:00:00.123456789Z"
```

## Common Patterns

### API Responses (UTC)

```ts
import { toIso } from '@gobrand/tiempo';

// Return normalized UTC string for APIs
return { scheduledAt: toIso(eventTime) };
```

### User-facing Display (Offset)

```ts
// Show local time with offset for clarity
return { displayTime: toIso(userTime, { mode: 'offset' }) };
```
