# now

Get the current date and time as a `ZonedDateTime` in the specified timezone.

## Signature

```ts
function now(timezone: Timezone): Temporal.ZonedDateTime

type Timezone = 'UTC' | string;
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `timezone` | `Timezone` | IANA timezone identifier (e.g., "America/New_York", "Europe/London") or "UTC" |

## Returns

A `Temporal.ZonedDateTime` representing the current moment in the specified timezone.

## Examples

### Server-side: Get now in UTC

```ts
import { now } from '@gobrand/tiempo';

const nowUtc = now("UTC");
```

### Server-side: Get now in user's timezone

```ts
import { now } from '@gobrand/tiempo';

// Get timezone from user preferences (stored in DB)
const nowUser = now(user.timezone);
```

### Client-side: Get now in browser's timezone

```ts
import { now, browserTimezone } from '@gobrand/tiempo';

const nowLocal = now(browserTimezone());
```

### Get now in a specific timezone

```ts
import { now } from '@gobrand/tiempo';

const nowInMadrid = now("Europe/Madrid");
const nowInTokyo = now("Asia/Tokyo");
```
